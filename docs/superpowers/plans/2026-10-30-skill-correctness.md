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

## Source reliability follow-up

User requested verification that researched information comes from trustworthy sources. Review found search results classified as primary evidence in valuation and inconsistent source tiers for filings. A baseline valuation consumer accepted snippet-only revenue under those instructions; the statement-policy consumer rejected it.

**Modify in place:**
- `C:/git/morningwealth/plugins/encryptedarc/skills/earnings/references/source-policy.md`
- `C:/git/morningwealth/plugins/encryptedarc/skills/fundamental/references/source-policy.md`
- `C:/git/morningwealth/plugins/encryptedarc/skills/valuation-deep-dive/references/core-finance-principles.md`
- `C:/git/morningwealth/plugins/encryptedarc/skills/valuation-deep-dive-html-report/references/core-finance-principles.md`
- `C:/git/morningwealth/plugins/encryptedarc/skills/valuation-deep-dive/references/data-sourcing-valuation.md`
- `C:/git/morningwealth/plugins/encryptedarc/skills/valuation-deep-dive-html-report/references/data-sourcing-valuation.md`
- `C:/git/morningwealth/tests/skill_evaluation.md`
- `C:/git/morningwealth/README.md`

**Acceptance:** search locates evidence but is not evidence; use original filings/data owners for relevant facts, attribute company claims, inspect article provenance rather than trust a host name, count common-origin republications once, reject uncorroborated promotion, link the exact supporting document, and label unverified supplied inputs as conditional.

**Verification:** fresh consumer exercises before/after policy changes, full existing suite, skill validation, and hash parity after syncing the changed references to both global skill roots. Preserve local extensions and back up overwritten references. These are local source-policy updates after v1.2.1; do not silently alter the published tag or claim the changed copies remain byte-identical to that release.

**Result:** revised valuation and earnings consumers passed the source-provenance scenarios; a fresh read-only reviewer found no material inconsistencies across the four skills. The full 20-test suite and repository skill validators passed. Six changed references were backed up and synced to each global skills root with matching hashes; Claude's local earnings extension was preserved. Global backups are under each host's `skill-backups/morningwealth-source-policy-20261030T035004Z`. No commit, push, tag change, or new release was performed for this follow-up.

## Source reliability release — v1.2.2

- The user subsequently authorized publishing a new version and installing it locally.
- Rerun checks, commit source-policy changes and the version bump, push the existing feature branch, merge through a PR, and publish `v1.2.2` at the verified main revision.
- Install all four standalone skills from the published tag into both global `.codex/skills` and `.claude/skills` roots using the skill-installer helper. Back up current copies, preserve local extensions, and verify release/installation byte parity plus package validation.
- The prior v1.2.1 tag remains unchanged; v1.2.2 replaces the temporary local source-policy patch with an identifiable published release.

## Company-first discovery and citation follow-up

The user requested company originals as the first source, citing the same Amazon earnings release on its IR site and as SEC Exhibit 99.1. Apply the same behavior to all four skills and both installed global copies.

- Discover company financial reports, releases, presentations, and calls on the verified company IR site first. Use regulator/exchange records to check provenance, period/version, and material figures, and inspect reputable independent reporting where available.
- When the same document/version is accessible at IR and a regulator, cite IR as the main source and label the regulator copy as document/provenance verification. The copies remain one issuer origin.
- Host preference does not outrank document authority: use the latest applicable amended/restated statements and full filed financial statements for accounting details over a conflicting preliminary release, regardless of host. Preserve audit/review status and independent verification requirements for external claims and quote outliers.
- If IR is blocked or incomplete, use the inspected regulator copy and disclose the fallback. If other verification is unavailable, record attempts and limits; do not invent confirmation or block otherwise usable attributed issuer results solely for lack of news coverage.
- Update the earnings/fundamental entrypoints, earnings document-discovery framework, both statement source policies, both valuation entrypoints and their core/input references, plus README and consumer scenarios. Keep each standalone package self-contained.
- Verify through baseline/revised fresh consumer cases (identical mirrors, later amendment, blocked IR, release-only availability), existing tests, skill validators, and global file parity; preserve personal local extensions.
- This follow-up does not authorize a new publication by itself; leave published v1.2.2 untouched unless a new release is requested.
- Consumer results: the released-policy baseline cited SEC first for an identical release; fresh revised statement and valuation consumers selected IR first while preserving amendment authority, blocked-IR fallback, release-only usability, independent-origin counting, and originating market/macro sources. Existing 20 tests and all four repository validators passed.
- Final review: fresh read-only reviewer found no material issues across all four entrypoints and their references. Eleven changed skill files were backed up and synced to both global roots under `skill-backups/morningwealth-company-first-20261030T045233Z`, with local extensions preserved. This remains an uncommitted local update after published v1.2.2.

## Structured earnings records and reusable content

The user approved adapting the detailed earnings-post critique, explicitly requesting clear headings/bullets and individually reusable information for future infographics.

**Files:** modify `C:/git/morningwealth/plugins/encryptedarc/skills/earnings/SKILL.md`, its `references/earnings-framework.md`, `C:/git/morningwealth/tests/test_skill_packages.py`, `C:/git/morningwealth/tests/skill_evaluation.md`, and `C:/git/morningwealth/README.md`; create `C:/git/morningwealth/plugins/encryptedarc/skills/earnings/references/quarter-record.md` after confirming no existing record reference.

**Behavior:**
- Default to a complete structured review with a short lead summary, clear localized Markdown headings and atomic bullets; explicit brief requests may condense chat.
- Preserve material guidance and management Q&A in self-contained topic blocks carrying period, unit/basis, statement type, source and qualifiers for later visual reuse. Do not generate an infographic unless requested.
- Load an available previous-quarter record, verify new financial facts against primary sources, and compare original as-issued guidance and revisions with like-for-like actuals. Retain original versions and distinguish targets not yet due or lacking comparable actuals.
- Build an archive-ready quarter record. Save it when the user, applicable instructions, or local extension configure an authorized destination; otherwise return the structured Markdown and disclose that persistence/baseline is unavailable. Do not invent a path or write inside the installed skill.
- Preserve raw prior records; create a new dated revision rather than overwrite an existing record. Existing personal extensions and company-first source rules remain intact.

**Verification:** baseline and revised offline consumer scenarios for prior guidance versions, long-term targets, derived midpoint ratios, attributed conditional Q&A and reusable topics; missing-baseline/call cases; actual saved-artifact inspection where configured; existing unittest suite/package validation and global-install parity. No new runtime/dependencies, commit, release, or image generation.

**Result:** the baseline already handled guidance arithmetic correctly but retained the compact/prose structure and detached source definitions. The revised full-report consumer produced a new `_v2` artifact with separate guidance versions, qualified Q&A and appropriate horizon/status labels; both the prior input and pre-existing output retained their hashes. A missing-input consumer exposed detached reference links, so a concrete topic/Source-bullet template was added; the fresh brief rerun preserved exact links and local context while disclosing unavailable baseline/call and unsaved status. Fresh read-only review found no material issues, including the template follow-up.

All 20 existing tests and four repository skill validators passed. Both installed earnings packages validated, and their five shipped files match repository hashes. Other installed skills retain equivalent content (unchanged release files may differ only in line endings). Existing earnings copies were fully backed up under each host's `skill-backups/morningwealth-quarter-record-20261030T053836Z`; installation receipts identify an unpublished local update after v1.2.2. Claude's personal extension retained its SHA-256. No commit, push, new release or financial-report vault save was performed.

## Earnings-call discovery and coverage follow-up

The user reports missing management speech/guidance after invoking earnings in Codex and supplies a public Facebook post. Read the actual post and locate its management topics in current full transcripts rather than assume the post's publisher/source. Diagnose source discovery separately from extraction on a supplied transcript; the earlier offline tests covered the latter only. A cached published plugin and the locally updated standalone skill coexist; bare invocation alone does not establish which was loaded.

**Modify:** `C:/git/morningwealth/plugins/encryptedarc/skills/earnings/SKILL.md`, `C:/git/morningwealth/plugins/encryptedarc/skills/earnings/references/earnings-framework.md`, `C:/git/morningwealth/plugins/encryptedarc/skills/earnings/references/source-policy.md`, `C:/git/morningwealth/tests/skill_evaluation.md` and this plan. Reuse existing references; no new runtime or source-provider dependency.

**Behavior:** discover the official event/replay first, then an inspected full transcript from a reputable publisher/identified provider if company text is absent or the player cannot be consumed. Distinguish transcript content from a generic quote aggregator; preserve its provider/source chain. Check issuer/period/date/participants, read through Q&A's end, record full/partial/unavailable coverage and actual limits, and retain all material distinct topics in detailed output. Retrieve formal guidance from the earnings release even when the call is blocked; label management outlook and derived ratios separately. A transcript is not an independent origin for the issuer's claims, and transcription discrepancies need reconciliation against official disclosures/audio rather than silent selection.

**Verify:** fresh consumer web discovery without a supplied transcript URL; controlled blocked-player/partial-transcript/identified-provider cases; actual management-topic/source coverage inspection; existing tests, package validators and global earnings file hashes with local-extension preservation. Sync only authorized standalone global copies, with backups/receipts; do not rewrite immutable published plugin caches or publish a new release without a request. Report unresolved runtime selection honestly.

**Result:** Facebook post was read through the browser and its topics located in full current call transcripts; the author's exact transcript supplier is not disclosed. Baseline and revised fresh consumers both discovered the live full transcript without a supplied transcript URL, so the user's original omission was not reproduced. Revised output disclosed full text coverage through closing, official audio not reviewed, publisher numeric discrepancies and unresolved speaker attribution. Synthetic full/partial variants passed without leaking inaccessible questions or dropping written guidance. Fresh read-only review found no material findings; 20 tests and repository earnings validation passed.

Backed up and synced five shipped earnings files to both standalone global roots under each host's `skill-backups/morningwealth-call-coverage-20261030T062610Z`, with matching hashes and Claude's extension preserved. Receipts identify an unpublished local update after v1.2.2. Published plugin caches remain intact; the user's bare Codex invocation alone does not establish which package was loaded. No commit/push/release or financial-report vault write.

## Release and machine installation — v1.3.0

The user explicitly authorized releasing the accumulated changes and installing the published version on this machine. Publish a minor feature release for company-first discovery, complete earnings/management coverage, versioned guidance/quarter records and reusable sourced topic blocks. Calculator/CLI semantics are unchanged.

- Bump `C:/git/morningwealth/plugins/encryptedarc/.codex-plugin/plugin.json` to 1.3.0 and document call discovery/coverage in `C:/git/morningwealth/README.md`; retain the accepted source, earnings and consumer-test changes above.
- Reuse the existing approved `feature/earnings-skill` branch, fast-forwarding it to current main; do not create an unapproved new branch. Commit logical source-policy, earnings-record and release-version units, push, merge through a PR, and publish tag v1.3.0 at the verified main commit. Check remote state before publishing; do not alter prior tags.
- Verify all 20 tests, four skill packages, both calculator selftests, diff hygiene and existing fresh consumer/reviewer results. The repository has no configured CI workflow; do not claim a nonexistent CI run.
- Use skill-installer to fetch all four skills from the published tag into a temporary staging directory. Back up both global installations, preserve local extensions, replace shipped files with release artifacts and verify exact hashes/package validation; write release/commit receipts outside skill directories.
- Update the configured Codex plugin through its supported marketplace/plugin command so it matches the released package, verify installed version/content, and preserve old backups for rollback. Do not manually relabel or overwrite an immutable older-version cache. Claude continues using the already authorized standalone global skills.
- Capture actual release/installation results in the existing Obsidian review note and final response. No financial report or infographic is generated by this release task.
