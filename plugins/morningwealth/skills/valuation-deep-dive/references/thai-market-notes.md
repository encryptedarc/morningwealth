# Thai Market & Cross-Currency Notes

Read this for any SET/mai-listed name, any Thai infra or property fund, and any foreign holding being valued for a THB-based investor. These are the mechanics that change the number or change its interpretation — not general market colour.

## 1. Which price and which share class

- **Ticker convention:** `PTT.BK` style on international data providers; plain `PTT` on SET/Settrade. Confirm you are pulling the same instrument on both.
- **NVDR (Thai NVDR Co.) vs local shares vs foreign board.** Foreign investors typically hold NVDRs, which carry economic rights but no voting rights. The foreign board can trade at a premium to the local board when the foreign ownership limit is binding. If the two differ materially, state which price you are valuing against — a fair value derived from local-board pricing does not transfer to a foreign-board buyer at a premium.
- **Free float.** SET small and mid caps often have low float with a dominant family or state holder. Low float means the traded multiple is not a fair reflection of what a controlling stake is worth, and it caps the reliability of any peer comparison. Note float when it is below ~30%.
- **Ceiling / floor (±30%) and trading halts.** Relevant when discussing entry, not when computing value, but say so rather than implying a limit-up price is a clean market price.

## 2. Dividend yield as a primary valuation anchor

The Thai market is materially more yield-driven than the US. For mature SET names — banks, utilities, telcos, property, staples — the dividend yield relative to the Thai 10-year government bond is often a better-behaved valuation signal than P/E, because that is what the domestic institutional and retail bid actually prices.

- Pull the **10y Thai government bond yield** live (ThaiBMA or BOT) and cite it. Compute `dividend yield − 10y govt yield` and compare that spread to its own history.
- Use the **sustainable** payout, not the last 12 months if it included a special dividend. Check the payout ratio against earnings and against free cash flow.
- **XD date matters for the quoted price.** A price just after XD is mechanically lower by roughly the dividend. If you compare a post-XD price to a pre-XD dividend yield you will overstate the yield — check the XD date when the yield looks unusually attractive.
- Thai dividends are subject to withholding tax (10% for individuals under the standard option). Net vs gross yield changes cross-market yield comparisons — say which basis you used.

## 3. Peer comparison inside and outside Thailand

- SET multiples and US multiples are not interchangeable. See `peer-calibration.md` §4 — anchor to the market index first, then compare relatives.
- For a Thai name, prefer SET peers even if the fit is imperfect, and use foreign names for **business** comparison (margins, growth, unit economics) rather than for the multiple.
- Thai state-linked companies (PTT group, airports, utilities) carry policy risk on pricing and dividend policy that a foreign peer does not. That is a real valuation input — treat it as an explicit discount or as a scenario, not as a WACC nudge.

## 4. Currency — for a THB-based investor holding foreign assets

Keep the valuation and the currency view separate. Mixing them hides both.

1. **Value the company in its own reporting currency**, discounted at that currency's risk-free rate. A USD-earning company gets a USD risk-free rate; a THB-earning company gets the Thai one. This is the rule from `dcf-and-cost-of-capital.md` §1 and it is not optional — a THB discount rate on USD cash flows silently embeds an FX forecast.
2. **Then** convert the fair value at the spot rate, cited with its date, and report the THB figure alongside the local-currency figure.
3. State FX as a **separate return driver**: "fair value $X (upside Y% in USD); at THB Z.ZZ/USD [source, date] that is ฿W — a 5% THB appreciation removes roughly 5% of the THB return." Never bake an FX forecast into the cash flows or the discount rate; you would be making two bets and reporting one number.
4. For a company with revenue and costs in different currencies (Thai exporters, refiners buying USD crude and selling in THB), the FX exposure is inside the operating margin, not just in the translation. That belongs in the scenario levers.

## 5. Filings and data — Thai specifics

- **56-1 One Report** is the annual filing (replaced the old 56-1 + annual report split). It carries the shareholder structure, related-party transactions, and board detail.
- Quarterly financials and the MD&A come through SET's company pages and SETSMART; the company's IR page usually has the same PDFs, often faster.
- **ก.ล.ต. (SEC Thailand)** for filings, insider transaction reports (Form 59), and enforcement history.
- Thai reporting is under **TFRS**, largely converged with IFRS — so TFRS 16 leases apply, the same trap as IFRS 16 (`archetype-playbooks.md` §3).
- Thai fiscal years are usually calendar years, which makes SET-to-SET comparison easier than US comparison. Confirm rather than assume for companies with foreign parents.
- Consensus coverage on Thai small and mid caps is thin and sometimes a single broker. When you cite a consensus target for a SET small cap, say how many analysts it represents — a "consensus" of two is one person's opinion plus a rounding error.

## 6. Language and register for output

Thai prose, English domain terms untranslated: P/E, P/BV, EV/EBITDA, ROE, COE, DDM, FCF, NCAV, AFFO, cap rate, exit multiple, ticker symbols. Do not translate these into Thai — it reduces precision and the reader already thinks in the English terms.
