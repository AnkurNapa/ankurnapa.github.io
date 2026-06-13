---
layout: post
title: "The Area and Stacked Area Chart in Brewing: Three Beer Use Cases"
image: /assets/og/area-chart-beer-use-cases.png
description: "An area chart is a line chart with the space below filled — good for cumulative totals and, stacked, for how a composition shifts over time. Three beer use cases and when a line or stacked bar is the better call."
date: 2020-06-02 09:00:00 -0700
updated: 2020-06-02
tags: [brewing-science, beer-chart-guide, data-visualization, commercial-planning, sales-forecasting]
faq:
  - q: "When should a brewery use an area chart?"
    a: "Use a plain area chart to emphasise a cumulative total or magnitude over time — year-to-date volume building up, or a single series where the 'amount' feeling matters. Use a stacked area chart to show how a composition shifts over time — style mix or channel mix across months — when you want both the total trend and the changing shares in one view."
  - q: "Stacked area chart or stacked bar chart?"
    a: "Stacked area suits many time periods and a continuous sense of flow — twelve months of style mix reading as smooth bands. Stacked bars suit fewer, discrete periods where you compare exact totals. Both share the weakness that only the bottom band has a clean baseline, so reserve them for when the shifting composition, not precise per-band comparison, is the point."
  - q: "What is the weakness of a stacked area chart?"
    a: "Like the stacked bar, only the bottom band sits on a flat baseline, so the bands above it are hard to read precisely — their movement is part real, part caused by the bands beneath. With many bands it becomes a hard-to-read 'stacked spaghetti.' Keep bands few, put the most important or most stable one on the bottom, and switch to lines if precise per-series comparison matters."
---

**Short answer: an area chart is a line chart with the area beneath filled, which emphasises cumulative magnitude; the stacked area chart fills several series on top of each other to show how a composition shifts over time. In a brewery: year-to-date volume building, style mix flowing across months, channel share evolving. Its weakness mirrors the stacked bar — only the bottom band has a clean baseline — so use it when the *shifting shape over time* is the message, not precise per-band comparison.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A stacked area chart showing three beer styles' volume as filled bands over twelve months, the total rising and the mix shifting."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">STACKED AREA — COMPOSITION FLOWING OVER TIME</text><line x1="80" y1="200" x2="940" y2="200" stroke="#6b6258"/><path d="M80 200 L80 168 C 300 162, 600 150, 920 132 L 920 200 Z" fill="#b45309" fill-opacity="0.7"/><path d="M80 168 C 300 162, 600 150, 920 132 L 920 104 C 600 116, 300 128, 80 138 Z" fill="#8a5a2b" fill-opacity="0.65"/><path d="M80 138 C 300 128, 600 116, 920 104 L 920 78 C 600 92, 300 104, 80 118 Z" fill="#cbb89a" fill-opacity="0.8"/><g font-family="sans-serif" font-size="10"><rect x="120" y="210" width="0" height="0"/></g><g font-family="sans-serif" font-size="10"><rect x="700" y="208" width="0" height="0"/></g><text x="120" y="216" font-family="sans-serif" font-size="10" fill="#6b6258">Jan</text><text x="900" y="216" font-family="sans-serif" font-size="10" fill="#6b6258">Dec</text><text x="500" y="232" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#6b6258">total rises and the mix shifts — both visible as flowing bands</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Filled bands show the total growing and the composition changing across the year at once.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). It's the [line]({{ '/2020/line-chart-beer-use-cases/' | relative_url }}) and the [stacked bar]({{ '/2020/stacked-bar-chart-beer-use-cases/' | relative_url }}) crossed — a filled line for flow.

## When to reach for it

Reach for a **plain area** when one series' cumulative magnitude over time is the feeling you want (year-to-date building up). Reach for a **stacked area** when you want the **total trend and the shifting composition together** across many time periods — the continuous cousin of the stacked bar.

## Use case 1 — Year-to-date volume building

A single filled area climbing through the year conveys "how much we've made so far" more viscerally than a line. Useful on a progress-to-target tile where the accumulating mass is the point.

## Use case 2 — Style mix shifting over the year

Stack styles as bands across twelve months: the total rises while the IPA band fattens and the lager band thins. The mix evolution reads as flowing shape — a [commercial planning]({{ '/tracks/commercial-planning/' | relative_url }}) staple for portfolio drift.

## Use case 3 — Channel share over time

Off-/on-premise/e-commerce as stacked bands, or as a 100% stacked area, shows a channel gaining ground smoothly across the year — the trend version of the [channel-mix stacked bar]({{ '/2020/stacked-bar-chart-beer-use-cases/' | relative_url }}).

## Where this breaks

**Floating bands** — only the bottom band has a clean baseline; upper bands' movement is partly caused by those below, so don't read them precisely. **Stacked spaghetti** — many bands become unreadable; keep to three or four and put the stable one on the bottom. **Occlusion in overlapping (non-stacked) areas** — filled areas hide each other; use transparency or switch to lines. **Precise comparison** — if per-series exact values matter, use [lines]({{ '/2020/line-chart-beer-use-cases/' | relative_url }}).

## The bottom line

The area chart fills a line to emphasise magnitude; stacked, it shows total and composition flowing over time — YTD volume, style mix, channel share. Use it when the shifting shape is the message, keep bands few with the stable one on the bottom, and switch to lines when precise comparison matters. Next, relationships between two variables: the [scatter plot]({{ '/2020/scatter-plot-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**When should a brewery use an area chart?**
Use a plain area chart to emphasise a cumulative total or magnitude over time — year-to-date volume building up, or a single series where the "amount" feeling matters. Use a stacked area chart to show how a composition shifts over time — style mix or channel mix across months — when you want both the total trend and the changing shares in one view.

**Stacked area chart or stacked bar chart?**
Stacked area suits many time periods and a continuous sense of flow — twelve months of style mix reading as smooth bands. Stacked bars suit fewer, discrete periods where you compare exact totals. Both share the weakness that only the bottom band has a clean baseline, so reserve them for when the shifting composition, not precise per-band comparison, is the point.

**What is the weakness of a stacked area chart?**
Like the stacked bar, only the bottom band sits on a flat baseline, so the bands above it are hard to read precisely — their movement is part real, part caused by the bands beneath. With many bands it becomes a hard-to-read "stacked spaghetti." Keep bands few, put the most important or most stable one on the bottom, and switch to lines if precise per-series comparison matters.
