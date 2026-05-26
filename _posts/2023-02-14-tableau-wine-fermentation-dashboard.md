---
layout: post
title: "A Wine Fermentation Monitoring Dashboard in Tableau"
image: /assets/og/tableau-wine-fermentation-dashboard.png
description: "Build a Tableau fermentation dashboard tracking per-tank Brix and temperature curves, stuck-ferment flags and YAN, with Explain Data diagnostics."
date: 2023-02-14
updated: 2023-02-14
tags: [winemaking, tableau, fermentation]
faq:
  - q: "What should a fermentation dashboard in Tableau actually show?"
    a: "Per-tank Brix descent and temperature against a target band, plus a stuck-ferment flag and the opening YAN reading. Those four together tell you whether each tank is on track or needs intervention."
  - q: "Can Tableau detect a stuck fermentation?"
    a: "It can flag the symptom — a Brix curve that has flattened above dryness — using a calculated field comparing the latest reading to the previous days. It cannot diagnose the cause; that still needs a cellar hand and a lab."
  - q: "Does Explain Data work on fermentation tanks?"
    a: "Explain Data can surface which fields correlate with a slow tank in your data, such as low YAN or a temperature dip. Treat its output as a prompt for investigation, not a verdict."
---

**Short answer: a fermentation dashboard earns its place when it shows every tank's Brix descent against a temperature band on one screen, so a sluggish ferment is obvious before it stalls.** Decide the target bands first; the charts follow.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Wine Fermentation Monitoring Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Wine Fermentation Monitoring Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Define the bands before you build
The data science habit — measure first — matters more in the cellar than the vineyard, because fermentation moves in hours. Fix your target windows up front: whites fermenting cool at roughly 12 to 18 °C, reds warm at 25 to 30 °C, opening YAN ideally landing somewhere around 150 to 250 mg/L. Those numbers become parameters and reference bands, not hard-coded marks, so a winemaker can shift the white-ferment ceiling without editing the workbook.

Your source is usually a tank-logging system or a manual log exported to a sheet. A live connection is ideal during peak ferment; otherwise a frequently refreshed .hyper extract is fine. Tableau Prep cleans the inevitable mess of tank renames mid-vintage and merges the lab's YAN results with the cellar's temperature logs.

## The per-tank small multiple
The workhorse view is a small-multiple grid: one mini-chart per tank, time on the axis, Brix on a descending line, with the target temperature band drawn as a shaded reference. Colour the Brix line by whether the latest temperature sits inside or outside the band, and the cellar reads in seconds.

A FIXED level-of-detail calculation pins each tank's starting Brix — `{FIXED [Tank] : MIN([Brix])}` — so you can compute percent of sugar consumed regardless of how many readings a tank has. A stuck-ferment flag is a table calculation comparing the latest Brix to the reading two or three days prior: if it has barely moved and sits above dryness, the tank turns red. Add a parameter action so clicking a tank loads its full detail view with YAN and malolactic status.

## Let Explain Data interrogate the slow tank
When one tank lags, right-click the mark and run Explain Data. Einstein's Explain Data scans the other fields and reports what statistically distinguishes that tank — perhaps it opened with low YAN, or its temperature dipped overnight. That is a fast, useful prompt. Tableau Pulse, set on the cellar-wide "tanks off-target" metric, sends a morning digest so the team knows what to walk to first.

## Where it breaks
The honest limits are about cadence and biology. If your sensors log every six hours, the dashboard cannot catch a temperature spike that peaks and passes in between. Native and wild ferments are erratic by nature — a flat Brix curve might be a healthy lag phase, not a stall — so a naïve stuck-ferment flag will cry wolf on a slow-but-fine tank. Explain Data only knows the columns you gave it; it will never suggest the real culprit was a nutrient addition nobody logged. And no dashboard manages SO2 or smells the volatile acidity creeping up; that remains a human job.

## The bottom line
A Tableau fermentation dashboard is an early-warning grid: per-tank Brix against a temperature band, a stuck-ferment flag, and YAN context, with Explain Data and Pulse pointing you at the tank that needs attention. Set the target bands as parameters, respect your sensor cadence, and remember the dashboard flags symptoms while the cellar diagnoses causes.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [AI wine fermentation control]({{ '/2024/ai-wine-fermentation-control/' | relative_url }}).

## Frequently asked questions

**What should a fermentation dashboard in Tableau actually show?**
Per-tank Brix descent and temperature against a target band, plus a stuck-ferment flag and the opening YAN reading. Those four together tell you whether each tank is on track or needs intervention.

**Can Tableau detect a stuck fermentation?**
It can flag the symptom — a Brix curve that has flattened above dryness — using a calculated field comparing the latest reading to the previous days. It cannot diagnose the cause; that still needs a cellar hand and a lab.

**Does Explain Data work on fermentation tanks?**
Explain Data can surface which fields correlate with a slow tank in your data, such as low YAN or a temperature dip. Treat its output as a prompt for investigation, not a verdict.
