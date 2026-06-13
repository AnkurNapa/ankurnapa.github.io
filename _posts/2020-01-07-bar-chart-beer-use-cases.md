---
layout: post
title: "The Bar Chart in Brewing: Three Beer Use Cases"
image: /assets/og/bar-chart-beer-use-cases.png
description: "The bar chart is the workhorse of brewery analytics — and the right default more often than any other chart. Three concrete beer use cases (style volumes, account ranking, brewhouse loss by stage) and the rules that keep it honest."
date: 2020-01-07 09:00:00 -0700
updated: 2020-01-07
tags: [brewing-science, beer-chart-guide, data-visualization, sales-intelligence, quality-control]
faq:
  - q: "When should a brewery use a bar chart?"
    a: "Whenever you're comparing a single value across distinct categories — volume by beer style, sales by account, loss by process stage, defects by cause. The bar chart is the clearest way to rank and compare discrete categories, and it's the correct default far more often than pie charts or fancier visuals. Use horizontal bars when category labels are long or there are many of them."
  - q: "What is the most common mistake with bar charts?"
    a: "Not starting the value axis at zero. Because a bar's length encodes its value, a truncated axis exaggerates differences and misleads — a 2% gap can look like a 50% gap. Other common errors are too many categories (sort and show the top N), and using a bar chart for time series where a line chart reads better."
  - q: "Bar chart or pie chart for beer sales by style?"
    a: "Bar chart, almost always. People compare lengths far more accurately than angles or areas, so a bar chart of volume by style is easier to read and rank than a pie. Reserve pie or donut charts for showing one simple part-to-whole split with very few slices, and even then a bar chart usually wins."
---

**Short answer: the bar chart compares one value across distinct categories, and it's the right default more often than any other chart because people read bar *lengths* far more accurately than angles, areas or slopes. In a brewery it answers "which is biggest" cleanly — volume by style, sales by account, loss by process stage. The two rules that keep it honest: always start the value axis at zero, and sort the bars by value (not alphabetically) so the ranking is the message.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A sorted bar chart of beer volume by style, bars descending from largest to smallest, value axis starting at zero."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">BAR CHART — RANK ACROSS CATEGORIES</text><line x1="80" y1="200" x2="940" y2="200" stroke="#6b6258"/><g font-family="sans-serif" font-size="10" fill="#6b6258"><rect x="110" y="70" width="90" height="130" fill="#b45309"/><text x="155" y="216" text-anchor="middle">Lager</text><rect x="240" y="100" width="90" height="100" fill="#b45309"/><text x="285" y="216" text-anchor="middle">IPA</text><rect x="370" y="128" width="90" height="72" fill="#b45309"/><text x="415" y="216" text-anchor="middle">Wheat</text><rect x="500" y="150" width="90" height="50" fill="#8a5a2b"/><text x="545" y="216" text-anchor="middle">Stout</text><rect x="630" y="166" width="90" height="34" fill="#8a5a2b"/><text x="675" y="216" text-anchor="middle">Pale</text><rect x="760" y="178" width="90" height="22" fill="#8a5a2b"/><text x="805" y="216" text-anchor="middle">NA</text></g><text x="500" y="228" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#6b6258">sorted by value, axis from zero — the ranking is the message</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">When the question is "which is biggest," the sorted bar chart answers it faster than anything else.</figcaption>
</figure>

This is part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}) — one chart per article. The bar chart is first because it's the one you'll reach for most, and the one most worth getting right.

## When to reach for it

Use a bar chart whenever you're comparing a single measure across **discrete categories** and the question is "which is biggest / smallest / how do they rank." Lengths are the most accurately-read visual encoding humans have, which is why the humble bar beats flashier charts for plain comparison. Go horizontal when labels are long or there are many categories.

## Use case 1 — Volume (or sales) by beer style

The classic: total hectolitres or revenue by style this quarter. Sorted descending, it instantly shows your volume drivers and your long tail. This is the bread-and-butter of any [depletions or sell-through view]({{ '/2023/tableau-depletions-sell-through-dashboard/' | relative_url }}) — and a bar chart reads it better than the pie a tool might suggest.

## Use case 2 — Top (and bottom) accounts

Rank your accounts or distributors by volume and the bar chart surfaces both your dependence on the top few and the underperformers worth a call. Showing the **top 15** sorted, with an "all others" bar, keeps it legible — a bar chart of 200 accounts is noise.

## Use case 3 — Loss or defects by stage / cause

A bar chart of extract loss by process stage, or QC rejects by defect cause, turns a problem into a priority list: the tallest bar is where to act first. It's the Pareto instinct in its simplest form, and a natural companion to the [brewhouse loss view]({{ '/2026/sankey-brewhouse-mass-energy-balance/' | relative_url }}).

## Where this breaks

**Truncated axes lie** — because length *is* the value, starting the axis above zero exaggerates differences; always start at zero. **Too many bars** — sort and cap at the top N with an "others" bar. **Wrong tool for time** — for a value over time, a [line chart]({{ '/2020/line-chart-beer-use-cases/' | relative_url }}) usually reads better; use bars for time only when periods are few and discrete.

## The bottom line

The bar chart compares a value across categories better than anything else, because we read lengths accurately. Reach for it whenever the question is "which is biggest," sort by value, start at zero, and cap the categories. It's the least glamorous and most useful chart in the brewery. Next in the guide: when you have *two* series to compare, the [grouped bar chart]({{ '/2020/grouped-bar-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**When should a brewery use a bar chart?**
Whenever you're comparing a single value across distinct categories — volume by beer style, sales by account, loss by process stage, defects by cause. The bar chart is the clearest way to rank and compare discrete categories, and it's the correct default far more often than pie charts or fancier visuals. Use horizontal bars when category labels are long or there are many of them.

**What is the most common mistake with bar charts?**
Not starting the value axis at zero. Because a bar's length encodes its value, a truncated axis exaggerates differences and misleads — a 2% gap can look like a 50% gap. Other common errors are too many categories (sort and show the top N), and using a bar chart for time series where a line chart reads better.

**Bar chart or pie chart for beer sales by style?**
Bar chart, almost always. People compare lengths far more accurately than angles or areas, so a bar chart of volume by style is easier to read and rank than a pie. Reserve pie or donut charts for showing one simple part-to-whole split with very few slices, and even then a bar chart usually wins.
