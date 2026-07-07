---
layout: post
title: "Vibe-Coding a Fermentation Tracker: A Brewer's Build Log"
image: /assets/og/vibe-coding-fermentation-dashboard-build-log.png
description: "A concrete, step-by-step build log of vibe-coding a small fermentation tracker with Claude Fable 5 — the actual prompts, the verify steps, the bug it introduced and how it got caught, so you can copy the loop for your own brewery tool."
date: 2026-06-12 11:20:00 -0700
updated: 2026-06-12
tags: [brewing-science, vibe-coding-brewers, vibe-coding, claude, building-with-ai]
faq:
  - q: "How do you vibe-code a brewery tool step by step?"
    a: "Start with the smallest useful version and one clear instruction: describe the tool, let Claude build it, then immediately verify the output against a batch whose numbers you already know. Add one feature at a time, verifying after each. Keep a known-answer test case handy so every change is checked against reality before you trust it."
  - q: "What prompts work best for building a tool with Claude?"
    a: "Specific, scoped, one step at a time. 'Build a page where I enter OG and FG and it shows ABV and apparent attenuation' beats 'build me a brewery app.' State the formula you expect or ask it to show the formula it used so you can check it. After each build, give it a concrete test case and the expected answer to verify against."
  - q: "What goes wrong when vibe-coding a brewing tool?"
    a: "The most common failure is a plausible-but-wrong formula or unit — an ABV calculation using the wrong constant, gravity in the wrong scale, an edge case (stuck or zero readings) unhandled. These pass casual inspection because the tool runs and the numbers look reasonable. They're caught only by checking against a batch whose real answer you already know."
---

**Short answer: here's an actual build log of vibe-coding a small fermentation tracker with Claude Fable 5 — the prompts, the verification, and the one real bug it introduced (a wrong ABV constant) and exactly how a known-answer check caught it. The pattern you should copy: smallest useful version first, one feature at a time, and after every single change, verify the output against a batch whose numbers you already know. The loop is boring and that's the point — boring is what makes a vibe-coded tool trustworthy.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 300" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A four-step build log: step one a minimal ABV tool verified against a known batch, step two add attenuation verified, step three add a stall flag verified on an edge case, step four a gravity chart, each step gated by a known-answer check."><rect width="1000" height="300" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">BUILD LOG — ONE VERIFIED FEATURE AT A TIME</text><g font-family="sans-serif" font-size="10.5"><rect x="40" y="70" width="210" height="150" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="145" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Step 1 &#183; ABV</text><text x="145" y="120" text-anchor="middle" fill="#4a6b64">enter OG, FG &#8594; ABV</text><text x="145" y="150" text-anchor="middle" font-size="9.5" fill="#06483f" font-weight="700">VERIFY</text><text x="145" y="168" text-anchor="middle" fill="#4a6b64">1.050&#8594;1.010 = 5.25%?</text><rect x="270" y="70" width="210" height="150" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="375" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Step 2 &#183; Attenuation</text><text x="375" y="120" text-anchor="middle" fill="#4a6b64">add apparent atten. %</text><text x="375" y="150" text-anchor="middle" font-size="9.5" fill="#06483f" font-weight="700">VERIFY</text><text x="375" y="168" text-anchor="middle" fill="#4a6b64">should read ~80%</text><rect x="500" y="70" width="210" height="150" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="605" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Step 3 &#183; Stall flag</text><text x="605" y="120" text-anchor="middle" fill="#4a6b64">warn if gravity flat</text><text x="605" y="150" text-anchor="middle" font-size="9.5" fill="#06483f" font-weight="700">VERIFY</text><text x="605" y="168" text-anchor="middle" fill="#4a6b64">test a stuck batch</text><rect x="730" y="70" width="230" height="150" rx="9" fill="#06483f"/><text x="845" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">Step 4 &#183; Chart</text><text x="845" y="120" text-anchor="middle" fill="#cfe6df">plot the gravity curve</text><text x="845" y="150" text-anchor="middle" font-size="9.5" fill="#f0f6f5" font-weight="700">VERIFY</text><text x="845" y="168" text-anchor="middle" fill="#cfe6df">curve matches the log</text><g stroke="#00695c" stroke-width="2" fill="#00695c"><line x1="250" y1="145" x2="264" y2="145"/><polygon points="264,140 273,145 264,150" stroke="none"/><line x1="480" y1="145" x2="494" y2="145"/><polygon points="494,140 503,145 494,150" stroke="none"/><line x1="710" y1="145" x2="724" y2="145"/><polygon points="724,140 733,145 724,150" stroke="none"/></g></g><text x="500" y="258" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#00695c">No feature is "done" until it passes a known-answer check.</text><text x="500" y="280" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#4a6b64">this is how the wrong-ABV-constant bug got caught at step 1, before it could matter</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The gate between every step is a batch whose real numbers you already know — that gate is the entire method.</figcaption>
</figure>

This is the hands-on post of the vibe-coding-for-brewers set, after [vibe-coding a brewing tool with Fable 5]({{ '/2026/vibe-coding-brewing-tool-claude-fable-5/' | relative_url }}) and [what Fable 5 changes]({{ '/2026/claude-fable-5-for-brewers-who-build/' | relative_url }}). No theory — an actual build log you can copy, including the bug, because the bug is the most instructive part.

## The goal and the setup

The tool: a small **fermentation tracker** — enter a batch's gravity readings over time, see the curve, get ABV and attenuation, and a flag if fermentation looks stalled. The setup: **Claude Code** in the terminal with **Fable 5**, and — this is the only real prerequisite — one batch from my records whose numbers I already know cold, to check everything against. Call it the *known-answer batch*: OG 1.050, FG 1.010, which I know is 5.25% ABV and roughly 80% apparent attenuation.

## Step 1 — the smallest useful version

The first prompt was deliberately tiny:

> *"Build a simple single-page tool where I enter original gravity and final gravity, and it shows ABV and apparent attenuation. Show me the formula you used for each."*

Asking it to *show the formula* is the trick — it turns verification from guesswork into a glance. Fable 5 built the page and printed its formulas. ABV looked right; attenuation looked right. Then the non-negotiable step: I entered my known-answer batch. Attenuation read ~80% — correct. ABV read **5.1%**, not 5.25%.

## Step 2 — catching the bug

A 5.1 vs 5.25 gap is small enough to shrug past, which is exactly why it's dangerous. I didn't shrug; I checked the formula it had printed. It had used `ABV = (OG − FG) × 131.25` but with a rounded gravity-points approach that dropped precision — a plausible, common, *slightly wrong* implementation. I told it:

> *"Your ABV is reading 5.1% for OG 1.050, FG 1.010, but it should be about 5.25%. Check the formula and fix it."*

Fable 5 found its own error, corrected the calculation, and ABV then read 5.25%. This is the loop working as designed: the model produced confident, runnable, *slightly wrong* code, and a known-answer check — not a code review — caught it. A brewer who didn't know the right answer would have shipped 5.1%.

## Steps 3 and 4 — grow one verified feature at a time

With ABV trustworthy, I added features one at a time, verifying after each:

- **A stall flag** — *"add a warning if the last three gravity readings are within 2 points of each other."* Verified by feeding it a deliberately stuck batch and confirming the warning fired, and a healthy one and confirming it didn't.
- **A gravity chart** — *"plot the readings over time as a line chart."* Verified by eye against the actual log curve.

Each step was small, each was checked, and because the foundation (ABV) was already verified, a later bug could only be in the new feature — which makes bugs easy to locate. That discipline — small steps, known-answer gate — is the whole method, and it's the same [build–verify–fix loop]({{ '/2026/vibe-code-a-product-with-claude/' | relative_url }}) the general post describes, just applied to beer.

## Where this breaks

The honest section. **My known-answer batch only tests what it covers** — it caught the ABV bug because ABV was in it; a tool feature with no known-answer case is effectively unverified, so build test cases for each. **Small wrong numbers are the real danger** — a wildly wrong output gets noticed; a 5.1-vs-5.25 error sails through casual use and into a spec sheet, which is why you check against exact known values, not "looks about right." **It worked in an evening because the scope was tiny** — a single-purpose tracker, not brewery software; the method holds but the timeline doesn't scale to ambitious scope. And **this is a personal tool, not validated infrastructure** — fine for tracking your own ferments; anything feeding compliance, labels or money needs far more checking and a human owning the output.

## The bottom line

Vibe-coding a real brewery tool with Fable 5 is a boring, repeatable loop: smallest useful version, ask the model to show its formulas, verify against a batch whose numbers you know, then add one feature at a time with a check after each. The headline of this build wasn't that Fable 5 wrote the tool — it was that a known-answer check caught a confident, slightly-wrong ABV formula before it could matter. Copy that loop and you can build genuinely useful tools; the model does the typing, and your brewer's knowledge of what the numbers *should* be does the part that counts. Start at [the overview]({{ '/2026/vibe-coding-brewing-tool-claude-fable-5/' | relative_url }}) if you skipped it.

## Frequently asked questions

**How do you vibe-code a brewery tool step by step?**
Start with the smallest useful version and one clear instruction: describe the tool, let Claude build it, then immediately verify the output against a batch whose numbers you already know. Add one feature at a time, verifying after each. Keep a known-answer test case handy so every change is checked against reality before you trust it.

**What prompts work best for building a tool with Claude?**
Specific, scoped, one step at a time. "Build a page where I enter OG and FG and it shows ABV and apparent attenuation" beats "build me a brewery app." State the formula you expect or ask it to show the formula it used so you can check it. After each build, give it a concrete test case and the expected answer to verify against.

**What goes wrong when vibe-coding a brewing tool?**
The most common failure is a plausible-but-wrong formula or unit — an ABV calculation using the wrong constant, gravity in the wrong scale, an edge case (stuck or zero readings) unhandled. These pass casual inspection because the tool runs and the numbers look reasonable. They're caught only by checking against a batch whose real answer you already know.
