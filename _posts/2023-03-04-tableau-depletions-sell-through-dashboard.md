---
layout: post
title: "A Depletions and Sell-Through Dashboard in Tableau"
image: /assets/og/tableau-depletions-sell-through-dashboard.png
description: "Build a depletions and sell-through dashboard in Tableau using LOD expressions, YoY table calcs and Pulse to spot accounts slowing down."
date: 2023-03-04
updated: 2023-03-04
tags: [sales-intelligence, tableau, analytics]
faq:
  - q: "What is the difference between depletions and shipments?"
    a: "Shipments are cases you sell into a distributor; depletions are cases the distributor sells out to retail accounts. Depletions are the truer demand signal, but they arrive later and depend on distributor reporting."
  - q: "How do I calculate sell-through rate in Tableau?"
    a: "Use a FIXED LOD expression to pin depletions and inventory at the account-SKU grain, then divide depletions by the sum of opening inventory plus shipments. This keeps the rate stable regardless of dashboard filters."
  - q: "Can Tableau alert me when an account starts slowing down?"
    a: "Yes. Tableau Pulse can monitor depletion velocity per account and send a natural-language digest when a metric falls outside its expected range, but it flags the change rather than diagnosing the cause."
---

**Short answer: depletions, not shipments, are the demand signal worth watching — and a well-built Tableau view makes sell-through legible per account and SKU.** Shipments tell you what left your warehouse; depletions tell you what the market actually pulled. The gap between them sits in a distributor's cellar, and that is where revenue quietly stalls.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Depletions and Sell-Through Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Depletions and Sell-Through Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Measure first, visualise second

Before opening Tableau, define the measures. The temptation is to build a chart and reverse-engineer the metric, which is how teams end up arguing about numbers in the meeting rather than acting on them. Decide three things up front: the grain (account by SKU by month), the demand metric (depletions in cases or nine-litre equivalents), and the efficiency metric (sell-through rate).

Sell-through rate is depletions divided by available stock — opening inventory plus shipments in the period. In Tableau, pin both sides with a FIXED level-of-detail expression so the ratio stays correct when a user filters to one brand or one chain:

`{ FIXED [Account], [SKU] : SUM([Depletion Cases]) } / { FIXED [Account], [SKU] : SUM([Opening Inv]) + SUM([Shipment Cases]) }`

FIXED ignores the dashboard's filter context, so the denominator does not shrink when someone drills in. That single discipline prevents most of the "why does the percentage change when I click" complaints.

## The dashboard layout

Lead with the shipments-versus-depletions divergence, because that is the headline insight. A dual-axis line — shipments as a faint band, depletions as the bold line — instantly shows when you are selling in faster than the market is pulling out. Add a YoY growth column using a table calculation (`(ZN(SUM([Depletions])) - LOOKUP(ZN(SUM([Depletions])), -12)) / ABS(LOOKUP(...))`) computed along the month axis, so a national manager sees momentum, not just absolute volume.

The workhorse view is a highlight table of accounts down the rows and recent months across the columns, coloured by sell-through rate. Hot cells are healthy; cool cells are stock that is not moving. Add a parameter that swaps the geographic dimension — territory, state, distributor — so one dashboard serves the field rep and the VP without duplicating sheets. Parameter actions let a click on a region filter the detail panel beneath, keeping navigation inside the canvas rather than scattered across tabs.

Layer the AI on top, not underneath. Tableau Pulse can watch depletion velocity per key account and issue a plain-language digest — "Depletions for Account 4471 are down 18% versus the trailing trend" — to the rep's inbox. That is genuine value: it draws a human's eye to the right row. It is monitoring, though, not diagnosis. Pulse tells you the account slowed; it cannot tell you the chain reset its planogram or a competitor bought the end-cap.

## Where it breaks

The honest constraint is upstream. Depletion data is only as timely and clean as your distributor feeds, and those often lag two to six weeks, arrive in inconsistent formats, or net out returns silently. A beautiful sell-through heatmap built on a fortnight-old, half-mapped feed will mislead with great confidence. Tableau Prep can standardise and dedupe the incoming files, but it cannot invent data a distributor never sent. Map your SKUs and accounts to a master list before trusting a single percentage — unmatched rows quietly vanish from FIXED totals and skew the rate.

Equally, sell-through is a ratio, and ratios hide volume. A 95% sell-through on four cases is noise; treat tiny denominators with suspicion and consider suppressing accounts below a minimum stock threshold.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Each stage loses some — the funnel shows where the drop-off is."><rect x="0" y="0" width="720" height="310" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">A Depletions and Sell-Through Dashboard in Tableau</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#b45309" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reach · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#b45309" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interest · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#b45309" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Trial · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#b45309" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Win · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Each stage loses some — the funnel shows where the drop-off is.</figcaption>
</figure>

## The bottom line

A depletions dashboard earns its keep by making the shipments-to-market gap impossible to ignore, with LOD-backed sell-through that survives filtering and YoY table calcs that show momentum. Let Pulse flag the slowdowns and let a human work out why. The dashboard is only as honest as the distributor feed beneath it, so invest in the data plumbing before the visuals.

*Part of the [Sales Intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) track.* Related: [Building a Distributor Scorecard in Tableau]({{ '/2023/tableau-distributor-scorecard/' | relative_url }}).

## Frequently asked questions

**What is the difference between depletions and shipments?**
Shipments are cases you sell into a distributor; depletions are cases the distributor sells out to retail accounts. Depletions are the truer demand signal, but they arrive later and depend on distributor reporting.

**How do I calculate sell-through rate in Tableau?**
Use a FIXED LOD expression to pin depletions and inventory at the account-SKU grain, then divide depletions by the sum of opening inventory plus shipments. This keeps the rate stable regardless of dashboard filters.

**Can Tableau alert me when an account starts slowing down?**
Yes. Tableau Pulse can monitor depletion velocity per account and send a natural-language digest when a metric falls outside its expected range, but it flags the change rather than diagnosing the cause.
