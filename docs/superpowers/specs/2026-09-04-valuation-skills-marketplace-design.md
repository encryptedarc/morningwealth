# Morning Wealth valuation skills marketplace design

## Goal

Package the supplied `valuation-deep-dive.v2.zip` as one Codex marketplace plugin in the private `encryptedth/morningwealth` repository. The plugin must expose two independently portable skills:

- `valuation-deep-dive` — chat-only equity valuation.
- `valuation-deep-dive-html-report` — equity valuation that creates a self-contained HTML report.

Each skill must be usable after copying only that skill directory into another compatible AI environment. Neither skill may depend on the other at runtime.

## Repository layout

```text
.agents/plugins/marketplace.json
plugins/morningwealth/
  .codex-plugin/plugin.json
  skills/
    valuation-deep-dive/
      SKILL.md
      agents/openai.yaml
      references/
      scripts/valuation.py
    valuation-deep-dive-html-report/
      SKILL.md
      agents/openai.yaml
      references/
      scripts/valuation.py
      assets/report-template.html
README.md
```

`marketplace.json` has one `morningwealth` plugin entry whose source is `./plugins/morningwealth`. Its internal marketplace name is the Codex default `personal`; `interface.displayName` is `Morning Wealth`. The plugin manifest contains no MCP server, app, hook, secret, credential, or external runtime dependency.
Each skill has an `agents/openai.yaml` presentation manifest with its approved Thai/English display name; it contains only presentation metadata and an implicit-invocation policy.

## Skill boundaries

### valuation-deep-dive

This is the chat-only skill. It retains the valuation archetype routing, source discipline, scenario requirements, financial references, and calculator. Its delivery contract is Markdown only; it must not claim widget, PDF, or file-output support.

### valuation-deep-dive-html-report

This is the HTML-report skill. It contains the same references and calculator so it remains standalone. Its delivery contract is a file named `Valuation_<TICKER>_<YYYY-MM-DD>.html` using a bundled template with inline CSS and no external assets. If the host cannot create files, it must return the complete HTML content and state that the user must save it.

The report must include Overview, Data, Valuation, Scenarios, Risks, Bottom Line, and Sources. PDF rendering and interactive widgets are deliberately out of scope.

## Portability and source changes

Both skills use capability-neutral language such as “use an available search/browsing capability” instead of provider-specific tool names. They do not refer to Morning Wealth project instructions, a project-local report pipeline, or unavailable assets.

The original `Personal use — Earth Encrypt / Buzzebees` frontmatter license is removed. No `LICENSE` file is added. The private repository therefore remains under the owner's default copyright.

The two skills preserve source discipline: current market data must be researched in the current session, material outliers require cross-verification, and derived valuation values remain clearly distinct from sourced inputs.

## Calculator hardening

The duplicated `valuation.py` remains standard-library Python. It will be updated to reject invalid scenario exit multiples and empty normalized-margin input. The residual-income terminal treatment will explicitly identify terminal growth as an assumption, rather than claiming an implicit fade or a payout-consistent terminal state it does not model.

## Documentation

The existing root README is expanded in Thai and English. It explains the difference between the two skills, their files, the Python self-test, Codex marketplace installation, and generic folder-copy use in other AI environments. It does not promise a provider-specific import mechanism that may not exist.

## Verification

Before the implementation is handed over:

1. Validate the plugin manifest and marketplace entry with the plugin validation tooling.
2. Run `valuation.py selftest` for both skills.
3. Execute a representative valid invocation for every calculator command in both copies.
4. Assert that each skill's referenced files are inside its own directory.
5. Check the HTML template for external URL dependencies and verify its required sections.
6. Inspect `git diff` to ensure the initial README is expanded rather than unrelated files changed.

## Non-goals

- PDF generation, browser widgets, MCP servers, hooks, apps, APIs, and credentials.
- Live financial analysis or investment recommendations.
- Publishing the repository publicly or adding an open-source license.
