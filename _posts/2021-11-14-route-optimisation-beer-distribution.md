---
layout: post
title: "Route Optimisation for Beer Distribution"
image: /assets/og/route-optimisation-beer-distribution.png
description: "How vehicle-routing optimisation cuts miles, cost and emissions on beer deliveries under time windows and capacity, and where real-world chaos limits it."
date: 2021-11-14
updated: 2021-11-14
tags: [commercial-planning, logistics, process-optimization]
faq:
  - q: "What is route optimisation for beer distribution?"
    a: "It is solving the vehicle-routing problem: deciding which van visits which bars and retailers, in what order, subject to time windows, vehicle capacity and drop constraints. The goal is fewer miles, lower cost and lower emissions."
  - q: "Can routes re-optimise when orders change?"
    a: "Yes. When a new order lands or one is cancelled, the optimiser can recompute the plan rather than forcing dispatch to patch it by hand. That responsiveness is much of the value."
  - q: "Why can't an optimiser replace dispatchers and drivers?"
    a: "Because the model does not see everything — live traffic, awkward access, a delivery that must reach a venue before service. Driver and dispatcher knowledge handles the chaos the data misses."
---

**Short answer: route optimisation solves the vehicle-routing problem for beer deliveries — fewer miles, lower cost and lower emissions under real-world constraints.** It is one of the most quantifiable analytics wins in distribution, provided you respect the limits of the map.

## The vehicle-routing problem, in beer terms
Distributing beer is a textbook vehicle-routing problem dressed in a brewery's clothes. You have a fleet of vans and a list of drops — bars, restaurants, off-licences and retailers — each with its own demands. Some venues only accept deliveries inside a time window. Each vehicle has a finite capacity in kegs and cases. Some drops have access or sequencing constraints. The task is to assign drops to vehicles and order them to minimise total distance and time.

Solve that well and the savings are direct: fewer miles driven means lower fuel cost, lower emissions, and more drops completed per shift. Unlike fuzzier analytics, this one comes with a tidy objective function, which makes the business case easy to measure and defend.

## Measure first, then optimise
The discipline here is the same as any analytics project: measure before you optimise. Capture your current routes, miles, cost per drop and time-window compliance for a representative period. That baseline is what proves the optimiser earned its keep — and it often reveals the easy wins before any algorithm runs, such as venues clustered badly across routes.

The real edge is responsiveness. Static weekly routes go stale the moment an order changes. A modern optimiser re-optimises when orders are added, cancelled or resized, so the plan reflects today's reality rather than last Monday's. That dynamic re-planning is where much of the saving lives, because demand in hospitality is rarely tidy.

Keg logistics and delivery routing reinforce each other, too: a route can fold in keg pickups as well as drops, so empties come home faster. If you are tracking your fleet, see [AI for keg fleet tracking and optimisation]({{ '/2021/ai-keg-fleet-tracking/' | relative_url }}) for the asset side of the same coin.

## A generative-AI layer for dispatch
Optimisers are notoriously opaque — they hand back a plan with no explanation, and dispatchers distrust what they cannot interrogate. A generative-AI assistant closes that gap. When the route changes, it can explain, in plain language, why: "this venue moved earlier to meet its noon window, so the two nearby drops shifted to the afternoon van."

That narration does two things. It builds trust, so dispatch follows the plan instead of overriding it on instinct. And it speeds up the human override when one is genuinely needed, because the dispatcher understands the trade-off they are breaking. The assistant explains the decision; it does not make it.

## Where it breaks
The honest limit is that the map is not the territory. An optimiser works from the constraints you give it, and the real world supplies ones you did not: a motorway closure, a loading bay blocked, a publican who is never there before eleven, a one-way system the data does not know. Live traffic helps but never fully captures the chaos.

This is why driver and dispatcher knowledge stays essential. Drivers know which back entrance to use and which landlord signs at the bar. The optimiser produces an excellent starting plan; humans adapt it to the day. Treat it as decision support — a strong default that frees people to handle exceptions — rather than an autopilot, and it delivers.

## The bottom line
Route optimisation is among the clearest analytics wins in beer distribution: a well-defined problem with measurable savings in miles, cost and emissions, plus the agility to re-plan as orders shift. Baseline first, add a generative-AI layer so dispatch trusts the output, and keep human judgement in the loop for the chaos no model can see.

*Part of the [Commercial Planning Analytics]({{ '/tracks/commercial-planning/' | relative_url }}) track.*

## Frequently asked questions

**What is route optimisation for beer distribution?**
It is solving the vehicle-routing problem: deciding which van visits which bars and retailers, in what order, subject to time windows, vehicle capacity and drop constraints. The goal is fewer miles, lower cost and lower emissions.

**Can routes re-optimise when orders change?**
Yes. When a new order lands or one is cancelled, the optimiser can recompute the plan rather than forcing dispatch to patch it by hand. That responsiveness is much of the value.

**Why can't an optimiser replace dispatchers and drivers?**
Because the model does not see everything — live traffic, awkward access, a delivery that must reach a venue before service. Driver and dispatcher knowledge handles the chaos the data misses.
