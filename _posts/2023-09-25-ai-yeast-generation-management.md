---
layout: post
title: "Data-Driven Yeast Generation Management and Cropping"
image: /assets/og/ai-yeast-generation-management.png
description: "Track yeast performance across serial generations to decide when to re-propagate and how to crop, balancing cost against drift in attenuation and flavour."
date: 2023-09-25
updated: 2023-09-25
tags: [brewing-science, yeast, process-optimization]
faq:
  - q: "How many generations can I re-pitch yeast?"
    a: "There is no fixed number. It depends on the strain, handling and hygiene. Rather than a hard limit, track attenuation, flavour, viability and flocculation per generation and re-propagate when performance drifts out of spec."
  - q: "What does cropping the right fraction mean?"
    a: "When you harvest yeast, the middle fraction is generally the healthiest. Cropping too much of the early or late fraction skews cell age and flocculation, which over generations degrades attenuation and VDK clearance."
  - q: "Why does over-flocculent yeast cause problems?"
    a: "Flocculation is driven by cell-wall mannoproteins. Too-flocculent yeast drops out early, leading to poor attenuation and high residual VDK because it leaves before finishing reuptake."
---

**Short answer: track yeast performance across serial generations and a model tells you when to re-propagate and how to crop, so you balance the cost of fresh culture against the cost of drift.** The decision is currently made by gut feel and an arbitrary generation cap.

## The real cost of an extra generation
Re-pitching yeast saves propagation cost and is standard practice, but every generation carries risk of drift. Attenuation can creep, flavour can shift, and flocculation behaviour can change as the population's age structure and contamination load evolve. The usual response, a fixed cap such as "retire at generation eight", is crude: a well-handled crop might be fine at generation twelve, while a stressed one is off by generation four. Managing by data beats managing by counter.

The mechanics give you levers. Cropping the right fraction, generally the healthy middle, keeps cell age sensible across generations. Acid washing controls bacterial load between pitches. Flocculation is driven by cell-wall mannoproteins, and a crop drifting too flocculent will drop out early, costing you attenuation and leaving residual VDK behind. Each of these shows up in the numbers before it shows up in the beer.

## What to record, and what to model
Discipline at the tank is the price of admission. Per generation, capture:

- **Attenuation** achieved versus target.
- **Lag time** and fermentation duration.
- **Diacetyl / VDK clearance** at the end.
- **Viability and vitality** of the crop.
- **Flocculation** behaviour and cropping fraction taken.
- **Acid-wash** and storage details.

With this history, a model fits a performance trajectory per yeast line and projects where the next generation is likely to land. It flags the generation at which expected attenuation or VDK clearance will breach spec, turning "retire at eight" into "this line is trending out by generation ten, re-propagate now". It can also recommend the cropping fraction that keeps the age structure healthiest.

A language model adds a review layer that operators actually read. Pointed at the generation history, it summarises the trend, calls retire-or-repropagate with stated reasons, for example "attenuation down 1.5 plato over three generations and flocculation rising, recommend re-propagation", and drafts the handover note. That makes the decision auditable and consistent across brewers.

## Where it breaks
The honest limit is record discipline. This entire approach collapses without complete, consistent per-generation data; a few skipped viability counts or unlogged crops and the trajectory is guesswork. Small breweries running few batches per line also have sparse histories, so projections carry wide uncertainty early on. And a model extrapolates from past behaviour, which a sudden contamination event or a handling change can break without warning. Use the projection to schedule re-propagation proactively, but keep the micro checks and tasting that catch the surprises.

## The bottom line
Yeast generation management is a cost-versus-drift trade-off, and a fixed generation cap throws away information. Record performance per generation, model the trajectory, and re-propagate and crop on evidence rather than a counter. The method is only as good as the records, so the real investment is disciplined logging at the tank.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Predicting yeast viability and vitality]({{ '/2023/predicting-yeast-viability-vitality/' | relative_url }})

## Frequently asked questions

**How many generations can I re-pitch yeast?**
There is no fixed number. It depends on the strain, handling and hygiene. Rather than a hard limit, track attenuation, flavour, viability and flocculation per generation and re-propagate when performance drifts out of spec.

**What does cropping the right fraction mean?**
When you harvest yeast, the middle fraction is generally the healthiest. Cropping too much of the early or late fraction skews cell age and flocculation, which over generations degrades attenuation and VDK clearance.

**Why does over-flocculent yeast cause problems?**
Flocculation is driven by cell-wall mannoproteins. Too-flocculent yeast drops out early, leading to poor attenuation and high residual VDK because it leaves before finishing reuptake.
