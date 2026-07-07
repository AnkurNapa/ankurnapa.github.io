---
layout: post
title: "Forecasting With No History: The Non-Alcoholic Beer Problem"
image: /assets/og/forecasting-new-products-na-beer.png
description: "New product forecasting for non-alcoholic beer with no sales history — analogue methods, Bayesian priors, and practical launch-stage approaches."
date: 2025-03-14
updated: 2025-03-14
tags: [forecasting, new-product-forecasting]
faq:
  - q: "How do you forecast a product with no sales history?"
    a: "The standard approach is analogue forecasting: identify two to five comparable products from previous launches, index their early growth curves, and use that pattern as the starting demand prior. Bayesian methods then update the forecast as early shipment data arrives."
  - q: "Why is non-alcoholic beer especially hard to forecast?"
    a: "NA beer sits at the intersection of multiple uncertain signals — it partially follows standard beer seasonality, partly tracks wellness and lifestyle trends, and its buyer base often differs from conventional beer drinkers. There are also few long-run analogues given how recently the category scaled."
  - q: "When should a brewery switch from analogue forecasting to a data-driven model for NA beer?"
    a: "Roughly 18–24 months of consistent weekly depletion data at the SKU level is the practical threshold before statistical time-series methods become reliable. Before that, a well-maintained analogue model with Bayesian updating will generally outperform a naively fitted statistical model."
---

**Short answer:** Non-alcoholic beer is one of the hardest commercial forecasting problems in beverages today — high growth, novel buyer behaviour, limited history, and significant cannibalization risk against the core lager portfolio. The right toolkit is analogue-based forecasting at launch, Bayesian updating as data accumulates, and honest scenario ranges rather than false-precision point forecasts.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The operating loop this post describes"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE OPERATING LOOP</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Forecasting With No History: The Non-Alcoholic Beer Problem</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Measure</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">data in</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analyse</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">find the signal</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Decide</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">choose</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Act</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">change the floor</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">repeat</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The operating loop this post describes: measure, analyse, decide, act — then repeat.</figcaption>
</figure>

## The Cold-Start Problem in Beverage Innovation

Every new product launch faces a cold-start problem: the demand signal that powers forecasting models simply does not exist yet. For most line extensions — a new seasonal variant of an existing brand — the cold start is manageable. Planners can anchor on the parent brand's velocity and adjust.

Non-alcoholic beer is different. The category itself is new at scale in most markets. The consumer is often distinct from the core beer buyer. The usage occasion (designated-driver moment, Dry January, fitness lifestyle) does not map neatly onto the seasonal or weekly rhythms that drive conventional beer planning. And the stakes are rising: NA is one of the fastest-growing segments in off-premise beer, making forecast error costly.

---

## Analogue Forecasting: The Practical Starting Point

The core technique for new product forecasting — regardless of category — is analogue selection. The process is methodical, not creative:

1. **Define the analogue criteria.** What makes a good comparable? Consider: launch channel (on-premise vs. off-premise), distribution rollout pace (regional vs. national), parent brand equity, price point, and packaging format.
2. **Index early-stage trajectories.** Pull depletion curves for the selected analogues from weeks 1 through 52. Normalise to a common launch baseline. The range of outcomes across analogues becomes your forecast cone.
3. **Weight analogues by similarity.** A pure malt NA lager from a major craft brand is a better analogue for a similar launch than a flavoured seltzer, even if both are "low-ABV beverages." Apply judgment explicitly — the weighting should be documented and reviewable.
4. **Generate three scenarios.** Use the upper quartile, median, and lower quartile of analogue performance as optimistic, base, and conservative cases. Resist the pressure to collapse these into a single point forecast for the launch plan.

The weakness of pure analogue forecasting is that analogues are historical. The NA beer category has changed substantially even in the past 36 months — earlier analogues may understate the current rate of growth, or overstate distribution velocity for a smaller brand.

---

## Bayesian Updating: Learning From Early Signals

Analogue forecasts should never be static. A Bayesian framework treats the analogue curve as a prior and updates it as actual data arrives. The mechanics can range from simple (manually recalibrating the analogue weights based on actual vs. expected weeks 1–8) to formal (a hierarchical Bayesian model that updates SKU-level parameters from each week's depletion data).

In practice, most beverage commercial teams can implement a light Bayesian discipline without specialist data science resources:

- Review actuals vs. analogue-based forecast at weeks 4, 8, and 13 post-launch.
- Document whether the NA SKU is tracking the upper, middle, or lower analogue quartile.
- Update production plans and distribution commitments accordingly.

The key discipline is separating distribution-driven volume gains (more accounts stocking the product) from genuine velocity gains (each account selling more). A model that conflates the two will overforecast once distribution plateaus.

---

## Category-Level Context as a Guardrail

Even without SKU-level history, category-level data provides useful guardrails. If the NA beer category in a given market is growing at a directionally observable rate and your new product is launching into that trend, the category growth rate constrains the plausible range of outcomes. A brand expecting to capture a realistic share of that growth can bound the forecast from above; a conservative floor is set by the typical failure rate of innovation launches in the broader beer category.

This two-sided constraint — category ceiling, innovation base rate floor — is a practical hedge against both over-optimism in sales planning and excessive conservatism in supply commitments.

For context on how NA beer interacts with the broader lager portfolio from a cannibalization perspective, see [Cannibalization: Does Non-Alcoholic Beer Eat Your Lager's Sales?]({{ '/2025/cannibalization-na-beer-lager/' | relative_url }}).

---

## The Honest Caveat

No forecasting method eliminates the fundamental uncertainty of a new product launch. The analogue and Bayesian approaches described here reduce error and force explicitness about assumptions — they do not produce accurate point forecasts. Commercial leaders should insist on seeing forecast ranges rather than single numbers, and supply teams should use those ranges to plan inventory buffers explicitly rather than treating the midpoint as a certainty.

The broader question of when to trust models versus human judgment is explored in [The Honest Limits of Sales Forecasting]({{ '/2026/honest-limits-sales-forecasting/' | relative_url }}).

*Part of the Sales Forecasting track — [browse all]({{ '/tags/' | relative_url }}#forecasting).*

---

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="History (solid) and the model&#39;s forward forecast (dashed); the shaded band is its uncertainty."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FORECAST</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Forecasting With No History: The Non-Alcoholic Beer Problem</text><g stroke="#06483f" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#00695c" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#00695c" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#06483f" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">today</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">history</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">forecast</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">History (solid) and the model&#39;s forward forecast (dashed); the shaded band is its uncertainty.</figcaption>
</figure>

## Frequently asked questions

**How do you forecast a product with no sales history?**  
The standard approach is analogue forecasting: identify two to five comparable products from previous launches, index their early growth curves, and use that pattern as the starting demand prior. Bayesian methods then update the forecast as early shipment data arrives.

**Why is non-alcoholic beer especially hard to forecast?**  
NA beer sits at the intersection of multiple uncertain signals — it partially follows standard beer seasonality, partly tracks wellness and lifestyle trends, and its buyer base often differs from conventional beer drinkers. There are also few long-run analogues given how recently the category scaled.

**When should a brewery switch from analogue forecasting to a data-driven model for NA beer?**  
Roughly 18–24 months of consistent weekly depletion data at the SKU level is the practical threshold before statistical time-series methods become reliable. Before that, a well-maintained analogue model with Bayesian updating will generally outperform a naively fitted statistical model.
