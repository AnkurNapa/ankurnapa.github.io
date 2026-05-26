---
layout: post
title: "AI for Filtration and Centrifugation Optimisation"
image: /assets/og/ai-filtration-centrifugation-optimization.png
description: "Optimise centrifuge flow and filter dosing to balance clarity against yield loss, oxygen pickup and filter-aid cost — and predict filter run length."
date: 2023-12-25
updated: 2023-12-25
tags: [brewing-science, process-optimization, clarification]
faq:
  - q: "What trade-offs does clarification involve?"
    a: "Clarity has to be balanced against beer yield loss, oxygen pickup and throughput. Push for brighter beer and you typically lose more product, spend more on filter aid, and risk picking up oxygen — so there is a genuine optimum, not a single best setting."
  - q: "Can a model predict when a filter will block?"
    a: "Yes, given pressure differential, flow and turbidity over a run, a model can estimate remaining run length and warn before throughput collapses. Variable solids load is the main thing that degrades that prediction."
  - q: "How does centrifugation compare with filtration?"
    a: "A disc-stack centrifuge removes solids by sedimentation without filter powder, reducing waste handling, while cross-flow membrane filtration also avoids kieselguhr. The right mix depends on solids load, clarity target and oxygen-pickup risk."
---

**Short answer: model-guided set-points can balance clarity against yield loss, oxygen pickup and filter-aid cost, and predict when a filter will block — turning clarification from a fixed recipe into a tuned operation.** The gains come from respecting the trade-offs, not ignoring them.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">AI for Filtration and Centrifugation Optimisation</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## A balancing act, not a single setting
Clarification spans sedimentation, centrifugation and filtration, and every option trades one good thing against another. A disc-stack centrifuge — whether opening-bowl or decanter — removes solids by sedimentation without filter powder. Filtration ranges from kieselguhr (diatomaceous earth) and sheet filters to membrane and cross-flow systems, with cross-flow avoiding the handling of filter powder altogether.

The tensions are constant: chase brighter beer and you generally lose more yield to the solids stream, dose more filter aid, slow throughput, or risk pulling in oxygen. There is no universally correct setting, only an optimum for a given beer, solids load and clarity target. That is exactly the kind of multi-objective problem where a model earns its place.

## Optimising the set-points
Treated as data, clarification offers plenty to work with: centrifuge feed rate and bowl-opening frequency, filter dosing rate, pressure differential, flow, inlet and outlet turbidity, and the resulting yield and oxygen pickup. Measure these across runs and a model can learn the response surface — how clarity, yield and run length move as you change feed flow or dosing.

Generative optimisation then searches that surface for set-points that hit the clarity target at the lowest cost in yield and filter aid, rather than relying on a fixed standard operating procedure inherited years ago. For filtration specifically, a model tracking the pressure differential over a run can predict blocking and estimate remaining run length, so a brewer plans a change-over instead of being caught when throughput collapses mid-shift.

## Where it breaks
The recurring spoiler is variable solids load. The same beer can arrive at the centrifuge or filter with very different turbidity depending on the fermentation, the yeast strain and how well it flocculated — and a model tuned to a typical load will misjudge an unusually heavy one. Clarification optimisation is only as stable as the upstream process feeding it.

Oxygen pickup is the other hard limit. Pushing flow and clarity can increase contact with air or shear that draws in oxygen, quietly undermining the flavour stability you protected elsewhere. Any optimiser that ignores TPO is optimising the wrong objective — clarity bought with oxygen is a poor trade. So the model must carry oxygen pickup as a real constraint, not an afterthought.

## An assistant for set-points and logs
The generative-AI contribution works at both ends of the shift. Before a run, an assistant recommends flow and dosing set-points for the target clarity and the current solids load, explaining the trade-off it is making. After the run, it auto-drafts the filtration log — volumes, dosing, pressure trend, run length, any blocking event — so the record is complete and consistent without a manual write-up. That removes friction from both the decision and the paperwork that usually gets skipped.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">AI for Filtration and Centrifugation Optimisation</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Process</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

## The bottom line
Filtration and centrifugation are ripe for optimisation precisely because they are full of trade-offs, and a model that respects yield, oxygen pickup and filter-aid cost can do better than a fixed SOP — while predicting run length so change-overs are planned. Keep oxygen as a hard constraint, watch for variable solids load, and remember the brightness you gain must not cost the [colloidal stability]({{ '/2024/predicting-chill-haze-colloidal-stability/' | relative_url }}) you are trying to protect.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*

## Frequently asked questions

**What trade-offs does clarification involve?**
Clarity has to be balanced against beer yield loss, oxygen pickup and throughput. Push for brighter beer and you typically lose more product, spend more on filter aid, and risk picking up oxygen — so there is a genuine optimum, not a single best setting.

**Can a model predict when a filter will block?**
Yes, given pressure differential, flow and turbidity over a run, a model can estimate remaining run length and warn before throughput collapses. Variable solids load is the main thing that degrades that prediction.

**How does centrifugation compare with filtration?**
A disc-stack centrifuge removes solids by sedimentation without filter powder, reducing waste handling, while cross-flow membrane filtration also avoids kieselguhr. The right mix depends on solids load, clarity target and oxygen-pickup risk.
