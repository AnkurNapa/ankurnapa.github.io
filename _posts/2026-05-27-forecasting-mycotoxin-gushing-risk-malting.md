---
layout: post
title: "Forecasting Mycotoxin and Gushing Risk in the Malthouse"
image: /assets/og/forecasting-mycotoxin-gushing-risk-malting.png
description: "Fusarium-infected barley brings DON mycotoxin and gushing risk. How machine learning scores incoming lots from harvest weather and grain data — and why a food-safety call keeps a human in the loop."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
tags: [brewing-science, malting, food-safety, machine-learning]
faq:
  - q: "What is gushing in beer?"
    a: "Gushing is the spontaneous over-foaming of beer the moment a pack is opened, with no obvious shaking or fault. Primary gushing is driven by hydrophobin proteins from Fusarium mould on the barley, which stabilise tiny carbon-dioxide bubbles; it traces back to field infection, not to the brewery."
  - q: "What is DON and why does it matter in malting?"
    a: "DON (deoxynivalenol) is a mycotoxin produced by Fusarium fungi on cereals. It is a food-safety hazard with regulatory limits, it largely survives malting and brewing, and the same field infection that raises DON often raises gushing risk — so it is screened at barley intake."
  - q: "Can AI predict mycotoxin or gushing risk?"
    a: "It can rank the risk. A model using harvest weather during flowering, region, variety susceptibility and grain inspection or near-infrared data flags high-risk lots for testing or rejection. It is a triage tool, not a substitute for the DON assay, because contamination is patchy and the cost of a miss is high."
---

**Short answer: you can forecast the *risk*, not the *result*. Fusarium infection in the field produces both DON mycotoxin and the hydrophobins that cause beer to gush, so a model fed harvest weather, region, variety susceptibility and grain-inspection data can rank incoming barley lots from low to high risk and route them to test, segregate or reject. That triage is genuinely useful — it focuses expensive assays where they matter. But contamination is patchy and the cost of a missed lot is a food-safety recall, so the model screens; the laboratory and a human decide.**

DON and gushing are the two malthouse problems that start before the barley ever arrives: both are sown in a warm, wet flowering window months earlier. By intake the damage is done and unevenly spread through the lot, which is what makes them both a forecasting problem and a sampling nightmare.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 250" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Incoming barley lots scored by a risk model and routed to accept, segregate and test, or reject">
<rect x="0" y="0" width="760" height="250" fill="#fdfbf7"/>
<text x="380" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Intake triage — score, then route</text>
<rect x="40" y="95" width="150" height="60" rx="6" fill="#f7ece0" stroke="#6b6258"/>
<text x="115" y="120" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">incoming lot</text>
<text x="115" y="138" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">weather · variety · NIR</text>
<rect x="270" y="95" width="150" height="60" rx="6" fill="#b45309"/>
<text x="345" y="122" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#fdfbf7">risk score</text>
<text x="345" y="140" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#fdfbf7">low · med · high</text>
<line x1="190" y1="125" x2="262" y2="125" stroke="#6b6258" stroke-width="2"/>
<polygon points="270,125 260,120 260,130" fill="#6b6258"/>
<g>
<rect x="500" y="50" width="220" height="40" rx="6" fill="#5b7a1f" fill-opacity="0.15" stroke="#5b7a1f"/>
<text x="610" y="75" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">accept</text>
<rect x="500" y="105" width="220" height="40" rx="6" fill="#b45309" fill-opacity="0.15" stroke="#b45309"/>
<text x="610" y="130" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">segregate &amp; assay DON</text>
<rect x="500" y="160" width="220" height="40" rx="6" fill="#7a1f3d" fill-opacity="0.15" stroke="#7a1f3d"/>
<text x="610" y="185" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">reject / divert</text>
</g>
<line x1="420" y1="120" x2="500" y2="72" stroke="#6b6258" stroke-width="1.5"/>
<line x1="420" y1="125" x2="500" y2="125" stroke="#6b6258" stroke-width="1.5"/>
<line x1="420" y1="130" x2="500" y2="178" stroke="#6b6258" stroke-width="1.5"/>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The model does not pass or fail a lot; it sorts lots so the lab assay and the human decision land where the risk is highest.</figcaption>
</figure>

## Where gushing and DON come from

Both trace to *Fusarium* head blight, a fungal infection of the cereal ear favoured by warm, humid weather during flowering. The fungus produces **deoxynivalenol (DON)**, a mycotoxin that is a regulated food-safety hazard and largely survives malting and brewing into the finished beer. The same infection deposits **hydrophobins** — small surface-active proteins that cling to carbon-dioxide bubbles and stabilise them, so the beer erupts when the pack is opened (primary gushing). Crucially, this is a *field* problem, not a brewery one: by the time the barley reaches the malthouse you are managing inherited risk, deciding which lots to trust.

## A risk score at intake

The model is a classic risk-ranking task. Features that genuinely carry signal: weather during the crop's flowering window (rainfall, humidity, temperature), growing region and field history, variety susceptibility, and grain-inspection or near-infrared (NIR) readings at intake that hint at fungal damage. Train on past lots labelled with their measured DON and any gushing incidents, and the model outputs a risk grade per delivery. You then act on the grade: accept the low-risk lots, segregate and assay the medium ones, divert the high-risk ones to a non-food use or back to the supplier. The point is not to skip the DON test — it is to aim it.

## The data and a generative reporting layer

This lives or dies on data discipline: tying each delivery to its agronomic origin, its NIR scan and, eventually, its laboratory DON result, so the model keeps learning. A generative-AI layer then does the unglamorous but real work of food-safety paperwork — drafting the HACCP note for a segregated lot, summarising "why was lot 88 flagged?" against the weather and region for the supplier conversation, and letting a quality manager query the season's intake risk in plain language. It complements existing [food-safety traceability from grain to glass]({{ '/2025/food-safety-traceability-grain-to-glass/' | relative_url }}) rather than replacing the assay or the auditor.

## Where a miss is expensive

This is the post where "where it breaks" matters most, because the failure mode is a safety failure. **Contamination is heterogeneous** — DON concentrates in pockets, so a lot can pass a sample and still carry a hot spot, and a model trained on lot-average labels cannot resolve what the sampling itself missed. **Gushing is multifactorial**: hydrophobins are the main primary cause, but carbonation, metal ions, calcium oxalate and packaging all contribute, so a clean barley risk score does not guarantee a calm pack. And the asymmetry is brutal — a false negative that lets a high-DON lot through is far costlier than a false positive that wastes an assay, so the model must be tuned to over-refer, and a human must own the release decision. Treat the score as the reason to test, never the reason not to.

## The bottom line

AI earns its place in the malthouse as a triage tool for inherited risk: it ranks incoming barley for DON and gushing potential and points your testing where it counts. It does not clear a lot — heterogeneous contamination and multifactorial gushing make that the lab's and the quality manager's job. Keep the assay in the loop, bias the model toward caution, and let it make your sampling smarter, not your safety thinner.

## Frequently asked questions

**What is gushing in beer?**
Gushing is the spontaneous over-foaming of beer the moment a pack is opened, with no obvious shaking or fault. Primary gushing is driven by hydrophobin proteins from Fusarium mould on the barley, which stabilise tiny carbon-dioxide bubbles; it traces back to field infection, not to the brewery.

**What is DON and why does it matter in malting?**
DON (deoxynivalenol) is a mycotoxin produced by Fusarium fungi on cereals. It is a food-safety hazard with regulatory limits, it largely survives malting and brewing, and the same field infection that raises DON often raises gushing risk — so it is screened at barley intake.

**Can AI predict mycotoxin or gushing risk?**
It can rank the risk. A model using harvest weather during flowering, region, variety susceptibility and grain inspection or near-infrared data flags high-risk lots for testing or rejection. It is a triage tool, not a substitute for the DON assay, because contamination is patchy and the cost of a miss is high.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
