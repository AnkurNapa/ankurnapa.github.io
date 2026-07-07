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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Detecting Wild Yeast and Bacterial Contamination Early With ML</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## What contamination looks like in the data
Spoilage organisms leave fingerprints in the process before they ruin the beer. Lactobacillus and Pediococcus drive unexpected acidification, so a pH falling faster or further than the recipe predicts is a signal. Pediococcus also produces diacetyl independently of normal yeast metabolism, so a diacetyl reading that climbs when it should fall is a warning a rest will not fix. Wild Saccharomyces and Brettanomyces show up as attenuation past the expected endpoint, the beer drying out further than the strain should manage. Acetobacter, Pectinatus and Megasphaera each shift the off-gas and chemistry in their own ways.

A model that watches gravity, pH, diacetyl and off-gas patterns against the expected trajectory for that recipe and yeast can flag deviations earlier than a person scanning logs. The point is not to identify the organism from process data alone, it is to raise a timely "this ferment is not behaving, look now".

## Pairing models with rapid micro methods
Measure first, and here that means the micro lab. Traditional detection uses selective media, membrane filtration and microscopy, which are reliable but slow, days of plate incubation. Rapid methods change the timing: PCR and ATP-bioluminescence return results far faster than plating, letting you confirm within a shift rather than after the batch is lost.

The strong design fuses both. The process-signal model triggers on a deviation and prompts a targeted rapid test, rather than testing everything on a fixed schedule. That focuses lab effort where the risk is, and it shortens the gap between "something is wrong" and "it is Pediococcus on tank four". A copilot ties it together: it reads the rapid micro result alongside the process data and issues a single early-warning alert with a recommended action, for example isolate the tank, escalate sampling, or stand down because the deviation was benign. That fusion is more useful than either signal alone, because process data gives speed and the micro method gives certainty.

## Where it breaks
The defining limit is rare-event data. In a clean brewery, contamination is infrequent, so you have very few positive examples to learn from. Models trained on imbalanced data over-trigger, and false alarms erode trust fast. Two mitigations help: weight the model towards catching true events even at the cost of some false positives, since a missed contamination is far more expensive than an extra test, and use synthetic data to fill the gap. Generating realistic synthetic contamination signatures, grounded in known organism behaviour, gives the model more varied positive examples to learn from than your handful of real incidents. Even so, the model only flags; rapid micro methods still confirm before you act on a batch.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Most readings sit inside the normal band; the model flags the one that doesn&#39;t."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">ANOMALY DETECTION</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Detecting Wild Yeast and Bacterial Contamination Early With ML</text><rect x="60" y="120" width="620" height="70" fill="#2e9e7c" opacity="0.12"/><line x1="60" y1="120" x2="680" y2="120" stroke="#2e9e7c" stroke-width="1" stroke-dasharray="4 3"/><line x1="60" y1="190" x2="680" y2="190" stroke="#2e9e7c" stroke-width="1" stroke-dasharray="4 3"/><circle cx="110" cy="150" r="5" fill="#4a6b64"/><circle cx="160" cy="140" r="5" fill="#4a6b64"/><circle cx="210" cy="165" r="5" fill="#4a6b64"/><circle cx="265" cy="148" r="5" fill="#4a6b64"/><circle cx="320" cy="158" r="5" fill="#4a6b64"/><circle cx="380" cy="143" r="5" fill="#4a6b64"/><circle cx="440" cy="168" r="5" fill="#4a6b64"/><circle cx="500" cy="150" r="5" fill="#4a6b64"/><circle cx="560" cy="160" r="5" fill="#4a6b64"/><circle cx="620" cy="146" r="5" fill="#4a6b64"/><circle cx="345" cy="92" r="7" fill="#06483f"/><text x="345" y="80" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">anomaly</text><text x="668" y="138" text-anchor="end" font-family="sans-serif" font-size="11" fill="#2e9e7c">normal band</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Most readings sit inside the normal band; the model flags the one that doesn&#39;t.</figcaption>
</figure>

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
