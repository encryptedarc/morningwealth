# Encrypted Arc

<p align="center">
  <img src="./assets/encryptedarc-logo.png" alt="Encrypted Arc multi-asset investing mark" width="180">
</p>

Encrypted Arc is a portable collection of rigorous fundamental-analysis and equity-valuation skills. It is packaged as a Codex marketplace plugin and can also be installed as standalone `SKILL.md` directories in AI environments that support Agent Skills.

The skills are provider-neutral: they do not require a particular model, API key, MCP server, search tool, or operating system. They guide an AI agent to use the research and file-writing capabilities available in its host environment.

## Included skills

| Skill | Use it when | Output |
|---|---|---|
| `fundamental` | You need a beginner-friendly, filing-first review of business quality and financial health in clear English. | Markdown chat |
| `valuation-deep-dive` | You need a cited, multi-method equity valuation in the conversation. | Markdown chat |
| `valuation-deep-dive-html-report` | You need the same analysis as a shareable report. | Self-contained HTML |

The `fundamental` skill explains in clear English how a company makes money, selects financial metrics that fit its business model, checks earnings quality and capital allocation, and separates business quality from share-price attractiveness.

The valuation skills classify a business before selecting a valuation method. They cover banks, cyclicals, REITs and infrastructure funds, holding companies, SaaS, asset owners, and deep-value situations. They separate sourced facts from derived valuation outputs and require time-sensitive inputs to be verified in the current session.

## Analysis workflow

The valuation skills use the same gated workflow:

1. **Research** — gather the current market data, latest filing, capital structure, discount-rate inputs, and business-model-specific evidence.
2. **Validate inputs** — verify timestamps, source quality, share-count type, units, accounting basis, and required cash-flow components before valuation begins.
3. **Calculate** — run multi-step valuation arithmetic through the bundled calculator and retain its printed input block.
4. **Semantic audit** — confirm that labels match the economic quantity, comparisons use the same metric and period, and narrative conclusions are supported by one-variable-at-a-time sensitivity checks.
5. **Render** — produce the Markdown or HTML report only after the input gate and semantic audit pass.

A stale or unresolved material input is a stop condition, not a footnote. When a dependent valuation cannot be supported, the skill reports what is missing and how to verify it instead of publishing a fair-value center with a warning attached.

## Plain-language reports

The `fundamental` skill defaults to clear English even when the request is written in another language. Valuation reports follow the user's language and explain specialist terminology where it first appears. An abbreviation is introduced only when it will recur, and a translated term must also explain what the measure means and why it matters to the valuation.

For example, a Thai valuation report should not leave phrases such as `diluted shares`, `discount-rate story`, `LSEG via CNBC`, or `reverse DCF` unexplained. It should instead describe the economic meaning in Thai, identify who compiled and who published a sourced estimate, and then place the English term or abbreviation in parentheses when useful. Valuation table and section headings follow the user's language as well.

## Install with Codex

Clone the repository, then add the repository root as a local marketplace. Use the command for your shell; neither example assumes a fixed drive or username.

```sh
git clone https://github.com/encryptedarc/morningwealth.git
cd morningwealth
```

macOS or Linux:

```sh
codex plugin marketplace add "$(pwd)"
```

Windows PowerShell:

```powershell
codex plugin marketplace add (Get-Location).Path
```

Then install the `encryptedarc` plugin from the marketplace. The marketplace manifest is `.agents/plugins/marketplace.json`, and the plugin source is `plugins/encryptedarc`.

## Install with Claude Code

Claude Code discovers project skills in `.claude/skills/`. From the repository root, copy any standalone skill into the target project's `.claude/skills/` directory. See the [Claude Code skills documentation](https://code.claude.com/docs/en/slash-commands) for the current discovery rules.

macOS or Linux:

```sh
mkdir -p /path/to/your-project/.claude/skills
cp -R plugins/encryptedarc/skills/fundamental /path/to/your-project/.claude/skills/
cp -R plugins/encryptedarc/skills/valuation-deep-dive /path/to/your-project/.claude/skills/
cp -R plugins/encryptedarc/skills/valuation-deep-dive-html-report /path/to/your-project/.claude/skills/
```

Windows PowerShell:

```powershell
$projectPath = (Resolve-Path "..\your-project").Path
New-Item -ItemType Directory -Force "$projectPath\.claude\skills"
Copy-Item -Recurse plugins\encryptedarc\skills\fundamental "$projectPath\.claude\skills\"
Copy-Item -Recurse plugins\encryptedarc\skills\valuation-deep-dive "$projectPath\.claude\skills\"
Copy-Item -Recurse plugins\encryptedarc\skills\valuation-deep-dive-html-report "$projectPath\.claude\skills\"
```

## Install in another Agent Skills environment

Copy any of these directories into the location required by your AI host:

```text
plugins/encryptedarc/skills/fundamental/
plugins/encryptedarc/skills/valuation-deep-dive/
plugins/encryptedarc/skills/valuation-deep-dive-html-report/
```

Each directory is self-contained. `fundamental` includes its own analysis framework and source policy. Each valuation skill includes its own references and standard-library Python calculator, while the HTML-report edition also includes an offline template.

## HTML reports

The report skill creates `Valuation_<TICKER>_<YYYY-MM-DD>.html`. The template localizes its section headings and as-of label to the user's language, embeds all styling, and loads no fonts, scripts, images, stylesheets, or data from the network. When a host cannot write files, the skill returns complete HTML for the user to save manually.

## Verify the calculator

From either valuation skill directory, run:

```sh
python scripts/valuation.py selftest
```

The calculator checks WACC, DCF, reverse DCF, enterprise-value bridges, scenario valuation, justified P/BV, DDM, residual income, NCAV, and normalized-EPS identities.

## License

This repository does not currently include a license. Publishing source code without a license does not automatically grant permission to copy, modify, or redistribute it. Choose and add a license before relying on the repository for open-source reuse.

## Investment disclaimer

This material is for educational purposes only and is not investment advice. Consult a licensed adviser before making investment decisions.
