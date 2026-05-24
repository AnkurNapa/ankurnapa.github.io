---
layout: post
title: "Building a Digital Tasting Program: Power Platform, ERP, and Gen AI"
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
