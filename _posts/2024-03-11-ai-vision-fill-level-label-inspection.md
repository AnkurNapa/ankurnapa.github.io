---
layout: post
title: "AI Vision for Fill-Level and Label Inspection"
image: /assets/og/ai-vision-fill-level-label-inspection.png
description: "How machine vision inspects fill height, label skew, and date-code legibility at line speed, rejecting beer defects more consistently than human spot checks."
date: 2024-03-11
updated: 2024-03-11
tags: [brewing-science, packaging, computer-vision]
faq:
  - q: "What can machine vision inspect on a packaging line?"
    a: "Fill level or height, label presence, skew and print quality, cap and crown seating, and date-code legibility. It checks every container at line speed rather than a sampled few."
  - q: "Is vision inspection better than human checks?"
    a: "For repetitive, high-speed checks, yes. It is faster and more consistent than human spot checks, which sample only a fraction of containers and tire over a shift."
  - q: "What makes a vision system fail?"
    a: "Lighting changes, glare, condensation, and biased training data. Edge cases the system has never seen, such as a new label or an unusual defect, are where it struggles most."
---

**Short answer: machine vision checks fill height, labels, caps, and date codes on every container at line speed, more consistently than a human spot-checking a sample.** It catches defects you would otherwise ship.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the whiskey production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">AI Vision for Fill-Level and Label Inspection</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Distil</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mature</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Bottle</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the whiskey production flow, start to finish.</figcaption>
</figure>

## What a camera catches that a person misses
Human inspection on a fast line is sampling, not inspecting. A person glances at a fraction of containers, gets tired, and applies a judgement that drifts across a shift. Machine vision looks at every unit. Fill-level or height inspection rejects under- and over-fills; label inspection flags missing, skewed, or poorly printed labels; cap and crown checks confirm seating; date-code reading confirms the code is present and legible. The defect is rejected at speed, before it reaches a pallet.

The consistency is the point as much as the speed. A vision system applies the same threshold to the first container and the hundred-thousandth, which is exactly what a quality standard is supposed to mean and exactly what human spot checks cannot deliver.

## Measure first: it is a data problem in disguise
A camera is a sensor, and a vision system is a model trained on data. The "measure first" discipline applies hard here. You need representative images of good product and of the defects you care about — low fills, lifted labels, smeared codes — across the lighting and product variation the line actually sees. The data-science work is curating that set so the model learns the real decision boundary rather than a shortcut.

Get this wrong and the failure is quiet. Train only on pristine daytime samples and the system stumbles when condensation films a chilled bottle or a glossy label throws glare. The features that matter — contrast at the fill line, label edge geometry, character legibility against background — have to be learned from images that span normal variation, or the model is confident exactly when it should not be.

## A vision-language model for reports and new artwork
The generative-AI angle is twofold. First, a vision-language model can auto-write the defect report: not just "reject," but "label skewed roughly eight degrees, lower-left lifted, batch trending worse since 13:00 — check the label applicator's vacuum." That turns a reject count into something a line lead can act on. Second, the same class of model adapts to new label artwork from only a handful of examples, instead of the lengthy re-training a classic vision system needs at every seasonal SKU change. For a brewery cycling through limited releases, that cuts the changeover pain that usually makes vision feel rigid.

## Where it breaks
The limits are the ones every vision deployment meets. Lighting and presentation drift — glare, condensation, a shifted camera — degrade accuracy silently, so the rig needs stable lighting and monitoring. Training bias means the system only reliably catches defects resembling what it has seen; a genuinely novel fault can sail through. Edge cases, oddly shaped containers, partial occlusion, an unusual reflection, are where rejects and false rejects cluster. Tune the false-reject rate too tight and you bin good product; too loose and defects escape. It is a tool that needs calibration and the occasional human audit, not a fire-and-forget box.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A vision model locates and labels features in each image, then scores them."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">COMPUTER VISION</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">AI Vision for Fill-Level and Label Inspection</text><rect x="80" y="80" width="360" height="180" rx="6" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><rect x="120" y="120" width="110" height="90" fill="none" stroke="#2e9e7c" stroke-width="2.5"/><rect x="270" y="150" width="120" height="70" fill="none" stroke="#00695c" stroke-width="2.5"/><text x="120" y="114" font-family="sans-serif" font-size="11" font-weight="700" fill="#2e9e7c">ok</text><text x="270" y="144" font-family="sans-serif" font-size="11" font-weight="700" fill="#00695c">flag</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="450" y1="170" x2="500" y2="170"/><polygon points="500,163 512,170 500,177" stroke="none"/></g><rect x="525" y="140" width="150" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600" y="176" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">label + score</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A vision model locates and labels features in each image, then scores them.</figcaption>
</figure>

## The bottom line
Vision inspects every container for fill, labels, caps, and date codes faster and more evenly than human sampling, and a vision-language model can write the defect report and adapt to new artwork from a few examples. Feed it representative images, control the lighting, and audit the edge cases — then it earns its place on the line.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [predicting packaging line downtime and lifting OEE]({{ '/2024/packaging-line-oee-downtime-prediction/' | relative_url }}).

## Frequently asked questions

**What can machine vision inspect on a packaging line?**
Fill level or height, label presence, skew and print quality, cap and crown seating, and date-code legibility. It checks every container at line speed rather than a sampled few.

**Is vision inspection better than human checks?**
For repetitive, high-speed checks, yes. It is faster and more consistent than human spot checks, which sample only a fraction of containers and tire over a shift.

**What makes a vision system fail?**
Lighting changes, glare, condensation, and biased training data. Edge cases the system has never seen, such as a new label or an unusual defect, are where it struggles most.
