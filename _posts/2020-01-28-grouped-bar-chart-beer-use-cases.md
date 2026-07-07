---
layout: post
title: "The Grouped Bar Chart in Brewing: Three Beer Use Cases"
image: /assets/og/grouped-bar-chart-beer-use-cases.png
description: "When you need to compare several series side by side — this year vs last, plan vs actual, style across regions — the grouped (clustered) bar chart is the tool. Three beer use cases and when to switch to a different chart."
date: 2020-01-28 09:00:00 -0700
updated: 2020-01-28
tags: [brewing-science, beer-chart-guide, data-visualization, sales-forecasting, commercial-planning]
faq:
  - q: "What is a grouped bar chart used for in a brewery?"
    a: "Comparing two or three series across the same categories — this year versus last year by style, plan versus actual by brand, or volume by style across regions. Each category gets a small cluster of bars, one per series, so you compare both within a category and across categories. It's the go-to for 'how does A compare to B across these groups.'"
  - q: "Grouped bar chart or stacked bar chart?"
    a: "Use grouped (side-by-side) bars when you want to compare the individual series against each other — actual vs plan, this year vs last. Use a stacked bar when the series are parts of a whole and the total matters — channel mix within total volume. Grouped answers 'which series is bigger'; stacked answers 'what's the composition.'"
  - q: "How many series can a grouped bar chart show?"
    a: "Two or three per cluster, rarely more. Beyond that the clusters get wide, the categories crowd, and comparison collapses into clutter. If you have many series or many time periods, switch to a line chart (for time) or small multiples (one mini-chart per series) instead."
---

**Short answer: the grouped (clustered) bar chart compares two or three series across the same categories — this year vs last year by style, plan vs actual by brand, volume by style across regions. Each category gets a little cluster of bars, so you read both within a category (is actual beating plan?) and across categories (which brand has the biggest gap?). Keep it to two or three series; beyond that it becomes clutter, and a line chart or small multiples does the job better.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A grouped bar chart comparing this year versus last year volume across four beer styles, two bars per style."><rect width="1000" height="240" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">GROUPED BAR — COMPARE SERIES SIDE BY SIDE</text><line x1="80" y1="200" x2="940" y2="200" stroke="#4a6b64"/><g font-family="sans-serif" font-size="10"><rect x="140" y="86" width="42" height="114" fill="#00695c"/><rect x="186" y="104" width="42" height="96" fill="#06483f"/><text x="184" y="216" text-anchor="middle" fill="#4a6b64">Lager</text><rect x="340" y="110" width="42" height="90" fill="#00695c"/><rect x="386" y="96" width="42" height="104" fill="#06483f"/><text x="384" y="216" text-anchor="middle" fill="#4a6b64">IPA</text><rect x="540" y="140" width="42" height="60" fill="#00695c"/><rect x="586" y="150" width="42" height="50" fill="#06483f"/><text x="584" y="216" text-anchor="middle" fill="#4a6b64">Wheat</text><rect x="740" y="158" width="42" height="42" fill="#00695c"/><rect x="786" y="138" width="42" height="62" fill="#06483f"/><text x="784" y="216" text-anchor="middle" fill="#4a6b64">NA</text></g><g font-family="sans-serif" font-size="10"><rect x="690" y="44" width="12" height="12" fill="#00695c"/><text x="708" y="54" fill="#4a6b64">last year</text><rect x="790" y="44" width="12" height="12" fill="#06483f"/><text x="808" y="54" fill="#4a6b64">this year</text></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Two bars per category: read within (this year vs last) and across (which style grew most).</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). The [plain bar chart]({{ '/2020/bar-chart-beer-use-cases/' | relative_url }}) compares one series; the grouped bar adds a second or third.

## When to reach for it

Reach for grouped bars when you have the **same categories measured under two or three conditions** and you want to compare the conditions directly. The clusters let the eye do two comparisons at once — within each category and across them — which is exactly the "did we beat last year, and where" question.

## Use case 1 — This year vs last year, by style

Two bars per style. You see growth and decline per style *and* rank which styles moved most — far richer than two separate charts, and the standard view in any [commercial planning]({{ '/tracks/commercial-planning/' | relative_url }}) review.

## Use case 2 — Plan vs actual, by brand

Plan and actual side by side per brand makes the gap a visible distance. Add a third bar for prior year if it doesn't crowd. This is the workhorse of an S&OP or [sales-forecasting]({{ '/tracks/sales-forecasting/' | relative_url }}) review meeting.

## Use case 3 — A metric across regions

Volume (or rate of sale) by style, clustered by region, shows where a style over- or under-indexes — the West loves the IPA, the South the lager. It turns "regional differences" from a claim into a picture.

## Where this breaks

**Too many series** — two or three bars per cluster is the limit; more becomes a picket fence. **Too many categories × series** — the product crowds fast; cap categories or split. **Time series** — for many time periods a [line chart]({{ '/2020/line-chart-beer-use-cases/' | relative_url }}) beats grouped bars; for many series, [small multiples]({{ '/2026/shelf-life-flavour-stability-trial-viz/' | relative_url }}) read cleaner.

## The bottom line

The grouped bar chart is for comparing two or three series across shared categories — this year vs last, plan vs actual, style across regions — letting the eye compare within and across at once. Keep series and categories few, start at zero, and switch to lines or small multiples when it crowds. Next: when the series are *parts of a whole*, the [stacked bar chart]({{ '/2020/stacked-bar-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**What is a grouped bar chart used for in a brewery?**
Comparing two or three series across the same categories — this year versus last year by style, plan versus actual by brand, or volume by style across regions. Each category gets a small cluster of bars, one per series, so you compare both within a category and across categories. It's the go-to for "how does A compare to B across these groups."

**Grouped bar chart or stacked bar chart?**
Use grouped (side-by-side) bars when you want to compare the individual series against each other — actual vs plan, this year vs last. Use a stacked bar when the series are parts of a whole and the total matters — channel mix within total volume. Grouped answers "which series is bigger"; stacked answers "what's the composition."

**How many series can a grouped bar chart show?**
Two or three per cluster, rarely more. Beyond that the clusters get wide, the categories crowd, and comparison collapses into clutter. If you have many series or many time periods, switch to a line chart (for time) or small multiples (one mini-chart per series) instead.
