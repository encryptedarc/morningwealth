# Fundamental Source Policy

Apply this policy to business-quality and financial-statement analysis. Web search is a way to locate documents, not a measure of a source's authority.

## Source hierarchy

Use sources in this order of authority:

1. **Regulatory filings and filed statements** — SEC EDGAR, SET, the Thai SEC, exchange filings, 10-K, 10-Q, 20-F, 6-K, 8-K, 56-1 One Report, and financial statements filed with a regulator
2. **Audited company reports** — annual reports, audited financial statements, and company footnotes
3. **Official earnings and management materials** — earnings releases, earnings presentations, earnings calls, investor days, and IR releases for results, strategy, guidance, and management claims. An earnings release may be unaudited, so reconcile it with filed statements when a filing is available.
4. **Independent secondary sources** — Reuters, Bloomberg, FT, WSJ, CNBC, Bangkok Post, and other reputable financial media for external-event confirmation or context
5. **Aggregators and quote pages** — Yahoo Finance, Google Finance, Settrade, TradingView, and summary databases only as a last resort, with timestamp and basis checks

Use web search and search snippets to find sources. Do not cite a snippet instead of the underlying filing when the primary document is accessible.

Do not use model memory, AI prediction sites, sponsored content without disclosure, forums, or unverified social posts as factual sources.

## Freshness by data type

### Live market data

Prices, market capitalization, FX rates, yields, and current valuation multiples must come from data within the last 24 hours or the expected market-close window and must include a timestamp:

- `✅ FRESH` — the latest close or data published within 24 hours
- `⚠️ INTRADAY` — data captured while the market is open
- `⚠️ PRE-MARKET / AFTER-HOURS` — extended-hours data
- If the source has no timestamp or is older than the expected close, write `No current data available`.

### Filing and financial-statement data

Do not apply the 24-hour rule to financial statements. Treat filing data as usable when:

- it is the latest annual or interim filing published by the company as of the research date
- the fiscal period and filing or publication date are stated
- no newer amended or restated filing exists
- the basis matches the comparison, such as reported versus reported and quarter versus the same period a year earlier

A newer filing or restatement supersedes the older document. If a new reporting period should be available but cannot be found, disclose the data gap rather than estimating it.

### Events after the reporting period

Check 8-K or 6-K filings, SET disclosures, company announcements, and reputable news published after the balance-sheet date. Clearly separate these events from the results of the historical reporting period.

## Cross-verification

- A figure taken directly from a filing does not require a duplicate secondary source when its period, unit, and basis are consistent.
- Reconcile totals, subtotals, and derived metrics with the financial statements and footnotes.
- If an aggregator or presentation conflicts with a filing, use the filing and explain the difference.
- If primary filings conflict, use the latest amended or restated filing and disclose the change.
- A price move of `|change| ≥ 3%`, a gap, or unusual volume requires confirmation from a second market-data source.
- If a material data conflict cannot be resolved, show both values and withhold the verdict for the affected area.

## Citation and precision

- Sourced figure: `[Source, publication date, fiscal period]`
- Material factual claim: `[Source, publication date]`, plus the fiscal period when the claim relates to financial statements or operating results
- Live figure: `[Source, timestamp, market session]`
- Derived figure: show the formula and cited inputs
- Management guidance: label it clearly as guidance or a target, not an actual result
- No verifiable data: write `No verifiable data available`

Example:

```text
Revenue FY2025 $10.2B [Company 10-K, Feb 20 2026, FY ended Dec 31 2025]
FCF $1.1B = CFO $1.6B - capex $0.5B [Company 10-K, Feb 20 2026, FY2025]
Management targets gross margin above 60% [Q2 earnings call, Aug 7 2026] — Management guidance
```

Do not use `~`, `approximately`, `around`, or figures recalled from model memory in place of sourced figures.

## Pre-output check

1. Are the company, ticker, and exchange correct?
2. Are the annual and interim filings the latest available?
3. Does every sourced number or claim include the appropriate source plus publication date or timestamp, and a fiscal period when applicable?
4. Is live market data within the freshness window and timestamped?
5. Are reported or adjusted, consolidated or segment, and currency or unit bases consistent?
6. Do derived figures show their formulas and reconcile to cited inputs?
7. Are management claims and analytical inferences separated from facts?

If any answer is no, research further or disclose the data gap. Do not fill it with an estimate.
