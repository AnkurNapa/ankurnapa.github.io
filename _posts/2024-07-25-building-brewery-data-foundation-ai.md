---
layout: post
title: "Building a Brewery Data Foundation Before You Touch AI"
image: /assets/og/building-brewery-data-foundation-ai.png
description: "Why a process historian, consistent tags, a data model and data quality are the prerequisites for brewery AI — and why most projects fail on plumbing, not algorithms."
date: 2024-07-25
updated: 2024-07-25
tags: [brewing-science, data-strategy, analytics]
faq:
  - q: "What does a brewery data foundation actually consist of?"
    a: "A process historian or time-series database, consistent tag naming, a data model that relates tags to assets and batches, and basic data quality. Those four pieces are the prerequisite for every AI use case in the brewery."
  - q: "Why do brewery AI projects fail?"
    a: "Most fail on data plumbing, not algorithms. Inconsistent tags, missing history and poor data quality starve the models — the maxim is measure first, model second."
  - q: "Can generative AI fix a missing data foundation?"
    a: "No. An LLM can let staff query a historian in plain language and help document tags and SOPs, but only once the foundation exists. It cannot conjure history that was never recorded."
---

**Short answer: before any brewery AI works, you need a process historian, consistent tags, a data model and basic data quality — because most AI projects fail on plumbing, not algorithms.** This is the unglamorous backbone under energy, water, maintenance and QC alike.

## The capstone everyone skips
Every other use case in this track — forecasting steam demand, cutting effluent, predicting a pump failure, calibrating NIR — assumes one thing: that the data exists, is consistent, and can be trusted. Strip that away and the cleverest model has nothing to learn from. The hard truth from the field is that the failure point is rarely the algorithm. It is the data plumbing: tags named three different ways, gaps where a logger dropped out, no link between a sensor reading and the batch it belongs to.

So the maxim is measure first, model second. A brewery that invests in its data foundation before chasing AI ends up with cheaper, faster, more reliable projects across the board. One that skips it pays for the same gaps over and over.

## The four pieces
A workable foundation has four parts.

**A process historian.** A time-series database that captures sensor and process data continuously, at a sensible resolution, and keeps it. You cannot model trends you never stored.

**Consistent tags.** Every measured point needs a stable, predictable name. "FV3 temperature" should mean the same thing everywhere, every time. Inconsistent tags are the single most common reason analytics stalls.

**A data model.** Tags alone are noise until you relate them — this sensor to that vessel, this reading to that batch, this batch to that recipe. The model is what lets you ask "how did this lager ferment" instead of staring at raw streams.

**Data quality.** Gaps, frozen values, miscalibrated sensors and unit muddles all poison models quietly. Basic quality checks — completeness, range, plausibility — are non-negotiable groundwork.

## Where it breaks
Be realistic about the limits of a foundation, too. It is an ongoing discipline, not a one-off project — tags proliferate, sensors drift, and new equipment arrives with its own conventions, so governance has to be maintained or the foundation decays. It also takes patience: the payback is indirect, because the historian itself does not optimise anything; it enables the things that do. And it cannot recover the past — history you never recorded is simply gone, which is exactly why you start logging before you think you need to. Resist the temptation to jump straight to a flashy model; the boring layer is what makes the flashy layer work.

## The generative layer
Here the gen-AI angle is genuinely useful — but conditional. Once the foundation exists, an LLM can sit on top of the historian and let staff query it in plain language: "show me last month's fermentation temperatures for the IPA tanks" returns a chart, not a SQL lesson. The same tool can auto-document tags and draft SOPs, easing the very governance burden that keeps foundations alive. But note the order. Generative AI amplifies a good foundation; it cannot substitute for a missing one. Point an LLM at chaotic, untagged, gap-ridden data and it will answer confidently and wrongly.

## The bottom line
The data foundation is the least exciting and most decisive part of brewery AI. A historian, consistent tags, a data model and data quality are what turn every other use case from aspiration into delivery. Build that first, keep it governed, and let generative tools make it accessible — in that order. Measure first, model second, and the rest of the track pays off.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Collect your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}) and [Brewhouse yield-loss analytics]({{ '/2023/brewhouse-yield-loss-analytics/' | relative_url }}).

## Frequently asked questions

**What does a brewery data foundation actually consist of?**
A process historian or time-series database, consistent tag naming, a data model that relates tags to assets and batches, and basic data quality. Those four pieces are the prerequisite for every AI use case in the brewery.

**Why do brewery AI projects fail?**
Most fail on data plumbing, not algorithms. Inconsistent tags, missing history and poor data quality starve the models — the maxim is measure first, model second.

**Can generative AI fix a missing data foundation?**
No. An LLM can let staff query a historian in plain language and help document tags and SOPs, but only once the foundation exists. It cannot conjure history that was never recorded.
