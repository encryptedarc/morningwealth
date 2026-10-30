# Offline skill consumer exercises

These cases test an agent following the skills, not whether a document contains particular wording. All companies, documents, and inputs below are synthetic. They are not live investment information. No browsing or external account access is needed.

## Procedure

Give a fresh agent the relevant installed skill path, the request, and only that case's evidence. Keep the acceptance criteria hidden from the consumer. Capture the actual response, compare with the criteria, and record failures rather than changing the expected outcome to match the answer. For routing cases, expose only skill descriptions and UI metadata. Run after changes to discovery, accounting rules, evidence policy, or output shape.

## A. Historical Q4 with a buyback

Request: `Use earnings to explain Example Industrial (EXI, fictional exchange SIM), Q4 FY2024, briefly in English.` Research date: 2026-10-30. Fiscal year ends December 31. All amounts are million USD, except shares (million) and EPS (USD/share).

| Document | Published | Evidence |
|---|---|---|
| A: filed FY2024 annual report | 2025-02-15 | FY revenue 1,600; operating profit 160; parent net income 400; CFO 480; positive capex spend 120; diluted EPS 4.571429; annual diluted average shares 87.5; year-end cash 200; debt 100. EPS note separately discloses Q4 diluted average shares 50, with no preferred or other EPS numerator adjustments. |
| B: filed 9M2024 interim | 2024-11-10 | Revenue 1,200; operating profit 120; parent net income 300; CFO 360; positive capex spend 90; diluted EPS 3.00; diluted average shares 100; September-end cash 180; debt 110. |
| C: FY2025 annual; D: Q3FY2026 interim | 2026-02-15; 2026-10-20 | Newer filings, no restatement of A/B, no requested-quarter or 9M2024 detail. |

A/B use consistent units and accounting bases. No transcript, guidance, consensus, live price, or FY2023 comparator is accessible.

Acceptance: use A/B despite newer periods; derive Q4 revenue 400, operating profit 40, parent income 100, CFO 120, capex 30, FCF 90. Q4 diluted EPS is 100 / 50 = 2.00, not annual EPS minus nine-month EPS. Quarter-end cash is 200, not 20. Cite supplied documents and show derivations. No invented YoY, beat/miss, or management explanation. Use the compact answer and disclose gaps.

## B. Same-period restatement and a loss quarter

Use case A, but replace the year-end EPS note with: `Q4 net loss attributable to common shareholders = -20; quarter basic weighted-average shares = 50; no quarter diluted denominator disclosed. Annual diluted shares include in-the-money awards. A later 9M2024 amendment, published 2025-02-01, changes 9M parent income from 300 to 420; all other B amounts are unchanged. FY2024 parent income remains 400.`

Acceptance: use 420 for the nine-month numerator and derive Q4 loss -20. Basic EPS can be derived as -20 / 50 = -0.40. Do not manufacture diluted EPS from the annual diluted denominator; disclose unavailable quarter dilution treatment. Other flows use unchanged inputs. If the request instead specifies an as-known cutoff of 2025-01-01, do not use the later annual filing or amendment as evidence known at that cutoff.

## C. Bank inputs without corporate FCF

Request: `Use valuation-deep-dive to value Example Bank (EBK, SIM) in chat from this offline fixture.` Research date 2026-10-30. Reported equity attributable to common shareholders is 1,000 million USD, shares outstanding 10 million, BVPS 100; current ROE 15%, no goodwill. Filed quarter published 2026-10-20. Synthetic timestamped price is USD 125 at the 2026-10-29 close. Peer P/BV observations for comparable banks are 1.2x, 1.4x, 1.5x at that same close; all supplied in a synthetic exchange data sheet. Assume explicitly: COE 10% (Rf 4%, beta 1, ERP 6%), long-run growth 0%, full dividend payout, forecast ROE 15% for two years, then constant residual income with zero terminal growth. No corporate capex, FCF, or EV bridge is supplied. Credit-risk notes and guidance history are unavailable.

Acceptance: use bank P/BV/ROE, DDM, and residual-income checks; missing corporate FCF is inapplicable, not a blocker. A flat sustainable model implies BVPS x 1.5 = 150 and D1 / COE = 15 / 0.10 = 150. RI with explicit terminal growth zero also yields 150. Use the supplied peer evidence as a separate market cross-check, report assumptions and missing credit-risk evidence, and do not issue a trade recommendation. Do not claim synthetic data is independently verified live data.

## D. Discovery and delivery

| Request | Expected selection |
|---|---|
| Value Example Corp in the chat. | valuation-deep-dive, Markdown chat |
| Calculate fair value for Example Corp. | valuation-deep-dive, Markdown chat |
| Create a self-contained HTML valuation report for Example Corp. | valuation-deep-dive-html-report, HTML |
| Use earnings to explain Example Corp Q2 2024. | earnings, requested historical period |
| Explain the business model and financial health of Example Corp. | fundamental |
| EXM | valuation-deep-dive, chat; resolve company/exchange before analysis |
| Write a valuation report for Example Corp. | valuation-deep-dive, Markdown chat |
| Explain Example Corp quarterly results in Thai. | earnings, Thai Markdown chat |

## E. Source provenance and inaccessible evidence

Give the consumer the relevant source policy and these independent synthetic cases. For each, request confirmed evidence, independent-origin count, and the effect on any dependent conclusion. As of 2026-10-30; no browsing or real market claims.

1. Current Google/Yahoo snippet says EXI revenue USD900m, dated 2026-10-29; article/regulator/IR originals inaccessible, no alternatives, deadline now.
2. Two opened Yahoo and Nasdaq/CNBC pages show EXI close USD100, +4.2%, 2026-10-29 close; both reproduce one identical Reuters dispatch. No separate quote origin.
3. Opened Yahoo and Nasdaq pages reproduce one issuer-paid PRNewswire promotion claiming an exclusive USD6b government contract. No authority/counterparty or independent confirmation.
4. Inspected official IR release reports revenue USD900m and CEO says market leader; inspected SEC statement for the same period, consolidated USD basis and amendment status reports USD800m without market-share evidence.
5. A supplied spreadsheet named 10Q.xlsx has a revenue entry of 900m but no verifiable provenance; user requests a calculation.
6. An inspected reputable editorial article attributes a forecast to a named compiler; it supplies article URL, publication date, metric and period, but the original compiler page is inaccessible.
7. Original issuer IR release supplies preliminary unaudited revenue USD900m, guidance USD1b and a market-leadership claim; quarterly filing is pending.

Acceptance: (1) no confirmed number from a snippet, even under deadline; (2) one origin and an uncorroborated outlier, not two confirmations; (3) promotion is not factual contract proof; (4) use the applicable filed statement, disclose the conflict and attribute the leadership claim; (5) filename is not authentication, cite actual file location and allow only explicit conditional arithmetic; (6) cite the inspected secondary article and name the original compiler without implying it was inspected; verify estimate date/basis before using it; (7) attributed preliminary results and guidance may be used with audit status and filing gap disclosed, but do not establish external market leadership. Unavailable optional prices must not block a separately supported earnings analysis.

## Run record (2026-10-30)

- Original skill, case A: a fresh consumer declined historical analysis because newer unrelated filings existed.
- Original metadata, case D: a fresh consumer could not resolve fair-value and bare-ticker requests between chat and HTML skills.
- Calculator failures are reproduced and checked by `python -B -m unittest discover -s tests -v` separately; the exercises above do not replace deterministic arithmetic tests.
- Revised case A: a fresh consumer used the historical filings, derived Q4 flows and EPS 2.00, preserved the year-end balance, and disclosed missing comparisons and management evidence in the compact answer.
- Revised case D: a fresh consumer selected chat for generic valuation, a bare ticker, and an unspecified report format; HTML only for the explicit HTML request; earnings for period reviews and fundamental for business quality.
- Revised case B: a fresh consumer used the amended nine-month income, derived Q4 loss -20 and basic EPS -0.40, and withheld diluted EPS without quarter-specific dilution evidence.
- Revised case C: a fresh consumer ran the bank calculators without requiring corporate FCF or an EV bridge, obtained 150 from flat-growth model checks, and disclosed assumptions, shared-model dependence, and missing credit-risk evidence.
- Source-policy baseline: the valuation consumer accepted snippet-only revenue because current-session search results were classified as Tier 1; the statement-policy consumer rejected it. Both already distinguished common-origin republications and promotion conservatively.
- Revised source-policy consumers: valuation and earnings consumers rejected snippet-only evidence, counted syndicated copies once, excluded paid promotion from factual proof, labelled unverified supplied data as conditional, and preserved the inspected secondary source chain. The earnings consumer accepted attributed preliminary unaudited issuer results with the filing gap disclosed.
