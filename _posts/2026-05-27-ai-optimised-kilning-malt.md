---
layout: post
title: "AI-Optimised Kilning: Hitting Colour and Diastatic Power While Cutting Gas"
image: /assets/og/ai-optimised-kilning-malt.png
description: "Kilning is malting's biggest energy cost and a hard trade-off between enzyme survival, colour and gas use. How machine learning optimises the kiln curve — and the physics it cannot cheat."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
tags: [brewing-science, malting, kilning, energy]
faq:
  - q: "What happens during kilning?"
    a: "Kilning dries green malt from around 45% moisture down to 4–5%, first in a free-drying phase at lower temperature, then a higher-temperature cure that develops colour and flavour and arrests modification. Pale malts are kilned gently to preserve enzymes; darker malts are cured hotter to build melanoidins."
  - q: "Why is enzyme survival a trade-off with colour?"
    a: "Heat combined with moisture destroys the amylase enzymes that give diastatic power, while colour forms through Maillard reactions that need heat, moisture and time. So you must drive moisture down before applying high heat, and any schedule that develops more colour generally costs some enzyme activity."
  - q: "Can AI cut malting kiln energy?"
    a: "Yes, modestly. A model can optimise the temperature and airflow ramp to hit target colour and diastatic power at the lowest specific energy in kWh per tonne, and schedule heat recovery. But it cannot break the physics: evaporating water off grain has a fixed latent-heat cost that no controller removes."
---

**Short answer: yes — within physics. Kilning is the single biggest energy line in malting and a genuine three-way trade-off between drying the grain, keeping its enzymes alive and developing colour. A model trained on your kiln runs can shape the temperature and airflow ramp to hit target colour (EBC) and diastatic power at the lowest specific energy, and squeeze more out of heat recovery. What it cannot do is dry grain for free or develop pale colour and high enzyme activity beyond what the chemistry allows.**

Once the floor hands over green malt at ~45% moisture, kilning does three jobs at once: it dries the grain to a stable 4–5%, it arrests modification, and it builds the colour and flavour that define the malt. Those jobs pull against each other, and they burn a great deal of gas — which is why this is where an optimiser earns real money.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 250" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Kiln schedule showing air-on temperature rising while bed moisture falls, with enzyme-safe and colour-development zones">
<rect x="0" y="0" width="760" height="250" fill="#fdfbf7"/>
<text x="380" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Kiln curve — dry first, then cure</text>
<line x1="60" y1="210" x2="710" y2="210" stroke="#6b6258" stroke-width="1.5"/>
<line x1="60" y1="50" x2="60" y2="210" stroke="#6b6258" stroke-width="1.5"/>
<polyline points="60,170 250,150 380,120 520,70 710,60" fill="none" stroke="#b45309" stroke-width="2.5"/>
<text x="600" y="52" font-family="sans-serif" font-size="11" font-weight="700" fill="#b45309">air-on temp</text>
<polyline points="60,70 250,95 380,140 520,185 710,195" fill="none" stroke="#1c1a17" stroke-width="2.5" stroke-dasharray="6 4"/>
<text x="120" y="64" font-family="sans-serif" font-size="11" font-weight="700" fill="#1c1a17">bed moisture</text>
<line x1="430" y1="50" x2="430" y2="210" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/>
<text x="430" y="228" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#6b6258">break point</text>
<text x="225" y="200" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#5b7a1f">free drying · enzymes safe</text>
<text x="575" y="172" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#7a1f3d">cure · colour develops</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Drive moisture down at low heat while the enzymes are still wet-vulnerable, then raise temperature for the cure once the bed is dry. The optimiser shapes both curves.</figcaption>
</figure>

## The kiln in three phases

A pale-malt kiln runs in stages. Free drying pulls bulk water off at a moderate air-on temperature with high airflow; the grain stays cool through evaporative cooling, so the enzymes survive. At the break point the bed is dry enough that further heating no longer cools it, and temperature can climb into the cure, where Maillard chemistry develops colour, melanoidins and flavour and the last moisture comes off. Pale lager malt is cured gently to protect diastatic power; Vienna, Munich and the crystal and roast malts are pushed hotter and wetter for colour. The art is the *shape* of the ramp, not any single set-point.

## The trade-off the model optimises

This is a constrained optimisation, and naming the constraint matters. **Enzymes (diastatic power) die under heat *plus* moisture**; **colour (Maillard) needs heat, moisture and time**. So the only route to a pale, high-DP malt is to remove moisture *before* the heat goes up — and even then more colour costs some enzyme. Frame the model's job precisely: find the temperature and airflow trajectory that lands target EBC colour and target diastatic power (°WK) while minimising specific energy in kWh per tonne, subject to a final moisture below ~5%. A model trained on your historical kiln runs — set-points, bed moisture, gas use, resulting malt analysis — learns this surface and proposes a curve, often trimming a few percent of gas by drying harder early (when airflow is cheap to use) and curing only as long as colour demands.

## Data, heat recovery and a generative layer

The honest enabler is instrumentation: air-on and air-off temperature, bed moisture or off-kiln humidity, airflow, and gas or electricity metered per batch. Measure first — an optimiser blind to bed moisture is dangerous. Heat recovery (glycol runaround, recirculation when humidity allows) is where much of the saving lives, and a model can schedule recirculation without over-wetting the bed. A generative-AI layer then makes it usable on shift: auto-drafting the energy-and-quality report after each kiln ("hit 4.2 EBC and 270 °WK at 11% below the standard recipe's gas; recovery contributed 18%"), and answering "which kiln schedules gave the lowest gas for pilsner malt last winter?" in plain language. It complements the [brewery energy and utilities optimisation]({{ '/2024/ai-brewery-energy-utilities-optimization/' | relative_url }}) work downstream.

## Where physics wins

Be blunt about the ceiling. Evaporating water carries a fixed latent heat (~2.3 MJ per kg) — no controller conjures that away, so most of the kiln's energy is simply non-negotiable and the optimiser fights only over the margin and the recovery. The enzyme–colour trade-off is chemistry, not a tuning oversight: a model cannot give you pale colour and untouched DP at once. Bed-moisture sensing is notoriously hard in a deep, shrinking grain bed, and a model trusting a bad reading can scorch a batch or leave it under-dried and unstable. And recovery from a kiln upset — a fan trip, a gas dip — is exactly the rare event the model has least data on. Keep target windows and a maltster's hand on the override.

## The bottom line

AI does not run the kiln; it shapes a smarter curve and books the heat-recovery savings, hitting your colour and diastatic-power targets with a few percent less gas. The trade-off between enzymes, colour and energy is physical and permanent — the model optimises inside it, not around it. Instrument the kiln properly, respect the latent-heat floor, and treat any unusually aggressive schedule with suspicion.

## Frequently asked questions

**What happens during kilning?**
Kilning dries green malt from around 45% moisture down to 4–5%, first in a free-drying phase at lower temperature, then a higher-temperature cure that develops colour and flavour and arrests modification. Pale malts are kilned gently to preserve enzymes; darker malts are cured hotter to build melanoidins.

**Why is enzyme survival a trade-off with colour?**
Heat combined with moisture destroys the amylase enzymes that give diastatic power, while colour forms through Maillard reactions that need heat, moisture and time. So you must drive moisture down before applying high heat, and any schedule that develops more colour generally costs some enzyme activity.

**Can AI cut malting kiln energy?**
Yes, modestly. A model can optimise the temperature and airflow ramp to hit target colour and diastatic power at the lowest specific energy in kWh per tonne, and schedule heat recovery. But it cannot break the physics: evaporating water off grain has a fixed latent-heat cost that no controller removes.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
