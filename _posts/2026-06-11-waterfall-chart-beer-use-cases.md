---
layout: post
title: "The Waterfall Chart in Brewing: Three Beer Use Cases"
image: /assets/og/waterfall-chart-beer-use-cases.png
description: "A waterfall chart shows how you got from one number to another — the steps that build or erode a total. Three beer use cases (margin bridge, volume bridge, budget variance) and the rule that keeps the bridge honest."
date: 2026-06-11 08:10:00 -0700
updated: 2026-06-11
tags: [brewing-science, beer-chart-guide, data-visualization, financial-planning-analytics, commercial-planning]
faq:
  - q: "What is a waterfall chart and when should a brewery use one?"
    a: "A waterfall (or bridge) chart shows how a starting value becomes an ending value through a sequence of positive and negative steps, each a floating bar. Breweries use it for a margin bridge (last year's margin to this year's, broken into price, mix, cost and volume effects), a volume bridge, or budget-vs-actual variance. It answers 'what drove the change', not just 'what changed.'"
  - q: "What is the difference between a waterfall chart and a bar chart?"
    a: "A bar chart compares independent categories; a waterfall shows a connected sequence where each step starts where the last ended, building from a start total to an end total. Use a bar chart to rank things, a waterfall to decompose a change — to explain why this quarter's margin is up or down versus last."
  - q: "How do you keep a waterfall chart honest?"
    a: "The steps must actually reconcile — start plus all the positive and negative contributions must equal the end total, with nothing hidden in an 'other' bucket. Order the steps logically, colour increases and decreases consistently, and label each step's value. A bridge that doesn't tie out is worse than no chart, because it looks precise while being wrong."
---

**Short answer: the waterfall (bridge) chart shows how a starting number becomes an ending number through a sequence of positive and negative steps — each a floating bar. It answers "what drove the change," not just "what changed." In a brewery it's the margin bridge (last year to this year, split into price, mix, cost and volume), the volume bridge, and budget variance. The one rule: the steps must reconcile — start plus every contribution equals the end, nothing hidden — or the bridge lies while looking precise.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A margin bridge waterfall: starting margin, a positive price step up, a negative cost step down, a positive mix step, a small negative volume step, ending at this year's margin."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">WATERFALL — HOW A TOTAL CHANGED, STEP BY STEP</text><line x1="70" y1="200" x2="930" y2="200" stroke="#6b6258"/><g font-family="sans-serif" font-size="9" fill="#6b6258"><rect x="90" y="120" width="90" height="80" fill="#8a5a2b"/><text x="135" y="216" text-anchor="middle">LY margin</text><rect x="220" y="92" width="90" height="28" fill="#2f6b3a"/><text x="265" y="216" text-anchor="middle">+ price</text><rect x="350" y="92" width="90" height="44" fill="#7a1f3d"/><text x="395" y="216" text-anchor="middle">&#8722; cost</text><rect x="480" y="76" width="90" height="22" fill="#2f6b3a"/><text x="525" y="216" text-anchor="middle">+ mix</text><rect x="610" y="76" width="90" height="18" fill="#7a1f3d"/><text x="655" y="216" text-anchor="middle">&#8722; volume</text><rect x="740" y="94" width="90" height="106" fill="#b45309"/><text x="785" y="216" text-anchor="middle">TY margin</text></g><g stroke="#cbb89a" stroke-dasharray="3 3"><line x1="180" y1="120" x2="220" y2="120"/><line x1="310" y1="92" x2="350" y2="92"/><line x1="440" y1="136" x2="480" y2="98"/><line x1="570" y1="76" x2="610" y2="76"/><line x1="700" y1="94" x2="740" y2="94"/></g><text x="500" y="232" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">green steps add, maroon steps subtract — start and end tie out exactly</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The bridge turns "margin is up a bit" into "price and mix added, cost and volume took some back."</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). Where a [bar chart]({{ '/2026/bar-chart-beer-use-cases/' | relative_url }}) compares, the waterfall *explains a change*.

## When to reach for it

Reach for a waterfall when you need to explain **how one total became another** — the contributing steps, positive and negative, in sequence. It's the chart that turns "margin moved" into "here's exactly what moved it," which is why finance lives in it.

## Use case 1 — The margin bridge

Last year's margin to this year's, decomposed into price, mix, cost and volume effects. Each step shows a lever's contribution, so the conversation moves from "margin's down" to "cost ate the price gain" — the [margin-bridge]({{ '/2025/margin-bridge-analytics-beverage/' | relative_url }}) view every [FP&A]({{ '/tracks/financial-planning-analytics/' | relative_url }}) team needs.

## Use case 2 — The volume bridge

Plan volume to actual, stepped by new accounts, lost accounts, rate-of-sale change and new SKUs. It turns a volume miss into an attributed story the commercial team can act on.

## Use case 3 — Budget vs actual variance

Start at budget, step through each cost line's over/under, land on actual. The waterfall makes the few big variances obvious and the noise small — far clearer than a variance table.

## Where this breaks

**It must reconcile** — start plus steps must equal the end exactly; a bridge that doesn't tie out looks precise and is wrong. **Hidden buckets lie** — a fat "other" step defeats the purpose; decompose it. **Order matters for some effects** — price/mix/volume splits depend on calculation order; state your method. **Too many steps** — a 15-step bridge is a wall; group small ones.

## The bottom line

The waterfall explains how a total changed — margin, volume, budget — by stepping through the drivers, increases and decreases, from start to end. Make it reconcile exactly, avoid hidden buckets, and keep the steps few. It's the finance team's favourite for a reason: it answers *why*, not just *what*. Next: stage-to-stage drop-off, the [funnel chart]({{ '/2026/funnel-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**What is a waterfall chart and when should a brewery use one?**
A waterfall (or bridge) chart shows how a starting value becomes an ending value through a sequence of positive and negative steps, each a floating bar. Breweries use it for a margin bridge (last year's margin to this year's, broken into price, mix, cost and volume effects), a volume bridge, or budget-vs-actual variance. It answers "what drove the change", not just "what changed."

**What is the difference between a waterfall chart and a bar chart?**
A bar chart compares independent categories; a waterfall shows a connected sequence where each step starts where the last ended, building from a start total to an end total. Use a bar chart to rank things, a waterfall to decompose a change — to explain why this quarter's margin is up or down versus last.

**How do you keep a waterfall chart honest?**
The steps must actually reconcile — start plus all the positive and negative contributions must equal the end total, with nothing hidden in an "other" bucket. Order the steps logically, colour increases and decreases consistently, and label each step's value. A bridge that doesn't tie out is worse than no chart, because it looks precise while being wrong.
