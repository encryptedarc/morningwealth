# Morning Wealth

Private Codex marketplace plugin for rigorous, source-disciplined equity valuation across Thai, US, and global markets.

## Skills

| Skill | Display name | Use it when | Output |
|---|---|---|---|
| `valuation-deep-dive` | วิเคราะห์มูลค่าหุ้นเชิงลึก / Deep Equity Valuation | You need a cited, multi-method valuation in the conversation. | Markdown chat |
| `valuation-deep-dive-html-report` | รายงานวิเคราะห์มูลค่าหุ้นเชิงลึก / Deep Equity Valuation Report | You need the same analysis saved as a shareable report. | Self-contained HTML |

Both skills classify the business before choosing a valuation method. They cover banks, cyclicals, REITs and infrastructure funds, holding companies, SaaS, asset owners, and deep value. They require live inputs to be sourced during the current session and distinguish sourced facts from derived valuation outputs.

## Codex installation

1. Clone this private repository locally.
2. Add the repository-root marketplace to Codex:

   ```powershell
   codex plugin marketplace add "C:\path\to\morningwealth"
   ```

3. Install the `morningwealth` plugin from that marketplace.

The marketplace file is `.agents/plugins/marketplace.json`, and the plugin source is `plugins/morningwealth`.

## Using another AI environment

Each skill is standalone. Copy exactly one of these folders into the target AI environment and follow that environment's skill-import documentation:

```text
plugins/morningwealth/skills/valuation-deep-dive/
plugins/morningwealth/skills/valuation-deep-dive-html-report/
```

Each folder includes its own `SKILL.md`, references, and Python calculator. The HTML-report skill also includes its own offline template. Neither requires the other skill, an API key, an MCP server, or a provider-specific search tool.

## HTML reports

The report skill creates a file named `Valuation_<TICKER>_<YYYY-MM-DD>.html`. Its template embeds all CSS and does not load fonts, scripts, images, stylesheets, or data from the network. If the AI host cannot write files, the skill returns complete HTML for you to save manually.

## Calculator check

Both skill directories contain the same standard-library Python calculator. From either skill directory, run:

```powershell
python scripts/valuation.py selftest
```

The calculator validates WACC, DCF, reverse DCF, enterprise-value bridges, scenario valuation, justified P/BV, DDM, residual income, NCAV, and normalized EPS identities.

## Repository policy

This repository is private and deliberately contains no `LICENSE` file. Do not redistribute its contents unless the copyright owner grants permission.

ข้อมูลนี้เพื่อการศึกษา ไม่ใช่คำแนะนำการลงทุน — กรุณาปรึกษา licensed advisor ก่อนตัดสินใจ
