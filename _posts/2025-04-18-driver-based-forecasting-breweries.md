---
layout: post
title: "Driver-Based Forecasting: Beyond the Annual Budget"
image: /assets/og/driver-based-forecasting-breweries.png
description: "Driver-based forecasting replaces static brewery budgets with dynamic models tied to real volume, mix, and cost drivers — including for NA beer."
date: 2025-04-18
updated: 2025-04-18
tags: [fpna, forecasting, budgeting]
faq:
  - q: "What is driver-based forecasting for a brewery?"
    a: "Driver-based forecasting builds the financial forecast from operational inputs — brew batches planned, hL per SKU, headcount per shift, commodity contract prices — rather than from last year's numbers with a percentage adjustment. The P&L becomes a downstream output of the operating model, not a starting point."
  - q: "How does driver-based forecasting handle non-alcoholic beer volume differently?"
    a: "NA beer often has a different demand seasonality than regular beer — the peak months can shift toward January and summer dry periods rather than traditional on-premise seasons. A driver-based model captures this by using NA-specific volume drivers rather than applying a blanket growth rate to the total portfolio."
  - q: "What is the biggest obstacle to driver-based forecasting in small and mid-size breweries?"
    a: "Data fragmentation. Volume data lives in the brewing system, price data in distributor portals, and cost data in the ERP. Until those three sources feed a single model, every forecast refresh is a manual reconciliation exercise that consumes the time it was supposed to save."
---

**Short answer:** The annual budget is the wrong tool for a business where barley prices can move 20% in a quarter, NA beer demand is reshaping the summer sales curve, and a single large wholesale account can shift your channel mix overnight. Driver-based forecasting replaces the calendar-driven ritual with a living model that updates whenever the inputs that actually drive your economics change.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The operating loop this post describes"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">THE OPERATING LOOP</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Driver-Based Forecasting: Beyond the Annual Budget</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Measure</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">data in</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analyse</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">find the signal</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Decide</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">choose</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Act</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">change the floor</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,52 840,52 800,52 L160,52 C140,52 140,52 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="46" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">repeat</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The operating loop this post describes: measure, analyse, decide, act — then repeat.</figcaption>
</figure>

## What "Driver-Based" Actually Means

Most brewery budgets are built by starting with last year's revenue line, applying a growth assumption, and then stress-testing whether the cost structure is affordable at that revenue level. The result is a document that is accurate on the day it is signed and increasingly fictional for the eleven months that follow.

Driver-based forecasting inverts the logic. The model starts with the operational drivers — planned brew schedule, SKU mix, price per hL by channel, and commodity contract prices — and derives the financials from those inputs. When a driver changes, the P&L and cash flow update automatically.

The distinction matters because it changes who owns the forecast. In a driver-based model, the head brewer's decision to shift two batch runs from a high-gravity seasonal to a standard lager has an immediate, visible financial consequence. That transparency creates accountability that a spreadsheet budget cannot.

## Building the Driver Tree

A brewery driver tree typically has three tiers:

**Volume drivers** — brew batches planned, expected yield loss, hL by SKU, projected sell-through by channel (on-premise, off-premise, DTC, export). Volume is the master lever; everything else scales from it.

**Price and mix drivers** — average net revenue per hL by channel, trade spend rate, and SKU mix. A shift toward NA beer — which often carries a higher gross price but also higher production cost — changes the mix-adjusted margin even if total volume is flat. This is where many brewery forecasts go wrong: they model total hL but not mix.

**Cost drivers** — standard COGS per hL (see the [cost of goods per hectoliter post]({{ '/2025/cost-of-goods-per-hectoliter/' | relative_url }})), commodity price assumptions, headcount per shift, and utility rates. Each of these should have a named assumption owner who is responsible for refreshing it when market conditions change.

## The Reforecasting Cadence

An annual budget with one mid-year reforecast is not a forecast — it is two budgets. A driver-based model enables a rolling forecast on a monthly or quarterly cadence without the political weight of a "budget revision."

The practical cadence for most breweries: a monthly flash focused on the top three volume and cost drivers, a quarterly rolling 12-month reforecast that updates all assumptions, and a scenario refresh whenever a macro input — grain, energy, aluminum — moves outside the tolerance range defined in the model.

## NA Beer as a Forecasting Challenge

Non-alcoholic beer complicates the forecast in two ways that deserve explicit treatment.

First, demand seasonality differs. Standard beer peaks in summer on-premise. NA beer sees demand spikes tied to dry-month campaigns and wellness trends that do not follow the same curve. Applying a standard seasonal index to NA volume will systematically under-forecast January and over-forecast May.

Second, the cost structure is different enough that NA hL should have its own driver row in the model, not be folded into a blended average. The dealcoholization cost, the often-smaller batch sizes, and the packaging mix (cans versus kegs) can make NA's unit economics look very different from the flagship lager — better in some channels, worse in others.

## Where Driver-Based Models Break Down

The honest caveat: a driver-based model is only as good as the discipline behind its inputs. If the commercial team is not updating volume assumptions monthly, if the purchasing team is not flagging commodity contract changes, and if the operations team is not recording actual batch yields, the model drifts back toward being a sophisticated-looking spreadsheet that nobody trusts.

The solution is governance, not more technology. Assign a named owner to each driver, define a refresh schedule, and build a simple variance report that shows when an assumption has deviated more than a defined threshold from actuals. The AI-assisted forecasting tools discussed in [AI demand forecasting for breweries]({{ '/2026/ai-demand-forecasting-for-breweries/' | relative_url }}) can help with the volume layer, but the cost and price drivers still require human judgment.

*Part of the Financial Planning & Analytics track — [browse all]({{ '/tags/' | relative_url }}#fpna).*

## Frequently asked questions

**What is driver-based forecasting for a brewery?**
Driver-based forecasting builds the financial forecast from operational inputs — brew batches planned, hL per SKU, headcount per shift, commodity contract prices — rather than from last year's numbers with a percentage adjustment. The P&L becomes a downstream output of the operating model, not a starting point.

**How does driver-based forecasting handle non-alcoholic beer volume differently?**
NA beer often has a different demand seasonality than regular beer — the peak months can shift toward January and summer dry periods rather than traditional on-premise seasons. A driver-based model captures this by using NA-specific volume drivers rather than applying a blanket growth rate to the total portfolio.

**What is the biggest obstacle to driver-based forecasting in small and mid-size breweries?**
Data fragmentation. Volume data lives in the brewing system, price data in distributor portals, and cost data in the ERP. Until those three sources feed a single model, every forecast refresh is a manual reconciliation exercise that consumes the time it was supposed to save.
