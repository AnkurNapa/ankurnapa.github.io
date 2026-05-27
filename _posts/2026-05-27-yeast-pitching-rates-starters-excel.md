---
layout: post
title: "Yeast Pitching Rates and Starters in Excel"
image: /assets/og/yeast-pitching-rates-starters-excel.png
description: "Size your yeast properly in a spreadsheet: cells required by gravity and volume, viability decay by pack age, packs needed, and a simple starter-growth model with worked examples."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
tags: [brewing-science, excel, yeast, fermentation]
faq:
  - q: "How do I calculate how much yeast to pitch?"
    a: "Cells required (in billions) = pitch rate × volume in litres × gravity in °Plato, where the rate is about 0.75 million cells per mL per °P for ales and 1.5 for lagers. In Excel that is =rate*litres*plato, so a 23 L ale at 12 °P needs 0.75×23×12 ≈ 207 billion cells."
  - q: "How does yeast viability change with age?"
    a: "Liquid yeast loses roughly 21% viability per month, about 0.7% per day from its manufacture date. Model it as =MAX(0,100-0.7*days)/100 to get the surviving fraction, then multiply the pack's cell count by it to find how many live cells you are really pitching."
  - q: "How big a yeast starter do I need?"
    a: "Estimate ending cells as =MIN(starter_litres*200, viable_cells_pitched + 140*starter_litres) billion. The first term is the density a stirred starter tops out at (~200 billion/L); the second is growth of about 1.4 billion new cells per gram of the ~100 g/L of extract in the starter."
---

**Short answer: pitching rate is three multiplications and viability is one subtraction. Cells needed (billion) = rate × litres × °Plato; live cells in an ageing pack = pack count × (1 − 0.007 × days); and a stirred starter ends near MIN(volume × 200, pitched + 140 × volume) billion cells. Put those in a sheet and you will stop under-pitching — the single most common avoidable fermentation fault.**

This takes use case 13 from the [20 brewing calculations in Excel]({{ '/2026/advanced-brewing-calculations-excel/' | relative_url }}) pillar and adds the two things that decide whether you actually hit the target: an ageing pack's real cell count, and how much a starter grows. It pairs with the data-driven view of [yeast viability and vitality]({{ '/2023/predicting-yeast-viability-vitality/' | relative_url }}).

## Step 1 — how many cells the beer needs

The target is a pitch rate in million cells per millilitre per degree Plato: about 0.75 for ales, 1.5 for lagers, higher for big beers. Multiply it out:

`cells_billion = rate * litres * plato`  →  `=B2*B3*B4`

A 23 L ale at 12 °P needs `0.75*23*12 = 207` billion cells. The same wort as a lager needs `1.5*23*12 = 414` billion — which is why lagers so often need a starter or multiple packs.

## Step 2 — how many cells you actually have

A fresh liquid pack is ~100 billion cells, but it bleeds viability at roughly 21% a month, about 0.7% a day from the date stamped on it. So the live count is what matters:

`viability = MAX(0,100-0.7*days)/100`
`live_cells = packs * 100 * viability`

A pack stamped 45 days ago is at `100-0.7*45 = 68.5%` viability — so two packs give `2*100*0.685 = 137` billion live cells, well short of even the ale target. The decay below is why "it's only a few weeks old" is not the same as enough yeast.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 620 340" width="100%" style="max-width:620px;height:auto" role="img" aria-label="Yeast viability declining roughly linearly from 100 percent at manufacture to about 16 percent at 120 days">
<rect x="0" y="0" width="620" height="340" fill="#fdfbf7"/>
<text x="320" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Liquid yeast viability vs pack age</text>
<g stroke="#e0d8cc" stroke-width="1"><line x1="60" y1="170" x2="560" y2="170"/></g>
<g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="40" x2="60" y2="300"/><line x1="60" y1="300" x2="560" y2="300"/></g>
<polyline points="60,40 185,94.6 310,149.2 435,203.8 560,258.4" fill="none" stroke="#b45309" stroke-width="3"/>
<circle cx="310" cy="149.2" r="5" fill="#7a1f3d"/>
<text x="318" y="143" font-family="sans-serif" font-size="12" fill="#7a1f3d">60 days ≈ 58%</text>
<g font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle">
<text x="60" y="318">0</text><text x="185" y="318">30</text><text x="310" y="318">60</text><text x="435" y="318">90</text><text x="560" y="318">120</text>
<text x="320" y="338">Days since manufacture</text>
</g>
<g font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="end">
<text x="52" y="44">100%</text><text x="52" y="174">50%</text><text x="52" y="304">0%</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Roughly 0.7% lost per day. Plug your pack's age into =MAX(0,100-0.7*days)/100 before you trust the cell count on the label.</figcaption>
</figure>

## Step 3 — size the starter to close the gap

If live cells fall short of the target, a starter grows more. A stirred 1.040 starter carries about 100 g of extract per litre and tops out near 200 billion cells per litre; growth runs around 1.4 billion new cells per gram of extract. Combine the cap and the growth:

`ending_cells = MIN(starter_litres*200, live_cells + 140*starter_litres)`

From the 137 billion live cells above, a 2 L starter ends at `MIN(2*200, 137+140*2) = MIN(400,417) = 400` billion — comfortably past the ale target and into lager territory. Add a column for grams of dry malt extract (`starter_litres*100`) so your shopping list falls out of the same sheet.

## Where the model gets loose

Two honest limits. First, **growth depends on aeration and agitation** — the 1.4-per-gram figure assumes a stir plate or frequent shaking; a still starter grows far less, and these formulas will overstate it. Second, **a count is an estimate until you measure it**; the only way to truly know your cell density is a haemocytometer and a microscope, or a measured pitch from a slurry. Use the sheet to get into the right order of magnitude and to stop habitual under-pitching, not to claim three-significant-figure precision the biology won't honour.

## The bottom line

Three formulas turn "pitch a pack and hope" into a sized decision: cells needed from gravity and volume, live cells after viability decay, and the ending count from a starter. Build them once, enter the date on the pack, and you will catch the under-pitch before it becomes a slow, estery, or stalled fermentation — not after.

## Frequently asked questions

**How do I calculate how much yeast to pitch?**
Cells required (in billions) = pitch rate × volume in litres × gravity in °Plato, where the rate is about 0.75 million cells per mL per °P for ales and 1.5 for lagers. In Excel that is =rate*litres*plato, so a 23 L ale at 12 °P needs 0.75×23×12 ≈ 207 billion cells.

**How does yeast viability change with age?**
Liquid yeast loses roughly 21% viability per month, about 0.7% per day from its manufacture date. Model it as =MAX(0,100-0.7*days)/100 to get the surviving fraction, then multiply the pack's cell count by it to find how many live cells you are really pitching.

**How big a yeast starter do I need?**
Estimate ending cells as =MIN(starter_litres*200, viable_cells_pitched + 140*starter_litres) billion. The first term is the density a stirred starter tops out at (~200 billion/L); the second is growth of about 1.4 billion new cells per gram of the ~100 g/L of extract in the starter.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
