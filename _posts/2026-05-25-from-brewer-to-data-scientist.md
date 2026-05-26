---
layout: post
title: "From Brewer to Data Scientist: Why I Traded the Brewhouse for AI (And Didn't Really Leave)"
image: /assets/og/from-brewer-to-data-scientist.png
description: "How I went from developing beers for AB InBev and SABMiller to building AI for breweries — and why a brewing background is an advantage, not a handicap, in data science."
date: 2026-05-25 12:00:00 -0700
updated: 2026-05-25
tags: [brewer-to-ai, career, data-science, brewing]
faq:
  - q: "Can a brewer become a data scientist?"
    a: "Yes. Brewing is already a data-rich, process-control discipline, so brewers understand the domain better than most data scientists ever will. The gap is tooling and statistics, which are learnable — the hard-won domain intuition is not."
  - q: "Do you have to quit brewing to work in AI?"
    a: "No. The most useful AI work in beverages comes from people who still think like brewers. I didn't abandon brewing; I added data skills on top of it."
  - q: "What makes brewers good at data science?"
    a: "Brewers already reason about variables, process control, measurement, and cause-and-effect under uncertainty. That mindset transfers directly to data work — often more easily than data scientists pick up brewing."
---

**Short answer: yes, a brewer can become a data scientist — and brewing is an unusually good launchpad for it. I spent about a decade in breweries before data took over my career, and the truth is I never left brewing behind. The domain knowledge turned out to be the hard part to acquire; the data skills were the part I could learn.** Here's how it happened.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="From raw data to a decision the team can act on — the pipeline behind this post."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DATA → DECISION</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">From Brewer to Data Scientist: Why I Traded the Brewhouse for AI (And Didn&#39;t Really…</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Data</text><text x="90.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">sensors, logs</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Features</text><text x="289.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">clean &amp; shape</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Model</text><text x="488.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">train / score</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Prediction</text><text x="687.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">what happens next</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Action</text><text x="886.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">the team acts</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">From raw data to a decision the team can act on — the pipeline behind this post.</figcaption>
</figure>

## I started where most brewers start

I came up through microbreweries before working with the big names: AB InBev, SABMiller, United Breweries. Along the way I developed a dozen beers for the Indian market. My training was classic: a B.Tech in biotechnology, then an MSc in Brewing Science & Technology.

That's a brewer's CV. Nothing about it says "AI."

## Data crept in through the side door

Here's the thing nobody tells you: brewing *is* a data discipline. Every batch is a controlled experiment — temperature curves, gravity readings, pitch rates, sensory panels. I was already living in spreadsheets and process records. Over time my role drifted from making beer to making sense of the numbers behind it, and I moved from graduate trainee toward a senior data-analyst role.

I didn't decide to "become a data scientist." I followed the questions the beer kept asking me — *why did this batch attenuate differently? which beers will sell next month?* — and those questions led straight into data.

## Why brewing beats a CS degree for this

The surprise of my career: my brewing background was an *advantage*, not a handicap. A pure data scientist can build a model, but they don't know what a stuck fermentation feels like or why a sales spike in summer isn't a fluke. I did. Domain intuition is the expensive, slow thing to acquire — and I already had it. The statistics and Python were the learnable part.

If you're a brewer eyeing this path, that's the reframe: you're not starting from zero. You're starting from the half that's hardest to teach.

## What this series is

This is the honest, 8-part story of that transformation — and a practical guide if you want to walk it. We'll cover [what AI actually means for a brewer]({{ '/2026/what-ai-means-for-a-brewer/' | relative_url }}), the unglamorous first steps, my real projects, and — just as important — [where AI burned me]({{ '/2026/where-ai-burned-me/' | relative_url }}). It builds on the bigger picture of [what AI can and can't do for a brewery]({{ '/2026/what-can-ai-do-for-a-brewery/' | relative_url }}).

I still think like a brewer. That's the whole point.

*From Brewer to AI — Part 1 of 8. [See the full series]({{ '/series/brewer-to-ai/' | relative_url }}) · [Next: What AI actually means for a brewer →]({{ '/2026/what-ai-means-for-a-brewer/' | relative_url }})*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 260" width="100%" style="max-width:720px;height:auto" role="img" aria-label="The handful of numbers this comes down to."><rect x="0" y="0" width="720" height="260" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">THE NUMBERS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">From Brewer to Data Scientist: Why I Traded the Brewhouse for AI (And Didn&#39;t…</text><rect x="70" y="90" width="160" height="120" rx="10" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90" y="120" font-family="sans-serif" font-size="12" fill="#6b6258">metric 1</text><rect x="90" y="135" width="120" height="22" rx="3" fill="#b45309"/><text x="90" y="190" font-family="sans-serif" font-size="11.5" fill="#6b6258">vs target</text><rect x="280" y="90" width="160" height="120" rx="10" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="300" y="120" font-family="sans-serif" font-size="12" fill="#6b6258">metric 2</text><rect x="300" y="135" width="100" height="22" rx="3" fill="#b45309"/><text x="300" y="190" font-family="sans-serif" font-size="11.5" fill="#6b6258">vs target</text><rect x="490" y="90" width="160" height="120" rx="10" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="510" y="120" font-family="sans-serif" font-size="12" fill="#6b6258">metric 3</text><rect x="510" y="135" width="80" height="22" rx="3" fill="#b45309"/><text x="510" y="190" font-family="sans-serif" font-size="11.5" fill="#6b6258">vs target</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The handful of numbers this comes down to.</figcaption>
</figure>

## Frequently asked questions

**Can a brewer become a data scientist?**
Yes. Brewing is already a data-rich, process-control discipline, so brewers understand the domain better than most data scientists ever will. The gap is tooling and statistics, which are learnable — the hard-won domain intuition is not.

**Do you have to quit brewing to work in AI?**
No. The most useful AI work in beverages comes from people who still think like brewers. I didn't abandon brewing; I added data skills on top of it.

**What makes brewers good at data science?**
Brewers already reason about variables, process control, measurement, and cause-and-effect under uncertainty. That mindset transfers directly to data work — often more easily than data scientists pick up brewing.
