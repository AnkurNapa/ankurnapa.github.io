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
