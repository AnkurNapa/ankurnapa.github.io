---
layout: post
title: "The Line Chart in Brewing: Three Beer Use Cases"
image: /assets/og/line-chart-beer-use-cases.png
description: "For anything that changes over time, the line chart is the default and usually the right one. Three beer use cases (fermentation curves, sales trends and seasonality, KPI vs target over time) and the rules that keep it readable."
date: 2020-04-21 09:00:00 -0700
updated: 2020-04-21
tags: [brewing-science, beer-chart-guide, data-visualization, sales-forecasting, fermentation]
faq:
  - q: "When should a brewery use a line chart?"
    a: "For anything that changes over time and where the trend, shape or rate of change is the message — fermentation gravity curves, daily or monthly sales, a KPI tracked against target. Lines connect points in time so the eye reads direction and slope naturally. It's the default for time series and usually the correct one."
  - q: "How many lines can one chart hold?"
    a: "Comfortably three to five if they're well separated; more becomes spaghetti. When you need many series, use small multiples (one mini-line-chart per series on shared axes) or highlight one or two lines and grey the rest. Direct-labelling lines at their end beats a legend the eye has to hunt through."
  - q: "Line chart or bar chart for beer sales over time?"
    a: "Line chart when you have many time periods and the trend is the point — twelve months, daily readings. Bar chart when periods are few and discrete and you want to compare their magnitudes — four quarters side by side. If in doubt for a continuous trend, the line reads the change more clearly."
---

**Short answer: the line chart is the default for anything that changes over time, and usually the right one, because connecting points lets the eye read direction, slope and turning points instantly. In a brewery it's the fermentation curve, the sales trend, the KPI tracked against target. Keep it to a few well-separated lines (or use small multiples for many), start the axis thoughtfully, and direct-label the lines. For continuous time series, almost nothing beats it.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A line chart with two fermentation gravity curves descending over days, one normal and one stalling, on shared axes."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">LINE CHART — CHANGE OVER TIME</text><line x1="80" y1="200" x2="940" y2="200" stroke="#6b6258"/><line x1="80" y1="60" x2="80" y2="200" stroke="#6b6258"/><polyline points="90,72 200,80 320,108 440,140 560,164 680,178 800,184 920,186" fill="none" stroke="#b45309" stroke-width="2.4"/><polyline points="90,74 200,86 320,120 440,140 560,146 680,148 800,149 920,149" fill="none" stroke="#7a1f3d" stroke-width="2.2" stroke-dasharray="6 3"/><text x="930" y="190" font-family="sans-serif" font-size="9.5" fill="#b45309">normal</text><text x="930" y="146" font-family="sans-serif" font-size="9.5" fill="#7a1f3d">stalling</text><text x="500" y="224" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#6b6258">slope and shape carry the meaning — a stall is a flattening line</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Two gravity curves: the healthy one keeps falling, the stalling one flattens early — the shape tells the story.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). If the question has "over time" in it, this is usually your chart.

## When to reach for it

Reach for a line whenever the data is **ordered in time** and the **trend, slope or turning point** is the message. Lines imply continuity, so use them for things that genuinely flow (gravity, temperature, sales over many periods) rather than a handful of unrelated categories.

## Use case 1 — Fermentation and process curves

Gravity, temperature or pH over the course of a ferment, with a healthy reference curve overlaid. A stall shows up as a flattening line long before a number does — the visual backbone of any [fermentation monitoring]({{ '/2023/tableau-fermentation-monitoring-dashboard/' | relative_url }}) view.

## Use case 2 — Sales trend and seasonality

Monthly or weekly volume across a year or more, where the line exposes seasonality, the summer peak, the trend beneath the noise. Add a prior-year line to see growth, the staple of [sales forecasting]({{ '/tracks/sales-forecasting/' | relative_url }}).

## Use case 3 — A KPI against its target over time

Plot the metric and draw the target as a flat reference line. Whether you're above or below, and trending which way, is instantly readable — the honest version of a KPI tile, with history attached.

## Where this breaks

**Spaghetti** — more than ~5 lines blur together; use small multiples or highlight one. **Misleading axis** — for trends a non-zero axis is often fine (unlike bars), but be deliberate and label it. **False continuity** — don't connect points that aren't a real sequence; a line implies "in between" values exist. **Discrete few periods** — four quarters may read better as [bars]({{ '/2020/bar-chart-beer-use-cases/' | relative_url }}).

## The bottom line

The line chart is the default for time and usually the right call: fermentation curves, sales trends, KPIs vs target. Keep the lines few and labelled, choose the axis deliberately, and don't imply continuity that isn't there. When you need two different metrics on one time axis, the next chart handles it: the [combo line + bar]({{ '/2020/combo-line-bar-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**When should a brewery use a line chart?**
For anything that changes over time and where the trend, shape or rate of change is the message — fermentation gravity curves, daily or monthly sales, a KPI tracked against target. Lines connect points in time so the eye reads direction and slope naturally. It's the default for time series and usually the correct one.

**How many lines can one chart hold?**
Comfortably three to five if they're well separated; more becomes spaghetti. When you need many series, use small multiples (one mini-line-chart per series on shared axes) or highlight one or two lines and grey the rest. Direct-labelling lines at their end beats a legend the eye has to hunt through.

**Line chart or bar chart for beer sales over time?**
Line chart when you have many time periods and the trend is the point — twelve months, daily readings. Bar chart when periods are few and discrete and you want to compare their magnitudes — four quarters side by side. If in doubt for a continuous trend, the line reads the change more clearly.
