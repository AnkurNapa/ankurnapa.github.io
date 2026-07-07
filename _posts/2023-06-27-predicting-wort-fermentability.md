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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Predicting Wort Fermentability From the Sugar Spectrum</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives wort, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Predicting Wort Fermentability From the Sugar Spectrum</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Wort</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">quality</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">What drives wort, and what it changes downstream.</figcaption>
</figure>

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
