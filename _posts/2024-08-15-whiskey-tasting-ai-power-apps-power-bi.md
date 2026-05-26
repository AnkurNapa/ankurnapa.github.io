---
layout: post
title: "Whiskey Tasting, Captured and Analysed: Power Apps, Power BI, and AI"
image: /assets/og/whiskey-tasting-ai-power-apps-power-bi.png
description: "Capture cask-sample and vatting scores in Power Apps linked to ERP, track maturation in Power BI, and use AI to cluster casks and flag off-notes — nose still decides."
date: 2024-08-15
updated: 2024-08-15
tags: [distilling-maturation, tasting, power-apps, power-bi]
faq:
  - q: "How do I track a cask's flavour over years of maturation?"
    a: "Capture each cask-sample tasting in a Power Apps app keyed to the cask record in ERP, then chart the attribute history in Power BI. Over time you build a flavour trajectory per cask — invaluable for deciding when to vat, extend, or move spirit."
  - q: "Can AI pick the casks for a vatting?"
    a: "It can cluster casks by flavour profile and flag outliers or off-notes, which narrows the field fast. It cannot decide the blend. The master blender's nose remains the instrument; AI organises the candidates and the data behind them."
  - q: "What's the catch with using AI in long maturation?"
    a: "Feedback is slow. A cask matures for years, so models learn from sparse, lagging data, and any prediction carries real uncertainty. Treat AI output as a prompt to nose the right casks, never as a substitute for the sample."
---

**Short answer: capture every cask sample as a structured, keyed record, and you build a flavour trajectory per cask that makes vatting decisions evidence-led — but the master blender's nose still picks the blend.** Maturation is the slowest feedback loop in beverage production. The casks that aren't measured consistently are the ones that surprise you at vatting.

## The problem: years of samples, no memory
A distillery noses casks for years before they are vatted. If each sample lives on a paper sheet or in a one-off spreadsheet, the history is effectively lost — you remember the standout casks and forget the trajectory of the rest. When it is time to build a vatting, you are working from recent impressions rather than the cask's full story.

The aim is a clean, continuous record per cask. Not a research instrument — just consistent capture, keyed to the cask, every time someone draws a sample.

## Capture at the warehouse, keyed to the cask
A **Power Apps** app on **Dataverse** lets the team score cask samples and vatting trials on a tablet in the warehouse — select the cask, rate the maturation attributes on the house scale (oak, spice, fruit, sulphur, off-notes), and log it. It works offline among the racks and syncs later.

Crucially, each score references the cask and batch record held in **ERP** (Dynamics 365 Business Central or similar), alongside fill date, wood type, previous fill, and spirit. That link gives you grain-to-glass traceability and ties the sensory history to the physical asset. A tasting result is no longer a note; it is part of the cask's record and supports the decision to vat, hold, or extend.

## See maturation move in Power BI
**Power BI** is where the slow story becomes visible:

- **Flavour over time per cask** — attribute trajectories across years of sampling, so you can see a cask developing or stalling.
- **Cross-cask comparison** — contrast casks of the same fill or wood type, surfacing the consistent performers and the outliers.
- **Off-note tracking** — monitor flagged faults across the warehouse before they spread through a vatting.

Because every point is keyed to a cask in ERP, the charts drill back to the physical asset. The Copilot in Power BI fields plain-language questions — "which first-fill casks gained spice fastest this year?" — returning a chart to verify.

## AI: cluster the casks, flag the off-notes
**Machine learning** suits this data well once you have enough of it. Clustering groups casks by flavour profile, which is a genuine head start when assembling a vatting from hundreds of candidates. Models can flag off-notes and outliers — sulphur, excessive wood, oxidation — so the team noses the casks that matter. Where you have instrument data, models can help predict attributes, with sampling used to validate.

The honest limits are sharper here than in beer or wine. **AI and dashboards don't taste.** Clustering proposes candidates; the master blender's nose composes the vatting and judges balance and house character. And maturation's slow feedback loop means models train on sparse, lagging data — a prediction about a cask three years out carries real uncertainty. Use AI to prioritise which casks to nose, never to replace the sample. For a small distillery with a few hundred casks, a disciplined spreadsheet keyed to cask numbers may be all you need; the Power Platform's per-user licensing and governance only pay back at scale.

## The bottom line
Whiskey tasting becomes an asset when every cask sample is a structured, keyed record rather than a fading memory. Power Apps captures it in the warehouse, ERP anchors it to the cask, Power BI reveals the maturation trajectory, and AI clusters profiles and flags off-notes. **Generative AI** can then draft consistent house-style tasting notes and a first-draft blend rationale from the scores — reviewed by the team. The nose still decides; the stack remembers everything else.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.* Related: [AI tasting notes for beer, wine, and whiskey]({{ '/2026/ai-tasting-notes-beer-wine-whiskey/' | relative_url }}) and [building a digital tasting program]({{ '/2024/digital-tasting-program-power-platform-erp-genai/' | relative_url }}).

## Frequently asked questions

**How do I track a cask's flavour over years of maturation?**
Capture each cask-sample tasting in a Power Apps app keyed to the cask record in ERP, then chart the attribute history in Power BI. Over time you build a flavour trajectory per cask — invaluable for deciding when to vat, extend, or move spirit.

**Can AI pick the casks for a vatting?**
It can cluster casks by flavour profile and flag outliers or off-notes, which narrows the field fast. It cannot decide the blend. The master blender's nose remains the instrument; AI organises the candidates and the data behind them.

**What's the catch with using AI in long maturation?**
Feedback is slow. A cask matures for years, so models learn from sparse, lagging data, and any prediction carries real uncertainty. Treat AI output as a prompt to nose the right casks, never as a substitute for the sample.
