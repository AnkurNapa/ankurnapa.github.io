---
layout: post
title: "An EHS Safety-Incident Dashboard in Tableau"
image: /assets/og/tableau-ehs-safety-dashboard.png
description: "Build an EHS safety dashboard in Tableau with TRIR-style rates, leading vs lagging indicators, a hotspot heatmap and Pulse alerts, plus the under-reporting caveat."
date: 2023-09-21
updated: 2023-09-21
tags: [ehs, tableau, safety]
faq:
  - q: "What is the difference between leading and lagging safety indicators?"
    a: "Lagging indicators count what already went wrong, such as recordable injuries or lost-time incidents. Leading indicators measure preventive activity, like near-miss reports, audits completed and corrective actions closed, which predict future risk."
  - q: "How do I calculate a TRIR-style rate in Tableau?"
    a: "Use a calculated field: recordable incidents multiplied by 200,000, divided by total hours worked. The 200,000 normalises to 100 full-time employees per year, making sites and periods comparable."
  - q: "Why might a falling incident count be a bad sign?"
    a: "Because it can reflect under-reporting rather than improving safety. If near-miss reporting falls at the same time, that is a red flag, people may have stopped reporting rather than stopped getting hurt."
---

**Short answer: a safety dashboard must watch leading indicators as closely as lagging ones, because falling incident counts can mean fewer reports, not fewer hazards.** The dashboard supports a safety culture; it does not create one.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for An EHS Safety-Incident Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">An EHS Safety-Incident Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Measure leading and lagging together
The defining discipline of EHS analytics is pairing what already happened with what predicts what happens next. Lagging indicators, recordable injuries, lost-time cases, a TRIR-style rate, are the legally required scorecard but they are rear-view mirrors. Leading indicators, near-miss reports submitted, safety observations logged, audits completed, corrective actions closed on time, are the early-warning system. A dashboard that shows only lagging metrics teaches an organisation to celebrate a quiet quarter without asking whether the quiet is real. Put both on the canvas, side by side, from the first sketch.

## Build it: rates, a hotspot heatmap and alerts
TRIR-style normalisation is a calculated field: recordable incidents times 200,000, divided by hours worked. The constant normalises to roughly 100 full-time staff over a year, so a small packaging line and a large brewhouse become comparable. Wrap it in a LOD if you need the rate computed at site grain while displaying a company roll-up.

The hotspot heatmap is the visual that earns the dashboard its keep. Cross-tab incident counts (or rates) by area against incident type or shift, and use a sequential colour ramp so the warehouse-loading-dock-on-night-shift cell jumps out. This is where patterns hide that a trend line misses. Add a parameter to switch site and period, wired through parameter actions so selecting a site refreshes the heatmap, the rate BANs and the leading-indicator panel in one click.

Layer leading indicators as a small panel: near-miss volume trend, percentage of corrective actions closed within target, audit completion rate. Then configure Tableau Pulse to monitor the recordable rate and corrective-action backlog, sending alerts and a plain-language digest to the EHS lead, "open corrective actions up 30% at Site B", so risk surfaces before the next incident rather than after. Explain Data can suggest what differs about a high-incident area, a useful prompt for the safety walk, not a conclusion.

## Where it breaks: under-reporting and the culture gap
The single biggest hazard is under-reporting bias, and no chart can detect it from inside the data. If frontline teams feel that reporting a near-miss triggers blame, reports dry up, the lagging numbers improve, and the dashboard cheerfully shows green while actual risk climbs. This is why a sudden drop in near-miss reporting should be read as a warning, not a win. Build that interpretation into how the dashboard is presented, or it will be misread.

The deeper limit is that safety is a culture, not a chart. A beautiful Tableau workbook does not close a guard, change a behaviour or make a tired worker speak up. Generative-AI summaries can even erode vigilance: a confident Pulse digest saying "incident rate at record low" invites complacency precisely when leading indicators might be flashing amber. Keep humans, the EHS team and frontline supervisors, owning the interpretation, and use the dashboard to start conversations rather than end them.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="The safety pyramid: many near-misses underlie each serious event — act on the base."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">SAFETY PYRAMID</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">An EHS Safety-Incident Dashboard in Tableau</text><polygon points="335.0,80 385.0,80 415.0,138 305.0,138" fill="#7a1f3d"/><text x="360" y="118" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">Serious · 1</text><polygon points="305.0,144 415.0,144 460.0,202 260.0,202" fill="#b45309"/><text x="360" y="182" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">Minor injuries · ~30</text><polygon points="260.0,208 460.0,208 520.0,266 200.0,266" fill="#5b7a1f"/><text x="360" y="246" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">Near-misses · ~300</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The safety pyramid: many near-misses underlie each serious event — act on the base.</figcaption>
</figure>

## The bottom line
Build the EHS dashboard around paired leading and lagging indicators, normalise with a TRIR-style rate, and let a hotspot heatmap surface where risk concentrates. Use Pulse for alerts but treat falling counts sceptically and watch near-miss reporting as a proxy for trust. The dashboard's real job is to keep the safety conversation honest and ongoing.

*Part of the [EHS]({{ '/tracks/ehs/' | relative_url }}) track.* Related: [EHS reporting automation]({{ '/2026/ehs-reporting-automation/' | relative_url }}).

## Frequently asked questions

**What is the difference between leading and lagging safety indicators?**
Lagging indicators count what already went wrong, such as recordable injuries or lost-time incidents. Leading indicators measure preventive activity, like near-miss reports, audits completed and corrective actions closed, which predict future risk.

**How do I calculate a TRIR-style rate in Tableau?**
Use a calculated field: recordable incidents multiplied by 200,000, divided by total hours worked. The 200,000 normalises to 100 full-time employees per year, making sites and periods comparable.

**Why might a falling incident count be a bad sign?**
Because it can reflect under-reporting rather than improving safety. If near-miss reporting falls at the same time, that is a red flag, people may have stopped reporting rather than stopped getting hurt.
