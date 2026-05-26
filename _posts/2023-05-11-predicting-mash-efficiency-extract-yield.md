---
layout: post
title: "Can AI Predict Mash Efficiency and Extract Yield?"
image: /assets/og/predicting-mash-efficiency-extract-yield.png
description: "A model can predict mash efficiency and kettle extract from crush, mash thickness, temperature profile, sparge and malt analysis — flagging low-yield brews early."
date: 2023-05-11
updated: 2023-05-11
tags: [brewing-science, brewhouse, machine-learning]
faq:
  - q: "What does a mash efficiency model predict?"
    a: "It predicts how much of the grist's potential extract you will recover into the kettle, from inputs like crush, mash thickness, temperature and time profile, sparge and the malt analysis."
  - q: "Can AI tell me a brew will miss yield before it happens?"
    a: "It can flag a brew as likely low-yield from the recipe and process settings, giving you a chance to adjust the sparge or extend the mash. It cannot fix a stuck lauter that has already happened."
  - q: "What stops a yield model from working?"
    a: "Inconsistent process and poor logging. If your mill gap and lauter behaviour drift batch to batch and you do not record settings, the model has nothing stable to learn from."
---

**Short answer: yes, within reason — a model can predict mash efficiency and kettle extract from your crush, mash profile, sparge and malt analysis, and flag a low-yield brew early, but only if your process is consistent and well logged.** It is a useful early-warning system, not a substitute for sound brewhouse practice.

## What "efficiency" really measures
Mash efficiency, or extract yield, is simply how much of the grain's potential extract you actually recover into the kettle. The ceiling is set by the malt's hot-water extract; the gap between that ceiling and what you collect is where the brewhouse either earns or loses money. Those gaps come from familiar places: the crush from your mill, mash thickness, mash time and temperature, sparge technique and lauter retention, plus trub, dead-space and transfer losses on the way to the kettle.

Because each of those drivers is measurable, predicting the outcome is a tractable problem. Give a model the crush setting, grist bill, mash thickness, the temperature-time profile, sparge volume and temperature, and the malt analysis, and it can estimate the extract you will collect. The value is timing: a prediction made when you set up the brew, or partway through the mash, leaves room to react — extend the rest, adjust the sparge — before the gravity into the kettle is locked in.

## Data quality decides everything
This model lives or dies on logging discipline, which is why the data-science groundwork matters more than the algorithm choice. The features are operational: mill gap, mash thickness ratio, rest temperatures and durations, sparge water volume and temperature (kept below about 78 °C to avoid dragging out tannins), and the malt figures. The label is the extract you actually achieved into the kettle.

Measure first is not a slogan here, it is the whole job. If you do not record your mill setting, your mash temperatures and your sparge volumes consistently, the model is learning from noise. Brewhouses that already log these to a batch record are most of the way there; those that do not should fix the logging before touching the modelling. A model trained on clean, consistent batch data will spot the patterns — this grist at this thickness with that sparge tends to run a point low — that are invisible across a handful of brews.

## Where it breaks
The honest limit is that physical drift dominates. A mill that wanders out of gap, or a lauter bed that compacts and channels, will swing your real efficiency more than any subtlety the model captures — and the model cannot see a mechanical problem it has no sensor for. If your process is genuinely inconsistent batch to batch, the predictions will be wide and you will rightly stop trusting them.

It is also a correlational model, not a physics simulation. It learns what usually happens on your kit, so a novel grist, a new malt supplier or an unfamiliar mash schedule sits outside its experience and the prediction gets shakier. And like any yield model, it predicts a central expectation; a one-off stuck run-off will still surprise it. Pair it with the wider [brewhouse yield-loss analytics]({{ '/2023/brewhouse-yield-loss-analytics/' | relative_url }}) view to separate recipe effects from equipment drift.

## Diagnosing a low brew in plain language
The generative-AI angle is a large language model that reads the batch log of a low-efficiency brew and explains it. Rather than handing the brewer a number, it narrates the likely cause: "This brew came in 4% under target extract. The mill setting was unchanged, but the lauter run-off was 25 minutes slower than your average and sparge volume was 8% low — the most likely causes are a slow or partial run-off and under-sparging." It turns the log into a diagnosis the brewer can act on, and it can auto-draft the deviation note for the batch record.

## The bottom line
A mash-efficiency model is a worthwhile early-warning tool when your process is stable and your logging is honest. It flags brews heading for a yield miss in time to react and helps diagnose the ones that miss anyway. But it cannot out-predict a drifting mill or a stuck lauter — fix the process and the logging first, then let the model sharpen what is already under control.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Predicting malt extract and diastatic power]({{ '/2023/predicting-malt-extract-diastatic-power/' | relative_url }}).

## Frequently asked questions

**What does a mash efficiency model predict?**
It predicts how much of the grist's potential extract you will recover into the kettle, from inputs like crush, mash thickness, temperature and time profile, sparge and the malt analysis.

**Can AI tell me a brew will miss yield before it happens?**
It can flag a brew as likely low-yield from the recipe and process settings, giving you a chance to adjust the sparge or extend the mash. It cannot fix a stuck lauter that has already happened.

**What stops a yield model from working?**
Inconsistent process and poor logging. If your mill gap and lauter behaviour drift batch to batch and you do not record settings, the model has nothing stable to learn from.
