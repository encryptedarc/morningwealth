# Quarterly Earnings Framework

Use this reference after resolving the company and period. It lists which documents to collect for each market, which quarter metrics fit each archetype, the pitfalls that most often distort a quarter, and the output structure.

## 1. Documents by market

### United States (10-Q filers)

| Document | Where | Notes |
|---|---|---|
| Earnings release | Company IR first; compare the corresponding 8-K Exhibit 99.1 on SEC EDGAR | Published on results day. Often unaudited and may include adjusted figures with a reconciliation. Identical IR/SEC copies are one issuer release, not independent confirmations. |
| 10-Q | Company IR financial-report library first; SEC EDGAR to verify or obtain missing filings/amendments | Filed after the release, often days or weeks later. Holds full statements, segment notes, debt, share count, and risk updates. There is usually no 10-Q for the fourth fiscal quarter. |
| 10-K | Company IR first; SEC EDGAR to verify or obtain the applicable version | Source for the fourth quarter when it is not reported separately, and for full-year comparisons. |
| Presentation and earnings call | IR page; transcript from a reputable publisher | Guidance, segment KPIs, and management explanations. Management claims, not independent evidence. |

### United States (foreign private issuers)

Find 20-F annual and 6-K interim reports on company IR first, then compare with SEC EDGAR or use its inspected copy as a fallback. Some issuers report only half-yearly; say so instead of inventing a quarter.

### Thailand (SET and mai)

| Document | Where | Notes |
|---|---|---|
| Interim financial statements | Company IR first; SET company news/page to compare the filed version | Reviewed, not audited, for the first three quarters. Each filing contains consolidated statements and separate (company-only) statements. Use consolidated figures. |
| Management discussion and analysis (MD&A) | Company IR first; compare the version filed with statements on SET | Management's explanation of the drivers. Often includes a core or normalized profit figure. |
| Annual audited statements and 56-1 One Report | Company IR first; SET/Thai SEC for verification or missing/amended records | Source for the fourth quarter, which many companies do not report separately. |
| Analyst meeting or Opportunity Day presentation | SET Opportunity Day archive; IR page | Guidance and KPIs. Many Thai companies hold no earnings call. |

Thai statements are frequently presented in thousands or millions of baht, sometimes with different units in different tables. Confirm the unit on each table before comparing.

### Other markets

Use the verified company IR site first, then compare with the market's regulatory filing system or exchange disclosure portal and reputable independent coverage where available. If IR is inaccessible, use an inspected official record and disclose the fallback. State whether the company reports quarterly or half-yearly.

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
10. **Guidance.** Compare actual results separately with original as-issued guidance and the latest pre-results revision when available. Preserve dated revisions and compare new versus old guidance only for the same target period and basis. Label formal guidance, management outlook and derived calculations distinctly; see `references/quarter-record.md`.
11. **Accounting standard.** Note the basis, such as US GAAP, IFRS, or TFRS. Lease accounting under IFRS 16 or TFRS 16 shifts costs between operating expense and depreciation and interest.

## 5. Reading the earnings call

Treat the call as evidence of what management chose to emphasize, not as evidence of results. Use, in order: the official transcript or replay on the IR page, a transcript from a reputable publisher, then reputable news coverage of the call. For Thai companies without a call, use the analyst meeting or Opportunity Day presentation and replay. If no transcript or replay is accessible, say so and do not reconstruct the call from headlines.

### Find the call and establish coverage

1. Open the requested period's IR results/event page and follow its transcript/replay link, including a service provider linked by the company. A webcast announcement or player URL proves availability, not that its speech was read/heard. Use browser rendering when available if the page is only a JavaScript shell; do not bypass login, paywalls or access controls.
2. If official text is absent or replay content cannot be consumed, search company/ticker + fiscal quarter/year + `earnings call transcript`, matching the actual call date. Open a credible full-text result, such as a publisher's transcript or a licensed provider's transcript carried on another site. Inspect issuer, period, date, participants and provider attribution; do not use search snippets, a different year's call or an AI summary as the transcript.
3. Read both prepared remarks and the analyst exchanges through the final Q&A/closing section. Fetch later sections/pages when the tool returns only an excerpt. A page title saying Full Transcript does not establish complete reading. For detailed output retain all material distinct topics, including relevant subquestions, rather than stopping after the first exchange or imposing a fixed question count. A secondary recap may split or combine actual caller exchanges; preserve real analyst/executive attribution.
4. Cross-check disclosed financial guidance against the release's guidance/outlook section. Collect call-only outlooks, business targets, capex intentions and explicit refusals to give targets separately. Retain qualifications and do not turn a statement that a plan can be funded into proof that it uses only operating cash flow or requires no debt.
5. Check consequential transcription discrepancies against official disclosures and, if consumable, the original audio. A second reputable transcript may expose differences, but two carriers of the same provider are not separate origins. Use written formal guidance for its stated metric/period/basis, disclose a discrepancy rather than silently correcting what a transcript says, and leave unresolved call-only wording/numbers uncertain.
6. If no usable full transcript is found, try another credible publisher/provider before closing the search. Stop when relevant accessible sources are exhausted or remaining routes require unavailable tools/access. Use inspected partial text or attributed news coverage within its limits; keep verified release guidance and disclose what could not be obtained.

Include a concise coverage note: call date; exact inspected source and originating provider; prepared remarks and Q&A status (`Full text read`, `Partial text read`, `Replay reviewed`, or `Unavailable`); sections/exchanges covered and any missing remainder. State separately if the official replay was linked but not listened to. No fixed minimum Q&A count substitutes for coverage evidence.

Extract:

1. **Prepared remarks: key themes** — the three to five topics management led with, and any metric newly disclosed or no longer disclosed.
2. **Analyst Q&A** — the questions analysts pressed on, and whether management answered directly, deflected, or declined. Repeated questions on one topic signal the market's main concern.
3. **Commitments and numbers** — guidance, outlooks, targets, timelines, capex plans, launch dates, and capital-return plans, each with speaker/role, target period, statement type and material conditions. A long-term aspiration is not a near-term commitment.
4. **Change in tone or message** — compare with the prior call when available: what was dropped, added, softened, or strengthened. Report it as `Analysis/Inference` with the two statements side by side.
5. **Statements versus results** — check each claim against the filed figures in the same quarter, and flag a claim that the numbers do not support.

Attribute each item to a named speaker and role, such as `CFO, Q3 2026 call, Oct 28 2026`. Paraphrase by default; quote only a short phrase when the exact wording matters, such as a guidance change, and keep quotes brief.

## 6. Output structure

Default to the structured report below. Use a company/period title, `##` section headings, `###` business or management-topic headings and clear bullets, in the user's language. Each topic should be reusable with its own period, units/basis, statement type, exact source link and material caveat. Avoid repeating the same narrative in business highlights and Q&A; keep Q&A's question, answer and follow-up context distinct.

### Compact answer (only when explicitly requested)

Open with the research date, company/ticker/exchange, fiscal period and quarter-end date when known. Then use these five sections in the user's language, with a small scoreboard only when it helps:

1. **Results and verdict** — the headline numbers and quarter verdict, with YoY or QoQ only when comparable evidence exists.
2. **Drivers** — the material business or segment changes; separate disclosed causes from inference.
3. **Earnings and cash quality** — one-offs, tax, dilution, cash conversion, and material balance-sheet changes. For banks and insurers, replace corporate FCF/net-debt analysis with the applicable credit, liquidity, underwriting, or capital measures from section 3.
4. **Guidance and management** — new versus prior guidance and the main call/Q&A point when accessible; otherwise state the missing evidence once.
5. **What to watch and data gaps** — the leading indicators, material risks, and unresolved evidence gaps. End with the educational disclaimer.

Cite figures and claims inline and identify documents by publication date and fiscal period. A separately authorized saved quarter record still retains material guidance versions, management/Q&A evidence and comparison fields under `references/quarter-record.md`. Missing optional consensus or price data does not prevent analysis of verified statements; omit the unavailable comparison or market reaction.

### Structured report (default)

Start with a brief summary, then preserve material detail under the following headings. Adapt metrics to the archetype and omit inapplicable metrics rather than inventing corporate FCF or net debt for a bank. Combine immaterial sections; a missing material call, prior baseline or financial disclosure needs an explicit gap, not an invented section body.

1. **Data as of and source checks** — research date, company, ticker, exchange, period, quarter-end date, documents/publication dates, primary company source and cross-check results/limits. Include the call coverage note from section 5. State the prior record used or that a prior-quarter baseline is unavailable. Flag pending filings.
2. **The quarter in 30 seconds** — three to five bullets covering the headline result, the biggest surprise, and the quarter verdict.
3. **Scoreboard** — a table with plain-language column headings: metric, this quarter, same quarter last year, YoY change, prior quarter, QoQ change, and consensus with beat or miss only when sourced. Lead with the archetype metrics.
4. **Revenue and business drivers** — separate `###` topics for material segments/products; contributions and growth split into volume, price, mix, FX or acquisitions when disclosed. Distinguish backlog, run rate, signed commitments and recognized revenue.
5. **Profit: from revenue to EPS** — margins, operating costs, then each layer between operating profit and EPS (non-operating items, tax, minority interests, share count). When EPS and operating profit move in different directions, show the layers that explain the gap.
6. **Cash flow, investment and funding** — CFO, reconciling items from net income, capex, FCF and material SBC; separate quarterly, YTD and TTM periods. Test funding claims against disclosed cash generation, liquidity and financing rather than presenting management confidence as proof.
7. **Balance sheet** — cash and investments, debt, net debt or net cash, working-capital items, and financing during the quarter.
8. **Guidance and outlook register** — original as-issued guidance, dated revisions, comparable actuals, new guidance, horizons and conditions under `references/quarter-record.md`. Separate formal guidance, management outlook/aspirations and derived midpoint figures; assess original and revised ranges separately.
9. **Management prepared remarks** — topic bullets with named speaker/role, statement type, evidence and conditions; new/dropped disclosures and supported changes in message versus the prior call.
10. **Analyst Q&A** — `###` topic blocks with question/analyst when known, answer/executive, conditions, source location, unanswered point and next observable check. Preserve explicit refusal to give a target. Mark unavailable if the call cannot be inspected.
11. **Market reaction** — optional; only with timestamped price data, session labels and required independent cross-checks.
12. **Changes since the prior record and next checks** — outcomes of previous guidance, milestones and open questions; distinguish what changed from what is not yet due. State two to five indicators and the evidence needed at the next report, with its date only when announced.
13. **Risks and What I Don't Know** — what would weaken the explanation/thesis, material missing data and the statement, footnote, transcript or later result that would resolve each gap. Preserve any configured personal-thesis section without disclosing personal position size in reusable/public content.
14. **Disclaimer** — educational only, not investment advice, in the user's language.

## 7. Pre-output check

1. Is the period the latest available, or the one the user requested?
2. Are units, currencies, and bases consistent within every comparison?
3. Do segment figures add up to the reported total?
4. Are derived quarters and ratios shown with formulas?
5. Is every non-operating or one-time item quantified and separated?
6. Are management claims and guidance labelled and attributed to a speaker, and was the call transcript or replay actually read?
7. Is any live price data timestamped and within the freshness window?
8. Are original guidance and later revisions retained, with like-for-like actuals and appropriate due-date/status labels?
9. Can each material topic be reused with its heading/bullets without losing source, period, units/basis, statement type or conditions?
10. Does the quarter record identify its prior baseline and persistence status without overwriting history or bypassing configured save permission?
11. Does stated call coverage match the text/audio actually inspected, including later Q&A, with release guidance retained even if call access is limited?

If any answer is no, research further or disclose the gap. Do not fill it with an estimate.
