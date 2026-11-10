import { constants } from "node:fs";
import { copyFile, mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const [inputPath, outputPath] = process.argv.slice(2);
if (!inputPath || !outputPath?.toLowerCase().endsWith(".xlsx")) {
  throw new Error("Usage: node build-dcf.mjs inputs.json output.xlsx");
}

const input = JSON.parse(await readFile(inputPath, "utf8"));
if (input.method?.discountTiming !== "year-end" || input.method?.terminalMethod !== "gordon-growth") {
  throw new Error("Confirm year-end discounting and Gordon growth before exporting this DCF.");
}
const caseNames = ["bear", "base", "bull"];
const bridgeKeys = ["cash", "debt", "minority", "preferred", "shares"];
const sourceKeys = ["input", "period", "basis", "source", "date", "notes"];
const years = input.cases?.base?.fcff?.length;
const hasText = (value) => typeof value === "string" && value.trim().length > 0;

if (!["company", "asOf", "currency", "scale"].every((key) => hasText(input[key]))) {
  throw new Error("Supply a company, as-of date, currency and scale.");
}
if (!bridgeKeys.every((key) => Number.isFinite(input[key]) && input[key] >= 0) || input.shares <= 0) {
  throw new Error("Supply nonnegative bridge inputs and a positive diluted share count.");
}
for (const name of caseNames) {
  const scenario = input.cases?.[name];
  if (!scenario || !Array.isArray(scenario.fcff) || !years || scenario.fcff.length !== years
      || !scenario.fcff.every(Number.isFinite) || !Number.isFinite(scenario.wacc)
      || !Number.isFinite(scenario.terminalGrowth) || scenario.wacc <= 0
      || scenario.terminalGrowth <= -1 || scenario.wacc <= scenario.terminalGrowth) {
    throw new Error(`Invalid ${name} case. Supply aligned annual FCFF, positive WACC and valid terminal growth.`);
  }
}
const { waccStep, growthStep } = input.sensitivity ?? {};
if (![waccStep, growthStep].every((step) => Number.isFinite(step) && step > 0)) {
  throw new Error("Supply positive sensitivity steps for WACC and terminal growth.");
}
if (!Array.isArray(input.sources) || !input.sources.length
    || !input.sources.every((row) => row && sourceKeys.every((key) => typeof row[key] === "string")
      && hasText(row.input) && hasText(row.basis) && (hasText(row.source) || hasText(row.notes)))) {
  throw new Error("Supply sources and assumption rationales using the documented source fields.");
}

const workbook = Workbook.create();
const sheet = workbook.worksheets.add("DCF");
const sources = workbook.worksheets.add("Sources");
const first = 17;
const last = first + years - 1;
const forecastPV = last + 2;
const terminal = forecastPV + 1;
const terminalPV = terminal + 1;
const enterprise = terminalPV + 1;
const equity = enterprise + 1;
const sensitivity = equity + 3;
const numberFormat = "#,##0.00;(#,##0.00);0.00";
const textValue = (value) => value.startsWith("=") ? "'" + value : value;
const value = (cell, data) => {
  sheet.getRange(cell).values = [[typeof data === "string" ? textValue(data) : data]];
};
const formula = (cell, expression) => {
  sheet.getRange(cell).formulas = [[expression]];
};
const header = (range) => {
  range.format.fill = "#243854";
  range.format.font.color = "#FFFFFF";
  range.format.font.bold = true;
};
const editable = (address) => {
  const range = sheet.getRange(address);
  range.format.fill = "#FFF1CB";
  range.format.font.color = "#1647A5";
};

value("A1", `DCF | ${input.company}`);
value("A2", `${input.asOf} | ${input.currency}, ${input.scale} | Year-end discounting`);
sheet.getRange("A4:D4").values = [["Scenario", "Bear", "Base", "Bull"]];
value("A5", `Value per share (${input.currency})`);
value("A6", "Input check");
sheet.getRange("A8:A14").values = [
  ["WACC"], ["Terminal growth"], ["Cash"], ["Debt"], ["Minority interest"], ["Preferred claims"], ["Diluted shares"],
];
sheet.getRange("B10:B14").values = bridgeKeys.map((key) => [input[key]]);
sheet.getRange("A16:D16").values = [["Year", "Bear FCFF", "Base FCFF", "Bull FCFF"]];
sheet.getRange(`A${first}:D${last}`).values = Array.from({ length: years }, (_, index) => [
  index + 1, ...caseNames.map((name) => input.cases[name].fcff[index]),
]);
sheet.getRange(`A${forecastPV}:A${equity}`).values = [
  ["PV of forecast FCFF"], ["Terminal value"], ["PV of terminal value"], ["Enterprise value"], ["Equity value"],
];

for (const [index, column] of ["B", "C", "D"].entries()) {
  const { wacc, terminalGrowth } = input.cases[caseNames[index]];
  const rate = `${column}8`;
  const growth = `${column}9`;
  const flows = `${column}${first}:${column}${last}`;
  value(rate, wacc);
  value(growth, terminalGrowth);
  const invalid = `OR(${rate}<=0,${growth}<=-1,${rate}<=${growth},MIN($B$10:$B$13)<0,$B$14<=0)`;
  formula(`${column}6`, `=IF(COUNT(${flows},${rate}:${growth},$B$10:$B$14)<>${years + 7},"Missing numeric input",IF(${invalid},"Check rate or bridge","OK"))`);
  const outputs = [
    [forecastPV, `NPV(${rate},${flows})`],
    [terminal, `${column}${last}*(1+${growth})/(${rate}-${growth})`],
    [terminalPV, `${column}${terminal}/(1+${rate})^${years}`],
    [enterprise, `${column}${forecastPV}+${column}${terminalPV}`],
    [equity, `${column}${enterprise}+$B$10-$B$11-$B$12-$B$13`],
    [5, `${column}${equity}/$B$14`],
  ];
  for (const [row, expression] of outputs) {
    formula(`${column}${row}`, `=IF(${column}6="OK",${expression},"")`);
  }
}

value(`A${sensitivity}`, "Base sensitivity | WACC by terminal growth");
value(`A${sensitivity + 1}`, "WACC step");
value(`B${sensitivity + 1}`, waccStep);
value(`A${sensitivity + 2}`, "Terminal growth step");
value(`B${sensitivity + 2}`, growthStep);
const axis = sensitivity + 4;
const sensitivityColumns = ["B", "C", "D", "E", "F"];
const axisValue = (base, step, offset) =>
  `=IF(AND(ISNUMBER(${base}),ISNUMBER(${step}),${step}>0),${base}+(${offset})*${step},"")`;
value(`A${axis}`, "WACC / Growth");
for (const [index, column] of sensitivityColumns.entries()) {
  formula(`${column}${axis}`, axisValue("$C$9", `$B$${sensitivity + 2}`, index - 2));
}
for (let index = 0; index < 5; index++) {
  const row = axis + index + 1;
  const rate = `$A${row}`;
  formula(`A${row}`, axisValue("$C$8", `$B$${sensitivity + 1}`, index - 2));
  for (const column of sensitivityColumns) {
    const growth = `${column}$${axis}`;
    const valid = `AND($C$6="OK",ISNUMBER(${rate}),ISNUMBER(${growth}),${rate}>0,${growth}>-1,${rate}>${growth})`;
    const ev = `NPV(${rate},$C$${first}:$C$${last})+$C$${last}*(1+${growth})/(${rate}-${growth})/(1+${rate})^${years}`;
    formula(`${column}${row}`, `=IF(${valid},(${ev}+$B$10-$B$11-$B$12-$B$13)/$B$14,"")`);
  }
}

for (const tab of [sheet, sources]) tab.showGridLines = false;
for (const address of ["A4:D4", "A16:D16", `A${axis}:F${axis}`]) header(sheet.getRange(address));
sheet.getRange("A:A").format.columnWidth = 41;
sheet.getRange("B:F").format.columnWidth = 23;
sheet.getRange("A1").format.font.bold = true;
sheet.getRange("A1").format.font.size = 14;
sheet.getRange("A5:D5").format.fill = "#DCE9F5";
sheet.getRange("A5:D5").format.font.bold = true;
sheet.getRange(`D${axis + 3}`).format.fill = "#DCE9F5";
const stepCells = `B${sensitivity + 1}:B${sensitivity + 2}`;
for (const address of ["B8:D9", "B10:B14", `B${first}:D${last}`, stepCells]) editable(address);
for (const address of ["B8:D9", `B${axis}:F${axis}`, `A${axis + 1}:A${axis + 5}`, stepCells]) {
  sheet.getRange(address).setNumberFormat("0.00%");
}
for (const address of ["B5:D5", "B10:B14", `B${first}:D${last}`, `B${forecastPV}:D${equity}`, `B${axis + 1}:F${axis + 5}`]) {
  sheet.getRange(address).setNumberFormat(numberFormat);
}

sources.getRange("A1:F1").values = [["Input", "Period", "Basis", "Source", "Source date", "Notes"]];
const sourceTable = sources.getRange(`A2:F${input.sources.length + 1}`);
sourceTable.values = input.sources.map((row) => sourceKeys.map((key) => textValue(row[key])));
header(sources.getRange("A1:F1"));
sources.getRange("A:C").format.columnWidth = 23;
sources.getRange("D:D").format.columnWidth = 42;
sources.getRange("E:E").format.columnWidth = 15;
sources.getRange("F:F").format.columnWidth = 52;
sourceTable.format.wrapText = true;
sourceTable.format.autofitRows();

workbook.recalculate();
const result = await SpreadsheetFile.exportXlsx(workbook);
const tempRoot = resolve(tmpdir());
const stagingDir = await mkdtemp(join(tempRoot, "encryptedarc-dcf-"));
if (dirname(resolve(stagingDir)) !== tempRoot) {
  throw new Error("Unexpected workbook staging directory.");
}
try {
  const stagedPath = join(stagingDir, "workbook.xlsx");
  await result.save(stagedPath);
  await copyFile(stagedPath, outputPath, constants.COPYFILE_EXCL);
} catch (error) {
  if (error.code === "EEXIST") {
    throw new Error("Output file already exists. Choose a new .xlsx path.", { cause: error });
  }
  throw error;
} finally {
  await rm(stagingDir, { recursive: true, force: true });
}
