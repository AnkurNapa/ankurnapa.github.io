---
layout: post
title: "Using AI to Time the Diacetyl Rest"
image: /assets/og/ai-diacetyl-rest-timing.png
description: "Predict when to start and end the diacetyl rest to drive VDKs below 0.10 mg/L without wasting tank time, using gravity, temperature and yeast state."
date: 2023-08-25
updated: 2023-08-25
tags: [brewing-science, fermentation, flavor]
faq:
  - q: "What is a diacetyl rest?"
    a: "It is raising fermentation temperature, usually about two-thirds of the way through, to speed yeast reuptake and reduction of diacetyl and other VDKs to flavourless compounds before you cool and package."
  - q: "What diacetyl level should I target?"
    a: "Below the flavour threshold of roughly 0.10 mg/L for diacetyl (butterscotch). The related compound 2,3-pentanedione has a higher threshold near 1 mg/L."
  - q: "Why does diacetyl come back or stay high?"
    a: "Premature flocculation drops yeast out before it finishes reuptake, leaving residual VDK. Pediococcus contamination also produces diacetyl, which a rest will not fix."
---

**Short answer: a model can call the start and end of the diacetyl rest from gravity, temperature, VDK readings and yeast state, so you clear butterscotch without parking the tank for days "to be safe".** Tank time is money, and most rests are timed by habit.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Using AI to Time the Diacetyl Rest</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## The chemistry you are timing
Diacetyl (2,3-butanedione) is the classic butterscotch off-flavour, with a threshold around 0.10 mg/L. The path matters because it sets what you can control. During growth, yeast excretes alpha-acetolactate. Outside the cell, that compound undergoes spontaneous oxidative decarboxylation to diacetyl. This step is non-enzymic and rate-limiting, which is why diacetyl can appear *after* the yeast has done its main work. The yeast then reuptakes diacetyl and reduces it to acetoin and on to flavourless 2,3-butanediol.

The diacetyl rest exploits the last step: raise temperature roughly two-thirds through fermentation and the yeast clears VDKs faster. Time it wrong and you either cool too early, trapping alpha-acetolactate that converts later in the package, or you hold warm needlessly and lose throughput.

## What the model watches
This is a measure-first problem. The useful signals are:

- **Gravity trajectory** and its slope, to locate the two-thirds point in real time rather than by recipe estimate.
- **Temperature** history of the actual tank.
- **VDK readings**, ideally a total-VDK assay that captures both free diacetyl and the alpha-acetolactate precursor still waiting to convert.
- **Yeast state**: pitching rate, generation, and flocculation behaviour.

A model trained on past fermentations predicts when alpha-acetolactate has peaked, when to start the rest, and when residual VDK will fall below 0.10 mg/L. The output is two timestamps and a confidence band, not a fixed recipe rule. For brewers using the ALDC enzyme (such as Maturex), which converts alpha-acetolactate straight to acetoin and bypasses diacetyl entirely, the model's role shifts to confirming the bypass worked rather than timing a long rest.

## Where it breaks
The honest limit is data. Without periodic VDK measurement, the model is inferring the one thing that actually defines the endpoint, and a total-VDK assay (forced or heated) is what reveals trapped precursor. Two confounders also bite. Premature flocculation drops yeast out before reuptake finishes, so the same gravity curve gives high residual VDK; the model needs flocculation as a feature or it will call the rest too early. And Pediococcus contamination produces diacetyl independently of normal metabolism, so a rest cannot fix it. If readings stay high despite a clean profile, the answer is a micro check, not more warm time.

A practical add-on is an assistant that makes the call and writes it up. It reads the live gravity, temperature and last VDK result, recommends starting or ending the rest, and drafts the tank action note with the numbers and reasoning. That keeps the decision consistent across shifts and leaves a record of why each rest was timed as it was.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives fermentation, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Using AI to Time the Diacetyl Rest</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 1</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 2</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">input 3</text><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#00695c"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Fermentation</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">quality</text><g fill="#2e9e7c" stroke="#2e9e7c" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">What drives fermentation, and what it changes downstream.</figcaption>
</figure>

## The bottom line
The diacetyl rest is a timing problem with a clear chemical basis, and timing problems are where models earn their keep. Feed in gravity, temperature, VDK readings and yeast state, watch for flocculation and contamination, and you can hit below 0.10 mg/L without burning days of capacity. Measure VDK, do not assume it.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Forecasting ester and higher-alcohol formation]({{ '/2023/forecasting-ester-higher-alcohol-formation/' | relative_url }})

## Frequently asked questions

**What is a diacetyl rest?**
It is raising fermentation temperature, usually about two-thirds of the way through, to speed yeast reuptake and reduction of diacetyl and other VDKs to flavourless compounds before you cool and package.

**What diacetyl level should I target?**
Below the flavour threshold of roughly 0.10 mg/L for diacetyl (butterscotch). The related compound 2,3-pentanedione has a higher threshold near 1 mg/L.

**Why does diacetyl come back or stay high?**
Premature flocculation drops yeast out before it finishes reuptake, leaving residual VDK. Pediococcus contamination also produces diacetyl, which a rest will not fix.
