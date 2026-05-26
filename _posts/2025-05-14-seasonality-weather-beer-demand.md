---
layout: post
title: "Seasonality and Weather: Beer's Most Predictable Swings"
image: /assets/og/seasonality-weather-beer-demand.png
description: "How weather and seasonality drive beer demand forecasting — decomposition methods, temperature indices, and what changes for non-alcoholic beer."
date: 2025-05-14
updated: 2025-05-14
tags: [forecasting, weather-demand-forecasting]
faq:
  - q: "How much does weather actually affect beer sales?"
    a: "Temperature and sunshine are among the strongest short-run drivers of beer volume — particularly for off-premise and on-premise outdoor occasions. The effect is well-documented directionally across markets, though the exact magnitude varies by brand, channel, and region."
  - q: "How do you separate seasonality from an underlying trend in a beer forecast?"
    a: "Time-series decomposition (e.g. STL or classical multiplicative decomposition) splits a demand series into trend, seasonal, and residual components. The seasonal component captures the repeating calendar pattern; the trend captures the underlying growth or decline; the residual is where promotions, weather anomalies, and one-off events show up."
  - q: "Does non-alcoholic beer follow the same seasonal pattern as conventional beer?"
    a: "Partially. NA beer shares the summer outdoor-occasion uplift but tends to show a second peak in January around Dry January and wellness-motivated abstinence periods — a pattern that conventional beer does not exhibit. Planners should model NA seasonality separately rather than assuming it mirrors lager."
---

**Short answer:** Seasonality is the most modellable driver in beer demand — it is repeating, quantifiable, and visible in every mature dataset. Weather adds a secondary layer of short-run variability. Together they account for a large share of the predictable variance in beer volume, making them the highest-ROI signals to embed in any forecasting model. Non-alcoholic beer shares the summer pattern but adds a distinctive January peak that conventional beer lacks.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The operating loop this post describes"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">THE OPERATING LOOP</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Seasonality and Weather: Beer&#39;s Most Predictable Swings</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Measure</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">data in</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analyse</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">find the signal</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Decide</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">choose</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Act</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">change the floor</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,52 840,52 800,52 L160,52 C140,52 140,52 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="46" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">repeat</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The operating loop this post describes: measure, analyse, decide, act — then repeat.</figcaption>
</figure>

## Why Seasonality Is the Foundation, Not a Refinement

Demand forecasting in beverages often treats seasonality as an adjustment applied after the "real" forecast is built. That framing is backwards. For most beer SKUs, the seasonal component explains the majority of week-to-week volume variation. A model that strips out seasonality first — and forecasts the de-seasonalised trend separately — will dramatically outperform one that tries to forecast raw volume directly.

The practical implication: every brewery operating above Stage 1 maturity (see [The Beverage Demand Forecasting Maturity Model]({{ '/2025/demand-forecasting-maturity-model/' | relative_url }})) should implement seasonal decomposition before adding any other forecasting sophistication.

---

## Decomposing the Signal: STL and Its Variants

STL (Seasonal and Trend decomposition using Loess) is the workhorse method for beverage seasonality. It offers several advantages over classical decomposition:

- **Robustness to outliers.** Promotional spikes, stock-outs, and COVID-era distortions are treated as residuals rather than distorting the seasonal estimate.
- **Flexible seasonal windows.** Beer may have both a weekly pattern (Friday-Saturday uplift in on-premise) and an annual pattern (summer peak, Q4 holiday bump). STL handles multiple periodicities.
- **Updatable.** Unlike classical methods that require a full year of history to re-estimate, STL seasonal estimates can be updated incrementally as new data arrives.

A practical starting point for a regional lager SKU: decompose three to five years of weekly depletion data, inspect the seasonal component visually, and confirm it is stable across years before assuming it will repeat. If the seasonal shape is shifting — as it may be for brands with changing distribution or a growing on-trade presence — a model that allows the seasonal component to evolve year-on-year is preferable.

---

## Weather as a Driver: Useful, but Not a Substitute for Process

Temperature and sunshine hours are genuine demand drivers for beer, particularly in off-premise and outdoor on-premise channels. The mechanism is intuitive: warm weather increases the frequency and size of informal outdoor consumption occasions.

Adding a temperature index to a regression-based forecast can improve short-run accuracy, especially during shoulder seasons (April–May, September–October) when year-on-year comparisons are noisiest. The practical approach:

1. Obtain historical daily temperature data for the key markets in the distribution footprint.
2. Aggregate to a weekly "cooling degree days" or simple above-threshold temperature index.
3. Include the index as a feature in a driver-based regression alongside distribution, promotional flags, and time trend.
4. When producing a forward forecast, use weather service probabilistic forecasts for the nearest 4–8 weeks; revert to seasonal norms for longer horizons.

**The limits of weather modelling** deserve equal attention. Weather explains volume volatility within a season — it does not explain why one summer outperforms another by more than expected. Distribution gains, competitive dynamics, and macro consumer confidence do more work at the annual level. Overweighting weather in the annual plan creates a false sense of precision.

---

## Non-Alcoholic Beer: A Different Seasonal Shape

NA beer's seasonal profile diverges from conventional beer in one important respect: the January spike. Dry January has become a genuine demand event in several key markets, concentrated in the first three weeks of the year. For well-distributed NA SKUs, January now rivals or exceeds summer as the highest-demand period of the calendar year.

Planners who apply a conventional beer seasonal index to NA SKUs will systematically underforecast January and potentially overforecast summer. The fix is straightforward but requires explicit modelling: build a separate seasonal index for NA lines rather than inheriting it from the broader portfolio.

Weather effects on NA beer are less certain. The casual, high-ABV outdoor occasion is less central to the NA buyer's motivation. More research is needed before confidently attributing the same temperature sensitivity to NA that conventional lager exhibits.

---

## The Honest Caveat

Seasonality models are only as good as the history they are built on. If the past three years included a pandemic, a distribution restructuring, or a major competitive entry, the "seasonal" component extracted by the model will contain artefacts from those events. Visual inspection of decomposition outputs — not just statistical fit measures — is an essential quality check before any seasonal model is put into production planning.

*Part of the Sales Forecasting track — [browse all]({{ '/tags/' | relative_url }}#forecasting).*

---

## Frequently asked questions

**How much does weather actually affect beer sales?**  
Temperature and sunshine are among the strongest short-run drivers of beer volume — particularly for off-premise and on-premise outdoor occasions. The effect is well-documented directionally across markets, though the exact magnitude varies by brand, channel, and region.

**How do you separate seasonality from an underlying trend in a beer forecast?**  
Time-series decomposition (e.g. STL or classical multiplicative decomposition) splits a demand series into trend, seasonal, and residual components. The seasonal component captures the repeating calendar pattern; the trend captures the underlying growth or decline; the residual is where promotions, weather anomalies, and one-off events show up.

**Does non-alcoholic beer follow the same seasonal pattern as conventional beer?**  
Partially. NA beer shares the summer outdoor-occasion uplift but tends to show a second peak in January around Dry January and wellness-motivated abstinence periods — a pattern that conventional beer does not exhibit. Planners should model NA seasonality separately rather than assuming it mirrors lager.
