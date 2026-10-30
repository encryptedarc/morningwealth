---
name: earnings
description: "Use when a user asks to read, explain, or break down a listed company's quarterly or interim results (earnings release, 10-Q, 6-K, SET interim financial statements and MD&A) for US, Thai, or other markets, or invokes the command with a ticker such as `earnings GOOG` or `earnings PTT.BK Q2 2026`. Explains what changed in the quarter in plain language for a beginner. Do not use for full business-quality reviews, fair value or target-price work, price-only requests, or trade recommendations."
---

# Earnings

Read the latest (or requested) quarterly results of a listed company and explain what happened, why, and what to watch next. Produce a clearly headed review with reusable evidence blocks and a quarter record for future comparisons. Explain specialist terms for a beginner without discarding material detail. Do not issue buy or sell recommendations.

## Arguments

When invoked as a command, the arguments are a ticker and an optional period:

- `GOOG`, `MSFT`, `PTT.BK`, `PTT`, `CPALL.BK`
- `GOOG Q2 2026`, `PTT.BK 9M 2026`, `AAPL FY2026 Q4`

A `.BK` suffix means the Stock Exchange of Thailand (SET or mai). A bare ticker that is listed in more than one market, or that does not resolve to one company, needs one clarifying question before research. With no period, use the most recent reported quarter.

## Language

Respond in the language of the user's request. When the request contains only a ticker and period, use the language of the surrounding conversation, or English when there is none. Explain each specialist term in plain language the first time it appears, such as EPS, operating margin, FCF, guidance, or backlog, then use the term normally.

Use a title for company/period, `##` headings for sections and `###` headings for individual business or management topics. Leave a blank line after headings and before lists. Use one substantive claim per bullet and tables for comparable metrics or guidance versions. Fill the reusable topic template in `references/quarter-record.md`, including its local context and Source bullet with inline exact links. This keeps the period, units, basis, uncertainty and source intact when a topic is extracted for a future infographic. Generate visual assets only when requested.

## Load before research

1. Read `references/source-policy.md` for the source hierarchy, freshness rules, citation format, and cross-verification rules.
2. Read `references/earnings-framework.md` for the market-specific documents, archetype metrics, quarter pitfalls, and output structure.
3. Read `references/quarter-record.md` for previous-record inputs, guidance revisions, management/Q&A records, reusable topics, and authorized persistence.

## Optional local extension

If `local/extension.md` exists in this skill directory, read it after the references and apply it. A local extension may set a default language, connect personal notes such as an investment thesis, or add a save step. It cannot override the source policy, the citation rules, or the no-recommendation rule.

## Scope boundaries

- Use this skill for one reporting period: results versus the prior year and prior quarter, versus guidance and consensus when sourced, plus cash flow, balance-sheet changes, and management commentary.
- For a multi-year review of business quality, moat, and capital allocation, use `fundamental`.
- For fair value, target price, cheap versus expensive, or DCF work, use `valuation-deep-dive`.
- If a sibling skill is not installed, explain the scope boundary and ask for it or offer the supported earnings analysis; do not assume it can be loaded.
- Report the market reaction only with timestamped price data under the live-data rules. Do not explain a price move with a cause the evidence does not support.

## Workflow

### 1. Resolve the company and period

State the current date first. Confirm the company name, ticker, exchange, fiscal year-end, and the period to analyze.

- If the next report date has passed but the results cannot be found, say so and analyze the latest available quarter instead.
- If results were released within the last few days, the full quarterly filing may not be filed yet. Use the earnings release and say which filing is still pending.
- Fiscal quarters that do not match calendar quarters must be labelled with both, such as `FY2027 Q1 (quarter ended Sep 30 2026)`.

Read a previous-quarter record when supplied or available in a location configured by applicable instructions/local extension. Use it to identify earlier guidance, open questions, and monitoring items before analyzing the new results. Treat it as a historical baseline, not a replacement for current primary evidence. If unavailable, disclose the missing baseline and continue with what can be verified; do not reconstruct prior statements from memory.

### 2. Gather the documents

Start at the verified company IR site and collect the documents listed for its market in `references/earnings-framework.md`: full statements and footnotes, the earnings release, presentations, and the call. Then compare the document/version and material headline figures with regulator/exchange records and inspect reputable independent coverage where available. Prefer the company-hosted original citation when the document/version matches; an Exhibit 99.1 copy on SEC is still the issuer's release, not a second independent origin. Use the latest applicable full/amended statements over a conflicting preliminary release regardless of host. Record publication dates, fiscal periods, and a concise source-check result; disclose blocked or unavailable verification.

Always look for the earnings call transcript or replay, or the analyst meeting for companies without a call. Read it using the earnings-call section of the framework, so the output reports what management said and what analysts pressed on, not only the numbers. If it is not accessible, say so.

Follow the discovery and coverage checks in framework section 5 before concluding the call is unavailable. If IR offers only an unreadable player, seek an inspected full transcript with identified provenance. Read the release's guidance separately even when the call is blocked; a missing call does not make disclosed guidance unavailable. Report the source/provider and whether prepared remarks and Q&A were fully or partially inspected.

### 3. Analyze

Classify the archetype, select the quarter metrics that fit it, and work through the sections of the output structure. For every material change, separate operating causes from accounting, one-off, FX, or share-count effects. Check every pitfall in the framework before writing.

Compare like-for-like actuals with both original as-issued guidance and later revisions. Keep formal guidance, management outlook, aspiration/milestone, derived figures, and analysis distinct. Capture material prepared remarks and Q&A with named speakers, conditions and source locations, using `references/quarter-record.md`.

### 4. Deliver

Deliver Markdown using the structured report in section 6 of `references/earnings-framework.md`. Start with a short summary, then retain material financial details, management explanations, guidance versions, Q&A and next-quarter checks under clear headings and bullets. Condense chat only when the user asks for a brief answer; a separately authorized saved quarter record retains the material evidence and comparison fields. Combine or omit immaterial/inapplicable sections without dropping material uncertainty.

### 5. Preserve the quarter record

Prepare the archive-ready record described in `references/quarter-record.md`. Save only when an authorized destination and permission are established by the user's request, applicable instructions or local extension. A configured path alone does not cancel an ask-before-save rule; existing session authorization need not be requested again. Preserve previous records and guidance versions. If persistence is unavailable or not authorized, return the structured Markdown in chat and state that no persistent record was saved.

## Evidence rules

- Cite every number with `[Source, publication date, fiscal period]` and state the currency, unit, and basis (reported or adjusted, consolidated or segment).
- Show the formula for every derived figure, including a Q4 derived from full-year minus nine months.
- Use the statement types in `references/quarter-record.md`: distinguish formal guidance, management outlook, aspirations/milestones and management claims from `Derived` calculations and `Analysis/Inference`.
- Cite consensus only with its compiler and publisher, such as `LSEG consensus via Reuters`. If no consensus is verifiable, omit the beat or miss column rather than estimating it.
- If a figure cannot be verified in the current session, write `No verifiable data available` and list it under What I Don't Know.

## Quarter verdict

Judge the quarter, not the stock. Choose one:

- `Strong quarter`
- `Mixed quarter`
- `Weak quarter`
- `Insufficient data to assess`

A strong quarter can coincide with a falling share price, and a weak quarter with a rising one. Say which evidence drove the verdict.

End every analysis with an educational-only disclaimer in the user's language:

> This material is for educational purposes only and is not investment advice. Consult a licensed adviser before making investment decisions.
