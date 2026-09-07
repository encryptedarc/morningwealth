# Valuation Skills Marketplace Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a private Codex marketplace plugin containing standalone chat-only and HTML-report equity-valuation skills.

**Architecture:** A single `morningwealth` plugin is registered from the repository marketplace file. It contains two independent skill directories; each owns its references and standard-library calculator. The HTML-report skill additionally owns an inline-CSS report template and never depends on PDF, widgets, MCP, or provider-specific tools.

**Tech Stack:** Markdown, JSON, HTML/CSS, Python 3 standard library, Git, Codex plugin validation tooling.

**Spec:** `docs/superpowers/specs/2026-09-04-valuation-skills-marketplace-design.md`

## Global Constraints

- Keep the Git remote private and do not add a `LICENSE` file.
- Use one marketplace entry named `morningwealth`, sourced from `./plugins/morningwealth`.
- Provide exactly two standalone skills: `valuation-deep-dive` and `valuation-deep-dive-html-report`.
- Both skills must contain their own references and `scripts/valuation.py`.
- Use tool-neutral AI instructions; do not mention `WebSearch`, `web_fetch`, `show_widget`, or project-local Morning Wealth pipelines.
- The report skill emits self-contained HTML only: no PDF, widget, CDN, MCP, app, hook, secret, or credential.
- Do not commit without the user's explicit approval at execution time.

---

## File Structure

- Modify: `README.md` — bilingual repository guide and portability instructions.
- Create: `.agents/plugins/marketplace.json` — one marketplace entry.
- Create: `plugins/morningwealth/.codex-plugin/plugin.json` — Codex plugin manifest.
- Create: `plugins/morningwealth/skills/valuation-deep-dive/SKILL.md` — chat-only routing and delivery contract.
- Create: `plugins/morningwealth/skills/valuation-deep-dive/agents/openai.yaml` — chat skill Thai/English display metadata.
- Create: `plugins/morningwealth/skills/valuation-deep-dive/references/*.md` — independent valuation research and modeling references.
- Create: `plugins/morningwealth/skills/valuation-deep-dive/scripts/valuation.py` — hardened calculator.
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/SKILL.md` — report routing and file-fallback contract.
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/agents/openai.yaml` — report skill Thai/English display metadata.
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/references/*.md` — independent duplicated references.
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/scripts/valuation.py` — byte-identical hardened calculator.
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/assets/report-template.html` — self-contained HTML skeleton.
- Create: `tests/test_valuation_calculators.py` — standard-library tests applied to both calculator copies.
- Create: `tests/test_skill_packages.py` — structural, path-isolation, and template-dependency verification.

## Task 1: Scaffold the marketplace plugin and write its metadata

**Files:**
- Create: `.agents/plugins/marketplace.json`
- Create: `plugins/morningwealth/.codex-plugin/plugin.json`

**Interfaces:**
- Produces marketplace source path `./plugins/morningwealth` consumed by Codex.
- Produces plugin root `plugins/morningwealth` consumed by Tasks 2-5.

- [ ] **Step 1: Add the marketplace contract**

Create `.agents/plugins/marketplace.json` with the required marketplace entry shape:

```json
{
  "name": "personal",
  "interface": { "displayName": "Morning Wealth" },
  "plugins": [
    {
      "name": "morningwealth",
      "source": { "source": "local", "path": "./plugins/morningwealth" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
      "category": "Finance"
    }
  ]
}
```

- [ ] **Step 2: Add the plugin manifest**

Create `plugins/morningwealth/.codex-plugin/plugin.json` with this validation-complete metadata. Do not add `apps`, `mcpServers`, `hooks`, credentials, or a license field.

```json
{
  "name": "morningwealth",
  "version": "1.0.0",
  "description": "Standalone deep-equity-valuation skills for chat analysis and HTML reports.",
  "author": { "name": "Morning Wealth" },
  "repository": "https://github.com/encryptedth/morningwealth",
  "keywords": ["valuation", "equity", "finance", "thai-market"],
  "skills": "./skills/",
  "interface": {
    "displayName": "Morning Wealth",
    "shortDescription": "Deep equity valuation skills",
    "longDescription": "Standalone valuation skills for cited chat analysis and self-contained HTML reports.",
    "developerName": "Morning Wealth",
    "category": "Finance",
    "capabilities": ["Analyze", "Write"],
    "defaultPrompt": [
      "ประเมินมูลค่าหุ้นนี้แบบละเอียด",
      "Create an HTML valuation report for this ticker"
    ]
  }
}
```

- [ ] **Step 3: Validate manifest and marketplace path**

Run:

```powershell
python "C:\Users\ThantapSoommat(Earth\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" "D:\Cowork\Morning Wealth\morningwealth-marketplace\plugins\morningwealth"
python -m json.tool ".agents\plugins\marketplace.json" > $null
```

Expected: plugin validation passes and JSON parsing exits with code 0.

- [ ] **Step 4: Review staged metadata**

Run:

```powershell
git diff --check
git status --short
```

Expected: only the two new metadata files are present at this stage.

## Task 2: Harden and test the calculator before copying it into both skills

**Files:**
- Create: `tests/test_valuation_calculators.py`
- Create: `plugins/morningwealth/skills/valuation-deep-dive/scripts/valuation.py`
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/scripts/valuation.py`

**Interfaces:**
- Consumes: source calculator from `C:\Users\ThantapSoommat(Earth\Encryted\Wealth\Skills\valuation-deep-dive.v2.zip`.
- Produces: `main(argv=None) -> int` and all documented subcommands in both skill directories.

- [ ] **Step 1: Write failing dual-copy regression tests**

Create `tests/test_valuation_calculators.py` using `unittest` and `importlib.util`. Load the two calculator files by absolute path, then test the current identity self-test and new input guards:

```python
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
CALCULATORS = [
    ROOT / "plugins/morningwealth/skills/valuation-deep-dive/scripts/valuation.py",
    ROOT / "plugins/morningwealth/skills/valuation-deep-dive-html-report/scripts/valuation.py",
]

class ValuationCalculatorTests(unittest.TestCase):
    def test_both_calculators_reject_non_positive_exit_multiple(self):
        for path in CALCULATORS:
            spec = importlib.util.spec_from_file_location(path.stem, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            with self.assertRaises(ValueError):
                module.scenario_price(100.0, 0.0, 0.0, 10.0)

    def test_both_calculators_reject_empty_normalized_margin_series(self):
        for path in CALCULATORS:
            spec = importlib.util.spec_from_file_location(path.stem, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            with self.assertRaises(ValueError):
                module.normalized_eps(100.0, [], 10.0)
```

- [ ] **Step 2: Run the tests before implementation**

Run:

```powershell
python -m unittest tests/test_valuation_calculators.py -v
```

Expected: FAIL because the two calculator paths do not exist.

- [ ] **Step 3: Copy the source calculator and implement minimum guards**

Mechanically extract `valuation-deep-dive/scripts/valuation.py` from the source ZIP into both destination paths. Add these guards without changing existing valid-model formulas:

```python
def scenario_price(fwd_metric, exit_multiple, net_cash, shares):
    if exit_multiple <= 0:
        raise ValueError("exit multiple must be positive")
    if shares <= 0:
        raise ValueError("shares must be positive")
    return (fwd_metric * exit_multiple + net_cash) / shares

def normalized_eps(revenue, margins, shares):
    if not margins:
        raise ValueError("at least one through-cycle margin is required")
    if shares <= 0:
        raise ValueError("shares must be positive")
    mid = sum(margins) / len(margins)
    return revenue * mid / shares, mid
```

Update the residual-income docstring and CLI output to call terminal growth an explicit assumption. Do not call the implementation a “fading terminal” and do not imply that `terminal_g` is automatically consistent with retention or payout.

- [ ] **Step 4: Run self-tests and regression tests**

Run:

```powershell
python "plugins/morningwealth/skills/valuation-deep-dive/scripts/valuation.py" selftest
python "plugins/morningwealth/skills/valuation-deep-dive-html-report/scripts/valuation.py" selftest
python -m unittest tests/test_valuation_calculators.py -v
```

Expected: both self-tests print `SELFTEST OK`; both new tests pass.

## Task 3: Build the standalone chat-only skill

**Files:**
- Create: `plugins/morningwealth/skills/valuation-deep-dive/SKILL.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive/agents/openai.yaml`
- Create: `plugins/morningwealth/skills/valuation-deep-dive/references/core-finance-principles.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive/references/archetype-playbooks.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive/references/dcf-and-cost-of-capital.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive/references/peer-calibration.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive/references/thai-market-notes.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive/references/data-sourcing-valuation.md`

**Interfaces:**
- Consumes: the calculator from Task 2 and only files inside this skill directory.
- Produces: a cited Thai Markdown valuation analysis with a fair-value range and mandatory disclaimer.

- [ ] **Step 1: Write a failing chat-package test**

Create `tests/test_skill_packages.py` using `unittest` with this initial content:

```python
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class SkillPackageTests(unittest.TestCase):
    def test_chat_skill_is_self_contained(self):
        root = ROOT / "plugins/morningwealth/skills/valuation-deep-dive"
        self.assertTrue((root / "SKILL.md").is_file())
        self.assertTrue((root / "agents/openai.yaml").is_file())
        self.assertTrue((root / "scripts/valuation.py").is_file())
        self.assertEqual(len(list((root / "references").glob("*.md"))), 6)

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test before adding the chat package**

Run:

```powershell
python -m unittest tests/test_skill_packages.py -v
```

Expected: FAIL because the chat skill directory does not exist yet.

- [ ] **Step 3: Copy source references into the chat skill**

Mechanically extract each listed reference from the ZIP. Preserve financial methodology, but remove the statement that project instructions outrank the standalone reference.

- [ ] **Step 4: Rewrite the router contract and presentation manifest**

Create `SKILL.md` with frontmatter name `valuation-deep-dive` and a tool-neutral description. Replace provider-specific calls with “use an available search/browsing capability.” Retain the archetype gate, sourcing rules, scenario range, and disclaimer. Replace all delivery-track text with a single Markdown-chat output contract.

Create `agents/openai.yaml`:

```yaml
interface:
  display_name: "วิเคราะห์มูลค่าหุ้นเชิงลึก / Deep Equity Valuation"
  short_description: "Cited, multi-method equity valuation in chat"
  default_prompt: "ประเมินมูลค่าหุ้นนี้แบบละเอียด"
policy:
  allow_implicit_invocation: true
```

- [ ] **Step 5: Run the structural test**

Run:

```powershell
python -m unittest tests/test_skill_packages.py -v
```

Expected: PASS after the router and its six references are present.

## Task 4: Build the standalone HTML-report skill and template

**Files:**
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/SKILL.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/agents/openai.yaml`
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/references/core-finance-principles.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/references/archetype-playbooks.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/references/dcf-and-cost-of-capital.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/references/peer-calibration.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/references/thai-market-notes.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/references/data-sourcing-valuation.md`
- Create: `plugins/morningwealth/skills/valuation-deep-dive-html-report/assets/report-template.html`
- Modify: `tests/test_skill_packages.py`

**Interfaces:**
- Consumes: only report-skill-local references, calculator, and HTML template.
- Produces: `Valuation_<TICKER>_<YYYY-MM-DD>.html` or the complete HTML when file writing is unavailable.

- [ ] **Step 1: Write report package checks before its files exist**

Add these checks to `tests/test_skill_packages.py`:

```python
def test_report_skill_is_self_contained_and_template_is_offline():
    root = ROOT / "plugins/morningwealth/skills/valuation-deep-dive-html-report"
    template = root / "assets/report-template.html"
    self.assertTrue((root / "SKILL.md").is_file())
    self.assertTrue((root / "agents/openai.yaml").is_file())
    self.assertTrue((root / "scripts/valuation.py").is_file())
    self.assertEqual(len(list((root / "references").glob("*.md"))), 6)
    content = template.read_text(encoding="utf-8")
    for heading in ("Overview", "Data", "Valuation", "Scenarios", "Risks", "Bottom Line", "Sources"):
        self.assertIn(heading, content)
    self.assertNotIn("http://", content)
    self.assertNotIn("https://", content)
```

- [ ] **Step 2: Run the report package checks**

Run:

```powershell
python -m unittest tests/test_skill_packages.py -v
```

Expected: FAIL because the report skill and template do not exist yet.

- [ ] **Step 3: Copy standalone references and write the report router**

Copy the same cleaned references used by Task 3 into the report skill. Create its `SKILL.md` with name `valuation-deep-dive-html-report`. Require the self-contained HTML file name, its seven sections, inline citations, and explicit fallback to returning HTML content when the host cannot write files. Do not mention PDF, widgets, CDNs, `show_widget`, or the Morning Wealth pipeline. Create `agents/openai.yaml` using `รายงานวิเคราะห์มูลค่าหุ้นเชิงลึก / Deep Equity Valuation Report` as `display_name`, `Create a self-contained HTML valuation report` as `short_description`, and `สร้าง HTML valuation report สำหรับหุ้นนี้` as `default_prompt`.

- [ ] **Step 4: Create an inline-CSS report template**

Create `assets/report-template.html` with UTF-8 metadata, a `<style>` block, neutral light-mode styles, Thai-capable system font fallbacks, and literal section headings required by the test. Use only replaceable content markers such as `{{TITLE}}`, `{{OVERVIEW}}`, `{{SOURCES}}`; do not load fonts, images, scripts, stylesheets, or data from URLs.

- [ ] **Step 5: Run report package checks**

Run:

```powershell
python -m unittest tests/test_skill_packages.py -v
```

Expected: PASS.

## Task 5: Document usage and perform end-to-end verification

**Files:**
- Modify: `README.md`
- Modify: `tests/test_skill_packages.py`

**Interfaces:**
- Consumes: marketplace metadata and both completed skill directories.
- Produces: repository documentation and reproducible validation commands.

- [ ] **Step 1: Replace the initial README with the bilingual guide**

Document the plugin purpose; two-skill comparison table; chat-only and HTML-report examples; calculator self-test; Codex marketplace installation from the repository; generic folder-copy use for other AI systems; no-license/private-repository status; and a statement that the skill provides analysis for education, not investment advice.

- [ ] **Step 2: Add package-isolation assertions**

Extend `tests/test_skill_packages.py` so each skill contains only its required local files and the report template renders all required sections without external URLs. Manually review the two `SKILL.md` files to confirm their instructions are tool-neutral and refer only to their own local paths.

- [ ] **Step 3: Execute the full verification suite**

Run:

```powershell
python -m unittest discover -s tests -v
python "C:\Users\ThantapSoommat(Earth\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" "D:\Cowork\Morning Wealth\morningwealth-marketplace\plugins\morningwealth"
python -m json.tool ".agents\plugins\marketplace.json" > $null
git diff --check
git status --short
```

Expected: all tests, plugin validation, JSON parsing, and whitespace checks pass. The status contains only the marketplace, plugin, two skills, tests, README, and approved design/plan documents.

- [ ] **Step 4: Review the final diff and request commit authorization**

Run:

```powershell
git diff -- README.md .agents/plugins/marketplace.json plugins tests docs
```

Expected: every change implements this plan; no `LICENSE` file appears. Ask the user for explicit authorization before `git add`, `git commit`, and `git push`.

## Spec Coverage Review

- Two independent skills: Tasks 3 and 4.
- One plugin and marketplace entry: Task 1.
- HTML-only report with offline template and fallback: Task 4.
- No license, credentials, PDF, widget, or provider-specific tooling: Tasks 1, 3, 4, and 5.
- Calculator hardening and formula checks: Task 2.
- Bilingual user documentation and reproducible validation: Task 5.
