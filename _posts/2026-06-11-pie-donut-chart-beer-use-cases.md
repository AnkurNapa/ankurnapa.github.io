---
layout: post
title: "The Pie and Donut Chart in Brewing: Use It Sparingly (Three Cases)"
image: /assets/og/pie-donut-chart-beer-use-cases.png
description: "The pie chart is overused and often the wrong choice — but it has a few honest beer use cases. Where a pie or donut genuinely works, where a bar chart beats it, and the one rule that keeps it readable."
date: 2026-06-11 06:30:00 -0700
updated: 2026-06-11
tags: [brewing-science, beer-chart-guide, data-visualization, commercial-planning, marketing]
faq:
  - q: "When is a pie chart appropriate for beer data?"
    a: "Rarely, and only for a simple part-to-whole split with very few slices (two to four) where the proportions are very different and the total genuinely is 100% of something. A single package-format share, or on- versus off-premise split, can work. For ranking, comparison, or more than a handful of categories, a bar chart is clearer because people read length better than angle."
  - q: "Pie chart or donut chart — does it matter?"
    a: "Barely. A donut is a pie with the centre removed, which frees space for a total or KPI label in the middle — useful on a dashboard tile. Neither fixes the core weakness that angles and areas are hard to compare. Choose a donut when you want the centre label; otherwise the distinction is cosmetic."
  - q: "Why do data people dislike pie charts?"
    a: "Because humans judge angles and areas far less accurately than lengths, so a pie makes comparison harder than a bar chart for almost no benefit. Pies with many slices, similar-sized slices, or 3D effects are genuinely misleading. The dislike is about overuse for jobs a bar chart does better, not the shape being evil."
---

**Short answer: the pie (and its donut cousin) shows one simple part-to-whole split — and it's overused for jobs a bar chart does better, because people read lengths far more accurately than angles. Reserve it for a single whole with two to four clearly-different slices where "share of total" is the literal message: package-format share, on- vs off-premise split. More slices, similar sizes, or any ranking question — use a [bar chart]({{ '/2026/bar-chart-beer-use-cases/' | relative_url }}). The donut just adds a centre label; otherwise the distinction is cosmetic.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A donut chart of package format share with three slices and a total in the centre, beside a note that more than four slices should become a bar chart."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PIE / DONUT — A SIMPLE PART-TO-WHOLE, FEW SLICES</text><g transform="translate(250,135)"><circle r="70" fill="none" stroke="#b45309" stroke-width="34" stroke-dasharray="220 440" transform="rotate(-90)"/><circle r="70" fill="none" stroke="#8a5a2b" stroke-width="34" stroke-dasharray="130 440" stroke-dashoffset="-220" transform="rotate(-90)"/><circle r="70" fill="none" stroke="#cbb89a" stroke-width="34" stroke-dasharray="90 440" stroke-dashoffset="-350" transform="rotate(-90)"/><text y="-2" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">100%</text><text y="16" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#6b6258">volume</text></g><g font-family="sans-serif" font-size="11"><rect x="360" y="100" width="13" height="13" fill="#b45309"/><text x="382" y="111" fill="#6b6258">Can &#183; 50%</text><rect x="360" y="128" width="13" height="13" fill="#8a5a2b"/><text x="382" y="139" fill="#6b6258">Keg &#183; 30%</text><rect x="360" y="156" width="13" height="13" fill="#cbb89a"/><text x="382" y="167" fill="#6b6258">Bottle &#183; 20%</text></g><text x="730" y="120" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">More than ~4 slices?</text><text x="730" y="142" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#6b6258">Use a bar chart instead —</text><text x="730" y="160" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#6b6258">length beats angle for comparison.</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A donut works for a clean three-way split with a centre total; past four slices, switch to bars.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). This is the short, cautionary entry — because the pie is the most overused chart in business.

## When to reach for it (and when not to)

A pie is honest only when **all** of these hold: the parts genuinely sum to one meaningful whole, there are very few slices (two to four), and the slices differ enough that angle comparison is easy. The moment you want to *rank*, compare across two pies, or show more than a handful of categories, a [bar chart]({{ '/2026/bar-chart-beer-use-cases/' | relative_url }}) wins. The donut variant simply frees the centre for a total or KPI — handy on a dashboard tile, otherwise the same chart.

## Use case 1 — Package-format share

Can / keg / bottle as a share of total volume — three clearly different slices, a real whole. A legitimate pie, and a donut lets you put total volume in the hole.

## Use case 2 — On- vs off-premise split

A two-slice donut on an executive tile, with the total in the centre, communicates the channel split at a glance. Two slices is where pies are genuinely fine.

## Use case 3 — A single survey or sentiment split

"Sober-curious vs regular" or a simple yes/no/maybe from a [consumer survey]({{ '/tracks/marketing/' | relative_url }}) — few categories, one whole. Past four answers, switch to bars.

## Where this breaks

**Many or similar slices** — angles you can't compare; use bars. **Comparing two pies** — almost impossible; use grouped or 100% stacked bars instead. **3D / exploded pies** — actively distort area and mislead; never. **Tiny slices** — get lost; group into "other" or change chart.

## The bottom line

The pie and donut earn a place only for a simple part-to-whole with very few, clearly-different slices where "share" is the literal message — package mix, channel split. For everything else, especially ranking and comparison, a bar chart is more honest because we read length better than angle. Use pies sparingly and you'll never mislead with one. Next, composition with many parts and a hierarchy: the [treemap]({{ '/2026/treemap-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**When is a pie chart appropriate for beer data?**
Rarely, and only for a simple part-to-whole split with very few slices (two to four) where the proportions are very different and the total genuinely is 100% of something. A single package-format share, or on- versus off-premise split, can work. For ranking, comparison, or more than a handful of categories, a bar chart is clearer because people read length better than angle.

**Pie chart or donut chart — does it matter?**
Barely. A donut is a pie with the centre removed, which frees space for a total or KPI label in the middle — useful on a dashboard tile. Neither fixes the core weakness that angles and areas are hard to compare. Choose a donut when you want the centre label; otherwise the distinction is cosmetic.

**Why do data people dislike pie charts?**
Because humans judge angles and areas far less accurately than lengths, so a pie makes comparison harder than a bar chart for almost no benefit. Pies with many slices, similar-sized slices, or 3D effects are genuinely misleading. The dislike is about overuse for jobs a bar chart does better, not the shape being evil.
