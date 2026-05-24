---
layout: post
title: "Predicting Hop Bitterness (IBU) With Machine Learning"
description: "Machine learning predicts IBU and hop utilisation from lot alpha-acid assay and boil conditions, compensating for hop lot drift across crop years."
date: 2023-02-25
updated: 2023-02-25
tags: [brewing-science, hops, machine-learning]
faq:
  - q: "What inputs does an IBU prediction model need?"
    a: "The hop lot's measured alpha-acid content plus the boil conditions — time, vigour, wort gravity, pH and the timing of each addition. Without a lot-specific alpha-acid assay, the model is largely guessing."
  - q: "Why does utilisation matter so much?"
    a: "Bitterness comes from iso-alpha-acids formed by isomerising alpha-acids in the boil, and utilisation is only around 30 percent. It falls at higher wort gravity, rises with longer boils and higher pH, and is far lower for late or whirlpool additions."
  - q: "Can the model predict perceived bitterness, not just IBU?"
    a: "Not reliably. Measured IBU and what a drinker perceives diverge, especially with heavy dry-hopping, so treat predicted IBU as a process target rather than a promise about taste."
---

**Short answer: machine learning predicts IBU and hop utilisation well when you feed it a lot-specific alpha-acid assay plus the boil conditions — and its real value is compensating for hop lot drift across crop years and scale changes.** Without that assay, you are guessing; with it, the model turns a notoriously variable input into a controllable one.

## What you are actually predicting
Bitterness is chemistry, not magic. Iso-alpha-acids, the bitter compounds, form when the alpha-acids in hops isomerise during the boil. The catch is utilisation: only about 30 percent of the available alpha-acids convert, and that figure moves. It falls as wort gravity rises, climbs with longer and more vigorous boils and higher pH, and drops sharply for late and whirlpool additions, which spend little time hot enough to isomerise much at all.

So predicting IBU means predicting utilisation under your specific conditions and multiplying through by the alpha-acids you actually added. A model trained on past batches — alpha-acid assay, boil time, vigour, gravity, pH, addition schedule, measured IBU — learns the utilisation surface across all those variables at once, which beats a single textbook utilisation factor applied uniformly.

## The problem it really solves: lot drift
The headline use is not squeezing out a more precise number on a stable recipe. It is dealing with hops that refuse to stay constant. Hops vary lot to lot by crop year, growing region and storage history, so the same variety can arrive at meaningfully different alpha-acid levels season to season. A recipe written for last year's lot will miss target this year if you dose by weight and hope.

A trained model closes that gap. Given this lot's measured alpha-acids, it tells you how much to add to land on the same IBU as last time, and how the answer shifts if you scale the batch or change the boil. That is recipe and scale transfer — keeping a beer consistent through ingredient variation, which is exactly the discipline behind designing a stable recipe in the first place, as in [can AI design a beer recipe]({{ '/2026/can-ai-design-a-beer-recipe/' | relative_url }}).

## Where it breaks
The hard limit is at the input. No lot-specific alpha-acid assay means no real prediction — the model falls back to variety averages and inherits all the lot drift you were trying to remove. The discipline is therefore to assay each lot, or at least each delivery, and to keep that paired history clean. Measure first, predict second.

The softer limit is perception. Measured IBU and perceived bitterness are not the same thing, and the gap widens with heavy late and dry-hop additions, where polyphenols, oils and biotransformation muddy what the drinker tastes. Dry-hopping adds almost no measured IBU yet changes perceived bitterness, so an IBU model says little about the finished impression of a hop-forward beer. Treat predicted IBU as a process target you can hold steady, not a guarantee of how bitter a beer will seem.

## A copilot for the missed batch
Two generative-AI angles fit. The first is explanation. When a batch lands off target IBU, a language-model copilot can read the batch record against the model and write the diagnosis in plain terms: "IBU came in 6 below target — your bittering lot assayed 9.8 percent alpha versus the 11 percent the recipe assumed, and the boil ran ten minutes short, so utilisation was lower than usual." That turns a frustrating miss into a learnable cause an operator can fix next time.

The second is data augmentation. IBU history is often sparse — you have not boiled every gravity at every pH for every addition schedule. Generating synthetic but physically plausible boil scenarios, sampled around your real data, can fill thin regions of the utilisation surface and steady the model, provided the synthetic points respect the known chemistry and are validated against any real batches you do run at those settings.

## The bottom line
Build IBU prediction as a lot-drift compensator: assay every hop lot, train on your own boil history, and use the model to keep bitterness constant through ingredient and scale changes. Lean on a copilot to explain misses and synthetic scenarios to cover gaps, but never confuse a steady IBU number with steady perceived bitterness — especially in hop-forward beer. For the aroma side of the same problem, see [AI for hop aroma profiling and substitution]({{ '/2023/ai-hop-aroma-profiling-substitution/' | relative_url }}).

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*

## Frequently asked questions

**What inputs does an IBU prediction model need?**
The hop lot's measured alpha-acid content plus the boil conditions — time, vigour, wort gravity, pH and the timing of each addition. Without a lot-specific alpha-acid assay, the model is largely guessing.

**Why does utilisation matter so much?**
Bitterness comes from iso-alpha-acids formed by isomerising alpha-acids in the boil, and utilisation is only around 30 percent. It falls at higher wort gravity, rises with longer boils and higher pH, and is far lower for late or whirlpool additions.

**Can the model predict perceived bitterness, not just IBU?**
Not reliably. Measured IBU and what a drinker perceives diverge, especially with heavy dry-hopping, so treat predicted IBU as a process target rather than a promise about taste.
