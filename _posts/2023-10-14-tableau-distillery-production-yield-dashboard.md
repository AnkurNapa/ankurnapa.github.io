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

## Define the run, then the metrics
The natural grain here is a production run: a mash and its resulting distillation. Each row carries cereal input in tonnes, litres of pure alcohol (LPA) collected, the volumes and strengths at each cut — heads, hearts and tails — and the energy consumed. Pull this from your process historian as a live connection where possible, or shape batch exports in Tableau Prep into a clean .hyper extract.

Spirit yield is the headline calculated field: LPA divided by tonnes of cereal. Measure first — agree how you define LPA and which losses count — because a yield number is only comparable if everyone computes it the same way. Once defined, the metric travels cleanly across runs, stills and seasons.

## Yield, cuts and energy on one screen
Three views carry most of the value. First, yield by run as a control-style chart against your target, so drift is obvious and you can spot the run that under-delivered. Second, cut performance: the hearts fraction as a share of total spirit, with the heads and tails alongside, revealing when the cut points are running rich or lean. Third, energy per LPA — energy used divided by LPA produced — which exposes the runs and stills where efficiency is poor.

LOD expressions let you hold a per-still baseline steady while the user filters by month, and a parameter for target yield lets the team flex the benchmark. Published to Tableau Cloud, a Pulse digest can tell the production manager "yield dipped 3% on Still 2 this week" in plain language. For the efficiency modelling, see [AI distillery energy and yield]({{ '/2024/ai-distillery-energy-yield/' | relative_url }}).

## Where it breaks
The trap is treating yield as the only goal. Cut points are a flavour decision as much as a volume one: a wider hearts cut lifts LPA per tonne but can pull heavier, less desirable congeners into the spirit. A dashboard that rewards yield alone will quietly push the operator toward a spirit that fills more casks but matures into something off-style. The second limit is metering: yield and energy figures are only as accurate as your flow meters and weighbridge, and small calibration errors compound across hundreds of runs. Show the metric, but keep the flavour trade-off in view and trust the still operator's judgement on where to cut.

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
