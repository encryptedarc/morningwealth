# Sourcing Valuation Inputs

`core-finance-principles.md` governs **price** sourcing. This file governs the balance-sheet and income-statement inputs that a valuation needs, because those fail differently: a stale price is obvious, a stale share count is invisible and silently rescales every per-share number you report.

## 1. Where each input comes from

| Input | Primary source | Notes |
|---|---|---|
| Diluted share count | Latest 10-Q/10-K cover page or EPS note; SET quarterly financials for Thai names | Use the **latest** count, not the weighted average used for EPS — they differ after a raise. For ADRs, check the ADS ratio before any per-share math. |
| Warrants / converts / RSUs | Filing footnotes, capitalization note | Material for recent IPOs, SPAC legacies, and cloud names. Report fully diluted. |
| Cash & equivalents, short-term investments | Balance sheet | Distinguish liquid ST investments from illiquid strategic stakes — see `archetype-playbooks.md` §4. |
| Total debt | Balance sheet, current + non-current | Include lease liabilities where lease-adjusting (`archetype-playbooks.md` §3), and be consistent across the subject and every peer. |
| Minority interest, preferred | Balance sheet / equity note | Needed for a correct EV bridge; omitting them understates EV. |
| TTM revenue, EBITDA, EBIT, net income | Sum the last 4 quarters from filings, or stockanalysis / macrotrends for the assembled series | If you use an aggregator, cite the aggregator — do not present it as if read from the filing. |
| Capex, D&A, ΔNWC, FCF | Cash flow statement | Separate maintenance from growth capex where the company discloses it; where it does not, say so rather than estimating silently. |
| SBC | Cash flow statement (add-back line) | Material for software and asset-light names. |
| Book value / tangible book | Balance sheet | Tangible = equity − goodwill − intangibles. Needed for §7 banks. |
| Bank-specific (NIM, credit cost, NPL, CET1) | MD&A, investor presentation, regulator filings | BOT publishes Thai banking-system aggregates for context. |
| Forward consensus | Search current coverage; note provider and analyst count | Thin coverage on SET small caps — see `thai-market-notes.md` §5. |
| Risk-free rate, ERP, beta | See `dcf-and-cost-of-capital.md` §1 | Cited or declared as an assumption. No third option. |
| Segment detail, concession terms, lease schedule | 10-K / 56-1 One Report, footnotes | The footnotes are where the archetype is actually confirmed. |

**Filing access:** SEC EDGAR (`sec.gov`) for US and for foreign private issuers (20-F); SET company pages and SETSMART, plus ก.ล.ต. and the company IR page, for Thai names. Investor presentations are fast and useful but are marketing documents — cross-check any headline number against the statements.

## 2. Hard rules

1. **Never mix a multiple from one source with the metric from another.** A forward multiple is computed off a specific estimate; substituting a different provider's revenue produces a number that corresponds to no one's view. Full detail in `peer-calibration.md` §2.
2. **Never mix fiscal-year and calendar-year figures** in the same table without labelling. Convert or label.
3. **Never mix adjusted and GAAP** across the subject and its peers.
4. **Financials older than two reported quarters are stale for valuation.** Say so and treat it as a stop condition (SKILL.md) rather than valuing off numbers that a subsequent quarter may have already contradicted.
5. **Do your own estimate before you look at analyst targets.** Reading the target first anchors the model, and the anchoring is invisible in the output. Build the valuation, then pull consensus, then explain the gap — the gap and its reason is the finding worth reporting, and it is the part the user cannot get from a broker note.
6. **If a source page is JS-rendered, paywalled, or bot-blocked, say so explicitly** and work from what is verified. A missing line becomes "ไม่มีข้อมูลอัปเดต" and goes into `What I Don't Know`, never into an estimate.
7. **Sourced numbers are exact; derived numbers are rounded.** A figure with a citation carries the source's precision and never takes `~` or `(ประมาณ)`. A figure you computed — fair value, normalized EPS, implied multiple — should be rounded to a clean number or given as a range, and it says so by being round. `฿255-280 (center ฿265)` is right; `~฿265` is not. See SKILL.md, "Precision register".
8. **Print the input set with the answer.** Every valuation output should carry the inputs it used (price, shares, net debt, forward metric, discount rate, growth, exit multiple) so the user can re-run or argue with any one of them. `scripts/valuation.py` does this by design.

## 3. Quick freshness triage for valuation inputs

| Input class | Acceptable age | If older |
|---|---|---|
| Price, market cap | Per `core-finance-principles.md` freshness flags | "ไม่มีข้อมูลอัปเดต" |
| Share count, net debt, book value | Latest reported quarter | Flag it; check for a raise or buyback since |
| TTM earnings / FCF | Latest reported quarter | Stale beyond 2 quarters → stop condition |
| Risk-free rate | Within a few days | Re-pull; rates move enough to matter |
| Consensus estimates | Post-latest-earnings | Pre-earnings consensus after a guidance change is worse than no consensus |
| Peer multiples | Same pull date across all rows | Re-pull the whole row set, not one row |
