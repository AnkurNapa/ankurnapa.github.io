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

## Frequently asked questions

**What is hierarchical forecasting?**  
Hierarchical forecasting is a method for generating forecasts at multiple levels of aggregation — SKU, brand, category, total portfolio — while ensuring they are mathematically consistent. A bottom-up SKU forecast that sums to more than the top-down portfolio target is a common and costly failure mode this method is designed to prevent.

**What is the difference between bottom-up and top-down forecasting in beverages?**  
Bottom-up forecasting starts at the SKU level and sums upward. Top-down starts at total portfolio or market-share level and allocates down. Each has blind spots: bottom-up can miss macro constraints; top-down can lose SKU-level accuracy. Hierarchical methods combine both using reconciliation algorithms.

**How does a non-alcoholic beer launch change the hierarchy?**  
A new NA SKU introduces a branch in the hierarchy that may have more top-down market context (category growth rates) than bottom-up data (it has no history). Hierarchical models handle this gracefully by allowing the top-down signal to dominate the NA node while the bottom-up signal anchors mature SKUs in the same brand family.
