---
layout: post
title: "Minimising Total Package Oxygen (TPO) With Data"
image: /assets/og/minimizing-total-package-oxygen-tpo.png
description: "Use data and ML to model total package oxygen from filler settings, hit tens-of-ppb TPO targets, and protect beer flavour and shelf life."
date: 2024-03-25
updated: 2024-03-25
tags: [brewing-science, packaging, oxygen]
faq:
  - q: "What is total package oxygen and why does it matter?"
    a: "TPO is the sum of headspace oxygen and dissolved oxygen in the sealed package. It is the master driver of oxidative staling — the cardboard T2N note — so brewers target levels in the tens of ppb to protect shelf life."
  - q: "Can a model really predict TPO from filler settings?"
    a: "Yes, within limits. CO2 jetting, fobbing, fill height, and line speed explain most of the variation, so a model trained on those features plus measured TPO predicts the likely outcome well. It will not catch every intermittent spike."
  - q: "How does generative AI help with oxygen pickup?"
    a: "A copilot can trace a TPO excursion to a specific setting — say, weak fobbing at high line speed — and draft the corrective action and a short note for the shift log, so the fix is consistent across operators."
---

**Short answer: TPO is predictable, and the levers that move it live on the filler — so model headspace and dissolved oxygen against your filler settings and you can hold tens-of-ppb targets shift after shift.** Oxygen is the slow poison of packaged beer, and most of it is picked up in the final seconds before the package seals.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the whiskey production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Minimising Total Package Oxygen (TPO) With Data</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Distil</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mature</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Bottle</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the whiskey production flow, start to finish.</figcaption>
</figure>

## Why TPO sits at the centre of shelf life
Total package oxygen is headspace oxygen plus dissolved oxygen in the sealed container. It is the single biggest driver of oxidative staling — the wet-cardboard flavour from trans-2-nonenal — which is why good packaging halls chase targets measured in tens of parts per billion. A few ppb extra does not show on day one; it shows three months out, in the trade, where you cannot fix it.

The hard part is that TPO is a small number produced by a fast, noisy process. Pickup happens in the splash and turbulence of fill, in the air left in the headspace, and in how cleanly the package seals. Get a handle on those, and you control the number.

## Measure first, then model
Before any model, you need clean measurement. TPO is measured per package, and the reading carries real variance — sampling position, instrument warm-up, and operator technique all move it. Pull a disciplined sample (multiple heads, across the run) and log it against the conditions that produced it.

The useful features are the ones you can actually turn: CO2 jetting or pre-evacuation, fobbing intensity, fill height and tightness, line speed, and product dissolved oxygen arriving from the bright tank. With a few weeks of paired data — settings in, TPO out — a straightforward regression or gradient-boosted model will tell you which levers matter most on your line and predict the TPO a given setup will deliver. That turns oxygen from a post-mortem into a set-point you choose.

The same model flags drift. If predicted TPO is fine but measured TPO climbs, something physical has changed — a tired fobbing jet, a worn valve seal, CO2 supply pressure sagging — and you investigate the machine, not the recipe.

## Where it breaks
Two honest limits. First, measurement variance: TPO instruments and sampling are noisy at the tens-of-ppb level, so a single bad reading is not a trend. Build decisions on rolling samples, not one package. Second, intermittent spikes: a model trained on steady-state settings will under-predict transient events — a fobber misfiring on one head, a momentary fill fault, a stop-start that lets air in. These are real and they damage shelf life, but they are sparse and bursty, so the model is a guide, not a guarantee. Keep physical checks and per-head sampling alongside it.

A model also cannot fix a process that is structurally leaky. If your dissolved oxygen is already high arriving at the filler, no amount of jetting saves you — fix the upstream first.

## Closing the loop with a copilot
This is where generative AI earns its place. When a TPO excursion fires, a copilot fuses the filler settings, line speed, and recent measurements and explains the most likely cause in plain language — "headspace O2 up on heads 3 and 7; CO2 jetting pressure dropped 12% in the last hour" — then drafts the corrective step and a handover note. The diagnosis stays consistent whoever is on shift, and the fix is logged automatically rather than living in someone's memory.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives oxygen control, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Minimising Total Package Oxygen (TPO) With Data</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Oxygen control</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">quality</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">What drives oxygen control, and what it changes downstream.</figcaption>
</figure>

## The bottom line
TPO is small, costly, and controllable. Measure it honestly per package, model it against the filler levers you can actually move, and use a copilot to turn excursions into fast, consistent fixes. Just respect the limits: trust trends over single readings, and keep watching for the intermittent spikes a steady-state model will miss.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [controlling dissolved oxygen with ML]({{ '/2024/controlling-dissolved-oxygen-beer-ml/' | relative_url }}) and [predicting flavour stability and staling]({{ '/2023/predicting-beer-flavor-stability-staling/' | relative_url }}).

## Frequently asked questions

**What is total package oxygen and why does it matter?**
TPO is the sum of headspace oxygen and dissolved oxygen in the sealed package. It is the master driver of oxidative staling — the cardboard T2N note — so brewers target levels in the tens of ppb to protect shelf life.

**Can a model really predict TPO from filler settings?**
Yes, within limits. CO2 jetting, fobbing, fill height, and line speed explain most of the variation, so a model trained on those features plus measured TPO predicts the likely outcome well. It will not catch every intermittent spike.

**How does generative AI help with oxygen pickup?**
A copilot can trace a TPO excursion to a specific setting — say, weak fobbing at high line speed — and draft the corrective action and a short note for the shift log, so the fix is consistent across operators.
