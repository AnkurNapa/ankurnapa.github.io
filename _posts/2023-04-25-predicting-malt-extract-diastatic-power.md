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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Predicting Malt Extract and Diastatic Power Before You Brew</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives malt, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Predicting Malt Extract and Diastatic Power Before You Brew</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Malt</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">quality</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">What drives malt, and what it changes downstream.</figcaption>
</figure>

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
