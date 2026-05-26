---
layout: post
title: "Brewhouse Yield: Using Analytics to Find Where Extract Disappears"
image: /assets/og/brewhouse-yield-loss-analytics.png
description: "Use mass-balance accounting and analytics to attribute the gap between theoretical and actual extract across milling, lauter, trub, transfer, and evaporation."
date: 2023-07-25
updated: 2023-07-25
tags: [brewing-science, brewhouse, analytics]
faq:
  - q: "Is this an AI project or an accounting project?"
    a: "Accounting first. A mass balance that attributes extract loss across milling, lauter retention, trub and dead-legs, transfer, and evaporation tells you most of what you need. Modelling and AI come after the numbers reconcile."
  - q: "What's usually the biggest loss?"
    a: "It varies by brewery, which is the whole point of measuring rather than guessing. Common culprits are lauter grain retention, trub and dead-leg losses, and over-specified evaporation — but you fix the biggest leak you actually find, not the one you assume."
  - q: "How accurate does my data need to be?"
    a: "Accurate enough to close the mass balance. If theoretical minus measured losses doesn't reconcile with actual extract, you have a measurement gap to fix before any analytics or model is trustworthy."
---

**Short answer: before you model anything, build a mass balance that attributes the gap between theoretical and actual extract across each loss point — then fix the biggest leak first.** Brewhouse yield is an accounting problem before it is an AI problem.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Brewhouse Yield: Using Analytics to Find Where Extract Disappears</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Yield loss has named addresses
The gap between theoretical extract and what lands in the fermenter is not a mystery; it has specific addresses. Extract leaks at milling and crush, at lauter grain retention, into trub and dead-legs, during transfer and whirlpool, and through evaporation in the boil. Each is a real, attributable loss.

Mass-balance accounting is the discipline of assigning the missing extract to those addresses. You start from theoretical extract for the grist, subtract each measured loss, and see whether the remainder matches actual extract in the fermenter. When it reconciles, you have a true picture of where your yield goes. When it does not, the discrepancy itself is information — usually a measurement you are not taking.

## Accounting before modelling
This is the data-science point worth repeating: measure first, and in this case the measurement *is* most of the work. A clean mass balance often answers the question outright, no model required. Weigh the grist, sample wort gravity and volume at each transfer, quantify grain-out moisture and retained extract, measure trub volume, and track evaporation. Lay those against theoretical extract and the leaks reveal themselves.

Only once the balance closes does analytics add value — spotting that lauter retention drifts with crush, or that evaporation creeps up on long-boil recipes. That is also why a yield programme depends on having collected the right data in the first place; our note on [collecting your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}) makes the case plainly. For the mash side of the same accounting, see [predicting mash efficiency and extract yield]({{ '/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}).

## From a balance to a ranked action list
The generative-AI angle is modest but genuinely useful. A mass balance is a table of numbers most brewers will not act on. An LLM can read that table and turn it into a ranked, plain-language action list: "Your biggest leak this quarter is lauter grain retention at 1.9% of extract — recheck crush and sparge volume first. Evaporation is second at 1.1%; trub losses are small and not worth chasing yet." It translates accounting into priorities, with the reasoning attached, so the brewhouse fixes the largest leak rather than the most visible one.

## Where it breaks
The limit is measurement honesty. A mass balance is only as good as the readings feeding it, and breweries routinely under-measure trub volume, dead-leg holdup, and grain-out extract because they are awkward to sample. If those numbers are estimates, the balance closes on false precision and the ranked action list points you at the wrong leak. Evaporation and transfer losses can also hide inside each other if your volume measurements are coarse. The fix is not a fancier model — it is better instrumentation and consistent sampling until the balance genuinely reconciles. Resist the urge to layer analytics on top of numbers that do not add up.

## The bottom line
Brewhouse yield is won with arithmetic, not algorithms. Build a mass balance that attributes lost extract to milling, lauter, trub, transfer, and evaporation; close it with honest measurement; then let a generative tool rank the leaks into an action list. Fix the biggest one, remeasure, and repeat. The AI is the messenger here — the accounting does the work.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [collecting your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}).

## Frequently asked questions

**Is this an AI project or an accounting project?**
Accounting first. A mass balance that attributes extract loss across milling, lauter retention, trub and dead-legs, transfer, and evaporation tells you most of what you need. Modelling and AI come after the numbers reconcile.

**What's usually the biggest loss?**
It varies by brewery, which is the whole point of measuring rather than guessing. Common culprits are lauter grain retention, trub and dead-leg losses, and over-specified evaporation — but you fix the biggest leak you actually find, not the one you assume.

**How accurate does my data need to be?**
Accurate enough to close the mass balance. If theoretical minus measured losses doesn't reconcile with actual extract, you have a measurement gap to fix before any analytics or model is trustworthy.
