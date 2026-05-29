---
layout: post
title: "Predicting Beer Flavour by Stacking Malt Flavour Wheels"
image: /assets/og/predicting-beer-flavour-malt-coa-flavour-wheels.png
description: "Give each malt its flavour wheel, scale it by its share of the grist, sum the wheels and ground the result in the COA. A weighted-sum fingerprint of beer flavour — and the perception physics it cannot fake."
date: 2026-05-29 09:00:00 -0700
updated: 2026-05-29
tags: [brewing-science, malting, flavour, data-science]
faq:
  - q: "Can you predict beer flavour from malt data alone?"
    a: "Partially. The malt-derived part of flavour — bready, biscuit, caramel, nutty, toffee, roast, coffee — can be approximated by taking each malt's flavour wheel, scaling it by that malt's share of the extract and summing the wheels into one fingerprint, anchored by the certificate of analysis. But hops, water, yeast and fermentation add and transform flavour the grist cannot predict, so malt data forecasts the malt character, not the whole beer."
  - q: "What is a malt flavour wheel?"
    a: "A malt flavour wheel, such as the ones Weyermann publishes, maps a malt's sensory character onto a set of descriptors — bready, honey, caramel, nutty, toffee, coffee, chocolate, roast — usually with an intensity for each. It turns a malt into a vector of flavour notes you can compare, blend and, with care, add together."
  - q: "Why isn't beer flavour just the sum of its malts?"
    a: "Because perception is non-linear. Notes mask each other, intensities saturate rather than add, and a small percentage of roast or crystal malt can dominate far beyond its weight. A weighted sum of flavour wheels is a useful first approximation, but it must be calibrated against a real tasting panel to correct for masking and saturation."
---

**Short answer: yes, for the malt half of the flavour — and only as a calibrated approximation. Give every malt its flavour wheel (Weyermann and others publish them), scale each wheel by that malt's share of the extract, lay the wheels on top of each other and sum them into a single fingerprint, then anchor the whole thing to the certificate of analysis. That predicts the malt-derived character of the beer — the bready, caramel, nutty, toffee, roast axis — surprisingly well. What it cannot do is add the hops, water, yeast and fermentation flavours that the grist knows nothing about, and it cannot be a naive sum: perception masks and saturates, so the stacked wheel must be calibrated against a real tasting panel before you trust it.**

It is a genuinely good idea, and an old brewer's instinct made explicit. A maltster looks at a grist — 80% pilsner, 15% Munich, 5% caramel — and already half-tastes the beer. The flavour wheel turns that instinct into arithmetic: each malt becomes a vector of notes with intensities, and a recipe becomes a weighted sum of those vectors. The trick is knowing exactly how far that arithmetic carries before the chemistry of the brewhouse takes over.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 290" width="100%" style="max-width:760px;height:auto" role="img" aria-label="A radar flavour wheel with two thin malt polygons and one bold predicted-beer polygon, beside a legend showing each malt scaled by its share of extract and summed">
<rect x="0" y="0" width="760" height="290" fill="#fdfbf7"/>
<text x="380" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Stack the malt wheels, weighted by extract share</text>
<!-- radar grid hexagon -->
<polygon points="210,55 292,103 292,197 210,245 128,197 128,103" fill="none" stroke="#d8cfc2" stroke-width="1"/>
<polygon points="210,103 251,127 251,174 210,197 169,174 169,127" fill="none" stroke="#e7dfd2" stroke-width="1"/>
<line x1="210" y1="150" x2="210" y2="55" stroke="#e7dfd2" stroke-width="1"/>
<line x1="210" y1="150" x2="292" y2="103" stroke="#e7dfd2" stroke-width="1"/>
<line x1="210" y1="150" x2="292" y2="197" stroke="#e7dfd2" stroke-width="1"/>
<line x1="210" y1="150" x2="210" y2="245" stroke="#e7dfd2" stroke-width="1"/>
<line x1="210" y1="150" x2="128" y2="197" stroke="#e7dfd2" stroke-width="1"/>
<line x1="210" y1="150" x2="128" y2="103" stroke="#e7dfd2" stroke-width="1"/>
<!-- axis labels -->
<text x="210" y="46" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">Bready</text>
<text x="300" y="100" text-anchor="start" font-family="sans-serif" font-size="10" fill="#6b6258">Caramel</text>
<text x="300" y="205" text-anchor="start" font-family="sans-serif" font-size="10" fill="#6b6258">Roast</text>
<text x="210" y="262" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">Nutty</text>
<text x="120" y="205" text-anchor="end" font-family="sans-serif" font-size="10" fill="#6b6258">Honey</text>
<text x="120" y="100" text-anchor="end" font-family="sans-serif" font-size="10" fill="#6b6258">Fruity</text>
<!-- malt A: pilsner (amber, thin) -->
<polygon points="210,65 226,141 214,152 210,174 181,167 194,141" fill="none" stroke="#b45309" stroke-width="1.5"/>
<!-- malt B: caramel/munich (maroon, thin) -->
<polygon points="210,112 276,112 226,160 210,202 161,179 185,136" fill="none" stroke="#7a1f3d" stroke-width="1.5"/>
<!-- predicted beer (ink, bold) -->
<polygon points="210,84 255,124 222,157 210,188 173,171 189,138" fill="#1c1a17" fill-opacity="0.07" stroke="#1c1a17" stroke-width="2.5"/>
<!-- legend / arithmetic -->
<text x="440" y="70" font-family="sans-serif" font-size="12" font-weight="700" fill="#1c1a17">Recipe → fingerprint</text>
<line x1="440" y1="100" x2="470" y2="100" stroke="#b45309" stroke-width="2"/>
<text x="478" y="104" font-family="sans-serif" font-size="11" fill="#1c1a17">Pilsner · 80% extract</text>
<line x1="440" y1="124" x2="470" y2="124" stroke="#7a1f3d" stroke-width="2"/>
<text x="478" y="128" font-family="sans-serif" font-size="11" fill="#1c1a17">CaraMunich · 15%</text>
<text x="478" y="150" font-family="sans-serif" font-size="11" fill="#6b6258">( + 5% roast → roast spike )</text>
<line x1="440" y1="170" x2="470" y2="170" stroke="#1c1a17" stroke-width="2.5"/>
<text x="478" y="174" font-family="sans-serif" font-size="11" font-weight="700" fill="#1c1a17">Σ weighted = predicted malt character</text>
<text x="440" y="214" font-family="sans-serif" font-size="11" fill="#6b6258">Then anchor to the COA (colour, Kolbach,</text>
<text x="440" y="230" font-family="sans-serif" font-size="11" fill="#6b6258">FAN) and calibrate against your panel.</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Each malt is a polygon on the flavour wheel. Scale by share of extract, sum into the bold fingerprint, ground it in the certificate — then correct for masking and saturation with real tasting scores.</figcaption>
</figure>

## The malt as a vector, the recipe as a sum

A malt flavour wheel — the kind [Weyermann](https://www.weyermann.de) publishes for its range — is exactly the structure a model wants: a fixed set of descriptors (bready, honey, biscuit, caramel, toffee, nutty, coffee, chocolate, roast) with an intensity on each. That makes a malt a vector. A grist is then a weighted combination of those vectors, and the natural first model is a linear one: multiply each malt's wheel by its **share of the extract** — not its mass, since a high-extract base malt and a low-yield roast malt contribute sugar, and therefore flavour, unequally per kilogram — and add the wheels together. Lay the polygons on top of each other and the summed outline is your predicted malt fingerprint. It is honest, transparent and computable in a spreadsheet before any machine learning is involved.

## Why the COA has to anchor it

A flavour wheel is a description of a malt *type*; the [certificate of analysis](/2026/genai-copilot-malt-certificate-analysis/) describes the *lot in front of you*, and the two must be combined. Colour (EBC) scales the roast and caramel axes — a darker-than-spec crystal lot pushes toffee toward burnt. The Kolbach index and free amino nitrogen shape the bready and worty notes and feed the [fermentation that yeast will later transform](/2026/ai-optimised-kilning-malt/). Kilning intensity moves a malt along its own wheel from bready toward biscuit and nutty. So the pipeline is: start from the published wheel for each malt, *correct* each vector using that lot's COA, then weight and sum. Without the COA the model predicts the recipe's intention; with it, the model predicts the batch.

## Where perception breaks the arithmetic

Be blunt about the ceiling, because this is where a naive sum misleads. **Flavour perception is non-linear.** Notes mask one another — roast and coffee will bury a delicate honey note that the arithmetic still shows at full height. Intensities saturate rather than add — two caramel malts do not give twice the caramel, they give a plateau. And small fractions dominate: 3% of a dark roast or a sharp crystal can define the beer far beyond its 3% weight, exactly the opposite of what a linear sum predicts. This is why the stacked wheel cannot stay linear. The fix is to train the weighting on outcomes: collect your own brews, each with its grist, its malt COAs and a **tasting-panel score** on the same descriptors, and fit a model that learns the masking and saturation corrections — a non-linear regression that maps the stacked-wheel input to the panel-measured output. The wheel-sum is the feature; the panel is the truth.

## What the grist simply cannot know

The larger honesty: malt predicts the malt half of the beer and no more. Hops bring bitterness, aroma and whole flavour dimensions the grist has no axis for. Water chemistry shifts perceived bitterness and roast harshness. And **yeast and fermentation are flavour factories** — esters, phenols, sulphur, the dryness of attenuation — that can swamp the malt fingerprint entirely in a Hefeweizen or a Brett beer, and barely touch it in a clean lager. A malt-only model is therefore a module, not the whole engine: it forecasts the malt-derived character accurately and should be combined with hop and fermentation models for the finished beer. It is also, like every malt prediction, only as good as the lot average — a COA [can hide a badly modified fraction](/2026/predicting-malt-modification-germination/) that the wheel never sees.

## The bottom line

Stacking malt flavour wheels, weighted by extract share and anchored to the certificate of analysis, is a real and useful way to predict the malt-derived flavour of a beer — and a lovely one, because it makes the maltster's instinct explicit and auditable. Build it in two layers: a transparent linear sum of the wheels as the baseline anyone can read, then a calibration model trained on your own tasting-panel scores to correct for the masking and saturation that perception insists on. Keep it modest about scope — it predicts the grain, not the hops, water or yeast — and it becomes a genuinely good recipe-design and quality tool. Treat it as the whole beer and it will confidently mis-taste your most interesting batches.

## Frequently asked questions

**Can you predict beer flavour from malt data alone?**
Partially. The malt-derived part of flavour — bready, biscuit, caramel, nutty, toffee, roast, coffee — can be approximated by taking each malt's flavour wheel, scaling it by that malt's share of the extract and summing the wheels into one fingerprint, anchored by the certificate of analysis. But hops, water, yeast and fermentation add and transform flavour the grist cannot predict, so malt data forecasts the malt character, not the whole beer.

**What is a malt flavour wheel?**
A malt flavour wheel, such as the ones Weyermann publishes, maps a malt's sensory character onto a set of descriptors — bready, honey, caramel, nutty, toffee, coffee, chocolate, roast — usually with an intensity for each. It turns a malt into a vector of flavour notes you can compare, blend and, with care, add together.

**Why isn't beer flavour just the sum of its malts?**
Because perception is non-linear. Notes mask each other, intensities saturate rather than add, and a small percentage of roast or crystal malt can dominate far beyond its weight. A weighted sum of flavour wheels is a useful first approximation, but it must be calibrated against a real tasting panel to correct for masking and saturation.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
