---
layout: post
title: "A Brewer's Map of Their Own Data — and What Each Source Can Actually Answer"
image: /assets/og/brewery-data-map-what-it-answers.png
description: "Brew logs, fermentation sensors, lab results, POS and inventory: a plain map of the data a small brewery already has, and the specific questions each source can — and cannot — answer."
date: 2026-06-06
updated: 2026-06-06
tags: [brewing-science, asking-better-questions, data-platform, analytics, beginners]
faq:
  - q: "What data does a small brewery already have without buying anything?"
    a: "More than most realise: brew-day logs (gravities, temperatures, times, volumes), fermentation readings, simple sensory notes, supplier certificates of analysis, plus sales, inventory and purchasing records. Most of it is just trapped in notebooks, PDFs and till systems."
  - q: "Which brewery questions need which data?"
    a: "Match the question to the source: consistency questions need brew logs across batches; fermentation questions need time-series gravity and temperature; profitability questions need sales and costing data; quality-complaint questions need packaging dates joined to sensory notes. A question that spans sources needs the sources joined — usually by batch number."
  - q: "Do I need sensors and a data platform before asking AI about my brewery data?"
    a: "No. A consistent spreadsheet with one row per batch and a real batch ID beats an expensive sensor stack with no discipline. Structure and consistency matter more than volume; you can paste a tidy CSV straight into an AI assistant today."
---

**Short answer: "use AI on your data" fails for most small breweries not because the data is missing but because nobody has mapped it. The data exists — brew sheets, fermentation readings, supplier COAs, the till, the stock count — it's just scattered across notebooks, PDFs and systems that don't talk to each other, and nobody has matched each source to the questions it can actually answer. Draw that map once and two things happen: your AI prompts get sharp, and you discover which questions you can't answer yet because you're not recording the thing that would answer them.** Here's the map.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Five piles of brewery data — brew-day logs, fermentation records, quality and sensory, commercial records, inventory and purchasing — each answering a different family of questions, all joined by the batch number."><rect width="1000" height="320" fill="#ffffff"/><text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE FIVE PILES &#8212; AND THE JOIN THAT CONNECTS THEM</text><g font-family="sans-serif"><rect x="20" y="60" width="180" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="110" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Brew-day logs</text><text x="110" y="115" text-anchor="middle" font-size="10.5" fill="#4a6b64">gravities &#183; temps &#183; times</text><text x="110" y="140" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">consistency &amp;</text><text x="110" y="155" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">efficiency questions</text><rect x="215" y="60" width="180" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="305" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Fermentation</text><text x="305" y="115" text-anchor="middle" font-size="10.5" fill="#4a6b64">gravity &amp; temp over time</text><text x="305" y="140" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">process &amp; strain</text><text x="305" y="155" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">questions</text><rect x="410" y="60" width="180" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="500" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Quality &amp; sensory</text><text x="500" y="115" text-anchor="middle" font-size="10.5" fill="#4a6b64">notes &#183; faults &#183; COAs</text><text x="500" y="140" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">"why does it taste</text><text x="500" y="155" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">like that" questions</text><rect x="605" y="60" width="180" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="695" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Commercial</text><text x="695" y="115" text-anchor="middle" font-size="10.5" fill="#4a6b64">POS &#183; taproom &#183; distributors</text><text x="695" y="140" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">demand &amp; pricing</text><text x="695" y="155" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">questions</text><rect x="800" y="60" width="180" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="890" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Inventory &amp; cost</text><text x="890" y="115" text-anchor="middle" font-size="10.5" fill="#4a6b64">stock &#183; lots &#183; prices</text><text x="890" y="140" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">margin &amp; planning</text><text x="890" y="155" text-anchor="middle" font-size="10.5" font-weight="700" fill="#06483f">questions</text></g><g stroke="#06483f" stroke-width="2"><line x1="110" y1="180" x2="110" y2="230"/><line x1="305" y1="180" x2="305" y2="230"/><line x1="500" y1="180" x2="500" y2="230"/><line x1="695" y1="180" x2="695" y2="230"/><line x1="890" y1="180" x2="890" y2="230"/></g><rect x="60" y="230" width="880" height="56" rx="10" fill="#06483f"/><text x="500" y="254" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">THE BATCH NUMBER &#8212; written the same way on every sheet</text><text x="500" y="274" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#f0f6f5">the cheapest data infrastructure a brewery will ever build; the cross-pile questions live here</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Each pile answers a small family of questions; the questions worth asking span piles — and the batch number is the join.</figcaption>
</figure>

## The five piles of brewery data

Nearly everything a small brewery records falls into five piles, and each pile answers a different family of questions.

**1. Brew-day logs** — grist weights, mash temperatures and times, pre- and post-boil gravities and volumes, hop additions, yeast and pitch details. This pile answers *consistency and efficiency* questions: "Is my brewhouse efficiency drifting?" "Which recipes show the worst batch-to-batch variance in OG?" One row per batch, and suddenly variance is visible instead of anecdotal.

**2. Fermentation records** — gravity and temperature over time, by tank. This is your only *time-series* pile, and it answers process questions nothing else can: "How long does this strain take from pitch to terminal at 18°C?" "Did the stuck batches share a slow first 48 hours?" Even hand-taken daily readings work; a Tilt or PLC just takes them more often.

**3. Quality and sensory** — tasting notes, fault flags, lab results if you have them, plus the supplier's certificates of analysis for malt, hops and yeast. This pile answers *"why does it taste like that"* questions — but only if notes are structured enough to compare. "Slightly off" written 40 different ways is 40 unjoinable opinions; a simple fixed checklist (clean / diacetyl / acetaldehyde / oxidised / phenolic, 1–5 intensity) is data.

**4. Commercial records** — the till or POS, distributor reports, taproom sales. Answers *demand* questions: what sells, when, at what price, in which format. This is the pile that fed [my first real AI project, demand forecasting]({{ '/2026/my-first-ai-project-beer-demand-forecasting/' | relative_url }}) — and it's usually the cleanest data in the building because money forces discipline.

**5. Inventory and purchasing** — raw-material stock, packaging stock, costs per lot. Answers *margin and planning* questions: true cost per batch, weeks of cover on a hop contract, which beer quietly loses money at keg prices.

## The join is where the good questions live

Each pile alone answers small questions. The questions worth asking sit *across* piles, and the thing that connects them is humble: **the batch number.** "Do batches fermented above 20°C get more off-flavour complaints?" joins pile 2 to pile 3. "Is the beer with the worst gravity variance also the one with the worst margin?" joins 1 to 5. "Did the lot change in pale malt (COA in pile 3) coincide with the efficiency dip (pile 1)?" — that's the question an experienced head brewer asks instinctively, and a beginner can now ask with a join.

This is why the advice in [collect your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}) comes first: a batch ID written consistently on the brew sheet, the tank board, the sensory sheet and the costing spreadsheet is the cheapest piece of data infrastructure a brewery will ever build.

## What this means for your AI prompts

Once the map exists, prompts stop being vague. Instead of "analyse my brewery data," you can paste one tidy table and ask one pile-appropriate question: *"Here are 30 batches of our pale ale — date, OG, FG, mash temp, efficiency. Which variables move together, and what would you check first to explain the efficiency drift after batch 18?"* A language model is genuinely good at this: reading a small table, spotting the pattern, explaining it in brewer's language, and telling you what it would want to see next. And classic machine learning enters the same way — the fermentation pile is exactly what trains a model to [predict where a fermentation will land]({{ '/2026/npd-recipe-sensory-data-development/' | relative_url }}) before the tank tells you.

## Where this breaks

The map has honest edges. **Paper that never becomes a table answers nothing** — a notebook is storage, not data, until someone types it in or photographs it into a model with vision. **Joins fail without discipline:** if the same beer is "PA-7", "Pale 7" and "the Citra one" across systems, no tool can connect them. **Small numbers limit conclusions** — with 12 batches a "pattern" is often noise, and AI will narrate noise as confidently as signal; treat early findings as hypotheses to test, not verdicts. And **sensitive commercial data deserves care**: keep customer names and supplier pricing out of what you paste into public tools, or use a structured export with those columns dropped.

## The bottom line

Before any brewery buys sensors, dashboards or an "AI platform," it should spend an afternoon with a whiteboard drawing five boxes — brew log, fermentation, quality, sales, inventory — listing what's actually recorded in each, and writing the batch number across all of them. That map turns "we should use AI on our data" into a dozen specific, answerable questions, and it exposes the gaps honestly: every question you want to ask but can't is a measurement you're not yet taking. Map first, measure second, model third.

## Frequently asked questions

**What data does a small brewery already have without buying anything?**
More than most realise: brew-day logs (gravities, temperatures, times, volumes), fermentation readings, simple sensory notes, supplier certificates of analysis, plus sales, inventory and purchasing records. Most of it is just trapped in notebooks, PDFs and till systems.

**Which brewery questions need which data?**
Match the question to the source: consistency questions need brew logs across batches; fermentation questions need time-series gravity and temperature; profitability questions need sales and costing data; quality-complaint questions need packaging dates joined to sensory notes. A question that spans sources needs the sources joined — usually by batch number.

**Do I need sensors and a data platform before asking AI about my brewery data?**
No. A consistent spreadsheet with one row per batch and a real batch ID beats an expensive sensor stack with no discipline. Structure and consistency matter more than volume; you can paste a tidy CSV straight into an AI assistant today.

*Part of the [Brewing Science]({{ '/tracks/brewing-science/' | relative_url }}) track.*
