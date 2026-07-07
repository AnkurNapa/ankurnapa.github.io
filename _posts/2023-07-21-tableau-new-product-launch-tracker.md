---
layout: post
title: "A New-Product Launch Tracker in Tableau"
image: /assets/og/tableau-new-product-launch-tracker.png
description: "Build a new-product launch tracker in Tableau using LOD calcs, table calculations and Pulse to follow trial, repeat and rate-of-sale per door."
date: 2023-07-21
updated: 2023-07-21
tags: [marketing, tableau, analytics]
faq:
  - q: "What metrics matter most when tracking a new product launch?"
    a: "Distribution build (doors selling), rate-of-sale per door, and the trial-to-repeat ratio. Volume alone flatters a launch; repeat rate tells you whether it will last."
  - q: "Can Tableau forecast how a launch will land?"
    a: "Tableau's built-in forecast uses exponential smoothing, which is fine for a rough trend line but weak on a launch with only a few weeks of noisy data. Treat it as directional, not gospel."
  - q: "How do I compare different launch cohorts in one view?"
    a: "Use a parameter to select the launch cohort or week-since-launch index, then drive a table calculation off it so every product is aligned to its own launch date rather than the calendar."
---

**Short answer: a good launch tracker measures repeat purchase and rate-of-sale per door, not just total cases shipped.** Shipments tell you what you pushed into the trade; the tracker has to tell you what actually sold through and came back for more.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typical dashboard layout for A New-Product Launch Tracker in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">A New-Product Launch Tracker in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filters:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Breakdown</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A typical layout for this dashboard: headline metrics up top, a trend and a breakdown below, filters to slice it.</figcaption>
</figure>

## Decide the measure before you touch a chart
The discipline of a launch tracker is deciding what "working" means before the data tempts you. For a new beer or RTD, three measures carry the verdict: distribution build (how many doors are stocking it), rate-of-sale per door (velocity, not just presence), and the trial-to-repeat ratio (did drinkers come back). Sketch those on paper first. A dashboard that opens with a vanity case-volume number trains everyone to celebrate sell-in and ignore sell-through, which is exactly how a launch dies quietly on shelf.

In data-science terms, you are separating a stock metric (cumulative distribution) from a flow metric (weekly rate-of-sale). Mixing them on one axis is the most common launch-tracking mistake I see.

## Build it: LOD, table calcs and a cohort parameter
The craft starts with alignment. Calendar weeks are useless when products launch on different dates, so build a "weeks since launch" index and let every product start at week zero. A FIXED LOD expression pins each product's launch date independent of the filters on the view:

`{ FIXED [Product] : MIN([First Sale Date]) }`

Subtract that from the sale date and you have your launch-relative axis. Rate-of-sale is then a table calculation: sold units divided by active doors, computed along the launch-week index. Distribution build is a running count of distinct doors, again a table calc partitioned by product.

Add a parameter to switch the analysis cohort, summer launches versus autumn, premium versus core, and wire it to a parameter action so a click on one product reframes the whole view. Trial-versus-repeat needs a calculated field flagging a customer's first purchase against subsequent ones; an INCLUDE LOD lets you count repeat buyers at customer grain while still displaying at product grain.

For the executive layer, point Tableau Pulse at rate-of-sale and repeat rate. Pulse monitors those metrics and sends a natural-language digest, "rate-of-sale up 12% week-on-week, driven by the South region", so leadership reads the launch without opening the workbook. Einstein Copilot's Explain Data can take a stab at why one region spiked, though you should verify its reasoning before repeating it.

## Where it breaks
Early launch data is genuinely noisy. Two weeks of sell-through across a handful of doors is not a trend, and a tracker that updates daily invites people to over-react to sampling noise. Repeat rate is the worst offender: it physically cannot stabilise until enough drinkers have had time to come back, often six to eight weeks for a regularly purchased category. If your dashboard flashes a confident repeat number in week two, it is lying with a straight face.

There is also the attribution trap. A spike might be a feature display, a competitor stockout, or a heatwave, none of which Tableau knows about. The chart shows the what; the why still needs a human who walked the trade. Generative-AI summaries amplify this risk: a fluent Pulse digest reads as authoritative even when the underlying sample is thin, so put confidence caveats in the dashboard itself.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="How much each channel contributes — the longer the bar, the bigger the effect."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">CONTRIBUTION</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">A New-Product Launch Tracker in Tableau</text><text x="60" y="109" font-family="sans-serif" font-size="12.5" fill="#06483f">Channel A</text><rect x="180" y="90" width="300" height="26" rx="4" fill="#00695c"/><text x="60" y="153" font-family="sans-serif" font-size="12.5" fill="#06483f">Channel B</text><rect x="180" y="134" width="230" height="26" rx="4" fill="#00695c"/><text x="60" y="197" font-family="sans-serif" font-size="12.5" fill="#06483f">Channel C</text><rect x="180" y="178" width="150" height="26" rx="4" fill="#00695c"/><text x="60" y="241" font-family="sans-serif" font-size="12.5" fill="#06483f">Channel D</text><rect x="180" y="222" width="90" height="26" rx="4" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">How much each channel contributes — the longer the bar, the bigger the effect.</figcaption>
</figure>

## The bottom line
A launch tracker earns its place when it shifts the conversation from "how many did we ship" to "is it coming back". Build the cohort alignment with LOD and table calcs, lead with rate-of-sale and repeat, and let Pulse carry the weekly read to executives. Then hold your nerve on early data and let repeat rate mature before you call the launch.

*Part of the [Marketing]({{ '/tracks/marketing/' | relative_url }}) track.* Related: the broader [brand and marketing performance dashboard]({{ '/2023/tableau-brand-marketing-dashboard/' | relative_url }}).

## Frequently asked questions

**What metrics matter most when tracking a new product launch?**
Distribution build (doors selling), rate-of-sale per door, and the trial-to-repeat ratio. Volume alone flatters a launch; repeat rate tells you whether it will last.

**Can Tableau forecast how a launch will land?**
Tableau's built-in forecast uses exponential smoothing, which is fine for a rough trend line but weak on a launch with only a few weeks of noisy data. Treat it as directional, not gospel.

**How do I compare different launch cohorts in one view?**
Use a parameter to select the launch cohort or week-since-launch index, then drive a table calculation off it so every product is aligned to its own launch date rather than the calendar.
