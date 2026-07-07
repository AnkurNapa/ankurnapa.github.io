---
layout: post
title: "Using AI to Optimise Adjunct and Cereal Costs"
image: /assets/og/ai-adjunct-cereal-cost-optimization.png
description: "How AI optimises the brewing grist bill across malt, adjuncts and syrups against cost, target extract and FAN constraints as commodity prices move."
date: 2023-03-25
updated: 2023-03-25
tags: [brewing-science, raw-materials, cost]
faq:
  - q: "Can AI lower my grist cost without changing the beer?"
    a: "Often, yes — within limits. An optimiser can reshuffle the malt-to-adjunct ratio to hold target original gravity while cutting cost, but flavour, colour and FAN constraints cap how far it can go before the beer changes."
  - q: "Why does too much adjunct cause fermentation problems?"
    a: "Nitrogen-free adjuncts such as maize, rice and syrups dilute the wort's free amino nitrogen (FAN). Low FAN stresses the yeast, which can raise higher alcohols and diacetyl and slow or stall fermentation."
  - q: "Do I need a data scientist to run grist optimisation?"
    a: "Not to use it. The modelling and constraints sit behind a natural-language or spreadsheet front end. You do need clean malt-analysis and cost data, which is the harder part."
---

**Short answer: AI can trim your grist cost by a few percent without touching the beer — but quality constraints, not the maths, set the ceiling.** The grist bill is one of the largest controllable input costs in brewing, and commodity prices for malt, maize, rice and syrups move constantly. An optimiser keeps your recipe at least-cost while respecting the constraints that actually matter.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Using AI to Optimise Adjunct and Cereal Costs</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## The grist bill is a constrained optimisation problem
Choosing how much malt, adjunct and syrup to blend is a textbook optimisation: minimise cost subject to constraints. The constraints are familiar to any brewer. You need to hit a target original gravity, which means recovering enough hot-water extract from the grist. You need to stay within a colour band and a flavour profile. And — the one that bites — you need to keep free amino nitrogen (FAN) above a floor your yeast can work with.

Adjuncts and processed cereals such as maize, rice, wheat and syrups supplement malt to cut cost or to adjust flavour and colour. The catch is that nitrogen-free adjuncts dilute wort FAN. Push them too far and you starve the yeast: low nitrogen raises higher alcohols and diacetyl and risks a poor or stuck fermentation. So the genuine trade-off is cost versus quality, and the model has to encode that honestly rather than chase the cheapest number.

## Measure first, then optimise
The optimisation is only as good as the data feeding it. This is where the data-science discipline matters more than the algorithm. Each malt and adjunct carries an analysis — extract potential, protein, colour — and each carries a moving price. You need those numbers reliable and current, ideally pulled from supplier certificates of analysis and your purchasing system rather than typed once and forgotten.

The features that drive the model are straightforward: extract contribution per ingredient, FAN contribution, colour units, and delivered cost per tonne. A machine-learning model can also learn from your own brews how predicted FAN translates into actual fermentation performance on your kit, which is more useful than a generic table. Measure first: a clean dataset of what you bought, what it analysed at, and how it fermented is worth more than a clever solver.

## Where it breaks
The model optimises the recipe, not your brewhouse. It assumes you will recover the extract it predicts; if your milling or lauter performance drifts, the real OG will miss regardless of how elegant the grist is. It also assumes your analysis data is honest — a syrup mislabelled or a malt lot that under-delivers on extract will quietly break the plan.

And the FAN constraint is a floor, not a target you can shave to the millimetre. Yeast health, pitching rate and aeration all interact with available nitrogen, so a model that treats FAN as a single hard number will occasionally be optimistic. Treat the optimiser's output as a strong starting recipe to validate on a pilot batch, not as gospel — especially when you swap to a cheaper adjunct you have not run before.

## A generative layer for scenarios
The most practical generative-AI angle here is a natural-language scenario tool. A brewer types "give me the cheapest grist that hits 12.5 °P and keeps FAN above 180 mg/L" and the system returns a costed recipe with the binding constraints called out. When maize jumps 15% or barley malt eases, an LLM can summarise the impact across your active recipes in plain language — "switching 5% of the grist from maize to rice saves £X per brew but pushes FAN within 8 mg/L of your floor" — so the decision sits with the brewer, not buried in a solver.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Start to finish, broken into the pieces that move the number."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">BRIDGE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Using AI to Optimise Adjunct and Cereal Costs</text><line x1="60" y1="250" x2="680" y2="250" stroke="#06483f" stroke-width="1.5"/><rect x="90" y="100" width="80" height="150" fill="#00695c"/><text x="130" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">Start</text><rect x="230" y="140" width="80" height="40" fill="#06483f"/><text x="270" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">−40</text><rect x="350" y="170" width="80" height="30" fill="#06483f"/><text x="390" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">−30</text><rect x="470" y="130" width="80" height="40" fill="#2e9e7c"/><text x="510" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">+40</text><rect x="590" y="130" width="80" height="120" fill="#00695c"/><text x="630" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">End</text><line x1="170" y1="100" x2="230" y2="100" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="310" y1="140" x2="350" y2="140" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="430" y1="170" x2="470" y2="170" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="550" y1="130" x2="590" y2="130" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Start to finish, broken into the pieces that move the number.</figcaption>
</figure>

## The bottom line
AI grist optimisation is a sober cost lever, not a magic one. It earns its keep when commodity prices swing and you have many recipes to re-cost, and it stays safe only if quality constraints — FAN above all — are built in and validated on real brews. Start by getting your malt-analysis and cost data clean; the optimisation is the easy half.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Collect your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}).

## Frequently asked questions

**Can AI lower my grist cost without changing the beer?**
Often, yes — within limits. An optimiser can reshuffle the malt-to-adjunct ratio to hold target original gravity while cutting cost, but flavour, colour and FAN constraints cap how far it can go before the beer changes.

**Why does too much adjunct cause fermentation problems?**
Nitrogen-free adjuncts such as maize, rice and syrups dilute the wort's free amino nitrogen (FAN). Low FAN stresses the yeast, which can raise higher alcohols and diacetyl and slow or stall fermentation.

**Do I need a data scientist to run grist optimisation?**
Not to use it. The modelling and constraints sit behind a natural-language or spreadsheet front end. You do need clean malt-analysis and cost data, which is the harder part.
