---
layout: post
title: "From Pilot to Full Scale: The NPD Data Problem Nobody Warns You About"
image: /assets/og/npd-scale-up-pilot-to-production-data.png
description: "A beer that's perfect on the pilot kettle can drift off-spec at full scale. Here's how I used batch data, control charts and AI to close the scale-up gap when developing beers for AB InBev, SABMiller and United Breweries."
date: 2026-05-29
updated: 2026-05-29
tags: [beer-npd, brewing-science, scale-up, data-science]
faq:
  - q: "Why does a beer taste different at full scale than on the pilot?"
    a: "Larger vessels change the physics: hop utilisation, boil vigour, and especially fermentation in tall cylindroconical tanks — temperature gradients, hydrostatic pressure and CO2 scrubbing all shift the ester and attenuation profile away from the pilot result."
  - q: "Can AI predict how a pilot beer will behave at production scale?"
    a: "Partly. A model trained on past scale-ups can predict the likely direction and size of the shift for familiar styles on familiar plant, so you adjust the recipe before the first full batch. It is far less reliable for a new style or a vessel it has no history on."
  - q: "How many batches does it take to stabilise a new beer in production?"
    a: "It varies, but the first few full-scale batches almost always drift; statistical process control on each batch is how you converge. Data shortens that learning curve — it does not remove it."
---

**Short answer: the cruellest surprise in new product development is that a beer perfected on the pilot kettle can come out wrong at full scale. The physics of a big vessel isn't the physics of a small one. Batch data, control charts and AI helped me predict the scale-up shift and converge faster across the first production runs — but the first few batches still drift, and data shortens that curve rather than erasing it.** Here's the part of NPD nobody warns you about.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 820 340" width="100%" style="max-width:820px;height:auto" role="img" aria-label="A control chart showing the pilot batch on target, the first full-scale batches drifting outside the spec band, then converging back inside it as the process is corrected over successive batches."><rect x="0" y="0" width="820" height="340" fill="#fdfbf7"/><text x="410" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">THE SCALE-UP GAP</text><rect x="90" y="120" width="680" height="80" fill="#f7ece0" opacity="0.6"/><line x1="90" y1="160" x2="770" y2="160" stroke="#6b6258" stroke-width="1.4" stroke-dasharray="5 4"/><text x="96" y="114" font-family="sans-serif" font-size="11.5" fill="#6b6258">upper spec</text><text x="96" y="214" font-family="sans-serif" font-size="11.5" fill="#6b6258">lower spec</text><text x="778" y="164" font-family="sans-serif" font-size="11" fill="#6b6258">target</text><g stroke="#1c1a17" stroke-width="1.4"><line x1="90" y1="60" x2="90" y2="270"/><line x1="90" y1="270" x2="780" y2="270"/></g><polyline points="130,160 220,96 310,92 400,128 490,150 580,156 670,159 740,160" fill="none" stroke="#7a1f3d" stroke-width="2.6"/><g fill="#7a1f3d"><circle cx="130" cy="160" r="5"/><circle cx="220" cy="96" r="5"/><circle cx="310" cy="92" r="5"/><circle cx="400" cy="128" r="5"/><circle cx="490" cy="150" r="5"/><circle cx="580" cy="156" r="5"/><circle cx="670" cy="159" r="5"/><circle cx="740" cy="160" r="5"/></g><text x="130" y="295" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#6b6258">pilot</text><text x="265" y="295" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#7a1f3d">first full batches drift</text><text x="660" y="295" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#b45309">corrected &amp; stable</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Pilot on target; the first full-scale batches drift outside spec, then converge as the process is corrected batch by batch.</figcaption>
</figure>

## A bigger kettle is a different beer

You sign off the pilot, everyone's happy, and then the first full-scale brew lands a shade darker, a touch more bitter, and with an ester profile the panel doesn't recognise. Nothing was done wrong. The plant is simply a different physical system, and [scaling a recipe up]({{ '/2022/scaling-homebrew-recipe-to-production/' | relative_url }}) is where many promising beers quietly die.

The reasons are pure process engineering. Hop utilisation changes with kettle size and boil vigour, so the same hop bill gives a different IBU. Above all, fermentation in a tall cylindroconical tank is not fermentation in a pilot vessel: hydrostatic pressure, temperature gradients top to bottom, and CO₂ scrubbing all push the yeast toward a different ester and attenuation profile. The recipe is identical; the beer is not.

## Treating scale-up as a prediction problem

The old way was to brew the full batch and find out. Expensive, because at full scale a missed batch is thousands of litres. So I reframed it: scale-up is a prediction problem, and I had history to learn from — every previous transfer from pilot to plant, with the shift it produced.

A model trained on those past scale-ups could predict the *direction and rough size* of the gap for a familiar style on familiar vessels — this hop bill will gain a few IBU on this kettle, this fermentation will throw more ester in tank 4. That let me pre-adjust the recipe before the first production brew instead of after. It didn't make the gap vanish, but it stopped me starting from the wrong place.

Underneath it, as always, the work was data science: capturing the plant process variables consistently — knockout temperatures, tank geometry, real fermentation curves — and tying each production batch back to its pilot. Without that genealogy there is nothing to learn from.

## Converging batch by batch

Prediction gets you close; statistical process control gets you stable. Once a new beer was in production I tracked every critical parameter on [control charts]({{ '/2023/tableau-qc-control-charts-brewing/' | relative_url }}), batch over batch, watching for the drift that signals a process settling in. Pair that with [brewhouse yield analytics]({{ '/2023/brewhouse-yield-loss-analytics/' | relative_url }}) and you can see not just that a batch moved, but where the loss or shift came from.

Generative AI now sits naturally on top of this. When a batch trips a control limit, an LLM copilot can pull that batch's process record against the in-spec ones and draft a plain-language first hypothesis — "attenuation low, fermentation ran cooler in the lower third of the tank" — and auto-draft the deviation report and the updated scale-up SOP. It's a faster starting point for the brewer's investigation, not a verdict. The brewer still confirms the cause.

## Where it breaks

The model is only as good as the plant history behind it. A brand-new style, a vessel it has never seen, or a recipe outside the range of past transfers, and the scale-up prediction is a guess wearing a confidence interval. It predicts the familiar shift well and the unprecedented one poorly — and a first-of-its-kind beer is precisely the unprecedented case.

It also can't feel the intangibles. Mouthfeel, drinkability, that hard-to-name sense that the full-scale version has lost the charm of the pilot — none of that is on a control chart. The numbers can be back inside spec and the beer still not be the one you signed off. Closing that last gap is judgement, and it stayed [mine to make]({{ '/2026/from-brewer-to-data-scientist/' | relative_url }}).

## The bottom line

Scale-up is where new product development is won or lost, and it is relentlessly a data problem: predict the shift from past transfers, then converge with process control on the live batches. AI and analytics shortened that learning curve and saved full-scale brews I would otherwise have written off. But they shorten the curve; they don't remove it. The first batches still drift, and the decision that a scaled-up beer is finally *right* — not just in spec — is the brewer's, every time. That, across three posts, is how data crunched the numbers behind the beers I developed: it narrowed the field, sped the trials, and tamed the scale-up — while the judgement stayed human.

*Beer NPD with Data — Part 3 of 3. [Full series]({{ '/series/beer-npd/' | relative_url }}) · [Previous: recipe and sensory data]({{ '/2026/npd-recipe-sensory-data-development/' | relative_url }})*

## Frequently asked questions

**Why does a beer taste different at full scale than on the pilot?**
Larger vessels change the physics: hop utilisation, boil vigour, and especially fermentation in tall cylindroconical tanks — temperature gradients, hydrostatic pressure and CO₂ scrubbing all shift the ester and attenuation profile away from the pilot result.

**Can AI predict how a pilot beer will behave at production scale?**
Partly. A model trained on past scale-ups can predict the likely direction and size of the shift for familiar styles on familiar plant, so you adjust the recipe before the first full batch. It is far less reliable for a new style or a vessel it has no history on.

**How many batches does it take to stabilise a new beer in production?**
It varies, but the first few full-scale batches almost always drift; statistical process control on each batch is how you converge. Data shortens that learning curve — it does not remove it.
