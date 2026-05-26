---
layout: post
title: "Predicting Yeast Viability, Vitality, and Pitching Rate"
image: /assets/og/predicting-yeast-viability-vitality.png
description: "How to model yeast viability and vitality from lab and process data to recommend the right pitching rate and decide when to re-propagate."
date: 2023-08-11
updated: 2023-08-11
tags: [brewing-science, yeast, machine-learning]
faq:
  - q: "What is the difference between yeast viability and vitality?"
    a: "Viability is the percentage of cells still alive, usually checked by methylene blue staining. Vitality is how active those live cells are, measured by acidification power, CO2 evolution, oxygen uptake rate, or sterol content."
  - q: "Can a model replace methylene blue counts?"
    a: "No. A model complements the lab by combining viability with generation number, storage history, and vitality markers, but you still need a measured viability count as an input and a sanity check."
  - q: "What pitching rate should I aim for?"
    a: "Roughly 0.5-1.5x10^7 cells/mL for ales and 1.0-2.0x10^7 cells/mL for lagers (about 0.2 kg/hL pressed). A model adjusts within that range based on the yeast's measured condition."
---

**Short answer: you can predict the right pitching rate before brew day by modelling viability and vitality together, rather than counting cells and hoping.** The data you need is mostly already in your yeast-lab logs.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Predicting Yeast Viability, Vitality, and Pitching Rate</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Why a healthy count is not enough
A pitch can have 95% viability and still ferment poorly. Viability tells you what fraction of cells are alive, typically by methylene blue staining. It says nothing about how *active* those cells are. Vitality covers that, and it is measured several ways: acidification power, CO2 evolution rate, oxygen uptake rate (OUR), and sterol content. Bud-scar count adds another signal, indicating cell age across the population.

Operators who pitch on viability alone tend to over- or under-pitch. Both shift flavour and yeast health: under-pitching stresses the crop and lifts esters and diacetyl, while over-pitching can flatten ester character and burn through reserves. The target range is well established (ale 0.5-1.5x10^7 cells/mL, lager 1.0-2.0x10^7 cells/mL), but the right point *within* that range depends on the specific crop in front of you.

## What goes into the model
Treat this as a measure-first exercise. The features are unglamorous but predictive:

- **Generation number** and serial-repitch history.
- **Storage time and temperature** since cropping.
- **Vitality markers**: acidification power, OUR, CO2 evolution.
- **Viability** from methylene blue.
- **Prior performance**: attenuation, lag time, and diacetyl reduction from that yeast line's last few batches.

A regression or gradient-boosted model maps these to two outputs: an expected fermentation performance (lag, attenuation, VDK clearance) and a recommended pitching rate. A second flag asks the more important operational question: is this crop good enough to re-pitch, or should you re-propagate from a fresh culture? That decision protects a whole batch.

Wort conditions matter too. Oxygen at pitching should sit at 8-16 mg/L for sterol and membrane synthesis, consumed within 3-9 hours. FAN of 150-220 mg/L supports clean growth; low nitrogen pushes higher alcohols and diacetyl up. A useful model treats yeast condition and wort condition as a pair, because a tired crop into low-FAN wort is the combination that bites.

## Where it breaks
Be honest about the limits. Methylene blue measures viability, not vitality, and it loses resolution above roughly 90% viability where most pitches live. Yeast biology is genuinely variable batch to batch, so a model gives you a calibrated expectation, not a guarantee. The model is also only as good as the per-generation records behind it; gaps in storage temperature or missing vitality assays widen the error bars fast. Use the prediction to set a starting pitch, then confirm with your standard lag-time and gravity checks.

A natural-language copilot helps close the loop here. Pointed at your yeast-lab logs, it can read the latest viability and vitality entries, the storage history, and the last few fermentations, then recommend a pitch rate and cropping fraction in plain English with its reasoning shown. That turns a spreadsheet of assays into a decision a cellar operator can act on at 6am, and it drafts the note that records why.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives yeast, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Predicting Yeast Viability, Vitality, and Pitching Rate</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Yeast</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">quality</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">What drives yeast, and what it changes downstream.</figcaption>
</figure>

## The bottom line
Viability alone under-specifies a pitch. Combine it with vitality markers, generation history, and storage data, and a model can recommend a pitching rate and a re-propagate decision before you open the tank. Keep measuring, keep the model honest with real fermentation outcomes, and treat its number as a starting point you confirm.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Can AI predict beer fermentation?]({{ '/2026/can-ai-predict-beer-fermentation/' | relative_url }})

## Frequently asked questions

**What is the difference between yeast viability and vitality?**
Viability is the percentage of cells still alive, usually checked by methylene blue staining. Vitality is how active those live cells are, measured by acidification power, CO2 evolution, oxygen uptake rate, or sterol content.

**Can a model replace methylene blue counts?**
No. A model complements the lab by combining viability with generation number, storage history, and vitality markers, but you still need a measured viability count as an input and a sanity check.

**What pitching rate should I aim for?**
Roughly 0.5-1.5x10^7 cells/mL for ales and 1.0-2.0x10^7 cells/mL for lagers (about 0.2 kg/hL pressed). A model adjusts within that range based on the yeast's measured condition.
