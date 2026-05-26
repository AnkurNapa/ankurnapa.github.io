---
layout: post
title: "A Wine Tasting-Score and Blending Dashboard in Tableau"
image: /assets/og/tableau-wine-tasting-blending-dashboard.png
description: "Build a Tableau blending dashboard with bench-trial scores by lot, attribute radar charts and what-if candidate blends via parameter actions."
date: 2023-04-14
updated: 2023-04-14
tags: [winemaking, tableau, blending]
faq:
  - q: "Can Tableau help with wine blending decisions?"
    a: "It can organise bench-trial scores, plot attribute profiles and let you model candidate blends with parameters. It supports the decision with structure; it does not make it, because blending is a sensory judgement."
  - q: "How do I build a what-if blend in Tableau?"
    a: "Create a parameter for each component lot's percentage, then a calculated field that weights each lot's attribute scores by those percentages. Parameter actions let you slide the proportions and watch the predicted profile shift."
  - q: "Will AI pick my best blend?"
    a: "No. Tableau Pulse can summarise which lots score highest and a model can rank candidates, but sensory quality is non-linear and AI cannot taste. The winemaker's palate makes the final call."
---

**Short answer: a blending dashboard is useful as a structured scratchpad — it organises bench-trial scores and models candidate blends — but the winemaker's palate, not the chart, decides.** Be clear about that division of labour before you build.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Wine Tasting-Score and Blending Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Wine Tasting-Score and Blending Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Structure the tasting data
The measure-first question for blending is "which lots, in what proportion, give the profile I want?" That sets the data: bench-trial scores by lot across attributes — fruit, tannin, acidity, oak, balance — usually from a tasting panel logged into a sheet. Decide your scoring scale and attribute list first, because inconsistent panels are the main reason these dashboards mislead.

Connect an extract and use Tableau Prep to reshape panel scores into a tidy long format, one row per lot per attribute per taster. A FIXED level-of-detail calculation gives each lot's average attribute score across the panel, while an INCLUDE expression can preserve per-taster variation so you can see where the panel disagreed — disagreement is signal, not noise.

## Profiles and the what-if blend
Plot each lot as a radar or small-multiple of bars across attributes, so the panel's collective view of a lot is one shape. The blending tool is the what-if: a parameter for each candidate lot's percentage, plus a calculated field that computes a weighted attribute profile — each lot's score times its proportion, summed. Parameter actions let the winemaker slide the proportions and watch the predicted blend profile move in real time against a target shape held in another parameter.

This is genuinely powerful for narrowing options before the bench. It turns "let's try a few" into "these three proportions are worth tasting," saving glassware and palate fatigue. Tableau Pulse can sit on the panel data and summarise which lots scored highest on each attribute as scores come in.

## Where it breaks
Here is the honest part, and it is the whole point. Sensory quality is non-linear: a blend is not the weighted average of its parts. Two lots that each score well can clash, and a small addition of a lot that scores poorly alone can lift the whole blend. The dashboard's weighted-profile calculation assumes linearity it does not possess, so treat the predicted profile as a hypothesis to taste, never a result. Neither Tableau nor any AI model can taste — Pulse summarises numbers, Explain Data correlates fields, but the synergy between components only reveals itself in the glass. The dashboard shortlists; the palate decides.

## The bottom line
A Tableau blending dashboard is a structured scratchpad: organise bench-trial scores, plot attribute profiles, and use parameter-driven what-ifs to shortlist candidate blends before the bench. Just hold the line on what it is — a way to taste fewer, better options — because the non-linearity of blending means the winemaker's palate makes the call.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [AI wine blending optimisation]({{ '/2024/ai-wine-blending-optimization/' | relative_url }}) and [the wine tasting data stack with AI, Power BI and ERP]({{ '/2024/wine-tasting-data-stack-ai-power-bi-erp/' | relative_url }}).

## Frequently asked questions

**Can Tableau help with wine blending decisions?**
It can organise bench-trial scores, plot attribute profiles and let you model candidate blends with parameters. It supports the decision with structure; it does not make it, because blending is a sensory judgement.

**How do I build a what-if blend in Tableau?**
Create a parameter for each component lot's percentage, then a calculated field that weights each lot's attribute scores by those percentages. Parameter actions let you slide the proportions and watch the predicted profile shift.

**Will AI pick my best blend?**
No. Tableau Pulse can summarise which lots score highest and a model can rank candidates, but sensory quality is non-linear and AI cannot taste. The winemaker's palate makes the final call.
