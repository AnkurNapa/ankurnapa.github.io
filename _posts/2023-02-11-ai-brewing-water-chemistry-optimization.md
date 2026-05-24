---
layout: post
title: "Optimising Brewing Water Chemistry With AI"
description: "AI as a salt and acid dosing adviser can hit target mash pH and sulphate-to-chloride balance across drifting source water and many recipes."
date: 2023-02-11
updated: 2023-02-11
tags: [brewing-science, water, process-optimization]
faq:
  - q: "What is the main target when adjusting brewing water?"
    a: "Mash pH in the 5.2 to 5.4 range, driven largely by the water's residual alkalinity, with the sulphate-to-chloride ratio set to tilt the beer toward hop-dry or malt-round character."
  - q: "Can't a brewer just use a spreadsheet for water adjustments?"
    a: "A spreadsheet works for a fixed recipe and stable water. AI earns its place when source water drifts seasonally, you run many recipes, or you blend supplies — situations where the right additions change batch to batch."
  - q: "Does water chemistry alone control mash pH?"
    a: "No. The grist buffers the mash too, so a dark, roasted grain bill pulls pH down on its own. A good adviser accounts for both the water ions and the malt, not the water in isolation."
---

**Short answer: AI is most valuable as a dosing adviser that recommends salt and acid additions to hit mash pH 5.2 to 5.4 and the sulphate-to-chloride balance you want — its payoff is operational, when water drifts and recipes multiply.** For a single recipe on stable water, a spreadsheet is fine. The case for AI is everything that breaks that simplicity.

## Water is a solution of ions, and each one has a job
Brewing water is not a backdrop; it is a reagent. Calcium lowers mash pH and supports enzyme activity, clarification and yeast flocculation. Bicarbonate and the alkalinity it represents resist that pH drop. Sulphate accentuates hop bitterness and dryness; chloride rounds the palate and favours malt. Magnesium and sodium play smaller supporting roles. The brewer's master target is mash pH between 5.2 and 5.4, governed largely by residual alkalinity, while the sulphate-to-chloride ratio is the dial that tilts a beer hop-dry or malt-round.

Because these ions interact — calcium and alkalinity fight over pH, sulphate and chloride trade off character — choosing additions is a small optimisation problem. An AI adviser frames it cleanly: given this source water, this grist and these style targets, what additions of gypsum, calcium chloride, and acid land you on spec with the least intervention?

## Why the operational case beats the textbook case
The textbook version of water treatment is solved with arithmetic. The real version is messy. Source water drifts seasonally as reservoir chemistry changes; a brewery running thirty recipes needs thirty different targets; and breweries that blend supplies or use reverse-osmosis-plus-build-up face a moving baseline every week. That combination — drift, variety and blending — is where a static spreadsheet quietly goes stale and a model that re-optimises per batch earns its keep.

This is also a data-discipline story. The adviser is only as good as your water analysis, and water analysis ages. A reading from last spring may not describe today's supply, so the measure-first discipline here means a sampling cadence that matches how fast your water actually moves. As with [collecting your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}), the unglamorous habit of regular, calibrated measurement is the whole foundation.

## Where it breaks
Two failure modes matter. The first is stale water analysis: feed the model a six-month-old ion report and it will confidently recommend additions for water you no longer have. The fix is operational, not algorithmic — measure more often, and let the model flag when its inputs are older than your drift rate. The second is forgetting the grist. Water chemistry does not set mash pH on its own; the malt buffers it too, and a heavily roasted grain bill drags pH down without any help from the water. An adviser that optimises ions in isolation will overshoot on dark beers. The model must take the grain bill as an input, not an afterthought, which ties water optimisation to [predicting mash efficiency and extract yield]({{ '/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}).

There is also a perceptual limit worth stating plainly: hitting a numerical sulphate-to-chloride ratio does not guarantee the sensory result a brewer imagines. The numbers narrow the search; the palate still decides.

## Asking your water a question in plain language
The generative-AI angle that fits here is a natural-language assistant over your water chemistry. Instead of toggling cells, a brewer asks: "What additions hit a Burton-style, hop-forward profile for this source water and this pale grist?" and gets a specific recommendation — grams of gypsum and calcium chloride, an acid dose to land in the 5.2 to 5.4 band, and a one-line explanation of the trade-off ("higher sulphate sharpens the bitterness; if it reads harsh, shift chloride up"). The value is not novelty; it is collapsing a fiddly calculation into a question an operator can ask mid-shift and a recommendation they can act on without misreading a spreadsheet under time pressure.

## The bottom line
Treat AI water optimisation as a per-batch dosing adviser, justified by operational reality rather than chemistry you could do by hand. Keep water analyses fresh, always feed the grist into the model, and let a plain-language assistant turn targets into specific additions. On stable water with one recipe, stick with the spreadsheet — the model is for the messy reality of many beers and shifting supply.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*

## Frequently asked questions

**What is the main target when adjusting brewing water?**
Mash pH in the 5.2 to 5.4 range, driven largely by the water's residual alkalinity, with the sulphate-to-chloride ratio set to tilt the beer toward hop-dry or malt-round character.

**Can't a brewer just use a spreadsheet for water adjustments?**
A spreadsheet works for a fixed recipe and stable water. AI earns its place when source water drifts seasonally, you run many recipes, or you blend supplies — situations where the right additions change batch to batch.

**Does water chemistry alone control mash pH?**
No. The grist buffers the mash too, so a dark, roasted grain bill pulls pH down on its own. A good adviser accounts for both the water ions and the malt, not the water in isolation.
