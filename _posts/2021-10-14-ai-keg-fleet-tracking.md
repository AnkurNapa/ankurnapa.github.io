---
layout: post
title: "AI for Keg Fleet Tracking and Optimisation"
description: "How IoT data and machine learning track keg location and dwell time, right-size your float, and cut lost-keg cost and over-purchasing."
date: 2021-10-14
updated: 2021-10-14
tags: [sales-intelligence, logistics, iot]
faq:
  - q: "How does AI help track a keg fleet?"
    a: "It combines IoT tag pings and scan data with machine learning to estimate where kegs are, how long they have sat idle, and the float size you actually need. The aim is to cut lost-keg cost and stop you over-buying stainless."
  - q: "What is keg dwell time and why does it matter?"
    a: "Dwell time is how long a keg sits at a venue or in transit before it returns. High dwell time ties up assets you have already paid for, so reducing it lets a smaller fleet serve the same volume."
  - q: "What are the limits of keg tracking with AI?"
    a: "Tags cost money and rarely cover the whole fleet, and scan data is often messy or missing. The model can only estimate what the data lets it see, so coverage and data quality cap accuracy."
---

**Short answer: pairing IoT and scan data with machine learning estimates keg location and dwell time, so you recover stranded kegs and stop over-buying a fleet you do not need.** Kegs are expensive returnable assets, and most breweries leak money on them quietly.

## The returnable-asset problem
A keg is a costly piece of stainless that you own but rarely see. It leaves the brewery full, lands at a bar or distributor, and then — too often — goes quiet. Some sit idle in a cellar long after they are empty. Some are misplaced, scrapped or quietly walk off. Every one that disappears or lingers is capital you have paid for and cannot use.

The classic reaction is to buy more kegs. That hides the problem and inflates cost. The smarter move is to understand the float you genuinely need, which depends on how fast kegs cycle back. That is a data question, and it is exactly where machine learning earns its place.

## Measure first: what the data tells you
Before any clever model, get the measurement right. IoT tags ping location; scan events at fill, dispatch, delivery and return mark each keg's journey. Feed that history to a model and it can estimate where kegs are now, how long they typically dwell at each stage, and how big a float you actually need to meet demand without surplus.

The payoff is twofold. You cut lost-keg cost by flagging assets that have gone dark or overstayed, so someone can chase them. And you cut over-purchasing by sizing the fleet to real cycle times instead of worst-case guesses. Both are measurable: track lost-keg rate and average dwell time before and after, and you have a clean before-and-after to justify the spend.

This is also the kind of project where collecting your data properly comes first. If your scan discipline is patchy, fix that before buying tags — see [collecting your data before AI]({{ '/2026/collect-your-data-before-ai/' | relative_url }}). A model trained on gaps will confidently mislead you.

## A generative-AI copilot on top
Once the estimates exist, the question becomes what to do about them. This is where a generative-AI copilot helps. Instead of handing operations a spreadsheet of dwell times, a copilot can flag the kegs most likely stranded, rank them by recovery value, and draft the actions — an email to the venue, a pickup added to a route, a note for the rep. It turns analysis into a to-do list.

Crucially, the copilot drafts; a human decides. It might be wrong about a keg that is simply slow to return, so the rep's local knowledge stays in the loop. The value is speed: less time staring at data, more time recovering assets.

## Where it breaks
Two honest limits apply. First, cost and coverage: IoT tags are not free, and few breweries tag every keg, so much of the fleet is tracked only by scans — and scans only happen if someone scans. Untagged, unscanned kegs are invisible to the model.

Second, data quality. Real scan logs are messy: missed scans, duplicate events, mislabelled venues. The model can only reason about what the data captures, so coverage and accuracy cap what you can trust. Treat the output as a well-informed estimate, not a live GPS map, and your decisions will hold up.

## The bottom line
Keg fleet tracking is a strong, practical use of IoT and machine learning: it recovers stranded assets and right-sizes your float, both with hard numbers attached. Start by measuring dwell time and lost-keg rate, add a copilot to turn insight into action, and stay clear-eyed about tag cost and messy data. Done well, it pays for itself in stainless you never have to buy.

*Part of the [Sales Intelligence]({{ '/tracks/sales-intelligence/' | relative_url }}) track.*

## Frequently asked questions

**How does AI help track a keg fleet?**
It combines IoT tag pings and scan data with machine learning to estimate where kegs are, how long they have sat idle, and the float size you actually need. The aim is to cut lost-keg cost and stop you over-buying stainless.

**What is keg dwell time and why does it matter?**
Dwell time is how long a keg sits at a venue or in transit before it returns. High dwell time ties up assets you have already paid for, so reducing it lets a smaller fleet serve the same volume.

**What are the limits of keg tracking with AI?**
Tags cost money and rarely cover the whole fleet, and scan data is often messy or missing. The model can only estimate what the data lets it see, so coverage and data quality cap accuracy.
