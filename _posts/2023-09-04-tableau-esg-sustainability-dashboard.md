---
layout: post
title: "An ESG Sustainability Dashboard in Tableau (Water, Energy, Carbon per hl)"
image: /assets/og/tableau-esg-sustainability-dashboard.png
description: "Build an ESG dashboard in Tableau tracking water-to-beer ratio, energy per hl and carbon by scope against targets, with Pulse digests and honest data caveats."
date: 2023-09-04
updated: 2023-09-04
tags: [esg, tableau, sustainability]
faq:
  - q: "What are the core ESG metrics for a brewery dashboard?"
    a: "Water-to-beer ratio (hl water per hl beer), energy intensity (kWh or MJ per hl), and carbon emissions by scope (1, 2 and ideally 3) per hl. Normalising per hl makes sites of different sizes comparable."
  - q: "How do I calculate carbon emissions in Tableau?"
    a: "Multiply activity data, such as gas or electricity consumption, by an emission factor in a calculated field. The number is only as good as the factor, so store factors as a maintained reference table, not hard-coded constants."
  - q: "Can a dashboard prevent greenwashing?"
    a: "It can help by making boundaries, factors and assumptions explicit, but it cannot prevent selective reporting. Greenwashing is a governance problem; the dashboard's role is to show the full picture honestly, including the bad trends."
---

**Short answer: an ESG dashboard lives or dies on data quality and clearly stated boundaries, not on the cleverness of the chart.** The hard part is not visualising water, energy and carbon; it is trusting the numbers you feed in.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for An ESG Sustainability Dashboard in Tableau (Water, Energy, Carbon per hl)"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">An ESG Sustainability Dashboard in Tableau (Water, Energy, Carbon per hl)</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Pick the intensity measures first
Sustainability data is easy to manipulate by switching between absolute and intensity views, so decide upfront. For a brewery, three normalised measures do most of the work: water-to-beer ratio (hl of water per hl of beer), energy intensity (kWh or MJ per hl), and carbon per hl split by scope. Per-hl normalisation is the data-science discipline that lets a small craft site and a large regional plant sit on the same chart fairly. Show absolute totals too, because a falling intensity with rising volume can still mean rising total emissions, but lead with intensity for operational accountability.

## Build it: calculated fields, targets and site comparison
Each metric is a calculated field. Water ratio is total water volume divided by total production volume. Carbon is the interesting one: activity data times an emission factor. Resist hard-coding factors into the calc, they change annually and vary by region, so join a maintained emission-factor reference table and compute:

`SUM([Gas kWh]) * [Gas Emission Factor] + SUM([Electricity kWh]) * [Grid Factor]`

Keep scopes separate. Scope 1 (direct combustion), Scope 2 (purchased electricity), and Scope 3 (everything upstream and downstream, packaging, distribution, agriculture) behave differently and have very different data confidence. Show them as stacked or small-multiple views so no one reads a tidy Scope 1 trend as the whole carbon story.

Plot each metric against target. A reference line for the annual target plus a colour-coded variance turns the dashboard into a management tool rather than a record. For site comparison, a small-multiples layout or a ranked bar lets the head of operations see which plant drags the average. Tableau Prep handles the messy reality of monthly meter readings arriving in different units and timestamps. Finally, point Tableau Pulse at the headline intensity metrics so the sustainability team receives a monthly natural-language digest, useful when feeding board and regulatory reporting cycles.

## Where it breaks: boundaries, factors and greenwashing
This is where ESG dashboards quietly mislead. Three failure modes recur. First, boundaries: if Site A meters incoming water at the mains and Site B meters it after treatment, your comparison is nonsense, and the chart will not warn you. Second, emission factors: Scope 3 in particular leans on estimates and industry averages, so a confident carbon-per-hl figure can carry a wide, invisible error bar. Third, greenwashing risk: a dashboard makes it trivially easy to feature the flattering metric and bury the rising one. The countermeasure is transparency on the canvas itself, footnote the boundary, name the factor source, and never hide a deteriorating trend behind a tab no one opens.

Generative AI adds a subtler hazard. A Pulse digest that narrates "carbon intensity improved 8%" reads as a clean fact, but it cannot see that half the improvement came from a methodology change in your emission factors. Keep a human, ideally with a sustainability-reporting background, between the AI narrative and any external disclosure.

## The bottom line
Build the ESG dashboard on normalised intensity metrics, separate the carbon scopes, and treat emission factors as maintained reference data rather than constants. Use Pulse to streamline routine reporting, but put boundaries and assumptions on the dashboard so the numbers can be defended. The chart is the easy 20%; the trustworthy data foundation is the 80% that actually matters.

*Part of the [ESG]({{ '/tracks/esg/' | relative_url }}) track.* Related: [building a brewery data foundation for AI]({{ '/2024/building-brewery-data-foundation-ai/' | relative_url }}).

## Frequently asked questions

**What are the core ESG metrics for a brewery dashboard?**
Water-to-beer ratio (hl water per hl beer), energy intensity (kWh or MJ per hl), and carbon emissions by scope (1, 2 and ideally 3) per hl. Normalising per hl makes sites of different sizes comparable.

**How do I calculate carbon emissions in Tableau?**
Multiply activity data, such as gas or electricity consumption, by an emission factor in a calculated field. The number is only as good as the factor, so store factors as a maintained reference table, not hard-coded constants.

**Can a dashboard prevent greenwashing?**
It can help by making boundaries, factors and assumptions explicit, but it cannot prevent selective reporting. Greenwashing is a governance problem; the dashboard's role is to show the full picture honestly, including the bad trends.
