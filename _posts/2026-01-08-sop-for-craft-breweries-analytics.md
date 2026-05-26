---
layout: post
title: "S&OP for Craft: An Analytics Playbook to Match Supply and Demand"
image: /assets/og/sop-for-craft-breweries-analytics.png
description: "Sales and operations planning for craft breweries: a practical analytics playbook that connects demand signals to production scheduling and closes the forecast gap."
date: 2026-01-08
updated: 2026-01-08
tags: [commercial-planning, sop, supply-demand-planning]
faq:
  - q: "What is sales and operations planning (S&OP) for a craft brewery?"
    a: "S&OP is a regular cross-functional process — typically monthly — that reconciles the demand plan (what the sales team expects to sell) with the supply plan (what the brewery can produce and package) and the financial plan (what the business has committed to deliver). The output is a single agreed production and supply schedule that every function trusts and plans against."
  - q: "How is craft brewery S&OP different from large-format CPG S&OP?"
    a: "The process logic is the same, but the data sources, cycle times, and organisational dynamics are different. Craft breweries typically have shorter production lead times, more volatile demand patterns (driven by seasonal releases and taproom traffic), less historical data for statistical forecasting, and a much smaller team to run the process. The playbook needs to be proportionate to those realities — a two-hour monthly meeting is often more valuable than a full enterprise IBP cycle."
  - q: "Where does AI help most in a brewery S&OP process?"
    a: "AI adds the most value in demand signal processing — identifying patterns in distributor sell-out data, taproom transaction history, and seasonal indicators that improve the statistical baseline forecast. The S&OP process itself — the cross-functional reconciliation meeting and the decisions it produces — is a human process that AI supports but does not replace."
---

**Short answer: Sales and operations planning is the management process that turns a demand forecast into a production schedule and a financial commitment. Most craft breweries do some version of this informally; the gap between informal and structured S&OP is where inventory overruns, stock-outs, and margin surprises are born. An analytics playbook does not need to be complex to close that gap — it needs to be consistent.**

S&OP has a reputation for being the domain of large food and beverage companies with dedicated planning teams and expensive software. That reputation is partly earned and partly a failure of imagination. The underlying logic — reconcile demand, supply, and finance into a single agreed plan, regularly, before decisions become crises — is scale-independent. A craft brewery with three brands and two tank sizes benefits from that logic as much as a national brewer with 200 SKUs.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The operating loop this post describes"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">THE OPERATING LOOP</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">S&amp;OP for Craft: An Analytics Playbook to Match Supply and Demand</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Measure</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">data in</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analyse</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">find the signal</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Decide</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">choose</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Act</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">change the floor</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,52 840,52 800,52 L160,52 C140,52 140,52 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="46" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">repeat</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The operating loop this post describes: measure, analyse, decide, act — then repeat.</figcaption>
</figure>

## The Four Steps of a Lean Brewery S&OP Cycle

**Step 1 — Demand review (week 1 of the month)**: Gather all available demand signals and produce an updated volume forecast by brand, by channel, for the next 12 weeks. At minimum, this means reviewing distributor order history and any confirmed sales commitments. Better inputs include retailer scan data, taproom transaction trends, and seasonal event calendars. The output is a single unconstrained demand plan — what the market would take if supply were unlimited.

**Step 2 — Supply review (week 2)**: The production and operations team reviews the demand plan against tank availability, raw material inventory, and packaging line capacity. The output is a constrained supply plan — what can actually be produced and packaged within the physical constraints of the brewery in the next 12 weeks.

**Step 3 — Pre-S&OP reconciliation (week 3)**: The commercial and operations leads compare the unconstrained demand plan with the constrained supply plan. Gaps — where demand exceeds supply, or where supply would exceed demand and create inventory risk — are identified and options for resolution are developed before the executive meeting.

**Step 4 — Executive S&OP meeting (week 4)**: The brewery owner or leadership team reviews the reconciled plan, makes decisions on unresolved gaps, and approves the agreed production schedule and financial outlook. This meeting should be 60–90 minutes; if it regularly runs longer, the pre-S&OP reconciliation is not doing its job.

## The Analytics That Power Each Step

**Demand review analytics**:
- Statistical baseline forecast using the most recent 12–24 weeks of shipment data, adjusted for seasonality
- Promotional event calendar overlay: where does a known promotional event or seasonal release affect the baseline?
- Taproom trend analysis: is taproom traffic trending up or down relative to seasonal norms?
- NA beer demand modelling: if the portfolio includes NA lines, track them separately — their seasonality and demand drivers differ materially from alcoholic lines

**Supply review analytics**:
- Tank utilisation model: current occupancy, expected fermentation and conditioning cycle times, projected availability by week
- Raw material coverage: current hop, malt, and adjunct inventory against the demand plan requirements
- Packaging line schedule: is there sufficient packaging capacity to process the fermented volume on time?

**Gap analysis**:
- Volume gap by brand: demand minus supply, by week, expressed in hectolitres or barrels
- Inventory risk flag: weeks where supply exceeds demand and would build inventory beyond safe holding levels
- Financial impact: the revenue and margin implication of the unresolved gaps, to frame executive decisions

## The Forecast Accuracy Diagnostic

A critical but often neglected S&OP metric is forecast accuracy — how closely the demand plan from four to eight weeks ago matched actual shipments. Tracking forecast accuracy at the brand level over time reveals which parts of the portfolio are structurally hard to forecast (typically seasonal and limited releases) and which should be more forecastable but aren't (often because the commercial process is informal rather than because the product is genuinely unpredictable).

For context on the AI tools that sharpen the demand forecasting step, see [AI Demand Forecasting for Breweries]({{ '/2026/ai-demand-forecasting-for-breweries/' | relative_url }}).

## The NA Beer Scheduling Complication

Non-alcoholic beer adds a specific complication to brewery S&OP that is worth flagging explicitly. If the brewery uses a dealcoholisation step — whether vacuum distillation, membrane filtration, or arrested fermentation — the production lead time and capacity constraints are different from standard beer. NA production often competes for the same packaging lines as alcoholic beer but uses different tank and processing equipment. The supply model needs to treat NA as a separate supply chain with its own constraints, not simply another brand in the standard production schedule.

## Where This Approach Breaks Down

Honest caveat: S&OP only works if the commercial team provides honest demand signals and the operations team provides accurate capacity data. In breweries where the culture rewards optimism in forecasting (to avoid being seen as sandbagging sales targets) and conservatism in capacity planning (to avoid being committed to schedules that are difficult to meet), the S&OP process will produce a plan that nobody believes and that everyone routes around with informal side-agreements. The process is a forcing function for commercial honesty — which makes it culturally uncomfortable before it is operationally useful.

*Part of the Commercial Planning Analytics track — [browse all]({{ '/tags/' | relative_url }}#commercial-planning).*

## Frequently asked questions

**What is sales and operations planning (S&OP) for a craft brewery?**

S&OP is a regular cross-functional process — typically monthly — that reconciles the demand plan (what the sales team expects to sell) with the supply plan (what the brewery can produce and package) and the financial plan (what the business has committed to deliver). The output is a single agreed production and supply schedule that every function trusts and plans against.

**How is craft brewery S&OP different from large-format CPG S&OP?**

The process logic is the same, but the data sources, cycle times, and organisational dynamics are different. Craft breweries typically have shorter production lead times, more volatile demand patterns (driven by seasonal releases and taproom traffic), less historical data for statistical forecasting, and a much smaller team to run the process. The playbook needs to be proportionate to those realities — a two-hour monthly meeting is often more valuable than a full enterprise IBP cycle.

**Where does AI help most in a brewery S&OP process?**

AI adds the most value in demand signal processing — identifying patterns in distributor sell-out data, taproom transaction history, and seasonal indicators that improve the statistical baseline forecast. The S&OP process itself — the cross-functional reconciliation meeting and the decisions it produces — is a human process that AI supports but does not replace.
