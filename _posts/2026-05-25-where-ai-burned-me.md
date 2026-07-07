---
layout: post
title: "Where AI Burned Me: Hallucinations, Bad Data, and Hype I Believed"
image: /assets/og/where-ai-burned-me.png
description: "An honest account of my worst AI mistakes in brewing — trusting confident-but-wrong outputs, building on dirty data, and chasing hype. The failures that taught me the most."
date: 2026-05-25 17:00:00 -0700
updated: 2026-05-25
tags: [brewer-to-ai, hallucination, ai-limits, lessons]
faq:
  - q: "What are common AI mistakes in brewing?"
    a: "Trusting confident but wrong outputs (including AI hallucinations), building models on inconsistent data, over-engineering simple problems, and believing vendor hype. Most failures trace back to bad data or misplaced trust, not bad algorithms."
  - q: "Does AI really hallucinate in brewing work?"
    a: "Yes. Generative AI will produce precise, authoritative, and completely wrong figures — recipe numbers, regulatory rules, tasting descriptions. If you don't verify every output, it will eventually burn you."
  - q: "How do you avoid getting burned by AI?"
    a: "Verify every number against real records, prefer the simplest tool that works, be ruthless about data quality, and never let a confident output replace your own judgment."
---

**Short answer: AI burned me more than once — and almost always in the same ways: I trusted a confident output that was wrong, I built on data that was dirtier than I admitted, or I believed the hype and over-engineered a simple problem. None of these were algorithm failures. They were trust failures. Here are the mistakes, so you can skip them.** This is the post I most want brewers to read.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="From raw data to a decision the team can act on — the pipeline behind this post."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DATA → DECISION</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Where AI Burned Me: Hallucinations, Bad Data, and Hype I Believed</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Data</text><text x="90.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">sensors, logs</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Features</text><text x="289.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">clean &amp; shape</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Model</text><text x="488.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">train / score</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Prediction</text><text x="687.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">what happens next</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Action</text><text x="886.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">the team acts</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">From raw data to a decision the team can act on — the pipeline behind this post.</figcaption>
</figure>

## Mistake 1: trusting confident, wrong answers

Modern AI — especially generative tools — produces output that *sounds* authoritative. Early on, I treated a clean, specific number as if "specific" meant "correct." It doesn't. Generative models **hallucinate**: they'll hand you a precise recipe figure, a regulatory threshold, or a tasting note with total confidence and zero basis. I've watched one invent a citation that didn't exist.

The fix is unglamorous and absolute: verify every number against real records. I learned to treat AI like a brilliant intern who writes beautifully and cannot be trusted with arithmetic. (More on this in [the honest limits of AI in brewing]({{ '/2026/the-honest-limits-of-ai-in-brewing/' | relative_url }}) and the very real danger of letting it near [TTB/compliance numbers]({{ '/2026/can-ai-write-your-ttb-reports/' | relative_url }}).)

## Mistake 2: building on bad data

I once got excited about a model's results before checking the data underneath. The data was inconsistent — gaps, mislabeled batches, two systems disagreeing. The model dutifully learned the mess and gave me confident garbage. "Garbage in, garbage out" isn't a cliché; it's the single most common way brewery AI projects fail, and I fell for it.

## Mistake 3: chasing hype and over-engineering

I spent time on sophisticated techniques for problems that a control chart or a seasonal average would have solved. The fancy approach felt like progress; it was mostly cost. The inefficiency wasn't slow code — it was spending effort and money on sophistication the problem never required.

## Mistake 4: believing AI would do more than it can

The marketing told me AI would "transform" everything. The reality: it's a sharp tool for a narrow band of well-defined, data-rich problems — and useless or harmful outside it. Mistaking the marketing for the map cost me time I won't get back.

## What the burns taught me

Every one of these lessons points the same direction: AI is an assistant with no judgment of its own. Which raises the question the next post tackles head-on — what, exactly, can't it do?

*From Brewer to AI — Part 6 of 8. [Full series]({{ '/series/brewer-to-ai/' | relative_url }}) · [Next: AI won't replace brewers →]({{ '/2026/ai-wont-replace-brewers/' | relative_url }})*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 260" width="100%" style="max-width:720px;height:auto" role="img" aria-label="The handful of numbers this comes down to."><rect x="0" y="0" width="720" height="260" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">THE NUMBERS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Where AI Burned Me: Hallucinations, Bad Data, and Hype I Believed</text><rect x="70" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">metric 1</text><rect x="90" y="135" width="120" height="22" rx="3" fill="#00695c"/><text x="90" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs target</text><rect x="280" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="300" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">metric 2</text><rect x="300" y="135" width="100" height="22" rx="3" fill="#00695c"/><text x="300" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs target</text><rect x="490" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="510" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">metric 3</text><rect x="510" y="135" width="80" height="22" rx="3" fill="#00695c"/><text x="510" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs target</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The handful of numbers this comes down to.</figcaption>
</figure>

## Frequently asked questions

**What are common AI mistakes in brewing?**
Trusting confident but wrong outputs (including AI hallucinations), building models on inconsistent data, over-engineering simple problems, and believing vendor hype. Most failures trace back to bad data or misplaced trust, not bad algorithms.

**Does AI really hallucinate in brewing work?**
Yes. Generative AI will produce precise, authoritative, and completely wrong figures — recipe numbers, regulatory rules, tasting descriptions. If you don't verify every output, it will eventually burn you.

**How do you avoid getting burned by AI?**
Verify every number against real records, prefer the simplest tool that works, be ruthless about data quality, and never let a confident output replace your own judgment.
