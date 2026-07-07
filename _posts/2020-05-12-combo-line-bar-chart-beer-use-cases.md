---
layout: post
title: "The Combo (Line + Bar) Chart in Brewing: Three Beer Use Cases"
image: /assets/og/combo-line-bar-chart-beer-use-cases.png
description: "Two metrics on two axes — volume as bars, margin as a line — the combo chart shows a quantity and a rate together. Three beer use cases and the dual-axis trap that makes this chart easy to misuse."
date: 2020-05-12 09:00:00 -0700
updated: 2020-05-12
tags: [brewing-science, beer-chart-guide, data-visualization, financial-planning-analytics, commercial-planning]
faq:
  - q: "What is a combo chart and when should a brewery use one?"
    a: "A combo (combination) chart puts two chart types — usually bars and a line — on one plot, often with two y-axes, to show two related but differently-scaled metrics together. Breweries use it for volume (bars) with margin percent (line), production (bars) with yield percent (line), or sales (bars) with forecast accuracy (line). It works when the two metrics tell a combined story over the same categories or time."
  - q: "What is the dual-axis trap in combo charts?"
    a: "With two independent y-axes, you can slide the scales to make the two series appear to track or diverge however you like — implying a correlation that isn't real. Use a second axis only when the two metrics are genuinely different units (volume and percent), set the scales honestly, label both axes clearly, and never use a dual axis just to overlay two unrelated lines."
  - q: "When should you avoid a combo chart?"
    a: "When both metrics share the same unit and scale — then plot them on one axis, no second axis needed. Also avoid it when the two series have no real relationship; overlaying them just implies a connection that misleads. If the chart needs a paragraph to explain which line uses which axis, it's too clever."
---

**Short answer: the combo chart overlays two chart types — typically bars for a quantity and a line for a rate — often on two y-axes, to tell a combined story: volume *and* margin %, production *and* yield %, sales *and* forecast accuracy. It's powerful when the two metrics genuinely belong together, and dangerous because two independent axes can be slid to imply a correlation that isn't there. Use a second axis only for genuinely different units, scale it honestly, and label both axes.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A combo chart with monthly volume as bars on the left axis and margin percent as a line on the right axis."><rect width="1000" height="240" fill="#ffffff"/><text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">COMBO — A QUANTITY (BARS) AND A RATE (LINE)</text><line x1="90" y1="200" x2="910" y2="200" stroke="#4a6b64"/><g font-family="sans-serif"><rect x="130" y="120" width="60" height="80" fill="#00695c"/><rect x="280" y="100" width="60" height="100" fill="#00695c"/><rect x="430" y="92" width="60" height="108" fill="#00695c"/><rect x="580" y="110" width="60" height="90" fill="#00695c"/><rect x="730" y="84" width="60" height="116" fill="#00695c"/></g><polyline points="160,150 310,142 460,120 610,150 760,108" fill="none" stroke="#06483f" stroke-width="2.6"/><g fill="#06483f"><circle cx="160" cy="150" r="4"/><circle cx="310" cy="142" r="4"/><circle cx="460" cy="120" r="4"/><circle cx="610" cy="150" r="4"/><circle cx="760" cy="108" r="4"/></g><text x="74" y="120" text-anchor="end" font-family="sans-serif" font-size="9.5" fill="#00695c">hl</text><text x="926" y="120" font-family="sans-serif" font-size="9.5" fill="#06483f">margin %</text><text x="500" y="226" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#4a6b64">volume on the left axis, margin % on the right — two units, one story</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Bars for the quantity, a line for the rate — useful when the two genuinely belong together.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). It marries the [bar]({{ '/2020/bar-chart-beer-use-cases/' | relative_url }}) and the [line]({{ '/2020/line-chart-beer-use-cases/' | relative_url }}) — handy, and easy to abuse.

## When to reach for it

Reach for a combo when **two related metrics of different units** share the same categories or time axis and the story is in *both together* — a quantity (bars) and a rate or percent (line). The bars carry magnitude; the line carries the rate riding on top.

## Use case 1 — Volume and margin %

Monthly volume as bars, gross margin % as a line. You see a high-volume month that's actually low-margin, or a small premium line carrying the profit — the [FP&A]({{ '/tracks/financial-planning-analytics/' | relative_url }}) view that volume-only charts hide.

## Use case 2 — Production and yield %

Batches or hectolitres produced as bars, extract or brewhouse yield % as a line. A production push that quietly dropped yield shows up immediately — output and efficiency in one frame.

## Use case 3 — Sales and forecast accuracy

Actual sales as bars with forecast-accuracy % as a line exposes whether big months are also the hard-to-predict ones — a useful [forecasting]({{ '/tracks/sales-forecasting/' | relative_url }}) diagnostic.

## Where this breaks

**The dual-axis trap** — two free axes can be scaled to fake a correlation; scale honestly and only for genuinely different units. **Same-unit overlay** — if both metrics share a unit and scale, drop the second axis and use one. **Unrelated series** — don't overlay two things just because you can; it implies a link. **Reading load** — clearly label which series uses which axis, or the chart confuses more than it shows.

## The bottom line

The combo chart shows a quantity and a rate together — volume + margin %, production + yield %, sales + accuracy — when the two genuinely belong on one canvas. Use a second axis only for different units, scale both honestly, and label clearly. Misused, two axes mislead; used well, the chart reveals what either metric alone would hide. Next, cumulative totals over time: the [area chart]({{ '/2020/area-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**What is a combo chart and when should a brewery use one?**
A combo (combination) chart puts two chart types — usually bars and a line — on one plot, often with two y-axes, to show two related but differently-scaled metrics together. Breweries use it for volume (bars) with margin percent (line), production (bars) with yield percent (line), or sales (bars) with forecast accuracy (line). It works when the two metrics tell a combined story over the same categories or time.

**What is the dual-axis trap in combo charts?**
With two independent y-axes, you can slide the scales to make the two series appear to track or diverge however you like — implying a correlation that isn't real. Use a second axis only when the two metrics are genuinely different units (volume and percent), set the scales honestly, label both axes clearly, and never use a dual axis just to overlay two unrelated lines.

**When should you avoid a combo chart?**
When both metrics share the same unit and scale — then plot them on one axis, no second axis needed. Also avoid it when the two series have no real relationship; overlaying them just implies a connection that misleads. If the chart needs a paragraph to explain which line uses which axis, it's too clever.
