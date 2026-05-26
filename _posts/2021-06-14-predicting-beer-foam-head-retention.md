---
layout: post
title: "Predicting Beer Foam and Head Retention"
image: /assets/og/predicting-beer-foam-head-retention.png
description: "How AI models beer foam and head retention from foam-positive polypeptides, iso-alpha-acids and lipids, where it helps QC, and where it breaks."
date: 2021-06-14
updated: 2021-06-14
tags: [brewing-science, quality-control, machine-learning]
faq:
  - q: "What makes beer foam last?"
    a: "Foam-positive hydrophobic polypeptides from malt protein and iso-alpha-acids from hops stabilise the bubbles. Foam-negative lipids, basic detergent residues and high gravity break them down, so head retention is the balance between the two."
  - q: "Can a model predict which batches will have poor foam?"
    a: "Yes, to a degree. A model trained on protein and bitterness measures, lipid contamination signals and carbonation can flag at-risk batches before packaging, though measurement variance limits the precision."
  - q: "Why does foam retention vary even with the same recipe?"
    a: "Glassware cleanliness, dispense conditions, carbonation level and trace lipid contamination all shift the result. These downstream factors often matter as much as the recipe, which is why measurement noise is a real constraint."
---

**Short answer: head retention can be modelled from the balance of foam-positive proteins and iso-alpha-acids against foam-negative lipids, plus carbonation, and AI can flag at-risk batches before they ship.** Foam is physics and chemistry you can measure, which makes it a good ML target.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Predicting Beer Foam and Head Retention</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## The chemistry behind a lasting head
Foam stability is a tug-of-war. On the foam-positive side are hydrophobic polypeptides derived from malt protein and the iso-alpha-acids contributed by hops; these adsorb at the bubble surface and hold the structure together. On the foam-negative side are lipids, basic detergent residues, and the destabilising effect of high gravity. A beer's head retention is essentially the net result of those competing influences, measured by methods such as NIBEM or the Rudin test.

Because each of those drivers is measurable, foam is a tractable data problem. You can quantify foam-positive protein fractions, bitterness as a proxy for iso-alpha-acids, and lipid contamination, then pair them with the measured retention time. That is the raw material a model needs.

## Measure first, then model the risk
The discipline is the same as always: measure first. Build a dataset that pairs each batch's protein and bitterness measures, any lipid or detergent-contamination signals, carbonation level, and the measured NIBEM or Rudin result. With enough paired batches, a regression model learns which combinations of inputs predict a short-lived head.

The practical payoff is not a precise retention number; it is a risk flag. A model that says "this batch has elevated lipid carry-over and below-target foam protein, expect poor retention" lets you intervene before packaging, when you still have options. Machine learning earns its keep here by capturing the interactions between foam-positive and foam-negative factors that a single threshold rule would miss, for example that a borderline protein level only becomes a problem when lipids are also high.

Tree-based models suit this well because the relationships are nonlinear and interacting, and they make it easy to read off which factor is driving a given prediction.

## A copilot for diagnosing a poor-foam batch
The generative-AI angle is diagnostic. When a batch fails its foam check, a brewer faces a list of suspects: contamination, low protein, over-attenuation, a carbonation miss, or a dispense problem. A copilot built on the foam model can take the batch's measurements and produce a ranked, plain-language hypothesis: "Foam is 30% below target. The most likely cause is lipid carry-over from the wort, given the contamination reading; a carbonation shortfall is a secondary suspect." That compresses a tedious detective exercise into a starting point, while the brewer confirms the cause with their own checks.

## Where it breaks
The honest limits are mostly about measurement. NIBEM and Rudin readings carry real variance, so the target you are training against is noisy, which caps how accurate any model can be. Trace lipid contamination is hard to quantify consistently. And much of the foam a drinker actually sees is decided downstream of the brewery: glassware cleanliness, line and glass temperature, dispense pressure and pour technique can wreck a head that was fine in the tank. A model built on brewery-side data cannot see those bar-side confounds, so it predicts the *potential* for good foam, not the foam in a specific glass.

Carbonation matters too, and it interacts with everything else, which is a reminder that foam never sits in isolation from the rest of the package.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Predicting Beer Foam and Head Retention</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Process</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

## The bottom line
Head retention is the net of foam-positive polypeptides and iso-alpha-acids against foam-negative lipids and high gravity, plus carbonation, and all of it is measurable. A model trained on that data flags at-risk batches and, paired with a copilot, helps diagnose failures fast. Just respect the measurement noise and the bar-side factors a brewery model cannot see.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [AI quality control in brewing]({{ '/2026/ai-quality-control-in-brewing/' | relative_url }})

## Frequently asked questions

**What makes beer foam last?**
Foam-positive hydrophobic polypeptides from malt protein and iso-alpha-acids from hops stabilise the bubbles. Foam-negative lipids, basic detergent residues and high gravity break them down, so head retention is the balance between the two.

**Can a model predict which batches will have poor foam?**
Yes, to a degree. A model trained on protein and bitterness measures, lipid contamination signals and carbonation can flag at-risk batches before packaging, though measurement variance limits the precision.

**Why does foam retention vary even with the same recipe?**
Glassware cleanliness, dispense conditions, carbonation level and trace lipid contamination all shift the result. These downstream factors often matter as much as the recipe, which is why measurement noise is a real constraint.
