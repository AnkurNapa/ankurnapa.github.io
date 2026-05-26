---
layout: post
title: "Predicting Lauter and Wort Separation Performance"
image: /assets/og/predicting-lauter-wort-separation.png
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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Predicting Lauter and Wort Separation Performance</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Predicting Lauter and Wort Separation Performance</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Process</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

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
