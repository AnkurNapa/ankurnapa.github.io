---
layout: post
title: "Predicting Stuck Fermentation Before It Happens"
image: /assets/og/predicting-stuck-fermentation-risk.png
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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Predicting Stuck Fermentation Before It Happens</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Most readings sit inside the normal band; the model flags the one that doesn&#39;t."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">ANOMALY DETECTION</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Predicting Stuck Fermentation Before It Happens</text><rect x="60" y="120" width="620" height="70" fill="#5b7a1f" opacity="0.12"/><line x1="60" y1="120" x2="680" y2="120" stroke="#5b7a1f" stroke-width="1" stroke-dasharray="4 3"/><line x1="60" y1="190" x2="680" y2="190" stroke="#5b7a1f" stroke-width="1" stroke-dasharray="4 3"/><circle cx="110" cy="150" r="5" fill="#6b6258"/><circle cx="160" cy="140" r="5" fill="#6b6258"/><circle cx="210" cy="165" r="5" fill="#6b6258"/><circle cx="265" cy="148" r="5" fill="#6b6258"/><circle cx="320" cy="158" r="5" fill="#6b6258"/><circle cx="380" cy="143" r="5" fill="#6b6258"/><circle cx="440" cy="168" r="5" fill="#6b6258"/><circle cx="500" cy="150" r="5" fill="#6b6258"/><circle cx="560" cy="160" r="5" fill="#6b6258"/><circle cx="620" cy="146" r="5" fill="#6b6258"/><circle cx="345" cy="92" r="7" fill="#7a1f3d"/><text x="345" y="80" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">anomaly</text><text x="668" y="138" text-anchor="end" font-family="sans-serif" font-size="11" fill="#5b7a1f">normal band</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Most readings sit inside the normal band; the model flags the one that doesn&#39;t.</figcaption>
</figure>

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
