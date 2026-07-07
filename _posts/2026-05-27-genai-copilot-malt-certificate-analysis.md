---
layout: post
title: "A Generative-AI Copilot for Reading Malt Certificates of Analysis"
image: /assets/og/genai-copilot-malt-certificate-analysis.png
description: "A grounded LLM copilot can read a malt certificate of analysis, explain every parameter, flag out-of-spec values against your recipe and draft the brew sheet — if you stop it inventing numbers."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
tags: [brewing-science, malting, generative-ai, data-science]
faq:
  - q: "What is on a malt certificate of analysis?"
    a: "A malt certificate reports moisture, extract (fine and coarse), the fine–coarse difference, colour in EBC, diastatic power in °WK, the Kolbach index (soluble-to-total protein), free amino nitrogen, beta-glucan, viscosity, friability and homogeneity. Together they describe how the malt will mill, convert in the mash and ferment."
  - q: "Can a large language model read a malt certificate of analysis?"
    a: "Yes, if it is grounded. With the certificate's numbers extracted into structured fields, an LLM can explain each parameter, compare a lot against your spec and past lots, and draft the malt section of a brew sheet. Left ungrounded it will invent plausible-looking values, so the numbers must come from extraction, not from the model."
  - q: "What is the Kolbach index?"
    a: "The Kolbach index is the ratio of soluble protein to total protein in malt, a measure of protein modification. Roughly 35–45% is well modified; lower suggests under-modification and higher suggests over-modification with more free amino nitrogen. It helps predict foam, body and fermentation behaviour."
---

**Short answer: yes — a generative-AI copilot is genuinely good at malt certificates, on one condition: it must read the real numbers, not guess them. Extract the certificate's values into structured fields first, and an LLM can then explain every parameter in plain language, compare the lot against your recipe spec and your last deliveries, flag anything out of range, and draft the malt section of the brew sheet. Skip the extraction step and the model will confidently invent a Kolbach index that was never on the page. The discipline is grounding; the payoff is turning a dense PDF into a decision in seconds.**

A malt certificate is a wall of numbers that a brewer learns to read by experience. New brewers find it opaque, and even experienced ones rarely have time to compare today's lot against the trend. This is exactly the kind of dense, structured-but-jargon-heavy document that generative AI handles well — provided you build it to stay honest.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 220" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Pipeline from a malt certificate PDF through extraction and grounding to explanation, flagging, drafting, and human sign-off">
<rect x="0" y="0" width="760" height="220" fill="#ffffff"/>
<text x="380" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#06483f">Grounded copilot — extract first, generate second</text>
<rect x="20" y="80" width="120" height="60" rx="6" fill="#f0f6f5" stroke="#4a6b64"/>
<text x="80" y="106" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#06483f">COA</text>
<text x="80" y="124" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#4a6b64">PDF / scan</text>
<rect x="175" y="80" width="120" height="60" rx="6" fill="#f0f6f5" stroke="#4a6b64"/>
<text x="235" y="106" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#06483f">extract</text>
<text x="235" y="124" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#4a6b64">structured fields</text>
<rect x="330" y="80" width="120" height="60" rx="6" fill="#00695c"/>
<text x="390" y="106" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="#ffffff">ground</text>
<text x="390" y="124" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#ffffff">spec + past lots</text>
<rect x="485" y="80" width="120" height="60" rx="6" fill="#f0f6f5" stroke="#4a6b64"/>
<text x="545" y="100" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#06483f">explain ·</text>
<text x="545" y="116" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#06483f">flag · draft</text>
<rect x="640" y="80" width="100" height="60" rx="6" fill="#2e9e7c" fill-opacity="0.18" stroke="#2e9e7c"/>
<text x="690" y="106" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#06483f">human</text>
<text x="690" y="124" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#4a6b64">sign-off</text>
<g stroke="#4a6b64" stroke-width="2" fill="#4a6b64">
<line x1="140" y1="110" x2="170" y2="110"/><polygon points="175,110 167,106 167,114"/>
<line x1="295" y1="110" x2="325" y2="110"/><polygon points="330,110 322,106 322,114"/>
<line x1="450" y1="110" x2="480" y2="110"/><polygon points="485,110 477,106 477,114"/>
<line x1="605" y1="110" x2="635" y2="110"/><polygon points="640,110 632,106 632,114"/>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The model only ever speaks about numbers that were extracted from the certificate and checked against your spec. It explains and drafts; the brewer signs off.</figcaption>
</figure>

## What the certificate actually tells you

A malt certificate is a compact prediction of how the malt will behave. Moisture and extract (fine and coarse) set how much sugar you get per kilogram; the **fine–coarse difference** hints at modification. Colour (EBC) sets the beer's hue; **diastatic power** (°WK) says whether there is enough enzyme to convert the mash, which matters the moment you add unmalted adjuncts. The **Kolbach index** — soluble to total protein — reports protein modification and, with **free amino nitrogen (FAN)**, predicts foam, body and how happily the yeast will ferment. Beta-glucan and viscosity warn of [slow runoff]({{ '/2026/predicting-beta-glucan-slow-runoff-malt/' | relative_url }}); friability and homogeneity round out the modification picture. None of these is hard alone — the work is reading all of them together, against your recipe, every delivery.

## Grounding the model so it stops inventing numbers

This is the entire engineering problem, so be explicit about it. A language model asked to "read this certificate" from a raw image will hallucinate — it pattern-matches to a plausible certificate, not yours. The fix is a two-step pipeline: first **extract** the values into structured fields (OCR or a vision model for scans, a parser for PDFs, with a validation check that flags low-confidence reads), then hand the model *only the extracted numbers plus your spec* and ask it to explain and compare. That is also where the machine-learning and data-science value sits — retrieval over your historic certificates and brews so the copilot can say "this is the lowest diastatic power you've taken in a year." The generation is the easy, visible part; the grounding is what makes it trustworthy.

## From explanation to drafting

Grounded, the copilot becomes a working tool. It explains each parameter to a new brewer ("Kolbach of 38% means well-modified — expect easy conversion and good FAN"). It flags out-of-spec values against your recipe and proposes the response — a protein rest, a diastatic-power top-up with enzyme or a high-DP base malt, a beta-glucanase rest. It compares the lot to your trend and drafts the malt section of the brew sheet or a supplier query. This is the same grounded-copilot pattern as [using Claude and Claude Code in a brewery]({{ '/2026/claude-ai-claude-code-for-breweries/' | relative_url }}): the model drafts, a person approves.

## Where it breaks

The headline risk is the one above: an ungrounded model invents numbers, and a fabricated diastatic power on a brew sheet is worse than no copilot at all — so never let it read a certificate without the extraction-and-validation step, and surface the extracted values for a human to eyeball. Extraction itself fails on messy scans, unusual lab layouts or unit mix-ups (°WK vs °L, EBC vs SRM), so the pipeline must flag low-confidence fields rather than guess. And a certificate, however well read, is still a [lot average that can hide a bad fraction]({{ '/2026/predicting-malt-modification-germination/' | relative_url }}) — the copilot reads what is on the page, not what the page missed. It is an assistant for a spec decision, not the decision-maker; the brewer signs off.

## The bottom line

A generative-AI copilot is one of the most immediately useful AI tools in a brewery — it makes a malt certificate legible, comparable and actionable in seconds. The whole trick is grounding: extract and validate the real numbers first, retrieve your own history, and let the model explain, flag and draft on top. Build it that way and it saves real time on every delivery; build it lazily and it will lie to you with great confidence.

## Frequently asked questions

**What is on a malt certificate of analysis?**
A malt certificate reports moisture, extract (fine and coarse), the fine–coarse difference, colour in EBC, diastatic power in °WK, the Kolbach index (soluble-to-total protein), free amino nitrogen, beta-glucan, viscosity, friability and homogeneity. Together they describe how the malt will mill, convert in the mash and ferment.

**Can a large language model read a malt certificate of analysis?**
Yes, if it is grounded. With the certificate's numbers extracted into structured fields, an LLM can explain each parameter, compare a lot against your spec and past lots, and draft the malt section of a brew sheet. Left ungrounded it will invent plausible-looking values, so the numbers must come from extraction, not from the model.

**What is the Kolbach index?**
The Kolbach index is the ratio of soluble protein to total protein in malt, a measure of protein modification. Roughly 35–45% is well modified; lower suggests under-modification and higher suggests over-modification with more free amino nitrogen. It helps predict foam, body and fermentation behaviour.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
