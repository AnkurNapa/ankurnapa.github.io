---
layout: post
title: "Predicting Packaging Line Downtime and Lifting OEE"
image: /assets/og/packaging-line-oee-downtime-prediction.png
description: "How machine learning predicts micro-stops on the filler and seamer bottleneck to pre-empt the downtime that dominates packaging line OEE losses."
date: 2024-02-25
updated: 2024-02-25
tags: [brewing-science, packaging, predictive-maintenance]
faq:
  - q: "What is OEE and how is it calculated?"
    a: "Overall Equipment Effectiveness is Availability times Performance times Quality. It captures stops, speed losses, and reject rates in one figure, so it shows the true output gap, not just uptime."
  - q: "Why focus on the filler and seamer?"
    a: "The filler and seamer, and sometimes the labeller, are usually the line bottleneck. Losses there cap the whole line, so a minute saved at the bottleneck is a minute of real extra output."
  - q: "What dominates packaging line losses?"
    a: "Micro-stops and changeovers, not big breakdowns. Dozens of short stalls a shift quietly erode Performance and Availability more than the occasional major failure."
---

**Short answer: the losses that wreck packaging OEE are micro-stops and changeovers at the filler and seamer, and machine learning can predict them early enough to pre-empt them.** Fix the bottleneck and you lift the whole line.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the whiskey production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Predicting Packaging Line Downtime and Lifting OEE</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Distil</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mature</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Bottle</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the whiskey production flow, start to finish.</figcaption>
</figure>

## OEE and where it leaks
Overall Equipment Effectiveness multiplies three things: Availability (is the line running when it should be), Performance (is it running at rated speed), and Quality (is output good first time). One number, three ways to lose. The mistake is to chase Availability alone — chasing big breakdowns — when the real drain is usually Performance, bled away by micro-stops: the five-second stalls that happen dozens of times a shift and barely register individually.

And not every machine matters equally. The filler and seamer, often with the labeller, are the bottleneck; whatever they lose, the line loses. A jam upstream that the buffer absorbs costs nothing. The same jam at the filler costs output directly. So the target is clear before any model is built: micro-stops and changeover losses at the bottleneck.

## Measure first: mining the line control system
The data already exists. The line control system logs stops, durations, fault codes, speeds, and reject counts. The data-science job is to clean it into honest features — stop frequency by station, micro-stop clustering, speed against rated, time-since-changeover, recent fault patterns — because raw logs are noisy, with mislabelled and uncoded stops that flatter or distort the picture.

With clean history, a model learns the signatures that precede a stall: a creeping rise in short stops on the seamer, a vibration or torque drift, the conditions under which a particular changeover runs long. It predicts the next likely loss with enough lead time to intervene — slow the line slightly, swap a worn part at the next break, adjust an infeed — rather than reacting after the stall. You are pre-empting Performance losses, which is where the OEE points hide.

## A copilot for the shift report
The generative-AI angle is the end-of-shift summary nobody enjoys writing. A copilot reads the shift's downtime logs and the model's predictions and produces the OEE summary automatically: the figure, its breakdown into Availability, Performance, and Quality, the top causes of lost time, and a ranked top-three of fixes for the next shift. "Seamer micro-stops cost 22 minutes, concentrated after the 11:00 changeover; recommend checking the infeed timing and replacing the suspect lifter." The handover stops depending on whoever happened to be paying attention.

## Where it breaks
The hard limit is data quality. If operators leave stops uncoded or the control system mislabels faults, the model learns fiction, and the shift report quietly inherits it. Worse, prediction does not equal cause — the model flags rising seamer stops, but the root cause is mechanical, and a maintainer still has to find and fix the worn part. There is no autonomous repair here. Treat predictions as an early warning that buys time, not as a diagnosis, and invest in disciplined downtime coding before trusting any of it.

## The bottom line
Aim at micro-stops and changeovers on the filler and seamer, use the control system's own logs to predict losses before they land, and let a copilot write the OEE summary and top fixes. The maths is simple — Availability times Performance times Quality — but the gains live in clean data and acting at the bottleneck.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [predictive maintenance for the filler and seamer]({{ '/2024/predictive-maintenance-filler-seamer/' | relative_url }}).

## Frequently asked questions

**What is OEE and how is it calculated?**
Overall Equipment Effectiveness is Availability times Performance times Quality. It captures stops, speed losses, and reject rates in one figure, so it shows the true output gap, not just uptime.

**Why focus on the filler and seamer?**
The filler and seamer, and sometimes the labeller, are usually the line bottleneck. Losses there cap the whole line, so a minute saved at the bottleneck is a minute of real extra output.

**What dominates packaging line losses?**
Micro-stops and changeovers, not big breakdowns. Dozens of short stalls a shift quietly erode Performance and Availability more than the occasional major failure.
