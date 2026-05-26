---
layout: post
title: "Predicting Beer Colour (EBC/SRM) From a Recipe"
image: /assets/og/predicting-beer-colour-recipe.png
description: "How AI predicts finished beer colour in EBC/SRM from malt colours and grist proportions, where it beats Morey's equation, and where it breaks."
date: 2021-04-14
updated: 2021-04-14
tags: [brewing-science, recipe, machine-learning]
faq:
  - q: "Can you predict beer colour before you brew?"
    a: "Yes, reasonably well. A recipe gives you each malt's colour and proportion, and models from Morey's equation to per-brewhouse ML can estimate finished EBC/SRM within a few units before the kettle is even lit."
  - q: "Why is my measured colour darker than the calculator predicts?"
    a: "Kettle caramelisation and Maillard reactions during a long, vigorous boil add colour that simple linear formulas ignore. Boil intensity, gravity, and pH all push the measured value past the recipe estimate."
  - q: "Does darker beer mean more flavour?"
    a: "No. Colour and flavour are correlated through malt choice but not identical. A model that nails EBC tells you nothing about bitterness, body, or off-flavours, so colour is a starting point, not a verdict."
---

**Short answer: yes, you can predict finished beer colour from a recipe surprisingly well, and per-brewhouse machine learning beats the textbook equations.** Colour is one of the most measurable things in brewing, which makes it an ideal first target for a data-driven approach.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Predicting Beer Colour (EBC/SRM) From a Recipe</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## What actually drives the colour in the glass
Beer colour is measured in EBC (Europe) or SRM (US), and it is driven mainly by the malt: the Lovibond or EBC rating of each grain, the proportion of each in the grist, and the colour developed through Maillard and caramelisation reactions during the boil. A pale pilsner malt at a high proportion keeps things straw-coloured; a few percent of roasted or crystal malt swings the result dramatically because dark malts are nonlinear contributors.

The classic starting point is Morey's equation, which estimates SRM from the malt colour units per unit volume using a power-law fit. It is fast, transparent, and good enough for homebrew planning. But it was fitted to a generic dataset, not to your kettle, your water, or your boil regime, so it systematically misses for any specific brewhouse.

## Measure first, then let the model learn your kettle
The honest way to improve on Morey is to measure first. Log the recipe inputs (each malt's colour and weight, mash and boil parameters) against the measured EBC/SRM of the finished beer for every batch you can. Once you have a few dozen paired observations, even a modest regression model learns the systematic offset that your process introduces.

This is where machine learning earns its place. A gradient-boosted model or a small neural network can capture the nonlinear contribution of dark malts and the interaction between boil length and gravity far better than a single power law. The model is not magic; it is simply fitted to *your* data instead of a generic average, so it corrects for the consistent bias your equipment introduces. In practice a per-brewhouse model often halves the prediction error of a generic formula, turning a "roughly right" estimate into something you can plan a grist around.

The data-science discipline matters more than the algorithm. Clean colour readings from a calibrated spectrophotometer, consistent sampling, and honest logging of process deviations beat any clever model trained on sloppy data.

## A generative-AI copilot for hitting a target colour
The interesting near-term application is generative, not just predictive. Instead of asking "what colour will this grist give me?", you ask the inverse: "I want 25 EBC for a Vienna lager, suggest grist tweaks." A copilot built on top of your fitted colour model can search the recipe space, propose two or three grist adjustments that land on target, and explain the trade-offs (more crystal malt for colour versus the sweetness it adds). It turns the model into a design assistant a brewer can actually converse with, while the brewer keeps final judgement.

## Where it breaks
Colour prediction is one of the friendlier problems in brewing, but it has hard limits. Kettle caramelisation depends on boil vigour, surface area, and gravity in ways that vary batch to batch, so process variation puts a floor on accuracy. Water chemistry and mash pH shift extraction and the final hue. Malt itself varies by harvest and maltster lot, so the colour rating on the bag is a nominal figure, not a guarantee.

Most importantly, colour is not flavour. A model can hit your target EBC perfectly and tell you nothing about whether the beer tastes the way you intended. Treat colour prediction as a planning tool that saves trial batches, not as a quality verdict. The reference for "does it taste right" remains a calibrated sensory panel, not a number.

## The bottom line
Beer colour is predictable, and a per-brewhouse model trained on your own measured batches beats generic equations like Morey's by correcting for your kettle's systematic bias. Measure first, keep the data clean, and use a generative copilot to suggest grist tweaks toward a target. Just remember the model predicts a colour, not a beer.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Can AI design a beer recipe?]({{ '/2026/can-ai-design-a-beer-recipe/' | relative_url }})

## Frequently asked questions

**Can you predict beer colour before you brew?**
Yes, reasonably well. A recipe gives you each malt's colour and proportion, and models from Morey's equation to per-brewhouse ML can estimate finished EBC/SRM within a few units before the kettle is even lit.

**Why is my measured colour darker than the calculator predicts?**
Kettle caramelisation and Maillard reactions during a long, vigorous boil add colour that simple linear formulas ignore. Boil intensity, gravity, and pH all push the measured value past the recipe estimate.

**Does darker beer mean more flavour?**
No. Colour and flavour are correlated through malt choice but not identical. A model that nails EBC tells you nothing about bitterness, body, or off-flavours, so colour is a starting point, not a verdict.
