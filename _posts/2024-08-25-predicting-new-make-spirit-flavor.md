---
layout: post
title: "Predicting New-Make Spirit Flavour"
image: /assets/og/predicting-new-make-spirit-flavor.png
description: "How AI and data science model new-make spirit congeners from ferment, still shape and cut, so distillers steer flavour before the cask."
date: 2024-08-25
updated: 2024-08-25
tags: [distilling-maturation, whiskey, flavor]
faq:
  - q: "What drives new-make spirit flavour?"
    a: "Congeners do: esters give fruitiness, higher alcohols give body, and aldehydes and sulphur compounds give green or savoury notes. These are shaped by ferment length, still shape and reflux, copper contact, and where you cut the spirit run."
  - q: "Can a model really predict flavour before distillation?"
    a: "It can predict the chemical congener profile reasonably well from process inputs, and that profile correlates with flavour. But sensory tasting remains the final judge, because perception is not a simple sum of compounds."
  - q: "How much historical data do I need to start?"
    a: "Enough labelled batches to cover your normal range of ferment lengths, still settings and cuts, ideally with both GC analysis and tasting scores. A few dozen well-recorded batches beats hundreds of poorly logged ones."
---

**Short answer: a model can predict the congener profile of your new-make from process inputs, letting you steer character before the spirit ever sees a cask.** Sensory tasting still confirms the result, but you stop flying blind.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the whiskey production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Predicting New-Make Spirit Flavour</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Distil</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mature</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Bottle</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the whiskey production flow, start to finish.</figcaption>
</figure>

## Flavour is set before the cask
It is tempting to treat maturation as where flavour is made, but the new-make spirit arrives at the cask already carrying its DNA. That DNA is congeners: esters for fruity notes, higher or fusel alcohols for body and weight, aldehydes for green and grassy character, and sulphur compounds for savoury or meaty notes that copper contact later strips out. Get the new-make wrong and no cask will fully rescue it.

Those congeners are not random. They respond to levers you already pull. Long ferments push more esters and a fruitier spirit. Still shape and the degree of reflux decide how much heavy material carries over: tall necks and high reflux make a lighter, cleaner spirit. Copper contact removes sulphur. And the cut, where you draw the heart of the run, sets the balance of light and heavy congeners in the final spirit.

## Modelling the levers
The data-science move is to make those levers explicit features and the congener profile the target. Measure first: log ferment duration and temperature, still geometry and reflux conditions, copper exposure, and cut points for each batch. Pair every batch with a GC analysis of its congeners and, crucially, a sensory score.

A regression or gradient-boosted model then learns how inputs map to outputs. Ask it what happens if you extend the ferment by twelve hours, or cut a touch earlier, and it estimates the shift in ester and fusel levels. That turns flavour from something you discover after the fact into something you target on purpose. For a distillery trying to hold a house style across seasons and feedstock variation, that predictability is worth more than any single clever recipe.

This sits directly downstream of how you set the cut. The same heart-cut decision that drives consistency also moves the congener balance, which is why it pays to model the two together; see [picking distillation cut points]({{ '/2024/predicting-distillation-cut-points-ai/' | relative_url }}).

## Where the model gets it wrong
The honest limit is interaction. Congener formation is a web of coupled chemistry and biology, not a set of independent dials. A change to ferment length interacts with yeast health, which interacts with still loading, which interacts with the cut. Models capture the strong, repeated patterns; they struggle with the rare combinations they have never seen, and they will happily extrapolate past your actual operating range with false confidence.

Then there is perception. Flavour is not the arithmetic sum of compounds. Two spirits with near-identical GC profiles can taste different, and a model that predicts chemistry is not predicting the verdict of the panel. Treat the predicted profile as a strong hypothesis and let the tasting confirm it. Where the model adds clear value is narrowing the search and flagging batches drifting off-style early, not declaring a spirit good.

## Asking the model in plain English
The generative angle flips the usual direction. Instead of feeding settings in and reading a profile out, a generative assistant lets you state the goal: "What wash and still settings give me an ester-forward, lightly sulphury new-make at this ABV?" The model then proposes candidate ferment lengths, reflux conditions and cut points that land near the target, with the trade-offs noted. It is a design tool, exploring the recipe space far faster than trial batches, while you keep the final say on which candidate is worth actually distilling.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="What drives maturation, and what it changes downstream."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WHAT DRIVES IT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Predicting New-Make Spirit Flavour</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">input 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Maturation</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">quality</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">cost / risk</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">What drives maturation, and what it changes downstream.</figcaption>
</figure>

## The bottom line
You can predict and steer new-make flavour from the inputs you already control, provided you measure congeners and taste consistently. The model narrows the options and catches drift; the panel still calls the spirit. Build the data habit first, because the prediction is only as good as the batches you logged.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.*

## Frequently asked questions

**What drives new-make spirit flavour?**
Congeners do: esters give fruitiness, higher alcohols give body, and aldehydes and sulphur compounds give green or savoury notes. These are shaped by ferment length, still shape and reflux, copper contact, and where you cut the spirit run.

**Can a model really predict flavour before distillation?**
It can predict the chemical congener profile reasonably well from process inputs, and that profile correlates with flavour. But sensory tasting remains the final judge, because perception is not a simple sum of compounds.

**How much historical data do I need to start?**
Enough labelled batches to cover your normal range of ferment lengths, still settings and cuts, ideally with both GC analysis and tasting scores. A few dozen well-recorded batches beats hundreds of poorly logged ones.
