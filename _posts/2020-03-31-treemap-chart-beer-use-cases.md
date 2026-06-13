---
layout: post
title: "The Treemap in Brewing: Three Beer Use Cases"
image: /assets/og/treemap-chart-beer-use-cases.png
description: "When composition has many parts and a hierarchy, a treemap shows the whole portfolio in one rectangle sized by value. Three beer use cases (SKU portfolio, sales by region then account, ingredient spend) and where it beats a pie or a long bar chart."
date: 2020-03-31 09:00:00 -0700
updated: 2020-03-31
tags: [brewing-science, beer-chart-guide, data-visualization, commercial-planning, financial-planning-analytics]
faq:
  - q: "What is a treemap and when should a brewery use one?"
    a: "A treemap shows composition as nested rectangles whose area is proportional to value, so a whole portfolio fits in one space and the big contributors are literally the biggest tiles. Breweries use it for a SKU portfolio (many products at once), sales broken down by region then account, or ingredient spend by category then item. It handles many categories and a hierarchy where a pie or long bar chart would fail."
  - q: "Treemap or bar chart?"
    a: "Use a bar chart when you have a manageable number of categories and precise ranking matters — people read bar length more accurately than rectangle area. Use a treemap when there are too many categories for bars, when a hierarchy matters (group within group), or when you want to show the whole portfolio's shape at once and approximate proportions are enough."
  - q: "What is the weakness of a treemap?"
    a: "Area is read less precisely than length, so fine differences between similar-sized tiles are hard to judge, and very small tiles become unreadable slivers. Treemaps are great for the big picture and the big contributors, weaker for exact comparison of mid-sized items. Label the major tiles with values to compensate."
---

**Short answer: a treemap shows composition with many parts — and a hierarchy — as nested rectangles sized by value, so a whole portfolio fits in one picture and the big contributors are the biggest tiles. In a brewery it's the chart for "show me the entire SKU range / all regions and accounts / total ingredient spend at once," where a pie would choke and a bar chart would scroll forever. Its cost: area is read less precisely than length, so it's a big-picture tool, not a precise-ranking one.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A treemap of a beer SKU portfolio: large tiles for the biggest sellers and many small tiles for the long tail, area proportional to volume."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">TREEMAP — THE WHOLE PORTFOLIO, SIZED BY VALUE</text><g font-family="sans-serif" font-size="11" fill="#fdfbf7">
<rect x="80" y="46" width="300" height="170" fill="#b45309" stroke="#fdfbf7" stroke-width="2"/><text x="230" y="128" text-anchor="middle" font-weight="700">Core Lager</text><text x="230" y="146" text-anchor="middle" font-size="9">38%</text>
<rect x="380" y="46" width="210" height="100" fill="#a35008" stroke="#fdfbf7" stroke-width="2"/><text x="485" y="100" text-anchor="middle" font-weight="700">IPA</text>
<rect x="380" y="146" width="210" height="70" fill="#8a5a2b" stroke="#fdfbf7" stroke-width="2"/><text x="485" y="186" text-anchor="middle">Wheat</text>
<rect x="590" y="46" width="150" height="90" fill="#8a5a2b" stroke="#fdfbf7" stroke-width="2"/><text x="665" y="96" text-anchor="middle">Stout</text>
<rect x="590" y="136" width="150" height="80" fill="#a06a30" stroke="#fdfbf7" stroke-width="2"/><text x="665" y="180" text-anchor="middle">Pale</text>
<rect x="740" y="46" width="100" height="60" fill="#cbb89a" stroke="#fdfbf7" stroke-width="2"/><text x="790" y="80" text-anchor="middle" fill="#1c1a17" font-size="9">NA</text>
<rect x="840" y="46" width="80" height="60" fill="#cbb89a" stroke="#fdfbf7" stroke-width="2"/><text x="880" y="80" text-anchor="middle" fill="#1c1a17" font-size="9">Sour</text>
<rect x="740" y="106" width="90" height="50" fill="#ddcdb4" stroke="#fdfbf7" stroke-width="2"/><rect x="830" y="106" width="90" height="50" fill="#ddcdb4" stroke="#fdfbf7" stroke-width="2"/><rect x="740" y="156" width="60" height="60" fill="#e6dac6" stroke="#fdfbf7" stroke-width="2"/><rect x="800" y="156" width="60" height="60" fill="#e6dac6" stroke="#fdfbf7" stroke-width="2"/><rect x="860" y="156" width="60" height="60" fill="#e6dac6" stroke="#fdfbf7" stroke-width="2"/></g><text x="500" y="234" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">the long tail of small SKUs is visible as small tiles — a pie or 30-bar chart couldn't show this</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Tile area = value. The big sellers dominate, the long tail is still visible, all in one frame.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). When a [pie]({{ '/2020/pie-donut-chart-beer-use-cases/' | relative_url }}) has too many slices and a [bar chart]({{ '/2020/bar-chart-beer-use-cases/' | relative_url }}) too many bars, the treemap is the answer.

## When to reach for it

Reach for a treemap when composition has **many parts**, optionally **nested in a hierarchy**, and you want the *shape of the whole* with approximate proportions. It trades precise ranking (bars do that) for the ability to show everything at once and reveal a hierarchy by nesting.

## Use case 1 — The SKU portfolio at a glance

Every product sized by volume or revenue in one frame: the core brands dominate, the long tail of seasonals and one-offs is still visible. It makes portfolio concentration — and tail bloat — obvious, the starting point of any rationalisation conversation.

## Use case 2 — Sales by region, then account

Nest accounts inside regions: big region rectangles subdivided into account tiles. You see regional weight and, within it, account concentration — two levels of [sales intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) in one picture.

## Use case 3 — Ingredient or cost spend

Total procurement spend nested by category (malt, hops, packaging) then item. The fattest tiles are where your money goes and where negotiation moves the most — a visual companion to the [cost build-up]({{ '/2020/stacked-bar-chart-beer-use-cases/' | relative_url }}).

## Where this breaks

**Area beats length for "lots at once" but loses on precision** — similar tiles are hard to rank; label major tiles with values. **Tiny tiles vanish** — the smallest SKUs become unreadable slivers; group a "other / tail" tile. **No good for trends** — a treemap is a snapshot; for change over time use a [line]({{ '/2020/line-chart-beer-use-cases/' | relative_url }}) or [stacked area]({{ '/2020/area-chart-beer-use-cases/' | relative_url }}).

## The bottom line

The treemap shows a whole portfolio — many parts, optional hierarchy — as area-sized tiles, perfect for "show me everything at once" when a pie chokes and a bar chart scrolls. Use it for the SKU range, nested sales, and spend; label the big tiles, group the tail, and don't ask it for precise ranking or trends. Next, the chart for change over time: the [line chart]({{ '/2020/line-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**What is a treemap and when should a brewery use one?**
A treemap shows composition as nested rectangles whose area is proportional to value, so a whole portfolio fits in one space and the big contributors are literally the biggest tiles. Breweries use it for a SKU portfolio (many products at once), sales broken down by region then account, or ingredient spend by category then item. It handles many categories and a hierarchy where a pie or long bar chart would fail.

**Treemap or bar chart?**
Use a bar chart when you have a manageable number of categories and precise ranking matters — people read bar length more accurately than rectangle area. Use a treemap when there are too many categories for bars, when a hierarchy matters (group within group), or when you want to show the whole portfolio's shape at once and approximate proportions are enough.

**What is the weakness of a treemap?**
Area is read less precisely than length, so fine differences between similar-sized tiles are hard to judge, and very small tiles become unreadable slivers. Treemaps are great for the big picture and the big contributors, weaker for exact comparison of mid-sized items. Label the major tiles with values to compensate.
