---
layout: post
title: "Anomaly Detection on Brewery Sensor Data"
image: /assets/og/anomaly-detection-brewery-sensors.png
description: "How anomaly detection learns the normal envelope of brewery sensor data to flag drift, leaks, and faults earlier than fixed thresholds."
date: 2021-07-14
updated: 2021-07-14
tags: [brewing-science, sensors, machine-learning]
faq:
  - q: "What is anomaly detection in a brewery context?"
    a: "It is a model that learns the normal behaviour of your tank and utility time-series, then flags readings that fall outside that learned pattern. Unlike a fixed threshold, it adapts to the operating context, so it can catch slow drift and odd combinations of readings, not just hard limits being breached."
  - q: "Do I need a process historian before I start?"
    a: "Effectively, yes. Anomaly detection needs a continuous, clean stream of tagged time-series data to learn from, and a historian is the simplest way to provide it. Without consistent tag naming and reliable timestamps, the model learns noise instead of process behaviour."
  - q: "Will it replace my existing alarms?"
    a: "No, and you should not let it. Keep safety-critical fixed-limit alarms exactly as they are. Anomaly detection sits alongside them as an early-warning layer for subtler problems that a single threshold would miss."
---

**Short answer: anomaly detection learns what "normal" looks like across your sensor streams and flags deviations earlier than a fixed threshold ever could.** A brewery is full of time-series data, and most of it is watched by alarms that only fire after something has already gone wrong. There is a better starting point.

## Why fixed thresholds quietly fail
Tanks, the brewhouse, and utilities all emit continuous signals: temperature, pressure, gravity, flow, and CO2. The traditional approach wraps each tag in a high and low limit. That works for catching the obvious, but it has two blind spots. First, a reading can drift steadily toward trouble while staying inside its limits the whole way. Second, a fault often shows up as an unusual *combination* of readings — normal pressure with abnormal flow, say — that no single threshold can see.

Anomaly detection takes a different view. Instead of asking "is this value too high?", it asks "is this pattern consistent with how the process normally behaves?" The model learns the normal operating envelope from historical data, including how variables move together. When the live signal departs from that envelope, you get a flag — often well before a hard limit would trip.

## Measure first, model second
This is where most projects live or die, and it has nothing to do with the algorithm. You need a process historian collecting clean, consistently tagged time-series, with reliable timestamps and a sensible sampling rate. If FV3's temperature probe is mislabelled or drops out for an hour every shift, the model will faithfully learn that mess as "normal".

So the honest sequence is: instrument the process, get the data plumbing right, then model. We have written more about getting that base in place in [building a brewery data foundation for AI]({{ '/2024/building-brewery-data-foundation-ai/' | relative_url }}). Skip it, and you will spend your time debugging data rather than catching faults. The unglamorous truth is that the historian and the tag dictionary matter more than the choice of model.

Once the data is trustworthy, the modelling itself is not exotic. Methods range from simple statistical envelopes and seasonal baselines through to autoencoders that reconstruct expected sensor behaviour and score how far reality has diverged. Start simple; a well-tuned baseline often beats a fancy model on dirty data.

## Where it breaks
Be honest about the limits, because they are real. Genuine faults are rare by definition, which means your training data is wildly imbalanced — the model sees thousands of normal hours for every abnormal minute. That makes some failure modes effectively invisible until the first time they happen.

The bigger operational risk is alarm fatigue. Set the sensitivity too high and you will bury the cellar team in flags for harmless blips, after which every alert gets ignored, including the one that mattered. Tuning the threshold between "missed fault" and "noise" is an ongoing job, not a one-off. And none of this works without the historian and clean tags mentioned above — a model trained on gappy data will flag the gaps, not the leaks.

There is also a scope limit: anomaly detection tells you *something* is off, not always *what*. It points; a human still investigates.

## A practical gen-AI angle
The "what is it?" gap is exactly where a generative-AI copilot earns its keep. When the system flags an anomaly on FV3, an LLM grounded in your batch records, maintenance logs, and SOPs can draft a plain-language explanation: which tags moved, what the likely causes are given similar past events, and which checks to run first. It turns a raw alert into a starting hypothesis the cellar team can act on. The caution is the same as for any LLM — it must be grounded in your real documents and cite them, or it will invent a confident, wrong story.

## The bottom line
Anomaly detection is one of the highest-value, lowest-glamour AI applications in a brewery: it catches drift and odd patterns that fixed limits miss, giving you time to act. But it lives or dies on data quality, demands careful tuning to avoid alarm fatigue, and only points at problems rather than diagnosing them. Get the historian right first, keep your safety alarms, and treat the model as an early-warning layer — not a replacement for judgement.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*

## Frequently asked questions

**What is anomaly detection in a brewery context?**
It is a model that learns the normal behaviour of your tank and utility time-series, then flags readings that fall outside that learned pattern. Unlike a fixed threshold, it adapts to the operating context, so it can catch slow drift and odd combinations of readings, not just hard limits being breached.

**Do I need a process historian before I start?**
Effectively, yes. Anomaly detection needs a continuous, clean stream of tagged time-series data to learn from, and a historian is the simplest way to provide it. Without consistent tag naming and reliable timestamps, the model learns noise instead of process behaviour.

**Will it replace my existing alarms?**
No, and you should not let it. Keep safety-critical fixed-limit alarms exactly as they are. Anomaly detection sits alongside them as an early-warning layer for subtler problems that a single threshold would miss.
