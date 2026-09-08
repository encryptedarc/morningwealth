#!/usr/bin/env python3
"""
valuation.py — calculation helpers for the valuation-deep-dive skill.

Why this exists: source discipline stops you fabricating an input, but it does
nothing about arithmetic done in prose. Multi-step present-value and scenario
math is exactly where a confident wrong number comes from, and the error is
invisible in the output. So: run the math here, and paste the block it prints.

Every command echoes its inputs before the result, so the user can re-run or
argue with any single assumption. That is the point — the printed input block
is part of the deliverable, not debug noise.

Pure stdlib. Python 3.8+.

Usage:
    python3 valuation.py <command> [args]
    python3 valuation.py --help
    python3 valuation.py selftest

Commands:
    wacc              cost of equity (CAPM) and WACC
    bridge            market cap <-> enterprise value, net cash/debt
    ncav              NCAV / NNWC per share (Graham, deep value only)
    dcf               DCF from an explicit FCF forecast + terminal value
    reverse-dcf       solve for the growth today's price already requires
    scenario          bear/base/bull implied price + probability-weighted EV
    justified-pbv     justified P/BV from ROE, g, COE  (banks, asset owners)
    ddm               dividend discount model + retention-consistency check
    residual-income   residual income valuation (banks)
    normalized-eps    mid-cycle EPS for cyclicals + through-cycle fair value
"""

import argparse
import sys

# ---------------------------------------------------------------- formatting


def _fmt(x, dp=2):
    if x is None:
        return "n/a"
    if isinstance(x, str):
        return x
    if abs(x) >= 1000:
        return f"{x:,.{dp}f}"
    return f"{x:.{dp}f}"


def _pct(x, dp=2):
    return "n/a" if x is None else f"{x * 100:.{dp}f}%"


def _block(title, rows):
    print(f"\n{title}")
    print("-" * max(len(title), 44))
    width = max((len(k) for k, _ in rows), default=0)
    for k, v in rows:
        print(f"  {k.ljust(width)} : {v}")


def _warn(msg):
    print(f"  [!] {msg}")


# ---------------------------------------------------------------- core maths


def cost_of_equity(rf, beta, erp, crp=0.0):
    """CAPM. crp = extra country risk premium, only if erp is a mature-market number."""
    return rf + beta * erp + crp


def wacc(coe, equity_value, debt_value, cost_of_debt, tax_rate):
    v = equity_value + debt_value
    if v <= 0:
        raise ValueError("equity + debt must be positive")
    we, wd = equity_value / v, debt_value / v
    return we * coe + wd * cost_of_debt * (1 - tax_rate), we, wd


def net_cash_bridge(market_cap, total_debt, cash, minority=0.0, preferred=0.0):
    """EV = mkt cap + debt + minority + preferred - cash. Returns (ev, net_cash)."""
    ev = market_cap + total_debt + minority + preferred - cash
    return ev, cash - total_debt


def pv_of_flows(flows, rate):
    return sum(f / (1 + rate) ** (t + 1) for t, f in enumerate(flows))


def terminal_value(last_flow, rate, g):
    if rate <= g:
        raise ValueError(f"discount rate ({rate}) must exceed terminal growth ({g})")
    return last_flow * (1 + g) / (rate - g)


def dcf_value(flows, rate, terminal_g):
    """Returns (enterprise_value, pv_forecast, pv_terminal, tv_share)."""
    pv_fc = pv_of_flows(flows, rate)
    tv = terminal_value(flows[-1], rate, terminal_g)
    pv_tv = tv / (1 + rate) ** len(flows)
    ev = pv_fc + pv_tv
    return ev, pv_fc, pv_tv, (pv_tv / ev if ev else None)


def _ev_at_growth(base_flow, g, years, rate, terminal_g):
    flows = [base_flow * (1 + g) ** t for t in range(1, years + 1)]
    ev, _, _, _ = dcf_value(flows, rate, terminal_g)
    return ev


def reverse_dcf(target_ev, base_flow, years, rate, terminal_g,
                lo=-0.60, hi=2.00, tol=1e-7):
    """Solve for the constant growth rate that makes PV(FCF) == target_ev."""
    if base_flow <= 0:
        raise ValueError("base flow must be positive — reverse DCF is undefined on negative FCF")
    f_lo = _ev_at_growth(base_flow, lo, years, rate, terminal_g) - target_ev
    f_hi = _ev_at_growth(base_flow, hi, years, rate, terminal_g) - target_ev
    if f_lo > 0:
        return lo, False   # even at the floor growth the model exceeds price
    if f_hi < 0:
        return hi, False   # even at 200% growth the model cannot reach price
    for _ in range(300):
        mid = (lo + hi) / 2
        f_mid = _ev_at_growth(base_flow, mid, years, rate, terminal_g) - target_ev
        if abs(f_mid) < tol * max(1.0, abs(target_ev)):
            return mid, True
        if f_mid < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2, True


def scenario_price(fwd_metric, exit_multiple, net_cash, shares):
    """implied price = (fwd metric x exit multiple + net cash) / shares"""
    if exit_multiple <= 0:
        raise ValueError("exit multiple must be positive")
    if shares <= 0:
        raise ValueError("shares must be positive")
    return (fwd_metric * exit_multiple + net_cash) / shares


def justified_pbv(roe, g, coe):
    """(ROE - g) / (COE - g). ROE == COE  =>  1.0x."""
    if coe <= g:
        raise ValueError(f"COE ({coe}) must exceed g ({g})")
    return (roe - g) / (coe - g)


def implied_roe(pbv, g, coe):
    """Inverse of justified_pbv: what ROE does the traded P/BV require?"""
    return pbv * (coe - g) + g


def ddm(d1, coe, g):
    if coe <= g:
        raise ValueError(f"COE ({coe}) must exceed g ({g})")
    return d1 / (coe - g)


def sustainable_growth(roe, payout):
    """g = ROE x (1 - payout). The identity a DDM must not violate."""
    return roe * (1 - payout)


def residual_income(bv0, roes, coe, terminal_g=0.0, retention=0.0):
    """
    Value = BV0 + sum[(ROEt - COE) x BV(t-1)] / (1+COE)^t, plus terminal RI.

    Book value rolls forward at ROE x retention. retention=0 (full payout) keeps
    BV flat, which is the conservative reading and the default — rolling it up
    requires a payout assumption, so the caller must supply one deliberately.
    terminal_g is an explicit terminal residual-income growth assumption; it is
    not inferred from the retention or payout inputs.
    """
    bv = bv0
    pv_ri = 0.0
    schedule = []
    for t, roe in enumerate(roes, start=1):
        ri = (roe - coe) * bv
        pv = ri / (1 + coe) ** t
        pv_ri += pv
        schedule.append((t, bv, roe, ri, pv))
        bv = bv * (1 + roe * retention)
    last_ri = schedule[-1][3]
    pv_terminal = 0.0
    if terminal_g:
        if coe <= terminal_g:
            raise ValueError("COE must exceed terminal g")
        pv_terminal = (last_ri * (1 + terminal_g) / (coe - terminal_g)) / (1 + coe) ** len(roes)
    return bv0 + pv_ri + pv_terminal, schedule, pv_ri, pv_terminal


def normalized_eps(revenue, margins, shares):
    """Mid-cycle net income = revenue x average through-cycle net margin."""
    if not margins:
        raise ValueError("at least one through-cycle margin is required")
    if shares <= 0:
        raise ValueError("shares must be positive")
    mid = sum(margins) / len(margins)
    return revenue * mid / shares, mid


def expected_value(cases):
    """cases = [(name, price, probability)]. Returns (ev, total_probability)."""
    total_p = sum(p for _, _, p in cases)
    ev = sum(price * p for _, price, p in cases)
    return (ev / total_p if total_p else None), total_p


# ---------------------------------------------------------------- commands


def cmd_wacc(a):
    coe = cost_of_equity(a.rf, a.beta, a.erp, a.crp)
    _block("INPUTS", [
        ("risk-free (cite it)", _pct(a.rf)),
        ("beta", _fmt(a.beta)),
        ("ERP (assumption)", _pct(a.erp)),
        ("country risk premium", _pct(a.crp)),
        ("equity value", _fmt(a.equity)),
        ("debt value", _fmt(a.debt)),
        ("cost of debt (pre-tax)", _pct(a.rd)),
        ("tax rate", _pct(a.tax)),
    ])
    rows = [("cost of equity (CAPM)", _pct(coe))]
    if a.debt or a.equity:
        w, we, wd = wacc(coe, a.equity, a.debt, a.rd, a.tax)
        rows += [("equity weight", _pct(we)), ("debt weight", _pct(wd)),
                 ("after-tax cost of debt", _pct(a.rd * (1 - a.tax))),
                 ("WACC", _pct(w)),
                 ("WACC band (+/-100bps)", f"{_pct(w - 0.01)} .. {_pct(w + 0.01)}")]
    _block("RESULT", rows)
    print("\n  Report the band, not the point. If the verdict flips inside +/-100bps,")
    print("  the honest finding is that DCF does not resolve this at today's price.")


def cmd_bridge(a):
    ev, net_cash = net_cash_bridge(a.mktcap, a.debt, a.cash, a.minority, a.preferred)
    _block("INPUTS", [
        ("market cap", _fmt(a.mktcap)), ("total debt (incl. leases if used)", _fmt(a.debt)),
        ("cash + liquid ST inv.", _fmt(a.cash)), ("minority interest", _fmt(a.minority)),
        ("preferred", _fmt(a.preferred)), ("shares", _fmt(a.shares) if a.shares else "n/a"),
    ])
    rows = [("enterprise value", _fmt(ev)),
            ("net cash / (net debt)", _fmt(net_cash))]
    if a.shares:
        rows.append(("net cash per share", _fmt(net_cash / a.shares)))
    _block("RESULT", rows)
    if net_cash > 0 and a.mktcap and net_cash / a.mktcap > 0.25:
        _warn("net cash > 25% of market cap — ex-cash multiples are the meaningful "
              "ones, and ask whether the cash is actually accessible to minorities.")


def cmd_ncav(a):
    ncav = a.current_assets - a.total_liabilities
    _block("INPUTS", [
        ("current assets", _fmt(a.current_assets)),
        ("total liabilities", _fmt(a.total_liabilities)),
        ("cash", _fmt(a.cash) if a.cash is not None else "n/a"),
        ("receivables", _fmt(a.receivables) if a.receivables is not None else "n/a"),
        ("inventory", _fmt(a.inventory) if a.inventory is not None else "n/a"),
        ("shares", _fmt(a.shares)), ("price", _fmt(a.price) if a.price else "n/a"),
    ])
    rows = [("NCAV (= equity - non-current assets)", _fmt(ncav)),
            ("NCAV per share", _fmt(ncav / a.shares))]
    if None not in (a.cash, a.receivables, a.inventory):
        nnwc = a.cash + 0.75 * a.receivables + 0.5 * a.inventory - a.total_liabilities
        rows += [("NNWC", _fmt(nnwc)), ("NNWC per share", _fmt(nnwc / a.shares))]
    if a.price:
        rows.append(("price / NCAV per share",
                     _fmt(a.price / (ncav / a.shares)) if ncav > 0 else "n/a (NCAV <= 0)"))
    _block("RESULT", rows)
    if ncav <= 0:
        _warn("NCAV <= 0. For an asset-heavy business this is arithmetic, not a "
              "verdict — non-current assets exceed equity by construction. Net-Net "
              "is the wrong tool here; go back to the archetype matrix.")


def cmd_dcf(a):
    flows = [float(x) for x in a.flows.split(",")]
    ev, pv_fc, pv_tv, tv_share = dcf_value(flows, a.wacc, a.terminal_g)
    equity = ev + a.net_cash
    _block("INPUTS", [
        ("FCF forecast", ", ".join(_fmt(f) for f in flows)),
        ("WACC", _pct(a.wacc)), ("terminal growth", _pct(a.terminal_g)),
        ("net cash / (net debt)", _fmt(a.net_cash)), ("shares", _fmt(a.shares)),
        ("current price", _fmt(a.price) if a.price else "n/a"),
        ("discounting", "year-end"),
    ])
    rows = [("PV of forecast FCF", _fmt(pv_fc)),
            ("PV of terminal value", _fmt(pv_tv)),
            ("terminal share of EV", _pct(tv_share)),
            ("enterprise value", _fmt(ev)),
            ("equity value", _fmt(equity)),
            ("value per share", _fmt(equity / a.shares))]
    if a.price:
        rows.append(("upside vs price", _pct(equity / a.shares / a.price - 1)))
    if a.terminal_ebitda:
        rows.append(("implied exit EV/EBITDA",
                     _fmt(terminal_value(flows[-1], a.wacc, a.terminal_g) / a.terminal_ebitda)))
    _block("RESULT", rows)
    if tv_share and tv_share > 0.75:
        _warn(f"terminal value is {_pct(tv_share)} of EV — this is an exit-multiple "
              "bet, not a cash-flow valuation. Say so, and sanity-check the implied "
              "exit multiple against peers.")
    if a.terminal_g >= a.wacc - 0.02:
        _warn("terminal g is within 200bps of WACC — the perpetuity multiplier is "
              "hypersensitive here. Show the sensitivity to g.")
    if a.rf is not None and a.terminal_g > a.rf:
        _warn(f"terminal g ({_pct(a.terminal_g)}) exceeds the risk-free rate "
              f"({_pct(a.rf)}) — implies the company outgrows the economy forever.")


def cmd_reverse_dcf(a):
    g, ok = reverse_dcf(a.target_ev, a.base_fcf, a.years, a.wacc, a.terminal_g)
    _block("INPUTS", [
        ("target EV (from market price)", _fmt(a.target_ev)),
        ("base FCF (TTM)", _fmt(a.base_fcf)),
        ("forecast years", str(a.years)),
        ("WACC", _pct(a.wacc)), ("terminal growth", _pct(a.terminal_g)),
        ("actual growth to compare", _pct(a.actual) if a.actual is not None else "n/a"),
    ])
    rows = [("implied FCF CAGR over the forecast", _pct(g) if ok else f"outside bracket ({_pct(g)})")]
    if a.actual is not None and ok:
        rows.append(("gap vs actual/consensus", f"{(g - a.actual) * 100:+.2f} pp"))
    _block("RESULT", rows)
    if not ok:
        _warn("no solution inside the search bracket — at this WACC the price cannot "
              "be reconciled with any plausible growth. Report that, don't force a number.")
    elif g > 0.25:
        _warn(f"{_pct(g)} sustained for {a.years} years is a strong claim. Test it "
              "against the company's own history, consensus, and the addressable market.")
    print("\n  Now repeat holding growth at consensus and solving for MARGIN instead.")
    print("  Whichever input needs the more heroic value carries the market's optimism.")


def cmd_scenario(a):
    cases = []
    for spec in a.case:
        parts = spec.split(":")
        if len(parts) != 5:
            raise SystemExit("each --case needs name:fwd_metric:exit_multiple:probability:label_note "
                             "e.g. base:1200:6.5:0.5:consensus")
        name, metric, mult, prob, _note = parts
        price = scenario_price(float(metric), float(mult), a.net_cash, a.shares)
        cases.append((name, float(metric), float(mult), float(prob), price))
    _block("INPUTS", [("net cash / (net debt)", _fmt(a.net_cash)),
                      ("shares", _fmt(a.shares)),
                      ("current price", _fmt(a.price) if a.price else "n/a"),
                      ("formula", "(fwd metric x exit multiple + net cash) / shares")])
    print("\nSCENARIOS")
    print("-" * 68)
    hdr = f"  {'case':<10}{'fwd metric':>14}{'exit x':>9}{'prob':>8}{'implied':>12}{'vs price':>12}"
    print(hdr)
    for name, metric, mult, prob, price in cases:
        vs = _pct(price / a.price - 1) if a.price else "n/a"
        print(f"  {name:<10}{_fmt(metric):>14}{_fmt(mult):>9}{_pct(prob, 0):>8}{_fmt(price):>12}{vs:>12}")
    ev, total_p = expected_value([(n, p, pr) for n, _, _, pr, p in cases])
    rows = [("probability-weighted EV", _fmt(ev)), ("probabilities sum to", _pct(total_p, 0))]
    if a.price:
        rows.append(("EV vs current price", _pct(ev / a.price - 1)))
    spread = max(c[4] for c in cases) - min(c[4] for c in cases)
    rows.append(("bull-bear spread", f"{_fmt(spread)} ({_pct(spread / a.price)} of price)"
                 if a.price else _fmt(spread)))
    _block("RESULT", rows)
    if abs(total_p - 1.0) > 0.001:
        _warn("probabilities do not sum to 100%.")
    mults = [c[2] for c in cases]
    metrics = [c[1] for c in cases]
    if max(mults) / min(mults) > max(metrics) / min(metrics):
        _warn("the exit multiple, not the forward metric, is driving the spread — "
              "say so. The user is being asked to bet on a re-rating, not on growth.")
    print("\n  Probabilities are YOUR judgment. State them as such and make them editable.")


def cmd_justified_pbv(a):
    jp = justified_pbv(a.roe, a.g, a.coe)
    _block("INPUTS", [("ROE", _pct(a.roe)), ("sustainable growth g", _pct(a.g)),
                      ("COE", _pct(a.coe)), ("book value per share", _fmt(a.bvps)),
                      ("price", _fmt(a.price) if a.price else "n/a")])
    rows = [("justified P/BV = (ROE-g)/(COE-g)", f"{_fmt(jp)}x"),
            ("ROE - COE spread", f"{(a.roe - a.coe) * 100:+.2f} pp")]
    if a.bvps:
        rows.append(("justified value per share", _fmt(jp * a.bvps)))
    if a.price and a.bvps:
        traded = a.price / a.bvps
        rows += [("traded P/BV", f"{_fmt(traded)}x"),
                 ("upside to justified", _pct(jp * a.bvps / a.price - 1)),
                 ("ROE the traded P/BV requires", _pct(implied_roe(traded, a.g, a.coe)))]
    _block("RESULT", rows)
    if a.roe < a.coe:
        _warn("ROE below COE mathematically implies P/BV < 1. If it trades above "
              "book, the market is pricing an ROE recovery — name it and test it.")


def cmd_ddm(a):
    d1 = a.d1 if a.d1 is not None else a.d0 * (1 + a.g)
    p = ddm(d1, a.coe, a.g)
    _block("INPUTS", [("D0", _fmt(a.d0) if a.d0 is not None else "n/a"),
                      ("D1", _fmt(d1)), ("COE", _pct(a.coe)), ("growth g", _pct(a.g)),
                      ("ROE", _pct(a.roe) if a.roe is not None else "n/a"),
                      ("payout ratio", _pct(a.payout) if a.payout is not None else "n/a"),
                      ("price", _fmt(a.price) if a.price else "n/a")])
    rows = [("DDM value per share", _fmt(p)),
            ("implied dividend yield at value", _pct(d1 / p))]
    if a.price:
        rows += [("current dividend yield", _pct(d1 / a.price)),
                 ("upside vs price", _pct(p / a.price - 1))]
    if a.roe is not None and a.payout is not None:
        g_sust = sustainable_growth(a.roe, a.payout)
        rows.append(("g implied by ROE x (1-payout)", _pct(g_sust)))
        if abs(g_sust - a.g) > 0.01:
            rows.append(("consistency", "MISMATCH > 100bps"))
    _block("RESULT", rows)
    if a.roe is not None and a.payout is not None and abs(sustainable_growth(a.roe, a.payout) - a.g) > 0.01:
        _warn("g and payout violate g = ROE x (1-payout). The model is internally "
              "inconsistent — you are growing faster than retained earnings allow.")


def cmd_residual_income(a):
    roes = [float(x) for x in a.roes.split(",")]
    val, schedule, pv_ri, pv_tv = residual_income(a.bvps, roes, a.coe, a.terminal_g, a.retention)
    _block("INPUTS", [("book value per share", _fmt(a.bvps)),
                      ("ROE forecast", ", ".join(_pct(r) for r in roes)),
                      ("COE", _pct(a.coe)), ("terminal RI growth (assumption)", _pct(a.terminal_g)),
                      ("price", _fmt(a.price) if a.price else "n/a"),
                      ("retention (1 - payout)", _pct(a.retention))])
    print("\nRESIDUAL INCOME SCHEDULE")
    print("-" * 60)
    print(f"  {'yr':<4}{'BV start':>12}{'ROE':>9}{'RI':>12}{'PV(RI)':>12}")
    for t, bv, roe, ri, pv in schedule:
        print(f"  {t:<4}{_fmt(bv):>12}{_pct(roe):>9}{_fmt(ri):>12}{_fmt(pv):>12}")
    rows = [("book value", _fmt(a.bvps)), ("+ PV of residual income", _fmt(pv_ri)),
            ("+ PV of terminal RI", _fmt(pv_tv)), ("= value per share", _fmt(val)),
            ("value / book", f"{_fmt(val / a.bvps)}x")]
    if a.price:
        rows.append(("upside vs price", _pct(val / a.price - 1)))
    _block("RESULT", rows)
    if not a.retention:
        print("\n  Retention defaults to 0, so book value is held flat — conservative.")
        print("  Pass --retention (1 - payout) if retained earnings matter to the answer.")


def cmd_normalized_eps(a):
    margins = [float(x) for x in a.margins.split(",")]
    eps, mid = normalized_eps(a.revenue, margins, a.shares)
    _block("INPUTS", [("revenue (current)", _fmt(a.revenue)),
                      ("through-cycle net margins", ", ".join(_pct(m) for m in margins)),
                      ("shares", _fmt(a.shares)),
                      ("through-cycle P/E", _fmt(a.pe) if a.pe else "n/a"),
                      ("current/TTM EPS", _fmt(a.current_eps) if a.current_eps else "n/a"),
                      ("price", _fmt(a.price) if a.price else "n/a")])
    rows = [("mid-cycle net margin", _pct(mid)),
            ("normalized EPS", _fmt(eps))]
    if a.pe:
        rows.append(("mid-cycle fair value", _fmt(eps * a.pe)))
        if a.price:
            rows.append(("upside vs price", _pct(eps * a.pe / a.price - 1)))
    if a.current_eps:
        rows.append(("current EPS vs normalized", f"{_fmt(a.current_eps / eps)}x"))
    if a.price:
        rows.append(("P/E on normalized EPS", _fmt(a.price / eps)))
        if a.current_eps:
            rows.append(("P/E on current EPS", _fmt(a.price / a.current_eps)))
    _block("RESULT", rows)
    if a.current_eps and a.current_eps > eps * 1.3:
        _warn("current EPS is >30% above mid-cycle — the low trailing P/E is a "
              "peak-earnings artifact. This is the classic cyclical value trap; "
              "lead with that, not with the multiple.")
    if a.current_eps and a.current_eps < eps * 0.7:
        _warn("current EPS is >30% below mid-cycle — a high or negative trailing "
              "P/E here does not mean expensive. Anchor the downside on P/BV at trough.")


# ---------------------------------------------------------------- self test


def cmd_selftest(_a):
    fails = []

    def check(name, got, want, tol=1e-6):
        if abs(got - want) > tol:
            fails.append(f"{name}: got {got!r}, want {want!r}")

    # CAPM / WACC
    check("coe", cost_of_equity(0.04, 1.2, 0.055), 0.04 + 1.2 * 0.055)
    w, we, wd = wacc(0.10, 800.0, 200.0, 0.05, 0.20)
    check("wacc", w, 0.8 * 0.10 + 0.2 * 0.05 * 0.8)
    check("we", we, 0.8)
    check("wd", wd, 0.2)

    # EV bridge
    ev, nc = net_cash_bridge(1000.0, 300.0, 500.0, 50.0)
    check("ev", ev, 850.0)
    check("net_cash", nc, 200.0)

    # NCAV identity: equity - non-current assets == current assets - total liabilities
    ca, nca, tl = 400.0, 600.0, 250.0
    equity = (ca + nca) - tl
    check("ncav identity", equity - nca, ca - tl)

    # PV / terminal / DCF
    check("pv", pv_of_flows([110.0], 0.10), 100.0)
    check("tv", terminal_value(100.0, 0.10, 0.02), 100.0 * 1.02 / 0.08)
    ev2, pv_fc, pv_tv, share = dcf_value([100.0, 100.0], 0.10, 0.0)
    check("dcf pv_fc", pv_fc, 100 / 1.1 + 100 / 1.21)
    check("dcf pv_tv", pv_tv, (100 / 0.10) / 1.21)
    check("dcf ev", ev2, pv_fc + pv_tv)
    check("tv share", share, pv_tv / ev2)

    # Reverse DCF round trip: price built from g=15% must solve back to 15%
    target = _ev_at_growth(100.0, 0.15, 5, 0.09, 0.025)
    g, ok = reverse_dcf(target, 100.0, 5, 0.09, 0.025)
    assert ok, "reverse dcf failed to bracket"
    check("reverse dcf round trip", g, 0.15, 1e-4)

    # Scenario + EV
    p = scenario_price(1000.0, 5.0, 500.0, 100.0)
    check("scenario price", p, 55.0)
    evx, tp = expected_value([("bear", 40.0, 0.25), ("base", 55.0, 0.5), ("bull", 80.0, 0.25)])
    check("prob-weighted ev", evx, 40 * 0.25 + 55 * 0.5 + 80 * 0.25)
    check("prob sum", tp, 1.0)

    # Justified P/BV: ROE == COE must give exactly 1.0x, and inverse must round trip
    check("jpbv at roe=coe", justified_pbv(0.10, 0.04, 0.10), 1.0)
    check("jpbv", justified_pbv(0.15, 0.05, 0.10), (0.15 - 0.05) / (0.10 - 0.05))
    check("implied roe round trip", implied_roe(justified_pbv(0.15, 0.05, 0.10), 0.05, 0.10), 0.15)

    # DDM + retention identity
    check("ddm", ddm(5.0, 0.10, 0.04), 5.0 / 0.06)
    check("sustainable g", sustainable_growth(0.12, 0.40), 0.12 * 0.6)

    # Residual income: ROE == COE every year must value exactly at book
    val, _, pv_ri, _ = residual_income(100.0, [0.10, 0.10, 0.10], 0.10)
    check("ri at no spread", val, 100.0)
    check("ri pv at no spread", pv_ri, 0.0)
    val2, _, _, _ = residual_income(100.0, [0.15, 0.15], 0.10)
    check("ri with spread", val2, 100.0 + (0.05 * 100) / 1.10 + (0.05 * 100) / 1.21)
    # with retention, year-2 book value must have grown by ROE x retention
    val3, sched3, _, _ = residual_income(100.0, [0.15, 0.15], 0.10, retention=0.40)
    check("ri bv roll-forward", sched3[1][1], 100.0 * (1 + 0.15 * 0.40))
    check("ri with retention", val3,
          100.0 + (0.05 * 100) / 1.10 + (0.05 * 100 * (1 + 0.06)) / 1.21)

    # Normalized EPS
    eps, mid = normalized_eps(1000.0, [0.05, 0.10, 0.15], 100.0)
    check("mid margin", mid, 0.10)
    check("normalized eps", eps, 1000.0 * 0.10 / 100.0)

    # Guards must raise
    for label, fn in [
        ("wacc<=g in terminal_value", lambda: terminal_value(100.0, 0.05, 0.05)),
        ("coe<=g in justified_pbv", lambda: justified_pbv(0.10, 0.10, 0.10)),
        ("coe<=g in ddm", lambda: ddm(5.0, 0.04, 0.04)),
        ("negative base fcf in reverse_dcf", lambda: reverse_dcf(100.0, -5.0, 5, 0.09, 0.02)),
        ("zero shares in scenario_price", lambda: scenario_price(100.0, 5.0, 0.0, 0.0)),
    ]:
        try:
            fn()
            fails.append(f"{label}: expected ValueError, none raised")
        except ValueError:
            pass

    if fails:
        print("SELFTEST FAILED")
        for f in fails:
            print("  -", f)
        return 1
    print("SELFTEST OK — all identity and round-trip checks pass.")
    return 0


# ---------------------------------------------------------------- CLI


def main(argv=None):
    p = argparse.ArgumentParser(prog="valuation.py", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("wacc", help="CAPM cost of equity and WACC")
    s.add_argument("--rf", type=float, required=True, help="risk-free rate as decimal (cite it)")
    s.add_argument("--beta", type=float, required=True)
    s.add_argument("--erp", type=float, required=True, help="equity risk premium (assumption)")
    s.add_argument("--crp", type=float, default=0.0, help="country risk premium")
    s.add_argument("--equity", type=float, default=0.0)
    s.add_argument("--debt", type=float, default=0.0)
    s.add_argument("--rd", type=float, default=0.0, help="pre-tax cost of debt")
    s.add_argument("--tax", type=float, default=0.20)
    s.set_defaults(func=cmd_wacc)

    s = sub.add_parser("bridge", help="market cap <-> EV, net cash")
    s.add_argument("--mktcap", type=float, required=True)
    s.add_argument("--debt", type=float, required=True)
    s.add_argument("--cash", type=float, required=True)
    s.add_argument("--minority", type=float, default=0.0)
    s.add_argument("--preferred", type=float, default=0.0)
    s.add_argument("--shares", type=float, default=0.0)
    s.set_defaults(func=cmd_bridge)

    s = sub.add_parser("ncav", help="NCAV / NNWC per share")
    s.add_argument("--current-assets", type=float, required=True, dest="current_assets")
    s.add_argument("--total-liabilities", type=float, required=True, dest="total_liabilities")
    s.add_argument("--shares", type=float, required=True)
    s.add_argument("--cash", type=float, default=None)
    s.add_argument("--receivables", type=float, default=None)
    s.add_argument("--inventory", type=float, default=None)
    s.add_argument("--price", type=float, default=None)
    s.set_defaults(func=cmd_ncav)

    s = sub.add_parser("dcf", help="DCF from an explicit FCF forecast")
    s.add_argument("--flows", required=True, help="comma-separated FCF forecast, e.g. 100,115,132")
    s.add_argument("--wacc", type=float, required=True)
    s.add_argument("--terminal-g", type=float, required=True, dest="terminal_g")
    s.add_argument("--net-cash", type=float, default=0.0, dest="net_cash",
                   help="net cash (positive) or net debt (negative)")
    s.add_argument("--shares", type=float, required=True)
    s.add_argument("--price", type=float, default=None)
    s.add_argument("--rf", type=float, default=None, help="risk-free, to check terminal g")
    s.add_argument("--terminal-ebitda", type=float, default=None, dest="terminal_ebitda",
                   help="terminal-year EBITDA, to show the implied exit multiple")
    s.set_defaults(func=cmd_dcf)

    s = sub.add_parser("reverse-dcf", help="solve for the growth the price requires")
    s.add_argument("--target-ev", type=float, required=True, dest="target_ev")
    s.add_argument("--base-fcf", type=float, required=True, dest="base_fcf")
    s.add_argument("--years", type=int, default=5)
    s.add_argument("--wacc", type=float, required=True)
    s.add_argument("--terminal-g", type=float, required=True, dest="terminal_g")
    s.add_argument("--actual", type=float, default=None,
                   help="historical or consensus growth, for the gap")
    s.set_defaults(func=cmd_reverse_dcf)

    s = sub.add_parser("scenario", help="bear/base/bull implied price + weighted EV")
    s.add_argument("--case", action="append", required=True,
                   help="name:fwd_metric:exit_multiple:probability:note (repeatable)")
    s.add_argument("--net-cash", type=float, default=0.0, dest="net_cash")
    s.add_argument("--shares", type=float, required=True)
    s.add_argument("--price", type=float, default=None)
    s.set_defaults(func=cmd_scenario)

    s = sub.add_parser("justified-pbv", help="justified P/BV from ROE, g, COE")
    s.add_argument("--roe", type=float, required=True)
    s.add_argument("--g", type=float, required=True)
    s.add_argument("--coe", type=float, required=True)
    s.add_argument("--bvps", type=float, default=0.0)
    s.add_argument("--price", type=float, default=None)
    s.set_defaults(func=cmd_justified_pbv)

    s = sub.add_parser("ddm", help="dividend discount model")
    s.add_argument("--d0", type=float, default=None, help="last dividend per share")
    s.add_argument("--d1", type=float, default=None, help="next dividend per share")
    s.add_argument("--coe", type=float, required=True)
    s.add_argument("--g", type=float, required=True)
    s.add_argument("--roe", type=float, default=None, help="for the retention check")
    s.add_argument("--payout", type=float, default=None, help="for the retention check")
    s.add_argument("--price", type=float, default=None)
    s.set_defaults(func=cmd_ddm)

    s = sub.add_parser("residual-income", help="residual income valuation")
    s.add_argument("--bvps", type=float, required=True)
    s.add_argument("--roes", required=True, help="comma-separated ROE forecast, e.g. 0.12,0.13,0.13")
    s.add_argument("--coe", type=float, required=True)
    s.add_argument("--terminal-g", type=float, default=0.0, dest="terminal_g")
    s.add_argument("--retention", type=float, default=0.0,
                   help="1 - payout ratio; rolls book value forward. 0 = BV flat")
    s.add_argument("--price", type=float, default=None)
    s.set_defaults(func=cmd_residual_income)

    s = sub.add_parser("normalized-eps", help="mid-cycle EPS for a cyclical")
    s.add_argument("--revenue", type=float, required=True)
    s.add_argument("--margins", required=True,
                   help="comma-separated through-cycle net margins, e.g. 0.03,0.07,0.11,0.05")
    s.add_argument("--shares", type=float, required=True)
    s.add_argument("--pe", type=float, default=None, help="through-cycle P/E")
    s.add_argument("--current-eps", type=float, default=None, dest="current_eps")
    s.add_argument("--price", type=float, default=None)
    s.set_defaults(func=cmd_normalized_eps)

    s = sub.add_parser("selftest", help="verify every formula against known identities")
    s.set_defaults(func=cmd_selftest)

    a = p.parse_args(argv)
    if a.cmd == "ddm" and a.d0 is None and a.d1 is None:
        p.error("ddm needs --d0 or --d1")
    rc = a.func(a)
    return rc or 0


if __name__ == "__main__":
    sys.exit(main())
