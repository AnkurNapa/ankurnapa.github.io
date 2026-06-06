---
layout: post
title: "You Don't Have an AI Problem, You Have a Question Problem"
image: /assets/og/ai-question-problem-new-brewers.png
description: "Why new brewers get generic mush from AI: the missing skill isn't prompt engineering, it's question literacy — knowing what is knowable about your beer and your process."
date: 2026-06-06
updated: 2026-06-06
tags: [brewing-science, asking-better-questions, ai-tools, generative-ai, beginners]
faq:
  - q: "Why do I get generic answers when I ask AI about my brewing?"
    a: "Because the question is generic. 'How do I make my beer better?' contains no gravity readings, no temperatures, no timeline and no symptom — so the model can only return textbook averages. Specific inputs are what unlock specific answers."
  - q: "What makes a good AI question for a brewer?"
    a: "A good question names the beer style, the process stage, the measured numbers (OG, FG, temperatures, times, pitch rate) and the specific symptom or decision. It asks about one thing, and it gives the model something real to reason over."
  - q: "Do new brewers need to learn prompt engineering?"
    a: "Not really. They need to learn their own process first — what to measure, what normal looks like, and what can go wrong at each stage. Once you can describe a problem precisely, the prompt almost writes itself."
---

**Short answer: when a new brewer asks AI "how do I make my beer better?" and gets a vague answer, the failure isn't the model — it's the question. A language model can only reason over what you give it, and a question with no numbers, no stage and no symptom gives it nothing. The skill that separates a useful AI session from a useless one isn't prompt engineering; it's question literacy — knowing your process well enough to describe one specific, measurable problem at a time.** This post is the first in a series on building exactly that skill.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 300" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Anatomy of a useful brewing question: a vague ask contains nothing to reason over, while a good ask combines a process stage, a measurement and a decision."><rect width="1000" height="300" fill="#fdfbf7"/><text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">ANATOMY OF A USEFUL BREWING QUESTION</text><rect x="40" y="55" width="400" height="90" rx="10" fill="#f7ece0" stroke="#6b6258" stroke-width="1.3"/><text x="240" y="88" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#6b6258">"Why does my beer taste off?"</text><text x="240" y="115" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#6b6258">no stage &#183; no numbers &#183; no decision</text><text x="240" y="133" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="#6b6258">&#8594; textbook averages back</text><rect x="40" y="170" width="400" height="100" rx="10" fill="#7a1f3d" opacity="0.08"/><rect x="40" y="170" width="400" height="100" rx="10" fill="none" stroke="#7a1f3d" stroke-width="1.5"/><text x="240" y="200" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#7a1f3d">"Lager stuck at 4.2&#176;P, 11&#176;C,</text><text x="240" y="220" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#7a1f3d">pitched 12M cells/mL &#8212; rank the causes"</text><text x="240" y="248" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#7a1f3d">stage + numbers + decision &#8594; a real answer</text><g font-family="sans-serif"><rect x="520" y="70" width="440" height="54" rx="8" fill="#fdfbf7" stroke="#b45309" stroke-width="1.5"/><text x="740" y="92" text-anchor="middle" font-size="13" font-weight="700" fill="#1c1a17">A STAGE</text><text x="740" y="111" text-anchor="middle" font-size="10.5" fill="#6b6258">mash &#183; boil &#183; fermentation &#183; conditioning &#183; packaging</text><rect x="520" y="138" width="440" height="54" rx="8" fill="#fdfbf7" stroke="#b45309" stroke-width="1.5"/><text x="740" y="160" text-anchor="middle" font-size="13" font-weight="700" fill="#1c1a17">A MEASUREMENT</text><text x="740" y="179" text-anchor="middle" font-size="10.5" fill="#6b6258">OG / FG &#183; temperature &#183; pH &#183; pitch rate &#183; time</text><rect x="520" y="206" width="440" height="54" rx="8" fill="#fdfbf7" stroke="#b45309" stroke-width="1.5"/><text x="740" y="228" text-anchor="middle" font-size="13" font-weight="700" fill="#1c1a17">A DECISION</text><text x="740" y="247" text-anchor="middle" font-size="10.5" fill="#6b6258">what will you do differently with the answer?</text></g><g stroke="#b45309" stroke-width="2" fill="#b45309"><line x1="460" y1="220" x2="505" y2="220"/><polygon points="505,215 514,220 505,225" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A vague ask gives the model nothing; a good ask binds a stage, a measurement and a decision into one question.</figcaption>
</figure>

## The question gap is an experience gap

Ask a brewer with twenty years in the cellar what they'd put to an AI assistant and you get something like: *"My lager is stuck at 4.2°P after a strong start, fermentation at 11°C, pitched at 12 million cells/mL — what are the likely causes and in what order should I rule them out?"* Ask a first-year brewer and you usually get: *"Why does my beer taste off?"*

Both brewers have the same model available. Only one gets a useful answer. The difference isn't typing skill — it's that the experienced brewer already carries a mental map of the process: what happens at mashing, what attenuation should look like, which faults map to which stage. The question encodes that map. The beginner's question can't encode a map they don't yet have.

That's the honest, slightly uncomfortable truth about generative AI in brewing: **it amplifies expertise, it doesn't substitute for it.** The same pattern shows up in [what AI actually means for a brewer]({{ '/2026/what-ai-means-for-a-brewer/' | relative_url }}) — the tool is only as sharp as the process understanding behind it.

## What "knowable" looks like in a brewery

Question literacy starts with knowing what is even answerable. A useful brewing question lives at the intersection of three things:

- **A stage** — mashing, lautering, boil, fermentation, conditioning, packaging. Faults have addresses. Diacetyl points at fermentation and maturation; astringency points at sparging and pH; oxidation points at transfers and packaging.
- **A measurement** — original and final gravity, mash and fermentation temperatures, pH, pitch rate, times. Numbers turn "tastes off" into "finished at 1.020 when the recipe predicted 1.012", which is a question a model can actually work on.
- **A decision** — what will you *do* with the answer? "Should I extend the diacetyl rest or repitch?" is a question. "Tell me about diacetyl" is a Wikipedia request.

From a data-science angle this is the oldest rule in the book: **measure first, model second.** If you don't record gravities and temperatures, no model — statistical or generative — has anything to reason over. (If that's where you are, start with [collecting your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}) — it's the unglamorous prerequisite for everything in this series.)

## The same gap exists beyond chatbots

This isn't only a generative-AI problem. Classic machine learning hits the identical wall: a demand-forecasting model or a fermentation-prediction model is framed by a question — *predict what, from what, to decide what?* A brewery that can't say "we want to predict final gravity at 48 hours from pitch temperature, pitch rate and original gravity, so we can schedule tank turns" doesn't have a modelling problem, it has a framing problem. The model class barely matters; the question is the design.

Generative AI just makes the gap more visible, because the feedback is instant. Ask a fuzzy question, get fuzzy prose, blame the tool.

## Where this breaks

Two honest limits. First, **a perfectly framed question can still get a confidently wrong answer** — models state hop alpha-acid figures and yeast attenuation ranges from memory, and memory drifts; verification is its own skill, covered later in this series. Second, **question literacy can't be fully outsourced**. AI can help you find the questions you're missing — that's the next post — but the judgement about which answer to act on in *your* cellar, with *your* beer, stays with you. The palate and the hydrometer remain the court of appeal.

## The bottom line

New brewers don't need a better model; they need a better map of their own process, because the map is what good questions are made of. Learn the stages, measure the basics, ask about one specific thing with real numbers attached — and AI turns from a vague oracle into a fast, well-read colleague. The rest of this series builds that skill deliberately: using AI to surface the questions you don't know yet, mapping what your data can answer, rewriting bad prompts into good ones, and learning to catch the confident wrong answer.

## Frequently asked questions

**Why do I get generic answers when I ask AI about my brewing?**
Because the question is generic. "How do I make my beer better?" contains no gravity readings, no temperatures, no timeline and no symptom — so the model can only return textbook averages. Specific inputs are what unlock specific answers.

**What makes a good AI question for a brewer?**
A good question names the beer style, the process stage, the measured numbers (OG, FG, temperatures, times, pitch rate) and the specific symptom or decision. It asks about one thing, and it gives the model something real to reason over.

**Do new brewers need to learn prompt engineering?**
Not really. They need to learn their own process first — what to measure, what normal looks like, and what can go wrong at each stage. Once you can describe a problem precisely, the prompt almost writes itself.

*Part of the [Brewing Science]({{ '/tracks/brewing-science/' | relative_url }}) track.*
