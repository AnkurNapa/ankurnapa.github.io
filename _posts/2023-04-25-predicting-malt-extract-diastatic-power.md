---
layout: post
title: "Predicting Malt Extract and Diastatic Power Before You Brew"
image: /assets/og/predicting-malt-extract-diastatic-power.png
description: "Predict hot-water extract and diastatic power from routine malt analysis so brewers adjust grist and mash before a brew, not after a yield miss."
date: 2023-04-25
updated: 2023-04-25
tags: [brewing-science, malt, machine-learning]
faq:
  - q: "What can you predict from a malt certificate of analysis?"
    a: "From routine figures like protein, modification (Kolbach) and moisture you can predict hot-water extract — your yield ceiling — and diastatic power, the enzyme potential for starch conversion."
  - q: "Does predicting extract guarantee my brewhouse yield?"
    a: "No. The model predicts what the malt can deliver. Your actual recovery still depends on milling, mashing, lautering and transfer losses in your own brewhouse."
  - q: "Why does diastatic power matter for the grist?"
    a: "Diastatic power is the alpha- and beta-amylase potential that converts starch. If a lot is low, or you run a lot of enzyme-free adjunct, you may not have enough enzyme to convert the mash fully."
---

**Short answer: routine malt analysis already contains enough signal to predict a lot's hot-water extract and diastatic power, so you can adjust the grist or mash before you brew rather than after a yield miss.** It will not predict your brewhouse recovery — only what the malt is capable of giving you.

## Two numbers that set your ceiling
Two malt figures shape the whole brew. Hot-water extract is your yield ceiling: it tells you how much soluble material the malt can give up, and therefore the most gravity you can ever pull from that grist. Diastatic power is the enzyme potential — the combined alpha- and beta-amylase activity — that converts starch in the mash. Alpha-amylase produces dextrins; beta-amylase produces fermentable maltose. Without enough diastatic power, the mash will not convert fully, and that limit bites hardest when you lean on enzyme-free adjuncts.

Both are predictable from analysis you already receive. Extract and diastatic power track with protein, modification (Kolbach index) and moisture in ways that are consistent enough to model. A lot that arrives over-protein and under-modified will tend to under-deliver on extract and behave differently in the mash — and you would rather know that the day it lands than the day you fall short in the kettle.

## Modelling from data you already have
This is a well-posed machine-learning problem precisely because the inputs are routine. Every malt delivery comes with a certificate of analysis; the features — protein, modification, moisture, and where available friability and beta-glucan — are the same ones maltsters report. A model trained on your historical lots and how they actually performed learns the relationship between those numbers and the extract and diastatic power you realise.

The data-science discipline is to measure first and capture the loop. Log each lot's analysis alongside the brew outcomes it produced, so the model is grounded in your malt and your kit rather than a generic regression from a textbook. Over time it learns your suppliers' quirks — which maltster's figures run optimistic, which variety converts low — and that local knowledge is exactly what a brewer cannot get from a single certificate.

## Where it breaks
The sharp limit is scope: the model predicts the malt, not the brew. It tells you the extract a lot can yield and the enzyme it carries, but it says nothing about how much of that you will recover. Milling, mash thickness, time and temperature, sparge and lauter losses all sit between the malt's potential and the gravity in your kettle. Treating a healthy predicted extract as a guaranteed yield is the classic mistake — that question belongs to your [mash efficiency and extract-yield]({{ '/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}) model, not this one.

The other limit is data drift. If your suppliers, varieties or analysis methods change, predictions degrade until the model relearns. And a certificate measures a sampled average — real lots vary within the delivery, so a prediction is a strong expectation, not a promise.

## A copilot for grist tweaks
The generative-AI angle is a copilot that closes the loop on the prediction. When a malt lot's predicted extract or diastatic power drifts from your recipe assumptions, the copilot explains it plainly and recommends a concrete adjustment: "Lot 220's predicted extract is 1.2% below spec and diastatic power is on the low side — increase grist by roughly 3% and consider trimming enzyme-free adjunct, or lower the saccharification rest to favour conversion." It turns a number on a certificate into a brewing decision, with the brewer signing off rather than recalculating by hand.

## The bottom line
Predicting malt extract and diastatic power from routine analysis is one of the higher-confidence uses of machine learning in the brewhouse, because the inputs already exist and the physics is well understood. Use it to adjust the grist and mash before you brew, keep it honest about being a malt model rather than a yield model, and feed it your own lot history so it speaks your supply base's language.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Predicting malt quality from barley]({{ '/2023/predicting-malt-quality-from-barley/' | relative_url }}).

## Frequently asked questions

**What can you predict from a malt certificate of analysis?**
From routine figures like protein, modification (Kolbach) and moisture you can predict hot-water extract — your yield ceiling — and diastatic power, the enzyme potential for starch conversion.

**Does predicting extract guarantee my brewhouse yield?**
No. The model predicts what the malt can deliver. Your actual recovery still depends on milling, mashing, lautering and transfer losses in your own brewhouse.

**Why does diastatic power matter for the grist?**
Diastatic power is the alpha- and beta-amylase potential that converts starch. If a lot is low, or you run a lot of enzyme-free adjunct, you may not have enough enzyme to convert the mash fully.
