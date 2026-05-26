---
layout: post
title: "Detecting Wine Faults Early: Brett, Volatile Acidity, TCA"
image: /assets/og/detecting-wine-faults-brett-va-tca.png
description: "How AI flags wine faults early — Brettanomyces, volatile acidity, and TCA cork taint — from cellar conditions and rapid analysis, since most faults are easier to prevent than reverse."
date: 2024-08-05
updated: 2024-08-05
tags: [winemaking, quality-control, microbiology]
faq:
  - q: "Can AI detect cork taint (TCA)?"
    a: "Only indirectly. TCA is detectable at single-digit nanograms per litre, far below what cellar sensors see, so AI helps mainly by flagging contamination risk and triggering targeted GC-MS testing rather than measuring TCA itself."
  - q: "Which wine faults can AI predict early?"
    a: "Microbial and chemical faults with measurable precursors — Brettanomyces, volatile acidity, reduction, and oxidation — by watching pH, free and molecular SO2, temperature, and oxygen exposure against rapid micro and chemistry results."
  - q: "Does early detection mean I can fix the fault?"
    a: "Sometimes, but the real win is prevention. Most faults are far easier to prevent than reverse, so the model's value is in catching the conditions before the fault sets in."
---

**Short answer: AI is most valuable for wine faults as an early-warning system on the conditions that cause them — because Brett, volatile acidity, and TCA are far easier to prevent than to reverse.** A single tainted lot can erase a vintage's margin, which is why catching the drift early pays for itself.

## The faults worth catching early
A handful of faults do most of the damage. *Brettanomyces* yeast produces 4-ethylphenol and 4-ethylguaiacol — the "barnyard" and "medicinal" notes — and thrives in warm, low-SO2, higher-pH conditions. Volatile acidity is acetic acid produced by *Acetobacter*, with a sensory threshold around 0.7-1.2 g/L. Cork taint is 2,4,6-trichloroanisole (TCA), detectable at only a few nanograms per litre — single-digit ng/L. Reduction throws hydrogen sulphide and mercaptans ("rotten egg"); oxidation shows up as acetaldehyde. Most of these are confirmed by GC-MS and trained sensory panels, but by the time a panel smells them, the lot may already be compromised.

The strategic point is the asymmetry: prevention is cheap and reversal is expensive or impossible. That is exactly the kind of problem where a predictive model earns its keep.

## Measure first: conditions plus rapid analysis
The model watches the cellar conditions that drive microbial and chemical faults, then cross-references rapid testing. The core data: pH, free and molecular SO2, temperature, and oxygen exposure across each lot, logged over time. SO2 deserves special attention because the active, protective fraction is molecular SO2, which depends on both free SO2 and pH — so the same addition does far more at low pH than at high. A model that tracks molecular SO2 rather than just free SO2 understands real spoilage risk much better.

Layer rapid microbiology (Brett cell counts) and targeted chemistry on top, and the model learns which combinations of conditions precede which faults. The aim is not to replace GC-MS or the sensory panel — it is to tell you which lots deserve their attention first. Panel calibration matters here too; see [AI for sensory panel and taster calibration]({{ '/2024/ai-sensory-panel-taster-calibration/' | relative_url }}).

## Where it breaks
TCA is the honest limit. At single-digit nanograms per litre it sits far below anything a cellar sensor can read, and its source is sporadic — a contaminated cork, a tainted barrel, a treated piece of cellar timber. AI cannot measure TCA from conditions; at best it flags contamination risk and routes suspect lots to GC-MS. The second limit is rare-event data: bad Brett outbreaks and high-VA lots are uncommon in a well-run cellar, so a model has few examples to learn from and can miss the unusual case. And lab confirmation is never optional — a model's "elevated Brett risk" is a prompt to test and act on SO2 and temperature, not a diagnosis. Treat the output as a triage signal, not a verdict.

## How generative AI fits in
The practical generative angle is a copilot that fuses microbiology and chemistry into an early-warning alert with a prevention checklist. Instead of three separate reports, the winemaker gets: "Barrel room lot 4 — pH has crept to 3.78, molecular SO2 has fallen below the protective level at this pH, temperature is running warm, and the last Brett count ticked up. Elevated Brett risk. Recommend an SO2 addition to restore molecular SO2, drop the room temperature, and re-test in a week." It explains the chain of reasoning and hands over actions, not just a red light. Synthetic data helps too: because severe faults are rare, simulated fault scenarios can train the model to recognise warning patterns it would otherwise almost never see — validated, always, against real lab results.

## The bottom line
AI does not measure cork taint and it will not save you from a fault you only smell at bottling. Its real value is steering attention: watch molecular SO2, pH, temperature, and oxygen across your lots, let the model triage which ones need the lab and the panel, and act on the conditions early. In fault management, prevention is the whole game — and that is what a good model helps you play.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [AI for sensory panel and taster calibration]({{ '/2024/ai-sensory-panel-taster-calibration/' | relative_url }}).

## Frequently asked questions

**Can AI detect cork taint (TCA)?**
Only indirectly. TCA is detectable at single-digit nanograms per litre, far below what cellar sensors see, so AI helps mainly by flagging contamination risk and triggering targeted GC-MS testing rather than measuring TCA itself.

**Which wine faults can AI predict early?**
Microbial and chemical faults with measurable precursors — Brettanomyces, volatile acidity, reduction, and oxidation — by watching pH, free and molecular SO2, temperature, and oxygen exposure against rapid micro and chemistry results.

**Does early detection mean I can fix the fault?**
Sometimes, but the real win is prevention. Most faults are far easier to prevent than reverse, so the model's value is in catching the conditions before the fault sets in.
