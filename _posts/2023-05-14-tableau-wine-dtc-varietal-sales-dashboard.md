---
layout: post
title: "A Wine DTC and Varietal Sales Dashboard in Tableau"
image: /assets/og/tableau-wine-dtc-varietal-sales-dashboard.png
description: "Build a Tableau wine sales dashboard comparing DTC and distribution, sales by varietal, region and vintage, with club retention and a market map."
date: 2023-05-14
updated: 2023-05-14
tags: [winemaking, tableau, sales]
faq:
  - q: "What should a wine sales dashboard in Tableau cover?"
    a: "Direct-to-consumer channels — cellar door, club and e-commerce — against distribution, plus sales broken down by varietal, region and vintage, and club retention over time. A market map adds the geographic view."
  - q: "How do I compare DTC and distribution margins in Tableau?"
    a: "Bring both channels into one source with a consistent channel field, then build a calculated field for margin per channel. A side-by-side bar makes the margin gap between DTC and distribution obvious."
  - q: "Can Tableau forecast wine sales by vintage?"
    a: "The built-in exponential-smoothing forecast gives a rough trend, but vintage volumes are finite and seasonal, so treat it as indicative. For real planning, model demand externally and visualise the result."
---

**Short answer: a wine sales dashboard works when it puts DTC against distribution, breaks revenue down by varietal, region and vintage, and tracks club retention — so you see where the margin really comes from.** Agree the channel definitions before you build, or the comparison is meaningless.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Wine DTC and Varietal Sales Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Wine DTC and Varietal Sales Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Define channels and margin first
The measure-first question is "which channel and which wine actually make money?" DTC and distribution behave nothing alike — cellar door, club and e-commerce carry far higher margin than a distributor sale, but lower volume. So the first job is a clean channel field and a margin calculation per channel, agreed with whoever owns the numbers. Varietal, region and vintage are your dimensions; revenue, units, margin and club retention are your measures.

Sales data usually arrives from more than one system — an e-commerce platform, a club tool, a distributor report — so Tableau Prep is essential to unify them into one source with consistent channel, varietal and vintage fields. Connect as a refreshed extract; sales rarely need a live feed.

## Build the channel and market views
Lead with a DTC-versus-distribution comparison: revenue and margin side by side, so the high-margin DTC story is visible against the high-volume distribution story. A FIXED level-of-detail calculation — `{FIXED [Varietal], [Vintage] : SUM([Revenue])}` — lets you build varietal-by-vintage breakdowns that hold steady regardless of other filters.

Add a market map using geographic roles so distribution and e-commerce sales appear by region, sized by revenue and coloured by margin — useful for spotting where a varietal sells. Track club retention as a cohort or simple retention curve by join month. Filter actions tie it together: click a varietal and every view reflows to that wine, with row-level security so a regional manager sees only their territory.

## Let Pulse watch the numbers that move
Set Tableau Pulse on club retention and DTC revenue, and it sends a natural-language digest when something shifts — "Club retention down two points this quarter" — before it shows up in a monthly report. Einstein Copilot can help a non-analyst ask "which varietal grew fastest in DTC last quarter" in plain language and get a chart back.

## Where it breaks
The honest limits are about data and sample size. Channel data lives in silos, and a distributor depletion report may lag weeks behind your DTC sales, so the comparison is never perfectly contemporaneous — be clear in the title which channels are current. Small wineries also hit small-sample problems: a club cohort of forty members produces a retention curve that swings wildly on a handful of cancellations, so do not over-read it. And the built-in forecast does not know a vintage is nearly sold out; it will project sales of wine that no longer exists.

## The bottom line
A Tableau wine sales dashboard ties channels together: DTC against distribution, revenue by varietal, region and vintage, club retention and a market map, with Pulse flagging the metrics that move. Define channels and margin first, mind the silos and small samples, and treat the built-in forecast as a hint rather than a plan.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [a cellar and barrel-ageing inventory dashboard in Tableau]({{ '/2023/tableau-wine-cellar-barrel-ageing-dashboard/' | relative_url }}).

## Frequently asked questions

**What should a wine sales dashboard in Tableau cover?**
Direct-to-consumer channels — cellar door, club and e-commerce — against distribution, plus sales broken down by varietal, region and vintage, and club retention over time. A market map adds the geographic view.

**How do I compare DTC and distribution margins in Tableau?**
Bring both channels into one source with a consistent channel field, then build a calculated field for margin per channel. A side-by-side bar makes the margin gap between DTC and distribution obvious.

**Can Tableau forecast wine sales by vintage?**
The built-in exponential-smoothing forecast gives a rough trend, but vintage volumes are finite and seasonal, so treat it as indicative. For real planning, model demand externally and visualise the result.
