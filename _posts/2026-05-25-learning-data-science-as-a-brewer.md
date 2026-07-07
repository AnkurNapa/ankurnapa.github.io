---
layout: post
title: "Teaching Myself Data Science as a Working Brewer: The Honest Learning Path"
image: /assets/og/learning-data-science-as-a-brewer.png
description: "How I learned data science while working full-time in breweries — what to study first, what to skip, and why self-study (svadhyaya) beats chasing certificates."
date: 2026-05-25 15:00:00 -0700
updated: 2026-05-25
tags: [brewer-to-ai, learning, data-science, career]
faq:
  - q: "How can a brewer learn data science?"
    a: "Start with statistics and spreadsheets, then SQL to pull your own data, then Python for analysis. Learn on your brewery's real problems, not toy datasets. A formal course helps for structure, but applied self-study on real data is what makes it stick."
  - q: "What should I learn first — Python, statistics, or SQL?"
    a: "Statistics first (so you understand what the numbers mean), then SQL (to get your data), then Python (to analyze it). Tools without statistical understanding produce confident nonsense."
  - q: "Do I need a master's degree to do data science in brewing?"
    a: "No. A degree gives structure and credibility, and I did pursue one by distance learning, but plenty is self-taught. What's non-negotiable is practicing on real problems until the concepts are intuitive."
---

**Short answer: you can learn data science as a working brewer — I did, largely through self-study and a distance master's. The honest path is statistics first, then SQL to get your data, then Python to analyze it — all practiced on your brewery's real problems, not toy datasets. Tools are easy; judgment is what takes time.** Here's the route that worked.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="From raw data to a decision the team can act on — the pipeline behind this post."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DATA → DECISION</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Teaching Myself Data Science as a Working Brewer: The Honest Learning Path</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Data</text><text x="90.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">sensors, logs</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Features</text><text x="289.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">clean &amp; shape</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Model</text><text x="488.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">train / score</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Prediction</text><text x="687.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">what happens next</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Action</text><text x="886.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">the team acts</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">From raw data to a decision the team can act on — the pipeline behind this post.</figcaption>
</figure>

## I learned on the job, then formalized it

My data skills started as curiosity about my own beer — and grew until I went back to school for it, eventually a master's in data science by distance learning while still working. But the degree wasn't the engine. The engine was *svadhyaya* — self-study — applied relentlessly to problems I actually cared about.

That's my first piece of advice: don't wait for a course to begin. Begin on a real question from your own brewhouse.

## The order that actually works

I see brewers rush to "learn Python" and stall. Here's the sequence I'd recommend instead:

1. **Statistics first.** Not heavy math — intuition. What's a distribution, a correlation, an average that lies to you, overfitting. Without this, tools just help you be wrong faster.
2. **SQL second.** Boring, essential. It's how you get your own data out of whatever system holds it. The moment you can answer your own questions, momentum builds.
3. **Python third.** Now you have something to analyze. Pandas and a plotting library go a long way before you ever touch machine learning.

Notice machine learning comes *last*, and it's a smaller part than the hype implies.

## Learn on real problems

The single biggest accelerator: practice on your brewery's data, not tutorials. "Will this batch finish on time?" "Which beer sells out in summer?" Real questions force you to deal with messy data, missing values, and ambiguous answers — which is the actual job. Tutorials never teach that.

## What to skip (for now)

You don't need deep learning, big-data infrastructure, or the latest model to add value. I wasted time early chasing shiny techniques. The fundamentals — clean data, sound statistics, a simple model you understand — carried 90% of the results. The fancy stuff is mostly for problems a brewery rarely has.

Next: my first real project, and the honest scorecard of what worked and what flopped.

*From Brewer to AI — Part 4 of 8. [Full series]({{ '/series/brewer-to-ai/' | relative_url }}) · [Next: My first AI project →]({{ '/2026/my-first-ai-project-beer-demand-forecasting/' | relative_url }})*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 260" width="100%" style="max-width:720px;height:auto" role="img" aria-label="The handful of numbers this comes down to."><rect x="0" y="0" width="720" height="260" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">THE NUMBERS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Teaching Myself Data Science as a Working Brewer: The Honest Learning Path</text><rect x="70" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">metric 1</text><rect x="90" y="135" width="120" height="22" rx="3" fill="#00695c"/><text x="90" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs target</text><rect x="280" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="300" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">metric 2</text><rect x="300" y="135" width="100" height="22" rx="3" fill="#00695c"/><text x="300" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs target</text><rect x="490" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="510" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">metric 3</text><rect x="510" y="135" width="80" height="22" rx="3" fill="#00695c"/><text x="510" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs target</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The handful of numbers this comes down to.</figcaption>
</figure>

## Frequently asked questions

**How can a brewer learn data science?**
Start with statistics and spreadsheets, then SQL to pull your own data, then Python for analysis. Learn on your brewery's real problems, not toy datasets. A formal course helps for structure, but applied self-study on real data is what makes it stick.

**What should I learn first — Python, statistics, or SQL?**
Statistics first (so you understand what the numbers mean), then SQL (to get your data), then Python (to analyze it). Tools without statistical understanding produce confident nonsense.

**Do I need a master's degree to do data science in brewing?**
No. A degree gives structure and credibility, and I did pursue one by distance learning, but plenty is self-taught. What's non-negotiable is practicing on real problems until the concepts are intuitive.
