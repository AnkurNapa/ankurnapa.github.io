---
layout: post
title: "AI for Brewery Energy and Utilities (Steam, Refrigeration, CO2)"
image: /assets/og/ai-brewery-energy-utilities-optimization.png
description: "How AI optimises brewery energy — steam, refrigeration, compressed air and CO2 recovery — by forecasting demand, shifting load and spotting drift."
date: 2024-06-09
updated: 2024-06-09
tags: [brewing-science, energy, process-optimization]
faq:
  - q: "Which brewery loads should I target first with AI?"
    a: "Start with the biggest: steam for the boil, refrigeration and glycol for fermentation cooling and cold storage, then compressed air and CO2 recovery. Those four account for most of your utility spend, so model them before anything smaller."
  - q: "What energy benchmarks should I track per hectolitre?"
    a: "Track thermal and electrical energy per hl and your water-to-beer ratio (hl water per hl beer). Better breweries push the water ratio toward roughly 3-4:1; energy figures vary widely, so trend your own site rather than chase a single industry number."
  - q: "Do I need new hardware before AI helps with energy?"
    a: "Usually yes. Without sub-metering on the main loads, a model is guessing. Fit meters first, then layer on forecasting and load-shifting — and budget separately for heat-recovery capital."
---

**Short answer: AI cuts brewery energy cost by forecasting demand, shifting load off peak, and catching drift on your biggest utilities — but only after you sub-meter them.** The prize is in the boil, the glycol, the air and the CO2, not the office lights.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">AI for Brewery Energy and Utilities (Steam, Refrigeration, CO2)</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Follow the energy, not the hype
A brewery's utility bill is lopsided. Thermal energy — mostly gas or steam — goes into the boil. Electrical energy is dominated by refrigeration and glycol for fermentation cooling and cold storage. Compressed air and CO2 recovery sit behind those. If you want AI to pay for itself, point it at those four loads and ignore the rest until they are under control.

The principle is measure first, model second. A model that forecasts steam demand for tomorrow's brew schedule, or predicts glycol load from the fermentation plan, lets you pre-heat hot-liquor tanks, stage compressors, and avoid running refrigeration flat-out at the worst tariff hour. None of that works if you cannot see the loads. Sub-metering the boil, the refrigeration plant and the air compressors is the unglamorous first step.

## What the models actually do
Three jobs, in order of payback.

**Forecast demand.** A time-series model trained on brew schedules, ambient temperature and tank states predicts steam and cooling demand hours ahead. That turns reactive firing into planned operation.

**Shift load.** Once you can forecast, you can move flexible loads — cold storage pull-down, CO2 compression, hot-liquor heating — into cheaper or greener windows. Load-shifting cuts cost without cutting output.

**Spot drift.** This is the quiet winner. Models flag when specific energy per hl creeps up: a fouling vapour condenser, a refrigeration compressor losing efficiency, an air leak. Drift detection finds money that benchmarking alone misses, because it compares the plant to itself.

Heat recovery underpins all three. A vapour condenser on the boil and well-managed hot-liquor tanks recover thermal energy you are otherwise venting; CO2 from fermentation can be captured and reused instead of bought. AI schedules these assets to match demand — but the recovery hardware is capital you have to commit to first.

## Where it breaks
Be honest about the limits. No model invents savings that the physics does not allow — if you have no heat-recovery kit, software cannot recover heat. Sub-metering is a real cost and takes weeks to commission. Forecasts degrade when your production schedule is chaotic or last-minute, because the model has nothing stable to learn from. And load-shifting only helps if your tariff or carbon signal actually varies; a flat-rate site sees little benefit from time-shifting alone. Treat AI as the optimiser on top of good engineering, not a substitute for it.

## The generative layer
Here is the genuinely new angle: a natural-language energy dashboard. Instead of digging through trends, an operator asks "where did last week's steam go?" and a generative model queries the historian, attributes consumption to brews and CIP cycles, and answers in plain English. The same tool auto-drafts the monthly energy report — consumption per hl, variance versus plan, the three biggest drift events — so your engineer reviews a draft rather than building one from scratch. It is a reporting and triage aid, not a control system; the optimisation still comes from the forecasting and load-shifting models underneath.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">AI for Brewery Energy and Utilities (Steam, Refrigeration, CO2)</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Process</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

## The bottom line
Energy is a brewery's most controllable hidden cost, and it concentrates in four loads. Sub-meter them, forecast demand, shift flexible load, and let the models flag drift before it becomes a bill. Generative tools then make the data legible to the people who run the plant. Start with metering — everything else compounds from there.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [AI for wort boiling energy]({{ '/2023/ai-wort-boiling-energy-optimization/' | relative_url }}).

## Frequently asked questions

**Which brewery loads should I target first with AI?**
Start with the biggest: steam for the boil, refrigeration and glycol for fermentation cooling and cold storage, then compressed air and CO2 recovery. Those four account for most of your utility spend, so model them before anything smaller.

**What energy benchmarks should I track per hectolitre?**
Track thermal and electrical energy per hl and your water-to-beer ratio (hl water per hl beer). Better breweries push the water ratio toward roughly 3-4:1; energy figures vary widely, so trend your own site rather than chase a single industry number.

**Do I need new hardware before AI helps with energy?**
Usually yes. Without sub-metering on the main loads, a model is guessing. Fit meters first, then layer on forecasting and load-shifting — and budget separately for heat-recovery capital.
