---
layout: post
title: "Detecting Wild Yeast and Bacterial Contamination Early With ML"
image: /assets/og/detecting-beer-contamination-early-ml.png
description: "Combine fermentation-signal ML with rapid micro methods like PCR and ATP-bioluminescence to flag Lacto, Pedio and wild-yeast contamination before it spoils a batch."
date: 2023-10-11
updated: 2023-10-11
tags: [brewing-science, quality-control, microbiology]
faq:
  - q: "Which organisms most often spoil beer?"
    a: "Common culprits are Lactobacillus, Pediococcus, Acetobacter, Pectinatus and Megasphaera, plus wild Saccharomyces and Brettanomyces. Pediococcus in particular raises diacetyl."
  - q: "Can ML detect contamination without a lab test?"
    a: "It can raise an early warning from process signals like unexpected attenuation and pH or diacetyl drift, but rapid micro methods such as PCR or ATP-bioluminescence, or selective media, still confirm what the organism is."
  - q: "Why are rare contamination events hard to model?"
    a: "Spoilage is infrequent in a well-run brewery, so you have few positive examples. Sparse data makes models prone to false alarms, which is why confirmation by a micro method matters."
---

**Short answer: ML on fermentation signals plus rapid micro methods can flag Lactobacillus, Pediococcus or wild-yeast contamination before it spoils a batch, but the lab still confirms the call.** Caught early, a contaminated batch is a decision; caught late, it is a write-off.

## What contamination looks like in the data
Spoilage organisms leave fingerprints in the process before they ruin the beer. Lactobacillus and Pediococcus drive unexpected acidification, so a pH falling faster or further than the recipe predicts is a signal. Pediococcus also produces diacetyl independently of normal yeast metabolism, so a diacetyl reading that climbs when it should fall is a warning a rest will not fix. Wild Saccharomyces and Brettanomyces show up as attenuation past the expected endpoint, the beer drying out further than the strain should manage. Acetobacter, Pectinatus and Megasphaera each shift the off-gas and chemistry in their own ways.

A model that watches gravity, pH, diacetyl and off-gas patterns against the expected trajectory for that recipe and yeast can flag deviations earlier than a person scanning logs. The point is not to identify the organism from process data alone, it is to raise a timely "this ferment is not behaving, look now".

## Pairing models with rapid micro methods
Measure first, and here that means the micro lab. Traditional detection uses selective media, membrane filtration and microscopy, which are reliable but slow, days of plate incubation. Rapid methods change the timing: PCR and ATP-bioluminescence return results far faster than plating, letting you confirm within a shift rather than after the batch is lost.

The strong design fuses both. The process-signal model triggers on a deviation and prompts a targeted rapid test, rather than testing everything on a fixed schedule. That focuses lab effort where the risk is, and it shortens the gap between "something is wrong" and "it is Pediococcus on tank four". A copilot ties it together: it reads the rapid micro result alongside the process data and issues a single early-warning alert with a recommended action, for example isolate the tank, escalate sampling, or stand down because the deviation was benign. That fusion is more useful than either signal alone, because process data gives speed and the micro method gives certainty.

## Where it breaks
The defining limit is rare-event data. In a clean brewery, contamination is infrequent, so you have very few positive examples to learn from. Models trained on imbalanced data over-trigger, and false alarms erode trust fast. Two mitigations help: weight the model towards catching true events even at the cost of some false positives, since a missed contamination is far more expensive than an extra test, and use synthetic data to fill the gap. Generating realistic synthetic contamination signatures, grounded in known organism behaviour, gives the model more varied positive examples to learn from than your handful of real incidents. Even so, the model only flags; rapid micro methods still confirm before you act on a batch.

## The bottom line
Early contamination detection is a fusion problem: process-signal ML for speed, rapid micro methods for certainty. Watch attenuation, pH and diacetyl against expectation, trigger targeted PCR or ATP tests on deviation, and let a copilot turn the two into one clear alert. Respect the rare-event limit, lean towards catching true events, and never skip lab confirmation.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Predicting microbiological and hygiene risk]({{ '/2024/predicting-microbiological-hygiene-risk/' | relative_url }})

## Frequently asked questions

**Which organisms most often spoil beer?**
Common culprits are Lactobacillus, Pediococcus, Acetobacter, Pectinatus and Megasphaera, plus wild Saccharomyces and Brettanomyces. Pediococcus in particular raises diacetyl.

**Can ML detect contamination without a lab test?**
It can raise an early warning from process signals like unexpected attenuation and pH or diacetyl drift, but rapid micro methods such as PCR or ATP-bioluminescence, or selective media, still confirm what the organism is.

**Why are rare contamination events hard to model?**
Spoilage is infrequent in a well-run brewery, so you have few positive examples. Sparse data makes models prone to false alarms, which is why confirmation by a micro method matters.
