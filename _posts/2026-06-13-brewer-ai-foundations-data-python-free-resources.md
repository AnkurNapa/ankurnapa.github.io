---
layout: post
title: "Foundations First: Data Literacy and Python for Brewers (Free Resources)"
image: /assets/og/brewer-ai-foundations-data-python-free-resources.png
description: "Stages 1 and 2 of the brewer's AI roadmap — data literacy with spreadsheets and Power BI, then Python — using only free, open resources: Microsoft Learn, Kaggle Learn and freeCodeCamp, with a real brewing project to learn against."
date: 2026-06-12 10:10:00 -0700
updated: 2026-06-12
tags: [brewing-science, brewer-ai-roadmap, learning, power-bi, data-science]
faq:
  - q: "What should a brewer learn first to get into data and AI?"
    a: "Data literacy before code: get fluent with spreadsheets (clean data, pivot tables, lookups) and then a real BI tool like Power BI to build a dashboard on your own brewery data. Microsoft Learn's free Power BI and Data Fundamentals (DP-900) paths cover this end to end. Only after you can confidently see and shape data does Python become worth your evenings."
  - q: "What free resources teach Python for data work?"
    a: "freeCodeCamp's Python curriculum and Kaggle Learn's Python and Pandas micro-courses are both free and hands-on. Kaggle runs entirely in the browser with no setup, which removes the most common reason beginners quit. Aim for enough Python to load a spreadsheet, clean it, and chart it — not software engineering."
  - q: "Do brewers need Power BI or Python first?"
    a: "Power BI (or any BI tool) first. It delivers value fastest, needs no coding, and builds the data-shaping instincts that make Python far easier later. Python is the second stage — it unlocks machine learning and automation, but it pays off much more once you already think clearly about tables, joins and clean data."
---

**Short answer: start with data literacy, not code. Stage 1 is spreadsheets done properly and then Power BI, so you can clean, join and actually see your brewery's data — Microsoft Learn's free Power BI and Data Fundamentals paths cover it. Stage 2 is Python, just enough to load a spreadsheet, clean it and chart it, learned hands-on through freeCodeCamp and Kaggle Learn. Both stages are free, and both should be driven by one real brewing question rather than toy datasets — that's the difference between finishing and quitting in week three.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 300" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Two foundation stages for a brewer: stage one data literacy from spreadsheets to Power BI using Microsoft Learn, stage two Python using freeCodeCamp and Kaggle Learn, both feeding into machine learning."><rect width="1000" height="300" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE TWO FOUNDATIONS — BUILD THESE FIRST</text><g font-family="sans-serif"><rect x="60" y="60" width="380" height="170" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="250" y="90" text-anchor="middle" font-size="14" font-weight="700" fill="#06483f">Stage 1 &#183; Data literacy</text><text x="250" y="118" text-anchor="middle" font-size="11" fill="#4a6b64">clean data &#183; pivot tables &#183; lookups</text><text x="250" y="140" text-anchor="middle" font-size="11" fill="#4a6b64">then a real Power BI dashboard</text><rect x="100" y="158" width="300" height="34" rx="6" fill="#ffffff" stroke="#00695c"/><text x="250" y="180" text-anchor="middle" font-size="10.5" fill="#06483f">Microsoft Learn: Power BI &#183; DP-900</text><text x="250" y="214" text-anchor="middle" font-size="11" font-weight="700" fill="#00695c">value on the floor immediately</text><rect x="560" y="60" width="380" height="170" rx="10" fill="#06483f"/><text x="750" y="90" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">Stage 2 &#183; Python</text><text x="750" y="118" text-anchor="middle" font-size="11" fill="#cfe6df">load &#183; clean &#183; chart a spreadsheet</text><text x="750" y="140" text-anchor="middle" font-size="11" fill="#cfe6df">Pandas, not software engineering</text><rect x="600" y="158" width="300" height="34" rx="6" fill="#ffffff"/><text x="750" y="180" text-anchor="middle" font-size="10.5" fill="#06483f">freeCodeCamp &#183; Kaggle Learn</text><text x="750" y="214" text-anchor="middle" font-size="11" font-weight="700" fill="#cfe6df">unlocks machine learning next</text></g><text x="500" y="270" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">do them in order — Python is far easier once you already think clearly in tables</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Power BI first for fast value and data instincts; Python second to unlock everything after.</figcaption>
</figure>

This is part two of the [brewer's AI roadmap]({{ '/2026/brewer-ai-roadmap-step-by-step/' | relative_url }}). Part one laid out the five stages; this post is the detailed walk-through of the two foundations — data literacy and Python — with the exact free resources and how to use them without burning out.

## Stage 1 — Data literacy, spreadsheets to Power BI

Most brewers already live in spreadsheets, but "using Excel" and "data literacy" aren't the same thing. The skills that matter: keeping data *tidy* (one row per observation, one column per variable — a fermentation log, not a formatted report), pivot tables to summarise, lookups to join your brew log to your QC results, and basic charts that don't mislead. Get these solid in a spreadsheet first; they are the same concepts every tool above reuses.

Then step up to **Power BI**, because seeing your data interactively is the fastest value in this whole roadmap and needs no code. The free path:

- [**Microsoft Learn — Power BI**](https://learn.microsoft.com/training/) — guided, hands-on modules from "connect to data" through building and sharing a report. Work the **PL-300** learning path if you want structure.
- [**Microsoft Learn — Data Fundamentals (DP-900)**](https://learn.microsoft.com/training/) — the vocabulary of data (tables, relational vs analytical, what a data model *is*) that makes everything later click.

Do it against **your own brewery data**, not the sample sales file. Build a real dashboard: extract efficiency by batch, fermentation curves, QC pass rates, cellar stock. The moment your head brewer asks a question and you answer it from your dashboard in ten seconds, the learning has paid for itself — and that's the loop from [the four analytics]({{ '/2026/four-types-data-analytics-distillery-fabric/' | relative_url }}), starting on the descriptive rung where it should.

## Stage 2 — Python, just enough

Python is where many brewers stall, usually because they're sold a computer-science course when they need a data-handling skill. Reframe it: you are learning to do *in code* what you already do in spreadsheets — load a file, clean it, join it, chart it — so it scales and repeats. That's **Pandas**, and it's a few evenings, not a degree.

The free, hands-on path:

- [**Kaggle Learn — Python**](https://www.kaggle.com/learn) then [**Pandas**](https://www.kaggle.com/learn) — short, browser-based, *zero setup*. No-install matters more than it sounds: "couldn't get Python installed" is where most beginners quit, and Kaggle removes it entirely.
- [**freeCodeCamp**](https://www.freecodecamp.org/learn) — for a fuller, project-driven grounding in Python if you want more depth before Pandas.

Set a concrete target: take a messy brew-log CSV, load it in Pandas, fix the dates and units, and plot original gravity against final attenuation for the year. When you've done that with your own data, you have enough Python to start machine learning — and not coincidentally, cleaning that file is 80% of what real data work actually is.

## Why this order, not the reverse

Brewers sometimes want to jump straight to Python because it sounds like "real AI". Resist it. Power BI first builds the table-and-join instincts that make Pandas legible instead of cryptic; it delivers visible value while Python is still abstract; and it keeps you motivated through the dry parts because you're already useful. Python second then unlocks the machine learning in [part three]({{ '/2026/brewer-first-machine-learning-model-free-courses/' | relative_url }}) and the automation beyond it. Skip the order and Python feels like punishment; follow it and Python feels like a power-up.

## Where this breaks

The honest caveats. **Tutorial hell is real** — endlessly watching courses *feels* like learning while building nothing; the cure is to stop a course the moment you can attempt your own brewery project and learn the rest by getting stuck on it. **Power BI's free tier has limits** — Desktop is free and enough to learn and build; *sharing* dashboards properly may need a paid licence your brewery buys, which is a workplace conversation, not a blocker to learning. **Python setup still bites outside Kaggle** — when you move to your own machine, expect a frustrating environment day; that's normal, not a sign you can't code. And **spreadsheets never fully go away** — learning Power BI and Python doesn't retire Excel; the goal is judgement about which tool fits, not purity.

## The bottom line

The two foundations are data literacy and Python, in that order, both free. Get tidy-data and pivot-table fluent, then build a real Power BI dashboard on your own beer data with Microsoft Learn; then learn just enough Python through Kaggle Learn and freeCodeCamp to load, clean and chart that same data in code. Drive both with one stubborn brewing question, ship something small at each step, and you'll arrive at machine learning already thinking like a data person. That's [the next stage]({{ '/2026/brewer-first-machine-learning-model-free-courses/' | relative_url }}): your first model.

## Frequently asked questions

**What should a brewer learn first to get into data and AI?**
Data literacy before code: get fluent with spreadsheets (clean data, pivot tables, lookups) and then a real BI tool like Power BI to build a dashboard on your own brewery data. Microsoft Learn's free Power BI and Data Fundamentals (DP-900) paths cover this end to end. Only after you can confidently see and shape data does Python become worth your evenings.

**What free resources teach Python for data work?**
freeCodeCamp's Python curriculum and Kaggle Learn's Python and Pandas micro-courses are both free and hands-on. Kaggle runs entirely in the browser with no setup, which removes the most common reason beginners quit. Aim for enough Python to load a spreadsheet, clean it, and chart it — not software engineering.

**Do brewers need Power BI or Python first?**
Power BI (or any BI tool) first. It delivers value fastest, needs no coding, and builds the data-shaping instincts that make Python far easier later. Python is the second stage — it unlocks machine learning and automation, but it pays off much more once you already think clearly about tables, joins and clean data.
