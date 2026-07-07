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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Rackhouse Microclimate Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">A Rackhouse Microclimate Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Why microclimate decides the dram
A traditional dunnage warehouse and a tall racked rackhouse mature spirit very differently, and within any single building the top shelves run warmer and drier than the floor. That vertical gradient is why two casks filled on the same day from the same spirit can diverge over a decade — different angel's share, different wood extraction of vanillin, lactones and tannins. If you cannot see the microclimate, you cannot explain the variation, and you certainly cannot manage it.

The job of this dashboard is to make position a first-class dimension of your data, alongside cask and time.

## Building the heatmap
Start by defining the grain: a reading per sensor per timestamp, joined to a cask-position table that records each cask's bay, row and height. In Tableau Prep, pivot and clean the sensor feed, then publish a .hyper extract. Build the core view as a heatmap with bay and row on the axes and height as a small-multiple or a parameter the user toggles, colouring cells by average temperature, relative humidity, or measured loss.

LOD expressions do the heavy lifting: `{ FIXED [Bay], [Height] : AVG([Temperature]) }` gives a stable per-zone average that does not shift as the user filters by month. Link that microclimate field to cask outcomes and you can rank rotation candidates — the casks sitting in the hottest, driest cells. A highlight action lets a user click a hot zone and see every cask in it. When something looks off, run Explain Data on the outlier and Tableau will propose candidate causes for you to verify.

## Where it breaks
The honest limit is sensor coverage. A handful of probes in a large rackhouse interpolates more than it measures, so your heatmap is a model, not a map. Spend on sensors before you trust the cell-level detail. The second limit is control: traditional warehouses are deliberately passive, and you cannot air-condition a dunnage shed without changing the character of the whisky. The dashboard mostly tells you where to move casks, not how to change the climate — and even rotation is constrained by labour and the spirit's intended style. For the optimisation side, see [AI rackhouse microclimate optimisation]({{ '/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}).

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives maturation, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">A Rackhouse Microclimate Dashboard in Tableau</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Maturation</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">quality</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">What drives maturation, and what it changes downstream.</figcaption>
</figure>

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
