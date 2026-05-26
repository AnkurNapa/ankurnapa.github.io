---
layout: post
title: "Mash Water and Temperature Calculator in Excel"
image: /assets/og/mash-water-temperature-calculator-excel.png
description: "Work out strike temperature, mash and sparge water volumes, grain absorption and total water needed in one Excel sheet — with a water balance that shows where every litre goes."
date: 2026-05-30 09:00:00 -0700
updated: 2026-05-30
tags: [brewing-science, excel, mashing, water-volumes]
faq:
  - q: "How do I calculate strike water temperature in metric?"
    a: "Strike temp Tw = (0.41/R)(T2 − T1) + T2, where R is the water-to-grain ratio in litres per kilogram, T1 is grain temperature and T2 is the target mash temperature, all in °C. In Excel: =(0.41/B2)*(B4-B3)+B4. For imperial (qt/lb, °F) use the constant 0.2 instead of 0.41."
  - q: "How much water does grain absorb in the mash?"
    a: "Crushed malt retains roughly 1 litre per kilogram (about 0.125 gallons per pound). Multiply your grain weight by that figure to get the water that never makes it to the kettle, then add it to your sparge calculation so you still hit your pre-boil volume."
  - q: "How do I work out sparge water volume?"
    a: "Total water needed = pre-boil volume + grain absorption + mash tun dead space, where pre-boil volume = into-fermenter + trub loss + boil-off. Sparge water is then total water minus mash water. Build it as a small chain of additions in Excel and the sparge figure falls out automatically."
---

**Short answer: mash water planning is one temperature formula and one volume chain. Strike temp = (0.41/R)(T2 − T1) + T2 in metric; and total water = pre-boil + grain absorption + dead space, with sparge = total − mash. Lay those out in Excel and you will hit both your mash temperature and your pre-boil volume on the first try, every brew.**

This builds out use cases 5, 7 and 8 from the [20 brewing calculations in Excel]({{ '/2026/advanced-brewing-calculations-excel/' | relative_url }}) pillar into a single water-and-temperature planner. Getting the volumes right is also half the battle in [mash efficiency]({{ '/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}) — miss your volumes and your gravity misses too.

## Step 1 — strike temperature

Cold grain pulls the mix down, so the liquor must go in hotter than your target rest. With R as the water-to-grain ratio (L/kg), T1 the grain temperature and T2 the target mash temperature (°C):

`=(0.41/B2)*(B4-B3)+B4`

Example: R = 3.0 L/kg, grain at 18 °C, target 66 °C → `(0.41/3.0)*(66-18)+66 = 72.6 °C`. (Working in qt/lb and °F? Swap the 0.41 for 0.2.)

## Step 2 — the volume chain

Build the volumes from the fermenter backwards, because that is the number you actually care about. Put each loss in its own cell:

- **Mash water** = grain × ratio → `=B2*B3` (4.5 kg × 3.0 = 13.5 L)
- **Grain absorption** = grain × 1.0 L/kg → `=B2*1.0` (4.5 L — water that never reaches the kettle)
- **Pre-boil** = into-fermenter + trub loss + boil-off → `=B5+B6+B7` (19 + 2 + 4 = 25 L)
- **Total water** = pre-boil + absorption + dead space → `=25+4.5+1.0` (30.5 L)
- **Sparge water** = total − mash → `=B_total-B_mash` (30.5 − 13.5 = 17 L)

Now changing any single loss — a longer boil, a deeper grain bed, a different batch size — reflows the whole sheet, and your sparge volume updates with it.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 200" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Water balance bar showing 30.5 litres splitting into fermenter, trub, boil-off, grain absorption and dead space">
<rect x="0" y="0" width="760" height="200" fill="#fdfbf7"/>
<text x="380" y="30" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Where 30.5 L of brewing water goes</text>
<rect x="60" y="60" width="398.6" height="44" fill="#b45309"/>
<rect x="458.6" y="60" width="42" height="44" fill="#7a1f3d"/>
<rect x="500.6" y="60" width="83.9" height="44" fill="#a9743a"/>
<rect x="584.5" y="60" width="94.4" height="44" fill="#8a5a2b"/>
<rect x="678.9" y="60" width="21" height="44" fill="#6b6258"/>
<text x="259" y="88" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#fdfbf7">into fermenter 19 L</text>
<g font-family="sans-serif" font-size="12.5" fill="#1c1a17">
<rect x="60" y="135" width="14" height="14" fill="#b45309"/><text x="80" y="147">Into fermenter — 19 L</text>
<rect x="250" y="135" width="14" height="14" fill="#7a1f3d"/><text x="270" y="147">Trub / chiller loss — 2 L</text>
<rect x="470" y="135" width="14" height="14" fill="#a9743a"/><text x="490" y="147">Boil-off — 4 L</text>
<rect x="60" y="160" width="14" height="14" fill="#8a5a2b"/><text x="80" y="172">Grain absorption — 4.5 L</text>
<rect x="250" y="160" width="14" height="14" fill="#6b6258"/><text x="270" y="172">Mash tun dead space — 1 L</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Only ~62% of the water you heat ends up as beer. The rest is absorbed, evaporated, or left behind — which is exactly why sparge volume has to account for it.</figcaption>
</figure>

## Step 3 — step mashes and mash-out

For a step mash, each rise needs an addition of boiling water (or a decoction). Boiling-water infusion in litres, with G as grain (kg), Wm as water already in the mash (L), T in °C and infusion water at 100 °C:

`=(T2-T1)*(0.41*G+Wm)/(100-T2)`

Stack a row per step — protein rest to saccharification to mash-out — and the sheet tells you how much boiling water each jump costs, and whether you'll overflow the tun before you get there.

## Where the numbers drift

Two honest caveats. First, **absorption and dead space are equipment constants you must measure once** — 1 L/kg and your tun's true dead volume vary by crush, false-bottom design and grain bill; brew once, reconcile actual pre-boil against the sheet, and correct the constants. Second, **boil-off is a rate, not a fixed figure** — it depends on kettle geometry, lid, and how hard you boil, so a number borrowed from someone else's system will be wrong on yours. The structure of the sheet is universal; the three constants (absorption, dead space, boil-off rate) are yours alone, and a single measured brew calibrates them.

## The bottom line

One temperature formula and a five-line volume chain give you strike temperature, mash water, sparge water and total water in a sheet that reflows the instant you change a loss. Calibrate the three equipment constants once from a real brew, and you'll stop both the cold mash-in and the "where did my pre-boil volume go" surprise.

## Frequently asked questions

**How do I calculate strike water temperature in metric?**
Strike temp Tw = (0.41/R)(T2 − T1) + T2, where R is the water-to-grain ratio in litres per kilogram, T1 is grain temperature and T2 is the target mash temperature, all in °C. In Excel: =(0.41/B2)*(B4-B3)+B4. For imperial (qt/lb, °F) use the constant 0.2 instead of 0.41.

**How much water does grain absorb in the mash?**
Crushed malt retains roughly 1 litre per kilogram (about 0.125 gallons per pound). Multiply your grain weight by that figure to get the water that never makes it to the kettle, then add it to your sparge calculation so you still hit your pre-boil volume.

**How do I work out sparge water volume?**
Total water needed = pre-boil volume + grain absorption + mash tun dead space, where pre-boil volume = into-fermenter + trub loss + boil-off. Sparge water is then total water minus mash water. Build it as a small chain of additions in Excel and the sparge figure falls out automatically.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
