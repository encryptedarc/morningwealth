# Peer Mapping & Fair-Multiple Calibration

A peer comp is a comparison, not a measurement. It is easy to produce a table that looks quantitative and is in fact meaningless — wrong peers, mismatched bases, or a "regression" through four points. This file is about making the comparison honest enough to lean on.

## 1. Picking genuine comps

A real peer shares the **economics**, not the sector label. Test each candidate on: revenue model (subscription vs transactional vs cyclical), capital intensity, growth rate within roughly 2x of the subject, profitability regime (profitable vs pre-profit), and market/regulatory regime.

- 3-5 comps is the practical target. Fewer than 3 is an anecdote; more than 6 usually means you widened the definition until it stopped meaning anything.
- Say who you **excluded and why**. That sentence is often the most informative part of the table — "excluded X because it is pre-profit and Y because 60% of revenue is hardware" tells the reader more than the multiples do.
- Note the index/market each peer trades in. That matters — see §4.

## 2. Basis consistency — the rule that breaks most comp tables

**Never mix a multiple from one source with a metric from another.** Forward multiples are computed off a specific consensus estimate; taking the multiple from one provider and the revenue from another produces a number that corresponds to nothing.

Concretely, hold these constant across every row:

- **Forward vs trailing** — all forward or all trailing, never a mix.
- **Fiscal year vs calendar year** — a January fiscal year end vs a December one means "FY2027" spans different periods. Convert to calendar year, or label the mismatch.
- **Consensus vs company guidance** — pick one. Guidance is systematically more conservative in some sectors and more promotional in others.
- **Same source where possible**, same pull date for all rows, and cite it. If you must mix sources, say which row came from where.
- **Adjusted vs GAAP** — if the subject's earnings are adjusted, the peers' must be too, on comparable adjustments.
- **Lease accounting** — see `archetype-playbooks.md` §3. Either lease-adjust all rows or use EV/EBIT for all rows.
- **EV built the same way** for every row: include minority interest, preferred, and lease liabilities consistently, or exclude them consistently.

If you cannot get a consistent basis for a row, drop the row and say so. A four-row consistent table beats a six-row inconsistent one.

## 3. The honesty guard

State these out loud when they apply, because they change how much weight the table deserves:

- **n < 5 is not a regression.** Do not report an R², a fitted line, or a "peer-implied fair value" from a handful of points as if it were statistics. Describe the relationship qualitatively and show the points.
- **A sales multiple vs growth chart penalizes profitability.** A company generating cash gets marked down against loss-making peers growing faster, because the axis ignores the thing that makes it better. Add a quality adjustment: profitability (FCF margin, or Rule of 40 for software), balance sheet (net cash vs leveraged), capital intensity, and revenue quality (recurring vs one-off).
- **Peer multiples are not a fair value, they are a market opinion.** If the whole group is expensive, calibrating to the group reproduces the bubble. Cross-check the peer-implied value against an independent DCF and the scenario expected value — three methods disagreeing is information, not a problem to hide.
- **Survivorship.** Comps are the companies still listed. In a sector that has consolidated, the surviving multiple is upward-biased.

## 4. Cross-market comparisons

Do not map a SET-listed company directly onto US peers' multiples. Market-level multiples differ persistently for reasons that have nothing to do with the individual company: index composition, liquidity and free float, domestic institutional flows, the local risk-free rate, dividend culture and tax treatment, and governance regime.

If a cross-market comparison is the only option:

1. Show the market-level anchor for both markets (e.g. SET forward P/E vs S&P 500 forward P/E), sourced and dated.
2. Compare the company to its **own market's** multiple first (relative-to-index), then compare those relatives across markets.
3. State the discount as structural rather than as an opportunity, unless you can name the specific mechanism that would close it.

Same logic for a Thai company with foreign peers in the same industry: the industry comparison is informative about the business; the multiple comparison is mostly informative about the two markets.

## 5. From comps to a fair-value range

1. Tabulate the chosen multiple against its driver (growth for revenue multiples, ROE for P/BV, AFFO yield for REITs) on a consistent basis, plus a growth-adjusted column (multiple ÷ growth %).
2. Locate the subject in the table and form a **fair multiple range**, not a point — typically the interquartile band of quality-adjusted peers, widened or narrowed with a stated reason.
3. Apply the range to the subject's own forward metric → a fair value range.
4. **Triangulate:** peer-implied range vs independent DCF vs scenario expected value. Report the center and the range. Where the three methods disagree, say which one you trust most for this archetype and why.
5. Never report a single number as "the fair value". A point target implies a precision the inputs do not contain, and it invites the user to trade on it. A range with the dominant lever named is the deliverable.

## 6. Reporting template

```
| Company | EV/Rev (fwd) | Rev growth | Mult ÷ growth | FCF margin | Net cash/(debt) |
|---|---|---|---|---|---|
```

Below the table, always: the pull date and source, which rows were adjusted and how, who was excluded and why, and one sentence on what the table does **not** capture.
