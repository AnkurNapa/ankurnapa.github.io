---
layout: post
title: "Using AI to Optimise Adjunct and Cereal Costs"
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
