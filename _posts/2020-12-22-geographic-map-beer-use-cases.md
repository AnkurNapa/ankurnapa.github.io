---
layout: post
title: "The Geographic Map in Brewing: Three Beer Use Cases"
image: /assets/og/geographic-map-beer-use-cases.png
description: "When location is the variable, a map beats any table — choropleths, dot maps and catchment views put beer sales on the ground. Three beer use cases (territory performance, distribution coverage, taproom catchment) and the map traps to avoid."
date: 2020-12-22 09:00:00 -0700
updated: 2020-12-22
tags: [brewing-science, beer-chart-guide, data-visualization, sales-intelligence, marketing]
faq:
  - q: "When should a brewery use a geographic map?"
    a: "When location is genuinely the variable that matters — sales by territory, distribution coverage, account locations, or a taproom's catchment area. A choropleth shades regions by a value; a dot or symbol map places points by location and size. Maps reveal spatial patterns — a strong region, a coverage gap, a cluster — that a table of place names cannot."
  - q: "What is the difference between a choropleth and a dot map?"
    a: "A choropleth shades predefined areas (territories, postcodes, states) by a value, good for rates and totals per region. A dot or symbol map places a marker at each location, sized or coloured by value, good for showing individual accounts or events and their clustering. Choropleths can mislead because big areas dominate visually; dot maps avoid that but can overlap in dense areas."
  - q: "What is the main trap with choropleth maps?"
    a: "Large regions grab attention regardless of their actual value — a big rural territory looks important even with low sales, while a tiny dense city region with high sales is hard to see. Normalise to a rate (per capita, per outlet) rather than raw totals where appropriate, and consider a dot or proportional-symbol map when area size would otherwise mislead."
---

**Short answer: when location is the variable, a map beats any table — choropleths shade regions by value, dot and symbol maps place accounts and events on the ground. In a brewery: territory performance, distribution coverage and white space, taproom catchment. Maps reveal spatial patterns a list of place names hides. The main trap is area bias — big regions dominate the eye regardless of value — so normalise to a rate or use proportional symbols where raw totals would mislead.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A stylised choropleth map of sales territories shaded light to dark by sales, with a few dot markers for taprooms and one highlighted coverage gap."><rect width="1000" height="240" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">GEOGRAPHIC MAP — WHEN LOCATION IS THE VARIABLE</text><g stroke="#ffffff" stroke-width="2"><polygon points="120,60 300,50 320,130 160,150" fill="#06483f"/><polygon points="300,50 470,60 460,140 320,130" fill="#79c9b7"/><polygon points="470,60 640,55 660,130 460,140" fill="#4db6a2"/><polygon points="160,150 320,130 340,200 180,205" fill="#c2e6dd"/><polygon points="320,130 460,140 470,200 340,200" fill="#0c5a4e"/><polygon points="460,140 660,130 670,200 470,200" fill="#cfe6df"/></g><circle cx="230" cy="100" r="6" fill="#06483f" stroke="#ffffff"/><circle cx="400" cy="95" r="9" fill="#06483f" stroke="#ffffff"/><circle cx="380" cy="170" r="5" fill="#06483f" stroke="#ffffff"/><rect x="475" y="148" width="185" height="46" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 3"/><text x="567" y="225" text-anchor="middle" font-family="sans-serif" font-size="9.5" fill="#06483f">coverage gap — pale &amp; no taproom</text><g font-family="sans-serif" font-size="9.5"><text x="710" y="70" fill="#4a6b64">low</text><rect x="740" y="60" width="150" height="14" fill="url(#gm)"/><text x="894" y="70" fill="#4a6b64">high</text><linearGradient id="gm" x1="0" x2="1"><stop offset="0" stop-color="#cfe6df"/><stop offset="1" stop-color="#06483f"/></linearGradient><circle cx="745" cy="100" r="6" fill="#06483f"/><text x="760" y="104" fill="#4a6b64">taproom</text></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Shaded territories show where sales are strong; the pale, taproom-free region is visible white space.</figcaption>
</figure>

This closes the specialized set of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). When the answer is "it depends where," only a map will do — building on your [geospatial sales maps]({{ '/2023/tableau-geospatial-sales-maps/' | relative_url }}).

## When to reach for it

Reach for a map when **location is genuinely the variable** — and not just decoration. A choropleth shades regions by value (sales per territory); a dot or proportional-symbol map places individual accounts or taprooms. If the spatial pattern is the insight, the map earns its place; if not, a [bar chart]({{ '/2020/bar-chart-beer-use-cases/' | relative_url }}) of regions is clearer.

## Use case 1 — Territory performance

A choropleth of sales (or growth, or share) by territory shows your strong and weak ground at a glance — and where neighbouring territories diverge, prompting the "why" questions a [sales intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) review needs.

## Use case 2 — Distribution coverage and white space

Overlay account locations (dots) on shaded demand or population. The gaps — areas with demand but no stockists — are your white space, a far more actionable target list than a spreadsheet of postcodes.

## Use case 3 — Taproom catchment

Plot where taproom customers come from (from loyalty or postcode data) to see the real catchment, guiding local [marketing]({{ '/tracks/marketing/' | relative_url }}) spend and whether a second site would cannibalise or extend reach.

## Where this breaks

**Area bias** — big regions dominate the eye regardless of value; normalise to a rate (per capita, per outlet) or use proportional symbols. **Choropleth on raw totals misleads** — shade rates, not counts, where area varies wildly. **Dot overlap** — dense cities become a blob; cluster or size sensibly. **Map for map's sake** — if location isn't the insight, a regional bar chart is honest and clearer. **Projection and boundary errors** — wrong region boundaries quietly misassign sales.

## The bottom line

The geographic map is the right chart only when location is the variable — territory performance, distribution white space, taproom catchment — revealing spatial patterns a table can't. Mind area bias (normalise to rates), handle dot overlap, and don't map data that location doesn't actually explain. That completes the field guide; the [index]({{ '/series/beer-chart-guide/' | relative_url }}) ties every chart type together, and for radar, CUSUM, trajectories and Sankey, see [Seeing Your Beer]({{ '/series/brewing-data-viz/' | relative_url }}).

## Frequently asked questions

**When should a brewery use a geographic map?**
When location is genuinely the variable that matters — sales by territory, distribution coverage, account locations, or a taproom's catchment area. A choropleth shades regions by a value; a dot or symbol map places points by location and size. Maps reveal spatial patterns — a strong region, a coverage gap, a cluster — that a table of place names cannot.

**What is the difference between a choropleth and a dot map?**
A choropleth shades predefined areas (territories, postcodes, states) by a value, good for rates and totals per region. A dot or symbol map places a marker at each location, sized or coloured by value, good for showing individual accounts or events and their clustering. Choropleths can mislead because big areas dominate visually; dot maps avoid that but can overlap in dense areas.

**What is the main trap with choropleth maps?**
Large regions grab attention regardless of their actual value — a big rural territory looks important even with low sales, while a tiny dense city region with high sales is hard to see. Normalise to a rate (per capita, per outlet) rather than raw totals where appropriate, and consider a dot or proportional-symbol map when area size would otherwise mislead.
