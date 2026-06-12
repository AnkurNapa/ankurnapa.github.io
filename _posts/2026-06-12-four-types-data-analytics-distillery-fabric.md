---
layout: post
title: "Descriptive, Diagnostic, Predictive, Prescriptive: The Four Analytics in a Distillery"
image: /assets/og/four-types-data-analytics-distillery-fabric.png
description: "The four classic types of data analytics translated into distillery language — spirit yield, cut points, the angel's share, cask allocation — and where Microsoft Fabric's lakehouse, real-time intelligence and Direct Lake actually fit each one."
date: 2026-06-12 09:00:00 -0700
updated: 2026-06-12
tags: [distilling-maturation, process-intelligence, data-strategy, microsoft-fabric, whiskey]
faq:
  - q: "What are the four types of data analytics?"
    a: "Descriptive (what happened — yields, losses, stock), diagnostic (why it happened — tracing a poor spirit yield back through fermentation and mashing), predictive (what will happen — the angel's share a cask will take, when it reaches bottling maturity) and prescriptive (what to do about it — which casks to vat, where to lay down new fill). Each builds on the one before it."
  - q: "How does a distillery use the four types of analytics?"
    a: "Descriptive: litres of pure alcohol per tonne, warehouse stock by age. Diagnostic: why this week's yield dropped — wash gravity, fermentation time, cut decisions. Predictive: per-cask evaporative loss and maturity windows. Prescriptive: recommended cut points, cask purchasing and warehouse placement. The order matters — you cannot prescribe from data you cannot yet describe."
  - q: "Where does Microsoft Fabric fit in distillery analytics?"
    a: "Fabric puts the whole ladder on one platform: OneLake as the single copy of production and warehouse data, eventstreams for live still and tank sensors, notebooks for the predictive models, Power BI on Direct Lake for the dashboards, and Data Activator to turn a prediction into an alert someone actually receives."
---

**Short answer: the four types of analytics are a ladder, not a menu. Descriptive tells you what happened (this week's litres of pure alcohol per tonne). Diagnostic tells you why (the wash gravity was down and the feints cut came early). Predictive tells you what will happen (this cask will lose 2.1% this year and reach its window in 2031). Prescriptive tells you what to do (vat these casks, lay the new fill on the cool ground floor). Each rung stands on the one below — and Microsoft Fabric is interesting to a distillery precisely because it puts the whole ladder on one platform instead of four stitched-together tools.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 360" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The four analytics as a ladder for a distillery: descriptive (what happened), diagnostic (why), predictive (what will happen), prescriptive (what to do), with rising value and rising data demands."><rect width="1000" height="360" fill="#fdfbf7"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#8a5a2b">THE FOUR ANALYTICS — DISTILLERY EDITION</text><g font-family="sans-serif"><rect x="40" y="250" width="220" height="68" rx="8" fill="#f7ece0" stroke="#8a5a2b" stroke-width="1.5"/><text x="150" y="274" text-anchor="middle" font-size="12.5" font-weight="700" fill="#8a5a2b">Descriptive</text><text x="150" y="292" text-anchor="middle" font-size="10.5" fill="#1c1a17">what happened</text><text x="150" y="308" text-anchor="middle" font-size="10" fill="#6b6258">LPA/tonne &#183; stock by age</text><rect x="280" y="200" width="220" height="118" rx="8" fill="#f7ece0" stroke="#8a5a2b" stroke-width="1.5"/><text x="390" y="224" text-anchor="middle" font-size="12.5" font-weight="700" fill="#8a5a2b">Diagnostic</text><text x="390" y="242" text-anchor="middle" font-size="10.5" fill="#1c1a17">why it happened</text><text x="390" y="258" text-anchor="middle" font-size="10" fill="#6b6258">yield drop &#8592; wash gravity</text><rect x="520" y="150" width="220" height="168" rx="8" fill="#f7ece0" stroke="#8a5a2b" stroke-width="1.5"/><text x="630" y="174" text-anchor="middle" font-size="12.5" font-weight="700" fill="#8a5a2b">Predictive</text><text x="630" y="192" text-anchor="middle" font-size="10.5" fill="#1c1a17">what will happen</text><text x="630" y="208" text-anchor="middle" font-size="10" fill="#6b6258">angel's share &#183; maturity</text><rect x="760" y="100" width="220" height="218" rx="8" fill="#7a1f3d"/><text x="870" y="124" text-anchor="middle" font-size="12.5" font-weight="700" fill="#fdfbf7">Prescriptive</text><text x="870" y="142" text-anchor="middle" font-size="10.5" fill="#f7ece0">what to do</text><text x="870" y="158" text-anchor="middle" font-size="10" fill="#f7ece0">cut points &#183; cask placement</text></g><line x1="30" y1="330" x2="970" y2="330" stroke="#6b6258" stroke-width="1.5"/><text x="40" y="350" font-family="sans-serif" font-size="11" fill="#6b6258">hindsight</text><text x="960" y="350" text-anchor="end" font-family="sans-serif" font-size="11" fill="#6b6258">foresight — more value, more data discipline →</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A ladder, not a menu: you cannot prescribe what to do from data you cannot yet describe.</figcaption>
</figure>

This post opens a three-part series on **process intelligence for distilleries** — the gap between having data and having answers on the production floor. Part one is the map: the four classic types of analytics, translated out of consulting-speak into wash, spirit and warehouse language, with an honest look at where Microsoft Fabric's newer capabilities fit. Part two asks [why so many Power BI dashboards die in drinks companies]({{ '/2026/why-power-bi-dashboards-fail-distilleries/' | relative_url }}), and part three is [what changes when the developer has stood at the spirit safe]({{ '/2026/brewer-distiller-power-bi-fabric-developer/' | relative_url }}).

## Descriptive: what happened

The foundation rung, and the one most distilleries genuinely need first. Descriptive analytics is the faithful mirror: litres of pure alcohol per tonne of malt this week against budget; warehouse stock by age band and wood type; fermentation times by washback; losses at each stage from grain intake to filling store. Nothing clever — and enormously valuable, because most operations have never seen their own numbers assembled in one trustworthy place. This is the "see it" rung of [where a distillery starts with AI]({{ '/2026/where-a-distillery-starts-with-ai/' | relative_url }}), and it is where Power BI lives most comfortably.

The IBD-trained instinct matters even here: *which* numbers you describe is a domain decision. A spirit yield figure means nothing until it's normalised per tonne at a stated moisture and extract; a stock figure is bulk litres or litres of pure alcohol, and confusing the two has embarrassed more than one board report.

## Diagnostic: why it happened

The rung where dashboards earn their keep. Yield is down three percent this week — *why?* Diagnostic analytics is the structured walk back up the process: was the original gravity of the wash low (a mashing or malt problem)? Did fermentations finish short (yeast health, temperature)? Did the stillman cut to feints early (and if so, was that judgement or necessity)? The data requirement is unforgiving: you need the **batch genealogy** — this grain lot, through this mash, into these washbacks, through these still charges, into these casks — joined end to end. Without that chain, "why" questions die as arguments in the morning meeting. With it, they become five-minute drill-downs.

## Predictive: what will happen

The rung machine learning lives on, covered in depth across this blog: [the angel's share a cask will take]({{ '/2024/forecasting-whiskey-angels-share/' | relative_url }}) given its wood, fill strength and warehouse position; [when a cask reaches its bottling window]({{ '/2024/predicting-optimal-bottling-maturity/' | relative_url }}); [how congeners will evolve]({{ '/2024/predicting-congener-evolution-maturation/' | relative_url }}). Prediction needs history — measured regauges, not estimates — which is why it sits *above* descriptive and diagnostic, never instead of them. A model trained on a ledger nobody reconciles is [a mirror of bad data]({{ '/2026/what-is-machine-learning-distillery/' | relative_url }}), confidently wrong.

## Prescriptive: what to do

The top rung and the most oversold. Prescriptive analytics turns a prediction into a recommendation: given predicted maturity curves and the blend plan, *these* are the casks to vat this quarter; given microclimate differences, lay the new make down on the cool ground floor and keep the top tier for fast-maturing stock; given energy tariffs, run the stills on this schedule. Done honestly, it's optimisation over predictions you already trust. Done dishonestly, it's a black box telling a stillman where to cut — and the correct response to that is the scepticism it will receive. Prescriptive output should arrive as a *recommendation with its reasoning showing*, owned by a human, especially anywhere near the spirit safe or a compliance number.

## Where Fabric actually fits

Microsoft Fabric's pitch to a distillery is not any single feature — it's that the four rungs stop being four separate products. **OneLake** holds one copy of production, warehouse and sales data instead of extracts scattered across laptops. **Eventstreams and Real-Time Intelligence** take live readings from stills, tanks and warehouse sensors — the IoT layer I covered in [sensors in the distillery]({{ '/2026/iot-in-the-distillery-sensors-process/' | relative_url }}) — without a custom streaming stack. **Notebooks** train the predictive models on the same data the dashboards read, so the model and the report never disagree about what a cask weighs. **Direct Lake** lets Power BI read the lakehouse without nightly refresh gymnastics. And **Data Activator** turns a threshold or a prediction into an alert to the person on shift — which is the difference between analytics and wallpaper. The full catalogue is in [Microsoft Fabric for distilleries: 20 use cases]({{ '/2026/microsoft-fabric-for-distilleries-20-use-cases/' | relative_url }}); the point here is the ladder view: one platform, four rungs, one copy of the truth.

## Where this breaks

The honest section, as always. **The ladder is climbed in order, and most attempts aren't.** A prescriptive cask-allocation engine bought before the regauge history is clean is an expensive way to automate guesswork. **Diagnostic depends on genealogy nobody glamorous wants to build** — the batch-to-cask chain is unsexy integration work, and skipping it caps you at descriptive forever. **Prediction inherits every flaw in the record** — estimates in, confident estimates out. And **prescriptive has a trust ceiling**: a recommendation that can't show its reasoning will be ignored by exactly the experienced people whose judgement it's trying to augment — and they will usually be right to ignore it. The platform doesn't fix any of this; it just removes the excuse that the tools couldn't talk to each other.

## The bottom line

Descriptive, diagnostic, predictive, prescriptive — what happened, why, what's next, what to do. A distillery that climbs in order turns its yield meetings from arguments into drill-downs, its warehouse from a mystery into a forecast, and its planning from instinct-only into instinct-plus-evidence. Fabric's contribution is putting the whole ladder on one platform with one copy of the data. What it cannot do is supply the domain judgement that decides *which* numbers matter and *whether* they can be trusted — and that gap is exactly where most dashboard projects in this industry quietly die. That's [the next post]({{ '/2026/why-power-bi-dashboards-fail-distilleries/' | relative_url }}).

## Frequently asked questions

**What are the four types of data analytics?**
Descriptive (what happened — yields, losses, stock), diagnostic (why it happened — tracing a poor spirit yield back through fermentation and mashing), predictive (what will happen — the angel's share a cask will take, when it reaches bottling maturity) and prescriptive (what to do about it — which casks to vat, where to lay down new fill). Each builds on the one before it.

**How does a distillery use the four types of analytics?**
Descriptive: litres of pure alcohol per tonne, warehouse stock by age. Diagnostic: why this week's yield dropped — wash gravity, fermentation time, cut decisions. Predictive: per-cask evaporative loss and maturity windows. Prescriptive: recommended cut points, cask purchasing and warehouse placement. The order matters — you cannot prescribe from data you cannot yet describe.

**Where does Microsoft Fabric fit in distillery analytics?**
Fabric puts the whole ladder on one platform: OneLake as the single copy of production and warehouse data, eventstreams for live still and tank sensors, notebooks for the predictive models, Power BI on Direct Lake for the dashboards, and Data Activator to turn a prediction into an alert someone actually receives.
