# Workbook model

## Inputs

Use a single currency and amount scale for the FCFF forecast and balance sheet, and the same scale for diluted shares. USD millions divided by shares in millions gives USD per share. Store rates as decimals. Treat the case forecasts as inputs to this workbook and document the operating assumptions that produced them. If a reviewed forecast already has a formula schedule, preserve that schedule and link its FCFF when the user wants those operating drivers editable.

The bundled authoring script accepts a UTF-8 JSON file with these keys:

| Key | Content |
|---|---|
| `company`, `asOf`, `currency`, `scale` | Company or ticker, ISO date, currency code, and common scale such as `millions` |
| `method` | An object with `discountTiming: "year-end"` and `terminalMethod: "gordon-growth"`. For an export, take these fields from the reviewed model after confirming its conventions. |
| `cash`, `debt`, `minority`, `preferred`, `shares` | Dated equity bridge and diluted share count |
| `cases` | `bear`, `base`, `bull` objects, each with numeric `wacc`, `terminalGrowth` and an ordered numeric `fcff` array. Align the arrays to the same annual horizon. |
| `sensitivity` | Positive `waccStep` and `growthStep`, both decimal rate increments. Choose increments suited to the valuation. |
| `sources` | Array of rows with `input`, `period`, `basis`, `source`, `date`, and `notes`. Include the supporting URL or document reference for sourced figures and the rationale for each material assumption. |

## Formulas

Put the three implied values per share at the top and keep all three live. Use year-end discounting and Gordon growth consistently across the case outputs, reference calculator, and sensitivity grid.

- Discount the forecast cash flows at WACC by periods 1 through N. Excel's `NPV` uses this convention.
- Terminal value is final FCFF × (1 + terminal growth) ÷ (WACC − terminal growth). Discount terminal value by N years at the same WACC and add its present value to the forecast present value to get enterprise value.
- Equity value is enterprise value + cash − debt − minority interest − preferred claims. Divide by positive diluted shares. Apply each bridge item once.
- Use a 5×5 grid centered on the exact Base WACC and terminal growth. Keep Base FCFF and the balance-sheet bridge fixed and recalculate the full formula at each axis intersection. Highlight the center. Leave invalid intersections blank. If WACC is nonpositive, terminal growth is at or below −100%, WACC is at or below terminal growth, or required numeric inputs are missing or invalid, display the case error and leave its outputs blank.
- Use live formulas for results, axis labels, and sensitivity values. Keep editable numbers visually distinct from results. Keep sources and assumption rationales visible on the Sources worksheet.

## Author and verify

In Codex, load the workspace dependencies and use [the workbook builder](../scripts/build-dcf.mjs) with the bundled artifact tool. Run it from a writable working directory where the script can resolve `@oai/artifact-tool`. If needed, copy the script into a temporary directory and link its `node_modules` to the bundled dependency directory. Run `node build-dcf.mjs inputs.json output.xlsx` with an unused output path. If the path already exists, choose a new name. On another host, use its spreadsheet tooling and follow the same workbook contract when the bundled authoring backend is unavailable.

Run the [reference calculator](../scripts/valuation.py) independently for each case. Pass cash minus debt to `--net-cash`, the minority and preferred claims separately, and shares on the same scale as the cash flows. A synthetic parity example:

```sh
python valuation.py dcf --flows 100,100 --wacc 0.10 --terminal-g 0 --net-cash 30 --minority 12 --preferred 8 --shares 10
```

The synthetic case gives enterprise value 1,000 and value per share 101.00. Changing the final-year FCFF to 110 gives 110.09 per share. Restore the original assumptions after checking recalculation. Check the recalculated workbook for formula errors, verify the center of the sensitivity table, and confirm labels and units before delivery.
