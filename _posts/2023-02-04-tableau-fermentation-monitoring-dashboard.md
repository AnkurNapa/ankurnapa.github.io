---
layout: post
title: "A Live Fermentation-Monitoring Dashboard in Tableau"
image: /assets/og/tableau-fermentation-monitoring-dashboard.png
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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Live Fermentation-Monitoring Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Live Fermentation-Monitoring Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">A Live Fermentation-Monitoring Dashboard in Tableau</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Process</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

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
