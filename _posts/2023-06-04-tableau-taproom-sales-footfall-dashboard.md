---
layout: post
title: "A Taproom Sales and Footfall Dashboard in Tableau"
image: /assets/og/tableau-taproom-sales-footfall-dashboard.png
description: "Build a taproom sales and footfall dashboard in Tableau — day-part heatmaps, weather-driven what-if and basket mix — with honest notes on small-sample noise."
date: 2023-06-04
updated: 2023-06-04
tags: [sales-intelligence, tableau, operations]
faq:
  - q: "What is the most useful first chart for a taproom dashboard?"
    a: "An hour-by-day-of-week sales heatmap. It instantly shows your day-parts — quiet Tuesday afternoons, the Friday peak — which is the foundation for staffing, promotions and stock decisions."
  - q: "How do I show the weather effect on footfall in Tableau?"
    a: "Join a daily weather feed to your POS data, then use a parameter to model a temperature or rainfall scenario. A calculated field scales expected footfall so the manager can see a wet weekend before it arrives."
  - q: "Can Tableau Pulse replace a manager reading the dashboard?"
    a: "No. Pulse monitors the headline metrics and sends a natural-language digest when something shifts, which is great for catching drift. But it describes change; the manager still interprets why and decides what to do."
---

**Short answer: a taproom dashboard pays off when it turns raw till data into day-part patterns a manager can act on — but only if you decide the measure first and treat small-sample swings with suspicion.** Footfall, sales and basket mix on one screen beats three reports nobody opens.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Taproom Sales and Footfall Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Taproom Sales and Footfall Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Decide the question before the chart
The temptation is to plot everything the POS exports. Resist it. A taproom manager has three live questions: when are we busy, what are people buying, and do I have the right people and stock on shift? Pick the measures that answer those — sales per hour, covers or transactions per hour, average spend per head, and item mix by category — and design backwards from them. Everything else is decoration. Defining the measure first is what separates a dashboard that gets checked every morning from one that gets bookmarked and forgotten.

## The day-part heatmap
The single most valuable view is an hour-by-day-of-week heatmap of sales or transactions. Put the day of week across the columns, the hour down the rows, and colour the cells by your measure. The pattern jumps out: the dead Monday afternoon, the steady weekday after-work hour, the Saturday surge that needs two extra staff. This is your operational backbone. Build it once in the data source at the right grain — one row per transaction with a clean timestamp — and you can drive staffing, happy-hour timing and keg-change scheduling from the same view. Layer a filter action so clicking a cell drills into the basket mix for that exact slot, and the heatmap becomes a navigation tool, not just a picture.

## Footfall, weather and basket mix
Footfall and weather belong together. Join a daily weather feed to your sales data and the correlation usually leaps out — warm, dry evenings fill the terrace. Make it interactive with a parameter: let the manager set a temperature or rainfall scenario and use a calculated field to scale expected footfall, so a wet bank holiday is planned for rather than discovered. Pair this with a basket-mix view — food versus drink, core range versus specials, the attach rate of snacks to pints — and you can see not just how many people came but what they actually spent on. For the staffing side of the same problem, see [taproom footfall and staffing forecasts]({{ '/2022/taproom-footfall-staffing-forecasts/' | relative_url }}).

For the manager who will not log in daily, set up Tableau Pulse on the headline metrics. It monitors sales, footfall and average spend and pushes a plain-English digest — "Saturday covers up 14% on last week" — straight to their inbox. Einstein Copilot's Explain Data can go a step further on an outlier cell, surfacing which items or hours drove an unusual spike. Useful prompts, not verdicts.

## Where it breaks
Two failure modes to be honest about. First, small-sample noise. A single taproom generates thin data; one rained-off festival or a coach party of forty can make a Tuesday look like a trend. Always show the underlying count alongside any average, and be wary of reading too much into a single week's heatmap cell. Second, POS hygiene. Voids, comps, staff drinks, split bills and mistimed clock-ins quietly corrupt the numbers, and the weather join is only as good as your timezone and date matching. Clean it in Tableau Prep and document the rules, or the dashboard will be precisely wrong. Neither Pulse nor Copilot fixes dirty data — they will happily narrate the error.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Each stage loses some — the funnel shows where the drop-off is."><rect x="0" y="0" width="720" height="310" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">A Taproom Sales and Footfall Dashboard in Tableau</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#b45309" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reach · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#b45309" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interest · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#b45309" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Trial · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#b45309" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Win · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Each stage loses some — the funnel shows where the drop-off is.</figcaption>
</figure>

## The bottom line
A taproom dashboard works when it answers the manager's real questions — when, what and who — from clean POS data, not when it shows everything the till can export. Lead with the day-part heatmap, make weather and basket mix interactive, and let Pulse watch the metrics overnight. Just keep the sample sizes visible and the data hygiene tight, because the manager, not the model, is making the staffing call.

*Part of the [Sales Intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) track.* Related: [Taproom footfall and staffing forecasts]({{ '/2022/taproom-footfall-staffing-forecasts/' | relative_url }}).

## Frequently asked questions

**What is the most useful first chart for a taproom dashboard?**
An hour-by-day-of-week sales heatmap. It instantly shows your day-parts — quiet Tuesday afternoons, the Friday peak — which is the foundation for staffing, promotions and stock decisions.

**How do I show the weather effect on footfall in Tableau?**
Join a daily weather feed to your POS data, then use a parameter to model a temperature or rainfall scenario. A calculated field scales expected footfall so the manager can see a wet weekend before it arrives.

**Can Tableau Pulse replace a manager reading the dashboard?**
No. Pulse monitors the headline metrics and sends a natural-language digest when something shifts, which is great for catching drift. But it describes change; the manager still interprets why and decides what to do.
