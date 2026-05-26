---
layout: post
title: "A COGS-per-Hectolitre Dashboard in Tableau"
image: /assets/og/tableau-cogs-per-hectolitre-dashboard.png
description: "Build a COGS-per-hectolitre dashboard in Tableau with calculated fields, a cost-driver waterfall and price parameters to see where beverage margin really goes."
date: 2023-05-04
updated: 2023-05-04
tags: [fpna, tableau, finance]
faq:
  - q: "How do you calculate COGS per hectolitre in Tableau?"
    a: "Aggregate total cost of goods for a product, then divide by volume produced in hectolitres using a calculated field. Define the cost components — ingredients, packaging, energy, labour, overhead allocation — explicitly so the denominator and numerator share the same scope."
  - q: "What is a cost-driver waterfall good for?"
    a: "It decomposes COGS per hectolitre into its contributing drivers in sequence, so finance can see whether a margin move came from malt prices, packaging, energy or yield rather than guessing from a single total."
  - q: "Does Explain Data tell you why margin fell?"
    a: "It suggests statistically plausible explanations for an outlier mark, such as which dimension values are unusually high. It is a hypothesis generator, not a verdict; you still confirm the driver against the actual cost ledger."
---

**Short answer: a COGS-per-hectolitre dashboard earns its keep when it decomposes cost into drivers with a waterfall and lets finance flex input prices through parameters — not when it shows one blended number.** The discipline is agreeing what goes into the cost before you divide by volume.

## Define the measure before you build
COGS per hectolitre sounds simple and is quietly contentious. The numerator is total cost of goods; the denominator is volume in hectolitres. The argument is always about what belongs in the numerator. Do you include packaging? Energy? An allocation of fixed overhead? Build the calculated field to mirror exactly how finance defines cost, and make every component its own field — ingredient cost, packaging, energy, direct labour, allocated overhead — so the total is transparent and auditable rather than a black box.

This measure-first habit pays off twice. First, when someone questions a number, you can trace it to a component. Second, it lets you build the cost-driver waterfall, which is the analytical heart of the dashboard. Without named components there is nothing to decompose. Get the definitions signed off by FP&A before drawing a single mark; the dashboard is downstream of that agreement, never a substitute for it.

## The waterfall and the price parameter
A waterfall chart takes a baseline COGS/hl and walks through each driver's contribution to the current figure: malt up, packaging flat, energy up, yield improvement down. In Tableau you build this with table calculations on the running total of driver deltas, sequencing the bars so each starts where the last finished. The result answers the only question a CFO asks about a margin move — *which lever moved it* — instead of leaving them to infer it from a single total.

Then add a what-if layer. Expose key input prices as parameters — malt price, aluminium, energy tariff — and wire them into the cost calculated fields. Now finance can drag a parameter and watch COGS/hl and the waterfall recompute live: "if malt rises eight per cent, where does margin land?" This is genuine scenario analysis inside the dashboard, and it sits naturally alongside the broader picture in the [CFO AI dashboard for beverage]({{ '/2026/cfo-ai-dashboard-beverage/' | relative_url }}), which pulls these unit economics up to the P&L view.

For the AI assist, use Explain Data on a margin dip. Select the offending mark and Tableau proposes which dimension values are statistically unusual — perhaps one SKU's energy cost spiked. Treat it as a fast hypothesis, then confirm against the ledger before you brief anyone.

## Where it breaks
The first limit is cost-allocation assumptions. How you spread fixed overhead across hectolitres is a judgement call, and a defensible one can still flatter a high-volume line and punish a small batch. The dashboard will present whatever allocation you coded as if it were fact. Document the basis on the dashboard itself so users read the number in context rather than as gospel.

The second limit is data quality — the familiar garbage-in problem. If energy is billed quarterly but volume is daily, or if a packaging cost lands in the wrong period, COGS/hl lurches for reasons that have nothing to do with operations. Tableau cannot reconcile your cost ledger; it can only divide what you give it. And the parameter what-if is linear by design: it flexes a price, not the second-order effects of that price change on demand or mix, so do not mistake a slider for a model.

## The bottom line
Build COGS per hectolitre from named, auditable cost components, decompose it with a waterfall so the driver behind any move is obvious, and add price parameters for live scenario testing. Use Explain Data to generate hypotheses, not conclusions. Above all, surface your allocation assumptions — the maths is only as honest as the cost data and the judgement calls feeding it.

*Part of the [Financial Planning & Analytics]({{ '/tracks/financial-planning-analytics/' | relative_url }}) track.* Related: [the CFO AI dashboard for beverage]({{ '/2026/cfo-ai-dashboard-beverage/' | relative_url }}).

## Frequently asked questions

**How do you calculate COGS per hectolitre in Tableau?**
Aggregate total cost of goods for a product, then divide by volume produced in hectolitres using a calculated field. Define the cost components — ingredients, packaging, energy, labour, overhead allocation — explicitly so the denominator and numerator share the same scope.

**What is a cost-driver waterfall good for?**
It decomposes COGS per hectolitre into its contributing drivers in sequence, so finance can see whether a margin move came from malt prices, packaging, energy or yield rather than guessing from a single total.

**Does Explain Data tell you why margin fell?**
It suggests statistically plausible explanations for an outlier mark, such as which dimension values are unusually high. It is a hypothesis generator, not a verdict; you still confirm the driver against the actual cost ledger.
