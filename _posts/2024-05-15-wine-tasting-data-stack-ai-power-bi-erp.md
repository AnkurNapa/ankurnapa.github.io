---
layout: post
title: "Wine Tasting Meets the Data Stack: AI, Power BI, and ERP"
image: /assets/og/wine-tasting-data-stack-ai-power-bi-erp.png
description: "Tie tasting and bench-trial scores to vintage, block, lot, and barrel in ERP, analyse in Power BI, and use AI to predict and flag faults — palate still decides."
date: 2024-05-15
updated: 2024-05-15
tags: [winemaking, tasting, power-bi, erp]
faq:
  - q: "Where does the tasting data actually live?"
    a: "In Dataverse, captured through a Power Apps app, with every score keyed to the lot, block, vintage, or barrel record held in your ERP. That link is what gives the result context and traceability — and what lets Power BI compare like with like."
  - q: "Can AI predict wine quality from analysis?"
    a: "It can predict sensory attributes from instrument data such as NIR or FTIR with chemometrics, and flag likely faults — useful as a screen. It cannot judge quality or balance. The winemaker's palate decides; the model points you at what to taste first."
  - q: "Is this overkill for a small winery?"
    a: "Often, yes. If you make a handful of lots a year, a clean spreadsheet keyed to your lot numbers may be enough. The data stack earns its keep when you have many lots, blend trials, and barrels to track across vintages."
---

**Short answer: the value is not in the tasting note — it's in tying every score to the lot, block, vintage, and barrel so you can compare, blend, and trace with confidence.** A tasting score floating free of its lot is an opinion. The same score keyed to a barrel and a vintage is a decision input.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the wine production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Wine Tasting Meets the Data Stack: AI, Power BI, and ERP</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Harvest</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Crush / press</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Age</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Bottle</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the wine production flow, start to finish.</figcaption>
</figure>

## Master data first: the cellar runs on keys
Winemaking is already a data problem — you just track it on whiteboards and in your head. Vintage, block, lot, barrel, additions, trial blends: each is a record, and the relationships between them are what matter. Your **ERP** (Dynamics 365 Business Central, Finance & Operations, or a wine-specific system) is the natural home for that master data — products, lots, vintages, barrels, suppliers, and inventory.

The discipline that makes everything downstream work is **data science** in its least glamorous form: a consistent attribute list, calibrated scales, and clean keys. Before any model or dashboard, every tasting and bench-trial score must reference a real lot or barrel. Get that right and the rest is mostly plumbing.

## Capture at the bench, not back at the desk
Bench trials and tasting sessions happen in the cellar, often with wet hands and no signal. A **Power Apps** app on **Dataverse** lets you and the panel score on a tablet — pick the lot or trial blend, rate structure, fruit, oak, and faults on the house scale, log the result against the barrel. It captures offline and syncs later. The score lands structured and linked, rather than as a scribble to be transcribed (and misremembered) next week.

This matters most for blend trials, where you are comparing many small permutations under time pressure. Structured capture means you can actually reconstruct which trial won and why.

## Analyse and decide in Power BI
With scores keyed to lots, **Power BI** turns the panel's work into decisions:

- **Lot comparisons** — rank and contrast lots on the attributes that drive your style.
- **Blend decisions** — see how trial blends score across attributes, with the contributing lots one click away.
- **Fault tracking** — monitor flagged faults across the cellar and across vintages, so a creeping problem shows up early.

Because the data inherits its context from ERP, every visual drills back to a barrel or block. The Copilot in Power BI answers plain-language questions — "which lots scored highest on fruit but flagged volatile acidity this vintage?" — and returns a chart you then verify.

## What AI adds — and where it stops
**Machine learning** has two solid roles here. First, predicting sensory outcomes from instrument data: NIR or FTIR readings plus chemometrics can estimate attributes and prioritise which lots to taste, with the panel validating the prediction. Second, fault flagging — surfacing likely **Brett** (4-EP/4-EG), **volatile acidity**, **TCA**, or oxidation from the data so the panel knows where to focus. Clustering can also group lots by flavour profile to inform blending.

The limit is firm. **AI and dashboards don't taste.** A model can tell you a lot looks chemically consistent with Brett; only the panel confirms whether the wine is faulted and unsaleable. The winemaker's palate decides on balance, typicity, and house style; the stack organises and communicates what the palate produces. Push the model past that line and you will eventually release a wine a dashboard liked and a person wouldn't.

There is a cost angle too. Power Platform licensing is per user or per app, and a clean data model takes governance effort. For a small producer, that overhead may not pay back — a disciplined spreadsheet keyed to lot numbers can carry you a long way.

## The bottom line
Wine tasting meets the data stack when scores stop being notes and start being keyed records. ERP holds the master data, Power Apps captures the scores in the cellar, Power BI turns them into blend and release decisions, and AI predicts and flags so the panel tastes the right things first. **Generative AI** can draft a house-style tasting note or answer questions over the cellar data — human-reviewed, always. The palate stays in charge.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [can AI predict wine quality?]({{ '/2026/can-ai-predict-wine-quality/' | relative_url }}) and [detecting wine faults: Brett, VA, TCA]({{ '/2024/detecting-wine-faults-brett-va-tca/' | relative_url }}).

## Frequently asked questions

**Where does the tasting data actually live?**
In Dataverse, captured through a Power Apps app, with every score keyed to the lot, block, vintage, or barrel record held in your ERP. That link is what gives the result context and traceability — and what lets Power BI compare like with like.

**Can AI predict wine quality from analysis?**
It can predict sensory attributes from instrument data such as NIR or FTIR with chemometrics, and flag likely faults — useful as a screen. It cannot judge quality or balance. The winemaker's palate decides; the model points you at what to taste first.

**Is this overkill for a small winery?**
Often, yes. If you make a handful of lots a year, a clean spreadsheet keyed to your lot numbers may be enough. The data stack earns its keep when you have many lots, blend trials, and barrels to track across vintages.
