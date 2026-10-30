---
name: earnings
description: "Use when a user asks to read, explain, or break down a listed company's quarterly or interim results (earnings release, 10-Q, 6-K, SET interim financial statements and MD&A) for US, Thai, or other markets, or invokes the command with a ticker such as `earnings GOOG` or `earnings PTT.BK Q2 2026`. Explains what changed in the quarter in plain language for a beginner. Do not use for full business-quality reviews, fair value or target-price work, price-only requests, or trade recommendations."
argument-hint: "<TICKER> [period, e.g. Q3 2026]"
---

# Earnings

Read the latest (or requested) quarterly results of a listed company and explain, in plain language for a beginner, what happened in the quarter, why it happened, and what to watch next. Do not issue buy or sell recommendations.

## Arguments

When invoked as a command, the arguments are a ticker and an optional period:

- `GOOG`, `MSFT`, `PTT.BK`, `PTT`, `CPALL.BK`
- `GOOG Q2 2026`, `PTT.BK 9M 2026`, `AAPL FY2026 Q4`

A `.BK` suffix means the Stock Exchange of Thailand (SET or mai). A bare ticker that is listed in more than one market, or that does not resolve to one company, needs one clarifying question before research. With no period, use the most recent reported quarter.

## Language

Respond in the language of the user's request. When the request contains only a ticker and period, use the language of the surrounding conversation, or English when there is none. Explain each specialist term in plain language the first time it appears, such as EPS, operating margin, FCF, guidance, or backlog, then use the term normally.

## Load before research

1. Read `references/source-policy.md` for the source hierarchy, freshness rules, citation format, and cross-verification rules.
2. Read `references/earnings-framework.md` for the market-specific documents, archetype metrics, quarter pitfalls, and output structure.

## Optional local extension

If `local/extension.md` exists in this skill directory, read it after the references and apply it. A local extension may set a default language, connect personal notes such as an investment thesis, or add a save step. It cannot override the source policy, the citation rules, or the no-recommendation rule.

## Scope boundaries

- Use this skill for one reporting period: results versus the prior year and prior quarter, versus guidance and consensus when sourced, plus cash flow, balance-sheet changes, and management commentary.
- For a multi-year review of business quality, moat, and capital allocation, use `fundamental`.
- For fair value, target price, cheap versus expensive, or DCF work, use `valuation-deep-dive`.
- Report the market reaction only with timestamped price data under the live-data rules. Do not explain a price move with a cause the evidence does not support.

## Workflow

### 1. Resolve the company and period

State the current date first. Confirm the company name, ticker, exchange, fiscal year-end, and the period to analyze.

- If the next report date has passed but the results cannot be found, say so and analyze the latest available quarter instead.
- If results were released within the last few days, the full quarterly filing may not be filed yet. Use the earnings release and say which filing is still pending.
- Fiscal quarters that do not match calendar quarters must be labelled with both, such as `FY2027 Q1 (quarter ended Sep 30 2026)`.

### 2. Gather the documents

Collect the documents listed for the company's market in `references/earnings-framework.md`. Prefer the filed statements, then the earnings release and presentation, then the earnings call. Record the publication date and fiscal period of each document.

Always look for the earnings call transcript or replay, or the analyst meeting for companies without a call. Read it using the earnings-call section of the framework, so the output reports what management said and what analysts pressed on, not only the numbers. If it is not accessible, say so.

### 3. Analyze

Classify the archetype, select the quarter metrics that fit it, and work through the sections of the output structure. For every material change, separate operating causes from accounting, one-off, FX, or share-count effects. Check every pitfall in the framework before writing.

### 4. Deliver

Use the output structure in `references/earnings-framework.md`, in Markdown in chat. Keep it as short as the quarter allows: a clean quarter needs fewer sections than a quarter with large one-offs.

## Evidence rules

- Cite every number with `[Source, publication date, fiscal period]` and state the currency, unit, and basis (reported or adjusted, consolidated or segment).
- Show the formula for every derived figure, including a Q4 derived from full-year minus nine months.
- Label management statements as `Management claim` or `Guidance`, and analysis as `Analysis/Inference`.
- Cite consensus only with its compiler and publisher, such as `LSEG consensus via Reuters`. If no consensus is verifiable, omit the beat or miss column rather than estimating it.
- If a figure cannot be verified in the current session, write `No verifiable data available` and list it under What I Don't Know.

## Quarter verdict

Judge the quarter, not the stock. Choose one:

- `Strong quarter`
- `Mixed quarter`
- `Weak quarter`
- `Insufficient data to assess`

A strong quarter can coincide with a falling share price, and a weak quarter with a rising one. Say which evidence drove the verdict.

End every analysis with an educational-only disclaimer in the user's language:

> This material is for educational purposes only and is not investment advice. Consult a licensed adviser before making investment decisions.
