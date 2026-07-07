---
layout: post
title: "Can AI Pick Distillation Cut Points (Heads, Hearts, Tails)?"
image: /assets/og/predicting-distillation-cut-points-ai.png
description: "Can AI choose distillation cut points? How models use ABV, temperature, time and congener data to make heads, hearts and tails cuts more consistent."
date: 2024-08-11
updated: 2024-08-11
tags: [distilling-maturation, whiskey, process-optimization]
faq:
  - q: "Can AI replace the stillman's nose?"
    a: "No. A model can recommend a cut point from ABV, temperature, time and congener signals, but sensory judgement remains the arbiter. Treat it as a second opinion that improves consistency, not a replacement."
  - q: "What data do I need to model cut points?"
    a: "At minimum, logged ABV, temperature and time across the spirit run, with each batch labelled by where the stillman actually cut. Inline spectroscopy or congener sensors help but are not essential to start."
  - q: "Does this work for column stills as well as pot stills?"
    a: "The idea transfers, but the problem differs. Pot still cuts are batch decisions on a falling ABV; column stills run continuously, so the model targets steady-state draw points rather than discrete heads, hearts and tails cuts."
---

**Short answer: yes, a model can recommend where to cut, but only as a disciplined second opinion to a stillman who still trusts the nose.** The cut defines house character, so the goal is consistency, not autonomy.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the whiskey production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Can AI Pick Distillation Cut Points (Heads, Hearts, Tails)?</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Distil</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mature</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Bottle</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the whiskey production flow, start to finish.</figcaption>
</figure>

## What the cut actually decides
The spirit run is split into three parts. Foreshots and heads come first: high in ABV, volatile, carrying low-boiling congeners, methanol, acetaldehyde and light esters you do not want. The heart, the middle cut, is the keeper, collected from a high ABV down to roughly 60-65% ABV in a pot still. Feints and tails come last: low in ABV, heavy with fusel oils and oily congeners.

Today those cut points are set by the stillman on ABV, temperature, time and nose. That works, but it travels poorly. A new operator, a tired shift, or a slightly different wash nudges the cut, and the new-make drifts. Cut consistency is a measurable quality problem hiding inside a craft decision.

## Where a model helps
Measure first. The features are already on the still: ABV through the run, vapour and spirit temperature, elapsed time, and the shape of how ABV falls. Label each historical batch with where the cut was actually made and how the resulting new-make scored on the bench and at the nose. A supervised model then learns the relationship between the run's trajectory and a good cut.

The payoff is repeatability. Instead of every stillman drawing on private rules of thumb, the model encodes the distillery's own best cuts and flags when a run is heading off its usual path. Where budget allows, inline spectroscopy or congener sensors sharpen the signal, letting the model react to actual chemistry rather than ABV as a proxy. That matters most at the back end, where the line between a clean heart and fusel-laden tails is thin.

For continuous operations the framing changes. A column still does not make discrete heads, hearts and tails cuts; it draws at steady state. There the model optimises draw plates and reflux to hold a target congener profile rather than calling a single cut moment.

## Where it breaks
Be honest about the limits. The nose still matters: some off-notes, particularly sulphur and certain esters, are caught by a trained human long before any affordable sensor sees them. Spectroscopy and congener analysers are expensive, and many distilleries simply do not have them inline. Most importantly, the cut is where house character is made. A model trained on last year's cuts will faithfully reproduce last year's style, including its flaws, and a confident-but-wrong recommendation on a high-value run is costly. Keep the human with the final say, and validate against sensory before trusting any automated cut.

There is also a cold-start problem. With only a handful of labelled runs the model has little to learn from, and rare events, an unusually slow ferment, a copper fault, are underrepresented precisely when guidance would help most.

## A generative angle worth having
The most useful generative AI here is a copilot, not an autopilot. Picture an assistant that watches the run, recommends a cut point, and explains the trade-off in plain language: "Cutting now keeps a fruitier, ester-forward heart but sacrifices around two litres of yield; holding 90 seconds adds body at the risk of early fusel carry-over." That explanation is what turns a model into a training tool. New stillmen learn faster when the reasoning is spelled out, and the distillery captures its tacit knowledge instead of losing it when an experienced operator retires.

The cut you make on the still shapes everything downstream, so it pays to connect this to how you [predict new-make spirit flavour]({{ '/2024/predicting-new-make-spirit-flavor/' | relative_url }}) and steer character before the spirit ever reaches a cask.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Can AI Pick Distillation Cut Points (Heads, Hearts, Tails)?</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Process</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

## The bottom line
AI can make cut points more consistent and turn an experienced stillman's judgement into a shared, teachable standard. It cannot, and should not, take the decision away from the person holding the glass. Start by logging your runs and labelling your cuts; the model is the easy part.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.*

## Frequently asked questions

**Can AI replace the stillman's nose?**
No. A model can recommend a cut point from ABV, temperature, time and congener signals, but sensory judgement remains the arbiter. Treat it as a second opinion that improves consistency, not a replacement.

**What data do I need to model cut points?**
At minimum, logged ABV, temperature and time across the spirit run, with each batch labelled by where the stillman actually cut. Inline spectroscopy or congener sensors help but are not essential to start.

**Does this work for column stills as well as pot stills?**
The idea transfers, but the problem differs. Pot still cuts are batch decisions on a falling ABV; column stills run continuously, so the model targets steady-state draw points rather than discrete heads, hearts and tails cuts.
