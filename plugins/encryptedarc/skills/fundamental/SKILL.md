---
name: fundamental
description: "Use when a user asks, in English or another language, for a beginner-friendly fundamental analysis of a listed company, including its business model, revenue quality, financial health, moat, management execution, capital allocation, or fundamental risks. Do not use for price-only requests, news-only requests, short-term trading, portfolio allocation, or fair value or target-price work."
---

# Fundamental

Analyze the business quality and financial condition of a listed company for a beginner. Explain the evidence in clear English so the user understands how the company makes money, how strong its fundamentals are, and what to investigate next. Do not issue buy or sell recommendations.

## Load before research

1. Read `references/source-policy.md` for the source hierarchy, freshness rules, citation requirements, and cross-verification rules that distinguish filing data from live market data.
2. Read `references/fundamental-framework.md` to select metrics by business archetype and apply the output structure and scoring rubric.

## Scope boundaries

- Use this skill for business models, customers, revenue quality, financial health, moats, growth options, management execution, capital allocation, and fundamental risks.
- Do not use it for requests focused on news, catalysts, price action, macroeconomics, or short-term trading theses.
- If the request asks for fair value, a target price, whether the stock is cheap or expensive, a DCF, or another valuation method, use `valuation-deep-dive`.
- Mention valuation context only when it is necessary to explain a risk and current, citable data is available. Do not derive fair value or a purchase entry point with this skill.

## Workflow

### 1. Resolve the company

State the current date first. Confirm the company name, ticker, and exchange. If the name is ambiguous or the ticker exists on multiple exchanges, ask one clarifying question before researching.

Use these defaults when the user does not specify them:

- Data horizon: the latest three annual periods plus the latest quarter or interim period compared year over year
- Output: Markdown in chat
- Language: clear English
- Audience: a beginner seeking to understand the fundamentals, not a trade setup

### 2. Classify before choosing metrics

Classify the company under at least one archetype before analyzing it: general corporate, bank, insurer, REIT or property fund, cyclical or commodity, SaaS or subscription, or pre-profit or high-growth. Use only the suitable metrics from `references/fundamental-framework.md`.

Do not force FCF, ROIC, debt, or P/E into every business model. Omit an unsuitable metric and briefly explain why it does not apply.

### 3. Research primary sources first

Use this evidence order:

1. Latest annual filing: 10-K, 20-F, annual report, or 56-1 One Report
2. Latest quarterly or interim filing: 10-Q, 6-K, financial statements, and MD&A
3. Earnings presentations and earnings calls for guidance, strategy, and management claims
4. Company IR disclosures and verifiable news for events after the reporting period

Investor presentations and earnings calls are management statements, not independent evidence. Reconcile headline numbers with filed financial statements before using them. If a transcript, segment disclosure, or customer-concentration figure is unavailable, say that no verifiable data is available.

### 4. Keep the evidence register explicit

- Cite every number and material factual claim with its source and publication date. Add the fiscal period when the claim relates to financial statements or operating results.
- State the currency, unit, and basis, such as reported or adjusted, consolidated or segment, and annual or quarterly.
- Show the formula for every calculated figure and distinguish derived figures from sourced figures.
- Separate `Fact`, `Management claim`, and `Analysis/Inference`.
- Do not say that the market has not "priced in" an option without valuation evidence. Use "not yet material in reported results" or "still a management target" when that is what the evidence supports.
- If the evidence is insufficient, do not guess a score. Use `N/A — insufficient data`.

### 5. Analyze, then deliver

Use the eight-part structure in `references/fundamental-framework.md`. Omit immaterial sections when appropriate, but always include Data as of, Financial Trend, Risks, Scorecard, What I Don't Know, and Final Verdict.

Define specialized terms in plain English the first time they appear. Use standard technical terms such as revenue, margin, FCF, ROIC, NIM, and AFFO normally.

## Verdict rules

Choose one evidence-based verdict:

- `Strong fundamentals`
- `Good fundamentals with material watchpoints`
- `Weak fundamentals`
- `Insufficient data to assess`

Keep company quality separate from stock-price attractiveness. A good company can be an expensive stock, and a cheap stock can represent a weak business.

End every analysis with:

> This material is for educational purposes only and is not investment advice. Consult a licensed adviser before making investment decisions.
