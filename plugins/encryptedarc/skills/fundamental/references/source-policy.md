# Financial-Statement Source Policy

Apply this policy to financial-statement analysis, including requested historical periods and their comparatives. Web search is a way to locate documents, not a measure of a source's authority. A document supplied by the user is current-session evidence: identify it as supplied, preserve its publication date and period, and disclose if its authenticity or amendment status cannot be independently checked.

Supplied documents are not independently verified merely because a filename says 10-Q or annual report. Check provenance against the regulator or issuer IR source when available. If provenance cannot be checked, label the input `User-supplied, unverified`; conditional calculations may proceed with explicit assumptions, but withhold affected factual conclusions or verdicts that require authentication.

## Source hierarchy

Use sources in this order of authority:

1. **Regulatory filings and filed statements** — SEC EDGAR, SET, the Thai SEC, exchange filings, 10-K, 10-Q, 20-F, 6-K, 8-K, 56-1 One Report, and financial statements filed with a regulator
2. **Audited company reports** — annual reports, audited financial statements, and company footnotes
3. **Official earnings and management materials** — earnings releases, earnings presentations, earnings calls, investor days, and IR releases for results, strategy, guidance, and management claims. An earnings release may be unaudited, so reconcile it with filed statements when a filing is available.
4. **Independent secondary sources** — Reuters, Bloomberg, FT, WSJ, CNBC, Bangkok Post, and other reputable financial media for external-event confirmation or context
5. **Aggregators and quote pages** — Yahoo Finance, Google Finance, Settrade, TradingView, and summary databases only as a last resort, with timestamp and basis checks

Search results, snippets, knowledge panels, and AI summaries are discovery aids only. Inspect the underlying document or attributable data record before using a material number or claim. If it is inaccessible, find an accessible authoritative source or reputable independent report; a snippet alone is never sufficient, even under time pressure.

For macro data, use the originating central bank, government statistics agency, or regulator. For market quotes, prefer the exchange or an attributable professional data feed, with the instrument, timestamp, and session identified. Financial media and aggregators do not become primary sources for company accounts or official statistics.

Before relying on a page, check its actual origin, byline/provider, publication/update date, relevant period, units, and whether it is editorial reporting, opinion, a company release, or paid content. Yahoo, Nasdaq, or another well-known host can republish third-party promotions; the host name alone does not establish reliability. A regulatory filing remains an issuer disclosure: preserve its audited, reviewed, or unaudited status and do not imply that the regulator guarantees its accuracy.

Do not use model memory, AI prediction sites, forums, or unverified social posts as factual sources. Sponsored or promotional articles are not independent factual evidence even when sponsorship is disclosed. An official issuer earnings release can support attributed results or guidance before the filing arrives, with its audit/review status disclosed; it does not independently establish market leadership, customer adoption, or external contract awards. Corroborate those claims with the relevant counterparty, authority, or independent reporting, or keep them labelled as management claims.

## Freshness by data type

### Live market data

Prices, market capitalization, FX rates, yields, and current valuation multiples must come from data within the last 24 hours or the expected market-close window and must include a timestamp:

- `✅ FRESH` — the latest close or data published within 24 hours
- `⚠️ INTRADAY` — data captured while the market is open
- `⚠️ PRE-MARKET / AFTER-HOURS` — extended-hours data
- If the source has no timestamp or is older than the expected close, write `No current data available`.

### Filing and financial-statement data

Do not apply the 24-hour rule to financial statements. Treat filing data as usable when:

- it covers the requested or comparative period; for a latest-results request, first identify the latest reported period
- the fiscal period and filing or publication date are stated
- the figures are the latest available amended, restated, or recast version for that same period as of the research date
- the basis matches the comparison, such as reported versus reported and quarter versus the same period a year earlier

A later reporting period does not invalidate an earlier filing needed for a historical quarter, YoY/QoQ comparison, or YTD subtraction. A newer amendment or restatement supersedes affected figures for the same period; use it consistently across the calculation and disclose the change. If a new reporting period should be available but cannot be found, disclose the data gap rather than estimating it. For an as-known-at-the-time analysis, use only documents published by the user's cutoff date and identify later restatements separately.

### Events after the reporting period

Check 8-K or 6-K filings, SET disclosures, company announcements, and reputable news published after the balance-sheet date. Clearly separate these events from the results of the historical reporting period. In a historical review, distinguish what was known at the release from later events; do not use later events to explain what management or the market knew then.

## Cross-verification

- A figure taken directly from a filing does not require a duplicate secondary source when its period, unit, and basis are consistent.
- Reconcile totals, subtotals, and derived metrics with the financial statements and footnotes.
- If an aggregator or presentation conflicts with a filing, use the filing and explain the difference.
- If primary filings conflict, use the latest amended or restated filing and disclose the change.
- A price move of `|change| ≥ 3%`, a gap, or unusual volume requires confirmation from a second independent market-data origin. Multiple copies of the same Reuters story, press release, or data feed count as one origin. If no independent corroboration is available, label the move uncorroborated and withhold conclusions that depend on it.
- If a material data conflict cannot be resolved, show both values and withhold the verdict for the affected area.

## Citation and precision

- Sourced figure: `[Source, publication date, fiscal period]`
- Material factual claim: `[Source, publication date]`, plus the fiscal period when the claim relates to financial statements or operating results
- Live figure: `[Source, timestamp, market session]`
- Derived figure: show the formula and cited inputs
- Management guidance: label it clearly as guidance or a target, not an actual result
- No verifiable data: write `No verifiable data available`

Make citations traceable: link the exact supporting filing, release, data record, or article, not a homepage or search result. Preserve the originating provider when citing a republisher. If the original is inaccessible but an inspected reputable secondary article supports the claim, cite that article and disclose the source chain; do not imply the original was read. For supplied files, cite the filename plus page/table/cell instead of inventing a URL.

Example:

```text
Revenue FY2025 $10.2B [Company 10-K, Feb 20 2026, FY ended Dec 31 2025]
FCF $1.1B = CFO $1.6B - capex $0.5B [Company 10-K, Feb 20 2026, FY2025]
Management targets gross margin above 60% [Q2 earnings call, Aug 7 2026] — Management guidance
```

Do not use `~`, `approximately`, `around`, or figures recalled from model memory in place of sourced figures.

## Pre-output check

1. Are the company, ticker, and exchange correct?
2. Do the documents cover the requested and comparison periods, using the latest applicable amendments or restatements within any user-specified cutoff?
3. Does every sourced number or claim include the appropriate source plus publication date or timestamp, and a fiscal period when applicable?
4. Is live market data within the freshness window and timestamped?
5. Are reported or adjusted, consolidated or segment, and currency or unit bases consistent?
6. Do derived figures show their formulas and reconcile to cited inputs?
7. Are management claims and analytical inferences separated from facts?
8. Was the supporting content inspected, its origin and independence checked, and its exact URL or supplied-file location included?

If any answer is no, research further or disclose the data gap. Do not fill it with an estimate.
