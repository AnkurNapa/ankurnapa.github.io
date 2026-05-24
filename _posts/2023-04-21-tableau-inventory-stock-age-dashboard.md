---
layout: post
title: "An Inventory and Stock-Age Dashboard in Tableau"
image: /assets/og/tableau-inventory-stock-age-dashboard.png
description: "Build an inventory and stock-age dashboard in Tableau using LOD calculations, days-of-cover and FIFO risk flags to spot ageing beverage stock early."
date: 2023-04-21
updated: 2023-04-21
tags: [commercial-planning, tableau, inventory]
faq:
  - q: "How do you calculate stock age in Tableau?"
    a: "Use a date difference between today and the receipt or production date, typically wrapped in a FIXED LOD expression so the age is computed per lot or per SKU regardless of the view's filters. You then bucket the result into age bands with a calculated field."
  - q: "Can Tableau reallocate ageing stock automatically?"
    a: "No. Tableau visualises and monitors the risk; it surfaces which lots are ageing and where cover is thin, but the reallocation or markdown decision sits with planners and your ERP or order system."
  - q: "What is days-of-cover and why show it next to stock age?"
    a: "Days-of-cover is on-hand quantity divided by average daily demand. Pairing it with stock age separates 'old but selling' from 'old and stranded', which is the distinction that drives write-off risk."
---

**Short answer: a stock-age dashboard works when you compute age and cover per lot with LOD expressions, then let the visuals rank risk rather than bury it in a table.** The hard part is not the chart; it is deciding what "old" means for each product before you draw anything.

## Measure first, then visualise
Begin with the measures, not the marks. For a beverage business the two that matter are stock age and days-of-cover, and both should be defined per lot or per SKU before any filter touches them. That is exactly what a FIXED level-of-detail expression is for: `{ FIXED [Lot ID] : MIN([Receipt Date]) }` pins the receipt date so a date diff against today gives a true age, even when the user later filters to a region or brand. Days-of-cover is on-hand divided by average daily demand, again computed at the grain you ship at. Settle these definitions with the supply-chain team first; if planners disagree on whether age starts at production or at warehouse receipt, no dashboard will rescue the conversation.

Once the measures are agreed, bucket age into bands with a calculated field — fresh, watch, ageing, critical — using thresholds that reflect real shelf life. Beer and unfortified wine age very differently, so a single threshold across the portfolio is a mistake. Buckets give you a colour-coded heatmap of SKUs by age band that a planner can read in seconds, which is the whole point.

## Building the FIFO risk view
The core view ranks SKUs by a blend of age band and cover. A SKU that is in the ageing band *and* has high days-of-cover is your write-off candidate; one that is ageing but has thin cover will clear itself. Encode age on colour, cover on size, and you get a single scatter where the dangerous corner — old and overstocked — is visually obvious.

Layer a FIFO risk flag on top with a boolean calculated field: flag any lot whose age exceeds its band threshold while newer lots of the same SKU are still being picked. This catches the classic failure where fresh stock ships ahead of old, leaving the oldest lots to expire. The flag is a judgement rule, not a law of physics, so expose its threshold as a parameter and let planners tune it. This sits alongside the broader FIFO discipline covered in [cellar inventory FIFO optimisation]({{ '/2022/cellar-inventory-fifo-optimisation/' | relative_url }}), where the same first-in-first-out logic drives the picking sequence itself.

For the AI layer, publish the dashboard to Tableau Cloud and point Tableau Pulse at the stock-age and cover metrics. Pulse will monitor them and push a natural-language digest when an SKU drifts into the ageing band or cover spikes — useful for catching slow build-ups that nobody is watching daily. It is monitoring, not magic; treat its digests as a prompt to look, not a decision.

## Where it breaks
The honest limit is data quality, specifically perishability and date integrity. If receipt dates are wrong, batch codes are missing, or returns re-enter stock without a fresh date, your age calculation is fiction and the FIFO flag fires on noise. Tableau will faithfully visualise bad data, which is worse than no dashboard because it looks authoritative.

The second limit is that the dashboard diagnoses, it does not act. It will show you forty pallets of seasonal cider drifting critical, but the markdown, the transfer, or the promotion is a human and ERP decision. Resist the urge to bolt allocation logic into calculated fields; that belongs in a planning system, not a viz. And remember the built-in forecast Tableau uses for demand is basic exponential smoothing — fine for a rough cover estimate, not a substitute for a proper demand model when the stakes are high.

## The bottom line
Define stock age and days-of-cover per lot with LOD expressions, bucket age into shelf-life-aware bands, and rank the old-and-overstocked corner so it cannot hide. Let Pulse watch the metrics and flag drift. Just keep the dashboard honest about its job: it spots risk early, but the data quality upstream and the reallocation decision downstream are still yours.

*Part of the [Commercial Planning Analytics]({{ '/tracks/commercial-planning/' | relative_url }}) track.* Related: [cellar inventory FIFO optimisation]({{ '/2022/cellar-inventory-fifo-optimisation/' | relative_url }}).

## Frequently asked questions

**How do you calculate stock age in Tableau?**
Use a date difference between today and the receipt or production date, typically wrapped in a FIXED LOD expression so the age is computed per lot or per SKU regardless of the view's filters. You then bucket the result into age bands with a calculated field.

**Can Tableau reallocate ageing stock automatically?**
No. Tableau visualises and monitors the risk; it surfaces which lots are ageing and where cover is thin, but the reallocation or markdown decision sits with planners and your ERP or order system.

**What is days-of-cover and why show it next to stock age?**
Days-of-cover is on-hand quantity divided by average daily demand. Pairing it with stock age separates 'old but selling' from 'old and stranded', which is the distinction that drives write-off risk.
