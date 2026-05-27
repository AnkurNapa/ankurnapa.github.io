---
layout: post
title: "Brewhouse Efficiency and Yield Reconciliation in Excel"
image: /assets/og/brewhouse-efficiency-yield-excel.png
description: "Separate conversion, lauter and brewhouse efficiency in one Excel sheet, reconcile predicted versus actual gravity, and diagnose exactly where your extract is being lost."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
tags: [brewing-science, excel, efficiency, quality-control]
faq:
  - q: "How do I calculate brewhouse efficiency in Excel?"
    a: "Brewhouse efficiency = collected gravity points ÷ maximum possible points. In Excel: =((OG-1)*1000*gallons)/SUMPRODUCT(weights,PPGs). For 5.5 gallons at OG 1.050 against 370 potential points that is (50×5.5)/370 ≈ 74%."
  - q: "What is the difference between conversion and lauter efficiency?"
    a: "Conversion efficiency is how much of the grain's starch the mash turned to sugar (typically ~95%). Lauter efficiency is how much of that sugar you actually rinsed into the kettle. Brewhouse efficiency is the two multiplied together, so a low number tells you which stage to fix."
  - q: "Why did my original gravity come in low?"
    a: "Split the miss: if conversion efficiency is low, suspect crush, mash pH, or rest time; if lauter efficiency is low, suspect sparging, grain absorption, or dead space. Reconciling predicted against actual points in a sheet points you at the right cause instead of guessing."
---

**Short answer: efficiency is one division done three ways. Brewhouse efficiency = collected points ÷ potential points; conversion efficiency = how much starch became sugar; and lauter efficiency = collected ÷ converted. Because brewhouse = conversion × lauter, splitting them in Excel tells you whether a low OG is a mash problem or a sparge problem — instead of leaving you to guess.**

This is the deep dive on use cases 2 and 3 from the [20 brewing calculations in Excel]({{ '/2026/advanced-brewing-calculations-excel/' | relative_url }}) pillar: not just measuring efficiency, but decomposing it to find the leak. It's the hands-on companion to [brewhouse yield-loss analytics]({{ '/2023/brewhouse-yield-loss-analytics/' | relative_url }}) and ties straight into [mash efficiency and extract yield]({{ '/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}).

## Step 1 — potential and collected points

Maximum extract is the grain bill's potential: each malt's weight times its points-per-pound-per-gallon. Collected extract is what you actually got, from measured OG and volume:

`potential =SUMPRODUCT(weights,PPGs)`   (10 lb pale × 37 = 370)
`collected =(OG-1)*1000*gallons`        (50 × 5.5 = 275)
`brewhouse_eff =collected/potential`     (275 / 370 = 74%)

That 74% is the headline — but it doesn't say *where* the missing 26% went.

## Step 2 — split conversion from lauter

Conversion efficiency is how completely the mash turned starch to sugar (a fine-crush, well-rested, correct-pH mash hits ~95%). Lauter efficiency is how much of that sugar you rinsed out. They chain:

`after_conversion =potential*conv_eff`   (370 × 0.95 = 351.5)
`lauter_eff =collected/after_conversion` (275 / 351.5 = 78%)

So our 74% brewhouse efficiency is 95% conversion × 78% lauter. The waterfall makes the two losses visible side by side.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 700 360" width="100%" style="max-width:700px;height:auto" role="img" aria-label="Efficiency waterfall: 370 potential points lose 18.5 to conversion and 76.5 to lauter, leaving 275 collected">
<rect x="0" y="0" width="700" height="360" fill="#fdfbf7"/>
<text x="350" y="26" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Where the extract goes (gravity points)</text>
<g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="40" x2="60" y2="320"/><line x1="60" y1="320" x2="660" y2="320"/></g>
<g stroke="#6b6258" stroke-width="1" stroke-dasharray="4 3">
<line x1="160" y1="61" x2="190" y2="61"/><line x1="280" y1="73.95" x2="310" y2="73.95"/>
<line x1="400" y1="73.95" x2="430" y2="73.95"/><line x1="520" y1="127.5" x2="550" y2="127.5"/>
</g>
<rect x="70" y="61" width="90" height="259" fill="#b45309"/>
<rect x="190" y="61" width="90" height="12.95" fill="#7a1f3d"/>
<rect x="310" y="73.95" width="90" height="246.05" fill="#a9743a"/>
<rect x="430" y="73.95" width="90" height="53.55" fill="#7a1f3d"/>
<rect x="550" y="127.5" width="90" height="192.5" fill="#b45309"/>
<g font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17" text-anchor="middle">
<text x="115" y="53">370</text><text x="235" y="55">−18.5</text><text x="355" y="66">351.5</text><text x="475" y="66">−76.5</text><text x="595" y="120">275</text>
</g>
<g font-family="sans-serif" font-size="11.5" fill="#6b6258" text-anchor="middle">
<text x="115" y="338">Potential</text><text x="235" y="338">Conversion</text><text x="355" y="338">Converted</text><text x="475" y="338">Lauter loss</text><text x="595" y="338">Collected</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The mash barely loses anything (95% conversion); the real leak is the lauter — sugar left in grain absorption and dead space.</figcaption>
</figure>

## Step 3 — reconcile and diagnose

Add a "predicted OG" cell from your *expected* brewhouse efficiency and compare to actual:

`predicted_OG =1+(potential*expected_eff)/(gallons*1000)`

When actual falls short, the split tells you where to look. **Low conversion** (the mash made less sugar than it should) points at crush coarseness, mash pH, rest temperature or time. **Low lauter** (you made the sugar but didn't collect it) points at sparge technique, grain absorption, or kettle/tun dead space — the same losses you sized in the [mash water calculator]({{ '/2026/mash-water-temperature-calculator-excel/' | relative_url }}). One sheet, and a missed OG becomes a named cause.

## Where the decomposition gets fuzzy

Two honest caveats. First, **conversion efficiency is hard to measure directly** without a fine-grind lab test or a first-wort gravity reading, so most brewers assume ~95% and attribute the rest to lauter; if your real conversion is poor, the sheet will wrongly blame the sparge. A first-runnings gravity reading is the cheap fix — it splits the two for real. Second, **PPG values are nominal** — maltsters publish potential under lab conditions, and your actual extract depends on the specific lot, so treat the efficiency number as consistent-relative-to-itself rather than a universal grade. Track it across brews and the *trend* is what catches a drifting mill or a tired mash tun.

## The bottom line

Efficiency is one division, but doing it three ways — brewhouse, conversion, lauter — turns "my OG was low again" into "my lauter efficiency dropped, check the crush gap." Reconcile predicted against actual every brew, and the sheet stops being a scorecard and starts being a diagnosis.

## Frequently asked questions

**How do I calculate brewhouse efficiency in Excel?**
Brewhouse efficiency = collected gravity points ÷ maximum possible points. In Excel: =((OG-1)*1000*gallons)/SUMPRODUCT(weights,PPGs). For 5.5 gallons at OG 1.050 against 370 potential points that is (50×5.5)/370 ≈ 74%.

**What is the difference between conversion and lauter efficiency?**
Conversion efficiency is how much of the grain's starch the mash turned to sugar (typically ~95%). Lauter efficiency is how much of that sugar you actually rinsed into the kettle. Brewhouse efficiency is the two multiplied together, so a low number tells you which stage to fix.

**Why did my original gravity come in low?**
Split the miss: if conversion efficiency is low, suspect crush, mash pH, or rest time; if lauter efficiency is low, suspect sparging, grain absorption, or dead space. Reconciling predicted against actual points in a sheet points you at the right cause instead of guessing.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
