---
layout: post
title: "A Cask Maturation and Angel's-Share Dashboard in Tableau"
image: /assets/og/tableau-whisky-cask-maturation-dashboard.png
description: "Build a Tableau cask maturation dashboard tracking age, strength and angel's-share evaporation loss, with projected ready dates and AI-driven monitoring."
date: 2023-06-14
updated: 2023-06-14
tags: [distilling-maturation, tableau, whiskey]
faq:
  - q: "How do I model angel's share in Tableau?"
    a: "Use a table calculation that compounds an annual loss rate (roughly 2% per year) across each cask's maturation timeline, ideally calibrated against your own weighing records rather than a flat assumption."
  - q: "Can Tableau forecast when a cask will be ready?"
    a: "Yes, via a calculated field that projects strength and volume forward to your target age, but treat the date as a planning estimate, not a promise, because per-cask variation is large."
  - q: "Does Tableau replace the master blender?"
    a: "No. Tableau monitors stock and flags casks worth nosing; the decision to bottle still rests on sensory assessment by the blending team."
---

**Short answer: Tableau turns scattered cask records into a living maturation view that shows what you have, how fast it is evaporating, and roughly when it is ready.** The hard part is not the charts; it is having clean data and accepting that whisky moves on a timescale no dashboard can hurry.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Cask Maturation and Angel&#39;s-Share Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">A Cask Maturation and Angel&#39;s-Share Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Measure first, visualise second
Before opening Tableau, decide what each row of data represents. The natural grain is a cask-by-date observation: cask ID, fill date, cask type (ex-bourbon, ex-sherry, virgin oak), original litres of pure alcohol, current strength, and the date of each weighing or dip. Most distilleries do not weigh every cask every month, so your data source will be sparse and uneven. Model that honestly. Bring it in as a live connection if your warehouse system supports it, or shape it in Tableau Prep into a tidy extract (.hyper) before building anything.

The discipline of defining the grain first is what separates a dashboard that survives contact with a real rackhouse from a pretty demo. Get this wrong and every calculated field downstream inherits the error.

## Cumulative loss and projected ready dates
Angel's share — the spirit lost to evaporation, around 2% of volume per year but highly variable — is the headline metric. Model it with a table calculation that compounds the annual loss across each cask's life, partitioned by cask ID and ordered by date. A LOD expression such as `{ FIXED [Cask ID] : MIN([Fill Date]) }` gives you a stable maturation-age field per cask, independent of whatever filters the user applies.

Layer in a parameter for target age so a user can ask: which casks reach twelve years next quarter? A what-if action lets you flex the assumed loss rate and watch projected volume and strength respond. Tableau Pulse can then sit on top of the published workbook and send a plain-language digest — "Warehouse 3 lost 0.4% more this quarter than last" — to the team without anyone opening the dashboard.

## Where it breaks
This dashboard is only as good as the cadence of your measurements. If casks are weighed once a year, your cumulative-loss curve is an interpolation between two points, and the projected ready date carries years of uncertainty. Built-in forecasting in Tableau uses exponential smoothing, which is fine for a smooth trend but cannot capture the cask-to-cask variation driven by wood, fill strength, and warehouse position. For that you need either richer data or an external model via TabPy — see [forecasting whiskey's angel's share]({{ '/2024/forecasting-whiskey-angels-share/' | relative_url }}) for the modelling side.

The deeper limit is physics. Maturation gives feedback in years, so the dashboard rewards patience, not speed. It tells you the state of your stock; it does not make the spirit ready any sooner.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives maturation, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">A Cask Maturation and Angel&#39;s-Share Dashboard in Tableau</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Maturation</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">quality</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">What drives maturation, and what it changes downstream.</figcaption>
</figure>

## The bottom line
A Tableau cask maturation dashboard is the cheapest way to see your entire maturing inventory at once, track evaporation honestly, and plan bottling around realistic ready dates. Treat its projections as planning aids and keep the master blender's nose as the final instrument. Built well, it earns its keep by surfacing the handful of casks that need attention this month from the thousands that do not.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.* Related: [forecasting whiskey's angel's share]({{ '/2024/forecasting-whiskey-angels-share/' | relative_url }}).

## Frequently asked questions

**How do I model angel's share in Tableau?**
Use a table calculation that compounds an annual loss rate (roughly 2% per year) across each cask's maturation timeline, ideally calibrated against your own weighing records rather than a flat assumption.

**Can Tableau forecast when a cask will be ready?**
Yes, via a calculated field that projects strength and volume forward to your target age, but treat the date as a planning estimate, not a promise, because per-cask variation is large.

**Does Tableau replace the master blender?**
No. Tableau monitors stock and flags casks worth nosing; the decision to bottle still rests on sensory assessment by the blending team.
