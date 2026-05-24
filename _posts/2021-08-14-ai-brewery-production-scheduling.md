---
layout: post
title: "AI for Brewery Production Scheduling"
description: "How optimisation and forecasting plan the brew, ferment, and package schedule across finite tanks, maturation times, and line slots to hit due dates."
date: 2021-08-14
updated: 2021-08-14
tags: [brewing-science, planning, process-optimization]
faq:
  - q: "Why is brewery scheduling a hard problem for software?"
    a: "A brewery is a constrained job-shop with finite tanks, fermentation and maturation that take days to weeks, limited packaging-line slots, and mandatory CIP windows. The number of valid plans explodes quickly, so finding one that hits every due date and keeps tanks turning is well beyond a spreadsheet for any sizeable site."
  - q: "What does the optimiser actually decide?"
    a: "It decides what to brew, when, in which vessel, and when to package — subject to all your constraints. The goal is usually to meet due dates while maximising tank turns and minimising idle capacity and changeovers, given a demand forecast for the weeks ahead."
  - q: "How accurate do my process durations need to be?"
    a: "Quite accurate. The schedule is only as good as its assumptions, so if fermentation and maturation times are guesses, the plan will be optimistic and brittle. Track actual durations per beer style and feed the real numbers back in before you trust the optimiser."
---

**Short answer: brewery scheduling is a classic constrained job-shop, and optimisation paired with demand forecasting plans what to brew when so you hit due dates and squeeze more turns out of finite tanks.** Most breweries still do this in a spreadsheet and a planner's head. That works until it doesn't.

## The brewery as a job-shop
Think about what a schedule has to respect. Tanks are finite and each beer occupies one for the duration of its fermentation and maturation — days to weeks, not minutes. Packaging lines have limited slots. CIP windows have to fit between fills. Some styles can only go in certain vessels. Every one of these is a hard constraint, and the planner has to satisfy all of them at once while still shipping orders on time.

This is precisely the shape of problem operations research has tackled for decades. An optimiser searches the space of valid plans and returns one that meets due dates while maximising a goal you choose — typically tank turns or capacity utilisation — and minimising idle vessels and changeovers. The "AI" here is mostly mathematical optimisation, often paired with a forecasting model that estimates demand for the coming weeks so you are planning against likely orders rather than yesterday's.

For a broader picture of where this sits among brewery use cases, see [what AI can do for a brewery]({{ '/2026/what-can-ai-do-for-a-brewery/' | relative_url }}).

## Measure first: the model is only as good as your durations
Before any optimiser earns its keep, you have to feed it the truth. That means accurate fermentation and maturation durations per style, realistic CIP and turnaround times, and honest line throughput. Most planners carry these numbers in their heads, where they cannot be optimised against.

The discipline is the same as everywhere else in analytics: measure the process first. Pull actual batch durations from your records, look at the spread rather than just the average, and feed the real distributions in. A plan built on optimistic durations looks brilliant on screen and falls apart in the cellar.

## Where it breaks
Three honest limits. First, demand is uncertain. The forecast driving the plan will be wrong to some degree, and a schedule optimised perfectly against a wrong forecast is still wrong. Second, the plan is brittle to disruption. A stuck fermentation, a packaging breakdown, or a late ingredient delivery can invalidate a tightly packed schedule, and the more aggressively you optimise for tank turns the less slack you leave to absorb shocks. Third, it all rests on accurate durations — get those wrong and the whole edifice is shaky.

The practical lesson is to optimise for a *robust* plan, not a theoretically perfect one. Leave a little headroom, and treat the schedule as something you re-run when reality moves, not a one-shot answer carved in stone.

## A practical gen-AI angle
Re-planning is where generative AI helps. When a tank slips by a day, a planner does not want to learn the optimiser's input format — they want to say "FV4 won't be free until Thursday, what changes?" An LLM assistant sitting on top of the optimiser can take that plain-language update, re-trigger the solve, and explain the new plan: which batches moved, which due dates are now at risk, and what the trade-off was. It makes a powerful but fiddly tool usable on the cellar floor. The caveat is that the LLM must call the real optimiser and report its real output — it should never invent a schedule of its own.

## The bottom line
Production scheduling is one of the clearest wins for optimisation in a brewery, turning a finite-tank juggling act into a plan that hits due dates and maximises turns. But it demands accurate process durations, copes badly with disruption if you optimise too aggressively, and rests on an inherently uncertain demand forecast. Build robustness in, re-plan when reality shifts, and use a gen-AI assistant to make re-planning effortless rather than to replace the maths.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*

## Frequently asked questions

**Why is brewery scheduling a hard problem for software?**
A brewery is a constrained job-shop with finite tanks, fermentation and maturation that take days to weeks, limited packaging-line slots, and mandatory CIP windows. The number of valid plans explodes quickly, so finding one that hits every due date and keeps tanks turning is well beyond a spreadsheet for any sizeable site.

**What does the optimiser actually decide?**
It decides what to brew, when, in which vessel, and when to package — subject to all your constraints. The goal is usually to meet due dates while maximising tank turns and minimising idle capacity and changeovers, given a demand forecast for the weeks ahead.

**How accurate do my process durations need to be?**
Quite accurate. The schedule is only as good as its assumptions, so if fermentation and maturation times are guesses, the plan will be optimistic and brittle. Track actual durations per beer style and feed the real numbers back in before you trust the optimiser.
