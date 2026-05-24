---
layout: post
title: "AI + NIR Spectroscopy for Rapid Brewery QC"
description: "How NIR/FTIR spectroscopy plus chemometrics predicts alcohol, extract, pH, bitterness and colour in seconds for fast in-process brewery quality control."
date: 2024-07-11
updated: 2024-07-11
tags: [brewing-science, quality-control, sensors]
faq:
  - q: "What can NIR predict in a single scan?"
    a: "Once calibrated, NIR or FTIR can predict alcohol, original and real extract, pH, bitterness and colour — and sometimes diacetyl precursors — in seconds from one scan, replacing several slower lab methods."
  - q: "How accurate is spectroscopy versus the lab?"
    a: "It is only as good as its calibration. Built against solid reference lab methods using PLS regression, it is fast and reliable in-process; a weak calibration gives confident but wrong numbers."
  - q: "What is the main ongoing challenge?"
    a: "Calibration transfer and drift. Instruments age and recipes change, so calibrations need periodic checks against the reference lab and may not move cleanly between machines."
---

**Short answer: NIR or FTIR plus chemometrics predicts alcohol, extract, pH, bitterness and colour in seconds from one scan — so QC moves from the lab queue to the process line, provided the calibration is sound.** Speed is the prize; calibration is the catch.

## One scan, many numbers
Traditional QC measures parameters one method at a time — a titration here, a spectrophotometer reading there — each adding hours to the feedback loop. Near-infrared (NIR), FTIR and MIR spectroscopy collapse that. A single scan captures a spectrum, and a calibrated model reads multiple parameters from it at once: alcohol, original and real extract, pH, bitterness and colour, sometimes even diacetyl precursors.

The "AI" here is chemometrics — specifically partial least squares (PLS) regression. It learns the relationship between the spectrum and the lab-measured values, then predicts those values for any new scan. This is the data-science discipline behind the speed, and it lives or dies on the quality of its training data.

## Measure first, calibrate properly
The phrase "measure first, model second" is literal in spectroscopy. You build a calibration by scanning samples and pairing each spectrum with a trusted reference lab measurement — the established titration, distillation or spectrophotometric method. PLS then maps spectrum to value. The reference methods do not disappear; they become the ground truth the model is judged against.

A good calibration covers the full range you will see in practice — across styles, strengths and colours — so the model interpolates rather than extrapolates. Get that right and a brewer scans a fermenting tank or a finished beer and reads extract, alcohol and pH in seconds, catching a drifting attenuation or an off-spec batch while there is still time to act.

## Where it breaks
This is the honest part. **Calibration build is real work** — you need enough reference-paired samples spanning the variation you care about, and that takes time and lab effort up front. **Calibration transfer** is awkward: a model built on one instrument may not move cleanly to another, so a second machine often needs its own work. **Drift** is the ongoing tax: instruments age, lamps degrade and recipes evolve, so a calibration that was excellent last year may quietly slip. The blunt rule is garbage calibration, garbage prediction — a poorly built model returns confident numbers that are simply wrong, which is more dangerous than no number at all. Schedule reference checks and treat the calibration as a living asset.

## The generative layer
The gen-AI angle sits on top of the predictions, not inside them. A QC copilot watches the stream of scans, flags any that fall out of spec, and explains why in context — "extract higher than target for this style; attenuation tracking low." For batches that pass, it drafts the QC release note: parameters measured, specifications met, instrument and calibration version used. The brewer reviews and signs rather than transcribes. Crucially, the copilot does not invent measurements; it interprets and documents what the calibrated model produced, keeping the human in the release decision.

## The bottom line
NIR and FTIR with PLS chemometrics turn multi-parameter QC from an hours-long lab queue into a seconds-long in-process check. The value is entirely contingent on calibration: build it against good reference methods, manage transfer and drift, and verify regularly. Add a generative copilot to flag out-of-spec scans and draft release notes, and QC becomes both faster and better documented.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [AI quality control in brewing]({{ '/2026/ai-quality-control-in-brewing/' | relative_url }}).

## Frequently asked questions

**What can NIR predict in a single scan?**
Once calibrated, NIR or FTIR can predict alcohol, original and real extract, pH, bitterness and colour — and sometimes diacetyl precursors — in seconds from one scan, replacing several slower lab methods.

**How accurate is spectroscopy versus the lab?**
It is only as good as its calibration. Built against solid reference lab methods using PLS regression, it is fast and reliable in-process; a weak calibration gives confident but wrong numbers.

**What is the main ongoing challenge?**
Calibration transfer and drift. Instruments age and recipes change, so calibrations need periodic checks against the reference lab and may not move cleanly between machines.
