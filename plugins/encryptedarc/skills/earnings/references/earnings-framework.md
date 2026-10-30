# Quarterly Earnings Framework

Use this reference after resolving the company and period. It lists which documents to collect for each market, which quarter metrics fit each archetype, the pitfalls that most often distort a quarter, and the output structure.

## 1. Documents by market

### United States (10-Q filers)

| Document | Where | Notes |
|---|---|---|
| Earnings release | 8-K, usually Exhibit 99.1, on SEC EDGAR; company IR page | Published on results day. Often unaudited and may include adjusted (non-GAAP) figures with a reconciliation table. |
| 10-Q | SEC EDGAR | Filed after the release, often days or weeks later. Holds full statements, segment notes, debt, share count, and risk updates. There is usually no 10-Q for the fourth fiscal quarter. |
| 10-K | SEC EDGAR | Source for the fourth quarter when it is not reported separately, and for full-year comparisons. |
| Presentation and earnings call | IR page; transcript from a reputable publisher | Guidance, segment KPIs, and management explanations. Management claims, not independent evidence. |

### United States (foreign private issuers)

20-F for annual results and 6-K for interim results. Some issuers report only half-yearly; say so instead of inventing a quarter.

### Thailand (SET and mai)

| Document | Where | Notes |
|---|---|---|
| Interim financial statements | SET company news and company page; company IR page | Reviewed, not audited, for the first three quarters. Each filing contains consolidated statements and separate (company-only) statements. Use consolidated figures. |
| Management discussion and analysis (MD&A) | Filed with the statements on SET | Management's explanation of the drivers. Often includes a core or normalized profit figure. |
| Annual audited statements and 56-1 One Report | SET; Thai SEC | Source for the fourth quarter, which many companies do not report separately. |
| Analyst meeting or Opportunity Day presentation | SET Opportunity Day archive; IR page | Guidance and KPIs. Many Thai companies hold no earnings call. |

Thai statements are frequently presented in thousands or millions of baht, sometimes with different units in different tables. Confirm the unit on each table before comparing.

### Other markets

Use the market's regulatory filing system first (for example, the stock exchange disclosure portal), then the company IR page. State whether the company reports quarterly or half-yearly.

## 2. Comparison periods

- Compare the quarter with the same quarter a year earlier (YoY) as the primary comparison, because it removes seasonality.
- Add the prior quarter (QoQ) when the business has little seasonality or when momentum matters, and say which comparison is seasonal.
- Use year-to-date figures when the company reports only cumulative cash flow, which is common: derive the single quarter as `current YTD - prior YTD` and show the formula.
- For a fourth quarter not reported separately, derive additive income-statement and cash-flow amounts as `Q4 = full year - nine months`, and label them derived. Both inputs must use the same accounting basis, scope, currency, and restatement version.
- EPS, margins, ratios, and weighted-average shares are not additive. Use the issuer's disclosed quarter EPS, or compute it from the quarter's common-share earnings numerator and quarter-specific weighted-average shares. Never subtract annual EPS minus nine-month EPS or divide by annual/YTD average shares. Recalculate margins from quarter amounts. If the quarter denominator or dilution treatment is unavailable, leave EPS unavailable; loss quarters can exclude securities that dilute full-year earnings.
- Balance-sheet figures are stocks at a date. Use the quarter-end balance and compare it with another stated date; their difference is a change in balance, not the quarter's revenue, profit, or cash flow.
- Use the restated comparative period when the company has restated or reclassified prior figures, and say so.

## 3. Quarter metrics by archetype

| Archetype | Quarter metrics to lead with | Avoid or treat with care |
|---|---|---|
| General corporate | revenue by segment, gross and operating margin, EPS (diluted), CFO, capex, FCF, net debt | EPS moved by one-offs; adjusted figures without the reconciliation |
| Bank | net interest income, NIM, loan and deposit growth, fee income, credit cost, NPL ratio, coverage ratio, CET1 or CAR | revenue growth, FCF, EBITDA |
| Insurer | premium growth, combined ratio, underwriting result, investment income, solvency ratio | net income without separating investment gains |
| REIT or property fund | occupancy, rental reversion, NOI, FFO or AFFO per unit, distribution per unit, gearing | EPS and net income moved by fair-value changes |
| Cyclical or commodity, including refiners and petrochemicals | volume, realized price or spread, unit cost, utilization, inventory gain or loss, hedging gain or loss | reported profit without removing inventory and hedging effects |
| Retail and consumer | same-store sales growth, store count, gross margin, inventory days | total sales growth driven only by new stores |
| SaaS or subscription | ARR, net revenue retention, remaining performance obligations or backlog, gross margin, SBC, FCF | adjusted EBITDA that excludes SBC |
| Pre-profit or high-growth | revenue growth, gross-margin trend, cash burn, cash runway, share issuance | P/E, ROE |

Use the metrics the company actually discloses. If a key metric is not disclosed, say so instead of approximating it.

## 4. Quarter pitfalls to check

1. **Reported versus adjusted.** Lead with reported figures. Use an adjusted figure only next to its reconciliation, and say what it excludes.
2. **Non-operating items.** Gains or losses on equity investments, fair-value changes, FX, impairments, restructuring, litigation, and disposals can dominate a quarter. Quantify them and show profit with and without them.
3. **Tax.** A one-time tax benefit or charge changes net income without changing the business. Compare the effective tax rate with the prior year.
4. **Share count.** EPS can move because of buybacks or dilution. Use the quarter-specific diluted weighted-average shares from the EPS note, not the period-end or annual share count. Quantify the share-count effect only when the earnings numerators and denominators reconcile; otherwise disclose the limitation.
5. **Owners of the parent.** Use profit attributable to owners of the parent, not total profit including minority interests.
6. **Cash versus profit.** Compare CFO with net income. Explain large working-capital swings in receivables, inventory, payables, and deferred revenue.
7. **Capex and FCF.** State whether capex was guided, and whether the rise is maintenance or growth when disclosed. `FCF = CFO - capex` unless the company defines it differently, in which case show both.
8. **Financing.** New debt, equity issuance, or large buybacks during the quarter change the balance sheet. Report them with the source.
9. **Segment changes.** A resegmentation breaks comparisons. Use the company's recast prior-period figures.
10. **Guidance.** Compare actual results with the most recent prior guidance when available, and compare new guidance with old guidance. Label guidance as management's forecast.
11. **Accounting standard.** Note the basis, such as US GAAP, IFRS, or TFRS. Lease accounting under IFRS 16 or TFRS 16 shifts costs between operating expense and depreciation and interest.

## 5. Reading the earnings call

Treat the call as evidence of what management chose to emphasize, not as evidence of results. Use, in order: the official transcript or replay on the IR page, a transcript from a reputable publisher, then reputable news coverage of the call. For Thai companies without a call, use the analyst meeting or Opportunity Day presentation and replay. If no transcript or replay is accessible, say so and do not reconstruct the call from headlines.

Extract:

1. **Prepared remarks: key themes** — the three to five topics management led with, and any metric newly disclosed or no longer disclosed.
2. **Analyst Q&A** — the questions analysts pressed on, and whether management answered directly, deflected, or declined. Repeated questions on one topic signal the market's main concern.
3. **Commitments and numbers** — guidance, targets, timelines, capex plans, launch dates, and capital-return plans, each with the speaker and the period it refers to.
4. **Change in tone or message** — compare with the prior call when available: what was dropped, added, softened, or strengthened. Report it as `Analysis/Inference` with the two statements side by side.
5. **Statements versus results** — check each claim against the filed figures in the same quarter, and flag a claim that the numbers do not support.

Attribute each item to a named speaker and role, such as `CFO, Q3 2026 call, Oct 28 2026`. Paraphrase by default; quote only a short phrase when the exact wording matters, such as a guidance change, and keep quotes brief.

## 6. Output structure

### Compact answer (default)

Open with the research date, company/ticker/exchange, fiscal period and quarter-end date when known. Then use these five sections in the user's language, with a small scoreboard only when it helps:

1. **Results and verdict** — the headline numbers and quarter verdict, with YoY or QoQ only when comparable evidence exists.
2. **Drivers** — the material business or segment changes; separate disclosed causes from inference.
3. **Earnings and cash quality** — one-offs, tax, dilution, cash conversion, and material balance-sheet changes. For banks and insurers, replace corporate FCF/net-debt analysis with the applicable credit, liquidity, underwriting, or capital measures from section 3.
4. **Guidance and management** — new versus prior guidance and the main call/Q&A point when accessible; otherwise state the missing evidence once.
5. **What to watch and data gaps** — the leading indicators, material risks, and unresolved evidence gaps. End with the educational disclaimer.

Cite figures and claims inline and identify documents by publication date and fiscal period. Combine related gaps in one sentence when appropriate. Missing optional consensus or price data does not prevent analysis of verified statements; omit the unavailable comparison or market reaction. Expand the affected section for material complexity instead of printing empty headings.

### Detailed answer (on request or when material complexity needs it)

Use the following as the full research checklist and the detailed output structure. Adapt metrics to the archetype; omit inapplicable metrics rather than inventing corporate FCF or net debt for a bank. Combine immaterial sections and disclose material data gaps.

1. **Data as of** — research date, company, ticker, exchange, period, and a table of documents used with publication dates. Flag any pending filing.
2. **The quarter in 30 seconds** — three to five bullets covering the headline result, the biggest surprise, and the quarter verdict.
3. **Scoreboard** — a table with plain-language column headings: metric, this quarter, same quarter last year, YoY change, prior quarter, QoQ change, and consensus with beat or miss only when sourced. Lead with the archetype metrics.
4. **Revenue: what drove it** — segment contributions; split growth into volume, price, mix, FX, and acquisitions when disclosed.
5. **Profit: from revenue to EPS** — margins, operating costs, then each layer between operating profit and EPS (non-operating items, tax, minority interests, share count). When EPS and operating profit move in different directions, show the layers that explain the gap.
6. **Cash flow** — CFO, the main reconciling items from net income to CFO, capex, FCF, and SBC when material.
7. **Balance sheet** — cash and investments, debt, net debt or net cash, working-capital items, and financing during the quarter.
8. **What management said** — follow section 5: key themes, analyst Q&A pressure points, commitments with speaker attribution, change in tone versus the prior call, and any claim the numbers do not support. Include a table of guidance with new versus prior values. Label every item `Management claim` or `Guidance`.
9. **Market reaction** — optional; only with timestamped price data and a session label.
10. **What changed and what to watch** — what the quarter changes about the business, and two to five leading indicators for the next report, with the next report date when announced.
11. **What I Don't Know** — each data gap and the filing, footnote, or transcript that would resolve it.
12. **Quarter verdict** — the verdict, with the evidence that drove it.
13. **Disclaimer** — educational only, not investment advice, in the user's language.

## 7. Pre-output check

1. Is the period the latest available, or the one the user requested?
2. Are units, currencies, and bases consistent within every comparison?
3. Do segment figures add up to the reported total?
4. Are derived quarters and ratios shown with formulas?
5. Is every non-operating or one-time item quantified and separated?
6. Are management claims and guidance labelled and attributed to a speaker, and was the call transcript or replay actually read?
7. Is any live price data timestamped and within the freshness window?

If any answer is no, research further or disclose the gap. Do not fill it with an estimate.
