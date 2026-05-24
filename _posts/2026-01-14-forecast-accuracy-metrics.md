---
layout: post
title: "Forecast Accuracy Metrics That Matter (and the Vanity Ones to Drop)"
description: "Which forecast accuracy metrics actually drive better beverage planning decisions — MAPE, WMAPE, bias, CFE — and which metrics flatter but mislead."
date: 2026-01-14
updated: 2026-01-14
tags: [forecasting, forecast-accuracy-metrics]
faq:
  - q: "What is the best forecast accuracy metric for beer demand planning?"
    a: "There is no single best metric — the right choice depends on the decision being supported. WMAPE (weighted mean absolute percentage error) is the most widely used operational metric for SKU-level supply planning because it naturally weights high-volume SKUs more heavily. Bias (or CFE, cumulative forecast error) is equally important because a low-error model that is consistently directionally wrong creates systematic inventory imbalances."
  - q: "Why is MAPE a problematic forecast accuracy metric?"
    a: "MAPE (mean absolute percentage error) is symmetric in percentage terms but asymmetric in business impact when applied to low-volume SKUs. A SKU selling 10 cases per week where you forecast 5 generates a 50% error; forecasting 15 also generates a 50% error — but the supply chain consequences are very different. MAPE also breaks down when actual values are near zero, which is common for new or seasonal SKUs."
  - q: "How should forecast accuracy be reported for a non-alcoholic beer portfolio with new SKUs?"
    a: "New NA SKUs should be reported separately from mature SKUs, with absolute error (cases or units) rather than percentage error, given the low volumes in early periods. Mixing new product accuracy into a MAPE calculation that includes high-volume mature SKUs masks performance in both directions."
---

**Short answer:** Most beverage companies measure forecast accuracy with MAPE, report the number in S&OP, and make no decisions with it. The metrics that actually drive better planning — bias detection, volume-weighted error, and service-level linkage — are less commonly used but far more actionable. A short, deliberate accuracy framework beats a long dashboard of vanity statistics.

---

## The Problem With MAPE as the Default

MAPE (mean absolute percentage error) became the standard forecast accuracy metric largely because it is intuitive: "we were 12% off on average" is easy to communicate. But MAPE has well-documented structural weaknesses that make it a poor primary metric for beverage supply planning:

- **Infinite or unstable values near zero.** Seasonal or new-launch SKUs with near-zero volumes in certain periods generate extreme MAPE values that distort portfolio-level averages.
- **Asymmetric business consequences.** A 20% over-forecast and a 20% under-forecast have identical MAPE impact but opposite supply chain effects — one creates overstock, the other creates stockouts. MAPE is blind to direction.
- **Low-volume SKU inflation.** Unweighted MAPE gives a 10-case-per-week SKU the same contribution to the average as a 10,000-case-per-week SKU. The result is a headline accuracy number that reflects performance on the least commercially important items.

None of these flaws mean MAPE is useless. For a single SKU with stable, mid-range volume, it is a reasonable error measure. The problem is using it as the primary portfolio-level metric in S&OP reporting.

---

## The Metrics That Drive Decisions

**WMAPE (Weighted Mean Absolute Percentage Error).** Weights absolute errors by actual volume, ensuring high-volume SKUs dominate the portfolio metric. This aligns the accuracy measure with commercial and supply significance. Most planning teams that upgrade from MAPE to WMAPE find their headline accuracy numbers change considerably — usually worsening, because it becomes harder to hide poor performance on important SKUs behind good performance on small ones.

**Bias / CFE (Cumulative Forecast Error).** Tracks whether the forecast is consistently high or consistently low over time. A model with zero average error but consistent over-forecasting in summer and under-forecasting in winter has a bias problem that MAPE will not surface. CFE = sum of (forecast minus actual) over a rolling period. A persistent positive CFE signals systematic over-forecasting; negative CFE signals under-forecasting. Both create structural inventory problems.

**Tracking Signal.** A normalised version of CFE that flags when the cumulative error exceeds a threshold — typically ±4 to ±6 — triggering a review of the underlying forecast model. This is the operational mechanism that converts bias detection into model intervention.

**Service-Level Linkage.** Ultimately, the purpose of an accurate demand forecast is to support a service level — fill rate, on-shelf availability, or case fill to retailers. Reporting forecast accuracy disconnected from actual service outcomes is measuring an input rather than the result. A brewery that achieves 95% case fill on a 15% WMAPE has a different problem than one achieving 80% case fill on a 15% WMAPE: the relationship between forecast error and service level tells you whether the supply buffer is correctly sized.

---

## Reporting Across the Portfolio Hierarchy

Accuracy metrics should mirror the forecasting hierarchy. As covered in [Hierarchical Forecasting: Reconciling SKU, Brand, and Total Volume]({{ '/2025/hierarchical-forecasting-beverage/' | relative_url }}), decisions are made at multiple aggregation levels — and accuracy should be measured and reported at each.

A common failure mode is measuring accuracy only at the brand or total portfolio level, where aggregation naturally smooths errors. SKU-level accuracy should be reported separately and is typically 30–50% worse than brand-level accuracy — a gap that reflects the genuine information content at each level, and that should inform safety stock policy and production flexibility requirements.

---

## NA Beer and New Product Accuracy

For non-alcoholic beer and other new-launch SKUs, percentage-based metrics are often inappropriate in the first 12 months. Absolute error (cases or equivalent units) is more useful:

- It is stable even when actual sales volumes are small.
- It connects directly to inventory impact.
- It forces a meaningful conversation about whether a 200-case error on a 1,000-case forecast is acceptable, rather than hiding behind "20% MAPE" which sounds equivalent regardless of scale.

New SKU accuracy should be tracked on a separate dashboard, with explicit acknowledgment that the analogue-based or Bayesian methods used for new product forecasting (see [Forecasting With No History: The Non-Alcoholic Beer Problem]({{ '/2025/forecasting-new-products-na-beer/' | relative_url }})) will produce higher errors than mature SKU models — and that this is expected, not a failure.

---

## The Accuracy Reporting Trap

There is a subtle but important distinction between measuring accuracy to improve the forecast and measuring accuracy to report a number. The latter is surprisingly common: accuracy metrics become KPIs managed for appearance rather than for insight.

Signs of the reporting trap: accuracy is only calculated for the periods after the last major error; low-volume SKUs are excluded from the calculation without documented rationale; the accuracy metric moves in lockstep with volume growth (because high-volume SKUs are easier to forecast) but is interpreted as methodological improvement.

The antidote is to define the accuracy measurement methodology once, document it, and apply it consistently across periods, SKUs, and planning cycles — including the ones where performance was poor.

---

## The Honest Caveat

No accuracy metric, however well-designed, tells you whether the forecast is good enough for the decision it supports. A 25% WMAPE may be perfectly acceptable for a low-margin seasonal SKU where the supply flexibility is high; it may be disqualifying for a high-margin, long-lead-time product. Contextualising accuracy targets by SKU class, lead time, and margin profile is the work that turns a metric dashboard into a planning tool.

*Part of the Sales Forecasting track — [browse all]({{ '/tags/' | relative_url }}#forecasting).*

---

## Frequently asked questions

**What is the best forecast accuracy metric for beer demand planning?**  
There is no single best metric — the right choice depends on the decision being supported. WMAPE (weighted mean absolute percentage error) is the most widely used operational metric for SKU-level supply planning because it naturally weights high-volume SKUs more heavily. Bias (or CFE, cumulative forecast error) is equally important because a low-error model that is consistently directionally wrong creates systematic inventory imbalances.

**Why is MAPE a problematic forecast accuracy metric?**  
MAPE (mean absolute percentage error) is symmetric in percentage terms but asymmetric in business impact when applied to low-volume SKUs. A SKU selling 10 cases per week where you forecast 5 generates a 50% error; forecasting 15 also generates a 50% error — but the supply chain consequences are very different. MAPE also breaks down when actual values are near zero, which is common for new or seasonal SKUs.

**How should forecast accuracy be reported for a non-alcoholic beer portfolio with new SKUs?**  
New NA SKUs should be reported separately from mature SKUs, with absolute error (cases or units) rather than percentage error, given the low volumes in early periods. Mixing new product accuracy into a MAPE calculation that includes high-volume mature SKUs masks performance in both directions.
