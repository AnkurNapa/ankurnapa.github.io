---
layout: post
title: "A Brewer's Step-by-Step Roadmap into AI (with Free Resources)"
image: /assets/og/brewer-ai-roadmap-step-by-step.png
description: "A practical, five-stage learning path for a working brewer who wants to get into AI — data literacy, spreadsheets to Power BI, Python, machine learning and generative AI — built entirely on free, open resources like Microsoft Learn, Kaggle and Google's PAIR guidebook."
date: 2026-06-13 10:00:00 -0700
updated: 2026-06-13
tags: [brewing-science, brewer-ai-roadmap, learning, ai-tools, generative-ai]
faq:
  - q: "How can a brewer start learning AI?"
    a: "Follow the data, not the hype. The path has five stages: (0) get your data into shape, (1) data literacy and spreadsheets to Power BI, (2) Python basics, (3) machine learning and a first model on brewing data, (4) generative and human-centred AI. Each stage has free, open resources — Microsoft Learn, Kaggle Learn, Google's Machine Learning Crash Course and the PAIR People + AI Guidebook — so the only cost is your time."
  - q: "Do I need to be good at maths or coding to learn AI as a brewer?"
    a: "Less than you think to start. Brewers already do applied statistics — attenuation, IBU, efficiency, control charts — which is the hard intuition. The early stages need spreadsheet skill and curiosity, not calculus. Coding (Python) comes at stage 2 and is learnable in evenings; the maths you need for practical machine learning is mostly conceptual, and the free courses teach it as you go."
  - q: "How long does it take a brewer to get into AI?"
    a: "To be genuinely useful — reading data, building a dashboard, running a simple model — a few months of consistent evenings, not years. The roadmap is deliberately staged so each step produces something usable on the brewery floor, so you are getting value long before you reach generative AI. Depth takes longer, but the journey pays from the first stage."
---

**Short answer: a brewer gets into AI by following the data, not the hype, through five staged steps — (0) get your data into shape, (1) data literacy and spreadsheets-to-Power-BI, (2) Python, (3) machine learning and a first model on your own brewing data, (4) generative and human-centred AI. Every step has a free, open resource behind it — Microsoft Learn, Kaggle Learn, Google's Machine Learning Crash Course, the PAIR People + AI Guidebook — so the only thing it costs is consistent evenings. And you already own the hardest part: a brewer's intuition for process, measurement and what a number means.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A brewer's five-stage AI learning roadmap: stage zero get data in shape, stage one data literacy and Power BI, stage two Python, stage three machine learning and a first model, stage four generative and human-centred AI, each a rising step with a free resource."><rect width="1000" height="340" fill="#fdfbf7"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">THE BREWER'S AI ROADMAP — ALL FREE RESOURCES</text><g font-family="sans-serif"><rect x="24" y="252" width="178" height="66" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="113" y="276" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">0 &#183; Your data</text><text x="113" y="294" text-anchor="middle" font-size="10" fill="#1c1a17">measure &amp; collect</text><text x="113" y="310" text-anchor="middle" font-size="9" fill="#6b6258">brewery records</text><rect x="214" y="208" width="178" height="110" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="303" y="232" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">1 &#183; Data literacy</text><text x="303" y="250" text-anchor="middle" font-size="10" fill="#1c1a17">Excel &#8594; Power BI</text><text x="303" y="266" text-anchor="middle" font-size="9" fill="#6b6258">Microsoft Learn</text><rect x="404" y="164" width="178" height="154" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="493" y="188" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">2 &#183; Python</text><text x="493" y="206" text-anchor="middle" font-size="10" fill="#1c1a17">the language of data</text><text x="493" y="222" text-anchor="middle" font-size="9" fill="#6b6258">freeCodeCamp &#183; Kaggle</text><rect x="594" y="120" width="178" height="198" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="683" y="144" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">3 &#183; Machine learning</text><text x="683" y="162" text-anchor="middle" font-size="10" fill="#1c1a17">your first model</text><text x="683" y="178" text-anchor="middle" font-size="9" fill="#6b6258">Google ML Crash Course</text><rect x="784" y="76" width="192" height="242" rx="8" fill="#7a1f3d"/><text x="880" y="100" text-anchor="middle" font-size="12" font-weight="700" fill="#fdfbf7">4 &#183; Generative + human AI</text><text x="880" y="118" text-anchor="middle" font-size="10" fill="#f7ece0">build with &amp; for people</text><text x="880" y="134" text-anchor="middle" font-size="9" fill="#f1e0d2">PAIR Guidebook</text></g><line x1="18" y1="330" x2="980" y2="330" stroke="#6b6258" stroke-width="1.5"/><text x="24" y="349" font-family="sans-serif" font-size="11" fill="#6b6258">start here — each step is usable on the floor</text><text x="972" y="349" text-anchor="end" font-family="sans-serif" font-size="11" fill="#6b6258">value compounds →</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Each step produces something useful in the brewery, so you are getting value long before the journey ends.</figcaption>
</figure>

This opens a four-part series: a **practical roadmap** for a brewer who wants into AI and doesn't know where to start. It's deliberately different from my [personal story of that journey]({{ '/series/brewer-to-ai/' | relative_url }}) — this is the *map and the reading list*, every resource free and open, so you can actually walk it. Part two covers [the foundations — data and Python]({{ '/2026/brewer-ai-foundations-data-python-free-resources/' | relative_url }}); part three, [your first machine-learning model]({{ '/2026/brewer-first-machine-learning-model-free-courses/' | relative_url }}); part four, [generative and human-centred AI]({{ '/2026/brewer-generative-human-centered-ai-pair-guidebook/' | relative_url }}).

## You already own the hardest part

Here's the thing nobody tells a brewer eyeing AI: you are not starting from zero. You calculate attenuation, hop utilisation, extract efficiency and IBU; you read control charts; you know a measurement from an estimate and a real trend from noise on the gauge. That *applied-statistics intuition* — knowing what a number means and when to distrust it — is the genuinely hard part of data work, and it takes most computer-science graduates years to acquire on a factory floor. You got it standing at the mash tun. What's missing is tooling and vocabulary, and tooling is learnable. Hold onto that: the gap is smaller than the hype makes it look.

## The five stages, in order

**Stage 0 — Get your data into shape.** Before any course, the rule that runs through this whole blog: AI sits on measured data. If your brew logs live in a notebook and three spreadsheets, the first project is simply getting them into one clean, consistent place. This is [collecting your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}), and it's stage zero because nothing above it works without it.

**Stage 1 — Data literacy: spreadsheets to Power BI.** Learn to *see* your data clearly before you try to predict from it — pivot tables, then a real dashboard. This is the highest-value, lowest-pain stage and it pays back immediately.

**Stage 2 — Python.** The lingua franca of data and AI. You do not need to become a software engineer; you need enough to load a spreadsheet, clean it, and plot it. Evenings, not years.

**Stage 3 — Machine learning.** The concepts, then a first model on a brewing question you actually care about — predicting attenuation, flagging a stuck-fermentation risk. Small, real, yours.

**Stage 4 — Generative and human-centred AI.** The chatbot kind — how to use it well, and crucially how to *build* with it responsibly, using Google's PAIR People + AI Guidebook so what you make is something a brewer would actually trust.

## The free toolkit at a glance

You can walk this entire path without paying for a course. The anchors:

| Stage | Resource | Cost |
|-------|----------|------|
| 1 | [Microsoft Learn](https://learn.microsoft.com/training/) — Power BI, data fundamentals (DP-900) | Free |
| 2 | [freeCodeCamp](https://www.freecodecamp.org/learn) and [Kaggle Learn](https://www.kaggle.com/learn) — Python, Pandas | Free |
| 3 | [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) and Kaggle Learn | Free |
| 3 | [Elements of AI](https://www.elementsofai.com/) — concepts, no code | Free |
| 4 | [Microsoft Learn AI fundamentals (AI-900)](https://learn.microsoft.com/training/) and responsible AI | Free |
| 4 | [Google PAIR People + AI Guidebook](https://pair.withgoogle.com/guidebook/) and its [workshop](https://pair.withgoogle.com/guidebook-v2/workshop) | Free |

Certifications (DP-900, PL-300, AI-900) are optional — the *learning* is free; only the exam costs money, and the badge matters far less than a working dashboard you built on your own brewery's data.

## How to actually stick with it

The roadmap fails the same way diets do — abandoned in week three — so build it like a brewing schedule, not a binge. **One stage at a time, finished before the next.** **A real brewery question as the spine** — you'll push through a dry Pandas lesson to answer "why did batch 412 finish high" in a way you never will for a toy dataset. **Ship something small at every stage** — a pivot table, a dashboard, a one-feature model — because momentum comes from use, not from completion certificates. And **two or three evenings a week, consistently**, beats a heroic weekend that never repeats.

## Where this breaks

Honesty is the house rule. **Free does not mean fast or frictionless** — open resources assume some self-direction, and you will hit a confusing week with no instructor to ask; the fix is a brewing question stubborn enough to pull you through it. **The path looks linear and isn't** — you'll loop back to data cleaning forever, because real data is messy and stage 0 never fully ends. **Certifications can become a trap** — collecting badges feels like progress while building nothing; the portfolio that gets a brewer a data role is *projects on real beer data*, not a wall of certificates. And **some of this won't stick, and that's fine** — you don't need all five stages to extract value; a brewer who only ever reaches a confident Power BI dashboard has already changed how their brewery runs.

## The bottom line

The route from the brewhouse to AI is a staircase with free resources on every step: get your data straight, learn to see it (Power BI), learn the language (Python), learn to predict (machine learning), then learn to build with generative AI responsibly (PAIR). You bring the rarest ingredient already — the process intuition to know what the numbers mean. Everything else is a free course and a few stubborn evenings. Next: [the foundations]({{ '/2026/brewer-ai-foundations-data-python-free-resources/' | relative_url }}) — data literacy and Python, with the exact Microsoft Learn and Kaggle paths to follow.

## Frequently asked questions

**How can a brewer start learning AI?**
Follow the data, not the hype. The path has five stages: (0) get your data into shape, (1) data literacy and spreadsheets to Power BI, (2) Python basics, (3) machine learning and a first model on brewing data, (4) generative and human-centred AI. Each stage has free, open resources — Microsoft Learn, Kaggle Learn, Google's Machine Learning Crash Course and the PAIR People + AI Guidebook — so the only cost is your time.

**Do I need to be good at maths or coding to learn AI as a brewer?**
Less than you think to start. Brewers already do applied statistics — attenuation, IBU, efficiency, control charts — which is the hard intuition. The early stages need spreadsheet skill and curiosity, not calculus. Coding (Python) comes at stage 2 and is learnable in evenings; the maths you need for practical machine learning is mostly conceptual, and the free courses teach it as you go.

**How long does it take a brewer to get into AI?**
To be genuinely useful — reading data, building a dashboard, running a simple model — a few months of consistent evenings, not years. The roadmap is staged so each step produces something usable on the brewery floor, so you are getting value long before you reach generative AI. Depth takes longer, but the journey pays from the first stage.
