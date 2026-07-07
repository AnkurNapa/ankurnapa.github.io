---
layout: post
title: "Predicting Carbonation and Dispense Consistency"
image: /assets/og/predicting-carbonation-dispense-consistency.png
description: "How AI models CO2 volumes and dispense quality from inline CO2, line temperature and pressure to cut fobbing, and where the model loses sight of the bar."
date: 2022-09-14
updated: 2022-09-14
tags: [brewing-science, packaging, process-optimization]
faq:
  - q: "What is the target carbonation level for beer?"
    a: "Many beers sit around 2.2 to 2.7 volumes of CO2, though the right target depends on the style. Dissolved CO2 can be measured inline, which makes carbonation a controllable, model-friendly variable."
  - q: "Can a model stop fobbing and pouring problems?"
    a: "It can reduce them on the brewery and cellar side by predicting good CO2, temperature and pressure set-points. But fobbing often happens at the dispense point, which is downstream of you, so a model cannot fix a warm or badly balanced bar line."
  - q: "Why does the same keg pour differently in two venues?"
    a: "Dispense quality depends on line temperature, applied pressure, line length and restriction, all of which vary by venue. The beer left your brewery identical; the pour changed because the dispense system did."
---

**Short answer: you can model target CO2 volumes and dispense quality from inline carbonation, line temperature, pressure and restriction to cut fobbing and over- or under-carbonation, but the dispense point is downstream of the brewery and a model cannot control it.** Carbonation is measurable, which makes it controllable.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the whiskey production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Predicting Carbonation and Dispense Consistency</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Distil</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mature</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Bottle</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the whiskey production flow, start to finish.</figcaption>
</figure>

## Carbonation as a controllable variable
Carbonation is one of the more forgiving things to model because it is directly measurable. Many beers target roughly 2.2 to 2.7 volumes of CO2, and dissolved CO2 can be read inline during carbonation and packaging. That gives you a continuous, quantitative target rather than a subjective judgement, which is exactly the kind of variable data science handles well.

The faults are well defined too. Over-carbonation leads to gushing and excessive foam; under-carbonation leaves beer flat and lifeless; fobbing, the foaming and spluttering at the tap, wastes product and frustrates the pour. Each of these maps to measurable conditions, so the path from data to control is short.

## Measure first, then model the set-points
Measure first applies cleanly here. Log inline CO2 readings against the process conditions that produce them: carbonation pressure and temperature, time, and on the dispense side, line temperature, applied pressure, line length and restriction. With those paired records, a model learns the relationship between set-points and outcomes, and can predict the conditions that land you on target CO2 with a stable, fob-free pour.

This is where machine learning beats a static balancing chart. The classic dispense-balance calculation assumes ideal, steady conditions; a model trained on your real readings captures how temperature swings, line runs and restriction interact in practice. It can predict not just the average outcome but the *variability*, flagging when a given configuration is likely to drift in and out of fobbing rather than sit comfortably on target. The goal is consistency, not a single perfect pour.

Carbonation also does not sit alone: the same CO2 that you are dialling in shapes the head on the beer, which ties this directly to [predicting beer foam and head retention]({{ '/2021/predicting-beer-foam-head-retention/' | relative_url }}). A model that optimises one without watching the other can trade a fobbing problem for a flat-head problem.

## A copilot for pressure and temperature set-points
The generative angle is prescriptive. Rather than reading a balance chart, a cellar or quality lead can ask a copilot: "This line is 25 metres, the cellar runs at 6 degrees, what applied pressure keeps a 2.5-volume lager pouring cleanly?" Built on the dispense model, the assistant proposes set-points and explains the trade-off, for example that raising pressure to stop the beer going flat over a long line risks fobbing if the cooler warms up. It turns a tacit, experience-bound skill into something a copilot can suggest and a human can sign off, with the operator still owning the decision.

## Where it breaks
The honest limit is ownership of the dispense point. Carbonation in the can or keg is yours; the pour in the glass usually is not. Once a keg leaves for a bar, the line temperature, applied gas pressure, line length and cleanliness are all set by someone else's cellar, and a warm or poorly balanced bar line will fob a perfectly carbonated beer. Your model can predict the *potential* for a good pour and prescribe ideal venue conditions, but it cannot enforce them downstream.

Sensor calibration is the other constraint. Inline CO2 measurement drifts and needs regular checking, and a model trained on a miscalibrated sensor will confidently aim at the wrong target. Garbage in, garbage out applies as firmly to carbonation as to anything else.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Emissions split by scope — most of the footprint usually hides in Scope 3."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FOOTPRINT BY SCOPE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Predicting Carbonation and Dispense Consistency</text><rect x="300" y="80" width="120" height="40" fill="#2e9e7c"/><rect x="300" y="120" width="120" height="40" fill="#00695c"/><rect x="300" y="160" width="120" height="90" fill="#06483f"/><rect x="460" y="84" width="14" height="14" fill="#2e9e7c"/><text x="482" y="96" font-family="sans-serif" font-size="12.5" fill="#06483f">Scope 1 — direct</text><rect x="460" y="124" width="14" height="14" fill="#00695c"/><text x="482" y="136" font-family="sans-serif" font-size="12.5" fill="#06483f">Scope 2 — energy</text><rect x="460" y="184" width="14" height="14" fill="#06483f"/><text x="482" y="196" font-family="sans-serif" font-size="12.5" fill="#06483f">Scope 3 — value chain (largest)</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Emissions split by scope — most of the footprint usually hides in Scope 3.</figcaption>
</figure>

## The bottom line
Carbonation and dispense are measurable, so they are controllable: a model trained on inline CO2, line temperature, pressure and restriction can hold you near a 2.2 to 2.7-volume target and cut fobbing and over- or under-carbonation. A copilot can prescribe set-points. Just remember the dispense point is often downstream of the brewery, and the model is only as good as your sensor calibration.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*

## Frequently asked questions

**What is the target carbonation level for beer?**
Many beers sit around 2.2 to 2.7 volumes of CO2, though the right target depends on the style. Dissolved CO2 can be measured inline, which makes carbonation a controllable, model-friendly variable.

**Can a model stop fobbing and pouring problems?**
It can reduce them on the brewery and cellar side by predicting good CO2, temperature and pressure set-points. But fobbing often happens at the dispense point, which is downstream of you, so a model cannot fix a warm or badly balanced bar line.

**Why does the same keg pour differently in two venues?**
Dispense quality depends on line temperature, applied pressure, line length and restriction, all of which vary by venue. The beer left your brewery identical; the pour changed because the dispense system did.
