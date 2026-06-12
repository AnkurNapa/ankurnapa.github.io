---
layout: post
title: "Where Your Extract, Water and Energy Go: Sankey and the Brewhouse Balance"
image: /assets/og/sankey-brewhouse-mass-energy-balance.png
description: "A brewery's biggest losses hide in plain sight across a dozen separate reports. A Sankey diagram puts the whole mass and energy balance in one picture — extract from grain to glass, water in to effluent out, energy in to heat lost — so the leaks become impossible to miss."
date: 2026-06-12 12:10:00 -0700
updated: 2026-06-12
tags: [brewing-science, brewing-data-viz, data-visualization, sustainability, process-intelligence]
faq:
  - q: "What is a Sankey diagram and how does a brewery use one?"
    a: "A Sankey diagram shows flows as bands whose width is proportional to quantity, so you see at a glance where a resource goes and where it's lost. A brewery can map extract from grain through mash, kettle, fermenter and packaging to finished beer; water from intake through brewing, cleaning and cooling to effluent; or energy from fuel and electricity to useful heat versus losses. The widest 'loss' band is where to look first."
  - q: "How do you visualize brewhouse efficiency and losses?"
    a: "A mass or energy balance rendered as a Sankey is the clearest single view: total input on the left, useful output and each loss as bands flowing right, sized by quantity. It turns a dozen separate yield, water and energy reports into one picture where the biggest leak is literally the widest band, making it far easier to prioritise than rows of percentages."
  - q: "What data do you need for a brewery Sankey diagram?"
    a: "Measured quantities at each stage of the flow you're mapping — for extract, the kg of extract entering and leaving mash, kettle, fermenter and packaging; for water, metered use by area; for energy, metered fuel and electricity by use. A Sankey is only as honest as the measurements behind it; gaps get hidden in a vague 'losses' band, so meter the major stages before trusting the picture."
---

**Short answer: a brewery's biggest losses — extract you paid for and threw away, water down the drain, energy up the stack — hide in plain sight, scattered across a dozen separate yield, utility and effluent reports where no single one shows the whole picture. A Sankey diagram fixes that: it draws every flow as a band sized by quantity, so the entire mass or energy balance sits in one image and the widest loss band is, literally, where to look first. It's the clearest way to make brewhouse losses impossible to ignore — provided the flows are measured, not guessed.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A Sankey diagram of brewery extract flow: total extract entering on the left splits into useful extract in finished beer and loss bands at mash (spent grain), kettle and whirlpool (trub), and fermenter and packaging, with band width proportional to loss."><rect width="1000" height="320" fill="#fdfbf7"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">EXTRACT FROM GRAIN TO GLASS — ONE PICTURE</text><g font-family="sans-serif"><rect x="60" y="80" width="34" height="180" fill="#8a5a2b"/><text x="77" y="274" text-anchor="middle" font-size="9.5" fill="#6b6258">extract in</text><text x="77" y="290" text-anchor="middle" font-size="9" fill="#6b6258">(100%)</text><path d="M94 80 C 260 80, 320 90, 470 96 L 470 150 C 320 150, 260 150, 94 152 Z" fill="#b45309" fill-opacity="0.5"/><path d="M94 152 C 220 152, 280 200, 430 206 L 430 240 C 280 240, 220 188, 94 186 Z" fill="#7a1f3d" fill-opacity="0.45"/><path d="M94 186 C 200 186, 240 250, 360 258 L 360 280 C 240 280, 200 222, 94 224 Z" fill="#7a1f3d" fill-opacity="0.3"/><path d="M94 224 C 180 224, 210 268, 300 276 L 300 290 C 210 290, 180 256, 94 256 Z" fill="#7a1f3d" fill-opacity="0.2"/><rect x="470" y="96" width="26" height="54" fill="#2f6b3a"/><text x="560" y="118" font-size="10.5" font-weight="700" fill="#2f6b3a">useful extract &#8594; finished beer</text><rect x="430" y="206" width="22" height="34" fill="#7a1f3d"/><text x="520" y="226" font-size="10" fill="#7a1f3d">spent grain (mash loss)</text><rect x="360" y="258" width="20" height="22" fill="#7a1f3d"/><text x="448" y="272" font-size="9.5" fill="#6b6258">trub / hot break (kettle)</text><rect x="300" y="276" width="18" height="14" fill="#7a1f3d"/><text x="384" y="287" font-size="9.5" fill="#6b6258">yeast / tank / packaging</text></g><text x="780" y="170" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1c1a17">The widest loss band</text><text x="780" y="190" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1c1a17">is where to look first.</text><text x="780" y="216" text-anchor="middle" font-size="10" fill="#6b6258">a dozen yield reports become</text><text x="780" y="232" text-anchor="middle" font-size="10" fill="#6b6258">one prioritised picture</text><text x="500" y="312" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#6b6258">same diagram works for water (intake &#8594; beer / cleaning / cooling / effluent) and energy (fuel &#8594; useful heat / losses)</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Band width = quantity, so loss prioritisation is visual: the fattest band is the first place to act.</figcaption>
</figure>

This closes the [brewing data-visualization series]({{ '/2026/brewing-viz-beyond-control-chart/' | relative_url }}). The previous posts visualized *quality* — conformance, drift, ageing. This one visualizes *resource*: where the things you pay for actually go, building on your existing [brewhouse yield and loss analytics]({{ '/2023/brewhouse-yield-loss-analytics/' | relative_url }}).

## Losses hide in the gaps between reports

A brewery measures a lot: mash efficiency here, kettle losses there, a water bill, a gas bill, an effluent volume, a packaging yield. Each report is fine on its own — and that's the problem. The single biggest losses live in the *gaps between* reports, where no one view shows the whole flow. You know mash efficiency and you know packaging yield, but the cumulative story — of every kilogram of extract you paid for, how much reaches a glass and how much you threw away at each stage — exists nowhere as one picture. So the loss everyone could act on stays invisible, split across a dozen spreadsheets that each show a slice.

## The Sankey shows the whole flow at once

A Sankey diagram draws flows as bands whose *width is proportional to quantity*. Put total extract on the left; let it branch right into the useful extract that reaches finished beer and a loss band at each stage — spent grain at the mash, trub and hot break at the kettle, yeast and tank and packaging losses downstream. Suddenly the entire balance is one image, and the eye does the prioritisation for free: the **widest loss band is where to look first**. No table of percentages communicates "this one stage is where a third of your loss happens" as immediately as a band three times fatter than its neighbours.

And the same diagram shape serves the brewery's other two big balances:

- **Water** — intake on the left, branching to water *in the beer*, cleaning (CIP), cooling and steam, and effluent out. The effluent band is usually sobering, and it's the one [water-stewardship]({{ '/2026/four-types-data-analytics-winery-fabric/' | relative_url }}) and sustainability reporting cares about most.
- **Energy** — fuel and electricity in, branching to useful heat (wort boiling, hot liquor) versus losses (flue, radiation, hot effluent). The losses you can recover — heat off the kettle, warm wastewater — are exactly the bands a Sankey makes obvious.

## From picture to priority

The reason this matters beyond aesthetics: a Sankey converts diffuse, hard-to-rank data into an ordered to-do list. Loss-reduction, water-saving and energy-recovery projects all compete for the same limited capital, and the Sankey answers "which one first?" by showing which band is fattest and therefore which fix moves the most. It's the resource-side equivalent of the [analytics ladder's diagnostic rung]({{ '/2026/four-types-data-analytics-distillery-fabric/' | relative_url }}) — not just *what* the losses are, but *where*, ranked, in a glance the whole team shares.

## Where this breaks

The honest section. **A Sankey is only as honest as its measurements** — unmetered stages get swept into a vague "other losses" band that can hide the very thing you're hunting, or worse, imply precision you don't have; meter the major stages before trusting the picture, and label estimated bands as estimated. **It shows magnitude, not ease or value** — the widest band isn't always the right first project; some big losses (spent grain) are largely irreducible or already [sold as feed]({{ '/2026/four-types-data-analytics-distillery-fabric/' | relative_url }}), while a smaller, cheaply-recoverable loss may pay back faster, so read the Sankey alongside cost and feasibility, not instead of them. **Balances must actually balance** — if inputs and outputs don't reconcile, you have a measurement gap, not a diagram problem, and a Sankey that's been "fudged to close" lies confidently. And **one snapshot isn't a trend** — a single brew's balance can mislead; build it from enough batches to be representative.

## The bottom line

The losses a brewery could most act on hide in the gaps between a dozen separate reports, and a Sankey diagram drags them into one picture — extract, water or energy drawn as bands sized by quantity, with the widest loss band pointing at the first place to act. It turns diffuse data into a ranked priority list the whole team reads the same way. Meter the real stages so the bands are honest, label estimates, and weigh band width against cost and feasibility before committing. That closes this series on the charts brewers underuse: [radar conformance]({{ '/2026/true-to-target-batch-brand-profile-viz/' | relative_url }}), [drift-catching SPC]({{ '/2026/spc-capability-cusum-ewma-brewing/' | relative_url }}), [shelf-life trajectories]({{ '/2026/shelf-life-flavour-stability-trial-viz/' | relative_url }}) and now the Sankey balance — each matched to a question the line chart answers badly.

## Frequently asked questions

**What is a Sankey diagram and how does a brewery use one?**
A Sankey diagram shows flows as bands whose width is proportional to quantity, so you see at a glance where a resource goes and where it's lost. A brewery can map extract from grain through mash, kettle, fermenter and packaging to finished beer; water from intake through brewing, cleaning and cooling to effluent; or energy from fuel and electricity to useful heat versus losses. The widest "loss" band is where to look first.

**How do you visualize brewhouse efficiency and losses?**
A mass or energy balance rendered as a Sankey is the clearest single view: total input on the left, useful output and each loss as bands flowing right, sized by quantity. It turns a dozen separate yield, water and energy reports into one picture where the biggest leak is literally the widest band, making it far easier to prioritise than rows of percentages.

**What data do you need for a brewery Sankey diagram?**
Measured quantities at each stage of the flow you're mapping — for extract, the kg of extract entering and leaving mash, kettle, fermenter and packaging; for water, metered use by area; for energy, metered fuel and electricity by use. A Sankey is only as honest as the measurements behind it; gaps get hidden in a vague "losses" band, so meter the major stages before trusting the picture.
