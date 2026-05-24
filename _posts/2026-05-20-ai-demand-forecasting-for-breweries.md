---
layout: post
title: "AI Demand Forecasting for Breweries: Useful, Until It Isn't"
image: /assets/og/ai-demand-forecasting-for-breweries.png
description: "When AI demand forecasting actually beats a spreadsheet for breweries — and the cases where it overfits, wastes money, and a simple moving average wins."
date: 2026-05-20
updated: 2026-05-20
tags: [demand-forecasting, machine-learning, reality-check]
faq:
  - q: "Does AI demand forecasting work for breweries?"
    a: "It works well for established beers with stable, seasonal demand and enough sales history. It works poorly for new releases, limited drops, and anything driven by one-off events — and in those cases it often does worse than a simple human estimate."
  - q: "Is AI forecasting better than a spreadsheet?"
    a: "Often not. For many breweries a moving-average or seasonal spreadsheet forecast is within a few percent of an ML model, at zero cost and full transparency. ML earns its keep only with many SKUs, complex seasonality, and clean data."
  - q: "Why do AI demand forecasts fail?"
    a: "The common failures are too little history, overfitting to noise, and demand driven by external events (a festival, a viral post, weather) the model never saw. Forecasts also silently rot when buying patterns shift."
---

**Short answer: AI demand forecasting genuinely helps breweries with many products and stable, seasonal demand — but for new releases, limited drops, and small catalogs it routinely loses to a simple spreadsheet. It overfits, it can't see one-off events, and it costs real money to run. Use it where the complexity is real, not by default.** Here's the honest map.

## Where it actually works

AI forecasting shines when the conditions favor it:

- **Many SKUs** — dozens of beers where manual forecasting doesn't scale.
- **Stable, repeating demand** — year-round beers with clear seasonal patterns.
- **Years of clean sales data** — enough signal to learn from.
- **Multiple drivers** — weather, day-of-week, promotions, holidays interacting.

In that setting, a model can shave waste and stockouts in ways a human juggling spreadsheets can't.

## Where it quietly fails

This is the part the demos skip:

1. **New and limited releases.** No history means nothing to learn from. The model falls back to generic guesses — often worse than a brewer's gut.
2. **Overfitting to noise.** Give a flexible model thin data and it "learns" random blips as if they were patterns, producing confident, wrong forecasts.
3. **External shocks.** A festival, a viral post, a heatwave, a competitor closing — the model never saw these and can't anticipate them.
4. **Silent rot.** Demand patterns drift. A model trained last year keeps forecasting last year's world until someone notices the misses.

## The spreadsheet you're underrating

For a surprising number of breweries, a **seasonal moving average** — last year's same-month sales, adjusted for trend — lands within a few percent of an ML model. It's free, transparent, and nobody has to maintain a data pipeline. The honest question isn't "can AI forecast this?" but **"does AI beat my spreadsheet by enough to justify the cost?"** Often it doesn't.

## The cost nobody prices in

An ML forecast carries ongoing overhead: data plumbing, retraining, monitoring for drift, and someone who understands it. If that cost exceeds the inventory savings — which it can for a small brewery — the "smart" forecast is a net loss. This is the inefficiency trap covered in [the honest limits of AI in brewing]({{ '/2026/the-honest-limits-of-ai-in-brewing/' | relative_url }}).

## How to decide

1. **Start with a spreadsheet forecast.** Measure its error honestly.
2. **Only escalate to ML if** that error is costing real money *and* you have the SKUs and data to justify it.
3. **Always keep a human sanity check** for new products and known events the model can't see.

## The bottom line

AI demand forecasting is a sharp tool for the right brewery and expensive theater for the wrong one. It's one of the seven use cases in [what AI can do for a brewery]({{ '/2026/what-can-ai-do-for-a-brewery/' | relative_url }}) — valuable, but only when the complexity is real and the data supports it.

## Frequently asked questions

**Does AI demand forecasting work for breweries?**
It works well for established beers with stable, seasonal demand and enough sales history. It works poorly for new releases, limited drops, and anything driven by one-off events — and in those cases it often does worse than a simple human estimate.

**Is AI forecasting better than a spreadsheet?**
Often not. For many breweries a moving-average or seasonal spreadsheet forecast is within a few percent of an ML model, at zero cost and full transparency. ML earns its keep only with many SKUs, complex seasonality, and clean data.

**Why do AI demand forecasts fail?**
The common failures are too little history, overfitting to noise, and demand driven by external events the model never saw. Forecasts also silently rot when buying patterns shift.
