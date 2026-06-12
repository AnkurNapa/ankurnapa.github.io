---
layout: post
title: "The Scatter Plot in Brewing: Three Beer Use Cases"
image: /assets/og/scatter-plot-beer-use-cases.png
description: "When the question is 'are these two things related,' the scatter plot is the answer — each point a batch, account or beer. Three beer use cases (process correlations, account value vs effort, recipe trade-offs) and the correlation-isn't-causation rule."
date: 2026-06-11 07:20:00 -0700
updated: 2026-06-11
tags: [brewing-science, beer-chart-guide, data-visualization, quality-control, sales-intelligence]
faq:
  - q: "When should a brewery use a scatter plot?"
    a: "When you want to see the relationship between two numeric variables across many items — fermentation temperature versus ester level across batches, original gravity versus final attenuation, account volume versus servicing cost. Each point is one batch, account or beer, and the cloud's shape shows whether and how the two variables move together."
  - q: "What can a scatter plot reveal that a line chart can't?"
    a: "A line chart shows one variable over time; a scatter shows how two variables relate across many cases, regardless of time. It reveals correlation strength, clusters, and outliers — the one odd batch sitting away from the cloud. It's the natural first look before any predictive model, because it shows whether a relationship even exists to model."
  - q: "Does a scatter plot prove causation?"
    a: "No. A scatter shows that two variables move together (correlation), not that one causes the other. A lurking third factor can drive both, or the relationship can be coincidence. Use the scatter to spot a relationship worth investigating, then test it properly — never present a trend line on a scatter as proof that changing X will change Y."
---

**Short answer: the scatter plot answers "are these two things related?" — each point a batch, account or beer, plotted by two numeric variables. In a brewery it reveals process correlations (fermentation temperature vs ester level), commercial trade-offs (account value vs cost to serve) and recipe relationships, plus the outliers that sit away from the cloud. It's the natural first look before any model — but it shows correlation, never causation, so treat a relationship as a lead to investigate, not proof.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A scatter plot of fermentation temperature versus ester level, points rising to the right with one clear outlier above the cloud."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">SCATTER — RELATIONSHIP BETWEEN TWO VARIABLES</text><line x1="120" y1="200" x2="900" y2="200" stroke="#6b6258"/><line x1="120" y1="60" x2="120" y2="200" stroke="#6b6258"/><line x1="150" y1="184" x2="860" y2="92" stroke="#cbb89a" stroke-width="2" stroke-dasharray="6 4"/><g fill="#b45309"><circle cx="170" cy="182" r="5"/><circle cx="220" cy="176" r="5"/><circle cx="280" cy="170" r="5"/><circle cx="330" cy="158" r="5"/><circle cx="390" cy="160" r="5"/><circle cx="440" cy="146" r="5"/><circle cx="500" cy="140" r="5"/><circle cx="560" cy="128" r="5"/><circle cx="620" cy="124" r="5"/><circle cx="690" cy="112" r="5"/><circle cx="760" cy="104" r="5"/><circle cx="820" cy="96" r="5"/></g><circle cx="520" cy="78" r="6" fill="#7a1f3d"/><text x="540" y="74" font-family="sans-serif" font-size="9.5" fill="#7a1f3d">outlier batch</text><text x="500" y="222" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">x: ferment temperature   y: ester level — the cloud trends up; one batch sits apart</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Each dot is a batch. The upward cloud suggests a relationship; the lone high point is worth a look.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). When the question is about a *relationship* rather than a trend or a ranking, this is the chart.

## When to reach for it

Reach for a scatter when you have **two numeric variables measured across many items** and you want to know whether they move together. The shape of the cloud — tight upward, loose, flat, clustered — answers it, and the stragglers reveal outliers no summary number would.

## Use case 1 — Process correlations

Fermentation temperature vs ester level, original gravity vs final attenuation, dissolved oxygen vs staling score — one point per batch. A clear cloud tells you a lever exists; a shapeless blob tells you it doesn't. This is the look you take before building any [predictive model]({{ '/2026/spc-capability-cusum-ewma-brewing/' | relative_url }}).

## Use case 2 — Account value vs cost to serve

Each account a point: revenue on one axis, servicing cost (drops, returns, support) on the other. The quadrants pop out — high-value-low-cost stars, high-cost-low-value drains — a sharp [sales intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) view that a ranked bar chart can't show.

## Use case 3 — Recipe or sensory trade-offs

Plot bitterness vs drinkability score, or hop rate vs cost-per-litre, across recipes to see the trade-off frontier and which recipes are off it (more bitter for no gain). Add a third variable as point size and it becomes a [bubble chart]({{ '/2026/bubble-chart-beer-use-cases/' | relative_url }}).

## Where this breaks

**Correlation isn't causation** — a relationship is a lead, not proof; a third factor may drive both. **Overplotting** — thousands of points become a blob; use transparency, sampling or density. **A trend line oversells** — fitting a line to a loose cloud implies more certainty than exists; show the scatter, not just the fit. **Spurious patterns** — with few points the eye invents relationships; be wary below a few dozen.

## The bottom line

The scatter plot reveals whether two variables are related — process levers, account economics, recipe trade-offs — and exposes outliers, making it the honest first look before any model. Read the cloud's shape, respect that correlation isn't causation, and handle overplotting. Add a third variable as size and you get the next chart: the [bubble chart]({{ '/2026/bubble-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**When should a brewery use a scatter plot?**
When you want to see the relationship between two numeric variables across many items — fermentation temperature versus ester level across batches, original gravity versus final attenuation, account volume versus servicing cost. Each point is one batch, account or beer, and the cloud's shape shows whether and how the two variables move together.

**What can a scatter plot reveal that a line chart can't?**
A line chart shows one variable over time; a scatter shows how two variables relate across many cases, regardless of time. It reveals correlation strength, clusters, and outliers — the one odd batch sitting away from the cloud. It's the natural first look before any predictive model, because it shows whether a relationship even exists to model.

**Does a scatter plot prove causation?**
No. A scatter shows that two variables move together (correlation), not that one causes the other. A lurking third factor can drive both, or the relationship can be coincidence. Use the scatter to spot a relationship worth investigating, then test it properly — never present a trend line on a scatter as proof that changing X will change Y.
