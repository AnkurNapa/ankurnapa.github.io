---
layout: post
title: "Predicting Wort Fermentability From the Sugar Spectrum"
image: /assets/og/predicting-wort-fermentability.png
description: "Predict apparent attenuation limit from mash schedule and malt, then dial the sugar spectrum to target dryness versus body before fermentation begins."
date: 2023-06-27
updated: 2023-06-27
tags: [brewing-science, wort, machine-learning]
faq:
  - q: "What sets wort fermentability in the first place?"
    a: "The sugar spectrum — the balance of fermentable glucose, maltose, and maltotriose against unfermentable dextrins. That balance is governed mainly by mash temperature and time and the malt's enzyme content, which together set the attenuation limit."
  - q: "Can a model predict final attenuation exactly?"
    a: "It can predict the wort's attenuation limit closely, but real attenuation also depends on yeast strain and health. Treat the prediction as the ceiling the wort allows, then account for your yeast on top."
  - q: "How do I validate the prediction?"
    a: "Measure real degree of fermentation or apparent attenuation limit with a forced or rapid fermentation test. Comparing predicted versus measured over several batches is how the model earns trust."
---

**Short answer: you can predict a wort's apparent attenuation limit from the mash schedule and malt, then adjust the sugar spectrum to hit your target dryness or body before a single cell of yeast goes in.** That moves the dryness decision upstream, where it is cheap to change.

## Fermentability is decided in the mash, not the fermenter
By the time wort reaches the fermenter, its fate is largely sealed. The sugar spectrum — glucose, maltose, and maltotriose on the fermentable side, dextrins on the unfermentable side — sets the attenuation limit. That spectrum is governed by mash temperature and time and by the malt's enzymes. A cooler, longer rest favours beta-amylase and a more fermentable wort, giving a drier beer; a warmer mash leaves more dextrins and more body.

So if you want to control dryness versus body, the lever is the mash, and the question is: what attenuation limit will *this* schedule and *this* malt produce? Answer that before you brew and you stop discovering surprises at the end of fermentation.

## What the model predicts
The machine-learning task is a regression: predict the apparent attenuation limit, or real degree of fermentation, from mash step temperatures and times, malt bill and its diastatic power, and liquor-to-grist ratio. The output is the ceiling your wort allows.

This rests on measurement. The data-science discipline is to log every mash schedule and pair it with a measured attenuation limit — a forced or rapid fermentation test that strips out yeast variability and reveals what the wort itself can do. A few dozen batches with honest labels beats a year of unrecorded brews. Mash design and prediction reinforce each other; our piece on [AI mash temperature profile optimisation]({{ '/2023/ai-mash-temperature-profile-optimization/' | relative_url }}) covers the other half of that loop.

## From a target back to a recipe
The generative-AI angle flips the question. Instead of "what will this mash give me?", a brewer can ask an assistant, "I want 82% apparent attenuation on this grist — what mash schedule gets me there?" The tool works backward from the target attenuation to a recommended step profile, explains which rest is doing the work, and flags if the malt's enzyme content cannot reach the target without an adjunct or enzyme addition. That makes recipe design a conversation about outcomes rather than a guess about temperatures.

## Where it breaks
The clean limit is yeast. The model predicts what the wort *allows*, but real attenuation is also set by yeast strain and health. A high-attenuating strain will chew further into the maltotriose than a sluggish or stressed pitch, and an underpitched or oxygen-starved fermentation can stall well short of the limit. So the prediction is a ceiling, not a guarantee — you still have to manage pitch rate, temperature, and yeast vitality to reach it. Mashing-in variability and inaccurate malt enzyme data can also skew the prediction; if your malt spec sheets are stale, the model inherits that error. Validate against measured attenuation regularly.

## The bottom line
Wort fermentability is one of the most predictable things in brewing because it is driven by physical mash variables you already control. Log your schedules, measure the attenuation limit, and a model will tell you the dryness ceiling before you brew — and a generative assistant will hand you the mash schedule for a target you name. Just remember the model sets the ceiling; your yeast decides how close you get.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [AI mash temperature profile optimisation]({{ '/2023/ai-mash-temperature-profile-optimization/' | relative_url }}).

## Frequently asked questions

**What sets wort fermentability in the first place?**
The sugar spectrum — the balance of fermentable glucose, maltose, and maltotriose against unfermentable dextrins. That balance is governed mainly by mash temperature and time and the malt's enzyme content, which together set the attenuation limit.

**Can a model predict final attenuation exactly?**
It can predict the wort's attenuation limit closely, but real attenuation also depends on yeast strain and health. Treat the prediction as the ceiling the wort allows, then account for your yeast on top.

**How do I validate the prediction?**
Measure real degree of fermentation or apparent attenuation limit with a forced or rapid fermentation test. Comparing predicted versus measured over several batches is how the model earns trust.
