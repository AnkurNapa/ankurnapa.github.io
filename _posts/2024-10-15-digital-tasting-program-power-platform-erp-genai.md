---
layout: post
title: "Building a Digital Tasting Program: Power Platform, ERP, and Gen AI"
image: /assets/og/digital-tasting-program-power-platform-erp-genai.png
description: "A practical sequence for beer, wine, and spirits: data model first, capture in Power Apps, anchor in ERP, analyse in Power BI, then layer AI and generative AI."
date: 2024-10-15
updated: 2024-10-15
tags: [brewing-science, tasting, power-platform, generative-ai]
faq:
  - q: "What's the right order to build a digital tasting program?"
    a: "Data model, then capture, then dashboards, then AI, then generative AI. Define attributes, scales, and batch/lot keys first; capture in Power Apps on Dataverse; anchor master data in ERP; analyse in Power BI; only then add AI and Gen AI on top of clean, structured data."
  - q: "When should I not build this?"
    a: "When you don't yet have a calibrated panel and a clean data model — software won't fix that — or when you're small enough that a tidy spreadsheet does the job. Power Platform licensing and governance carry real cost; buy the stack when scale justifies it."
  - q: "What does generative AI actually do here?"
    a: "It drafts house-style tasting notes from the scores, summarises a session, writes a first-draft QC release note, and answers plain-language questions via Copilot. Everything is human-reviewed. It communicates what the panel produced — it does not taste."
---

**Short answer: build it in sequence — data model, capture, dashboards, AI, generative AI — and don't buy the stack until you have a calibrated panel and a clean data model behind it.** A digital tasting program fails the same way most data projects fail: people start with the dashboard and discover the data underneath won't support it. Reverse the order.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Building a Digital Tasting Program: Power Platform, ERP, and Gen AI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Step one: the data model decides everything
Before any tool, settle the **data science** basics. Agree the attribute list and scales for each product type. Define your sensory methods — difference tests (triangle, duo-trio, paired), descriptive profiling, trueness-to-type — and how results get statistical treatment for panel agreement and significance. Most importantly, decide the keys: every session must reference a batch, lot, vintage, or cask.

Those keys live in your **ERP** (Dynamics 365 Business Central, Finance & Operations, or similar), which already holds products, batches and lots, recipes, suppliers, and inventory. Linking tasting results to the lot record is what delivers traceability and supports the pass/hold/reject release decision. Skip this step and everything downstream wobbles.

## Step two and three: capture, then visualise
With the model fixed, **capture** comes next. A **Power Apps** canvas or model-driven app on **Dataverse** lets panellists score on a phone or tablet at the bench — across beer, wine, and spirits, the pattern is the same: pick the sample, rate the attributes, flag faults from a controlled list, save offline, sync later. Structured data, entered once, keyed correctly.

Then **dashboards**. **Power BI** turns the scores into the views that drive decisions: attribute trends, control charts against spec, panellist agreement and variance, lot and blend comparisons, fault tracking — all drilling back to the batch or lot from ERP. Resist adding AI until this layer is trusted. If the dashboards are right, the analytics are sound; if they're wrong, no model will save you.

## Step four and five: AI, then generative AI
Only now layer **machine learning**. Use it to calibrate and screen panellists against flavour standards (spiked diacetyl around 0.10 mg/L, acetaldehyde near 10 mg/L, DMS, T2N for staling) and detect drift over time. Use it to flag likely faults — Brett, volatile acidity, TCA, diacetyl, oxidation — and, where you have NIR or FTIR data, to predict sensory attributes with chemometrics so the panel tastes the priorities first.

Then **generative AI** on the very top. From the structured scores it can draft a consistent house-style tasting note, summarise a session for the team, write a first-draft QC release note, and answer plain-language questions through Copilot in Power BI or a Copilot Studio assistant — "show me batches where bitterness drifted above spec this quarter." Every output is human-reviewed before it counts.

## Where this breaks
The most common failure is sequence: buying the Power Platform before the panel is calibrated or the data model is clean. Software amplifies whatever you feed it, so it amplifies a messy panel into messy dashboards faster. The second failure is cost blindness — per-user and per-app licensing, plus the governance effort a clean Dataverse model demands. For a small producer with one or two products, a tidy spreadsheet keyed to lot numbers is often the right answer, and the stack is overkill.

And the limit that never moves: **AI and dashboards don't taste.** The calibrated human panel stays the instrument. Everything in this program — capture, ERP keys, Power BI, ML, Gen AI — exists to capture, structure, analyse, and communicate what the panel produces. The day you let a model make the release call instead of the panel is the day the program has gone wrong.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives the process, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Building a Digital Tasting Program: Power Platform, ERP, and Gen AI</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">The process</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">quality</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">What drives the process, and what it changes downstream.</figcaption>
</figure>

## The bottom line
A digital tasting program is a sequence, not a purchase: data model, capture, dashboards, AI, generative AI — each step earning the next. Anchor it in ERP, capture in Power Apps, analyse in Power BI, and add AI and Gen AI only on clean, calibrated data. Build it in that order and the stack pays back; skip a step and it won't. The panel still tastes.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [building a brewery data foundation for AI]({{ '/2024/building-brewery-data-foundation-ai/' | relative_url }}) and [AI and NIR spectroscopy for rapid QC]({{ '/2024/ai-nir-spectroscopy-rapid-qc/' | relative_url }}).

## Frequently asked questions

**What's the right order to build a digital tasting program?**
Data model, then capture, then dashboards, then AI, then generative AI. Define attributes, scales, and batch/lot keys first; capture in Power Apps on Dataverse; anchor master data in ERP; analyse in Power BI; only then add AI and Gen AI on top of clean, structured data.

**When should I not build this?**
When you don't yet have a calibrated panel and a clean data model — software won't fix that — or when you're small enough that a tidy spreadsheet does the job. Power Platform licensing and governance carry real cost; buy the stack when scale justifies it.

**What does generative AI actually do here?**
It drafts house-style tasting notes from the scores, summarises a session, writes a first-draft QC release note, and answers plain-language questions via Copilot. Everything is human-reviewed. It communicates what the panel produced — it does not taste.
