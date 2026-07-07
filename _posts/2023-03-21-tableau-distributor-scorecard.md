---
layout: post
title: "Building a Distributor Scorecard in Tableau"
image: /assets/og/tableau-distributor-scorecard.png
description: "Build a weighted distributor scorecard in Tableau with calculated fields, rank, highlight actions and Explain Data — and avoid the gaming traps."
date: 2023-03-21
updated: 2023-03-21
tags: [sales-intelligence, tableau, analytics]
faq:
  - q: "What metrics belong on a distributor scorecard?"
    a: "The durable three are distribution breadth (how many target accounts are stocked), velocity (rate of sale per account), and compliance (orders, payments and reporting hitting agreed terms). Add price or display execution only if you can measure them consistently."
  - q: "How do I build a weighted score in Tableau?"
    a: "Normalise each metric to a common 0–100 scale with a calculated field, multiply by its weight, and sum the components. Keep the weights in parameters so reviewers can see and adjust them rather than burying them in the formula."
  - q: "Can Tableau explain why a distributor scored badly?"
    a: "Explain Data can surface the dimensions and records most associated with an unusual mark, which is a useful starting point. It is a statistical hint, not a verdict, so treat it as a prompt for a human conversation."
---

**Short answer: a distributor scorecard is only as fair as the weights behind it, so build those weights in the open and let Tableau do the ranking, highlighting and explaining.** A scorecard turns a sprawling partner network into a ranked list a regional manager can act on in a quarterly business review — provided the maths is defensible.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for Building a Distributor Scorecard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Building a Distributor Scorecard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Define the measure before the visual

A score is a model, not a chart, so design it like one. Pick a small set of metrics that genuinely drive results and that you can measure cleanly across every distributor: distribution breadth, velocity, and compliance. Resist the urge to bolt on a dozen vanity metrics; each one you add dilutes the signal and invites disputes.

Normalise each metric to the same scale before weighting, because raw values do not combine — cases per account and percentage compliance live in different units. A simple min-max calculation works:

`( SUM([Velocity]) - WINDOW_MIN(SUM([Velocity])) ) / ( WINDOW_MAX(SUM([Velocity])) - WINDOW_MIN(SUM([Velocity])) ) * 100`

Then combine the normalised components against weights held in parameters: `[w_dist] * [Dist Score] + [w_vel] * [Vel Score] + [w_comp] * [Comp Score]`. Exposing the weights as parameters is the single most important design choice — it makes the model auditable and lets a sceptical sales director re-run the ranking under their own assumptions during the meeting.

## Rank, highlight and explain

Use Tableau's `RANK()` table calculation to order distributors, and present the result as a horizontal bar chart sorted by total score, with the weighted components stacked so a viewer sees not just the rank but its composition. A distributor scoring 72 because of strong velocity but weak compliance is a very different conversation from one scoring 72 on the reverse.

Highlight actions tie the dashboard together. Hovering or clicking a distributor highlights its row across every linked sheet — its trend, its account list, its compliance detail — so the whole story moves with the selection rather than forcing the user to re-filter. When a mark looks off, right-click and run Explain Data: Tableau models the expected value and surfaces the records or dimensions most associated with the deviation. That might point to one delinquent chain dragging down compliance. Treat it as a lead to investigate, not a conclusion; Explain Data describes the data, it does not know your commercial context.

## Where it breaks

The deepest risk is not technical, it is behavioural. Any score you publish becomes a target, and targets get gamed. Weight velocity too heavily and a distributor may chase fast-moving SKUs while letting your premium range gather dust. Reward distribution breadth alone and you get token placements with no rate of sale. Goodhart's law applies in full: when a measure becomes a target, it ceases to be a good measure. Review the weights periodically and watch for behaviour that optimises the score rather than the business.

The second limit is fairness across uneven partners. A scorecard that ignores territory size, account mix or tenure will punish a distributor for a market it inherited rather than performance it controls. Where possible, compare like with like — segment by market type — rather than ranking a rural wholesaler against a metro powerhouse on one absolute scale. And as ever, Tableau will faithfully rank dirty data; a missing compliance feed reads as a zero, not as "unknown", unless you handle nulls deliberately.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Each stage loses some — the funnel shows where the drop-off is."><rect x="0" y="0" width="720" height="310" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Building a Distributor Scorecard in Tableau</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#00695c" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reach · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#00695c" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interest · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#00695c" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Trial · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#00695c" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Win · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Each stage loses some — the funnel shows where the drop-off is.</figcaption>
</figure>

## The bottom line

A good distributor scorecard normalises a few honest metrics, weights them transparently through parameters, and uses rank and highlight actions to make the ranking navigable. Explain Data accelerates the diagnosis but does not replace the judgement call. Guard against gaming by revisiting weights and segmenting fairly, and remember the model is a conversation-starter, not the final word.

*Part of the [Sales Intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) track.* Related: [A Depletions and Sell-Through Dashboard in Tableau]({{ '/2023/tableau-depletions-sell-through-dashboard/' | relative_url }}).

## Frequently asked questions

**What metrics belong on a distributor scorecard?**
The durable three are distribution breadth (how many target accounts are stocked), velocity (rate of sale per account), and compliance (orders, payments and reporting hitting agreed terms). Add price or display execution only if you can measure them consistently.

**How do I build a weighted score in Tableau?**
Normalise each metric to a common 0–100 scale with a calculated field, multiply by its weight, and sum the components. Keep the weights in parameters so reviewers can see and adjust them rather than burying them in the formula.

**Can Tableau explain why a distributor scored badly?**
Explain Data can surface the dimensions and records most associated with an unusual mark, which is a useful starting point. It is a statistical hint, not a verdict, so treat it as a prompt for a human conversation.
