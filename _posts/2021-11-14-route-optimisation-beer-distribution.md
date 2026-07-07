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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The operating loop this post describes"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE OPERATING LOOP</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Route Optimisation for Beer Distribution</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Measure</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">data in</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analyse</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">find the signal</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Decide</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">choose</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Act</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">change the floor</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">repeat</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The operating loop this post describes: measure, analyse, decide, act — then repeat.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 320" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Where it happens on the ground — sites, routes and territory."><rect x="0" y="0" width="720" height="320" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">ON THE GROUND</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Route Optimisation for Beer Distribution</text><rect x="120" y="80" width="480" height="200" rx="10" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><line x1="180" y1="80" x2="180" y2="280" stroke="#d8e6e1"/><line x1="260" y1="80" x2="260" y2="280" stroke="#d8e6e1"/><line x1="340" y1="80" x2="340" y2="280" stroke="#d8e6e1"/><line x1="420" y1="80" x2="420" y2="280" stroke="#d8e6e1"/><line x1="500" y1="80" x2="500" y2="280" stroke="#d8e6e1"/><line x1="580" y1="80" x2="580" y2="280" stroke="#d8e6e1"/><line x1="120" y1="120" x2="600" y2="120" stroke="#d8e6e1"/><line x1="120" y1="180" x2="600" y2="180" stroke="#d8e6e1"/><line x1="120" y1="240" x2="600" y2="240" stroke="#d8e6e1"/><polyline points="220,150 360,200 470,130 540,240" fill="none" stroke="#00695c" stroke-width="2" stroke-dasharray="5 4"/><circle cx="220" cy="144" r="9" fill="#06483f"/><polygon points="214,148 226,148 220,158" fill="#06483f"/><circle cx="360" cy="194" r="9" fill="#06483f"/><polygon points="354,198 366,198 360,208" fill="#06483f"/><circle cx="470" cy="124" r="9" fill="#06483f"/><polygon points="464,128 476,128 470,138" fill="#06483f"/><circle cx="540" cy="234" r="9" fill="#06483f"/><polygon points="534,238 546,238 540,248" fill="#06483f"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where it happens on the ground — sites, routes and territory.</figcaption>
</figure>

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
