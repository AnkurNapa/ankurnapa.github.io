---
layout: post
title: "The Heat Map in Brewing: Three Beer Use Cases"
image: /assets/og/heat-map-beer-use-cases.png
description: "When two categories meet — hour by day, style by month, account by SKU — a heat map shows intensity as colour, so patterns jump out of a grid. Three beer use cases and the colour-scale rules that keep it honest."
date: 2020-09-15 09:00:00 -0700
updated: 2020-09-15
tags: [brewing-science, beer-chart-guide, data-visualization, sales-intelligence, commercial-planning]
faq:
  - q: "When should a brewery use a heat map?"
    a: "When you want to see a value across two categorical dimensions at once and spot patterns — taproom sales by hour and day of week, style demand by month (seasonality), or account-by-SKU purchasing. Each cell's colour shows the value, so hot spots and cold spots emerge from the grid in a way rows of numbers never would."
  - q: "What makes a heat map misleading?"
    a: "The colour scale. A poorly chosen scale can hide real differences or invent dramatic ones, and rainbow scales distort because colour isn't perceived evenly. Use a single-hue sequential scale for magnitude (light to dark), a diverging scale only when there's a meaningful midpoint (above/below target), keep the scale consistent, and always show a legend."
  - q: "What is the difference between a heat map and a table?"
    a: "A heat map is a table where the cell values are encoded as colour, so patterns across the whole grid are visible at a glance rather than read cell by cell. Use a heat map when the pattern across two dimensions is the message; keep a plain table when readers need exact values. Many tools let you do both — colour the table cells and keep the numbers."
---

**Short answer: a heat map shows a value across two categorical dimensions as a grid of coloured cells, so patterns leap out — the busy Friday-evening cell in taproom sales, the summer band in style seasonality, the account-SKU gaps in distribution. It's the chart for "where are the hot and cold spots across these two dimensions." Its honesty lives entirely in the colour scale: choose a sequential scale for magnitude, keep it consistent, show a legend, and never let a rainbow distort the story.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 250" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A heat map of taproom sales by day of week and hour, with dark hot cells on Friday and Saturday evenings and light cells on weekday afternoons."><rect width="1000" height="250" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">HEAT MAP — INTENSITY ACROSS TWO DIMENSIONS</text><g font-family="sans-serif" font-size="9" fill="#6b6258"><text x="150" y="58" text-anchor="end">Mon</text><text x="150" y="88" text-anchor="end">Wed</text><text x="150" y="118" text-anchor="end">Fri</text><text x="150" y="148" text-anchor="end">Sat</text></g>
<g><!-- rows: Mon, Wed, Fri, Sat ; cols: noon..late -->
<rect x="160" y="46" width="80" height="26" fill="#f1e3d2"/><rect x="240" y="46" width="80" height="26" fill="#ecd9c2"/><rect x="320" y="46" width="80" height="26" fill="#e6cdb0"/><rect x="400" y="46" width="80" height="26" fill="#dcbd97"/><rect x="480" y="46" width="80" height="26" fill="#d3ad7e"/><rect x="560" y="46" width="80" height="26" fill="#e0c4a4"/>
<rect x="160" y="76" width="80" height="26" fill="#eedfca"/><rect x="240" y="76" width="80" height="26" fill="#e6cdb0"/><rect x="320" y="76" width="80" height="26" fill="#dcbd97"/><rect x="400" y="76" width="80" height="26" fill="#cda06b"/><rect x="480" y="76" width="80" height="26" fill="#b9854a"/><rect x="560" y="76" width="80" height="26" fill="#cda06b"/>
<rect x="160" y="106" width="80" height="26" fill="#e6cdb0"/><rect x="240" y="106" width="80" height="26" fill="#d3ad7e"/><rect x="320" y="106" width="80" height="26" fill="#b9854a"/><rect x="400" y="106" width="80" height="26" fill="#9c6a30"/><rect x="480" y="106" width="80" height="26" fill="#7a4f1f"/><rect x="560" y="106" width="80" height="26" fill="#9c6a30"/>
<rect x="160" y="136" width="80" height="26" fill="#dcbd97"/><rect x="240" y="136" width="80" height="26" fill="#c9a064"/><rect x="320" y="136" width="80" height="26" fill="#a8763a"/><rect x="400" y="136" width="80" height="26" fill="#7a4f1f"/><rect x="480" y="136" width="80" height="26" fill="#5e3c14"/><rect x="560" y="136" width="80" height="26" fill="#7a4f1f"/></g>
<g font-family="sans-serif" font-size="9" fill="#6b6258"><text x="200" y="178" text-anchor="middle">12</text><text x="360" y="178" text-anchor="middle">4pm</text><text x="520" y="178" text-anchor="middle">8pm</text><text x="600" y="178" text-anchor="middle">late</text></g>
<g font-family="sans-serif" font-size="9.5"><text x="700" y="60" fill="#6b6258">low</text><rect x="730" y="50" width="150" height="14" fill="url(#hm)"/><text x="884" y="60" fill="#6b6258">high</text><linearGradient id="hm" x1="0" x2="1"><stop offset="0" stop-color="#f1e3d2"/><stop offset="1" stop-color="#5e3c14"/></linearGradient></g>
<text x="780" y="110" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="#1c1a17">Fri &amp; Sat evenings</text><text x="780" y="128" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#6b6258">are the hot cells — staff for them</text><text x="500" y="222" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">the pattern across two dimensions emerges from colour — no row of numbers shows it this fast</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Day × hour as colour: the weekend-evening hot spot is obvious, the quiet weekday afternoons just as clear.</figcaption>
</figure>

This closes [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). The heat map is the chart for *two* categorical dimensions at once — where a [bar]({{ '/2020/bar-chart-beer-use-cases/' | relative_url }}) handles one.

## When to reach for it

Reach for a heat map when a value lives at the intersection of **two categories** and the *pattern across the grid* is the message. Colour encodes magnitude per cell, so clusters, bands and gaps emerge that a table of numbers would bury.

## Use case 1 — Taproom sales by hour × day

The canonical heat map: day of week across, hour down, sales as colour. The Friday-and-Saturday-evening hot block tells you exactly when to staff and run events — the actionable core of a [taproom view]({{ '/2023/tableau-taproom-sales-footfall-dashboard/' | relative_url }}) that a daily total hides.

## Use case 2 — Style demand by month (seasonality)

Styles down, months across, volume as colour. Seasonal bands appear instantly — the summer wheat-and-lager heat, the winter stout warmth — guiding brew scheduling and [forecasting]({{ '/tracks/sales-forecasting/' | relative_url }}) far faster than twelve separate lines.

## Use case 3 — Account × SKU distribution gaps

Accounts down, SKUs across, with colour for volume (or a flag for "stocked / not"). The cold cells are your distribution white space — accounts not buying SKUs they should — a concrete [sales intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) target list.

## Where this breaks

**The colour scale is everything** — use a sequential single-hue scale for magnitude; reserve diverging scales for a real midpoint (above/below target); avoid rainbow, which distorts. **No legend, no meaning** — always show the scale. **Too fine a grid** — hundreds of tiny cells overwhelm; aggregate sensibly. **Exact values lost** — colour is approximate; if readers need numbers, colour the table cells and keep the figures. **Accessibility** — choose colourblind-safe palettes.

## The bottom line

The heat map reveals patterns across two categorical dimensions — hour × day, style × month, account × SKU — by encoding value as colour, surfacing hot spots and gaps a table buries. Choose the colour scale honestly, always show a legend, and aggregate to a readable grid. That completes the field guide; for the charts not covered here — radar, CUSUM, trajectories and Sankey — see the [Seeing Your Beer]({{ '/series/brewing-data-viz/' | relative_url }}) series, and the [full index]({{ '/series/beer-chart-guide/' | relative_url }}) ties them all together.

## Frequently asked questions

**When should a brewery use a heat map?**
When you want to see a value across two categorical dimensions at once and spot patterns — taproom sales by hour and day of week, style demand by month (seasonality), or account-by-SKU purchasing. Each cell's colour shows the value, so hot spots and cold spots emerge from the grid in a way rows of numbers never would.

**What makes a heat map misleading?**
The colour scale. A poorly chosen scale can hide real differences or invent dramatic ones, and rainbow scales distort because colour isn't perceived evenly. Use a single-hue sequential scale for magnitude (light to dark), a diverging scale only when there's a meaningful midpoint (above/below target), keep the scale consistent, and always show a legend.

**What is the difference between a heat map and a table?**
A heat map is a table where the cell values are encoded as colour, so patterns across the whole grid are visible at a glance rather than read cell by cell. Use a heat map when the pattern across two dimensions is the message; keep a plain table when readers need exact values. Many tools let you do both — colour the table cells and keep the numbers.
