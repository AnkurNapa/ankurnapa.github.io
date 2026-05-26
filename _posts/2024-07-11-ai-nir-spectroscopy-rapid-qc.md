---
layout: post
title: "AI + NIR Spectroscopy for Rapid Brewery QC"
image: /assets/og/ai-nir-spectroscopy-rapid-qc.png
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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">AI + NIR Spectroscopy for Rapid Brewery QC</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">AI + NIR Spectroscopy for Rapid Brewery QC</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Process</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

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
