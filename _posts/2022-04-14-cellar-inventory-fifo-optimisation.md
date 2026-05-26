---
layout: post
title: "Cellar Inventory and FIFO Optimisation With AI"
image: /assets/og/cellar-inventory-fifo-optimisation.png
description: "How shelf-life-aware FIFO and allocation across brewery tanks and finished stock cut waste while holding fill rate, and where the approach breaks down."
date: 2022-04-14
updated: 2022-04-14
tags: [brewing-science, inventory, process-optimization]
faq:
  - q: "Why does a brewery need more than basic FIFO?"
    a: "Plain FIFO ships the oldest stock first, which is sensible but blunt. Beer is perishable across both bright tanks and finished goods, so a shelf-life-aware approach also weighs how much freshness each order needs, what changeovers cost, and which allocation keeps fill rate high while waste low — decisions basic FIFO ignores."
  - q: "What does the optimiser balance?"
    a: "It balances three things that pull against each other: product freshness, fill rate, and changeover cost. Shipping the freshest beer to every order maximises quality but can strand older stock; minimising changeovers is efficient but can let stock age out. The optimiser finds an allocation that respects all three."
  - q: "Is this worth it for a small brewery?"
    a: "Often not. If you turn stock quickly and rarely write any off, the spreadsheet is doing fine and an optimiser is overkill. The payback appears when you carry many SKUs, hold stock long enough that ageing is a real cost, and lose meaningful product to expiry."
---

**Short answer: shelf-life-aware FIFO and allocation cut waste by deciding which perishable stock to ship where, while still holding your fill rate.** Beer ages in the bright tank and on the pallet alike, so inventory decisions are quietly time-critical. Optimisation can sharpen them — when the problem is big enough to warrant it.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Cellar Inventory and FIFO Optimisation With AI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Why perishability changes the inventory game
In many industries inventory is fungible: a widget is a widget. Beer is not. A batch has a shelf life, and its value to a customer depends on how fresh it arrives. That perishability runs through both fermenting and bright tanks and through finished stock waiting to ship. The result is that two decisions which look identical on a stock report — ship pallet A or pallet B — can have very different consequences for waste and quality.

FIFO is the sensible default: move the oldest first. But it is a blunt rule. It does not weigh how much freshness a particular order actually needs, what a changeover between SKUs costs on the line, or how an allocation today strands stock tomorrow. Shelf-life-aware optimisation takes those factors into account, balancing freshness, fill rate, and changeovers across the whole order book rather than one line at a time.

This sits naturally downstream of your brew plan — what you allocate depends on what you made and when. If you have not read it, [AI for brewery production scheduling]({{ '/2021/ai-brewery-production-scheduling/' | relative_url }}) covers the upstream decision that feeds this one.

## Measure first: shelf-life data is the foundation
None of this works without trustworthy perishability data. You need real fill dates, real best-before logic per product, and an inventory record that actually matches the cellar. The discipline is the familiar one — measure the process before you model it. If your stock system says a tank is full when it was emptied last week, the optimiser will confidently allocate beer that does not exist.

So the first job is not the algorithm; it is accurate, current stock and shelf-life data. Get that right and even simple shelf-life-aware FIFO will cut waste. Get it wrong and the most sophisticated optimiser will simply automate your errors at speed.

## Where it breaks
Two honest limits. The first is data quality. Perishability optimisation is acutely sensitive to bad dates and stale stock records — more so than scheduling, because the whole point is to reason about age. If those inputs are shaky, do not deploy yet.

The second is scale. For a small brewery turning stock fast with few SKUs and negligible write-offs, this is over-engineering. The honest answer is that a clean FIFO spreadsheet is the right tool until waste, SKU count, and holding times grow enough that the trade-offs genuinely bite. Optimisation earns its place by reducing a cost you can actually measure; if that cost is near zero, leave it alone.

## A practical gen-AI angle
A modest, well-grounded use of generative AI fits neatly here. A copilot watching stock ages can flag which lots are at risk of expiring before they are likely to ship, and draft the allocation note or customer communication that goes with rerouting them — "lot 1142 is nine days from best-before; suggest allocating to the Tuesday wholesale run." It surfaces the at-risk stock a busy cellar manager would otherwise miss and turns the decision into a quick yes or no. As always, it must read from the real inventory record and cite the lots, not invent them.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Cellar Inventory and FIFO Optimisation With AI</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Process</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

## The bottom line
Shelf-life-aware FIFO and allocation cut waste while protecting fill rate by treating beer as the perishable, time-sensitive product it is. The catch is that it depends entirely on accurate stock and shelf-life data, and it only pays back once your SKU count and holding times make ageing a real cost — small, fast-turning breweries should stick with simple FIFO. Measure first, deploy where waste is genuinely measurable, and let a grounded copilot flag the lots at risk.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*

## Frequently asked questions

**Why does a brewery need more than basic FIFO?**
Plain FIFO ships the oldest stock first, which is sensible but blunt. Beer is perishable across both bright tanks and finished goods, so a shelf-life-aware approach also weighs how much freshness each order needs, what changeovers cost, and which allocation keeps fill rate high while waste low — decisions basic FIFO ignores.

**What does the optimiser balance?**
It balances three things that pull against each other: product freshness, fill rate, and changeover cost. Shipping the freshest beer to every order maximises quality but can strand older stock; minimising changeovers is efficient but can let stock age out. The optimiser finds an allocation that respects all three.

**Is this worth it for a small brewery?**
Often not. If you turn stock quickly and rarely write any off, the spreadsheet is doing fine and an optimiser is overkill. The payback appears when you carry many SKUs, hold stock long enough that ageing is a real cost, and lose meaningful product to expiry.
