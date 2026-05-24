---
layout: post
title: "Controlling Dissolved Oxygen in Beer With Machine Learning"
description: "How machine learning pinpoints dissolved oxygen pickup and predicts package TPO, so you control the biggest driver of beer staling at the source."
date: 2024-01-11
updated: 2024-01-11
tags: [brewing-science, quality-control, oxygen]
faq:
  - q: "What is a good total package oxygen target?"
    a: "Most breweries chasing flavour stability aim for total package oxygen in the tens of ppb, commonly below 50-100 ppb. The exact target depends on style and shelf-life expectations, but lower is almost always better."
  - q: "Can machine learning replace inline DO meters?"
    a: "No. ML predicts and explains, but it needs real measurements to learn from. Inline DO instrumentation at transfer, filtration, and filling is the foundation; the model sits on top of it."
  - q: "Where does most oxygen pickup happen?"
    a: "Usually at three points: tank-to-tank transfer, filtration, and filling. Pickup tends to be intermittent rather than constant, which is exactly why pattern-finding models help."
---

**Short answer: machine learning won't lower your oxygen for you, but it will tell you exactly where you are picking it up and predict the package TPO a given run will produce.** That turns staling from a post-mortem into something you manage at the source.

## Why oxygen is the quiet flavour killer
Post-fermentation oxygen pickup is the enemy of flavour stability. Once beer is fermented, dissolved oxygen drives oxidative staling reactions that flatten hop character and push the cardboard, sherry-like notes drinkers notice within weeks. The painful part is that pickup is invisible at the moment it happens. You only taste the consequence later, on a shelf, in someone else's hand.

Total package oxygen (TPO) — the dissolved plus headspace oxygen in the finished container — is the number that correlates with shelf life. Serious breweries hold TPO in the tens of ppb, often below 50-100 ppb. Hitting that consistently is a process control problem, not a recipe problem.

## Measure first: the data that makes a model possible
There is no shortcut around instrumentation. Inline DO meters at transfer, filtration, and filling give you the readings; without them, any model is guessing. The data-science job is to turn those readings into features that explain variation: transfer flow rate and counter-pressure, filter differential pressure, filler speed, headspace fill, CO2 purge timing, even ambient factors during changeovers.

With a few weeks of run data tagged to final TPO, you can fit a model that predicts package oxygen from process settings before the beer is packaged. More usefully, the same model attributes the predicted TPO across steps — showing that, say, 60% of a high reading traces to filling and most of the rest to a particular transfer. That attribution is where the value sits, because pickup is intermittent: the model surfaces the conditions under which a normally fine line suddenly leaks oxygen.

## A copilot for the corrective action
This is the natural home for a generative-AI assistant. When a TPO result comes back high, a copilot can read the run's sensor trace, compare it against the model's attribution, and write a plain-language explanation: "TPO 140 ppb, ~70% attributable to the filler — fill heights ran low on heads 3 and 7 during the changeover at 14:20; CO2 purge was 1.2 s short of target." It then drafts the corrective action and the deviation note for sign-off.

That saves the engineer the forensic slog through logs and, more importantly, captures the reasoning so the next operator inherits it rather than rediscovering it.

## Where it breaks
Be honest about the limits. The model is only as good as the DO instrumentation feeding it — drifting or poorly maintained meters produce confident nonsense. Because pickup is intermittent, rare spike events are under-represented in training data, so the model can miss the exact failure mode you most want to catch until it has seen a few examples. And ML explains correlation, not mechanism: it points you to the filler, but a human still has to find the worn seal. Treat predictions as a prioritised investigation list, not a verdict.

## The bottom line
Control TPO at the source by instrumenting transfer, filtration, and filling, then let a model predict package oxygen and attribute it to the worst step. Add a copilot to explain results and draft corrective actions. The technology amplifies good measurement; it cannot substitute for it.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [minimising total package oxygen]({{ '/2024/minimizing-total-package-oxygen-tpo/' | relative_url }}) and [predicting flavour stability and staling]({{ '/2023/predicting-beer-flavor-stability-staling/' | relative_url }}).

## Frequently asked questions

**What is a good total package oxygen target?**
Most breweries chasing flavour stability aim for total package oxygen in the tens of ppb, commonly below 50-100 ppb. The exact target depends on style and shelf-life expectations, but lower is almost always better.

**Can machine learning replace inline DO meters?**
No. ML predicts and explains, but it needs real measurements to learn from. Inline DO instrumentation at transfer, filtration, and filling is the foundation; the model sits on top of it.

**Where does most oxygen pickup happen?**
Usually at three points: tank-to-tank transfer, filtration, and filling. Pickup tends to be intermittent rather than constant, which is exactly why pattern-finding models help.
