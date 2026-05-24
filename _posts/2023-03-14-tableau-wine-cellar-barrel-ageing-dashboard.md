---
layout: post
title: "A Cellar and Barrel-Ageing Inventory Dashboard in Tableau"
image: /assets/og/tableau-wine-cellar-barrel-ageing-dashboard.png
description: "Build a Tableau cellar dashboard tracking barrels by type and age via LOD, top-up and evaporation, SO2 status and an ageing timeline with Pulse alerts."
date: 2023-03-14
updated: 2023-03-14
tags: [winemaking, tableau, inventory]
faq:
  - q: "How do I aggregate barrels by lot in Tableau?"
    a: "Use a FIXED level-of-detail calculation keyed on lot, such as the total volume or average free SO2 per lot. That gives you a clean per-lot rollup even though each row is a single barrel."
  - q: "Can Tableau track barrel evaporation?"
    a: "Yes, if you log top-ups. Calculate the volume added per barrel over time and the dashboard shows evaporation as a running top-up total, which also flags barrels losing more than expected."
  - q: "Will Tableau Pulse tell me which barrels are due?"
    a: "Pulse monitors the metric you define, such as days since last SO2 check or months in barrel, and sends a digest naming the barrels crossing your threshold. It surfaces the list; the cellar still does the work."
---

**Short answer: a cellar dashboard is worth building when it answers "what is in barrel, how old is it, and which barrels need attention" without anyone opening the cellar map in their head.** Define the rollup grain — barrel, lot, type — before you draw anything.

## Model the cellar grain first
Barrel data is hierarchical, so decide your levels before building: individual barrel, lot, barrel type (new versus used oak), and vintage. Each row in your source is usually one barrel with attributes — fill date, oak type, lot, last top-up, free and total SO2. The measure-first discipline means agreeing what a "barrel due for top-up" or "barrel at risk on SO2" actually means before you visualise it.

Cellar data is often hand-logged, so connect a refreshed extract rather than chasing a live feed, and use Tableau Prep to reconcile barrel IDs that drift between spreadsheets. Level-of-detail calculations do the heavy lifting: `{FIXED [Lot] : SUM([Volume])}` gives litres per lot, and an INCLUDE expression lets you average free SO2 at barrel grain while displaying it by lot.

## The inventory and ageing views
Build a matrix of barrels coloured by oak type and sized by volume, filtered by lot and vintage — the cellar at a glance. Beside it, an ageing timeline plots each lot's months in barrel against a target ageing window held in a parameter, so a lot drifting past its plan is obvious.

Track top-ups and evaporation as a running total of litres added per barrel; a barrel demanding far more top-up than its neighbours is either thirsty oak or a problem. An SO2 status view colours each barrel red, amber or green against your free-SO2 floor, with a filter action so clicking a lot reveals its barrels. Parameter actions let you flex the ageing target and watch which lots fall in or out of plan.

## Let Pulse flag what is due
Set Tableau Pulse on "barrels past SO2 check" and "lots approaching end of ageing window." It monitors those metrics and sends a digest naming the barrels and lots crossing the line — the cellar's morning to-do list, written in plain language. Einstein's Explain Data can help when one lot's SO2 is dropping faster than the rest, pointing at the fields that differ.

## Where it breaks
The candid limits are about data and biology. Cellar data is largely manual, so the dashboard is only as current as the last person who wrote in the log; a barrel topped up but never recorded looks neglected. Barrel-to-barrel variation is real — two barrels of the same oak and age can age very differently — so an aggregate by type hides individual outliers that matter at blending. And the dashboard tracks ageing; it cannot tell you a wine is ready. That is a bench-trial and a palate decision, and even an AI quality model is an estimate rather than a tasting.

## The bottom line
A Tableau cellar dashboard turns a scattered barrel log into a managed inventory: LOD rollups by lot and type, top-up and evaporation tracking, SO2 status, and an ageing timeline, with Pulse naming the barrels due. Keep the data current and remember it tracks ageing, not readiness.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [Can AI predict wine quality?]({{ '/2026/can-ai-predict-wine-quality/' | relative_url }}).

## Frequently asked questions

**How do I aggregate barrels by lot in Tableau?**
Use a FIXED level-of-detail calculation keyed on lot, such as the total volume or average free SO2 per lot. That gives you a clean per-lot rollup even though each row is a single barrel.

**Can Tableau track barrel evaporation?**
Yes, if you log top-ups. Calculate the volume added per barrel over time and the dashboard shows evaporation as a running top-up total, which also flags barrels losing more than expected.

**Will Tableau Pulse tell me which barrels are due?**
Pulse monitors the metric you define, such as days since last SO2 check or months in barrel, and sends a digest naming the barrels crossing your threshold. It surfaces the list; the cellar still does the work.
