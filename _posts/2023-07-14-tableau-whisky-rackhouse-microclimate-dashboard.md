---
layout: post
title: "A Rackhouse Microclimate Dashboard in Tableau"
image: /assets/og/tableau-whisky-rackhouse-microclimate-dashboard.png
description: "Build a Tableau rackhouse microclimate dashboard mapping warehouse temperature and humidity by position to maturation loss, with AI outlier explanations."
date: 2023-07-14
updated: 2023-07-14
tags: [distilling-maturation, tableau, whiskey]
faq:
  - q: "How do I map warehouse position in Tableau?"
    a: "Treat bay, row and height as coordinates and build a heatmap using those as rows and columns, colouring each cell by temperature, humidity or measured loss so the rackhouse's vertical gradient becomes visible."
  - q: "Can Tableau tell me which casks to rotate?"
    a: "It can rank candidates by exposure to hot or dry zones and flag them, but rotation decisions also depend on the spirit's target style, so the dashboard informs rather than dictates."
  - q: "What does Explain Data add here?"
    a: "Explain Data proposes statistical reasons for an outlier — such as a cask high in a warm bay losing more — giving you a fast hypothesis to check against sensor and weighing records."
---

**Short answer: a Tableau rackhouse dashboard turns warehouse sensor readings into a heatmap that shows exactly where heat and dryness are driving faster loss and bigger cask-to-cask variation.** It makes an invisible microclimate visible — provided you have enough sensors to map it.

## Why microclimate decides the dram
A traditional dunnage warehouse and a tall racked rackhouse mature spirit very differently, and within any single building the top shelves run warmer and drier than the floor. That vertical gradient is why two casks filled on the same day from the same spirit can diverge over a decade — different angel's share, different wood extraction of vanillin, lactones and tannins. If you cannot see the microclimate, you cannot explain the variation, and you certainly cannot manage it.

The job of this dashboard is to make position a first-class dimension of your data, alongside cask and time.

## Building the heatmap
Start by defining the grain: a reading per sensor per timestamp, joined to a cask-position table that records each cask's bay, row and height. In Tableau Prep, pivot and clean the sensor feed, then publish a .hyper extract. Build the core view as a heatmap with bay and row on the axes and height as a small-multiple or a parameter the user toggles, colouring cells by average temperature, relative humidity, or measured loss.

LOD expressions do the heavy lifting: `{ FIXED [Bay], [Height] : AVG([Temperature]) }` gives a stable per-zone average that does not shift as the user filters by month. Link that microclimate field to cask outcomes and you can rank rotation candidates — the casks sitting in the hottest, driest cells. A highlight action lets a user click a hot zone and see every cask in it. When something looks off, run Explain Data on the outlier and Tableau will propose candidate causes for you to verify.

## Where it breaks
The honest limit is sensor coverage. A handful of probes in a large rackhouse interpolates more than it measures, so your heatmap is a model, not a map. Spend on sensors before you trust the cell-level detail. The second limit is control: traditional warehouses are deliberately passive, and you cannot air-condition a dunnage shed without changing the character of the whisky. The dashboard mostly tells you where to move casks, not how to change the climate — and even rotation is constrained by labour and the spirit's intended style. For the optimisation side, see [AI rackhouse microclimate optimisation]({{ '/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}).

## The bottom line
Mapping microclimate in Tableau is the clearest way to understand why your casks diverge and which ones are exposed to the harshest conditions. It rewards investment in sensors and a clean position table, and it pairs naturally with AI features that explain outliers. Use it to inform rotation and fill strategy, but remember the warehouse is a slow, passive instrument — the dashboard helps you read it, not override it.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.* Related: [AI rackhouse microclimate optimisation]({{ '/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}).

## Frequently asked questions

**How do I map warehouse position in Tableau?**
Treat bay, row and height as coordinates and build a heatmap using those as rows and columns, colouring each cell by temperature, humidity or measured loss so the rackhouse's vertical gradient becomes visible.

**Can Tableau tell me which casks to rotate?**
It can rank candidates by exposure to hot or dry zones and flag them, but rotation decisions also depend on the spirit's target style, so the dashboard informs rather than dictates.

**What does Explain Data add here?**
Explain Data proposes statistical reasons for an outlier — such as a cask high in a warm bay losing more — giving you a fast hypothesis to check against sensor and weighing records.
