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
