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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Maturing-Stock Inventory and Valuation Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Maturing-Stock Inventory and Valuation Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## The grain is a cask, the question is capital
Maturing whisky is the largest tied-up asset in most distilleries: spirit filled years ago, still aging, not yet sellable. The dashboard's job is to make that capital legible. Set the data grain at one row per cask, carrying fill date, cask type, current strength, current litres of pure alcohol after losses, and an age band. From there a calculated value field assigns a per-litre figure driven by age, cask and strength — older, sherry-matured, higher-strength stock is worth more per litre.

Use LOD expressions to value each cask exactly once: `{ FIXED [Cask ID] : ... }` prevents the double counting that wrecks naive sums when a user pivots by warehouse or year. Measure first — agree the valuation rule with finance — and the visuals follow easily.

## What the dashboard answers
Three questions earn their place. First, where is the capital? A treemap by age band and cask type shows concentration at a glance. Second, when does it unlock? A parameter for target age, compared against each cask's maturation age, reveals how many litres cross twelve, fifteen or eighteen years each quarter — directly feeding bottling and cash-flow plans. Third, how is it trending? A cumulative view of laid-down versus matured stock shows whether you are building or drawing down inventory.

Publish to Tableau Cloud with row-level security so finance sees company-wide value while a site manager sees only their warehouse. Tableau Pulse can then deliver a monthly digest to finance — "stock reaching 12 years rose 8% this quarter" — in plain language, without anyone building a report. For the selection angle, see [AI cask selection and inventory]({{ '/2024/ai-cask-selection-inventory/' | relative_url }}).

## Where it breaks
Every figure on this dashboard rests on assumptions. The per-litre values are estimates, sensitive to market conditions you do not control; the future losses are projected from a variable angel's share; and demand years out is genuinely unknown. A dashboard that prints one confident number invites bad decisions. Show the assumptions, let users flex them with parameters, and present value as a range. The dashboard's strength is making capital visible and testable — not pretending the future is settled.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives maturation, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">A Maturing-Stock Inventory and Valuation Dashboard in Tableau</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Maturation</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">quality</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">What drives maturation, and what it changes downstream.</figcaption>
</figure>

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
