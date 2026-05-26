---
layout: post
title: "A Procurement and Commodity-Price Dashboard in Tableau"
image: /assets/og/tableau-procurement-commodity-price-dashboard.png
description: "Build a procurement and commodity-price dashboard in Tableau to track malt, hop and energy prices, contract coverage versus spot, and price exposure scenarios."
date: 2023-05-21
updated: 2023-05-21
tags: [fpna, tableau, procurement]
faq:
  - q: "What should a commodity-price dashboard track for a brewery?"
    a: "At minimum: spot and contract prices for malt, hops and energy over time, contracted coverage as a share of forecast demand, and unhedged exposure. The exposure measure is what turns a price chart into a procurement decision tool."
  - q: "Can Tableau forecast commodity prices?"
    a: "Tableau's built-in forecast uses exponential smoothing, which is fine for stable series but weak for volatile commodities with shocks and seasonality. Use it for a rough trend line, not for hedging decisions, and bring an external model in via TabPy when you need rigour."
  - q: "How do you model price scenarios in Tableau?"
    a: "Expose a price assumption as a parameter and wire it into a calculated field that computes spend on the unhedged volume. Dragging the parameter shows how a price move flows through to cost and exposure."
---

**Short answer: a commodity-price dashboard is useful when it pairs price trends with contract coverage and unhedged exposure — and honest about the fact that Tableau's built-in forecast is too basic to hedge on.** Track the exposure, not just the price.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Procurement and Commodity-Price Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Procurement and Commodity-Price Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Measure exposure, not just price
A wall of price lines for malt, hops and energy looks informative and decides nothing. The measure that matters to a procurement lead is exposure: the unhedged volume multiplied by the gap between your contracted price and the prevailing spot. Build it as a calculated field that takes forecast demand, subtracts contracted volume, and prices the remainder at spot. Now the dashboard answers the real question — how much spend is still exposed to the market — rather than merely plotting history.

Put coverage front and centre too: contracted volume as a percentage of forecast demand, per commodity, over the planning horizon. A FIXED LOD expression aggregating contracted volume per commodity lets you show coverage cleanly regardless of which time filter the user applies. The two measures together — coverage and exposure — frame every hedging conversation, and they should anchor the layout before any price line is drawn.

## Building the view
Lead with a coverage-versus-time area chart per commodity, then overlay spot and contract price on a dual axis so the user sees price moving against how protected they are. Where coverage is thin and spot is climbing, the exposure mark should glow — encode exposure on colour so the dangerous combination is unmissable.

Add a scenario parameter for each commodity price. Wire it into the exposure calculation so a procurement analyst can ask, "if energy rises fifteen per cent, what does our unhedged spend become?" and watch the figure move. This is what-if analysis that respects the structure of the problem: you are flexing the price applied to genuinely unhedged volume, not pretending to predict the market. It complements the heavier modelling in [forecasting malt and hop prices for procurement]({{ '/2021/forecasting-malt-hop-prices-procurement/' | relative_url }}), where the actual price prediction lives; the dashboard consumes those forecasts rather than reinventing them.

For monitoring, publish to Tableau Cloud and let Tableau Pulse watch coverage and exposure. A natural-language digest that flags "energy exposure up 20% as coverage fell below target" lands in the right inbox before the month-end surprise does. Pulse is a watcher, not an analyst — it tells you something moved, you decide what to do about it.

## Where it breaks
The sharpest limit is forecasting. Tableau's built-in forecast is exponential smoothing, which assumes a series that trends and seasons gently. Commodities do neither — they jump on weather, geopolitics and energy shocks. Lean on that forecast for hedging and you will be confidently wrong. If you need real predictions, push the series to a proper time-series model through TabPy and bring the result back as a field; keep the heavy lifting outside Tableau and let the dashboard display it.

The second limit is data latency and quality. Spot prices may update daily while your contract data refreshes monthly, so exposure can flicker for reasons of timing, not reality. And contract terms — caps, collars, volume bands — rarely fit neatly into a single price field, so a simplified coverage measure can overstate or understate protection. Document those simplifications, because the dashboard will present the simplified version as if it were the contract.

## The bottom line
Centre the dashboard on coverage and unhedged exposure, not a gallery of price lines, and use parameters for disciplined price scenarios. Let Pulse monitor the exposure so nobody is blindsided. But treat Tableau's built-in forecast as a sketch, lean on TabPy or an external model for anything you would hedge on, and be explicit about the contract details your coverage measure has had to simplify.

*Part of the [Financial Planning & Analytics]({{ '/tracks/financial-planning-analytics/' | relative_url }}) track.* Related: [forecasting malt and hop prices for procurement]({{ '/2021/forecasting-malt-hop-prices-procurement/' | relative_url }}).

## Frequently asked questions

**What should a commodity-price dashboard track for a brewery?**
At minimum: spot and contract prices for malt, hops and energy over time, contracted coverage as a share of forecast demand, and unhedged exposure. The exposure measure is what turns a price chart into a procurement decision tool.

**Can Tableau forecast commodity prices?**
Tableau's built-in forecast uses exponential smoothing, which is fine for stable series but weak for volatile commodities with shocks and seasonality. Use it for a rough trend line, not for hedging decisions, and bring an external model in via TabPy when you need rigour.

**How do you model price scenarios in Tableau?**
Expose a price assumption as a parameter and wire it into a calculated field that computes spend on the unhedged volume. Dragging the parameter shows how a price move flows through to cost and exposure.
