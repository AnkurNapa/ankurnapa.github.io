---
layout: post
title: "Predicting Hop Bitterness (IBU) With Machine Learning"
image: /assets/og/predicting-hop-bitterness-ibu.png
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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Predicting Hop Bitterness (IBU) With Machine Learning</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

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

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives hopping, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Predicting Hop Bitterness (IBU) With Machine Learning</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Hopping</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">quality</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">What drives hopping, and what it changes downstream.</figcaption>
</figure>

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
