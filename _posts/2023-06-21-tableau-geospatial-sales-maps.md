---
layout: post
title: "Mapping Beer Sales by Market in Tableau"
image: /assets/og/tableau-geospatial-sales-maps.png
description: "Map beer sales by market in Tableau using geographic roles, custom geocoding, filled and density maps — with honest limits on geocoding gaps and population bias."
date: 2023-06-21
updated: 2023-06-21
tags: [sales-intelligence, tableau, geospatial]
faq:
  - q: "How do I map sales data that Tableau does not recognise automatically?"
    a: "Assign a geographic role to your field — postcode, county, country — so Tableau geocodes it. For territories Tableau does not know, import a custom geocoding file that maps each name to a latitude and longitude."
  - q: "Should I use a filled map or a density map for beer sales?"
    a: "Filled (choropleth) maps suit volume by defined territory like county or distributor region. Density (heat) maps suit lots of individual points such as accounts, showing concentration without needing boundaries."
  - q: "Can a Tableau map show me white-space opportunity?"
    a: "Yes, indirectly. Plot your accounts as one layer and a market reference such as licensed venues as another; the gaps where venues exist but you have no account are your white space. It points you to look — it does not confirm demand."
---

**Short answer: a Tableau sales map turns territory data into where-to-act intelligence — but get the geocoding right and remember a map shows where people are, not where the demand is.** Geographic roles, a clean custom geocode file and the right map type do most of the work.

## Measure first, then map
A map is seductive, which is exactly why you should decide the measure before you plot it. Are you showing volume sold, growth rate, distribution penetration, or white space? Each needs a different map. Volume by distributor region is a filled map; account concentration is a density map; growth is best as colour on points or regions. Settle the question first, clean the geography in the data source, and only then open the marks card. A map built before the measure is decided usually ends up showing population density dressed up as insight.

## Geographic roles and custom geocoding
Tableau recognises common geographies out of the box: assign a field the role of postcode, county or country and it geocodes automatically, dropping points or filling shapes. The friction is always the territories Tableau does not know — your own sales regions, distributor patches, festival catchments. For these, build a custom geocoding file that maps each name to a latitude and longitude (or import custom polygons for filled shapes). Spend the time getting this right once; it is reused across every map you ever build. Standardise the source field in Tableau Prep too — "Gtr Manchester", "Greater Manchester" and "Manchester (Gtr)" will scatter your sales across three phantom locations otherwise.

## Filled, density and layered maps
Match the map to the measure. A filled choropleth — counties shaded by volume — reads well for aggregate sales across defined regions. A density map turns hundreds of individual accounts into a heat surface, ideal for spotting where business clusters without drawing boundaries. The real power comes from map layers: stack your accounts over a layer of all licensed venues, split on-premise from off-premise with a colour, and the white space — venues with no account near them — becomes visible. Add a filter action so selecting a region updates a supporting bar chart, and the map becomes the entry point to the whole sales story. Once the map tells you where to sell, the next question is how to get there efficiently — see [route optimisation for beer distribution]({{ '/2021/route-optimisation-beer-distribution/' | relative_url }}).

## Where it breaks
Maps mislead more easily than any other chart, so be honest about three things. First, geocoding gaps: a few unmatched postcodes silently vanish from the view, so always check Tableau's "unknown locations" count and reconcile the mapped total back to your actuals. Second, the population trap. A big red region usually means more people live there, not that you are winning — normalise by population, outlets or A1 spend before you call it a strong market, or you will chase cities and ignore underserved rural patches. Third, white space is a prompt, not proof: an empty area might be genuinely untapped or might have no demand, no licence density or a competitor lock-in. The map shows you where to look; a rep visit or external data confirms whether it is real. AI helpers like Pulse or Explain Data can flag a region that has moved, but they read the same possibly-biased numbers — they do not validate the underlying demand.

## The bottom line
A Tableau sales map is one of the fastest ways to move from "what did we sell" to "where should we act", provided the geocoding is clean and the measure is decided before the marks card. Use filled maps for territories, density for accounts, layers for white space — and always normalise before declaring a winner. The map narrows the search; the human, armed with the right denominator, makes the territory call.

*Part of the [Sales Intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) track.* Related: [Route optimisation for beer distribution]({{ '/2021/route-optimisation-beer-distribution/' | relative_url }}).

## Frequently asked questions

**How do I map sales data that Tableau does not recognise automatically?**
Assign a geographic role to your field — postcode, county, country — so Tableau geocodes it. For territories Tableau does not know, import a custom geocoding file that maps each name to a latitude and longitude.

**Should I use a filled map or a density map for beer sales?**
Filled (choropleth) maps suit volume by defined territory like county or distributor region. Density (heat) maps suit lots of individual points such as accounts, showing concentration without needing boundaries.

**Can a Tableau map show me white-space opportunity?**
Yes, indirectly. Plot your accounts as one layer and a market reference such as licensed venues as another; the gaps where venues exist but you have no account are your white space. It points you to look — it does not confirm demand.
