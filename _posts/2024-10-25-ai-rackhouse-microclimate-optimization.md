---
layout: post
title: "Optimising Rackhouse Microclimate With AI"
image: /assets/og/ai-rackhouse-microclimate-optimization.png
description: "How AI and warehouse sensors map rackhouse microclimate to reduce cask-to-cask variation in extraction and angel's share, and guide smarter cask placement."
date: 2024-10-25
updated: 2024-10-25
tags: [distilling-maturation, whiskey, process-optimization]
faq:
  - q: "Can AI control the climate inside a traditional warehouse?"
    a: "Not directly in most cases. Dunnage and racked warehouses are largely passive, so AI mostly informs where you place or rotate casks rather than overriding the building's natural microclimate."
  - q: "How many sensors do I need to map a rackhouse?"
    a: "Enough to capture the spread, not every cask. A grid sampling height levels and several positions per floor usually captures the gradients that matter; you interpolate the rest."
  - q: "Does cask rotation actually even out maturation?"
    a: "It can narrow the spread between top and bottom positions, but it is laborious and the feedback loop runs over years, so model the expected gain before committing the labour."
---

**Short answer: you cannot fully control a rackhouse, but with sensors and a model you can map its microclimate and place casks to shrink cask-to-cask variation.** The building is largely passive; your leverage is knowing where the gradients are and acting on them.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the whiskey production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Optimising Rackhouse Microclimate With AI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Distil</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mature</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Bottle</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the whiskey production flow, start to finish.</figcaption>
</figure>

## Why two identical casks mature differently
Fill two casks from the same batch, set one on the top tier near the roof and one low in a corner, and you will pull two different whiskies years later. Temperature, humidity, and cask position drive extraction of oak vanillin, lactones, and tannins, and they drive the angel's share — the roughly 2% of volume lost to evaporation each year. Warm, dry spots accelerate evaporation and oak pickup; cool, humid floors slow both. Dunnage warehouses, low and earthen, stay stable; tall racked or palletised warehouses show far more spread from floor to roof. That spread is the problem a blender inherits.

## Measure first: the warehouse as a dataset
Before any model, instrument the building. Temperature and humidity loggers at multiple heights and positions, logged continuously through the seasons, turn a vague sense of "the top tier runs hot" into a quantified map. Add cask metadata — fill date, wood type, position, fill strength — and you have a feature set. Periodic sampling (ABV, colour, a few congener markers) gives you the labels that connect microclimate to outcome. The discipline is unglamorous but decisive: a model trained on a poorly sampled warehouse will confidently mislead you.

## The model: predicting variation from position
With that data, a machine-learning model can predict how a given position will affect a cask's evaporation rate and extraction trajectory. Practically, it answers two questions. First, where in this warehouse will a cask mature fastest or slowest? Second, given a target profile, where should this particular fill go? You can then place new casks deliberately and identify which existing casks sit in extreme positions and would benefit from rotation. Some distilleries already rotate casks by hand to even out maturation; the model tells you which moves are worth the effort rather than rotating on a blanket schedule.

A useful generative-AI layer sits on top. A copilot can take the model's output and produce a plain-language recommendation: "move these twelve casks from the top south tier to mid-floor north; expected effect is roughly half a percentage point less annual loss and slower tannin pickup, narrowing them toward the batch median." It explains the why, drafts the move list, and lets the warehouse team act without reading a heat map.

## Where this breaks
Be honest about the limits. A passive warehouse resists control — you are nudging placement, not setting a thermostat. Rotation is heavy manual labour, and moving full casks carries its own risk and cost. The feedback loop is brutally slow: a placement decision made today is only validated years later when you sample, so the model improves over decades, not quarters. Sensor drift, gaps in fill records, and one-off events (a hot summer, a roof repair) all inject noise. Treat the model as a decision aid that gets better with every fill cycle, not as an oracle.

## The bottom line
Rackhouse microclimate is the hidden driver of cask-to-cask variation, and you cannot manage what you have not measured. Sensors plus a placement model let you reduce that variation and curb avoidable angel's share, with a generative copilot turning predictions into a clear move list. Expect modest, compounding gains over years — not a quick fix.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.* Related: [Forecasting whiskey's angel's share]({{ '/2024/forecasting-whiskey-angels-share/' | relative_url }}).

## Frequently asked questions

**Can AI control the climate inside a traditional warehouse?**
Not directly in most cases. Dunnage and racked warehouses are largely passive, so AI mostly informs where you place or rotate casks rather than overriding the building's natural microclimate.

**How many sensors do I need to map a rackhouse?**
Enough to capture the spread, not every cask. A grid sampling height levels and several positions per floor usually captures the gradients that matter; you interpolate the rest.

**Does cask rotation actually even out maturation?**
It can narrow the spread between top and bottom positions, but it is laborious and the feedback loop runs over years, so model the expected gain before committing the labour.
