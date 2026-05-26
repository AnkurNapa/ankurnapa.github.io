---
layout: post
title: "A Sensory-Panel Results Dashboard in Tableau"
image: /assets/og/tableau-sensory-panel-dashboard.png
description: "Build a sensory-panel dashboard in Tableau: attribute scores, panellist agreement and variance, trueness-to-type radar charts and Pulse drift digests."
date: 2023-10-04
updated: 2023-10-04
tags: [brewing-science, tableau, sensory]
faq:
  - q: "How do I show whether panellists agree?"
    a: "Plot the spread of scores per attribute — a box plot or the standard deviation across panellists — alongside the mean. Wide spread on an attribute means low agreement and a panel that may need recalibration on that descriptor."
  - q: "What is a trueness-to-type chart?"
    a: "It compares the panel's mean scores for a beer against the target profile for that style or brand, attribute by attribute. A radar or spider chart overlaying actual versus target makes any drift from the intended character obvious at a glance."
  - q: "Can AI replace the tasting panel?"
    a: "No. Tableau and AI can visualise, monitor and summarise panel data, and instruments can measure some compounds, but neither tastes the beer. The calibrated human panel is the measuring instrument; the dashboard only reports what it recorded."
---

**Short answer: a sensory dashboard makes a trained panel's output legible, but it never replaces the panel.** Tableau is brilliant at showing attribute scores, agreement and trueness-to-type — as long as you remember the panel itself is the instrument and the data is only as good as its calibration.

## Treating the panel as an instrument
A sensory panel is a measuring instrument made of people. Like any instrument it produces data — attribute intensity scores, off-flavour ratings, overall acceptability — and like any instrument it has precision and drift. A sensory dashboard exists to monitor both the beer and the instrument.

The data model is one row per panellist per sample per attribute per session: who tasted, what, when, which descriptor, what score. With that grain, your "measure first" calculated fields fall out naturally — mean score per attribute, standard deviation across panellists (agreement), and per-panellist deviation from the panel mean (calibration). Get this model right and you can analyse the beer *and* the people scoring it.

The companion question of keeping panellists calibrated in the first place is covered in [AI sensory-panel taster calibration]({{ '/2024/ai-sensory-panel-taster-calibration/' | relative_url }}); this post assumes you have the data and want to see it.

## Building the views
Three views carry most of the value.

First, **attribute profile**: bar or line the panel-mean intensity for each descriptor — bitterness, fruity esters, diacetyl, astringency — so you can read the beer's character. Second, **agreement and variance**: a box plot per attribute, or a standard-deviation measure, exposing where the panel diverges. Tight boxes mean a confident, calibrated read; a sprawling box on "diacetyl" flags a descriptor the panel does not share a reference for. Third, **trueness-to-type**: a radar/spider chart overlaying the panel mean against the brand or style target, attribute by attribute, so any drift from the intended profile is unmistakable.

Add a panellist view — each taster's deviation from the panel mean over time — to spot a drifting or harsh-scoring assessor before they distort results. Parameters let you flip between products or sessions; highlight actions let you click an attribute and trace it back to individual scores.

On the AI side, **Tableau Pulse** can monitor the trueness-to-type metric per brand and push a digest when a beer starts drifting from its target profile across sessions — a useful early-warning signal that something has changed in the process or the panel. A generative-AI layer can draft a readable session summary from the scores. Both are reporting aids, not tasters.

## Where it breaks
The hard limit is blunt: AI and Tableau do not taste. They visualise numbers a human panel generated. If the panel is miscalibrated, the dashboard renders the miscalibration in beautiful detail and calls it data. A radar chart of nonsense is still nonsense.

Sensory data is also noisy and small. You are not working with thousands of sensor readings but a handful of trained palates and a few sessions, so apparent "drift" can simply be a panellist with a cold or a tricky sample. Resist over-interpreting small movements; that is exactly the kind of variation a control-chart mindset, borrowed from the QC side, helps you discount. And while instruments can measure some volatiles, they do not capture the integrated perception of flavour balance that is the panel's whole point.

Treat the dashboard as a way to keep your instrument honest and your beers on profile — not as a substitute for the tasting itself.

## The bottom line
A Tableau sensory dashboard turns scattered panel scores into three clear stories: what the beer tastes like, how much the panel agrees, and how true the beer is to type. Pulse can watch for drift and generative AI can draft the write-up, but the calibrated human panel remains the instrument. The dashboard reports the tasting; it does not do it.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [AI sensory-panel taster calibration]({{ '/2024/ai-sensory-panel-taster-calibration/' | relative_url }}).

## Frequently asked questions

**How do I show whether panellists agree?**
Plot the spread of scores per attribute — a box plot or the standard deviation across panellists — alongside the mean. Wide spread on an attribute means low agreement and a panel that may need recalibration on that descriptor.

**What is a trueness-to-type chart?**
It compares the panel's mean scores for a beer against the target profile for that style or brand, attribute by attribute. A radar or spider chart overlaying actual versus target makes any drift from the intended character obvious at a glance.

**Can AI replace the tasting panel?**
No. Tableau and AI can visualise, monitor and summarise panel data, and instruments can measure some compounds, but neither tastes the beer. The calibrated human panel is the measuring instrument; the dashboard only reports what it recorded.
