---
layout: post
title: "AI for Brewery Workforce and Shift Scheduling"
image: /assets/og/ai-brewery-workforce-shift-scheduling.png
description: "How optimisation matches brewery labour to the production plan under skills, availability, and labour rules — and why people aren't widgets."
date: 2022-08-14
updated: 2022-08-14
tags: [brewing-science, planning, process-optimization]
faq:
  - q: "How is workforce scheduling different from production scheduling?"
    a: "Production scheduling decides what to brew and when; workforce scheduling decides who works when to deliver that plan. It takes the production and packaging schedule as an input and matches labour to it, subject to skills, availability, and labour rules. The two are linked — the roster is only as good as the production plan it serves."
  - q: "What constraints does a roster optimiser handle?"
    a: "Skills matching, so the right qualified people cover each task; availability, including leave and part-time patterns; and labour rules such as maximum hours, minimum rest, and break entitlements. On top of those hard rules, it can weigh softer goals like fairness and preference, which is where the real difficulty lies."
  - q: "Can it forecast how many people I'll need?"
    a: "Yes. Because the production schedule implies a workload — brews, packaging runs, CIP cycles — you can forecast labour demand from it and roster against the expected load rather than a flat headcount. That said, the forecast inherits any uncertainty in the production plan it is built on."
---

**Short answer: optimisation can match labour to your brew and packaging plan under skills, availability, and labour rules, and forecast how many people each shift needs — but people are not widgets, and the soft constraints are where it gets hard.** Rostering is one of the most time-consuming jobs a brewery manager does. It is also a well-shaped optimisation problem.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">AI for Brewery Workforce and Shift Scheduling</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Package</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## From production plan to labour plan
Workforce scheduling does not start from scratch; it starts from the production schedule. Once you know what is being brewed, packaged, and cleaned over the coming weeks, you know the workload that implies. From there, forecasting turns the plan into a labour demand — how many people, with which skills, at which times — and an optimiser assigns staff to shifts to meet it.

The hard constraints are familiar to any manager filling a rota by hand: only qualified staff can run certain equipment, people have availability and leave, and labour rules cap hours, mandate rest, and protect breaks. Doing this manually for a busy site is slow and error-prone. An optimiser can satisfy all those rules at once and produce a feasible roster in seconds — which is genuinely useful, because the manual version eats hours and still slips up.

Because the roster depends entirely on the production plan, it is worth getting that right first; [AI for brewery production scheduling]({{ '/2021/ai-brewery-production-scheduling/' | relative_url }}) covers the upstream decision that drives the workload here.

## Measure first: model the real workload
The optimiser is only as good as its picture of the work. That means measuring how long tasks actually take, which skills each role genuinely requires, and how workload varies across the week — not assuming a flat, tidy demand. The discipline is the same as everywhere in this track: measure the process before you model it.

If your labour-demand forecast assumes every brew day looks identical, the roster will be wrong on the days that matter — the heavy packaging run, the double CIP, the awkward changeover. Capture the real variation in workload and the optimiser can staff to it. Skip that step and you will roster the average and be short-handed exactly when it counts.

## Where it breaks
This is the application where the honest limits matter most, because the "resources" being scheduled are people. Labour rules are genuinely complex and vary by contract and jurisdiction; encoding them correctly is real work, and an optimiser that gets them wrong creates compliance risk, not efficiency.

Harder still is fairness. A roster that is mathematically optimal for cost or coverage can be deeply unpopular if it dumps every awkward shift on the same people. Fairness, preference, and morale are soft constraints that resist clean formulation, and over-optimising for the hard numbers while ignoring them is a fast route to resentment and churn. People are not widgets; a roster that treats them as interchangeable units will technically work and quietly fail. The optimiser should propose, and a manager who knows the team should decide.

## A practical gen-AI angle
Generative AI fits as an explainer and drafter on top of the optimiser. It can produce a compliant draft roster and, crucially, explain the trade-offs in plain language — "this rota keeps everyone within hours but gives Sam three late shifts; swapping with Priya balances it but needs the forklift ticket she has and Sam doesn't." That makes the soft, human judgement easier, because the manager can see *why* the optimiser chose what it did and adjust with full sight of the consequences. As ever, it must reason over the real availability and rules, and the final call stays with a person.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">AI for Brewery Workforce and Shift Scheduling</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Process</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

## The bottom line
Workforce scheduling is a strong optimisation fit: it takes your production plan, forecasts the labour it implies, and builds a rule-compliant roster far faster than doing it by hand. But labour rules are intricate and fairness resists formulae, so this is the application where you most need a human in the loop. Measure the real workload, encode the rules carefully, let the optimiser propose and a gen-AI assistant explain — and let a manager who knows the team make the final call.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*

## Frequently asked questions

**How is workforce scheduling different from production scheduling?**
Production scheduling decides what to brew and when; workforce scheduling decides who works when to deliver that plan. It takes the production and packaging schedule as an input and matches labour to it, subject to skills, availability, and labour rules. The two are linked — the roster is only as good as the production plan it serves.

**What constraints does a roster optimiser handle?**
Skills matching, so the right qualified people cover each task; availability, including leave and part-time patterns; and labour rules such as maximum hours, minimum rest, and break entitlements. On top of those hard rules, it can weigh softer goals like fairness and preference, which is where the real difficulty lies.

**Can it forecast how many people I'll need?**
Yes. Because the production schedule implies a workload — brews, packaging runs, CIP cycles — you can forecast labour demand from it and roster against the expected load rather than a flat headcount. That said, the forecast inherits any uncertainty in the production plan it is built on.
