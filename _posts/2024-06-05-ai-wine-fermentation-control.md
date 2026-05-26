---
layout: post
title: "AI for Wine Fermentation Control (and Stuck Ferments)"
image: /assets/og/ai-wine-fermentation-control.png
description: "How AI models wine fermentation kinetics and stuck-ferment risk from YAN, sugar, and temperature — to guide nutrient and temperature decisions for whites and reds, and manage MLF."
date: 2024-06-05
updated: 2024-06-05
tags: [winemaking, fermentation, process-optimization]
faq:
  - q: "Can AI predict a stuck fermentation before it happens?"
    a: "Often, yes — early in the ferment. A model watching the sugar-drop curve alongside YAN, temperature, and starting sugar can flag a high-risk tank while you can still intervene with nutrients or temperature."
  - q: "What is YAN and why does the model care?"
    a: "Yeast-assimilable nitrogen, usually targeted around 150-250 mg/L. Low YAN is a leading cause of sluggish and stuck ferments, so it is one of the strongest predictors in any model."
  - q: "Does this work for wild or native ferments?"
    a: "Less well. Native ferments are driven by a shifting mix of wild yeasts, so they are far harder to model than a clean inoculation with a known Saccharomyces strain."
---

**Short answer: AI can flag a stuck or sluggish ferment early and recommend a nutrient or temperature correction — but only if your tank is actually instrumented and your ferment is a clean, inoculated one.** Fermentation is where chemistry turns into wine, and a stuck tank is one of the most expensive things that can go wrong.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the wine production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">AI for Wine Fermentation Control (and Stuck Ferments)</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Harvest</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Crush / press</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Age</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Bottle</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the wine production flow, start to finish.</figcaption>
</figure>

## What a fermentation model is actually predicting
Most musts are inoculated with wine strains of *Saccharomyces cerevisiae*, and a healthy ferment follows a recognisable sugar-drop curve. The model's job is to predict two things: the shape of that curve, and the risk that it stalls. Stuck and sluggish ferments come from a known short list of causes — low yeast-assimilable nitrogen (YAN, often targeted around 150-250 mg/L), high sugar and the osmotic stress it brings, temperature extremes, and ethanol toxicity as alcohol climbs. A model trained on past ferments learns how these factors combine and how the early curve betrays trouble before the tank visibly stalls.

It also has a role in malolactic fermentation (MLF), where *Oenococcus oeni* converts sharp malic acid into softer lactic acid and can throw buttery diacetyl. Predicting whether and how fast MLF will run helps you plan the cellar calendar.

## Measure first: the data the model needs
The inputs are the levers a winemaker already pulls. Starting sugar (°Brix), YAN, fermentation temperature, and the time-series of the sugar drop are the core. Temperature is not a single number but a control decision: whites ferment cooler, roughly 12-18 °C to preserve aromatics, while reds run warmer, around 25-30 °C to aid colour and tannin extraction. The model learns how the same nutrient or temperature move plays out differently across those regimes.

The catch is sensors. A model that watches a ferment in real time needs the data to exist — temperature probes and, ideally, density or sugar tracking on each tank. Many cellars measure once or twice a day by hand, which is enough to spot a stall but thin for a kinetic model. The honest starting point is more frequent, consistent logging on your problem tanks first.

## Where it breaks
Stuck ferments are, thankfully, rare — which is exactly why they are hard to model. The events you most want to predict are the ones you have the fewest examples of, so a model can be confidently wrong on the unusual tank. Native or wild ferments compound this: with a shifting community of wild yeasts rather than a single known strain, the kinetics are genuinely less predictable, and a model trained on clean inoculations will not transfer cleanly. And no model rescues a tank you are not measuring. The realistic posture is to use AI as an early-warning system on instrumented, inoculated ferments, and to keep the rescue protocols — rehydrated yeast, nutrient additions, temperature correction — firmly in human hands.

## How generative AI fits in
The most useful generative angle is a cellar copilot that explains a sluggish ferment in words and proposes a rescue. Rather than a winemaker squinting at a flattening curve at 11 p.m., the copilot reads the tank's data and says: "Tank 12 sugar drop has slowed to under 0.5 °Brix/day at 32 g/L residual sugar; YAN came in low at 110 mg/L and temperature has drifted to 31 °C. Likely nitrogen-limited with thermal stress. Consider a staggered nutrient addition and dropping temperature toward 26 °C; re-check density in 12 hours." It states the reasoning, not just an alert, and can draft the cellar note so the intervention is on record. Synthetic data also has a quiet role here — because real stuck ferments are scarce, simulated stress scenarios can help a model learn the warning signs it would otherwise rarely see, provided you validate against real tanks.

## The bottom line
A fermentation model's real value is catching a stuck or sluggish tank early enough to fix it — when nutrient or temperature corrections still work. That payoff is real for clean, instrumented ferments and weak for sparsely measured or native ones. Instrument your problem tanks, model the early curve, and let a copilot turn the data into a decision the winemaker can act on tonight.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [AI for wine blending optimisation]({{ '/2024/ai-wine-blending-optimization/' | relative_url }}).

## Frequently asked questions

**Can AI predict a stuck fermentation before it happens?**
Often, yes — early in the ferment. A model watching the sugar-drop curve alongside YAN, temperature, and starting sugar can flag a high-risk tank while you can still intervene with nutrients or temperature.

**What is YAN and why does the model care?**
Yeast-assimilable nitrogen, usually targeted around 150-250 mg/L. Low YAN is a leading cause of sluggish and stuck ferments, so it is one of the strongest predictors in any model.

**Does this work for wild or native ferments?**
Less well. Native ferments are driven by a shifting mix of wild yeasts, so they are far harder to model than a clean inoculation with a known Saccharomyces strain.
