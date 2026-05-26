---
layout: post
title: "Build an IBU Recipe Builder in Excel (Tinseth, Multi-Addition)"
image: /assets/og/ibu-recipe-builder-excel.png
description: "A multi-addition IBU calculator in Excel: Tinseth utilisation per hop addition, total bitterness, the BU:GU balance ratio, hop substitution and scaling to a target IBU."
date: 2026-05-31 09:00:00 -0700
updated: 2026-05-31
tags: [brewing-science, excel, hops, recipe-formulation]
faq:
  - q: "How do I calculate total IBU for multiple hop additions in Excel?"
    a: "Give each addition a row with its grams, alpha acid %, and boil time, compute Tinseth IBU per row, then sum the rows. Per row: utilisation =(1.65*0.000125^(OG-1))*((1-EXP(-0.04*time))/4.15), and IBU =utilisation*((AA/100)*grams*1000)/litres. Total IBU is just =SUM() of the rows."
  - q: "What is the BU:GU ratio?"
    a: "BU:GU is total IBU divided by the original gravity points ((OG−1)×1000). It measures bitterness against malt sweetness, so it captures perceived balance better than IBU alone. Roughly: under 0.4 is malty, ~0.5 balanced, 0.7–0.8 hoppy, and 1.0+ is IPA territory. In Excel: =IBU/((OG-1)*1000)."
  - q: "How do I scale hops to hit a target IBU?"
    a: "Work out your recipe's calculated IBU, then multiply every hop weight by target ÷ calculated. If the sheet says 33 IBU and you want 40, scale by 40/33 = 1.21, so a 28 g addition becomes about 34 g. The ratios between additions stay the same, only the totals move."
---

**Short answer: an IBU builder is one Tinseth formula copied down a table of hop additions, summed. Each row computes utilisation from boil time and gravity, multiplies by the alpha-acid concentration, and totals to your bitterness; divide by gravity points for the BU:GU balance ratio, and multiply weights by target÷calculated to hit a number. All in plain Excel.**

This expands use cases 10 and 11 from the [20 brewing calculations in Excel]({{ '/2026/advanced-brewing-calculations-excel/' | relative_url }}) pillar from a single addition into a full recipe with bittering, flavour, aroma and whirlpool hops. It's the transparent version of what sits behind [predicting hop bitterness]({{ '/2023/predicting-hop-bitterness-ibu/' | relative_url }}).

## Step 1 — one row per addition

Lay out a table: grams, alpha-acid %, boil time. Put the batch volume (litres) and OG in fixed cells you can reference with `$`. The Tinseth IBU for each row is two factors — utilisation (how much isomerises, from time and gravity) and concentration (how much alpha acid you added):

`utilisation =(1.65*0.000125^($OG-1))*((1-EXP(-0.04*time))/4.15)`
`IBU =utilisation*((AA/100)*grams*1000)/$litres`

Copy it down every row. Then total: `=SUM(IBU_column)`.

Worked example, 23 L at OG 1.050:

| Addition | g | AA% | min | IBU |
|---|---|---|---|---|
| Bittering | 28 | 6.4 | 60 | 18.0 |
| Flavour | 28 | 6.4 | 15 | 8.9 |
| Whirlpool | 28 | 6.4 | 10* | 6.5 |
| **Total** | | | | **33.4** |

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 620 340" width="100%" style="max-width:620px;height:auto" role="img" aria-label="Bar chart of IBU contribution by hop addition: 60 minute addition dominates">
<rect x="0" y="0" width="620" height="340" fill="#fdfbf7"/>
<text x="320" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">IBU contribution by addition (same 28 g each)</text>
<g stroke="#1c1a17" stroke-width="1.5"><line x1="80" y1="40" x2="80" y2="300"/><line x1="80" y1="300" x2="560" y2="300"/></g>
<rect x="120" y="66" width="90" height="234" fill="#b45309"/>
<rect x="270" y="184.3" width="90" height="115.7" fill="#a9743a"/>
<rect x="420" y="215.5" width="90" height="84.5" fill="#8a5a2b"/>
<g font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17" text-anchor="middle">
<text x="165" y="58">18.0</text><text x="315" y="176">8.9</text><text x="465" y="207">6.5</text>
</g>
<g font-family="sans-serif" font-size="12.5" fill="#6b6258" text-anchor="middle">
<text x="165" y="318">60 min</text><text x="315" y="318">15 min</text><text x="465" y="318">whirlpool</text>
</g>
<text x="36" y="170" font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle" transform="rotate(-90 36 170)">IBU</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Identical weights, very different bitterness: the 60-minute addition does more than the other two combined. *Whirlpool modelled as a 10-minute equivalent — see the caveat.</figcaption>
</figure>

## Step 2 — the balance ratio and the target

IBU on its own doesn't tell you how a beer tastes — 40 IBU is aggressive in a 1.040 bitter and mild in a 1.080 double IPA. The BU:GU ratio fixes that by dividing bitterness by malt:

`=total_IBU/(($OG-1)*1000)`

Our example: `33.4/50 = 0.67` — a firmly hop-forward pale ale. Under 0.4 reads malty, ~0.5 balanced, 1.0+ is IPA territory.

To hit a target, scale: `scale_factor =target_IBU/calculated_IBU`, then multiply each weight by it. Want 40 from 33.4? `40/33.4 = 1.20`, so every addition grows 20% and the balance between them is preserved.

## Where the estimate is softest

Two honest limits. First, **whirlpool and hop-stand additions are the least predictable** — Tinseth was fit to rolling boils, so a sub-boiling whirlpool keeps isomerising but at a rate the formula doesn't model. Treating it as a short "equivalent boil time" (10 minutes here) is a usable fudge, not physics; if you stand hops hot for 30 minutes, real bitterness lands somewhere between zero and a 10-minute boil, and only tasting your own system calibrates it. Second, **dry hops contribute essentially no IBU** even though they smell intensely bitter — leave them at zero in the sheet and trust your nose, not the number. The total is a reliable *relative* guide and a good absolute one for boil additions; treat late and dry hops as aroma, costed separately.

## The bottom line

Copy one Tinseth formula down a table of additions, sum it, divide by gravity points, and you have a recipe-grade bitterness calculator with a balance ratio and a one-cell scaler. It nails boil additions; just keep an asterisk on whirlpool and dry hops, where the chemistry outruns the formula.

## Frequently asked questions

**How do I calculate total IBU for multiple hop additions in Excel?**
Give each addition a row with its grams, alpha acid %, and boil time, compute Tinseth IBU per row, then sum the rows. Per row: utilisation =(1.65*0.000125^(OG-1))*((1-EXP(-0.04*time))/4.15), and IBU =utilisation*((AA/100)*grams*1000)/litres. Total IBU is just =SUM() of the rows.

**What is the BU:GU ratio?**
BU:GU is total IBU divided by the original gravity points ((OG−1)×1000). It measures bitterness against malt sweetness, so it captures perceived balance better than IBU alone. Roughly: under 0.4 is malty, ~0.5 balanced, 0.7–0.8 hoppy, and 1.0+ is IPA territory. In Excel: =IBU/((OG-1)*1000).

**How do I scale hops to hit a target IBU?**
Work out your recipe's calculated IBU, then multiply every hop weight by target ÷ calculated. If the sheet says 33 IBU and you want 40, scale by 40/33 = 1.21, so a 28 g addition becomes about 34 g. The ratios between additions stay the same, only the totals move.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
