---
layout: post
title: "Planning for CO2 Shortages With Predictive Models"
image: /assets/og/planning-co2-shortages-predictive.png
description: "Forecast CO2 demand against fermentation recovery and supply to size buffers and recovery investment — a lesson sharpened by the 2022 supply crunch."
date: 2022-01-14
updated: 2022-01-14
tags: [brewing-science, planning, sustainability]
faq:
  - q: "How can predictive models help with CO2 supply?"
    a: "By forecasting how much CO2 you will need for purging, carbonation and packaging, and comparing that against the CO2 your fermentations recover and what you can buy, models help you size buffer storage and decide whether recovery investment pays off."
  - q: "Can a model predict a CO2 shortage?"
    a: "It can predict your own demand and recovery fairly well because those follow your production schedule, but external supply shocks like the 2022 crunch are driven by markets and outages that are genuinely hard to forecast. The realistic goal is resilience, not perfect prediction."
  - q: "Is recovering fermentation CO2 worth it?"
    a: "It depends on your volumes, demand pattern and the capital cost of recovery equipment. A forecast of demand versus recovery potential is exactly the input that makes that business case clear rather than a guess."
---

**Short answer: you can forecast your own CO2 demand and fermentation recovery accurately enough to size buffers and justify recovery kit — but external supply shocks stay hard to predict.** The 2022 crunch made that gap impossible to ignore.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Planning for CO2 Shortages With Predictive Models</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Why CO2 is a planning problem
CO2 sits on both sides of a brewery's ledger. Fermentation produces it — and that CO2 can be recovered and reused. At the same time, breweries buy CO2 for purging vessels, carbonating beer and packaging. So you are simultaneously a producer and a consumer of the same gas, and the two flows rarely line up neatly with each other or with what suppliers can deliver.

That is fundamentally a forecasting and balancing problem, and it maps cleanly onto data you already hold. Your production schedule drives demand: how many vessels you will purge, how much beer you will carbonate, how much you will package. Your fermentation volumes drive recovery potential. Put those together and you have the makings of a CO2 balance you can project forward.

## What to model, and how
Start by measuring, because you cannot plan against numbers you have never captured — the same discipline that applies to any AI effort, as covered in [collect your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}). Track CO2 purchased, CO2 used per process step, and the CO2 your fermentations generate.

With that history, a demand forecast is a fairly standard time-series and scheduling problem: future brews and packaging runs translate into future CO2 draw. Layer recovery potential on top — driven by fermentation volume and timing — and you get a projected net position over the coming weeks. From there the planning questions become concrete. How big a buffer of stored CO2 do you need to ride out a delivery gap? At what production scale does on-site recovery pay back its capital cost? Those are decisions a forecast turns from gut-feel into a sized, defensible number.

## Where it breaks: shocks and capex
Here is the honest limit. Your internal flows are predictable because they follow your own schedule, but the external supply side is not. The 2022 crunch was driven by upstream plant outages and market dynamics far outside any brewery's data. No model trained on your production history will see that coming, and pretending otherwise is dangerous.

So the goal shifts from prediction to resilience. Use the forecast to know your demand precisely and to right-size buffers and recovery so a supply gap is survivable, not catastrophic. The other limit is capital: recovery equipment is a real investment, and the forecast tells you whether your volumes justify it — for a small producer the answer may honestly be no, and a larger buffer plus supplier diversification is the better bet.

A generative-AI assistant adds value here by turning the forecast into a plan: "Given a two-week supply interruption next month, here is your projected shortfall, the buffer you'd draw down, and the carbonation runs to reschedule first." It converts a numeric projection into a contingency playbook people can actually follow under pressure.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 320" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A continuous cycle — each step feeds the next, then round again."><rect x="0" y="0" width="720" height="320" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">THE CYCLE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Planning for CO2 Shortages With Predictive Models</text><circle cx="360" cy="190" r="95" fill="none" stroke="#d8e6e1" stroke-width="1.5" stroke-dasharray="5 5"/><circle cx="360" cy="95" r="34" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360" y="100" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">Plan</text><circle cx="455" cy="190" r="34" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="455" y="195" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">Do</text><circle cx="360" cy="285" r="34" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360" y="290" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">Check</text><circle cx="265" cy="190" r="34" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="265" y="195" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">Act</text><circle cx="428" cy="140" r="4" fill="#00695c"/><circle cx="410" cy="258" r="4" fill="#00695c"/><circle cx="292" cy="240" r="4" fill="#00695c"/><circle cx="310" cy="122" r="4" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A continuous cycle — each step feeds the next, then round again.</figcaption>
</figure>

## The bottom line
Predictive models genuinely help with CO2 because demand and recovery follow your production schedule, which is data you can capture and project. That lets you size buffers and build a clear case for recovery investment. What they cannot do is foresee external supply shocks — so plan for resilience, measure your flows first, and let a gen-AI assistant turn the forecast into a contingency plan.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [what can AI do for a brewery]({{ '/2026/what-can-ai-do-for-a-brewery/' | relative_url }}).

## Frequently asked questions

**How can predictive models help with CO2 supply?**
By forecasting how much CO2 you will need for purging, carbonation and packaging, and comparing that against the CO2 your fermentations recover and what you can buy, models help you size buffer storage and decide whether recovery investment pays off.

**Can a model predict a CO2 shortage?**
It can predict your own demand and recovery fairly well because those follow your production schedule, but external supply shocks like the 2022 crunch are driven by markets and outages that are genuinely hard to forecast. The realistic goal is resilience, not perfect prediction.

**Is recovering fermentation CO2 worth it?**
It depends on your volumes, demand pattern and the capital cost of recovery equipment. A forecast of demand versus recovery potential is exactly the input that makes that business case clear rather than a guess.
