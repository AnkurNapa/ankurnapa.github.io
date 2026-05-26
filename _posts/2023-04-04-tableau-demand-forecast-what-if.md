---
layout: post
title: "Demand Forecasting and What-If Analysis in Tableau"
image: /assets/og/tableau-demand-forecast-what-if.png
description: "Build a demand forecast and what-if dashboard in Tableau using built-in forecasting, parameters and TabPy — and know where the basic model stops."
date: 2023-04-04
updated: 2023-04-04
tags: [forecasting, tableau, analytics]
faq:
  - q: "Is Tableau's built-in forecast a machine learning model?"
    a: "No. It uses exponential smoothing, a classic time-series method that extends recent trend and seasonality. It is not a trained, causal ML model and has no view of price, weather or promotions."
  - q: "How do I add what-if scenarios to a Tableau forecast?"
    a: "Use parameters for the levers you want to test — uplift percentage, price change, distribution points — then reference them inside calculated fields. Parameter actions let users drag or click to change the scenario live."
  - q: "When should I move forecasting out of Tableau into TabPy?"
    a: "When you need causal drivers, multiple SKUs forecast together, or a model you can validate with hold-out error. TabPy runs Python (Prophet, statsmodels, scikit-learn) and returns the result to Tableau for display."
---

**Short answer: Tableau is excellent for showing and stress-testing a forecast, but its built-in model is basic — measure first, then decide whether exponential smoothing is enough or you need real ML via TabPy.** A demand dashboard earns its keep when a planner can see the trend and immediately ask "what if we run the promotion?".

## Start with the measure, not the chart
Before you draw anything, define the number the business actually plans against. For most breweries that is depletions or shipped cases per SKU per week, not orders or revenue. Get the grain right in the data source — one row per SKU per period — and clean it in Tableau Prep so gaps, returns and unit changes do not poison the trend. A forecast is only ever as honest as the series feeding it. If you cannot reconcile the historical actuals to your finance numbers, stop and fix that first; a tidy chart on dirty data is worse than no chart.

## The built-in forecast, used honestly
Tableau's native forecast applies exponential smoothing: it learns the level, trend and seasonality from your history and projects them forward with a confidence band. Drop your weekly cases measure on the view, add the continuous date, and turn on Analytics → Forecast. It is fast, it is defensible for stable repeat-purchase volume, and the prediction interval is the part you should show most prominently — it tells the planner how much to trust the line.

What it does not do matters just as much. It is not causal. It has no idea you cut the price, gained three distribution points or that a heatwave is coming. It simply assumes the recent past continues. For steady core lines that is often fine. For a seasonal or promotion-driven SKU, it will confidently miss. Say so on the dashboard — a one-line caption ("trend + seasonality only; excludes price and promo") prevents a lot of misplaced confidence in a planning meeting.

## Wiring up what-if with parameters
This is where Tableau shines. Create parameters for the levers planners argue about: a promotional uplift percentage, a price index, a new-distribution multiplier. Then build a calculated field — `[Forecast] * (1 + [Promo Uplift])` is the simplest version — and put that adjusted line beside the base forecast. Parameter actions turn the static control into something a planner can drag during the conversation, watching the scenario reshape in real time. Add a couple of toggles for best/likely/worst case and you have replaced a fortnight of spreadsheet emails with a five-minute working session. For the deeper modelling that should sit behind these levers, see [AI demand forecasting for breweries]({{ '/2026/ai-demand-forecasting-for-breweries/' | relative_url }}).

## Where it breaks
Three honest limits. First, the built-in forecast degrades fast on short or erratic histories — under two seasonal cycles it is guessing. Second, what-if parameters are assumptions, not evidence: a 20% uplift slider is only as good as the judgement behind the 20%, and a slick interactive view can lend false authority to a made-up number. Third, when you genuinely need causal drivers or per-SKU accuracy you measure with hold-out error, push the work to TabPy and let Tableau do what it is best at — displaying the result and letting humans interrogate it. Tableau Pulse can then monitor the live metric and send a plain-language digest when the trend drifts, but Pulse describes; it does not decide. The planner still owns the call.

## The bottom line
Use Tableau's forecast for what it is: a clean, fast projection of trend and seasonality with an honest confidence band, paired with parameters that make scenario planning a conversation rather than a spreadsheet chore. Be candid that it is not causal and not ML. When accuracy or drivers matter, move the model to TabPy and keep Tableau as the window onto it. The chart informs; the human commits.

*Part of the [Sales Forecasting]({{ '/tracks/sales-forecasting/' | relative_url }}) track.* Related: [AI demand forecasting for breweries]({{ '/2026/ai-demand-forecasting-for-breweries/' | relative_url }}).

## Frequently asked questions

**Is Tableau's built-in forecast a machine learning model?**
No. It uses exponential smoothing, a classic time-series method that extends recent trend and seasonality. It is not a trained, causal ML model and has no view of price, weather or promotions.

**How do I add what-if scenarios to a Tableau forecast?**
Use parameters for the levers you want to test — uplift percentage, price change, distribution points — then reference them inside calculated fields. Parameter actions let users drag or click to change the scenario live.

**When should I move forecasting out of Tableau into TabPy?**
When you need causal drivers, multiple SKUs forecast together, or a model you can validate with hold-out error. TabPy runs Python (Prophet, statsmodels, scikit-learn) and returns the result to Tableau for display.
