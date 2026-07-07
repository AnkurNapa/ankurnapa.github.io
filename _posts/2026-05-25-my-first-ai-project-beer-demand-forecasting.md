---
layout: post
title: "My First Real AI Project: Forecasting Beer Demand — What Worked, What Flopped"
image: /assets/og/my-first-ai-project-beer-demand-forecasting.png
description: "An honest postmortem of building beer demand forecasting at iWort — where machine learning beat the spreadsheet, where it didn't, and the data lessons that cost me the most."
date: 2026-05-25 16:00:00 -0700
updated: 2026-05-25
tags: [brewer-to-ai, demand-forecasting, machine-learning, iwort]
faq:
  - q: "Can AI forecast beer demand?"
    a: "Yes, for established beers with stable, seasonal demand and enough clean sales history. It struggles with new releases and one-off events, where it often does no better than a careful human estimate."
  - q: "Was machine learning better than a spreadsheet for demand forecasting?"
    a: "Only sometimes. For high-volume, many-SKU, seasonal cases, ML added real value. For small catalogs and new products, a simple seasonal spreadsheet was within a few percent — at zero cost and full transparency."
  - q: "What's the hardest part of a brewery forecasting project?"
    a: "The data, not the model. Inconsistent sales records, products that didn't exist last year, and demand driven by events the model never saw are what break forecasts in practice."
---

**Short answer: my first serious AI project was beer demand forecasting — predicting which beers to make, and how much, so breweries sell at the right time and place. It worked genuinely well for established, seasonal products with clean history. It flopped on new releases and one-off events, where a simple spreadsheet held its own. The hard part was never the model; it was the data.** Here's the honest postmortem.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="From raw data to a decision the team can act on — the pipeline behind this post."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DATA → DECISION</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">My First Real AI Project: Forecasting Beer Demand — What Worked, What Flopped</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Data</text><text x="90.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">sensors, logs</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Features</text><text x="289.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">clean &amp; shape</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Model</text><text x="488.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">train / score</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Prediction</text><text x="687.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">what happens next</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Action</text><text x="886.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">the team acts</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">From raw data to a decision the team can act on — the pipeline behind this post.</figcaption>
</figure>

## The problem worth solving

Demand forecasting is one of the highest-value things a brewery can get right: over-produce and you pour money down the drain; under-produce and you miss sales. It's the problem I built around at **iWort** — making AI/data forecasting affordable for craft and commercial breweries so they can match supply to real demand.

It's also a problem where you have data you already collect: sales history. That made it the right first project.

## What worked

For beers with a track record — year-round products, clear seasonality, enough clean sales history — machine learning earned its place. It picked up patterns across weather, day-of-week, holidays, and promotions that a person juggling spreadsheets simply can't hold in their head. For multi-SKU, higher-volume operations, that's real money saved.

## What flopped

The honest part. The model was weakest exactly where I most wanted help:

- **New releases** had no history, so the model fell back to generic guesses — sometimes worse than a brewer's gut.
- **One-off events** — a festival, a viral moment, a heatwave — were invisible to it. It can only learn from what it has seen.
- **Thin data overfit.** Give a flexible model too little history and it "learns" noise, then forecasts it back to you with total confidence.

I dig into when forecasting is and isn't worth it in [AI demand forecasting for breweries]({{ '/2026/ai-demand-forecasting-for-breweries/' | relative_url }}). The short version: sometimes a seasonal spreadsheet was within a few percent of the model — free, transparent, and good enough.

## The lesson that stuck

The model was maybe 20% of the work. The other 80% was wrangling messy sales data and being honest about what the forecast could and couldn't see. My biggest early mistake was trusting a confident number from thin data. That mistake — and a few worse ones — is the subject of the next post.

*From Brewer to AI — Part 5 of 8. [Full series]({{ '/series/brewer-to-ai/' | relative_url }}) · [Next: Where AI burned me →]({{ '/2026/where-ai-burned-me/' | relative_url }})*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="History (solid) and the model&#39;s forward forecast (dashed); the shaded band is its uncertainty."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FORECAST</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">My First Real AI Project: Forecasting Beer Demand — What Worked, What Flopped</text><g stroke="#06483f" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#00695c" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#00695c" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#06483f" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">today</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">history</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">forecast</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">History (solid) and the model&#39;s forward forecast (dashed); the shaded band is its uncertainty.</figcaption>
</figure>

## Frequently asked questions

**Can AI forecast beer demand?**
Yes, for established beers with stable, seasonal demand and enough clean sales history. It struggles with new releases and one-off events, where it often does no better than a careful human estimate.

**Was machine learning better than a spreadsheet for demand forecasting?**
Only sometimes. For high-volume, many-SKU, seasonal cases, ML added real value. For small catalogs and new products, a simple seasonal spreadsheet was within a few percent — at zero cost and full transparency.

**What's the hardest part of a brewery forecasting project?**
The data, not the model. Inconsistent sales records, products that didn't exist last year, and demand driven by events the model never saw are what break forecasts in practice.
