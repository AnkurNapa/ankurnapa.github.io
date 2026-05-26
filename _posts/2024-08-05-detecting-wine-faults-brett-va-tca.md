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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the wine production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Detecting Wine Faults Early: Brett, Volatile Acidity, TCA</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Harvest</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Crush / press</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Age</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Bottle</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the wine production flow, start to finish.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Most readings sit inside the normal band; the model flags the one that doesn&#39;t."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">ANOMALY DETECTION</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Detecting Wine Faults Early: Brett, Volatile Acidity, TCA</text><rect x="60" y="120" width="620" height="70" fill="#5b7a1f" opacity="0.12"/><line x1="60" y1="120" x2="680" y2="120" stroke="#5b7a1f" stroke-width="1" stroke-dasharray="4 3"/><line x1="60" y1="190" x2="680" y2="190" stroke="#5b7a1f" stroke-width="1" stroke-dasharray="4 3"/><circle cx="110" cy="150" r="5" fill="#6b6258"/><circle cx="160" cy="140" r="5" fill="#6b6258"/><circle cx="210" cy="165" r="5" fill="#6b6258"/><circle cx="265" cy="148" r="5" fill="#6b6258"/><circle cx="320" cy="158" r="5" fill="#6b6258"/><circle cx="380" cy="143" r="5" fill="#6b6258"/><circle cx="440" cy="168" r="5" fill="#6b6258"/><circle cx="500" cy="150" r="5" fill="#6b6258"/><circle cx="560" cy="160" r="5" fill="#6b6258"/><circle cx="620" cy="146" r="5" fill="#6b6258"/><circle cx="345" cy="92" r="7" fill="#7a1f3d"/><text x="345" y="80" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">anomaly</text><text x="668" y="138" text-anchor="end" font-family="sans-serif" font-size="11" fill="#5b7a1f">normal band</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Most readings sit inside the normal band; the model flags the one that doesn&#39;t.</figcaption>
</figure>

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
