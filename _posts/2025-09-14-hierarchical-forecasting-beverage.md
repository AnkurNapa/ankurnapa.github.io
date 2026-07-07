---
layout: post
title: "Hierarchical Forecasting: Reconciling SKU, Brand, and Total Volume"
image: /assets/og/hierarchical-forecasting-beverage.png
description: "How hierarchical forecasting reconciles demand signals across SKU, brand, and portfolio levels — and why misalignment between levels destroys planning credibility."
date: 2025-09-14
updated: 2025-09-14
tags: [forecasting, hierarchical-forecasting]
faq:
  - q: "What is hierarchical forecasting?"
    a: "Hierarchical forecasting is a method for generating forecasts at multiple levels of aggregation — SKU, brand, category, total portfolio — while ensuring they are mathematically consistent. A bottom-up SKU forecast that sums to more than the top-down portfolio target is a common and costly failure mode this method is designed to prevent."
  - q: "What is the difference between bottom-up and top-down forecasting in beverages?"
    a: "Bottom-up forecasting starts at the SKU level and sums upward. Top-down starts at total portfolio or market-share level and allocates down. Each has blind spots: bottom-up can miss macro constraints; top-down can lose SKU-level accuracy. Hierarchical methods combine both using reconciliation algorithms."
  - q: "How does a non-alcoholic beer launch change the hierarchy?"
    a: "A new NA SKU introduces a branch in the hierarchy that may have more top-down market context (category growth rates) than bottom-up data (it has no history). Hierarchical models handle this gracefully by allowing the top-down signal to dominate the NA node while the bottom-up signal anchors mature SKUs in the same brand family."
---

**Short answer:** A forecast that is accurate at the SKU level but inconsistent with the brand-level target — or a brand plan that doesn't add up to the portfolio total — is not just a mathematical annoyance. It destroys planning credibility, creates adversarial S&OP processes, and leads to conflicting production and commercial commitments. Hierarchical forecasting solves this structurally, not by negotiation.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The operating loop this post describes"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE OPERATING LOOP</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Hierarchical Forecasting: Reconciling SKU, Brand, and Total Volume</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Measure</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">data in</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analyse</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">find the signal</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Decide</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">choose</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Act</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">change the floor</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">repeat</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The operating loop this post describes: measure, analyse, decide, act — then repeat.</figcaption>
</figure>

## The Reconciliation Problem That Breaks S&OP

Most beverage companies run at least two forecasting processes in parallel: a commercial or top-line forecast built from market share and category growth assumptions, and an operational or supply forecast built from SKU-level history. These two forecasts almost never agree by default.

The resulting "gap" becomes the focus of monthly Sales & Operations Planning (S&OP) meetings — not because the underlying demand signal is genuinely uncertain, but because no one has specified a consistent method for reconciling the two levels. Managers spend hours debating which number is "right" rather than making decisions.

Hierarchical forecasting eliminates this structural inconsistency by design.

---

## The Hierarchy: Levels and Their Purpose

A typical beverage demand hierarchy has three to five levels:

- **Total portfolio** — the number that feeds financial planning and corporate commitments
- **Brand family** — the number that drives brand investment decisions and commercial targets
- **SKU × channel** — the number that drives production scheduling and inventory positioning
- **SKU × channel × region** — the number that drives distribution and field sales targets (relevant for larger breweries with national footprints)

Each level serves a different decision-maker with different planning horizons. Total portfolio forecasts lock annually with quarterly updates. SKU-level forecasts update weekly in most modern supply chains.

The hierarchy must be defined explicitly before any reconciliation method is applied. Ambiguity about where non-alcoholic beer sits in the hierarchy — is it a brand family, a sub-brand of an existing lager, or a separate category node? — causes persistent reconciliation failures.

---

## Reconciliation Methods: Bottom-Up, Top-Down, and Optimal

**Bottom-up (BU):** Generate SKU-level forecasts independently, then sum to brand and portfolio. Advantage: captures SKU-level signals well. Risk: the portfolio sum may contradict macroeconomic or market-share expectations.

**Top-down (TD):** Generate a portfolio forecast, then disaggregate using historical share proportions. Advantage: respects macro constraints. Risk: loses SKU-level accuracy, particularly for fast-growing or fast-declining individual SKUs.

**Optimal reconciliation (MinT / ERM):** A family of methods that generates forecasts at all levels independently and then finds a set of reconciled forecasts that minimises total forecast error across the hierarchy while enforcing the summing constraints. Academic research over the past decade has established that optimal reconciliation consistently outperforms both pure BU and pure TD approaches on real commercial datasets.

For most beverage planning teams, the practical starting point is a well-implemented BU forecast with a manual top-down constraint applied at the portfolio level — a "constrained BU." Full optimal reconciliation requires statistical tooling and clean data across all levels simultaneously, but it is achievable with modern forecasting platforms.

---

## NA Beer in the Hierarchy

Non-alcoholic beer creates a specific hierarchical challenge: it has strong top-down signals (the NA category is growing, and category growth rates are observable) but weak bottom-up signals (individual SKUs have limited history). This is the inverse of a mature lager SKU, which has reliable bottom-up history but limited differentiated top-down signal.

The natural solution is to allow the information weight to vary by node in the hierarchy. For NA SKUs, the top-down category growth rate should receive more weight in the reconciled forecast. For mature lager SKUs, the bottom-up time-series estimate should dominate. Hierarchical frameworks designed with explicit weighting by level maturity handle this cleanly.

This also connects to the analogue forecasting approach for new product introductions discussed in [Forecasting With No History: The Non-Alcoholic Beer Problem]({{ '/2025/forecasting-new-products-na-beer/' | relative_url }}) — the analogue-based NA forecast can be inserted into the hierarchy as a node with explicit high uncertainty, allowing the reconciliation to treat it accordingly.

---

## Accuracy Reporting Across the Hierarchy

A common mistake is measuring forecast accuracy only at the level where the forecast is easiest to produce — typically the brand or total portfolio level — while the SKU-level forecast driving actual supply decisions is left unmeasured.

Accuracy metrics should be reported at every level of the hierarchy, and the metrics should be appropriate for each level's decision use. For more on which accuracy metrics to use and which to discard, see [Forecast Accuracy Metrics That Matter]({{ '/2026/forecast-accuracy-metrics/' | relative_url }}).

---

## The Honest Caveat

Hierarchical forecasting is technically compelling but organisationally demanding. The method requires that all stakeholders agree on the hierarchy definition, that data is consistently tagged at every level, and that the reconciled forecast — rather than any individual level's preferred number — is the one that actually drives decisions. In organisations where commercial and supply teams have historically defended their own forecasts, this requires change management as much as statistical methodology.

*Part of the Sales Forecasting track — [browse all]({{ '/tags/' | relative_url }}#forecasting).*

---

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="History (solid) and the model&#39;s forward forecast (dashed); the shaded band is its uncertainty."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FORECAST</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Hierarchical Forecasting: Reconciling SKU, Brand, and Total Volume</text><g stroke="#06483f" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#00695c" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#00695c" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#06483f" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">today</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">history</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">forecast</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">History (solid) and the model&#39;s forward forecast (dashed); the shaded band is its uncertainty.</figcaption>
</figure>

## Frequently asked questions

**What is hierarchical forecasting?**  
Hierarchical forecasting is a method for generating forecasts at multiple levels of aggregation — SKU, brand, category, total portfolio — while ensuring they are mathematically consistent. A bottom-up SKU forecast that sums to more than the top-down portfolio target is a common and costly failure mode this method is designed to prevent.

**What is the difference between bottom-up and top-down forecasting in beverages?**  
Bottom-up forecasting starts at the SKU level and sums upward. Top-down starts at total portfolio or market-share level and allocates down. Each has blind spots: bottom-up can miss macro constraints; top-down can lose SKU-level accuracy. Hierarchical methods combine both using reconciliation algorithms.

**How does a non-alcoholic beer launch change the hierarchy?**  
A new NA SKU introduces a branch in the hierarchy that may have more top-down market context (category growth rates) than bottom-up data (it has no history). Hierarchical models handle this gracefully by allowing the top-down signal to dominate the NA node while the bottom-up signal anchors mature SKUs in the same brand family.
