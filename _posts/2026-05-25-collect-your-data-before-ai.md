---
layout: post
title: "Before You Touch AI, Collect Your Data: The Unglamorous First Step"
image: /assets/og/collect-your-data-before-ai.png
description: "The first move in any brewery's AI journey isn't a model — it's data collection. What to log, what sensors matter, and why clean records beat clever algorithms every time."
date: 2026-05-25 14:00:00 -0700
updated: 2026-05-25
tags: [brewer-to-ai, brewing-data, data-collection]
faq:
  - q: "What's the first step for a brewery getting into AI?"
    a: "Collecting clean, consistent data — not buying a model. Log fermentation temperature, gravity, pitch rate, batch outcomes, and sales over time. Without that history, no AI tool has anything to learn from."
  - q: "What data should a brewery collect?"
    a: "Process data (temperature over time, gravity, pH, dissolved oxygen, pitch rate), batch outcomes (what went right or wrong), and commercial data (sales by product, time, and place). Consistency matters more than volume."
  - q: "Do I need expensive sensors to start?"
    a: "No. Start by logging consistently what you already measure. Continuous sensors help, but a disciplined manual record beats a fancy sensor that nobody reads."
---

**Short answer: the first step in a brewery's AI journey isn't a model or a sensor — it's collecting clean, consistent data. Every project I've ever built lived or died on the quality of the records feeding it. Boring as it sounds, disciplined data collection beats clever algorithms every single time.** Here's what I wish I'd logged earlier.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="From raw data to a decision the team can act on — the pipeline behind this post."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DATA → DECISION</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Before You Touch AI, Collect Your Data: The Unglamorous First Step</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Data</text><text x="90.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">sensors, logs</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Features</text><text x="289.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">clean &amp; shape</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Model</text><text x="488.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">train / score</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Prediction</text><text x="687.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">what happens next</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Action</text><text x="886.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">the team acts</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">From raw data to a decision the team can act on — the pipeline behind this post.</figcaption>
</figure>

## The mistake everyone makes (including me)

When I first got excited about data, I wanted to build models. What I learned the hard way: a model is only as good as the history behind it, and most breweries — mine included — had gaps everywhere. Readings taken "when someone remembered," outcomes never recorded, sales data living in a different system entirely.

You can't predict what you never measured. So before any AI, you instrument and you log.

## What to actually collect

Three categories cover most of it:

1. **Process data** — fermentation temperature *over time*, gravity, pH, dissolved oxygen, pitch rate. The "over time" part matters: a curve teaches a model far more than a single reading. This is the foundation for things like [fermentation forecasting]({{ '/2026/can-ai-predict-beer-fermentation/' | relative_url }}) and [quality control]({{ '/2026/ai-quality-control-in-brewing/' | relative_url }}).
2. **Batch outcomes** — what actually happened. Was it on-style? Did it stick? Any off-flavor? Without labeled outcomes, a model can't learn what "good" and "bad" look like.
3. **Commercial data** — sales by product, time, and place. This is the fuel for [demand forecasting]({{ '/2026/ai-demand-forecasting-for-breweries/' | relative_url }}), one of the highest-ROI uses there is.

## Consistency beats sophistication

You do not need a wall of expensive sensors to begin. You need to log *consistently* what you already measure. A cheap setup recorded faithfully every batch is worth more than a research-grade sensor whose data nobody trusts because half the entries are missing.

When I advise breweries now, the unglamorous truth I lead with is this: spend your first months on measurement discipline, not on models. The models can wait. The data can't be recovered after the fact.

## The payoff

Do this, and everything downstream gets easier and cheaper. Skip it, and you'll spend money on AI that has nothing reliable to learn from — the most common way breweries waste their first AI budget.

Next: how I taught myself the data side while still working as a brewer.

*From Brewer to AI — Part 3 of 8. [Full series]({{ '/series/brewer-to-ai/' | relative_url }}) · [Next: Teaching myself data science →]({{ '/2026/learning-data-science-as-a-brewer/' | relative_url }})*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 260" width="100%" style="max-width:720px;height:auto" role="img" aria-label="The handful of numbers this comes down to."><rect x="0" y="0" width="720" height="260" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">THE NUMBERS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Before You Touch AI, Collect Your Data: The Unglamorous First Step</text><rect x="70" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">metric 1</text><rect x="90" y="135" width="120" height="22" rx="3" fill="#00695c"/><text x="90" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs target</text><rect x="280" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="300" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">metric 2</text><rect x="300" y="135" width="100" height="22" rx="3" fill="#00695c"/><text x="300" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs target</text><rect x="490" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="510" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">metric 3</text><rect x="510" y="135" width="80" height="22" rx="3" fill="#00695c"/><text x="510" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs target</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The handful of numbers this comes down to.</figcaption>
</figure>

## Frequently asked questions

**What's the first step for a brewery getting into AI?**
Collecting clean, consistent data — not buying a model. Log fermentation temperature, gravity, pitch rate, batch outcomes, and sales over time. Without that history, no AI tool has anything to learn from.

**What data should a brewery collect?**
Process data (temperature over time, gravity, pH, dissolved oxygen, pitch rate), batch outcomes (what went right or wrong), and commercial data (sales by product, time, and place). Consistency matters more than volume.

**Do I need expensive sensors to start?**
No. Start by logging consistently what you already measure. Continuous sensors help, but a disciplined manual record beats a fancy sensor that nobody reads.
