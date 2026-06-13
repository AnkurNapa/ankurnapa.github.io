---
layout: post
title: "The Gantt Chart in Brewing: Three Beer Use Cases"
image: /assets/og/gantt-chart-beer-use-cases.png
description: "A Gantt chart lays tasks against time as bars — perfect for schedules and overlaps. Three beer use cases (the brew schedule, tank and vessel occupancy, NPD project timeline) and where a calendar or a different view serves better."
date: 2026-06-11 08:40:00 -0700
updated: 2026-06-11
tags: [brewing-science, beer-chart-guide, data-visualization, commercial-planning, beer-npd]
faq:
  - q: "When should a brewery use a Gantt chart?"
    a: "When you're scheduling activities against time and overlaps and dependencies matter — the brew and packaging schedule, tank or fermenter occupancy, or a new-product project timeline. Each task is a horizontal bar positioned and sized by its start and duration, so clashes (two brews needing the same vessel) and critical paths become visible."
  - q: "What is a Gantt chart good at that a calendar isn't?"
    a: "Showing duration and overlap across many parallel tracks at once. A calendar shows what's on a given day; a Gantt shows how long each activity runs and where activities collide across resources — ideal for spotting that two beers both need the bright tank in week three. For simple day-by-day scheduling a calendar may be plenty."
  - q: "What is the weakness of a Gantt chart for brewing?"
    a: "It can become complex fast — many vessels, many batches, shifting durations — and a static Gantt goes stale the moment the schedule changes. It also shows time and duration well but not capacity utilisation as a number. For live scheduling, a Gantt needs to be connected to real data, and for pure occupancy percentages a different chart is clearer."
---

**Short answer: the Gantt chart lays activities against time as horizontal bars, sized by duration, so schedules, overlaps and dependencies become visible. In a brewery it's the brew and packaging schedule, tank and fermenter occupancy, and the new-product project timeline — anywhere two things might collide over the same vessel or week. Its strength is showing duration and overlap across parallel tracks; its weakness is going stale the moment the plan changes, so keep it connected to real data.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A Gantt chart of fermenter occupancy across four weeks, with overlapping bars for several batches and one highlighted clash where two batches need the same vessel."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">GANTT — TASKS AGAINST TIME, OVERLAPS VISIBLE</text><g font-family="sans-serif" font-size="9.5" fill="#6b6258"><text x="120" y="66" text-anchor="end">FV1</text><text x="120" y="98" text-anchor="end">FV2</text><text x="120" y="130" text-anchor="end">FV3</text><text x="120" y="162" text-anchor="end">Bright</text></g><g stroke="#e4d9c8"><line x1="140" y1="46" x2="140" y2="190"/><line x1="340" y1="46" x2="340" y2="190"/><line x1="540" y1="46" x2="540" y2="190"/><line x1="740" y1="46" x2="740" y2="190"/><line x1="920" y1="46" x2="920" y2="190"/></g><g font-family="sans-serif" font-size="9" fill="#fdfbf7"><rect x="140" y="56" width="280" height="20" rx="4" fill="#b45309"/><text x="150" y="71">Lager #41</text><rect x="440" y="56" width="240" height="20" rx="4" fill="#8a5a2b"/><text x="450" y="71">Pils #42</text><rect x="240" y="88" width="300" height="20" rx="4" fill="#8a5a2b"/><text x="250" y="103">IPA #43</text><rect x="140" y="120" width="220" height="20" rx="4" fill="#b45309"/><text x="150" y="135">Stout #44</text><rect x="560" y="120" width="300" height="20" rx="4" fill="#8a5a2b"/><text x="570" y="135">Wheat #45</text><rect x="500" y="152" width="180" height="20" rx="4" fill="#7a1f3d"/><text x="510" y="167">Pkg run</text><rect x="640" y="152" width="120" height="20" rx="4" fill="#7a1f3d" opacity="0.6"/></g><text x="700" y="186" font-family="sans-serif" font-size="9" fill="#7a1f3d">bright-tank clash &#8212; resolve</text><text x="500" y="216" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">rows = vessels, bars = batches over time — overlaps on one row are conflicts to fix</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Each row a vessel, each bar a batch's occupancy — two bars overlapping on one row is a scheduling clash.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). It's the scheduling chart — time on one axis, resources or tasks stacked on the other.

## When to reach for it

Reach for a Gantt when you're **placing activities on a timeline** and **overlap or sequence matters** — when the question is "what runs when, and does anything collide." Bars sized by duration make clashes and critical paths jump out.

## Use case 1 — Tank and vessel occupancy

Rows for fermenters and bright tanks, bars for each batch's residency. The Gantt instantly shows where two batches want the same vessel in the same week — the single most useful scheduling view a [planning]({{ '/tracks/commercial-planning/' | relative_url }}) brewer has.

## Use case 2 — The brew and packaging schedule

Brew days, fermentation, conditioning and packaging runs laid against the calendar across the brewhouse and line. Dependencies (you can't package before it's conditioned) become visible, and gaps reveal under-used capacity.

## Use case 3 — The NPD project timeline

For a new product, the stages from recipe trials through pilot, scale-up and launch as a Gantt. It keeps a cross-functional [beer NPD]({{ '/series/beer-npd/' | relative_url }}) project honest about what must finish before launch.

## Where this breaks

**Staleness** — a static Gantt is wrong the moment the plan shifts; connect it to live data or it misleads. **Complexity** — many vessels and batches crowd fast; filter to a horizon or a resource group. **Not a utilisation number** — it shows time and overlap, not capacity %; for that, use a [bar]({{ '/2026/bar-chart-beer-use-cases/' | relative_url }}) or [heat map]({{ '/2026/heat-map-beer-use-cases/' | relative_url }}). **Over-detailed** — a Gantt of every micro-task is unreadable; show the activities that actually clash or gate.

## The bottom line

The Gantt chart shows activities against time with duration and overlap — tank occupancy, the brew/packaging schedule, the NPD timeline — making clashes and critical paths visible at a glance. Keep it connected to real data, filtered to a sensible horizon, and reserve a different chart for pure utilisation. Last in the field guide's specialized set: spatial data, the [geographic map]({{ '/2026/geographic-map-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**When should a brewery use a Gantt chart?**
When you're scheduling activities against time and overlaps and dependencies matter — the brew and packaging schedule, tank or fermenter occupancy, or a new-product project timeline. Each task is a horizontal bar positioned and sized by its start and duration, so clashes (two brews needing the same vessel) and critical paths become visible.

**What is a Gantt chart good at that a calendar isn't?**
Showing duration and overlap across many parallel tracks at once. A calendar shows what's on a given day; a Gantt shows how long each activity runs and where activities collide across resources — ideal for spotting that two beers both need the bright tank in week three. For simple day-by-day scheduling a calendar may be plenty.

**What is the weakness of a Gantt chart for brewing?**
It can become complex fast — many vessels, many batches, shifting durations — and a static Gantt goes stale the moment the schedule changes. It also shows time and duration well but not capacity utilisation as a number. For live scheduling, a Gantt needs to be connected to real data, and for pure occupancy percentages a different chart is clearer.
