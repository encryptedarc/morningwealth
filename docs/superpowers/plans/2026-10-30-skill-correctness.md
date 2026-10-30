# Skill Correctness Implementation Plan

> Execute inline using test-driven-development, writing-skills, and verification-before-completion. The user approved the review fixes and four improvement areas in chat. The initial implementation was review-only; the user subsequently authorized commit, push, and a new release.

**Goal:** Correct calculator errors and conflicting skill instructions, shorten default earnings answers, and verify standalone packages and realistic consumer behavior.

**Architecture:** Retain all four standalone skill directories and the duplicated valuation resources. Apply equivalent fixes to both calculator copies and enforce parity in tests. No shared runtime or generation pipeline.

**Tech Stack:** Markdown skills, JSON manifests, standard-library Python calculators and unittest.

**Spec:** The 2026-10-30 review and the user's approval in this chat.

## Global Constraints

- Work in `C:/git/morningwealth` on the existing `feature/earnings-skill` branch.
- Preserve existing CLI calls: omitted residual-income terminal growth still means no terminal; explicitly supplied zero means a flat perpetuity.
- Keep tests deterministic and financial inputs synthetic; do not fetch live market data for fixtures.
- Keep source hierarchy and no-recommendation boundaries intact.
- Agent exercises test consumer behavior; do not substitute assertions on instruction wording.

## Review Focus

- Historical requested periods and comparative filings remain usable, with same-period restatements preferred.
- Q4 subtraction applies to additive flows, never EPS, ratios, share averages, or balance-sheet stocks; loss-period dilution needs the issuer's quarter denominator.
- Financial institutions use suitable inputs and valuation cross-checks without being blocked by missing corporate FCF.
- Terminal growth omitted, explicitly zero, positive, negative, and at/above COE have distinct, documented behavior.
- Common-equity DCF deducts minority and preferred claims once, while preserving old calls without those claims.

## Task 1 — Calculator regression fixes

**Modify:**
- `C:/git/morningwealth/tests/test_valuation_calculators.py`
- `C:/git/morningwealth/plugins/encryptedarc/skills/valuation-deep-dive/scripts/valuation.py`
- `C:/git/morningwealth/plugins/encryptedarc/skills/valuation-deep-dive-html-report/scripts/valuation.py`

- [x] Add tests for flat terminal RI, default finite forecast, nonzero terminal growth and COE boundary.
- [x] Add CLI tests that deduct minority/preferred claims, echo them, and preserve calls omitting them.
- [x] Observe relevant tests fail on the original calculators, then implement minimal fixes in both copies.
- [x] Run the calculator tests and both selftests.

## Task 2 — Skill behavior and routing

**Modify:** earnings entrypoint/framework/source policy; fundamental source policy; both valuation entrypoints and their peer-calibration and DCF references, all under `C:/git/morningwealth/plugins/encryptedarc/skills/`.

**Create:** `C:/git/morningwealth/tests/skill_evaluation.md`.

- [x] Exercise the original earnings instructions and routing descriptions with fresh agents before editing; keep outputs outside the repo.
- [x] Restrict Q4 subtraction, clarify historical/restated evidence, and support supplied financial documents as session evidence.
- [x] Use a compact earnings answer by default, with the full framework as the research checklist and detailed format on request.
- [x] Make model input gates and cross-checks conditional on the selected archetype.
- [x] Reserve HTML discovery for explicit file/report-format requests; preserve chat as the default valuation output.
- [x] Remove the nonportable earnings frontmatter hint; retain argument syntax in the body.
- [x] Repeat the consumer exercises with fresh agents against the revised skills and record outcomes.

## Task 3 — Package verification and handoff

**Modify:** `C:/git/morningwealth/tests/test_skill_packages.py`, `C:/git/morningwealth/README.md`.

- [x] Validate JSON manifest resolution, bundled references, and calculator/reference parity without adding dependencies.
- [x] Document full verification command, earnings answer shape, and terminal-growth/DCF claim semantics.
- [x] Run the whole unittest suite, both selftests, skill validation, and syntax compilation without bytecode files.
- [x] Obtain a fresh review, address material findings, and inspect `git diff --check` and working-tree scope.

## Execution Record

- Initial state: clean worktree at `dbb5eef`.
- Implementation decision: use `None` for an omitted RI terminal assumption; preserve existing finite-horizon calls and make explicit zero an actual growth assumption.
- Calculator RED: original implementations produced eight failing subtests across the two copies, including missing DCF claim flags, flat terminal RI, and the zero-growth COE boundary. Fixed a Windows test-process encoding mismatch before recording the reproducible RED result.
- Calculator GREEN: nine calculator tests and both selftests passed after the fixes; the full suite subsequently passed 19 tests.
- Skill RED: baseline consumer rejected historical filings solely because newer periods existed; metadata consumer could not resolve fair-value/bare-ticker output format.
- Skill GREEN: fresh consumers completed historical Q4 with correct EPS and chose the intended skill for all eight routing cases. The loss-quarter consumer used amended income and withheld unsupported diluted EPS. The bank consumer selected suitable models, ran calculators without corporate FCF, and disclosed missing credit evidence.
- Full verification: 20 unittest tests passed, both calculator selftests passed, all four skills passed quick_validate, and all Python files compiled without emitting bytecode.
- Final fresh read-only review: no actionable material findings; reviewer independently ran all 20 tests successfully. Company-specific reasonableness of retention/terminal assumptions remains an analysis-time judgment, explicitly disclosed in the skill references.
- Initial implementation handoff: all planned changes implemented; no branch switch, commit, push, installation, or publication had been performed.

## Release follow-up

- User authorization: push the completed work and publish a new release.
- Version: `1.2.1`, a patch after the `1.2.0` earnings addition already merged through PR #9.
- Release sequence: rerun checks, commit fixes and version bump separately, push the existing feature branch, merge through a PR into main, then publish tag/release `v1.2.1` at the verified main revision.
- Compatibility note: omitting RI terminal growth preserves the finite forecast; explicitly passing zero now selects a flat perpetuity.
