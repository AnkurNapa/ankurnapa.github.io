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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Vineyard Yield and Harvest Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">A Vineyard Yield and Harvest Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives the harvest, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">A Vineyard Yield and Harvest Dashboard in Tableau</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">The harvest</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">quality</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">What drives the harvest, and what it changes downstream.</figcaption>
</figure>

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
