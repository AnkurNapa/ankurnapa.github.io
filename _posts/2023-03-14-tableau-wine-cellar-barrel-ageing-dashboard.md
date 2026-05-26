---
layout: post
title: "A Cellar and Barrel-Ageing Inventory Dashboard in Tableau"
image: /assets/og/tableau-wine-cellar-barrel-ageing-dashboard.png
description: "Build a Tableau cellar dashboard tracking barrels by type and age via LOD, top-up and evaporation, SO2 status and an ageing timeline with Pulse alerts."
date: 2023-03-14
updated: 2023-03-14
tags: [winemaking, tableau, inventory]
faq:
  - q: "How do I aggregate barrels by lot in Tableau?"
    a: "Use a FIXED level-of-detail calculation keyed on lot, such as the total volume or average free SO2 per lot. That gives you a clean per-lot rollup even though each row is a single barrel."
  - q: "Can Tableau track barrel evaporation?"
    a: "Yes, if you log top-ups. Calculate the volume added per barrel over time and the dashboard shows evaporation as a running top-up total, which also flags barrels losing more than expected."
  - q: "Will Tableau Pulse tell me which barrels are due?"
    a: "Pulse monitors the metric you define, such as days since last SO2 check or months in barrel, and sends a digest naming the barrels crossing your threshold. It surfaces the list; the cellar still does the work."
---

**Short answer: a cellar dashboard is worth building when it answers "what is in barrel, how old is it, and which barrels need attention" without anyone opening the cellar map in their head.** Define the rollup grain — barrel, lot, type — before you draw anything.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Cellar and Barrel-Ageing Inventory Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Cellar and Barrel-Ageing Inventory Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Model the cellar grain first
Barrel data is hierarchical, so decide your levels before building: individual barrel, lot, barrel type (new versus used oak), and vintage. Each row in your source is usually one barrel with attributes — fill date, oak type, lot, last top-up, free and total SO2. The measure-first discipline means agreeing what a "barrel due for top-up" or "barrel at risk on SO2" actually means before you visualise it.

Cellar data is often hand-logged, so connect a refreshed extract rather than chasing a live feed, and use Tableau Prep to reconcile barrel IDs that drift between spreadsheets. Level-of-detail calculations do the heavy lifting: `{FIXED [Lot] : SUM([Volume])}` gives litres per lot, and an INCLUDE expression lets you average free SO2 at barrel grain while displaying it by lot.

## The inventory and ageing views
Build a matrix of barrels coloured by oak type and sized by volume, filtered by lot and vintage — the cellar at a glance. Beside it, an ageing timeline plots each lot's months in barrel against a target ageing window held in a parameter, so a lot drifting past its plan is obvious.

Track top-ups and evaporation as a running total of litres added per barrel; a barrel demanding far more top-up than its neighbours is either thirsty oak or a problem. An SO2 status view colours each barrel red, amber or green against your free-SO2 floor, with a filter action so clicking a lot reveals its barrels. Parameter actions let you flex the ageing target and watch which lots fall in or out of plan.

## Let Pulse flag what is due
Set Tableau Pulse on "barrels past SO2 check" and "lots approaching end of ageing window." It monitors those metrics and sends a digest naming the barrels and lots crossing the line — the cellar's morning to-do list, written in plain language. Einstein's Explain Data can help when one lot's SO2 is dropping faster than the rest, pointing at the fields that differ.

## Where it breaks
The candid limits are about data and biology. Cellar data is largely manual, so the dashboard is only as current as the last person who wrote in the log; a barrel topped up but never recorded looks neglected. Barrel-to-barrel variation is real — two barrels of the same oak and age can age very differently — so an aggregate by type hides individual outliers that matter at blending. And the dashboard tracks ageing; it cannot tell you a wine is ready. That is a bench-trial and a palate decision, and even an AI quality model is an estimate rather than a tasting.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives barrel ageing, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">A Cellar and Barrel-Ageing Inventory Dashboard in Tableau</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Barrel ageing</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">quality</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">What drives barrel ageing, and what it changes downstream.</figcaption>
</figure>

## The bottom line
A Tableau cellar dashboard turns a scattered barrel log into a managed inventory: LOD rollups by lot and type, top-up and evaporation tracking, SO2 status, and an ageing timeline, with Pulse naming the barrels due. Keep the data current and remember it tracks ageing, not readiness.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [Can AI predict wine quality?]({{ '/2026/can-ai-predict-wine-quality/' | relative_url }}).

## Frequently asked questions

**How do I aggregate barrels by lot in Tableau?**
Use a FIXED level-of-detail calculation keyed on lot, such as the total volume or average free SO2 per lot. That gives you a clean per-lot rollup even though each row is a single barrel.

**Can Tableau track barrel evaporation?**
Yes, if you log top-ups. Calculate the volume added per barrel over time and the dashboard shows evaporation as a running top-up total, which also flags barrels losing more than expected.

**Will Tableau Pulse tell me which barrels are due?**
Pulse monitors the metric you define, such as days since last SO2 check or months in barrel, and sends a digest naming the barrels crossing your threshold. It surfaces the list; the cellar still does the work.
