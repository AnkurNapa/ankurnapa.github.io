---
layout: post
title: "Cellar Inventory and FIFO Optimisation With AI"
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
