---
layout: post
title: "A Carbonation Calculator in Excel: Priming Sugar, PSI and Line Balancing"
image: /assets/og/carbonation-calculator-excel.png
description: "Carbonate beer with confidence in Excel: priming sugar from residual CO2, the keg pressure for any target volume and temperature, and a simple draught line-length balance."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
tags: [brewing-science, excel, carbonation, packaging]
faq:
  - q: "How do I calculate priming sugar in Excel?"
    a: "First the residual CO2 the beer already holds: =3.0378-0.050062*T+0.00026555*T^2 with T the warmest temperature it saw, in °F. Then corn sugar in grams =(target_volumes - residual)*litres*4.0. For table sugar multiply the result by 0.91."
  - q: "What pressure carbonates beer to a target volume?"
    a: "Set keg pressure (psi gauge) =(volumes+0.003342)/(0.01821+0.090115*EXP(-(T-32)/43.11))-14.695, where T is the serving temperature in °F. For 2.5 volumes at 38 °F that gives about 11 psi. Colder beer holds CO2 more easily, so it needs less pressure."
  - q: "How long should a draught beer line be?"
    a: "Balance the line so its resistance matches keg pressure: length in feet ≈ (keg_psi − rise×0.5 − 1) ÷ resistance, where 3/16-inch line is about 2.2 psi/ft and rise is the height to the tap. At 11 psi and 3 ft of rise that is roughly 4 ft of line for a clean, slow pour."
---

**Short answer: carbonation is three small formulas. Priming sugar = (target − residual CO2) × litres × 4.0 grams of corn sugar; keg pressure = (volumes + 0.003342) ÷ (0.01821 + 0.090115·e^(−(T−32)/43.11)) − 14.695 psi; and balanced line length ≈ (keg psi − rise − 1) ÷ 2.2 feet. Put them in Excel and you bottle and keg to a number instead of by feel.**

This is the deep dive on use case 17 from the [20 brewing calculations in Excel]({{ '/2026/advanced-brewing-calculations-excel/' | relative_url }}) pillar, covering both bottle priming and forced carbonation, plus the line balance that decides whether it actually pours well. It connects to the data side in [carbonation and dispense consistency]({{ '/2022/predicting-carbonation-dispense-consistency/' | relative_url }}).

## Priming sugar for bottles

Beer already holds some dissolved CO2, set by the warmest temperature it reached. That residual comes off your target first:

`residual =3.0378-0.050062*T+0.00026555*T^2`   (T in °F)
`corn_sugar_g =(target_vols-residual)*litres*4.0`

Example: beer that sat at 68 °F, target 2.4 volumes, 23 L → residual `0.86`, sugar `(2.4-0.86)*23*4.0 ≈ 141 g` of corn sugar. Priming with table sugar instead? Multiply by 0.91. The single biggest mistake here is forgetting the residual term and over-priming a warm-conditioned beer into gushers.

## Forced carbonation pressure

Kegging skips the sugar — you set a pressure and let the beer equilibrate. Solve the carbonation relationship for gauge pressure at your serving temperature:

`=(vols+0.003342)/(0.01821+0.090115*EXP(-(T-32)/43.11))-14.695`

Example: 2.5 volumes at 38 °F → about **11 psi**. The chart shows why you can't set one pressure and forget it: the colder the beer, the less pressure it takes to hold the same CO2.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 620 340" width="100%" style="max-width:620px;height:auto" role="img" aria-label="Forced carbonation chart: keg pressure rising with temperature for 2.0, 2.5 and 3.0 volumes of CO2">
<rect x="0" y="0" width="620" height="340" fill="#ffffff"/>
<text x="320" y="26" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#06483f">Keg pressure for a target carbonation</text>
<g stroke="#d8e6e1" stroke-width="1"><line x1="60" y1="170" x2="560" y2="170"/></g>
<g stroke="#06483f" stroke-width="1.5"><line x1="60" y1="40" x2="60" y2="300"/><line x1="60" y1="300" x2="560" y2="300"/></g>
<polyline points="60,255 310,224 560,189" fill="none" stroke="#06483f" stroke-width="3"/>
<polyline points="60,207 310,168 560,124" fill="none" stroke="#00695c" stroke-width="3"/>
<polyline points="60,159 310,112 560,60" fill="none" stroke="#06483f" stroke-width="3"/>
<g font-family="sans-serif" font-size="12" font-weight="700">
<text x="566" y="189" fill="#06483f">2.0 vol</text><text x="566" y="124" fill="#00695c">2.5 vol</text><text x="566" y="60" fill="#06483f">3.0 vol</text>
</g>
<g font-family="sans-serif" font-size="12" fill="#4a6b64" text-anchor="middle">
<text x="60" y="318">34 °F</text><text x="310" y="318">42 °F</text><text x="560" y="318">50 °F</text>
<text x="310" y="338">Serving temperature</text>
</g>
<g font-family="sans-serif" font-size="12" fill="#4a6b64" text-anchor="end">
<text x="52" y="44">26</text><text x="52" y="174">13</text><text x="52" y="304">0</text></g>
<text x="22" y="170" font-family="sans-serif" font-size="12" fill="#4a6b64" text-anchor="middle" transform="rotate(-90 22 170)">psi (gauge)</text>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Each line is a target volume; pressure rises with temperature. Set the pressure for your fridge temperature, not a generic number.</figcaption>
</figure>

## Line balancing

Set the right pressure and the pour can still foam if the line is too short to bleed it off. Balance the line so its resistance roughly equals keg pressure, allowing for the climb to the tap:

`length_ft =(keg_psi - rise_ft*0.5 - 1)/2.2`

(3/16-inch line is ~2.2 psi/ft; 1 psi is left for pour speed.) At 11 psi with a 3 ft rise: `(11 - 1.5 - 1)/2.2 ≈ 4 ft`. Too short and it foams; far too long and it pours slowly — the formula gets you to the right ballpark to trim from.

## Where it needs a sanity check

Two honest caveats. First, **residual CO2 assumes the beer fully equilibrated at that temperature** — a beer that spiked warm briefly, or one still off-gassing, won't match, so when in doubt prime to the lower end and let conditioning finish the job. Second, **line resistance is nominal** — real tubing varies by bore, brand and temperature, and the 2.2 psi/ft figure is a starting point, not gospel; expect to trim an inch or two after the first pours. The formulas remove the guesswork from the *target*; your senses still close the last few percent.

## The bottom line

Three formulas cover the whole carbonation question: how much sugar to prime, what pressure to set, and how long to cut the line. Build them once and you carbonate to a number — no more gushers, flat kegs, or all-foam pours that you can only diagnose after the fact.

## Frequently asked questions

**How do I calculate priming sugar in Excel?**
First the residual CO2 the beer already holds: =3.0378-0.050062*T+0.00026555*T^2 with T the warmest temperature it saw, in °F. Then corn sugar in grams =(target_volumes - residual)*litres*4.0. For table sugar multiply the result by 0.91.

**What pressure carbonates beer to a target volume?**
Set keg pressure (psi gauge) =(volumes+0.003342)/(0.01821+0.090115*EXP(-(T-32)/43.11))-14.695, where T is the serving temperature in °F. For 2.5 volumes at 38 °F that gives about 11 psi. Colder beer holds CO2 more easily, so it needs less pressure.

**How long should a draught beer line be?**
Balance the line so its resistance matches keg pressure: length in feet ≈ (keg_psi − rise×0.5 − 1) ÷ resistance, where 3/16-inch line is about 2.2 psi/ft and rise is the height to the tap. At 11 psi and 3 ft of rise that is roughly 4 ft of line for a clean, slow pour.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
