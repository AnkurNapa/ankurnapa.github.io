---
layout: post
title: "Reducing Packaging Material Waste With AI"
image: /assets/og/reducing-packaging-material-waste-ai.png
description: "Use AI and checkweigher data to cut overfill, giveaway, rejects, and changeover scrap — trimming packaging COGS and carbon without breaking the strength floor."
date: 2024-04-25
updated: 2024-04-25
tags: [brewing-science, packaging, sustainability]
faq:
  - q: "Where does packaging material waste actually come from?"
    a: "Mostly four places: liquid and material giveaway from overfill, reject rates on the line, scrap during changeovers, and lightweighting decisions that leave material on the table. Packaging is a major COGS and carbon line, so each adds up."
  - q: "Can you lightweight cans and glass safely with AI?"
    a: "Only within the strength floor. A model can find the giveaway, but the body-maker draw-and-iron limits and pressure-vessel strength requirements are hard constraints — the optimisation must treat quality and integrity as non-negotiable."
  - q: "How does generative AI help with packaging sustainability?"
    a: "An LLM can turn waste and checkweigher data into a ranked savings plan and draft the sustainability note — quantifying the material, cost, and carbon saved — so the case is ready for operations and reporting."
---

**Short answer: packaging is one of your largest COGS and carbon lines, and AI cuts the four big leaks — overfill giveaway, rejects, changeover scrap, and conservative lightweighting — without crossing the strength floor.** The savings are real because the waste is structural, repeated every shift, and mostly invisible until you measure it.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the whiskey production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Reducing Packaging Material Waste With AI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Distil</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mature</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Bottle</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the whiskey production flow, start to finish.</figcaption>
</figure>

## Find the waste before you cut it
Material — glass, aluminium, PET, kegs — is bought by weight and counted by the pallet, so small per-unit losses scale fast. Aluminium cans are drawn and ironed by the body maker using tungsten-carbide rings; PET has a pasteurisation ceiling near 78 °C; glass and cans both carry strength specs you cannot ignore. Each format has its own waste profile.

The four leaks are consistent. Overfill is giveaway: every millilitre above target, multiplied across a run, is product and material given away free. Rejects are units scrapped for fill, seam, or label faults. Changeovers throw away start-up cans and bottles before the line settles. And lightweighting — using less material per unit — is often left conservative because nobody has the data to push it safely.

The data-science job is to measure first. The checkweigher and the line controls already produce most of what you need: fill weights, reject reasons and counts, changeover durations and scrap, and material-spec data per SKU. Bring those together per run and the waste stops being a vague monthly variance and becomes a measurable, attributable number.

## Optimise to the limit, not past it
With that data, a model can do two useful things. It can tighten the fill distribution — predicting the set-point that holds you just above the legal and quality minimum rather than padding to be safe, which is where most giveaway hides. And it can attribute rejects and changeover scrap to causes, so you fix the SKU, setting, or sequence that produces them.

Generative optimisation extends this: given the strength and quality constraints, the model searches the trade-off space — fill target versus giveaway, material weight versus integrity, run order versus changeover scrap — and proposes the configuration that minimises waste while staying inside every limit. The point is that lightweighting and tighter fills are optimisation problems with hard constraints, not guesses.

## Where it breaks
The non-negotiable limit is the strength and quality floor. A can must survive ~8 bar; a bottle must not fail; a fill must stay legal and on-brand. An optimiser that shaves material until cans crumple or fills run short has not saved money — it has created recalls and complaints. Treat quality and integrity as inviolable constraints, not variables to trade.

The other limit is data quality. If the checkweigher is poorly calibrated, or reject reasons are logged as a single catch-all "fault", the model optimises against noise. Clean attribution comes first; the savings follow. And material specs from suppliers vary batch to batch, so a setting that was safe last month may have less margin this month — keep the constraints current.

## From numbers to a plan and a report
The last mile is decision-making. An LLM reads the waste and checkweigher data and produces a ranked savings plan: the largest, most achievable wins first, each with the material, cost, and carbon it removes. It then drafts the sustainability note — the kind operations and finance actually need — quantifying the reduction in tonnes of aluminium or glass and the associated carbon. The analysis becomes a decision and a document in one step, rather than a spreadsheet nobody acts on.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 320" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A continuous cycle — each step feeds the next, then round again."><rect x="0" y="0" width="720" height="320" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">THE CYCLE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Reducing Packaging Material Waste With AI</text><circle cx="360" cy="190" r="95" fill="none" stroke="#e0d8cc" stroke-width="1.5" stroke-dasharray="5 5"/><circle cx="360" cy="95" r="34" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360" y="100" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">Plan</text><circle cx="455" cy="190" r="34" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="455" y="195" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">Do</text><circle cx="360" cy="285" r="34" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360" y="290" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">Check</text><circle cx="265" cy="190" r="34" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="265" y="195" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">Act</text><circle cx="428" cy="140" r="4" fill="#b45309"/><circle cx="410" cy="258" r="4" fill="#b45309"/><circle cx="292" cy="240" r="4" fill="#b45309"/><circle cx="310" cy="122" r="4" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A continuous cycle — each step feeds the next, then round again.</figcaption>
</figure>

## The bottom line
Packaging waste is large, repeatable, and measurable — which makes it ideal for AI. Measure the four leaks with checkweigher and line data, optimise fills and lightweighting up to the strength floor but never past it, and let an LLM turn the result into a ranked plan and a sustainability note. The carbon savings and the COGS savings are the same number.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [predictive maintenance for fillers and seamers]({{ '/2024/predictive-maintenance-filler-seamer/' | relative_url }}).

## Frequently asked questions

**Where does packaging material waste actually come from?**
Mostly four places: liquid and material giveaway from overfill, reject rates on the line, scrap during changeovers, and lightweighting decisions that leave material on the table. Packaging is a major COGS and carbon line, so each adds up.

**Can you lightweight cans and glass safely with AI?**
Only within the strength floor. A model can find the giveaway, but the body-maker draw-and-iron limits and pressure-vessel strength requirements are hard constraints — the optimisation must treat quality and integrity as non-negotiable.

**How does generative AI help with packaging sustainability?**
An LLM can turn waste and checkweigher data into a ranked savings plan and draft the sustainability note — quantifying the material, cost, and carbon saved — so the case is ready for operations and reporting.
