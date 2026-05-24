---
layout: post
title: "Predicting Stuck Fermentation Before It Happens"
description: "How machine learning predicts stuck fermentation risk from pitching rate, viability, wort oxygen and the early gravity curve — in time to act."
date: 2023-10-25
updated: 2023-10-25
tags: [brewing-science, fermentation, machine-learning]
faq:
  - q: "What are the earliest signs of a stuck fermentation?"
    a: "A gravity plateau that sits above your target and a slowing of CO2 evolution are the two clearest early signals. Both appear before the batch is obviously off, which is exactly when intervention still works."
  - q: "Can a model predict a stuck fermentation if it has never seen one?"
    a: "Not reliably. Stuck batches are rare, so they are under-represented in your data. A model trained mostly on healthy ferments will be confident and sometimes wrong on the bad ones — treat its risk score as an alert, not a verdict."
  - q: "What inputs matter most for predicting fermentation risk?"
    a: "Pitching rate and yeast viability/vitality, wort dissolved oxygen and FAN, original gravity, fermentation temperature, and the shape of the early gravity-drop curve. The curve shape often carries the most predictive signal."
---

**Short answer: yes — you can score the risk of a stuck or sluggish fermentation within the first day or two, while a rouse, re-pitch or warm-up can still save the batch.** The trick is feeding a model the right early signals rather than waiting for the gravity to flatline.

## What actually stalls a fermentation
Stuck and sluggish ferments rarely have one cause. The usual suspects are under-pitching, low yeast viability or vitality, insufficient wort oxygen (target 8-16 mg/L) or FAN (150-220 mg/L), a temperature that drops too far, premature flocculation, and high-gravity worts that stress the yeast. Most of these are knowable at or shortly after pitching.

The early warning signs are consistent: gravity plateaus above the target attenuation (most ales land around 75-85% apparent attenuation), and CO2 evolution slows sooner than expected. By the time a brewer notices on a twice-daily gravity sample, hours of head start are already gone.

## Measure first, then model
A useful risk model is mostly an exercise in disciplined measurement. Capture pitching rate (ale 0.5-1.5×10^7 cells/mL, lager 1.0-2.0×10^7), a viability and vitality reading on the pitched yeast, wort O2 and FAN, OG, and tank temperature. Then add the feature that does the heavy lifting: the early gravity-drop curve, ideally from an inline density or CO2 sensor rather than a manual reading.

The shape of that first 24-48 hours — how fast gravity falls and when the rate inflects — separates a healthy ferment from one heading for trouble far better than any single static input. A gradient-boosted model on these features will flag elevated risk early, and the value is in the lead time, not in decimal-place precision.

## Where this breaks
The honest limitation is structural: the bad batch you most want to predict is the one you have the fewest examples of. A brewery running well might log fifty clean ferments for every stuck one, so the model sees stuck fermentation as a rare event and tends to under-call it. This is the under-sampling problem, and no amount of clever tuning fully removes it.

It also depends on continuous data. A model fed two manual gravity points a day cannot resolve the curve shape that carries the signal — so the sensor investment usually matters more than the algorithm. And a risk score is a prompt to look, not a substitute for a brewer who knows the recipe and the yeast.

This is one place synthetic data earns its keep. Because stuck ferments are scarce, generating plausible synthetic examples of the rare failure modes — under-pitched high-gravity worts, low-O2 batches — can help a model learn the warning patterns without waiting years to accumulate real failures. Used carefully, it widens the training set for exactly the cases that hurt.

## A copilot for the rescue decision
The generative-AI angle is not the prediction; it is the explanation. When the risk score rises, an LLM copilot sitting on top of the model can name the likely drivers in plain language — "low pitching rate plus a 2 °C temperature drop overnight" — and suggest a proportionate response: rouse the yeast, raise the temperature, or re-pitch. That turns a number into a decision a duty brewer can act on at 6am without a data scientist in the room.

## The bottom line
Predicting stuck fermentation is realistic and worthwhile, but only with continuous early data and a clear head about its limits. Score the risk, let a copilot explain the drivers, and act while you still can — and never trust a confident model on the rare batch it has barely seen.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Can AI predict beer fermentation?]({{ '/2026/can-ai-predict-beer-fermentation/' | relative_url }})

## Frequently asked questions

**What are the earliest signs of a stuck fermentation?**
A gravity plateau that sits above your target and a slowing of CO2 evolution are the two clearest early signals. Both appear before the batch is obviously off, which is exactly when intervention still works.

**Can a model predict a stuck fermentation if it has never seen one?**
Not reliably. Stuck batches are rare, so they are under-represented in your data. A model trained mostly on healthy ferments will be confident and sometimes wrong on the bad ones — treat its risk score as an alert, not a verdict.

**What inputs matter most for predicting fermentation risk?**
Pitching rate and yeast viability/vitality, wort dissolved oxygen and FAN, original gravity, fermentation temperature, and the shape of the early gravity-drop curve. The curve shape often carries the most predictive signal.
