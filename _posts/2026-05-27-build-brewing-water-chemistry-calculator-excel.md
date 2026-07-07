---
layout: post
title: "Build a Brewing Water Chemistry Calculator in Excel"
image: /assets/og/build-brewing-water-chemistry-calculator-excel.png
description: "A step-by-step Excel water calculator for brewers: enter your source profile, add salts, and read out calcium, sulfate, chloride, residual alkalinity and the sulfate-to-chloride ratio."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
tags: [brewing-science, excel, water-chemistry, recipe-formulation]
faq:
  - q: "How do I calculate brewing salt additions in Excel?"
    a: "Build a table where each salt's grams are multiplied by its ppm-per-gram-per-litre contribution, summed, and divided by your total water volume. For example, gypsum adds 232.8 ppm calcium and 557.9 ppm sulfate per gram per litre, so =source_ppm+(gypsum_g*232.8)/litres gives your new calcium level."
  - q: "What is residual alkalinity and how do I work it out?"
    a: "Residual alkalinity (RA) is the alkalinity your calcium and magnesium cannot offset, and it drives mash pH. The formula is RA = alkalinity − (calcium ÷ 3.5 + magnesium ÷ 7), all in ppm as CaCO₃. In Excel: =B2-(B3/3.5+B4/7)."
  - q: "What sulfate-to-chloride ratio should I aim for?"
    a: "Below ~0.5 leans malty, around 1 is balanced, and above ~2 accentuates hop bitterness and dryness. It is a ratio, not a target concentration, so two waters with very different mineral levels can share the same balance. Calculate it as =sulfate/chloride."
---

**Short answer: a brewing water calculator is just a salt-addition table plus four read-out formulas. Enter your source water profile, type in grams of each brewing salt, and Excel returns your finished calcium, magnesium, sodium, sulfate and chloride levels, the residual alkalinity that sets mash pH, and the sulfate-to-chloride ratio that sets the malt–hop balance. No add-ins, and you can see exactly how every number moves.**

This expands use case 9 from the [20 brewing calculations in Excel]({{ '/2026/advanced-brewing-calculations-excel/' | relative_url }}) pillar into a full sheet you can keep next to the brewhouse. It's the manual, transparent cousin of the [AI water-chemistry models]({{ '/2023/ai-brewing-water-chemistry-optimization/' | relative_url }}) — same arithmetic, fully visible.

## Step 1 — lay out the source water

Put your water report across one row, in ppm: calcium (Ca), magnesium (Mg), sodium (Na), sulfate (SO₄), chloride (Cl) and alkalinity (as CaCO₃). If you brew on RO or distilled water, every cell is zero and you are building the profile from scratch — the easiest case to model. Put your total treated volume (mash plus sparge, in litres) in its own cell; that single denominator drives the whole sheet.

## Step 2 — the salt contribution table

Each salt dissolves to add a fixed amount of each ion per gram per litre. Hard-code this table once:

| Salt | Adds (ppm per g/L) |
|---|---|
| Gypsum (CaSO₄·2H₂O) | Ca +232.8, SO₄ +557.9 |
| Calcium chloride (CaCl₂·2H₂O) | Ca +272.6, Cl +482.3 |
| Epsom salt (MgSO₄·7H₂O) | Mg +98.6, SO₄ +389.7 |
| Table salt (NaCl) | Na +393.4, Cl +606.6 |
| Baking soda (NaHCO₃) | Na +273.6, alkalinity +595 |

A salt's contribution to the batch is `grams × ppm-per-g/L ÷ litres`. So calcium after additions is the source plus every calcium-bearing salt:

`=Ca_source + (gypsum_g*232.8 + cacl2_g*272.6)/litres`

Repeat the pattern for each ion (sulfate gets gypsum and Epsom; chloride gets calcium chloride and salt; and so on). Lay the salt grams in their own input cells so you can dial them while watching the read-outs change.

Worked example: 5 g gypsum in 30 L raises calcium by `5*232.8/30 = 38.8 ppm` and sulfate by `5*557.9/30 = 93 ppm`.

## Step 3 — the four read-outs that matter

With finished ion levels in place, four formulas tell you whether the water suits the beer.

- **Residual alkalinity** (sets mash pH): `=alkalinity-(Ca/3.5+Mg/7)`. Pale, hoppy beers want low or negative RA; dark beers tolerate or even need positive RA so the roasted malt acidity has something to push against.
- **Sulfate-to-chloride ratio** (sets balance): `=SO4/Cl`. See the spectrum below.
- **Total calcium** (process health): aim for roughly 50–150 ppm — calcium drops mash pH, aids clarity, helps yeast floc and protects against beerstone problems at the high end.
- **Effective hardness check**: keeping sodium under ~150 ppm and magnesium under ~30 ppm avoids a minerally, harsh finish.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 180" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Sulfate to chloride ratio spectrum from malty to balanced to hoppy">
<rect x="0" y="0" width="760" height="180" fill="#ffffff"/>
<text x="380" y="30" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#06483f">Sulfate : chloride ratio — the malt–hop dial</text>
<rect x="60" y="70" width="80" height="40" fill="#06483f"/>
<rect x="140" y="70" width="80" height="40" fill="#4db6a2"/>
<rect x="220" y="70" width="160" height="40" fill="#00695c"/>
<rect x="380" y="70" width="320" height="40" fill="#2e9e7c"/>
<polygon points="540,62 533,52 547,52" fill="#06483f"/>
<text x="540" y="46" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#06483f">you: 3.0</text>
<g font-family="sans-serif" font-size="12" fill="#4a6b64" text-anchor="middle">
<text x="100" y="128">0.5</text><text x="220" y="128">1.0</text><text x="380" y="128">2.0</text><text x="700" y="128">4.0</text>
</g>
<g font-family="sans-serif" font-size="13" font-weight="700" text-anchor="middle">
<text x="100" y="152" fill="#06483f">malty</text><text x="300" y="152" fill="#00695c">balanced</text><text x="540" y="152" fill="#2e9e7c">hoppy / dry</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The ratio, not the absolute levels, sets perceived balance. A pale ale sits comfortably at 2–4; a malty lager near 0.5.</figcaption>
</figure>

## Where the sheet is only an estimate

Two honest caveats. First, **mash pH is the goal, not these ions directly** — RA and calcium predict the *direction* pH will move, but grist colour and acidity matter just as much, so the only truth is a calibrated pH meter reading at mash temperature. A full pH model needs each malt's acidity, which is more than a one-row sheet carries. Second, **chalk (CaCO₃) barely dissolves** in a cold mash, so any sheet that lets you add it as if fully soluble overstates the alkalinity you actually get; prefer baking soda for raising alkalinity and acid (not subtraction) for lowering it. Treat the read-outs as a recipe target you then confirm with a meter.

## The bottom line

A useful brewing water calculator is three things: a source row, a salt table, and four read-out formulas. Build it once and you can design a water profile for any style in minutes, see instantly how 2 grams of gypsum shifts the balance, and stop guessing. Just remember the sheet predicts *additions* precisely and *mash pH* only approximately — keep a meter in the loop.

## Frequently asked questions

**How do I calculate brewing salt additions in Excel?**
Build a table where each salt's grams are multiplied by its ppm-per-gram-per-litre contribution, summed, and divided by your total water volume. For example, gypsum adds 232.8 ppm calcium and 557.9 ppm sulfate per gram per litre, so =source_ppm+(gypsum_g*232.8)/litres gives your new calcium level.

**What is residual alkalinity and how do I work it out?**
Residual alkalinity (RA) is the alkalinity your calcium and magnesium cannot offset, and it drives mash pH. The formula is RA = alkalinity − (calcium ÷ 3.5 + magnesium ÷ 7), all in ppm as CaCO₃. In Excel: =B2-(B3/3.5+B4/7).

**What sulfate-to-chloride ratio should I aim for?**
Below ~0.5 leans malty, around 1 is balanced, and above ~2 accentuates hop bitterness and dryness. It is a ratio, not a target concentration, so two waters with very different mineral levels can share the same balance. Calculate it as =sulfate/chloride.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
