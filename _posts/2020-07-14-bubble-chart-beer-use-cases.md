---
layout: post
title: "The Bubble Chart in Brewing: Three Beer Use Cases"
image: /assets/og/bubble-chart-beer-use-cases.png
description: "A scatter plot with a third variable encoded as bubble size — show volume, value and growth together. Three beer use cases (portfolio maps, account prioritisation, market opportunity) and why size can mislead."
date: 2020-07-14 09:00:00 -0700
updated: 2020-07-14
tags: [brewing-science, beer-chart-guide, data-visualization, commercial-planning, sales-intelligence]
faq:
  - q: "What is a bubble chart and when should a brewery use one?"
    a: "A bubble chart is a scatter plot with a third variable mapped to the size of each point, so you show three dimensions at once — for example growth rate (x), margin (y) and volume (bubble size) across brands. Breweries use it for portfolio maps, account prioritisation (value, effort, size), and market opportunity (size, growth, fit). It's the chart for 'three things matter and I want them in one picture.'"
  - q: "Why can bubble size be misleading?"
    a: "Because people judge area imprecisely and some tools scale bubbles by radius instead of area, which exaggerates large values. Always size bubbles by area, keep the size range moderate, and label key bubbles with the actual value. Reserve size for a variable where rough magnitude is enough, not one needing precise comparison."
  - q: "Bubble chart or scatter plot?"
    a: "Use a plain scatter when two variables tell the story — adding a third as size only when that third dimension genuinely matters and rough magnitude suffices. If you find yourself squinting to compare bubble sizes, the third variable probably deserves its own chart, or belongs on a colour scale or a small table instead."
---

**Short answer: a bubble chart is a scatter plot with a third variable encoded as bubble size, letting you show three dimensions at once — growth, margin and volume across brands; value, effort and size across accounts. It's the natural chart for "three things matter and I want them together," like a BCG-style portfolio map. The catch: people read area imprecisely and tools sometimes mis-scale bubbles, so size is for rough magnitude, never precise comparison — label the bubbles that matter.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A bubble chart positioning beer brands by growth on the x-axis and margin on the y-axis, with bubble size showing volume, forming quadrants."><rect width="1000" height="240" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">BUBBLE — THREE VARIABLES IN ONE PICTURE</text><line x1="120" y1="200" x2="900" y2="200" stroke="#4a6b64"/><line x1="120" y1="50" x2="120" y2="200" stroke="#4a6b64"/><line x1="510" y1="50" x2="510" y2="200" stroke="#a9ddd0" stroke-dasharray="4 4"/><line x1="120" y1="125" x2="900" y2="125" stroke="#a9ddd0" stroke-dasharray="4 4"/><circle cx="300" cy="95" r="34" fill="#00695c" fill-opacity="0.55" stroke="#00695c"/><text x="300" y="98" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#06483f">Lager</text><circle cx="680" cy="85" r="22" fill="#00695c" fill-opacity="0.55" stroke="#00695c"/><text x="680" y="88" text-anchor="middle" font-family="sans-serif" font-size="8.5" fill="#06483f">IPA</text><circle cx="700" cy="160" r="14" fill="#06483f" fill-opacity="0.55" stroke="#06483f"/><text x="700" y="163" text-anchor="middle" font-family="sans-serif" font-size="8" fill="#06483f">NA</text><circle cx="270" cy="165" r="18" fill="#06483f" fill-opacity="0.55" stroke="#06483f"/><text x="270" y="168" text-anchor="middle" font-family="sans-serif" font-size="8" fill="#06483f">Stout</text><text x="906" y="205" font-family="sans-serif" font-size="9.5" fill="#4a6b64">growth &#8594;</text><text x="120" y="44" text-anchor="middle" font-family="sans-serif" font-size="9.5" fill="#4a6b64">margin</text><text x="500" y="230" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#4a6b64">x: growth   y: margin   size: volume — quadrants reveal stars, drains and bets</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Position for two variables, size for the third: a portfolio's shape in one frame.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). It extends the [scatter plot]({{ '/2020/scatter-plot-beer-use-cases/' | relative_url }}) with a third dimension.

## When to reach for it

Reach for a bubble chart when **three variables matter together** and rough magnitude is enough for the third — two on the axes, one as size. It's the classic portfolio map: position tells you where, size tells you how much.

## Use case 1 — Brand portfolio map

Growth (x), margin (y), volume (size). Quadrants reveal your stars (high growth, high margin, big), your cash cows, and your problem children — the [commercial planning]({{ '/tracks/commercial-planning/' | relative_url }}) conversation in one chart.

## Use case 2 — Account prioritisation

Value (x), cost to serve (y), current volume (size). It turns "which accounts deserve attention" into a visible map — big bubbles in the wrong quadrant are your priorities, a richer [sales intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) view than a list.

## Use case 3 — Market or style opportunity

Category growth (x), your fit/right-to-win (y), market size (size). A big bubble high-and-right is where to launch next — a [marketing]({{ '/tracks/marketing/' | relative_url }}) opportunity scan that holds three factors at once.

## Where this breaks

**Area is imprecise** — size shows rough magnitude only; label key bubbles. **Radius vs area scaling** — ensure your tool sizes by area, or large values explode; check it. **Overlap** — big bubbles occlude small ones; use transparency and sensible size ranges. **Too many bubbles** — a crowded map is unreadable; cap the items or filter.

## The bottom line

The bubble chart shows three variables at once — position for two, size for the third — making it the go-to portfolio and prioritisation map for brands, accounts and opportunities. Keep size for rough magnitude, scale by area, label what matters, and don't overcrowd. Next, the distribution of a single variable: the [histogram]({{ '/2020/histogram-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**What is a bubble chart and when should a brewery use one?**
A bubble chart is a scatter plot with a third variable mapped to the size of each point, so you show three dimensions at once — for example growth rate (x), margin (y) and volume (bubble size) across brands. Breweries use it for portfolio maps, account prioritisation (value, effort, size), and market opportunity (size, growth, fit). It's the chart for "three things matter and I want them in one picture."

**Why can bubble size be misleading?**
Because people judge area imprecisely and some tools scale bubbles by radius instead of area, which exaggerates large values. Always size bubbles by area, keep the size range moderate, and label key bubbles with the actual value. Reserve size for a variable where rough magnitude is enough, not one needing precise comparison.

**Bubble chart or scatter plot?**
Use a plain scatter when two variables tell the story — adding a third as size only when that third dimension genuinely matters and rough magnitude suffices. If you find yourself squinting to compare bubble sizes, the third variable probably deserves its own chart, or belongs on a colour scale or a small table instead.
