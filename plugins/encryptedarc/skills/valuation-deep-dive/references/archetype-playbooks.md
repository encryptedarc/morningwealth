# Archetype Playbooks

Read ONLY the playbook for the archetype you classified in STEP 0. Each one gives you: value driver → inputs to pull → steps → the trap that specifically kills this archetype → sanity check.

## Contents

| § | Archetype | Read when |
|---|---|---|
| 1 | Asset-light hypergrowth compounder | moat + future earnings power, low capital intensity |
| 2 | Capital-heavy asset owner | value sits in vessels / plants / PP&E |
| 3 | Concession / lease-heavy operator | recurring concession or contract cash flow, big lease liabilities |
| 4 | Cash-rich platform / ADR | large net cash + non-operating investment portfolio |
| 5 | High-growth SaaS / cloud | ARR / subscription revenue, FCF near breakeven |
| 6 | Deep-value / net-cash small cap | market cap near or below liquid balance sheet |
| 7 | Banks / financials | net interest income, loan book, regulatory capital |
| 8 | Commodity / cyclical producer | earnings swing with a price you don't control |
| 9 | REIT / infra fund / property fund | mandated distribution of stabilized cash flow |
| 10 | Holding company / conglomerate | value = sum of stakes, not consolidated P&L |
| 11 | Turnaround / pre-profit non-SaaS | negative earnings, path-to-breakeven is the thesis |
| 12 | Pre-revenue / pre-commercial | no revenue at all → mostly out of scope |

A company can straddle two archetypes (a bank with a big insurance arm; a cyclical that is also a holdco). When it does, value the pieces separately and add them — that is §10's method applied to a hybrid. Say explicitly that you did this.

---

## 1. Asset-light hypergrowth compounder

**Value driver:** durability of above-cost-of-capital returns — how long the moat keeps reinvestment earning excess returns.

**Pull:** revenue + growth (last 4-8 quarters), gross/operating margin trend, TTM FCF, capex/revenue, SBC, diluted shares, net cash, forward consensus revenue/EPS.

**Steps**
1. Reverse DCF first, not forward DCF. At a high multiple the useful question is not "what is it worth" but "what does today's price require, and is that achievable?" See `dcf-and-cost-of-capital.md` §3.
2. FCF yield on TTM and forward FCF. Deduct SBC — for asset-light names SBC is real dilution and excluding it flatters FCF badly.
3. P/E vs growth, but as a cross-check only. Note PEG's weakness out loud: it treats a 1-year growth rate as if it were permanent.
4. Scenario table (SKILL.md scenario section) because dispersion is the whole story.

**Trap:** balance-sheet tools. Net-Net / P/BV on a company whose value is intangible will scream "overvalued" at every price, forever. That output carries zero information.

**Sanity check:** if your DCF's terminal value is >75% of enterprise value, you did not do a DCF — you made an exit-multiple bet with extra steps. Say so and show the exit multiple you implicitly assumed.

---

## 2. Capital-heavy asset owner

(shipping, tankers, power plants, industrial plant, hotels holding their own real estate)

**Value driver:** replacement value of the asset base and the through-cycle spread between charter/tariff rates and operating cost.

**Pull:** EV bridge inputs (market cap, total debt, cash, minority interest), EBITDA, D&A, capex vs maintenance capex, book value of PP&E, fleet/asset list with age, contracted vs spot revenue split, ROE and ROIC, second-hand asset prices if available.

**Steps**
1. EV/EBITDA — the primary tool, because D&A on old assets makes P/E almost meaningless. Compare against the company's own history, not just peers.
2. P/BV against ROE. An asset owner earning ROE below its cost of equity deserves to trade below book; that is arithmetic, not sentiment. See `dcf-and-cost-of-capital.md` §5.
3. NAV / asset-based: market value of assets − net debt. If you cannot source second-hand asset values, say "ไม่มีข้อมูลอัปเดต" and lean on book value with the caveat stated.
4. DCF on the contracted portion only — contracted revenue is forecastable, spot is not. Do not run a 10-year DCF over spot rates and present it as a valuation.

**Trap:** Net-Net. Use the identity `NCAV = Equity − Non-current assets` to show it immediately: when the fleet dominates the balance sheet, NCAV is negative by construction. That is a statement about the accounting, not about value.

**Sanity check:** does EV/EBITDA sit inside the range this asset class trades at across the cycle? A trough multiple at peak rates and a peak multiple at trough rates are both traps.

---

## 3. Concession / lease-heavy operator

(out-of-home media, airport/retail concessions, leased-network operators)

**Value driver:** length and renewal odds of the concession, plus the cash flow after lease payments.

**Pull:** revenue by concession, EBITDA, EBIT, lease liability (current + non-current), lease payments in the cash flow statement, D&A split (asset vs right-of-use), concession expiry dates, occupancy/utilization.

**Steps**
1. Use **EV/EBIT**, or lease-adjusted EBITDA. Under TFRS 16 / IFRS 16 lease payments sit below EBITDA as D&A + interest, so raw EBITDA is inflated and raw EV/EBITDA looks artificially cheap. Also make sure lease liabilities are in your net-debt figure — if they are not, EV is understated too, which compounds the error.
2. FCF yield after actual lease cash outflow. This is the number that pays dividends.
3. P/E + growth as a cross-check once leases are handled consistently.
4. Concession expiry is a valuation input, not a footnote. A concession expiring in 3 years is a 3-year annuity plus a renewal option — value it that way and state your renewal probability as your own judgment.

**Trap:** quoting raw EV/EBITDA next to peers on a different lease-accounting basis. Either adjust all of them or use EV/EBIT for all of them. Mixing is the single most common error in this archetype.

**Sanity check:** EBITDA − lease payments − maintenance capex should be roughly recognizable as FCF. If it is not, find out why before you value anything.

---

## 4. Cash-rich platform / ADR

**Value driver:** the operating business, valued separately from the cash and investment pile — plus a discount for whatever structural overhang exists (ADR/VIE structure, regulatory regime, capital controls).

**Pull:** market cap, cash + short-term investments, long-term investment portfolio (fair value), total debt, GAAP net income, non-GAAP/adjusted net income, the reconciliation line items, share count (ADS ratio!), buyback authorization and actual execution.

**Steps**
1. Bridge market cap → EV explicitly. Show the arithmetic. `scripts/valuation.py net_cash_bridge` does it and prints the inputs.
2. Ex-cash P/E: `(market cap − net cash) ÷ adjusted net income`. This is the multiple you are actually paying for the business.
3. Use adjusted earnings. Fair-value gains and losses on an investment portfolio swing GAAP net income wildly and have nothing to do with operations — but list what you excluded, and note if the "adjustment" is recurring every quarter (then it is not one-off and should not be excluded).
4. Overhang discount: state it as an explicit percentage with your reasoning, and show valuation both with and without it. Do not bury a 30% haircut inside a discount rate where the user cannot see or argue with it.
5. Check the ADS-to-ordinary-share ratio before computing any per-share number. Getting this wrong scales your answer by 2x, 4x or 8x.

**Trap:** GAAP P/E, and treating a large investment portfolio as if it were cash. Illiquid strategic stakes are not cash — mark them down or exclude them and say which.

**Sanity check:** if ex-cash P/E is very low, ask why the market is not repricing it. Usually the answer is that the cash is not accessible to minority shareholders. If that is true, your net-cash add-back deserves a haircut.

---

## 5. High-growth SaaS / cloud

**Value driver:** ARR durability (net revenue retention) plus the credibility of the path from current margins to steady-state margins.

**Pull:** revenue + growth, ARR if disclosed, net revenue retention / churn, gross margin, FCF and FCF margin, SBC, capex (real for cloud/infra players — do not assume asset-light), diluted shares plus warrants/converts, net debt, Rule of 40 inputs.

**Steps**
1. EV/Revenue (or EV/ARR) plotted against growth, all on the same forward basis. Add a growth-adjusted ratio (multiple ÷ growth %).
2. EV/FCF once FCF is meaningfully positive. If FCF is near zero, say so rather than computing a 400x number and presenting it as a multiple.
3. Rule of 40 = revenue growth % + FCF margin %. State which margin you used. Running it on adjusted EBITDA while FCF is near zero produces a flattering number that misleads — if you use adjusted EBITDA, show FCF next to it.
4. Peer-calibrated exit multiple → scenario table → probability-weighted expected value. See `peer-calibration.md`.
5. Dilution: use fully diluted share count including warrants and convertibles. Cloud/infra names raise capital; a share count from two quarters ago understates it.

**Trap:** trailing P/E alone. Also: comparing a profitable name's sales multiple against loss-making peers without a quality adjustment penalizes the profitable one. `peer-calibration.md` handles this.

**Sanity check:** what steady-state FCF margin does your exit multiple imply, and has any company in this category actually achieved it? If not, the scenario is a Bull case, not a Base case.

---

## 6. Deep-value / net-cash small cap

**Value driver:** liquidation / balance-sheet value. This is the one archetype where Graham's tools genuinely apply.

**Pull:** current assets broken into cash / receivables / inventory, total liabilities (including off-balance-sheet and pension if disclosed), share count, insider ownership, cash burn rate, any related-party transactions.

**Steps**
1. `NCAV = Current assets − Total liabilities` (equivalently `Equity − Non-current assets`). Per share vs price.
2. NNWC (stricter): `Cash + 0.75×Receivables + 0.5×Inventory − Total liabilities`. Use this when inventory quality is doubtful.
3. Burn rate check: NCAV is a snapshot. A company burning cash is destroying your margin of safety every quarter — annualize the burn and show how long the NCAV lasts.
4. Governance check. Cheap-and-stays-cheap is usually about who controls the cash, not about the multiple. Note insider ownership and any history of value transfer to related parties.

**Trap:** DCF. When earnings are unstable or negative, a DCF here is a fabrication engine — every input is a guess. Don't.

**Sanity check:** is this a value trap? Ask what has to happen for the gap to close (buyback, special dividend, sale, activist). If you cannot name a mechanism, say so — that is the honest finding.

---

## 7. Banks / financials

**Value driver:** ROE relative to cost of equity, and the credibility of book value (i.e. whether provisions are adequate).

**Pull:** book value / total equity, tangible book value, net income, ROE and ROA, NIM, cost-to-income, credit cost (provision expense ÷ average loans), NPL ratio + coverage ratio, CET1 / capital adequacy ratio, loan growth, dividend per share and payout ratio, shares outstanding.

**Steps**
1. **P/BV against ROE.** This is the core. Compute justified P/BV = `(ROE − g) ÷ (COE − g)` and compare to the traded P/BV. The gap is the finding. (`scripts/valuation.py justified_pbv`.) Prefer tangible book (P/TBV) when goodwill is large.
2. Build COE from CAPM with a live, cited risk-free rate — see `dcf-and-cost-of-capital.md` §1. For a bank, COE is not a detail; it is half the answer.
3. **DDM** — banks are dividend machines and their payout is capital-constrained rather than opportunity-constrained. Gordon: `P = D1 ÷ (COE − g)`. Two-stage if payout is normalizing.
4. **Residual income** as the third leg: `Value = BV₀ + Σ (ROEt − COE) × BVt₋₁ ÷ (1+COE)^t`. It is the most honest bank model because it makes the ROE-vs-COE spread the explicit driver.
5. Credit cycle: current-year credit cost tells you where you are in the cycle, not what is normal. Show credit cost vs its own 5-year range. Under-provisioning inflates both earnings and book value, so a "cheap" P/BV built on a stale NPL book is not cheap.

**Trap:** **EV/EBITDA and FCF-based DCF are meaningless for banks.** Debt is raw material, not financing, so you cannot separate operating from financing cash flow, and EV has no coherent definition. If a user asks for a bank DCF, say plainly why it does not apply and offer DDM / residual income instead. Also: EBITDA is undefined in any useful sense when interest IS the revenue line.

**Sanity check:** ROE < COE mathematically implies P/BV < 1. If a bank earns 8% ROE with a 10% COE and trades at 1.3x book, the market is pricing a recovery in ROE — name it, and test whether it is plausible.

---

## 8. Commodity / cyclical producer

(oil & gas, refining, petrochem, cement, steel, shipping rates, paper, sugar)

**Value driver:** mid-cycle earnings power, not current earnings. You do not control the output price, so the current price level is an input you must normalize away.

**Pull:** revenue and EBITDA by segment for 5-10 years (a full cycle), the relevant spread/price benchmark (crack spread, GRM, polymer-naphtha spread, freight rate index), production volume, unit cash cost, capex, net debt, book value, and where the commodity price sits vs its own 5-10y range.

**Steps**
1. **Establish where you are in the cycle before valuing anything.** Put the current spread/price next to its 5-10 year range, cited. This single step prevents the classic error.
2. **Normalized / mid-cycle EPS** × a through-cycle P/E. Normalize by averaging margin or the spread across the cycle, holding current volume and capacity constant. (`scripts/valuation.py normalized_eps`.)
3. P/BV at trough as the downside anchor — cyclicals trade on book at the bottom, on earnings at the top.
4. EV/EBITDA at mid-cycle EBITDA, not at TTM EBITDA.
5. Replacement cost / EV per unit of capacity as an independent cross-check.
6. Balance sheet is a valuation input here: net debt / mid-cycle EBITDA determines whether the company survives to see the next up-cycle. A leveraged cyclical at trough is an option, not a value stock.

**Trap:** **trailing P/E at peak earnings.** This is the most reliable value trap in equities — the multiple is lowest exactly when earnings are about to fall. Whenever the user says a cyclical "looks cheap on P/E", check the cycle position first and push back if the low multiple is a peak-earnings artifact. The reverse also holds: an infinite or negative P/E at trough does not mean expensive.

**Sanity check:** what commodity price does the current market cap imply, and how does it compare to the forward curve or the long-run average? That framing is more useful than a point target.

---

## 9. REIT / infrastructure fund / property fund

**Value driver:** distributable cash flow per unit, priced against the risk-free alternative. These vehicles distribute most of their income by mandate, so they trade as spread instruments.

**Pull:** distribution per unit (last 4 quarters), NAV per unit and its date, occupancy, WALE (weighted average lease expiry), rental reversion, gearing/LTV, cost of debt and refinancing schedule, FFO/AFFO if disclosed, cap rate on the portfolio, and the 10-year government bond yield of the currency the distributions are paid in.

**Steps**
1. **Distribution yield spread** = distribution yield − 10y govt bond yield (TH govt bond for Thai funds, UST for US REITs). Compare that spread to its own history — the spread, not the yield, is the valuation signal. Rate moves reprice this archetype directly.
2. Price/NAV per unit. Note the NAV valuation date; property NAVs are appraised, often annually, and can be stale.
3. FFO / AFFO multiple. `FFO = Net income + D&A − gains on asset sales`; `AFFO = FFO − recurring maintenance capex`. AFFO is the one that supports distributions.
4. Cap rate: `NOI ÷ property value`. Compare to market cap rates for that asset class and location, and to the fund's cost of debt — a cap rate below the cost of debt means acquisitions destroy value.
5. Sustainability of the distribution: is it covered by AFFO, or topped up by asset sales, capital return, or a sponsor guarantee that expires? For Thai infra funds with a fixed concession life, the distribution is partly return *of* capital — a yield compared naively against a perpetual bond is misleading. Say so.

**Trap:** P/E and EPS. Heavy D&A on properties makes accounting earnings unrepresentative of cash. Also: comparing a finite-life fund's yield to a perpetual instrument's yield without adjusting for capital return.

**Sanity check:** does the distribution yield still look attractive if the 10y yield moves 100 bps? Show that sensitivity — for this archetype it is the dominant risk.

---

## 10. Holding company / conglomerate → SOTP

**Value driver:** the sum of the parts, minus what the holding structure costs you.

**Pull:** the full list of holdings with ownership percentage, which are listed (get market value) vs unlisted (need a valuation), holdco-level net debt and holdco-level opex, minority interests, dividend flow up from subsidiaries, and the historical range of the holdco discount if you can source it.

**Steps**
1. Value each material subsidiary on **its own** archetype — a holdco containing a bank and a cyclical needs §7 for one and §8 for the other. This is why SOTP belongs at the end of the playbook list.
2. For listed stakes use market value × ownership %. State the price date. For unlisted stakes use a peer multiple and label it as an estimate, not a fact.
3. Sum → subtract holdco net debt → subtract the capitalized value of holdco-level overhead → gross asset value.
4. **Holdco discount:** apply it explicitly as a percentage with a stated reason (minority control, tax on internal disposals, poor capital allocation history, opacity). Where possible, calibrate it against the company's own historical discount rather than picking a conventional number. Show the valuation before and after so the user can argue with the discount.
5. Report the discount the market currently applies vs the discount you think is fair. That comparison is the actual output.

**Trap:** valuing the consolidated income statement with a single multiple. Consolidation mixes businesses that deserve different multiples, and it includes revenue attributable to minorities that the holdco shareholder does not own. Also: double-counting — if a subsidiary's value already reflects its own debt, do not subtract that debt again at the holdco level.

**Sanity check:** does your SOTP sum to something close to the market cap plus a plausible discount? A 60% gap usually means a mis-sourced stake, a missed minority interest, or double-counted debt — check the arithmetic before you call it an opportunity.

---

## 11. Turnaround / pre-profit non-SaaS

**Value driver:** the probability and timing of reaching sustainable breakeven, and whether the balance sheet survives long enough to get there.

**Pull:** revenue trend, gross margin trend (the leading indicator), operating loss, cash burn per quarter, cash + undrawn facilities, debt maturities, covenants, dilution history, management's stated breakeven target.

**Steps**
1. Runway first: `cash ÷ quarterly burn`. If runway is short, the next financing — and its dilution — is the dominant valuation variable, ahead of any multiple.
2. EV/Sales against peers, with an explicit note that you are using it because earnings-based tools do not yet apply.
3. Build the path to breakeven as a scenario tree: what revenue and gross margin are needed, by when. Probability-weight it. The honest output is a wide range with the failure branch valued near the liquidation floor.
4. Downside anchor from §6 (NCAV / liquidation), so the Bear case has a floor rather than being a guess.

**Trap:** discounting a hockey-stick forecast at an ordinary WACC. If a plan has a 40% chance of failure, that belongs in the probability weights, not smuggled into the discount rate.

**Sanity check:** who funds the gap between here and breakeven, and at what price? If the answer is "an equity raise", your per-share numbers need the post-raise share count.

---

## 12. Pre-revenue / pre-commercial

No revenue means no multiple and no meaningful DCF. Say this plainly rather than producing a number.

What you *can* honestly do: describe the milestone structure (what event reprices this and when), the funding runway, and — for pharma specifically — note that rNPV with probability-of-success by phase is the standard method while stating that its inputs (peak sales, PoS, launch date) are assumptions, not sourced facts.

Treat a request to "value" one of these as a STOP condition: explain that any number would be an assumption chain, and offer the milestone/runway framing instead. That is more useful than false precision.
