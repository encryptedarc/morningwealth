# DCF, Cost of Capital, and the Equity-Model Family

The discount rate is the single largest lever in any present-value model, and it is the one most often invented. A DCF built on a guessed WACC is a fabricated number wearing a spreadsheet — it violates the same principle as quoting an unsourced price, just less visibly. So the rule is: **every component of the discount rate is either sourced and cited, or declared as an assumption in the open where the user can change it.** Nothing in between.

## 1. Cost of equity and WACC

```
COE  = Rf + β × ERP        (+ CRP for an emerging market, if not already inside ERP)
WACC = (E/V) × COE + (D/V) × Rd × (1 − tax rate)
```

**Where each input comes from:**

| Input | Source discipline |
|---|---|
| `Rf` risk-free | **Search it live and cite it.** 10y UST for USD cash flows; 10y Thai government bond (ThaiBMA / BOT) for THB cash flows. Match the currency of the cash flows, always. Treat it like a price quote: source + date + freshness flag. |
| `β` beta | Pull a published beta (stockanalysis, Yahoo, Bloomberg) and cite it, or use a sector beta. Say which. Raw 5-year betas on small caps are noisy — when β looks implausible (>2.5 or <0.3 for an ordinary operating company), use a sector beta and say why. |
| `ERP` equity risk premium | An **assumption**. State the number and where it comes from — Damodaran's published country ERP tables (`pages.stern.nyu.edu/~adamodar`) are the usual citable anchor. Do not silently use 5% or 6%; write it down. |
| `CRP` country risk | Only if your ERP is a mature-market number. Thailand carries a country premium over the US; do not apply a US ERP to a SET name without saying so. |
| `Rd` cost of debt | Effective rate from the filings (`interest expense ÷ average total debt`) or the company's stated coupon. Cite it. |
| `tax rate` | Statutory rate (Thailand 20%, US federal 21% + state) or the effective rate from the filing. Say which and why. |

**Report the discount rate as a range, not a point.** A ±100 bps band on COE is honest and its effect on the answer is usually larger than the effect of a whole year of revenue growth. Show the fair value at the low, mid, and high end of that band. If a 100 bps move in WACC flips your verdict from cheap to expensive, the honest finding is "this is not resolvable by DCF at today's price" — say that instead of picking a point.

**Never solve backwards for the discount rate** to reach a conclusion you already wanted, and never bury a qualitative haircut (regulatory risk, governance, illiquidity) inside WACC. Haircuts belong as a visible, separate, arguable percentage — see `archetype-playbooks.md` §4 and §10.

## 2. Building the DCF

Match the cash flow to the discount rate. Mixing them is the most common structural error in the model:

```
FCFF = EBIT × (1 − t) + D&A − Capex − ΔNWC     → discount at WACC   → gives ENTERPRISE value
FCFE = Net income + D&A − Capex − ΔNWC + Net borrowing
                                               → discount at COE    → gives EQUITY value
```

- Discounting FCFF at WACC gives EV. **Then** bridge: `equity value = EV − total debt + cash (− minority interest − preferred)`. Show that bridge.
- Discounting FCFE at COE already gives equity value — do **not** add cash back or subtract debt again. Doing both double-counts the balance sheet, and the error is large.
- Deduct SBC from FCF for names where it is material. Treating SBC as non-cash while using diluted shares from two years ago understates dilution twice.
- Forecast horizon: 5 years is the default; 10 only when the business has contracted or regulated visibility that far out (see §2 of the playbooks). A 10-year explicit forecast on a business you cannot forecast for 2 years is false precision — the extra years add noise, not information.
- Mid-year discounting vs year-end changes the answer by a couple of percent. Pick one, say which, and don't pretend that choice is precision.

## 3. Reverse DCF — the honest tool for an expensive stock

For a high-multiple name, "what is it worth?" invites a made-up answer, because the output is dominated by inputs nobody can source. **"What does today's price already require?"** is answerable and falsifiable. That reframing is the whole value of this method: you stop defending a target price and start testing a claim.

**Method**
1. Take the current EV as given (bridge from market cap — show it).
2. Fix everything except growth: WACC (from §1, cited), steady-state margin, capex/revenue, forecast horizon, terminal growth.
3. Solve for the revenue (or FCF) CAGR over the forecast horizon that makes PV = current EV. Use `scripts/valuation.py reverse_dcf` rather than iterating in your head.
4. **Judge that implied growth against evidence:** the company's own last 3-5 years, consensus for the next 2, the addressable market size (does the implied revenue exceed a plausible share of it?), and — the strongest test — how many companies have historically sustained that rate for that long.
5. Repeat once holding growth at consensus and solving for the **margin** instead. Whichever variable needs the more heroic value is the one carrying the market's optimism. Name it.

**Output shape:** "ราคาปัจจุบัน imply revenue CAGR X% ต่อ 5 ปี ที่ steady-state FCF margin Y% — เทียบกับ 3 ปีที่ผ่านมาทำได้ Z% [source, date]" then your judgment on whether that is plausible. That is more useful than any point target, and it cannot be fabricated without being visible.

## 4. Terminal value sanity checks

Terminal value usually dominates a DCF, which means the "10-year forecast" is mostly theatre around one assumption. Handle it explicitly:

- **Terminal growth `g` ≤ the risk-free rate**, and never above long-run nominal GDP of the company's market. A perpetual growth rate above nominal GDP means the company eventually becomes the whole economy. If you need g > Rf to justify the price, you have found your answer.
- `TV = FCF_n × (1 + g) ÷ (WACC − g)`. This is hypersensitive when `WACC − g` is small: WACC 8% with g 4% puts the multiplier at 25x; g 5% takes it to 33x. Show the TV sensitivity to g, always.
- **The 75% rule:** compute `TV ÷ EV`. Above ~75%, state plainly that the valuation is an exit-multiple bet rather than a cash-flow valuation, and show what exit EV/EBITDA or EV/FCF multiple your terminal value implies. Then sanity-check *that* multiple against peers (`peer-calibration.md`). This converts a hidden assumption into a checkable one.
- Cross-check the perpetuity TV against an exit-multiple TV. If they disagree by more than ~25%, one of the two assumptions is out of line — resolve it before reporting.
- Terminal ROIC should not exceed the current ROIC by much. Perpetual growth at excess returns assumes the moat lasts forever, which is the strongest claim in the model and deserves to be stated as such.

## 5. The equity-model family — for banks, insurers, and dividend-constrained businesses

FCF-based DCF does not work when debt is raw material rather than financing (see `archetype-playbooks.md` §7). Use these instead:

**Justified P/BV (Gordon-growth form)**

```
justified P/BV = (ROE − g) ÷ (COE − g)
```

The mechanism worth stating out loud: value relative to book is driven by the **spread between ROE and COE**, so ROE = COE implies P/BV = 1 exactly, and ROE < COE implies a discount to book as arithmetic rather than pessimism. When a bank earning below its COE trades above book, the market is pricing an ROE recovery — identify it and test it, rather than calling the stock expensive.

Use tangible book (P/TBV) when goodwill is a large share of equity, since goodwill does not generate the ROE.

**Dividend discount model**

```
single stage:  P = D₁ ÷ (COE − g)
two stage:     PV of forecast dividends + terminal PV using the stage-2 payout and g
```

Appropriate when payout is stable and capital-constrained. Sanity-check that the implied payout is consistent with the retention needed to fund `g`: `g ≈ ROE × (1 − payout)`. If your g and payout violate that identity, the model is internally inconsistent — a very common and invisible error.

**Residual income**

```
Value = BV₀ + Σ [ (ROEt − COE) × BVt₋₁ ] ÷ (1 + COE)^t
```

The most transparent bank model, because the value above book is *explicitly* the excess-return stream. It also degrades gracefully: get the forecast wrong and you still anchor on book value, whereas a wrong DCF can produce any number at all.

## 6. Failure modes to check before you report

Run through these — each one has produced confidently wrong valuations:

1. FCFE discounted at WACC, or the debt/cash bridge applied twice.
2. Terminal `g` above the risk-free rate, or above nominal GDP.
3. Discount rate with no cited risk-free rate.
4. Share count that predates the latest raise, or an ADS-vs-ordinary-share mix-up.
5. Nominal cash flows discounted at a real rate (or the reverse) — pick one basis and hold it.
6. Cash flows in one currency discounted at another currency's rate. See `thai-market-notes.md` §4.
7. A qualitative risk applied twice — once as a WACC bump and once as a probability weight.
8. Arithmetic done in prose. Multi-step present-value math belongs in `scripts/valuation.py`, with the inputs printed so the user can re-run it.
