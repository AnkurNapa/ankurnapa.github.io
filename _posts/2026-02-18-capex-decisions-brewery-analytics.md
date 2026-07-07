---
layout: post
title: "Capex with Analytics: When to Add a Tank or a Canning Line"
image: /assets/og/capex-decisions-brewery-analytics.png
description: "Capex decision analytics for breweries — how to use capacity utilization, margin contribution, and payback modeling to time tank and canning line investments."
date: 2026-02-18
updated: 2026-02-18
tags: [fpna, capex, capacity-planning]
faq:
  - q: "What financial metrics should drive a brewery's decision to add fermentation capacity?"
    a: "The primary metrics are tank utilization rate (if peak utilization is consistently above 85%, constraint costs are likely accruing), incremental margin contribution from the constrained volume (what gross margin is being lost to the capacity limit), and payback period on the new tank at realistic throughput assumptions. A tank sitting at 60% utilization with no credible demand signal does not justify the capital."
  - q: "How should a brewery evaluate a canning line investment versus contract canning?"
    a: "The comparison should be built on a total cost basis: in-house canning cost per case (amortized capital, direct labor, consumables, maintenance) versus contract canning cost per case including freight and lead time premium. The break-even volume threshold — the volume at which in-house is cheaper — should be modeled against the brewery's credible 3-year demand forecast. Below that threshold, contract canning preserves capital and maintains flexibility."
  - q: "Does adding a non-alcoholic beer line change the capex evaluation framework?"
    a: "Yes in one important respect: NA beer dealcoholization equipment (reverse osmosis or vacuum distillation) is a relatively specialized capital investment with a narrower set of alternative uses if the NA line underperforms. The residual value risk is higher than for a standard fermenter, which can be repurposed across the beer portfolio. The hurdle rate applied to NA-specific capex should reflect that reduced optionality."
---

**Short answer:** The wrong time to evaluate a tank or canning line investment is when the production team says the brewery is running out of capacity. By that point, the decision is being made under operational pressure rather than analytical clarity. Breweries that build a standing capex framework — trigger metrics, payback model, scenario range — make better investments and avoid both under-building and over-building.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The operating loop this post describes"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE OPERATING LOOP</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Capex with Analytics: When to Add a Tank or a Canning Line</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Measure</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">data in</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analyse</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">find the signal</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Decide</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">choose</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Act</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">change the floor</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">repeat</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The operating loop this post describes: measure, analyse, decide, act — then repeat.</figcaption>
</figure>

## The Two Failure Modes of Brewery Capex

Brewery capital investment fails in predictable ways at both ends of the spectrum.

**Over-investment** is the more visible failure: a brewery buys two fermenters based on a demand forecast that doesn't materialize, runs the new tanks at 40% utilization, and carries depreciation that compresses margin for years. Lenders and investors see the asset on the balance sheet; they rarely see the opportunity cost of the working capital and interest expense it consumed.

**Under-investment** is less visible but equally costly: the brewery turns away orders, ships short against distributor commitments, misses seasonal windows, or — most expensively — loses distribution agreements because it cannot supply reliably. The lost margin from underfilled demand rarely appears as a line item anywhere in the management accounts.

An analytics-driven capex framework reduces both failure modes by making the investment trigger explicit and evidence-based rather than reactive.

## The Capex Trigger Framework

A practical trigger framework for production capacity investments has three components:

**Utilization threshold** — define a rolling utilization rate (for fermenters, expressed as tank-days occupied versus tank-days available; for the canning line, as hours run versus hours available) above which a capacity constraint is confirmed. A sustained peak utilization rate above 80–85% is a common threshold, but the right number depends on how much buffer the production schedule requires for cleaning, maintenance, and recipe changeovers.

**Lost margin calculation** — at the point the constraint is confirmed, quantify the volume the brewery cannot produce or ship against known demand. Multiply by the contribution margin per hL for the constrained SKU. This produces a concrete number: "we are leaving approximately X dollars of gross margin per quarter on the floor because of this constraint." That number is the economic case for the investment, stated in terms the board and lenders can evaluate.

**Payback model** — a realistic payback calculation at three volume scenarios (base, conservative, optimistic) using the actual capital cost, installation cost, incremental operating cost (additional labor, utilities, maintenance), and the incremental margin contribution. A tank that pays back in under three years at the conservative volume case is usually a straightforward approval. A tank that requires optimistic volume assumptions to reach a five-year payback is a strategic bet, and should be presented as one.

## Canning Line vs. Contract: The Build-or-Buy Decision

The decision between investing in an in-house canning line and continuing to use contract canning is one of the most common capex decisions in craft brewing, and one of the most frequently made on intuition rather than analysis.

The financial case should be built on a total cost per case comparison. In-house canning cost includes amortized capital (the line cost divided by useful life, divided by annual cans), direct labor, consumables (seaming compound, ink, CO2), maintenance allowance, and quality control overhead. Contract canning cost includes the contract rate per case, inbound and outbound freight, and a premium for lead time — contract lines often require four to eight weeks of planning horizon, which has a working capital cost and a responsiveness cost.

The break-even volume is the point at which in-house cost per case equals contract cost per case. For most mid-range canning lines, that break-even falls somewhere in the range of several hundred thousand cases annually, though the exact number varies significantly with line speed, labor cost, and contract pricing in the local market. The brewery's 3-year demand forecast, stress-tested against the scenario framework from [input cost scenario planning]({{ '/2025/scenario-planning-input-costs/' | relative_url }}), should be the input to that calculation — not the best-case volume assumption.

## The NA Beer Capex Case

Non-alcoholic beer introduces a specific capex consideration: dealcoholization equipment. Whether the investment is a reverse osmosis membrane system or a vacuum distillation unit, the capital is relatively specialized compared to a standard fermenter or canning line. The residual value if the NA line underperforms is lower, and the market for used dealcoholization equipment is thinner.

This does not argue against the investment — but it argues for applying a higher hurdle rate and requiring a more conservative payback case before approval. The working capital dynamics of NA — discussed in [working capital in brewing]({{ '/2025/working-capital-brewing/' | relative_url }}) — should also be incorporated into the total capital cost calculation, since NA inventory can turn more slowly than standard beer inventory.

## The Honest Limit

Capex analytics produces better-informed decisions, not correct ones. Demand forecasts can be wrong, installation costs can overrun, and market conditions can change between capital approval and full production. The discipline of building the framework is valuable even when the inputs are uncertain — it forces explicit assumption-making and creates a post-investment audit trail that improves future decisions.

*Part of the Financial Planning & Analytics track — [browse all]({{ '/tags/' | relative_url }}#fpna).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Start to finish, broken into the pieces that move the number."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">BRIDGE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Capex with Analytics: When to Add a Tank or a Canning Line</text><line x1="60" y1="250" x2="680" y2="250" stroke="#06483f" stroke-width="1.5"/><rect x="90" y="100" width="80" height="150" fill="#00695c"/><text x="130" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">Start</text><rect x="230" y="140" width="80" height="40" fill="#06483f"/><text x="270" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">−40</text><rect x="350" y="170" width="80" height="30" fill="#06483f"/><text x="390" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">−30</text><rect x="470" y="130" width="80" height="40" fill="#2e9e7c"/><text x="510" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">+40</text><rect x="590" y="130" width="80" height="120" fill="#00695c"/><text x="630" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">End</text><line x1="170" y1="100" x2="230" y2="100" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="310" y1="140" x2="350" y2="140" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="430" y1="170" x2="470" y2="170" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="550" y1="130" x2="590" y2="130" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Start to finish, broken into the pieces that move the number.</figcaption>
</figure>

## Frequently asked questions

**What financial metrics should drive a brewery's decision to add fermentation capacity?**
The primary metrics are tank utilization rate (if peak utilization is consistently above 85%, constraint costs are likely accruing), incremental margin contribution from the constrained volume (what gross margin is being lost to the capacity limit), and payback period on the new tank at realistic throughput assumptions. A tank sitting at 60% utilization with no credible demand signal does not justify the capital.

**How should a brewery evaluate a canning line investment versus contract canning?**
The comparison should be built on a total cost basis: in-house canning cost per case (amortized capital, direct labor, consumables, maintenance) versus contract canning cost per case including freight and lead time premium. The break-even volume threshold — the volume at which in-house is cheaper — should be modeled against the brewery's credible 3-year demand forecast. Below that threshold, contract canning preserves capital and maintains flexibility.

**Does adding a non-alcoholic beer line change the capex evaluation framework?**
Yes in one important respect: NA beer dealcoholization equipment (reverse osmosis or vacuum distillation) is a relatively specialized capital investment with a narrower set of alternative uses if the NA line underperforms. The residual value risk is higher than for a standard fermenter, which can be repurposed across the beer portfolio. The hurdle rate applied to NA-specific capex should reflect that reduced optionality.
