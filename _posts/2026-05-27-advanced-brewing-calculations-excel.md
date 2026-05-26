---
layout: post
title: "20 Advanced Brewing Calculations You Can Do in Excel (Formulas Included)"
image: /assets/og/advanced-brewing-calculations-excel.png
description: "Strike temperature, IBU, ABV, pitching rate, carbonation, colour, efficiency and more — 20 advanced brewing calculations as ready-to-paste Excel formulas with worked examples."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
tags: [brewing-science, excel, brewing-calculations, recipe-formulation, quality-control]
faq:
  - q: "Can you calculate ABV in Excel?"
    a: "Yes. The standard formula is =(OG-FG)*131.25, where OG and FG are your original and final specific gravities. For higher-strength beers a more accurate version is =(76.08*(OG-FG)/(1.775-OG))*(FG/0.794). Both work in any version of Excel with no add-ins."
  - q: "What is the Excel formula for mash strike water temperature?"
    a: "Strike temp Tw = (0.2/R)(T2-T1)+T2, where R is the water-to-grain ratio in quarts per pound, T1 is grain temperature and T2 is your target mash temperature in °F. In Excel: =(0.2/B2)*(B4-B3)+B4 with R in B2, grain temp in B3 and target in B4. For metric (L/kg, °C) swap the 0.2 for 0.41."
  - q: "Do I need special brewing software to do these calculations?"
    a: "No. Every calculation here — gravity, efficiency, IBU, colour, pitching rate, carbonation, ABV — is just arithmetic that brewing software runs under the hood. A single Excel sheet with these formulas reproduces it, and because you can see every cell you understand and trust the result."
---

**Short answer: every number a brewing app gives you — strike temperature, IBU, ABV, pitching rate, priming sugar, colour, efficiency — is plain arithmetic you can build in one Excel sheet with no add-ins. Below are 20 advanced brewing calculations as ready-to-paste formulas with worked examples, organised across the brew day. Set up the cells once and you have a brewhouse calculator you fully understand.**

Brewing software hides the maths. That's fine until you need to tweak a recipe at 6 a.m., reconcile an efficiency miss, or explain a carbonation set point to a new brewer. A spreadsheet you built yourself does all of it and shows its working. If you are still talking yourself into the idea, [collecting the data first]({{ '/2026/collect-your-data-before-ai/' | relative_url }}) is the right instinct — these formulas are what turn those numbers into decisions.

A convention for the whole article: cell references like `B2` are examples — put your input in that cell and paste the formula next to it. Gravities are specific gravity (e.g. 1.050) unless stated; "points" means the last three digits ((SG − 1) × 1000), so 1.050 = 50 points. Spellings are British (colour, litres); imperial and metric notes are given where the constant changes.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1046 280" width="100%" style="max-width:1046px;height:auto" role="img" aria-label="Brew-day process flow showing which of the 20 calculations apply at each stage">
<rect x="0" y="0" width="1046" height="280" fill="#fdfbf7"/>
<text x="523" y="34" text-anchor="middle" font-family="sans-serif" font-size="18" font-weight="700" fill="#1c1a17">The brew day, by the numbers — where each calculation lands</text>
<g font-family="sans-serif">
<rect x="4" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="83" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">RECIPE</text>
<text x="83" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">1 · SG ↔ °Plato</text>
<text x="83" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">2 · OG from grist</text>
<text x="83" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">3 · Efficiency</text>
<text x="83" y="186" text-anchor="middle" font-size="12.5" fill="#1c1a17">12 · Colour SRM</text>
<rect x="180" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="259" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">MASH</text>
<text x="259" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">5 · Strike temp</text>
<text x="259" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">6 · Step infusion</text>
<text x="259" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">7 · Liquor:grist</text>
<text x="259" y="186" text-anchor="middle" font-size="12.5" fill="#1c1a17">9 · Water salts</text>
<rect x="356" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="435" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">BOIL</text>
<text x="435" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">8 · Boil-off</text>
<text x="435" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">10 · IBU (Tinseth)</text>
<text x="435" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">11 · Hop sub</text>
<rect x="532" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="611" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">FERMENT</text>
<text x="611" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">13 · Pitch rate</text>
<text x="611" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">14 · Attenuation</text>
<text x="611" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">4 · Temp correct</text>
<text x="611" y="186" text-anchor="middle" font-size="12.5" fill="#1c1a17">15 · Refractometer</text>
<rect x="708" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="787" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309">PACKAGE</text>
<text x="787" y="114" text-anchor="middle" font-size="12.5" fill="#1c1a17">16 · ABV</text>
<text x="787" y="138" text-anchor="middle" font-size="12.5" fill="#1c1a17">17 · Carbonation</text>
<text x="787" y="162" text-anchor="middle" font-size="12.5" fill="#1c1a17">18 · Blend/dilute</text>
<text x="787" y="186" text-anchor="middle" font-size="12.5" fill="#1c1a17">19 · Calories</text>
<rect x="884" y="60" width="158" height="190" rx="8" fill="#f7ece0" stroke="#7a1f3d" stroke-width="1.5"/>
<text x="963" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#7a1f3d">COST</text>
<text x="963" y="118" text-anchor="middle" font-size="12.5" fill="#1c1a17">20 · COGS / hL</text>
<text x="963" y="142" text-anchor="middle" font-size="12.5" fill="#1c1a17">&amp; cost per pint</text>
</g>
<g fill="#b45309" stroke="#b45309" stroke-width="2">
<line x1="162" y1="155" x2="174" y2="155"/><polygon points="174,150 181,155 174,160" stroke="none"/>
<line x1="338" y1="155" x2="350" y2="155"/><polygon points="350,150 357,155 350,160" stroke="none"/>
<line x1="514" y1="155" x2="526" y2="155"/><polygon points="526,150 533,155 526,160" stroke="none"/>
<line x1="690" y1="155" x2="702" y2="155"/><polygon points="702,150 709,155 702,160" stroke="none"/>
<line x1="866" y1="155" x2="878" y2="155"/><polygon points="878,150 885,155 878,160" stroke="none"/>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The 20 calculations, mapped to the stage where you use them. Numbers below match this map.</figcaption>
</figure>

## Recipe and gravity

**1. Convert specific gravity to °Plato.** Brewers and instruments disagree on scale; convert without a lookup table.
Formula: °P ≈ 259 − (259 ÷ SG).
Excel (SG in `B2`): `=259-(259/B2)`. Reverse (Plato → SG): `=259/(259-B2)`.
Example: SG 1.048 → `=259-(259/1.048)` = **11.9 °P**.

**2. Predict original gravity from the grain bill.** Know your OG before you brew.
Formula: points = Σ(weight × PPG) × efficiency ÷ volume; OG = 1 + points ÷ 1000. PPG is points-per-pound-per-gallon (≈ 37 for pale malt).
Excel (weights in `B2:B6`, PPGs in `C2:C6`, efficiency in `F2`, post-boil gallons in `G2`): `=1+(SUMPRODUCT(B2:B6,C2:C6)*F2)/(G2*1000)`.
Example: 10 lb pale malt (PPG 37) at 75% into 5.5 gal → **1.050**.

**3. Brewhouse and mash efficiency.** The single number that explains why your OG missed.
Formula: efficiency = (measured points × volume) ÷ maximum possible points.
Excel (OG in `B2`, gallons collected in `B3`, total potential points Σ(lb × PPG) in `B4`): `=((B2-1)*1000*B3)/B4*100`.
Example: OG 1.050, 5.5 gal, 370 potential points → **74%**.

**4. Hydrometer temperature correction.** A warm sample reads low; correct it instead of guessing.
Formula: a cubic in sample temperature relative to the hydrometer's calibration temperature (°F).
Excel (measured SG `B2`, sample temp °F `B3`, calibration temp °F `B4`): `=B2*((1.00130346-0.000134722124*B3+0.00000204052596*B3^2-0.00000000232820948*B3^3)/(1.00130346-0.000134722124*B4+0.00000204052596*B4^2-0.00000000232820948*B4^3))`.
Example: 1.050 read at 100 °F, calibrated at 60 °F → **1.056**.

## Mash and water

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 230" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Strike water heat balance: hot liquor plus cool grain equals mash at target temperature">
<rect x="0" y="0" width="760" height="230" fill="#fdfbf7"/>
<rect x="20" y="60" width="180" height="110" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="110" y="100" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#1c1a17">Hot liquor</text>
<text x="110" y="126" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#b45309">Tw ≈ 164 °F</text>
<text x="110" y="150" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">(what you heat to)</text>
<text x="230" y="122" text-anchor="middle" font-family="sans-serif" font-size="30" font-weight="700" fill="#6b6258">+</text>
<rect x="260" y="60" width="180" height="110" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/>
<text x="350" y="100" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#1c1a17">Grain</text>
<text x="350" y="126" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#b45309">T1 = 65 °F</text>
<text x="350" y="150" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">(specific heat ≈ 0.2)</text>
<g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="450" y1="115" x2="490" y2="115"/><polygon points="490,108 502,115 490,122" stroke="none"/></g>
<rect x="510" y="60" width="220" height="110" rx="8" fill="#b45309"/>
<text x="620" y="100" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#fdfbf7">Mash tun</text>
<text x="620" y="126" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#fdfbf7">T2 = 152 °F target</text>
<text x="620" y="150" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#f7ece0">(what you want)</text>
<text x="380" y="205" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#1c1a17">Tw = (0.2 ÷ R)(T2 − T1) + T2  →  heat the water hotter to absorb the grain's cold mass</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Strike-water heat balance (use case 5): the water must run hot enough that cool grain pulls the mix down to target.</figcaption>
</figure>

**5. Strike (mash-in) water temperature.** Heat the liquor hot enough that cold grain lands you on target.
Formula: Tw = (0.2 ÷ R)(T2 − T1) + T2 — R = water:grain in qt/lb, T1 = grain temp, T2 = target mash temp (°F).
Excel (R in `B2`, grain temp in `B3`, target in `B4`): `=(0.2/B2)*(B4-B3)+B4`.
Example: R = 1.5 qt/lb, grain 65 °F, target 152 °F → **163.6 °F**. Metric (L/kg, °C): replace `0.2` with `0.41`.

**6. Step-mash infusion (boiling water addition).** How much boiling water raises the mash to the next rest.
Formula: Wa = (T2 − T1)(0.2·G + Wm) ÷ (Tw − T2) — G = grain (lb), Wm = water already in mash (qt), Tw = 212 °F.
Excel (G `B2`, current temp `B3`, target `B4`, mash water `B5`, infusion temp `B6`): `=(B4-B3)*(0.2*B2+B5)/(B6-B4)`.
Example: 10 lb, 152→168 °F, 15 qt in mash, 212 °F water → **6.2 qt**.

**7. Liquor-to-grist ratio (mash thickness).** Thin mashes favour fermentability; thick mashes protect enzymes.
Formula: ratio = water ÷ grain.
Excel (water `B2`, grain `B3`): `=B2/B3`. Convert qt/lb → L/kg with `=B2/B3*2.086`.
Example: 15 qt ÷ 10 lb = **1.5 qt/lb** (≈ 3.13 L/kg).

**8. Pre-boil volume and boil-off.** Hit your post-boil volume by starting with the right pre-boil.
Formula: pre-boil = target post-boil + (evaporation rate × boil hours); add ~4% for cooling shrinkage.
Excel (target post-boil litres `B2`, evap L/hr `B3`, hours `B4`): `=(B2/0.96)+B3*B4`.
Example: 23 L target, 4 L/hr, 1 hr → **≈ 28 L** pre-boil.

**9. Water chemistry — residual alkalinity and sulfate:chloride.** Two numbers that decide mash pH and hop character.
Formulas: RA = alkalinity − (Ca ÷ 3.5 + Mg ÷ 7), all as ppm; SO₄:Cl = sulfate ÷ chloride.
Excel (alkalinity as CaCO₃ `B2`, Ca `B3`, Mg `B4`, sulfate `B5`, chloride `B6`): RA `=B2-(B3/3.5+B4/7)`, ratio `=B5/B6`.
Salt additions (per gram per gallon): gypsum adds 61.5 ppm Ca + 147.4 ppm SO₄; calcium chloride adds 72 ppm Ca + 127.4 ppm Cl. New level: `=base_ppm + grams_per_gal*61.5`.
Example: alkalinity 100, Ca 50, Mg 10 → RA **84 ppm**; SO₄ 150, Cl 50 → **3.0** (hop-forward).

## Boil and hops

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 620 350" width="100%" style="max-width:620px;height:auto" role="img" aria-label="Tinseth hop utilisation curve rising steeply then plateauing by 60 minutes of boil">
<rect x="0" y="0" width="620" height="350" fill="#fdfbf7"/>
<text x="320" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Hop utilisation vs boil time (Tinseth)</text>
<g stroke="#e0d8cc" stroke-width="1">
<line x1="60" y1="40" x2="580" y2="40"/><line x1="60" y1="170" x2="580" y2="170"/>
</g>
<g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="40" x2="60" y2="300"/><line x1="60" y1="300" x2="580" y2="300"/></g>
<polyline points="60,300 117.8,217.3 175.6,161.9 233.3,124.9 291.1,100.1 406.7,72.1 493.3,61.9 580,56.2" fill="none" stroke="#b45309" stroke-width="3"/>
<g font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle">
<text x="60" y="318">0</text><text x="233" y="318">30</text><text x="406" y="318">60</text><text x="580" y="318">90</text>
<text x="320" y="340">Boil time (minutes)</text>
</g>
<text x="20" y="170" font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle" transform="rotate(-90 20 170)">Utilisation</text>
<line x1="406" y1="72" x2="470" y2="120" stroke="#7a1f3d" stroke-width="1"/>
<text x="475" y="124" font-family="sans-serif" font-size="12" fill="#7a1f3d">most bitterness</text>
<text x="475" y="140" font-family="sans-serif" font-size="12" fill="#7a1f3d">locked in by ~60 min</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Why a 90-minute addition isn't much more bitter than a 60-minute one (use case 10).</figcaption>
</figure>

**10. IBU by the Tinseth method.** The industry-standard bitterness estimate, in two cells.
Formulas: utilisation = (1.65 × 0.000125^(OG−1)) × ((1 − e^(−0.04·t)) ÷ 4.15); IBU = utilisation × (AA% × grams × 1000 ÷ litres).
Excel (AA% `B2`, grams `B3`, boil min `B4`, litres `B5`, OG `B6`): utilisation in `B7` = `=(1.65*0.000125^(B6-1))*((1-EXP(-0.04*B4))/4.15)`; IBU = `=B7*((B2/100)*B3*1000)/B5`.
Example: 28 g at 6.4% AA, 60 min, 23 L, OG 1.050 → **≈ 18 IBU**.

**11. Hop substitution by alpha acid.** Out of stock? Match the bitterness, not the weight.
Formula: new weight = (original weight × original AA%) ÷ new AA%.
Excel (original grams `B2`, original AA% `B3`, substitute AA% `B4`): `=(B2*B3)/B4`.
Example: recipe wants 28 g at 6.4%; you have 9.2% AA hops → **19.5 g**.

**12. Beer colour (SRM and EBC).** Estimate the glass before you mash.
Formulas: MCU = Σ(grain °L × weight lb) ÷ gallons; SRM = 1.4922 × MCU^0.6859 (Morey); EBC = SRM × 1.97.
Excel (°L `B2:B3`, weights `C2:C3`, gallons `D2`): MCU `E2` = `=SUMPRODUCT(B2:B3,C2:C3)/D2`; SRM `F2` = `=1.4922*E2^0.6859`; EBC = `=F2*1.97`.
Example: 9 lb pale (3 °L) + 1 lb crystal (60 °L) in 5.5 gal → MCU 15.8 → **≈ 10 SRM / 19 EBC** (amber).

## Yeast and fermentation

**13. Yeast pitching rate.** Under-pitching is the most common avoidable fault; size it.
Formula: billion cells = pitch rate (M cells/mL/°P) × volume (L) × °Plato. Rate ≈ 0.75 for ales, 1.5 for lagers.
Excel (rate `B2`, litres `B3`, °P `B4`): cells `=B2*B3*B4`; packs at 100 B each `=B2*B3*B4/100`.
Example: ale at 0.75, 23 L, 12 °P → **207 billion cells** ≈ 2 fresh packs or a starter.

**14. Apparent and real attenuation.** How far the yeast actually went.
Formulas: apparent = (OG − FG) ÷ (OG − 1) × 100; real ≈ apparent × 0.81 (true real degree uses real extract from Plato).
Excel (OG `B2`, FG `B3`): apparent `=(B2-B3)/(B2-1)*100`; real `=(B2-B3)/(B2-1)*100*0.81`.
Example: 1.050 → 1.010 → **80% apparent / ≈ 65% real**.

**15. Refractometer final-gravity correction.** Refractometers lie once alcohol is present; this fixes it.
Formula: Terrill cubic in initial and final Brix (divide each reading by your wort correction factor, ~1.04, first).
Excel (corrected initial Brix `B2`, corrected final Brix `B3`): `=1.0000-0.0044993*B2+0.011774*B3+0.00027581*B2^2-0.0012717*B3^2-0.00000728*B2^3+0.000063293*B3^3`.
Example: 12.5 → 6.0 Brix → FG **≈ 1.011**.

**16. ABV from gravity.** The headline number, two ways.
Formulas: simple = (OG − FG) × 131.25; more accurate (stronger beers) = (76.08 × (OG − FG) ÷ (1.775 − OG)) × (FG ÷ 0.794).
Excel (OG `B2`, FG `B3`): simple `=(B2-B3)*131.25`; accurate `=(76.08*(B2-B3)/(1.775-B2))*(B3/0.794)`.
Example: 1.050 → 1.011 → **5.1% (simple) / 5.2% (accurate)**.

## Packaging and finishing

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 560 300" width="100%" style="max-width:560px;height:auto" role="img" aria-label="Pearson's square for blending two beers to a target ABV">
<rect x="0" y="0" width="560" height="300" fill="#fdfbf7"/>
<text x="280" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Pearson's square — blend to a target</text>
<rect x="170" y="60" width="220" height="180" fill="none" stroke="#b45309" stroke-width="1.5"/>
<line x1="170" y1="60" x2="390" y2="240" stroke="#e0d8cc" stroke-width="1.5"/>
<line x1="170" y1="240" x2="390" y2="60" stroke="#e0d8cc" stroke-width="1.5"/>
<rect x="232" y="128" width="96" height="44" rx="6" fill="#b45309"/>
<text x="280" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#fdfbf7">TARGET</text>
<text x="280" y="164" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#fdfbf7">5.0%</text>
<text x="178" y="84" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">A: 6.5%</text>
<text x="178" y="232" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">B: 3.0%</text>
<text x="382" y="84" text-anchor="end" font-family="sans-serif" font-size="13" fill="#7a1f3d">parts A = 5.0−3.0 = 2.0</text>
<text x="382" y="232" text-anchor="end" font-family="sans-serif" font-size="13" fill="#7a1f3d">parts B = 6.5−5.0 = 1.5</text>
<text x="280" y="278" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#1c1a17">Blend 2.0 : 1.5 (A : B) → 5.0% ✓</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Pearson's square (use case 18): each corner subtracts diagonally to give the blend ratio.</figcaption>
</figure>

**17. Priming sugar for bottle carbonation.** Hit a target CO₂ without bottle bombs.
Formulas: residual CO₂ (vols) = 3.0378 − 0.050062·T + 0.00026555·T² (T = highest temp the beer saw, °F); corn sugar (g) = (target vols − residual) × litres × 4.0.
Excel (max temp °F `B2`, target vols `B3`, litres `B4`): residual `B5` = `=3.0378-0.050062*B2+0.00026555*B2^2`; sugar = `=(B3-B5)*B4*4.0`.
Example: 68 °F, target 2.4 vols, 23 L → residual 0.86 → **≈ 141 g corn sugar**. (Table sugar: × 0.91.)

**18. Blend or dilute to a target.** Trim a high-gravity wort with water, or marry two beers to a number.
Dilution formula: water to add = volume × (current points − target points) ÷ target points.
Excel (volume `B2`, current points `B3`, target points `B4`): `=B2*(B3-B4)/B4`.
Example: 25 L at 1.060 (60 pts) down to 1.050 (50 pts) → add **5 L water**. For blending two finished beers to a target ABV, use Pearson's square above: parts = the diagonal differences.

**19. Calories per serving.** A label number marketing always asks for.
Formulas (per 12 oz / 355 mL): alcohol cal = 1881.22 × FG × (OG − FG) ÷ (1.775 − OG); carbohydrate cal = 3550 × FG × ((0.1808 × OG) + (0.8192 × FG) − 1.0004); total = sum.
Excel (OG `B2`, FG `B3`): alcohol `=1881.22*B3*(B2-B3)/(1.775-B2)`; carbs `=3550*B3*((0.1808*B2)+(0.8192*B3)-1.0004)`; scale by serving size from 355 mL.
Example: 1.050 → 1.011 → ≈ 102 (alcohol) + 64 (carbs) = **≈ 166 cal** per 12 oz.

## Costing

**20. Cost of goods per hectolitre and per pint.** Where recipe maths meets the P&L.
Formulas: COGS/hL = total batch cost ÷ batch volume (hL); cost/pint = COGS/hL × 0.00568 (a UK pint is 0.568 L; 1 hL = 100 L).
Excel (total batch cost `B2`, batch hL `B3`): COGS/hL `B4` = `=B2/B3`; cost/pint = `=B4*0.00568`.
Example: £450 batch, 10 hL → **£45/hL ≈ £0.26 per pint**. Build it up properly with the method in [cost of goods per hectolitre]({{ '/2025/cost-of-goods-per-hectoliter/' | relative_url }}).

## The bottom line

These 20 formulas cover the brew day end to end: recipe design, mash and water, boil and hops, fermentation, packaging and cost. None needs an add-in — paste them into one sheet, label your input cells, and you have a brewhouse calculator that shows its working and that you can audit line by line. Keep the inputs honest (weigh, measure, record) and the maths will be right every time; that discipline is also exactly what makes the jump [from brewer to data scientist]({{ '/2026/from-brewer-to-data-scientist/' | relative_url }}) a short one when you're ready for it.

## Frequently asked questions

**Can you calculate ABV in Excel?**
Yes. The standard formula is =(OG-FG)*131.25, where OG and FG are your original and final specific gravities. For higher-strength beers a more accurate version is =(76.08*(OG-FG)/(1.775-OG))*(FG/0.794). Both work in any version of Excel with no add-ins.

**What is the Excel formula for mash strike water temperature?**
Strike temp Tw = (0.2/R)(T2-T1)+T2, where R is the water-to-grain ratio in quarts per pound, T1 is grain temperature and T2 is your target mash temperature in °F. In Excel: =(0.2/B2)*(B4-B3)+B4 with R in B2, grain temp in B3 and target in B4. For metric (L/kg, °C) swap the 0.2 for 0.41.

**Do I need special brewing software to do these calculations?**
No. Every calculation here — gravity, efficiency, IBU, colour, pitching rate, carbonation, ABV — is just arithmetic that brewing software runs under the hood. A single Excel sheet with these formulas reproduces it, and because you can see every cell you understand and trust the result.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
