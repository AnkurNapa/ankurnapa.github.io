---
layout: post
title: "AI for Vineyard Yield Forecasting"
image: /assets/og/ai-vineyard-yield-forecasting.png
description: "How AI forecasts vineyard yield from bunch counts, berry weight, NDVI remote sensing, and weather — to plan tanks, barrels, and sales — and why vintage weather still breaks the model."
date: 2024-04-05
updated: 2024-04-05
tags: [winemaking, viticulture, forecasting]
faq:
  - q: "How accurate is AI yield forecasting?"
    a: "Good enough to plan tanks and sales, not good enough to bet the vintage on. Errors widen the further you forecast from harvest, and a frost or poor fruit set can swamp any model."
  - q: "What inputs drive a yield forecast?"
    a: "Bunch counts per vine, berry and bunch weight, historical block yields, NDVI canopy maps from satellite or drone, and weather through flowering and set."
  - q: "Can I forecast yield without remote sensing?"
    a: "Yes. Disciplined bunch counts, berry weights, and a few years of block history get you most of the way. NDVI mainly helps you sample smarter and map variability within a block."
---

**Short answer: AI sharpens vineyard yield forecasts enough to plan tanks, barrels, and sales — but vintage weather can still blow the estimate apart, so forecast in ranges, not points.** Yield is the number every downstream decision hangs on, and most cellars still guess it.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the wine production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">AI for Vineyard Yield Forecasting</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Harvest</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Crush / press</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Age</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Bottle</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the wine production flow, start to finish.</figcaption>
</figure>

## Why a yield number drives the whole season
Get yield wrong and the costs compound. Under-forecast and you scramble for tank space or sell fruit you could have vinified; over-forecast and you commit barrels, packaging, and sales orders against wine that never arrives. Yield forecasting underpins tank and barrel planning, picking logistics, and the sales commitments you make months before harvest. A forecast that lands within a sensible range, early enough to act on, is worth real money.

Traditionally this is bunch counts times bunch weight times a lag factor, adjusted by gut feel. AI does not throw that out — it formalises it, learns each block's historical behaviour, and folds in signals a clipboard cannot.

## Measure first: the inputs that matter
A useful model is built on a few solid data streams. Bunch counts per vine and representative berry and bunch weights give you the core estimate. Several seasons of block-level historical yields let the model learn each parcel's typical output and its sensitivity to conditions. NDVI from satellite or drone maps canopy vigour, so you can see variability within a block and target your sampling where it counts rather than walking every row. Weather through flowering and fruit set — the window that decides how many berries actually set — is often the single biggest swing factor.

The discipline matters more than the algorithm. If you have never built this habit, start with [collect your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}): a few seasons of consistent counts and weights beats a sophisticated model fed on one afternoon's sampling.

## Where it breaks
Vintage weather is the great humbler of yield models. A spring frost, a cold snap during flowering that wrecks fruit set, or a midsummer heat event can change actual yield by tens of percent — and these are precisely the events models forecast worst, because they are rare and abrupt. A model trained on five "normal" vintages has little to say about the freak one.

Ground-truth data is the other weakness. Bunch counts are labour-intensive, so most cellars sample sparsely, and small samples in a variable block produce wide error bars. Block-to-block and within-block variability means a single average hides a lot. The honest move is to forecast as a range with a stated confidence, widen the range early in the season, and tighten it as harvest approaches and the fruit is on the vine where you can actually count it.

## How generative AI fits in
Two angles are genuinely useful here. First, natural-language querying: instead of digging through spreadsheets, a winemaker asks "expected tonnes for block 7 this vintage, and how does that compare to last year?" and a generative layer over the vineyard data answers in plain English with the assumptions shown. Second, auto-drafted reporting: at the end of each sampling round the system writes a yield report — block by block, with the estimate, the range, the main risks (set, frost exposure, disease pressure), and what changed since the last round. That saves the viticulturist an afternoon and gives the sales and operations teams a document they can actually plan against. The generative layer does not improve the forecast; it makes the forecast usable by everyone who needs it.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="History (solid) and the model&#39;s forward forecast (dashed); the shaded band is its uncertainty."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FORECAST</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">AI for Vineyard Yield Forecasting</text><g stroke="#06483f" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#00695c" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#00695c" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#06483f" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">today</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">history</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">forecast</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">History (solid) and the model&#39;s forward forecast (dashed); the shaded band is its uncertainty.</figcaption>
</figure>

## The bottom line
AI yield forecasting turns scattered counts, canopy maps, and weather into a planning number you can run a season on — provided you treat it as a range and respect what frost and poor fruit set can do to it. Invest in disciplined ground-truth sampling first, forecast in ranges, and let a generative layer make the numbers easy to query and report.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [Collect your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}).

## Frequently asked questions

**How accurate is AI yield forecasting?**
Good enough to plan tanks and sales, not good enough to bet the vintage on. Errors widen the further you forecast from harvest, and a frost or poor fruit set can swamp any model.

**What inputs drive a yield forecast?**
Bunch counts per vine, berry and bunch weight, historical block yields, NDVI canopy maps from satellite or drone, and weather through flowering and set.

**Can I forecast yield without remote sensing?**
Yes. Disciplined bunch counts, berry weights, and a few years of block history get you most of the way. NDVI mainly helps you sample smarter and map variability within a block.
