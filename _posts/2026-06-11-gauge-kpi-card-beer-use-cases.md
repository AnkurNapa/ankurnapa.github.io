---
layout: post
title: "The Gauge and KPI Card in Brewing: Three Beer Use Cases"
image: /assets/og/gauge-kpi-card-beer-use-cases.png
description: "The gauge and the KPI card answer one question fast: are we hitting target right now? Three beer use cases (production vs plan, OEE, on-time-in-full) and why a single number needs context to mean anything."
date: 2026-06-11 08:30:00 -0700
updated: 2026-06-11
tags: [brewing-science, beer-chart-guide, data-visualization, commercial-planning, quality-control]
faq:
  - q: "When should a brewery use a gauge or KPI card?"
    a: "On a dashboard's top row, to show a single headline metric against its target at a glance — production vs plan, packaging-line OEE, on-time-in-full, yield vs target. A KPI card shows the number, its target and a trend arrow; a gauge adds a dial with coloured bands. Both are for instant status, not detail."
  - q: "What is wrong with gauge charts?"
    a: "A gauge uses a lot of space to show one number and its position in a range, which a small KPI card or a bullet chart does more compactly. Gauges with arbitrary coloured zones can also imply judgements ('red') that aren't justified. They're fine for a single hero metric but waste dashboard space if overused; prefer KPI cards or bullet charts for many metrics."
  - q: "How do you make a single-number KPI meaningful?"
    a: "Give it context: show the target, a comparison (vs last period or plan), and a trend or sparkline so 'good or bad' and 'improving or worsening' are both visible. A number alone — '92%' — means nothing without knowing the target, the direction, and whether 92% is up or down. Context is what turns a number into a signal."
---

**Short answer: the gauge and the KPI card answer one question instantly — are we hitting target right now? They belong on a dashboard's top row for headline metrics: production vs plan, OEE, on-time-in-full, yield vs target. The catch is that a single number is meaningless without context, so always pair it with its target, a comparison and a trend. A gauge's dial is space-hungry; for many metrics, compact KPI cards or bullet charts serve better.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A gauge dial showing production at 92% of plan in the amber band, beside two KPI cards for OEE and on-time-in-full with target and trend arrows."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">GAUGE &amp; KPI CARD — STATUS VS TARGET, AT A GLANCE</text><g transform="translate(210,150)"><path d="M-100 0 A 100 100 0 0 1 -31 -95" fill="none" stroke="#7a1f3d" stroke-width="18"/><path d="M-31 -95 A 100 100 0 0 1 80 -60" fill="none" stroke="#d3ad7e" stroke-width="18"/><path d="M80 -60 A 100 100 0 0 1 100 0" fill="none" stroke="#2f6b3a" stroke-width="18"/><line x1="0" y1="0" x2="62" y2="-78" stroke="#1c1a17" stroke-width="3"/><circle r="6" fill="#1c1a17"/><text y="34" text-anchor="middle" font-family="sans-serif" font-size="20" font-weight="700" fill="#1c1a17">92%</text><text y="54" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">production vs plan</text></g><g font-family="sans-serif"><rect x="430" y="78" width="240" height="100" rx="10" fill="#f7ece0" stroke="#cbb89a"/><text x="450" y="106" font-size="11" fill="#6b6258">Packaging OEE</text><text x="450" y="142" font-size="30" font-weight="700" fill="#1c1a17">78%</text><text x="450" y="164" font-size="10" fill="#2f6b3a">&#9650; +3 pts vs target 75%</text><rect x="700" y="78" width="240" height="100" rx="10" fill="#f7ece0" stroke="#cbb89a"/><text x="720" y="106" font-size="11" fill="#6b6258">On-time-in-full</text><text x="720" y="142" font-size="30" font-weight="700" fill="#1c1a17">94%</text><text x="720" y="164" font-size="10" fill="#7a1f3d">&#9660; &#8722;2 pts vs target 97%</text></g><text x="500" y="218" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#6b6258">a number plus target, comparison and trend — that's the difference between data and a signal</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">A gauge for the hero metric, compact cards for the rest — each with target and trend, never a bare number.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). These aren't really "charts" so much as **status indicators** — the top row of almost every dashboard.

## When to reach for it

Reach for a gauge or KPI card when a **single headline metric vs target** needs to be readable in half a second — the executive glance. Use a gauge for one hero metric; use KPI cards (with target and trend) when you have several to line up.

## Use case 1 — Production vs plan

A gauge or card showing today's or the month's output against plan, with the gap and direction. It's the first thing a [commercial planning]({{ '/tracks/commercial-planning/' | relative_url }}) or ops review wants — are we on track, yes or no.

## Use case 2 — Packaging-line OEE

Overall Equipment Effectiveness as a single number against target, with a trend arrow. It headlines the [packaging-line view]({{ '/2023/tableau-packaging-line-oee-dashboard/' | relative_url }}); the detail (availability, performance, quality) lives below.

## Use case 3 — On-time-in-full (OTIF)

Service level as a KPI card with target and vs-last-month. One glance tells the team whether delivery reliability is holding — a board-level supply metric that needs no chart, just context.

## Where this breaks

**A bare number lies by omission** — always show target, comparison and trend; "92%" alone is meaningless. **Gauges waste space** — one dial for one number; for many metrics, cards or [bullet-style]({{ '/2026/bar-chart-beer-use-cases/' | relative_url }}) indicators are tighter. **Arbitrary colour zones judge** — red/amber/green bands imply thresholds; set them deliberately, not by default. **No history** — a card is a snapshot; add a sparkline so direction is visible.

## The bottom line

Gauges and KPI cards deliver instant status-vs-target for headline metrics — production, OEE, OTIF — and belong on the dashboard's top row. Their one rule: never a bare number; pair it with target, comparison and trend, or it signals nothing. Use a gauge for the hero metric and cards for the rest. Next, scheduling and timelines: the [Gantt chart]({{ '/2026/gantt-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**When should a brewery use a gauge or KPI card?**
On a dashboard's top row, to show a single headline metric against its target at a glance — production vs plan, packaging-line OEE, on-time-in-full, yield vs target. A KPI card shows the number, its target and a trend arrow; a gauge adds a dial with coloured bands. Both are for instant status, not detail.

**What is wrong with gauge charts?**
A gauge uses a lot of space to show one number and its position in a range, which a small KPI card or a bullet chart does more compactly. Gauges with arbitrary coloured zones can also imply judgements ("red") that aren't justified. They're fine for a single hero metric but waste dashboard space if overused; prefer KPI cards or bullet charts for many metrics.

**How do you make a single-number KPI meaningful?**
Give it context: show the target, a comparison (vs last period or plan), and a trend or sparkline so "good or bad" and "improving or worsening" are both visible. A number alone — "92%" — means nothing without knowing the target, the direction, and whether 92% is up or down. Context is what turns a number into a signal.
