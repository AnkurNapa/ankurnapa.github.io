---
layout: post
title: "An Executive KPI Scorecard for a Brewery in Tableau"
image: /assets/og/tableau-executive-kpi-scorecard.png
description: "Build a one-page executive scorecard in Tableau with BANs, sparklines and RAG status across volume, margin, yield, OEE, safety and ESG, delivered weekly by Pulse."
date: 2023-10-21
updated: 2023-10-21
tags: [commercial-planning, tableau, analytics]
faq:
  - q: "What is a BAN in Tableau and why use it on a scorecard?"
    a: "A BAN is a Big Aggregate Number, a large single figure such as monthly volume or margin. On an executive scorecard it lets a leader read the headline in seconds, with a sparkline beneath for trend context."
  - q: "How many KPIs should an executive scorecard have?"
    a: "Few. Aim for six to nine headline metrics that a CEO can absorb in under a minute. A scorecard crowded with thirty metrics is a report, not a scorecard, and it will not get read."
  - q: "Can Tableau Pulse replace the weekly leadership review?"
    a: "No. Pulse can deliver a weekly digest and flag what moved, but the review is where judgement happens. The digest prepares the conversation; it does not make the decisions."
---

**Short answer: an executive scorecard is a statement of priorities, so the danger is not building it badly but choosing the wrong KPIs and steering the business by them.** Get the metric selection right and the Tableau craft is the easy part.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for An Executive KPI Scorecard for a Brewery in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">An Executive KPI Scorecard for a Brewery in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Choose the six numbers that run the brewery
A scorecard is a forcing function: every metric you put on it tells the organisation what leadership cares about, and everything you leave off says the opposite. For a brewery owner, a defensible set spans the value chain, volume (commercial), gross margin (financial), brewhouse yield and OEE (operational efficiency), a safety rate, and an ESG intensity metric such as water-to-beer ratio. That is six numbers covering growth, profit, productivity, people and planet. The data-science discipline here is resisting the urge to add a seventh, then an eighth; each addition dilutes the signal. Measure first, design second.

## Build it: BANs, sparklines and RAG
The visual grammar of an executive scorecard is deliberately spare. Each KPI gets a BAN (Big Aggregate Number) for the current value, a sparkline beneath for trend, and a RAG status, red, amber, green, against target. Build RAG as a calculated field comparing actual to a target reference, returning a status that drives the colour. Keep the colour logic honest: amber should mean amber, not "a green we would prefer not to discuss".

Sparklines are minimalist line charts with axes and labels stripped away, sized to sit inside a tile. Use a parameter to switch the comparison basis, versus target, versus last year, versus plan, so the same scorecard answers different leadership questions without three separate dashboards. LOD expressions keep each KPI at the right grain while the page rolls up to a company view; a FIXED calc, for example, holds the annual target steady regardless of the date filter applied elsewhere.

The whole point is one page. If a leader has to scroll or click through tabs, it is not a scorecard. Then let Tableau Pulse do the distribution: configure it to monitor the headline KPIs and deliver a weekly natural-language digest to the leadership inbox, "margin up 1.2 points, OEE down at Site C". That turns a static page into a proactive weekly read and means the Monday review starts from a shared, current picture.

## Where it breaks: the scorecard reflects your priorities
The honest limit is uncomfortable: a scorecard cannot tell you whether you are measuring the right things. If you pick volume and ignore mix, leadership will chase cases at the expense of margin and the scorecard will glow green while profit erodes. Goodhart's law bites hard here, once a number becomes the target, people optimise the number rather than the underlying reality. The chart is faithful; the strategy embedded in the metric choice may not be.

Generative AI sharpens the trap. A Pulse digest is fluent and authoritative, and a confident weekly narrative can lull leaders into governing by digest rather than by judgement. The digest does not know your competitive context, your covenant constraints or the conversation you had with a key customer last week. Keep the weekly review as the place where humans interrogate the numbers, and revisit the KPI set itself at least annually, because the right six numbers for this year are not automatically right for next.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Each stage loses some — the funnel shows where the drop-off is."><rect x="0" y="0" width="720" height="310" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">An Executive KPI Scorecard for a Brewery in Tableau</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#00695c" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reach · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#00695c" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interest · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#00695c" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Trial · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#00695c" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Win · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Each stage loses some — the funnel shows where the drop-off is.</figcaption>
</figure>

## The bottom line
Build the scorecard around six to nine genuinely strategic KPIs, render them as BANs, sparklines and RAG on a single page, and let Pulse carry the weekly digest to leadership. Then treat the metric selection as the real decision, review it deliberately, and never let a tidy green board substitute for the judgement that running a business demands.

*Part of the [Commercial Planning Analytics]({{ '/tracks/commercial-planning/' | relative_url }}) track.* Related: the [CFO's AI dashboard for beverage]({{ '/2026/cfo-ai-dashboard-beverage/' | relative_url }}).

## Frequently asked questions

**What is a BAN in Tableau and why use it on a scorecard?**
A BAN is a Big Aggregate Number, a large single figure such as monthly volume or margin. On an executive scorecard it lets a leader read the headline in seconds, with a sparkline beneath for trend context.

**How many KPIs should an executive scorecard have?**
Few. Aim for six to nine headline metrics that a CEO can absorb in under a minute. A scorecard crowded with thirty metrics is a report, not a scorecard, and it will not get read.

**Can Tableau Pulse replace the weekly leadership review?**
No. Pulse can deliver a weekly digest and flag what moved, but the review is where judgement happens. The digest prepares the conversation; it does not make the decisions.
