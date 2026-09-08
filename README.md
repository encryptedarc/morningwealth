# Morning Wealth

<p align="center">
  <img src="./assets/morning-wealth-logo.png" alt="Morning Wealth multi-asset investing mark" width="180">
</p>

Morning Wealth is a portable collection of rigorous equity-valuation skills. It is packaged as a Codex marketplace plugin and can also be installed as standalone `SKILL.md` directories in AI environments that support Agent Skills.

The skills are provider-neutral: they do not require a particular model, API key, MCP server, search tool, or operating system. They guide an AI agent to use the research and file-writing capabilities available in its host environment.

## Included skills

| Skill | Use it when | Output |
|---|---|---|
| `valuation-deep-dive` | You need a cited, multi-method equity valuation in the conversation. | Markdown chat |
| `valuation-deep-dive-html-report` | You need the same analysis as a shareable report. | Self-contained HTML |

Both skills classify a business before selecting a valuation method. They cover banks, cyclicals, REITs and infrastructure funds, holding companies, SaaS, asset owners, and deep-value situations. They separate sourced facts from derived valuation outputs and require time-sensitive inputs to be verified in the current session.

## Install with Codex

Clone the repository, then add the repository root as a local marketplace. Use the command for your shell; neither example assumes a fixed drive or username.

```sh
git clone https://github.com/encryptedth/morningwealth.git
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

Then install the `morningwealth` plugin from the marketplace. The marketplace manifest is `.agents/plugins/marketplace.json`, and the plugin source is `plugins/morningwealth`.

## Install with Claude Code

Claude Code discovers project skills in `.claude/skills/`. From the repository root, copy either standalone skill into the target project's `.claude/skills/` directory. See the [Claude Code skills documentation](https://code.claude.com/docs/en/slash-commands) for the current discovery rules.

macOS or Linux:

```sh
mkdir -p /path/to/your-project/.claude/skills
cp -R plugins/morningwealth/skills/valuation-deep-dive /path/to/your-project/.claude/skills/
cp -R plugins/morningwealth/skills/valuation-deep-dive-html-report /path/to/your-project/.claude/skills/
```

Windows PowerShell:

```powershell
$projectPath = (Resolve-Path "..\your-project").Path
New-Item -ItemType Directory -Force "$projectPath\.claude\skills"
Copy-Item -Recurse plugins\morningwealth\skills\valuation-deep-dive "$projectPath\.claude\skills\"
Copy-Item -Recurse plugins\morningwealth\skills\valuation-deep-dive-html-report "$projectPath\.claude\skills\"
```

## Install in another Agent Skills environment

Copy exactly one of these directories into the location required by your AI host:

```text
plugins/morningwealth/skills/valuation-deep-dive/
plugins/morningwealth/skills/valuation-deep-dive-html-report/
```

Each directory is self-contained: it includes its own `SKILL.md`, valuation references, and standard-library Python calculator. The HTML-report edition also includes an offline template. The two skills do not depend on one another.

## HTML reports

The report skill creates `Valuation_<TICKER>_<YYYY-MM-DD>.html`. The template embeds all styling and loads no fonts, scripts, images, stylesheets, or data from the network. When a host cannot write files, the skill returns complete HTML for the user to save manually.

## Verify the calculator

From either skill directory, run:

```sh
python scripts/valuation.py selftest
```

The calculator checks WACC, DCF, reverse DCF, enterprise-value bridges, scenario valuation, justified P/BV, DDM, residual income, NCAV, and normalized-EPS identities.

## License

This repository does not currently include a license. Publishing source code without a license does not automatically grant permission to copy, modify, or redistribute it. Choose and add a license before relying on the repository for open-source reuse.

## Investment disclaimer

This material is for educational purposes only and is not investment advice. Consult a licensed adviser before making investment decisions.
