---
layout: post
title: "Visualising Packaging-Line OEE in Tableau"
image: /assets/og/tableau-packaging-line-oee-dashboard.png
description: "Build a packaging-line OEE dashboard in Tableau with Availability, Performance and Quality as calculated fields, a downtime Pareto and line filters."
date: 2023-02-21
updated: 2023-02-21
tags: [brewing-science, tableau, packaging]
faq:
  - q: "How is OEE calculated as a Tableau calculated field?"
    a: "OEE is Availability multiplied by Performance multiplied by Quality, each a ratio you build as a calculated field: Availability is run time over planned time, Performance is actual output over theoretical output, and Quality is good units over total units. The product is your OEE percentage."
  - q: "What is the most useful chart on an OEE dashboard?"
    a: "A Pareto of downtime reasons. It ranks the causes of lost availability so you can see the vital few stoppages that account for most of the loss, which is usually where the fastest gains are."
  - q: "Why does my OEE look wrong?"
    a: "Almost always because of how downtime is coded at the line. If operators log stoppages inconsistently or lump everything under 'other', the availability component — and therefore OEE — is unreliable. The maths is only as good as the downtime data."
---

**Short answer: OEE in Tableau is three honest ratios multiplied together, and a Pareto that tells you where to look.** The build is straightforward; the value depends entirely on how cleanly the line records its downtime.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for Visualising Packaging-Line OEE in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Visualising Packaging-Line OEE in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Defining OEE before you chart it
Overall Equipment Effectiveness condenses a packaging line's productivity into one number: Availability × Performance × Quality. The discipline is defining each component precisely as a calculated field before drawing anything.

- **Availability** = actual run time ÷ planned production time (the hit from breakdowns and changeovers).
- **Performance** = actual output ÷ theoretical output at rated speed (the hit from minor stops and slow running).
- **Quality** = good units ÷ total units produced (the hit from rejects and rework).

Multiply the three and you have OEE. Build them as named calculated fields on a clean data model — one row per production run or shift per line, with planned time, run time, counts and reject counts — and the rest of the dashboard is assembly. This "measure first" rigour matters because each component points at a different problem; a single OEE figure hides whether you are losing to stoppages, speed or scrap.

## Building the dashboard
Headline the OEE percentage with a BAN (big aggregate number) and a gauge against target. Beneath it, break out Availability, Performance and Quality separately so the story is legible — an 85% OEE made of weak availability is a very different problem from one made of weak quality.

The workhorse view is a **Pareto of downtime reasons**: bar the lost minutes by reason, sorted descending, with a running-total table calculation drawing the cumulative line. This is where Tableau's table calcs earn their place. A **parameter** lets the user pick the line and shift, swapping context without new sheets; parameter actions make it click-driven. Trend OEE over time with a reference line for target, and add a filter action so clicking a day drills into that shift's runs and stoppages.

For prediction — turning recorded downtime into an estimate of *future* downtime — Tableau itself is the wrong tool; that is a modelling job. The natural companion piece is [packaging-line OEE and downtime prediction]({{ '/2024/packaging-line-oee-downtime-prediction/' | relative_url }}), where an external model does the forecasting and Tableau visualises the result. A generative-AI summary can also turn the week's Pareto into a short narrative for the production meeting, which a manager sanity-checks.

## Where it breaks
Here is the uncomfortable truth: garbage downtime coding in means garbage OEE out. The Availability and Performance components depend entirely on operators logging stoppages accurately and consistently. If half the micro-stops never get recorded, Performance looks fine while the line crawls. If every unexplained stop is filed under "other", your Pareto is a single useless bar. No amount of Tableau polish fixes this — the dashboard faithfully reflects whatever the line clerk typed.

The AI layer has the same dependency. Tableau Pulse can monitor OEE and flag a drop, and Explain Data can suggest which factor moved, but both reason over the recorded data. They cannot recover a stoppage nobody logged. The fix is upstream: a tight, well-trained downtime reason taxonomy and disciplined capture, ideally semi-automated from the line's own counters. Get that right and OEE becomes one of the most actionable numbers in the brewery; get it wrong and it is theatre.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives the process, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Visualising Packaging-Line OEE in Tableau</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">The process</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">quality</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">What drives the process, and what it changes downstream.</figcaption>
</figure>

## The bottom line
A Tableau OEE dashboard is three clear calculated fields, a Pareto of downtime, and parameters to slice by line and shift. It will tell you exactly where your packaging losses live — but only if the downtime data is captured honestly. Fix the capture first, then let Tableau make the losses impossible to ignore.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [packaging-line OEE and downtime prediction]({{ '/2024/packaging-line-oee-downtime-prediction/' | relative_url }}).

## Frequently asked questions

**How is OEE calculated as a Tableau calculated field?**
OEE is Availability multiplied by Performance multiplied by Quality, each a ratio you build as a calculated field: Availability is run time over planned time, Performance is actual output over theoretical output, and Quality is good units over total units. The product is your OEE percentage.

**What is the most useful chart on an OEE dashboard?**
A Pareto of downtime reasons. It ranks the causes of lost availability so you can see the vital few stoppages that account for most of the loss, which is usually where the fastest gains are.

**Why does my OEE look wrong?**
Almost always because of how downtime is coded at the line. If operators log stoppages inconsistently or lump everything under 'other', the availability component — and therefore OEE — is unreliable. The maths is only as good as the downtime data.
