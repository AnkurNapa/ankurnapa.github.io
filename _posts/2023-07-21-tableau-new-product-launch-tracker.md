---
layout: post
title: "A New-Product Launch Tracker in Tableau"
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
