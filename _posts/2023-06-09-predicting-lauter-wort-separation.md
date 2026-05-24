---
layout: post
title: "Predicting Lauter and Wort Separation Performance"
description: "Predict run-off time and stuck-mash risk, then tune crush, rake depth, and flow from grist and mash data to protect brewhouse turns and extract."
date: 2023-06-09
updated: 2023-06-09
tags: [brewing-science, brewhouse, process-optimization]
faq:
  - q: "Can you really predict a stuck mash before it happens?"
    a: "You can predict elevated risk, not a certainty. A model trained on crush, grain-bed depth, and early run-off behaviour flags batches likely to run slow, giving you time to slow the flow or recut before the bed seals."
  - q: "What data do I need to start?"
    a: "At minimum: mill gap or crush distribution, grist bill, grain-bed depth, run-off flow rate, and the time and clarity of each run-off. Even logging these by hand for 30-40 batches gives a usable baseline."
  - q: "Will this replace my brewer's judgement?"
    a: "No. It turns hard-won judgement into something repeatable across shifts and recipes. The brewer still owns the call; the model just makes the early-warning signal louder and earlier."
---

**Short answer: you can predict run-off time and stuck-mash risk from grist and mash data, then adjust crush, rake depth, and flow before the bed seals — protecting both your brewhouse turns and your extract.** Lautering is where slow batches quietly eat the day. A little prediction goes a long way.

## Why separation performance is worth predicting
Wort separation sits at the heart of brewhouse throughput. Extract recovery and run-off speed both depend on crush, grain-bed depth and permeability, rake or cut depth, flow rate, and sparge. Push too hard and you compact the bed: run-off stalls, the batch runs late, and the next brew slides back. Run off too fast and you pull haze and poor clarity into the kettle. Keep sparge water below roughly 78 °C or you start extracting tannins and polyphenols you do not want.

Each of those failure modes costs money in a different currency — time on the slow side, quality on the fast side. The point of prediction is to stay in the narrow band between them without babysitting every batch.

## What the model actually does
The machine-learning piece is a predictor of run-off time and stuck-mash risk. Feed it the grist bill, mill setting or crush distribution, grain-bed depth, and the shape of the early run-off curve, and it returns an expected run-off duration plus a risk score. When that score climbs, it is telling you the bed is heading toward compaction.

That only works if you measure first. The data-science groundwork is unglamorous: log mill gap, crush fineness, bed depth, flow rate, and the time and turbidity of each run-off, batch after batch. Differential pressure across the bed, where you have it, is one of the most informative single signals you can add. None of this is exotic — but lautering is a sensor-poor step in most breweries, so the data often simply does not exist yet. If that is you, start collecting before you start modelling.

## A copilot for the run-off, not just a dashboard
The generative-AI angle here is practical. Instead of a static risk number, picture a copilot watching the run-off live and saying, in plain language: "Flow has dropped 30% and differential pressure is rising — recut to 15 mm and ease the flow by 20% before the bed sets, because your crush this morning ran finer than last week." It recommends the rake and flow adjustment *and* explains the reasoning, so the operator learns the pattern rather than blindly following a prompt. Over time that turns one expert brewer's instinct into shared shop-floor knowledge.

## Where it breaks
Be honest about the limits. This is a sensor-poor step, so models often lean on proxies and a thin data history. Mill drift is the quiet killer: rollers wear, the crush gradually shifts, and a model trained on last quarter's crush slowly goes stale. You need to recalibrate the mill and retrain on fresh batches, or the predictions decay. Malt varies by lot, too — a new barley shipment can change husk integrity and bed permeability overnight. Treat the model as an assistant that needs feeding, not a set-and-forget control system. And if you only have ten batches of clean data, the right move is to keep logging, not to over-trust a fragile fit.

## The bottom line
Predicting separation performance is one of the higher-leverage, lower-cost wins in the brewhouse, because the failure is so expensive and the inputs are so few. Start by measuring crush, bed depth, flow, and run-off time, build a simple risk model, then layer a copilot on top to guide adjustments mid-run-off. Just budget for mill drift and lot variation — the model is only as current as the data you feed it.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [predicting mash efficiency and extract yield]({{ '/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}).

## Frequently asked questions

**Can you really predict a stuck mash before it happens?**
You can predict elevated risk, not a certainty. A model trained on crush, grain-bed depth, and early run-off behaviour flags batches likely to run slow, giving you time to slow the flow or recut before the bed seals.

**What data do I need to start?**
At minimum: mill gap or crush distribution, grist bill, grain-bed depth, run-off flow rate, and the time and clarity of each run-off. Even logging these by hand for 30-40 batches gives a usable baseline.

**Will this replace my brewer's judgement?**
No. It turns hard-won judgement into something repeatable across shifts and recipes. The brewer still owns the call; the model just makes the early-warning signal louder and earlier.
