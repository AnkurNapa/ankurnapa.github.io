---
layout: post
title: "A Maturing-Stock Inventory and Valuation Dashboard in Tableau"
image: /assets/og/tableau-whisky-maturing-stock-valuation-dashboard.png
description: "Build a Tableau maturing-stock dashboard valuing whisky inventory by age, cask and strength, tracking tied-up capital and casks reaching age targets."
date: 2023-08-14
updated: 2023-08-14
tags: [distilling-maturation, tableau, inventory]
faq:
  - q: "How do I value maturing whisky stock in Tableau?"
    a: "Build calculated fields that apply a per-litre value driven by age band, cask type and strength, then aggregate with LOD expressions so each cask is valued once before rolling up to warehouse and company totals."
  - q: "Can the dashboard show which casks reach an age target?"
    a: "Yes. Use a parameter for the target age and a calculated field comparing it to each cask's maturation age, so finance and production can see how much stock crosses a threshold in any given period."
  - q: "Is the valuation reliable years ahead?"
    a: "Treat it as a scenario, not a forecast. Multi-year uncertainty in loss, market price and demand means the dashboard should show ranges and assumptions, not a single confident number."
---

**Short answer: a Tableau maturing-stock dashboard shows how much capital is locked in casks, how that value is spread across age and cask type, and when stock crosses the age targets that release it.** It is a finance tool as much as a production one, because the spirit was laid down years before anyone can sell it.

## The grain is a cask, the question is capital
Maturing whisky is the largest tied-up asset in most distilleries: spirit filled years ago, still aging, not yet sellable. The dashboard's job is to make that capital legible. Set the data grain at one row per cask, carrying fill date, cask type, current strength, current litres of pure alcohol after losses, and an age band. From there a calculated value field assigns a per-litre figure driven by age, cask and strength — older, sherry-matured, higher-strength stock is worth more per litre.

Use LOD expressions to value each cask exactly once: `{ FIXED [Cask ID] : ... }` prevents the double counting that wrecks naive sums when a user pivots by warehouse or year. Measure first — agree the valuation rule with finance — and the visuals follow easily.

## What the dashboard answers
Three questions earn their place. First, where is the capital? A treemap by age band and cask type shows concentration at a glance. Second, when does it unlock? A parameter for target age, compared against each cask's maturation age, reveals how many litres cross twelve, fifteen or eighteen years each quarter — directly feeding bottling and cash-flow plans. Third, how is it trending? A cumulative view of laid-down versus matured stock shows whether you are building or drawing down inventory.

Publish to Tableau Cloud with row-level security so finance sees company-wide value while a site manager sees only their warehouse. Tableau Pulse can then deliver a monthly digest to finance — "stock reaching 12 years rose 8% this quarter" — in plain language, without anyone building a report. For the selection angle, see [AI cask selection and inventory]({{ '/2024/ai-cask-selection-inventory/' | relative_url }}).

## Where it breaks
Every figure on this dashboard rests on assumptions. The per-litre values are estimates, sensitive to market conditions you do not control; the future losses are projected from a variable angel's share; and demand years out is genuinely unknown. A dashboard that prints one confident number invites bad decisions. Show the assumptions, let users flex them with parameters, and present value as a range. The dashboard's strength is making capital visible and testable — not pretending the future is settled.

## The bottom line
A maturing-stock dashboard in Tableau gives finance and production a shared, honest view of the asset that defines a whisky business: casks laid down long ago, slowly becoming sellable. Built on a clean per-cask grain with explicit valuation rules, it answers where the capital sits and when it unlocks. Keep the assumptions on the surface, treat long-range value as a scenario, and it becomes one of the most useful screens in the distillery.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.* Related: [AI cask selection and inventory]({{ '/2024/ai-cask-selection-inventory/' | relative_url }}).

## Frequently asked questions

**How do I value maturing whisky stock in Tableau?**
Build calculated fields that apply a per-litre value driven by age band, cask type and strength, then aggregate with LOD expressions so each cask is valued once before rolling up to warehouse and company totals.

**Can the dashboard show which casks reach an age target?**
Yes. Use a parameter for the target age and a calculated field comparing it to each cask's maturation age, so finance and production can see how much stock crosses a threshold in any given period.

**Is the valuation reliable years ahead?**
Treat it as a scenario, not a forecast. Multi-year uncertainty in loss, market price and demand means the dashboard should show ranges and assumptions, not a single confident number.
