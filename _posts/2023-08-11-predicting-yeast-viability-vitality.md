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
