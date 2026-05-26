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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Anomaly Detection on Brewery Sensor Data</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Most readings sit inside the normal band; the model flags the one that doesn&#39;t."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">ANOMALY DETECTION</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Anomaly Detection on Brewery Sensor Data</text><rect x="60" y="120" width="620" height="70" fill="#5b7a1f" opacity="0.12"/><line x1="60" y1="120" x2="680" y2="120" stroke="#5b7a1f" stroke-width="1" stroke-dasharray="4 3"/><line x1="60" y1="190" x2="680" y2="190" stroke="#5b7a1f" stroke-width="1" stroke-dasharray="4 3"/><circle cx="110" cy="150" r="5" fill="#6b6258"/><circle cx="160" cy="140" r="5" fill="#6b6258"/><circle cx="210" cy="165" r="5" fill="#6b6258"/><circle cx="265" cy="148" r="5" fill="#6b6258"/><circle cx="320" cy="158" r="5" fill="#6b6258"/><circle cx="380" cy="143" r="5" fill="#6b6258"/><circle cx="440" cy="168" r="5" fill="#6b6258"/><circle cx="500" cy="150" r="5" fill="#6b6258"/><circle cx="560" cy="160" r="5" fill="#6b6258"/><circle cx="620" cy="146" r="5" fill="#6b6258"/><circle cx="345" cy="92" r="7" fill="#7a1f3d"/><text x="345" y="80" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">anomaly</text><text x="668" y="138" text-anchor="end" font-family="sans-serif" font-size="11" fill="#5b7a1f">normal band</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Most readings sit inside the normal band; the model flags the one that doesn&#39;t.</figcaption>
</figure>

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
