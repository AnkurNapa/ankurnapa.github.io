---
layout: post
title: "Building a Brewery Production and Yield Dashboard in Tableau"
image: /assets/og/tableau-brewery-production-yield-dashboard.png
description: "How to build a brewery production and yield dashboard in Tableau using LOD expressions, brewhouse yield trends and Tableau Pulse digests."
date: 2023-01-04
updated: 2023-01-04
tags: [brewing-science, tableau, analytics]
faq:
  - q: "What is the most important metric to model first in a yield dashboard?"
    a: "Brewhouse yield (actual extract recovered versus theoretical extract available) is the anchor metric. Everything else — tank turns, batch volume, loss — should be derived consistently from the same batch-level grain so the numbers reconcile."
  - q: "Why use LOD expressions instead of normal aggregations?"
    a: "Yield is naturally a per-batch ratio, and naive averages of ratios are misleading. A FIXED level-of-detail expression pins the calculation to the batch before you roll it up, so a monthly figure is a true volume-weighted yield rather than an average of averages."
  - q: "Can Tableau Pulse tell me why yield dropped?"
    a: "Pulse will flag the drop and write a plain-language digest of the trend, which is useful for catching it early. It will not diagnose the cause — that needs your process data, the brewlog and a person who knows the brewhouse."
---

**Short answer: a good Tableau yield dashboard is 80% data model and 20% chart.** Get the batch-level grain and the yield definition right first, and the visuals almost build themselves. Get them wrong, and you ship a beautiful dashboard that quietly lies.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for Building a Brewery Production and Yield Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Building a Brewery Production and Yield Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Start with the batch, not the chart
The temptation is to drag a few fields onto a sheet and call it a dashboard. Resist it. The first decision is your data model: what is the atomic unit? For a yield and production dashboard, that unit is the batch (or brew). Every fact — wort volume into fermenter, original gravity, extract recovered, racking loss, packaged volume — should hang off a batch key.

Once the grain is clean, define your metrics explicitly as calculated fields. Brewhouse yield is actual extract divided by theoretical extract from the grist; apparent yield loss is the gap between volume in and volume out at each transfer. Write these once, name them clearly, and reuse them everywhere. This is the "measure first" discipline that separates a reporting tool from a decoration — and it is the same foundation that AI work later depends on. If your batch data is messy, fix that before anything else; see [building a brewery data foundation for AI]({{ '/2024/building-brewery-data-foundation-ai/' | relative_url }}).

## LOD expressions and a metric you can switch
Yield is a ratio, and ratios do not average cleanly. If you take a simple mean of each batch's yield percentage, a tiny 2 hL pilot batch counts the same as a 200 hL production brew. The fix is a level-of-detail expression: use `{ FIXED [Batch ID] : SUM([Extract Recovered]) }` and `{ FIXED [Batch ID] : SUM([Theoretical Extract]) }`, then divide the rolled-up sums. Now your monthly yield is properly volume-weighted.

With the model solid, add a **parameter** to let the user switch the headline metric — brewhouse yield, hL per brew, tank turns per month, or loss percentage — without building four dashboards. A parameter action plus a CASE statement in a calculated field swaps the measure on the fly. Trend it over time, add a reference line for your target, and you can read the story at a glance: are we drifting, holding, or improving?

Tank turns deserve their own view. Count distinct batches per fermenter per period, dual-axis against capacity utilisation, and you can see whether yield problems are really capacity problems in disguise.

## Where it breaks
Be honest about what this dashboard does and does not do. Tableau shows you the gap between actual and theoretical yield; it does not close it. A dashboard cannot improve mash efficiency, tighten transfers or reduce trub loss. It only makes the loss visible enough that someone acts.

The bigger risk is dirty input. If brewers log volumes inconsistently, or gravity readings are temperature-uncorrected, or a batch is split across two fermenters but recorded as one, the LOD maths is flawless and the answer is still wrong. Tableau will not catch that — it trusts your data completely.

On the AI side, **Tableau Pulse** can monitor your yield metric and push a weekly natural-language digest ("brewhouse yield down 1.8% versus the prior four weeks, driven by three low batches"). That is genuinely useful for early warning. But Pulse summarises the trend; it does not explain causation, and its built-in forecasting is exponential smoothing — fine for a smooth headline number, not a substitute for a proper model when you want to predict yield from grist, mash profile and equipment. For that you would push features to an external model via TabPy and visualise the result, with a generative layer only ever drafting the commentary a human then checks.

## The bottom line
A Tableau production and yield dashboard earns its keep when the batch-level data model is clean and the yield definitions are explicit. LOD expressions keep your ratios honest, a parameter keeps the view flexible, and Pulse keeps an eye on the trend so you do not have to. Just remember the tool reveals the loss — your brewhouse closes it.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [building a brewery data foundation for AI]({{ '/2024/building-brewery-data-foundation-ai/' | relative_url }}).

## Frequently asked questions

**What is the most important metric to model first in a yield dashboard?**
Brewhouse yield (actual extract recovered versus theoretical extract available) is the anchor metric. Everything else — tank turns, batch volume, loss — should be derived consistently from the same batch-level grain so the numbers reconcile.

**Why use LOD expressions instead of normal aggregations?**
Yield is naturally a per-batch ratio, and naive averages of ratios are misleading. A FIXED level-of-detail expression pins the calculation to the batch before you roll it up, so a monthly figure is a true volume-weighted yield rather than an average of averages.

**Can Tableau Pulse tell me why yield dropped?**
Pulse will flag the drop and write a plain-language digest of the trend, which is useful for catching it early. It will not diagnose the cause — that needs your process data, the brewlog and a person who knows the brewhouse.
