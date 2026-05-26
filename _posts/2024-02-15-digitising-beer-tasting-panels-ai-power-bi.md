---
layout: post
title: "Digitising Beer Tasting Panels: Power Apps, Power BI, and AI"
image: /assets/og/digitising-beer-tasting-panels-ai-power-bi.png
description: "How breweries can digitise tasting panels with a Power Apps capture app, Power BI analytics, and AI fault and drift detection — without losing the palate."
date: 2024-02-15
updated: 2024-02-15
tags: [brewing-science, tasting, power-apps, power-bi]
faq:
  - q: "Do I need the full Microsoft stack to digitise my tasting panel?"
    a: "No. A well-structured spreadsheet beats messy software, and many small breweries are fine staying there. Move to Power Apps and Power BI when paper or spreadsheets stop scaling — multiple tasters, several sessions a week, and a real need to link results to batches."
  - q: "Can AI replace the tasting panel?"
    a: "No. AI and dashboards don't taste. The calibrated human panel stays the instrument; the stack captures, structures, analyses, and communicates what the panel produces. AI flags drift and faults and drafts notes — it doesn't make the call."
  - q: "What should I get right before adding dashboards?"
    a: "The basics of sensory science: a consistent attribute list and scales, a screened and calibrated panel, and a clean data model that keys every session to a batch or lot. Dashboards built on inconsistent data just visualise the mess faster."
---

**Short answer: replace the clipboard with a tablet, key every score to a batch, and let the analytics surface drift and faults — but keep the calibrated panel as the instrument.** Most breweries already run a tasting panel. Far fewer can answer a simple question: did bitterness drift above spec across this quarter's brews, and which taster flagged it first?

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Digitising Beer Tasting Panels: Power Apps, Power BI, and AI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Why paper and spreadsheets quietly cost you
A paper score sheet is fast to start and slow to learn from. Scores get transcribed (or don't), sessions sit in separate files, and the link between a tasting result and the actual batch in the brewhouse is a memory rather than a record. When a customer complaint arrives, you cannot easily pull every panel result for that lot.

The fix is not a research-grade sensory suite. It is structured capture. A **Power Apps** canvas app on **Dataverse** lets panellists score samples on a phone or tablet at the bench — picking the sample, rating attributes on the house scale, noting faults from a controlled list. It works offline in a cold cellar and syncs later, so you are not chained to Wi-Fi. The point is that the data is clean and structured the moment it is entered, not a week later.

## Anchor every session to the batch in ERP
Tasting data is only useful in context. The context lives in your **ERP** — Dynamics 365 Business Central or similar — which already holds your products, recipes, batches and lots, and suppliers. When the capture app references the batch or lot record, each session becomes part of the grain-to-glass trail.

That link is what turns tasting from a ritual into a release control. A panel result tied to a lot supports the pass, hold, or reject decision and gives you traceability when something goes wrong. You can ask the data which malt shipment, which yeast pitch, or which fermenter correlates with an off-note — because the keys are all there.

## Turn scores into trends in Power BI
Once capture and master data are sorted, **Power BI** does the visible work. Useful views for a brewing panel include:

- **Attribute trends** — how bitterness, body, ester character, or DMS track across brews of the same beer over time.
- **Control charts vs spec** — each attribute plotted against your house range, so drift is obvious before it becomes a complaint.
- **Panellist agreement and variance** — where the panel agrees, where it splits, and which taster sits consistently high or low.

Because the data is keyed to lots from ERP, every chart drills back to a specific batch. The Copilot in Power BI lets you ask in plain language — "show me batches where bitterness drifted above spec this quarter" — and get a chart back, though you should always sanity-check what it returns.

## Where AI helps, and where it can't
This is where **machine learning** earns its place — narrowly. Trained on enough scored sessions, models can flag panellist **drift** (a taster whose ratings creep over months), screen for unusual results, and help flag likely **faults**: diacetyl, acetaldehyde, DMS, or staling markers like T2N. Calibrating against flavour standards — spiked diacetyl around 0.10 mg/L, acetaldehyde near 10 mg/L — keeps the panel honest, and the model learns from that calibrated baseline. Further out, you can predict sensory attributes from instrument data such as NIR, using the panel to validate, not replace, the prediction.

Here is the honest limit. **AI and dashboards don't taste.** They detect patterns in numbers the panel produced. If the panel is uncalibrated or the attribute list is inconsistent, the model learns noise. The calibrated human palate is the instrument; everything in the stack captures, structures, analyses, and communicates its output. And for a small brewery running one beer and a weekly panel, a tidy spreadsheet may be all the rigour you need — the licensing and governance overhead of the Power Platform only pays back at scale.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="The model sorts each sample into a class from its measured features."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">CLASSIFICATION</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Digitising Beer Tasting Panels: Power Apps, Power BI, and AI</text><rect x="120" y="120" width="150" height="120" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="195" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b45309">Class A</text><circle cx="145" cy="145" r="6" fill="#b45309"/><circle cx="177" cy="145" r="6" fill="#b45309"/><circle cx="209" cy="145" r="6" fill="#b45309"/><rect x="330" y="120" width="150" height="120" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="405" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#5b7a1f">Class B</text><circle cx="355" cy="145" r="6" fill="#5b7a1f"/><circle cx="387" cy="145" r="6" fill="#5b7a1f"/><circle cx="419" cy="145" r="6" fill="#5b7a1f"/><circle cx="451" cy="145" r="6" fill="#5b7a1f"/><rect x="540" y="120" width="150" height="120" rx="8" fill="#f7ece0" stroke="#7a1f3d" stroke-width="1.5"/><text x="615" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">Class C</text><circle cx="565" cy="145" r="6" fill="#7a1f3d"/><circle cx="597" cy="145" r="6" fill="#7a1f3d"/><circle cx="629" cy="145" r="6" fill="#7a1f3d"/><circle cx="661" cy="145" r="6" fill="#7a1f3d"/><circle cx="565" cy="175" r="6" fill="#7a1f3d"/><text x="360" y="92" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">new sample → sorted into the best-fit class</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The model sorts each sample into a class from its measured features.</figcaption>
</figure>

## The bottom line
Digitising a beer tasting panel is mostly an exercise in discipline: consistent attributes, a calibrated panel, and a clean data model that ties scores to lots. Power Apps captures it, ERP anchors it, Power BI reveals the trends, and AI flags what deserves a second sniff. **Generative AI** can then draft a consistent house-style tasting note or a QC release summary from the structured scores — reviewed by a human before it ships. None of it tastes for you; that is still the panel's job.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [AI and taster calibration]({{ '/2024/ai-sensory-panel-taster-calibration/' | relative_url }}) and [whiskey tasting with Power Apps and Power BI]({{ '/2024/whiskey-tasting-ai-power-apps-power-bi/' | relative_url }}).

## Frequently asked questions

**Do I need the full Microsoft stack to digitise my tasting panel?**
No. A well-structured spreadsheet beats messy software, and many small breweries are fine staying there. Move to Power Apps and Power BI when paper or spreadsheets stop scaling — multiple tasters, several sessions a week, and a real need to link results to batches.

**Can AI replace the tasting panel?**
No. AI and dashboards don't taste. The calibrated human panel stays the instrument; the stack captures, structures, analyses, and communicates what the panel produces. AI flags drift and faults and drafts notes — it doesn't make the call.

**What should I get right before adding dashboards?**
The basics of sensory science: a consistent attribute list and scales, a screened and calibrated panel, and a clean data model that keys every session to a batch or lot. Dashboards built on inconsistent data just visualise the mess faster.
