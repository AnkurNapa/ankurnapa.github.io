---
layout: post
title: "A Distillery Production and Spirit-Yield Dashboard in Tableau"
image: /assets/og/tableau-distillery-production-yield-dashboard.png
description: "Build a Tableau distillery dashboard tracking litres of pure alcohol per tonne, yield by run, cut performance and energy per LPA, with AI monitoring."
date: 2023-10-14
updated: 2023-10-14
tags: [distilling-maturation, tableau, spirits]
faq:
  - q: "How do I calculate spirit yield in Tableau?"
    a: "Build a calculated field dividing litres of pure alcohol collected by tonnes of cereal used, computed per production run so you can compare batches and track yield against your target."
  - q: "Can Tableau monitor cut points?"
    a: "It can chart the volume and strength of heads, hearts and tails per run and flag runs where the hearts fraction drifts, but the still operator's judgement on where to cut still drives flavour."
  - q: "Why track energy per LPA?"
    a: "Distilling is energy-intensive, so dividing energy used by litres of pure alcohol produced exposes which runs and stills are costly, helping target efficiency without chasing yield at the expense of character."
---

**Short answer: a Tableau distillery dashboard turns each production run into comparable numbers — litres of pure alcohol per tonne, cut performance and energy per LPA — so you can see which runs are efficient and which are quietly wasteful.** The discipline is to optimise without sacrificing the flavour that yield figures cannot capture.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A Distillery Production and Spirit-Yield Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">A Distillery Production and Spirit-Yield Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Define the run, then the metrics
The natural grain here is a production run: a mash and its resulting distillation. Each row carries cereal input in tonnes, litres of pure alcohol (LPA) collected, the volumes and strengths at each cut — heads, hearts and tails — and the energy consumed. Pull this from your process historian as a live connection where possible, or shape batch exports in Tableau Prep into a clean .hyper extract.

Spirit yield is the headline calculated field: LPA divided by tonnes of cereal. Measure first — agree how you define LPA and which losses count — because a yield number is only comparable if everyone computes it the same way. Once defined, the metric travels cleanly across runs, stills and seasons.

## Yield, cuts and energy on one screen
Three views carry most of the value. First, yield by run as a control-style chart against your target, so drift is obvious and you can spot the run that under-delivered. Second, cut performance: the hearts fraction as a share of total spirit, with the heads and tails alongside, revealing when the cut points are running rich or lean. Third, energy per LPA — energy used divided by LPA produced — which exposes the runs and stills where efficiency is poor.

LOD expressions let you hold a per-still baseline steady while the user filters by month, and a parameter for target yield lets the team flex the benchmark. Published to Tableau Cloud, a Pulse digest can tell the production manager "yield dipped 3% on Still 2 this week" in plain language. For the efficiency modelling, see [AI distillery energy and yield]({{ '/2024/ai-distillery-energy-yield/' | relative_url }}).

## Where it breaks
The trap is treating yield as the only goal. Cut points are a flavour decision as much as a volume one: a wider hearts cut lifts LPA per tonne but can pull heavier, less desirable congeners into the spirit. A dashboard that rewards yield alone will quietly push the operator toward a spirit that fills more casks but matures into something off-style. The second limit is metering: yield and energy figures are only as accurate as your flow meters and weighbridge, and small calibration errors compound across hundreds of runs. Show the metric, but keep the flavour trade-off in view and trust the still operator's judgement on where to cut.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives maturation, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">A Distillery Production and Spirit-Yield Dashboard in Tableau</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Maturation</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">quality</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">What drives maturation, and what it changes downstream.</figcaption>
</figure>

## The bottom line
A Tableau production dashboard gives the distillery a clear, comparable view of yield, cut performance and energy intensity across every run. Built on a clean per-run grain with agreed definitions, it surfaces the costly and the inconsistent runs fast. Just remember that yield and flavour pull against each other, and that every number rests on meter accuracy — use the dashboard to manage efficiency, not to override the craft of the cut.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.* Related: [AI distillery energy and yield]({{ '/2024/ai-distillery-energy-yield/' | relative_url }}).

## Frequently asked questions

**How do I calculate spirit yield in Tableau?**
Build a calculated field dividing litres of pure alcohol collected by tonnes of cereal used, computed per production run so you can compare batches and track yield against your target.

**Can Tableau monitor cut points?**
It can chart the volume and strength of heads, hearts and tails per run and flag runs where the hearts fraction drifts, but the still operator's judgement on where to cut still drives flavour.

**Why track energy per LPA?**
Distilling is energy-intensive, so dividing energy used by litres of pure alcohol produced exposes which runs and stills are costly, helping target efficiency without chasing yield at the expense of character.
