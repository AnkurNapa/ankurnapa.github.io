---
layout: post
title: "A Vineyard Yield and Harvest Dashboard in Tableau"
image: /assets/og/tableau-vineyard-yield-harvest-dashboard.png
description: "Build a Tableau vineyard dashboard mapping blocks, tracking Brix and acidity ripeness curves, and sequencing harvest with Pulse digests."
date: 2023-01-14
updated: 2023-01-14
tags: [winemaking, tableau, viticulture]
faq:
  - q: "What data do I need for a vineyard yield dashboard in Tableau?"
    a: "At minimum you need block-level sampling (°Brix, titratable acidity, pH), bunch counts or berry weights for yield estimates, and a geographic reference for each block. Weather and NDVI feeds are useful extras but not essential to start."
  - q: "Can Tableau forecast my harvest date?"
    a: "Tableau's built-in forecast uses exponential smoothing, which is fine for a rough ripeness trajectory but not a true harvest model. For a defensible prediction, score an external model through TabPy and visualise the output."
  - q: "Should I map vineyard blocks in Tableau?"
    a: "Yes, if your decisions are spatial. Assign geographic roles or use custom geocoding so each block appears on a map, then colour it by ripeness or yield to read the whole estate at a glance."
---

**Short answer: a vineyard dashboard works when it puts ripeness, yield and geography on one screen so you can sequence the pick, not just admire the harvest after it happens.** The discipline is to decide what you measure before you draw a single chart.

## Measure first, then map
Start with the question, not the data source. The vineyard question at véraison is brutally simple: which block do I pick, and when? That tells you the measures: °Brix as the sugar proxy, titratable acidity and pH (you want pH landing somewhere around 3.2 to 3.6 for most reds), and a yield estimate built from bunch counts and berry weights. Phenolic ripeness rarely lives in a spreadsheet, so flag it as a manual tasting note rather than pretending you have a number.

Connect your sampling data as a live source if it updates daily during harvest, or an extract (.hyper) if it is a weekly drop. Tableau Prep earns its keep here: sampling sheets arrive with inconsistent block names and stray units, and Prep lets you standardise them once rather than fighting calculated fields forever.

## Build the block map and the ripeness curve
Give each block a geographic role or load custom geocoding, and you get an estate map where colour encodes °Brix and size encodes estimated yield. That single view answers "where is the fruit and how ripe is it" without a table.

Pair it with a ripeness curve: sampling date on the axis, °Brix on the line, one mark per block. Add a parameter for your target Brix by varietal and draw it as a reference line, so the gap between the curve and the target is visible. A FIXED level-of-detail calculation — `{FIXED [Block] : AVG([Brix])}` — lets you aggregate per block cleanly even when you have multiple samples per row, which keeps the colour encoding honest. Filter actions let you click a block on the map and drive the curve below it.

For yield sequencing, a simple table sorted by projected pick date, coloured by tank capacity available, turns the dashboard into an operations tool rather than a report.

## Let Pulse watch the trend
This is where the AI layer adds something real. Point Tableau Pulse at your ripeness metric per block and it monitors the trajectory, then sends a natural-language digest — "Block 7 Cabernet up 1.4 °Brix this week, tracking ahead of target." That is genuinely useful during a compressed harvest when nobody has time to open the dashboard hourly. Einstein Copilot's Explain Data can also surface why one block jumped, though it explains the data you fed it, not the vine.

## Where it breaks
Be honest about the limits. The map is only as good as your sampling cadence: a dashboard updated weekly cannot warn you about a heat spike that ripens fruit in three days. NDVI imagery has gaps from cloud and revisit timing, so treat it as a vigour hint, not gospel. Weather swings vintages more than any chart can, and Tableau's built-in forecast will happily extrapolate a smooth ripening line straight through a forecast heatwave it knows nothing about. The dashboard sequences the pick; it does not replace walking the rows and tasting the fruit.

## The bottom line
A vineyard yield dashboard in Tableau is a sequencing tool: map the blocks, track ripeness against a parameterised target, and let Pulse flag the movers. Keep the measures few and well-defined, and accept that sampling gaps and weather set the ceiling on accuracy. For an actual predictive model, look beyond the built-in forecast.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [AI vineyard yield forecasting]({{ '/2024/ai-vineyard-yield-forecasting/' | relative_url }}).

## Frequently asked questions

**What data do I need for a vineyard yield dashboard in Tableau?**
At minimum you need block-level sampling (°Brix, titratable acidity, pH), bunch counts or berry weights for yield estimates, and a geographic reference for each block. Weather and NDVI feeds are useful extras but not essential to start.

**Can Tableau forecast my harvest date?**
Tableau's built-in forecast uses exponential smoothing, which is fine for a rough ripeness trajectory but not a true harvest model. For a defensible prediction, score an external model through TabPy and visualise the output.

**Should I map vineyard blocks in Tableau?**
Yes, if your decisions are spatial. Assign geographic roles or use custom geocoding so each block appears on a map, then colour it by ripeness or yield to read the whole estate at a glance.
