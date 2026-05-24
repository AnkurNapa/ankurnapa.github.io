---
layout: post
title: "A Taproom Sales and Footfall Dashboard in Tableau"
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

## Decide the question before the chart
The temptation is to plot everything the POS exports. Resist it. A taproom manager has three live questions: when are we busy, what are people buying, and do I have the right people and stock on shift? Pick the measures that answer those — sales per hour, covers or transactions per hour, average spend per head, and item mix by category — and design backwards from them. Everything else is decoration. Defining the measure first is what separates a dashboard that gets checked every morning from one that gets bookmarked and forgotten.

## The day-part heatmap
The single most valuable view is an hour-by-day-of-week heatmap of sales or transactions. Put the day of week across the columns, the hour down the rows, and colour the cells by your measure. The pattern jumps out: the dead Monday afternoon, the steady weekday after-work hour, the Saturday surge that needs two extra staff. This is your operational backbone. Build it once in the data source at the right grain — one row per transaction with a clean timestamp — and you can drive staffing, happy-hour timing and keg-change scheduling from the same view. Layer a filter action so clicking a cell drills into the basket mix for that exact slot, and the heatmap becomes a navigation tool, not just a picture.

## Footfall, weather and basket mix
Footfall and weather belong together. Join a daily weather feed to your sales data and the correlation usually leaps out — warm, dry evenings fill the terrace. Make it interactive with a parameter: let the manager set a temperature or rainfall scenario and use a calculated field to scale expected footfall, so a wet bank holiday is planned for rather than discovered. Pair this with a basket-mix view — food versus drink, core range versus specials, the attach rate of snacks to pints — and you can see not just how many people came but what they actually spent on. For the staffing side of the same problem, see [taproom footfall and staffing forecasts]({{ '/2022/taproom-footfall-staffing-forecasts/' | relative_url }}).

For the manager who will not log in daily, set up Tableau Pulse on the headline metrics. It monitors sales, footfall and average spend and pushes a plain-English digest — "Saturday covers up 14% on last week" — straight to their inbox. Einstein Copilot's Explain Data can go a step further on an outlier cell, surfacing which items or hours drove an unusual spike. Useful prompts, not verdicts.

## Where it breaks
Two failure modes to be honest about. First, small-sample noise. A single taproom generates thin data; one rained-off festival or a coach party of forty can make a Tuesday look like a trend. Always show the underlying count alongside any average, and be wary of reading too much into a single week's heatmap cell. Second, POS hygiene. Voids, comps, staff drinks, split bills and mistimed clock-ins quietly corrupt the numbers, and the weather join is only as good as your timezone and date matching. Clean it in Tableau Prep and document the rules, or the dashboard will be precisely wrong. Neither Pulse nor Copilot fixes dirty data — they will happily narrate the error.

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
