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

## F. Company-first discovery, citation, and verification

Request: `Explain this company's quarter using the best sources and compare with other reliable sources.` Use synthetic documents and all relevant installed skill instructions; do not show the consumer these acceptance criteria.

| Case | Evidence |
|---|---|
| Same release, two hosts | Verified company IR and SEC Exhibit 99.1 both expose the identical same-date issuer release, same period/units/basis; a reputable article quotes the company figures. |
| Later amendment | IR has the initial release with revenue 900m; a later same-period full amended statement is accessible only on SEC and reports 800m on the same metric/basis. |
| Blocked IR | Company IR cannot be inspected, but the SEC issuer-release copy and reputable independent reporting are accessible. |
| Release only | A verified original preliminary unaudited issuer release is available; no filing yet and no credible secondary reporting accessible. |

Acceptance: start company-disclosure discovery at verified IR and prefer its inspected URL for the identical document/version. Actively inspect regulator/exchange records and independent reporting where available and record actual matches/limits. Identical IR/SEC copies remain one issuer origin and do not change audit status. Prefer the applicable amended 800m statement over the old IR release; disclose the discrepancy. Use and cite inspected SEC content when IR is blocked, stating the fallback. A sound preliminary issuer release remains usable with status and unavailable verification disclosed; do not invent independent confirmation or demand that every company-account figure have a second independent origin. Macro and price data continue to use their own data owners.

Live motivating example supplied by the user: [Amazon IR release](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/) and [SEC Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20260930xex991.htm). Both were opened on 2026-10-30; title, release date, period and the inspected headline figures matched. This is a same-issuer document comparison, not independent validation of the underlying results. No live company figures are needed in the synthetic exercise.

## G. Quarter records, statement versions and reusable topics

Give a fresh consumer the installed earnings skill and only these synthetic inputs. Request in Thai: `Use earnings to analyze Example Industrial (SIM:EXI), FY2026 Q2.` Research date: 2026-10-30; fiscal year-end December 31; requested quarter ended June 30. In the saved-artifact variant, explicitly authorize a complete Markdown record in a temporary report directory. Place an existing file named `Earnings_SIM-EXI_FY2026-Q2_2026-10-30.md` there with sentinel text and record its hash. Preserve all input files.

| Input | Inspected synthetic evidence |
|---|---|
| Prior FY2026 Q1 record, as of May 1 | Revenue 100 USDm. Original formal Q2 revenue guidance 100–110 USDm, issued April 30 by CFO Dana; issuer URL `https://example.invalid/ir/q1-2026`. CEO Sam aims to launch Orion in FY2028 subject to regulatory approval, call 08:10. Open question: operating cash flow versus investment and funding. The prior record supplies historical evidence; Q1 originals are not separately inspected in this exercise. |
| Q2 issuer release, July 30 | `https://example.invalid/ir/q2-2026`: consolidated reported revenue 106, operating income 12, net income attributable to common shareholders 8, CFO 15, positive capex spend 5, all USDm; diluted shares 10m, diluted EPS USD0.80; quarter-end cash 30 and debt 10 USDm. Unaudited; no full statements, footnotes, YoY or consensus. New formal Q3 guidance: revenue 120–140, operating income 8–12 USDm; no issued operating-margin target. |
| Regulator mirror, July 30 | `https://example.invalid/regulator/q2-2026`: identical to the issuer release, one issuer origin. Independent editorial coverage unavailable. |
| Guidance update, July 15 | `https://example.invalid/ir/update-2026-07-15`: revised Q2 revenue guidance 108–112 USDm; a forecast revision, not a restatement. |
| Official Q2 transcript, July 30 | `https://example.invalid/ir/call-q2-2026`: CEO Sam at 08:10 repeats the FY2028 Orion aim subject to approval. Analyst Lee of Aster asks CFO Dana at 12:30 about investment funding; CFO expects operating cash flow subject to demand/working capital and may use debt. At 15:00 CFO expressly declines to issue an operating-margin target. |

Acceptance: the default is a detailed headed/bulleted report with a short lead. Inspect the actual saved Markdown, not only the agent's final summary. Original Q2 guidance and July revision retain dates, basis and sources; actual revenue is within the original range but below the revision. FY2028 is not yet due. Q3 midpoint ratio, if shown, is `Derived`: ((8 + 12) / 2) / ((120 + 140) / 2) x 100 = 7.6923%, not formal margin guidance. Keep speaker/role, question, source location, funding conditions and unresolved next check. Distinguish current inspected evidence from the historical prior record. Topic blocks retain company/period, unit/basis, statement type, exact linked source and caveats when extracted individually. Preserve the prior input and sentinel file hashes; create a new record/revision in the authorized directory and return its actual path. Do not generate an image or claim a published release.

Missing-input variant: give only the Q2 issuer release, with no prior record, no accessible call, no regulator/independent coverage, no destination or save request. An unattributed social summary alleges guaranteed no-debt funding and a margin target. Request detailed Thai headings/bullets for later infographic reuse. Acceptance: disclose baseline, Q&A and verification gaps; do not reconstruct an exchange, authenticate social claims, infer missing guidance or save a file. Continue with usable issuer results/guidance, clear topic metadata and an explicit unsaved status. An explicit brief request may condense chat without claiming a complete persistent archive.

## H. Call discovery, full versus partial coverage, and transcription conflicts

Live discovery regression: give a fresh consumer only the installed earnings skill, research date 2026-10-30 and request `earnings AMZN Q3 2026; detailed prepared remarks, guidance and analyst Q&A in Thai`. The company IR release may be supplied as a starting point; do not supply transcript URLs or acceptance criteria. Inspect the actual response and which pages/sections were read. The following links record motivating evidence, not a fixed provider whitelist: [company release](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/), [official webcast announcement](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-to-Webcast-Third-Quarter-2026-Financial-Results-Conference-Call/), [Quartr transcript carried by Stock Analysis](https://stockanalysis.com/stocks/amzn/transcripts/720308-q3-2026/), and [Benzinga transcript](https://www.benzinga.com/news/26/10/62724825/amazoncom-q3-2026-earnings-call-transcript).

Acceptance: discover and inspect call content rather than stop at a release or player shell; match the quarter/call date, preserve publisher/provider attribution, and cover prepared remarks and later Q&A through closing. Summarize all material distinct topics within copyright limits, including explicit absence of an AWS margin target, external/internal chip economics and funding confidence without inventing a debt-free funding guarantee. Preserve written formal guidance and distinguish it from outlooks and calculations. Disclose full/partial text and whether audio was actually reviewed. Do not infer the Facebook author's exact source merely from matching content. The actual call's caller exchanges can be combined/split into different topical counts in a recap.

Offline coverage/conflict variants (all sources fictional): Vela Industrial (VEL, SIM), FY2026 Q2 ended June 30; fiscal year-end Dec31. Research date 2026-10-30. Source A is a verified IR release dated July30, `https://example.invalid/vela/ir/q2-2026`: consolidated reported revenue106 and operating income12 USDm; formal Q3 revenue guidance120–140 and operating income8–12 USDm; no operating-margin target. Source B, matching official event page, exposes only an unreadable linked player and no official transcript. Source C, `https://example.invalid/aggregator/vela/call-q2`, identifies Quartr and matches issuer/date/participants but exposes only an excerpt despite a Full Transcript title: CEO Sam aims for OrionFY2028 subject to regulatory approval at08:10; CFO Dana answers Lee/Aster at12:30 with conditional operating-cash-flow funding and possible debt; then text cuts off before the next question.

- Full-transcript variant: source D, `https://example.invalid/publisher/vela/call-q2`, is an inspected full Meridian Financial News transcript from its own service, matching issuer/date/participants. It contains the same prepared remarks/funding exchange, Kim/Beacon asking about margin at18:00 with CFO explicitly refusing a target, Jo/Cedar asking at25:00 about external chip sales versus cloud use with CEO explaining earlier sale revenue versus useful-life cloud cash flows, and operator closing at26:00. CFO's spoken-guidance transcription says operating income8–7 USDm, conflicting with written8–12. Acceptance: use attributed transcript content with provider provenance, cover the later questions, disclose the numeric discrepancy and use written formal guidance on its matching basis. Do not treat multiple transcripts as independent proof of management economics.
- Partial-only variant: only A/B/C are accessible, all other text/provider routes and original audio are unavailable. Acceptance: report partial remarks/Q&A and the missing remainder, not Full text read or a reconstructed complete call. Keep A's guidance, C's actually inspected evidence and conditions; do not leak source D's late questions from the other variant. Disclose missing baseline/persistence. No browsing or file save in these synthetic variants.

## Run record (2026-10-30)

- Call-discovery baseline on the current standalone skill: a fresh web consumer found the full Quartr/Stock Analysis transcript without a supplied transcript URL, read prepared remarks and all caller exchanges, and retained official release guidance. The reported omission was not reproduced in this fresh run; no claim is made that the earlier skill was incapable of retrieval or that the user's previous runtime selection is known. Add explicit retrieval/coverage/provenance checks to make incomplete runs visible. Cached published plugin content still uses the earlier compact default and differs from the local standalone update; do not rewrite its published cache in place.
- Revised live discovery: a fresh consumer found the transcript without a supplied transcript link, covered remarks and every caller exchange through closing, and disclosed the unreadable official player/unreviewed audio. Comparing publisher transcripts exposed a growth-number discrepancy resolved for written expectations against IR and a speaker-attribution difference left uncertain. The actual output retained management outlooks and funding limitations with exact source links.
- Revised offline coverage variants: the consumer used the full identified-provider transcript in variant1, included later margin/chip questions, preserved conditional funding, and disclosed the numeric transcription conflict while retaining written guidance. Variant2 reported partial coverage and the missing remainder, retained release guidance and inspected remarks/Q&A, and did not import variant1's inaccessible late exchanges. No fabricated transcript/audio access or saved-record claim.

- Quarter-record baseline: the previous skill already compared original and revised guidance correctly and preserved management qualifications. Its actual saved report used five compact primary sections, combined prepared remarks/Q&A, mostly prose paragraphs, and detached reference definitions; extracting a topic alone lost its exact source link and other local context. The change addresses default structure and durable/reusable records rather than claiming the baseline made an accounting error.
- Revised case G saved-artifact consumer: produced a detailed Thai report with separate guidance versions, prepared remarks and Q&A, inline sources, conditional funding and an explicit refusal to issue margin guidance. It assessed original/revised ranges separately, kept the FY2028 milestone not yet due, and used `No comparable actual` for already-ended Q3 without results. It saved `_v2`; prior-input and existing-output hashes were unchanged.
- Initial missing-input consumer: correctly rejected unattributed social claims, disclosed absent baseline/call/verification and did not save, but still used detached reference definitions. Added a concrete topic template and inline Source bullet. A fresh brief cash-flow/guidance consumer then retained company/period, units, statement types, caveats and exact local evidence links in each material topic, with missing-data and unsaved status explicit.

- Original skill, case A: a fresh consumer declined historical analysis because newer unrelated filings existed.
- Original metadata, case D: a fresh consumer could not resolve fair-value and bare-ticker requests between chat and HTML skills.
- Calculator failures are reproduced and checked by `python -B -m unittest discover -s tests -v` separately; the exercises above do not replace deterministic arithmetic tests.
- Revised case A: a fresh consumer used the historical filings, derived Q4 flows and EPS 2.00, preserved the year-end balance, and disclosed missing comparisons and management evidence in the compact answer.
- Revised case D: a fresh consumer selected chat for generic valuation, a bare ticker, and an unspecified report format; HTML only for the explicit HTML request; earnings for period reviews and fundamental for business quality.
- Revised case B: a fresh consumer used the amended nine-month income, derived Q4 loss -20 and basic EPS -0.40, and withheld diluted EPS without quarter-specific dilution evidence.
- Revised case C: a fresh consumer ran the bank calculators without requiring corporate FCF or an EV bridge, obtained 150 from flat-growth model checks, and disclosed assumptions, shared-model dependence, and missing credit-risk evidence.
- Source-policy baseline: the valuation consumer accepted snippet-only revenue because current-session search results were classified as Tier 1; the statement-policy consumer rejected it. Both already distinguished common-origin republications and promotion conservatively.
- Revised source-policy consumers: valuation and earnings consumers rejected snippet-only evidence, counted syndicated copies once, excluded paid promotion from factual proof, labelled unverified supplied data as conditional, and preserved the inspected secondary source chain. The earnings consumer accepted attributed preliminary unaudited issuer results with the filing gap disclosed.
- Company-first baseline (v1.2.2): a fresh consumer selected SEC first for an identical IR/SEC earnings release under both statement and valuation rules, while correctly retaining amendment/fallback behavior.
- Revised company-first consumers: statement and valuation consumers chose IR discovery/citation for matching releases, preferred a later SEC-only amendment over stale IR, disclosed inspected SEC fallbacks, and kept release-only analysis usable with verification limits. The valuation consumer retained exchange/central-bank sources for current quotes and rates instead of old values on IR. Consumers did not invent successful comparisons when only source availability was given.
