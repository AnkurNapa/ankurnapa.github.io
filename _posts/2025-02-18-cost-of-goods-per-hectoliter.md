---
layout: post
title: "Cost of Goods per Hectoliter: The Number to Automate First"
description: "How breweries can automate cost of goods per hectoliter to get accurate, real-time production economics — including for NA beer."
date: 2025-02-18
updated: 2025-02-18
tags: [fpna, cost-accounting, brewing-economics]
faq:
  - q: "What is cost of goods per hectoliter in brewing?"
    a: "It is the total direct cost — raw materials, packaging, direct labor, and overhead allocated to production volume — divided by the hectoliters produced in a given period. It is the foundational unit economics metric for any brewery."
  - q: "Why is cost of goods per hectoliter harder to calculate for non-alcoholic beer?"
    a: "NA beer typically involves an additional dealcoholization step (vacuum distillation, reverse osmosis, or arrested fermentation), which adds energy, equipment depreciation, and sometimes yield loss. These costs must be correctly coded to the NA SKU, which many brewery ERP setups do not handle by default."
  - q: "How often should a brewery recalculate cost of goods per hectoliter?"
    a: "Best practice is monthly, aligned to a standard cost roll. High-volume or commodity-exposed operations benefit from a rolling 13-week view that refreshes whenever key input costs — malt, energy, aluminum — move more than a defined threshold."
---

**Short answer:** Cost of goods per hectoliter (COGS/hL) is the single most important unit-economics figure in a brewery's finance stack, and it is almost always calculated too infrequently, too manually, or with cost pools that quietly distort SKU-level truth. Automating it is not a technology project — it is a data discipline project that pays for itself within one budget cycle.

## Why This Number Is the Anchor of Every FP&A Conversation

Every material planning, pricing, and capital decision a brewery makes traces back to COGS/hL. Yet in most sub-200,000 hL operations the figure is produced once a quarter from a spreadsheet that pulls selectively from the ERP, applies a single overhead absorption rate across all brands, and lands on the CFO's desk three weeks after the period closes.

By then the number is historical trivia. The brew runs that drove the variance have already been replicated — or abandoned — on gut feel.

The goal of automation is not to eliminate accountants. It is to compress the feedback loop from thirty days to three, so the production and commercial teams are making decisions against current economics, not last quarter's.

## The Driver Tree Behind COGS/hL

A clean driver tree has four branches:

**Raw materials per hL** — malt, hops, adjuncts, yeast. The key variable is yield: actual extract efficiency against the theoretical. A 1% drop in brewhouse yield is invisible in the P&L until it compounds across a full quarter.

**Packaging per hL** — cans, glass, crowns, labels, secondary cartons. Aluminum in particular moves with commodity markets; a fixed-price assumption baked into an annual budget can be materially wrong within ninety days.

**Direct labor per hL** — shift hours charged to production, adjusted for volume throughput. Overtime loading and seasonal staffing changes distort this if labor is not mapped to brew batch IDs.

**Allocated overhead per hL** — depreciation, utilities, quality lab, maintenance. The absorption rate should be recalculated when capacity utilization shifts materially; using last year's rate on a half-empty cellar systematically understates true cost.

## Where NA Beer Breaks the Standard Model

Non-alcoholic beer adds a fifth cost node that standard brewery charts of accounts are not built for: the dealcoholization step. Whether the operation uses vacuum distillation, reverse osmosis, or a cold-contact arrested fermentation, there is incremental energy, incremental labor, and — in the case of RO or distillation — a meaningful yield loss that must be captured as a cost of the NA volume, not spread across the full brew.

The practical implication: if your ERP routes NA hL through the same cost center as your standard lager, your NA margin is almost certainly overstated and your standard lager margin is understated. Fixing the cost center mapping is a one-time configuration task, but it requires the finance team and the head brewer to agree on where dealcoholization begins and ends in the production workflow.

## The Automation Roadmap

The minimum viable automation stack does three things:

1. **Batch-level cost capture** — every brew batch gets a job order that captures actual grain usage, actual energy (sub-metered if possible), and actual labor hours at close. This is usually a configuration change in the existing ERP, not a new system.

2. **Commodity price refresh** — malt and aluminum contract prices feed into the standard cost file on a schedule that matches the purchasing cycle, so variances reflect real price moves rather than stale assumptions.

3. **Monthly COGS/hL dashboard** — a single view, by SKU and by channel, that shows actual versus standard cost, the three largest variance drivers, and a rolling 13-week trend. This can be built in Power BI, Tableau, or a well-governed spreadsheet connected to live ERP exports.

The honest limit: automation surfaces the numbers faster, but it cannot improve the underlying data quality if brew batch records are incomplete or overhead allocation logic is disputed between finance and operations. The governance work — agreeing on definitions — has to precede the tooling.

## The "So What" for Finance Leaders

A brewery that knows its COGS/hL by SKU, refreshed monthly, can do three things its competitors probably cannot: price with confidence when a distributor asks for a volume discount, identify which SKUs to rationalize before the next capacity crunch, and model the true economics of adding an NA line before committing to the capital. That is the payoff. The automation is just the means.

*Part of the Financial Planning & Analytics track — [browse all]({{ '/tags/' | relative_url }}#fpna).*

## Frequently asked questions

**What is cost of goods per hectoliter in brewing?**
It is the total direct cost — raw materials, packaging, direct labor, and overhead allocated to production volume — divided by the hectoliters produced in a given period. It is the foundational unit economics metric for any brewery.

**Why is cost of goods per hectoliter harder to calculate for non-alcoholic beer?**
NA beer typically involves an additional dealcoholization step (vacuum distillation, reverse osmosis, or arrested fermentation), which adds energy, equipment depreciation, and sometimes yield loss. These costs must be correctly coded to the NA SKU, which many brewery ERP setups do not handle by default.

**How often should a brewery recalculate cost of goods per hectoliter?**
Best practice is monthly, aligned to a standard cost roll. High-volume or commodity-exposed operations benefit from a rolling 13-week view that refreshes whenever key input costs — malt, energy, aluminum — move more than a defined threshold.
