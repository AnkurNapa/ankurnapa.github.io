---
layout: post
title: "Forecasting the Angel's Share: Modelling Cask Evaporation Loss"
description: "How AI and data science forecast the angel's share, the ~2%/year cask evaporation loss, to plan fill volumes and value maturing whisky stock."
date: 2024-09-11
updated: 2024-09-11
tags: [distilling-maturation, whiskey, inventory]
faq:
  - q: "How much whisky is lost to the angel's share?"
    a: "Roughly 2% of the cask volume per year, though it varies with warehouse temperature and humidity, climate, cask size and position. Over a long maturation that compounds into a substantial share of the original fill."
  - q: "Can a model forecast evaporation loss accurately?"
    a: "It can forecast the average loss across a warehouse well, because the drivers are physical and repeatable. Per-cask precision is harder, since position, wood and seal vary cask to cask and weighing data is usually sparse."
  - q: "What data do I need to forecast the angel's share?"
    a: "Cask fill volumes and strengths, cask type and size, position in the warehouse, and periodic weights or dips. Warehouse temperature and humidity logs make the forecast considerably more reliable."
---

**Short answer: the angel's share is predictable enough to plan around, because evaporation is driven by physics you can measure, even if any single cask still surprises you.** Model the loss and you fill, forecast yield and value stock with far less guesswork.

## A 2% problem that compounds
Maturing spirit loses volume to evaporation through the wood, the angel's share, at roughly 2% per year. That sounds small until it compounds. Over a decade or two it removes a meaningful fraction of the original fill, and because it varies with warehouse temperature and humidity, climate, cask size and position, the loss is uneven and hard to predict cask by cask. A warm, dry rackhouse loses spirit faster; a cool, damp dunnage warehouse loses less but shifts strength differently.

This is not just shrinkage. It changes how much you can bottle, when a cask falls below a viable fill or strength, and what your maturing stock is actually worth. Get the forecast wrong and you over- or under-fill years in advance, with no way to correct it later.

## Turning physics into a forecast
The drivers of evaporation are physical, which is exactly why a model can learn them. Measure first: log warehouse temperature and humidity by zone and height, record cask type, size, fill strength and position, and weigh or dip casks periodically. Those features feed a model that predicts loss rate as a function of conditions, rather than applying a flat 2% to everything.

At the warehouse level the forecasts are genuinely useful, because the strong drivers, climate, cask size, warehouse zone, repeat year after year. The model tells you how much spirit a given fill will yield at the target age, so you can plan fill volumes to hit a release and value the maturing inventory with a real loss curve instead of a rule of thumb. Tie that into how you select casks and manage maturing-stock capital, covered in [AI for cask selection and inventory]({{ '/2024/ai-cask-selection-inventory/' | relative_url }}), and the forecast stops being an accounting curiosity and becomes a planning lever.

## Where the forecast frays
The honest limit is the individual cask. Position, wood quality, seal integrity and prior contents vary, so two neighbouring casks filled the same day can lose at noticeably different rates. The model nails the average and the warehouse total; it is much weaker predicting which specific cask will lose the most.

Two data problems make this worse. Weighing every cask is labour, so most distilleries weigh infrequently and sparsely, leaving the model short of the very signal it needs. And the horizons are long: a forecast over fifteen or twenty years extrapolates well past the conditions in your data, and a warming climate quietly invalidates the historical loss rates the model learned from. Treat long-range forecasts as ranges, not points, and re-fit them as fresh weights come in.

## A copilot for the inventory note
The generative angle is practical rather than glamorous. A copilot can take the model's loss projections and draft the inventory note finance actually reads: projected stock losses by warehouse and vintage, the casks approaching minimum viable fill, and the yield implications for next year's bottling plan, written in plain language with the assumptions stated. That saves the analyst hours and, more importantly, makes the forecast legible to people who will never open the model. The microclimate that drives much of this variation is itself optimisable; see [rackhouse microclimate optimisation]({{ '/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}).

## The bottom line
You can forecast the angel's share well at the warehouse and vintage level, and that is enough to plan fills, project yield and value maturing stock with confidence. Per-cask precision and multi-decade horizons remain genuinely hard, so model the average, weigh more often than you do now, and quote ranges for the long bets.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.*

## Frequently asked questions

**How much whisky is lost to the angel's share?**
Roughly 2% of the cask volume per year, though it varies with warehouse temperature and humidity, climate, cask size and position. Over a long maturation that compounds into a substantial share of the original fill.

**Can a model forecast evaporation loss accurately?**
It can forecast the average loss across a warehouse well, because the drivers are physical and repeatable. Per-cask precision is harder, since position, wood and seal vary cask to cask and weighing data is usually sparse.

**What data do I need to forecast the angel's share?**
Cask fill volumes and strengths, cask type and size, position in the warehouse, and periodic weights or dips. Warehouse temperature and humidity logs make the forecast considerably more reliable.
