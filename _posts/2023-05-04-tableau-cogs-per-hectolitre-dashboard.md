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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A COGS-per-Hectolitre Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">A COGS-per-Hectolitre Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Start to finish, broken into the pieces that move the number."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">BRIDGE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">A COGS-per-Hectolitre Dashboard in Tableau</text><line x1="60" y1="250" x2="680" y2="250" stroke="#06483f" stroke-width="1.5"/><rect x="90" y="100" width="80" height="150" fill="#00695c"/><text x="130" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">Start</text><rect x="230" y="140" width="80" height="40" fill="#06483f"/><text x="270" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">−40</text><rect x="350" y="170" width="80" height="30" fill="#06483f"/><text x="390" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">−30</text><rect x="470" y="130" width="80" height="40" fill="#2e9e7c"/><text x="510" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">+40</text><rect x="590" y="130" width="80" height="120" fill="#00695c"/><text x="630" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">End</text><line x1="170" y1="100" x2="230" y2="100" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="310" y1="140" x2="350" y2="140" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="430" y1="170" x2="470" y2="170" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="550" y1="130" x2="590" y2="130" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Start to finish, broken into the pieces that move the number.</figcaption>
</figure>

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
