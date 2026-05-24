---
layout: post
title: "A Live Fermentation-Monitoring Dashboard in Tableau"
description: "Build a live fermentation-monitoring dashboard in Tableau with gravity, temperature and CO2 curves per tank, target bands and a TabPy ML forecast."
date: 2023-02-04
updated: 2023-02-04
tags: [brewing-science, tableau, fermentation]
faq:
  - q: "Can Tableau show fermentation data in real time?"
    a: "Not truly real time. Tableau refreshes a live connection or a .hyper extract on a schedule, so the dashboard is near-live — minutes behind, not seconds. For most fermentations, a refresh every few minutes is more than adequate."
  - q: "How do I show whether a fermentation is on track?"
    a: "Plot the live gravity and temperature curves against a target band built from reference lines or a shaded area derived from past good batches of the same recipe. When the curve leaves the band, the tank needs attention."
  - q: "Is Tableau's built-in forecasting good enough to predict fermentation?"
    a: "For a rough projection of a smooth curve, yes; it uses exponential smoothing. For a real prediction of attenuation or stuck fermentation, push the data to an external model via TabPy and visualise its output — Tableau's native forecast is not a process model."
---

**Short answer: Tableau gives you a near-live fermentation cockpit, not a real-time control system.** It is excellent at showing every tank against its target band so a brewer can spot a drifting fermentation early — provided you are honest about refresh cadence and what the forecast actually is.

## Designing for "is this tank behaving?"
A fermentation dashboard answers one question per tank: is this fermentation following the expected path, or wandering off it? Everything in the design should serve that question.

Start, as always, with the data model. One row per reading: tank, batch, recipe, timestamp, gravity, temperature, and CO2 or pressure if you log it. The "measure first" payoff is a target band — for each recipe, derive an expected gravity-versus-time and temperature-versus-time corridor from a set of historical good batches. That band is your reference; the live curve is the test.

Connect Tableau to your fermentation data either as a live connection or, more commonly, a scheduled `.hyper` extract refresh. Either way the dashboard is near-live, lagging reality by minutes — which is fine, because a healthy fermentation moves over hours and days, not seconds.

## Building the per-tank view
Lay out small-multiple line charts, one per active tank, each showing the live gravity curve overlaid on the recipe's target band as a shaded **reference band**. Dual-axis temperature on a secondary scale, and you can see the classic relationship: temperature climbs, gravity drops, then both settle. A calculated field flags when the current point sits outside the band, driving a colour change and a simple "attention" indicator so a brewer scanning twenty tanks sees the one in trouble.

Filter actions let you click a tank and drill into its full history, fermentation start, dissolved oxygen at pitch, yeast generation. Parameters let you flip the target band between recipes or strengths.

For prediction, this is where you go beyond Tableau's built-ins. Pass the recent curve to a model through **TabPy** — a Python service Tableau can call — and return a projected final gravity or a probability of a stuck fermentation, then plot that projection as a dashed extension of the live curve. A generative-AI layer can then draft the morning's "tanks to watch" note from those projections, which a brewer reviews. That is a proper forecast, unlike the native exponential-smoothing line, which is fine for eyeballing a trend but knows nothing about yeast.

The deeper modelling question — what it actually takes to predict fermentation — is its own topic; see [can AI predict beer fermentation?]({{ '/2026/can-ai-predict-beer-fermentation/' | relative_url }}).

## Where it breaks
The honest limit is the word "live". Tableau is not a SCADA or process-control platform; it visualises data that something else has captured and landed, on a refresh schedule. Do not wire safety-critical alarms to a Tableau extract — use it for monitoring and decision support, not for tripping a valve.

The second limit is the forecast. Built-in forecasting will extrapolate a smooth curve and look convincing, but it cannot anticipate a stall, because it has no concept of attenuation limits or yeast health. Even a good TabPy model is only as honest as its training data; a recipe it has never seen will be guessed, not known. And no model — generative or otherwise — replaces a hydrometer reading or a quick taste when something looks wrong.

## The bottom line
A Tableau fermentation dashboard turns a wall of tank readings into one glanceable view: every fermentation against its expected band, with the strays highlighted. Treat it as near-live monitoring, lean on an external model via TabPy for real prediction, and keep the brewer — not the dashboard — in the loop for the calls that matter.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [can AI predict beer fermentation?]({{ '/2026/can-ai-predict-beer-fermentation/' | relative_url }}).

## Frequently asked questions

**Can Tableau show fermentation data in real time?**
Not truly real time. Tableau refreshes a live connection or a .hyper extract on a schedule, so the dashboard is near-live — minutes behind, not seconds. For most fermentations, a refresh every few minutes is more than adequate.

**How do I show whether a fermentation is on track?**
Plot the live gravity and temperature curves against a target band built from reference lines or a shaded area derived from past good batches of the same recipe. When the curve leaves the band, the tank needs attention.

**Is Tableau's built-in forecasting good enough to predict fermentation?**
For a rough projection of a smooth curve, yes; it uses exponential smoothing. For a real prediction of attenuation or stuck fermentation, push the data to an external model via TabPy and visualise its output — Tableau's native forecast is not a process model.
