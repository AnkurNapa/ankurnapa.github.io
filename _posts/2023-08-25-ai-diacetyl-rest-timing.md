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
