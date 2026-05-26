---
layout: post
title: "Classifying Beer Styles With Machine Learning"
image: /assets/og/classifying-beer-styles-ml.png
description: "How machine learning classifies beer styles from OG, FG, ABV, IBU and colour, where it helps QC and competition sorting, and where styles blur."
date: 2021-05-14
updated: 2021-05-14
tags: [brewing-science, machine-learning, recipe]
faq:
  - q: "What features does a beer-style classifier use?"
    a: "Mostly the measurable specs that style guidelines like BJCP define: original and final gravity, ABV, IBU, and colour in SRM or EBC, often with ingredient flags like hop variety or malt type. The model maps those numbers to a style label."
  - q: "Why does my beer get classified as two different styles?"
    a: "Because style guidelines overlap. An American pale ale and a session IPA share much of the same OG, IBU and colour space, so a beer near the boundary genuinely sits between two labels, and a good classifier reports both with probabilities."
  - q: "Can a classifier judge whether my beer is good?"
    a: "No. It judges trueness-to-type, which is whether your beer matches its declared style on paper. Quality, balance and flavour are a separate question that only a calibrated sensory panel can answer."
---

**Short answer: machine learning can label a beer's style from its core specs with useful accuracy, but the styles themselves are fuzzy, so treat the output as guidance, not a verdict.** Style classification is one of the cleanest supervised-learning problems brewing offers.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the beer production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Classifying Beer Styles With Machine Learning</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Grain</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mash</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Boil &amp; hops</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ferment</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Package</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Where this sits in the beer production flow, start to finish.</figcaption>
</figure>

## Style as a feature-mapping problem
Beer styles are defined by guidelines such as the BJCP, which specify ranges for measurable parameters: original gravity (OG), final gravity (FG), ABV, bitterness (IBU), and colour in SRM or EBC, alongside ingredient expectations and sensory descriptors. From a data-science angle this is straightforward: each beer is a point in a feature space, and classification is the task of mapping that point to the nearest style label.

Because the inputs are numbers a brewer already records, the data is cheap. Lab QC logs, competition entry forms, and recipe databases all carry OG, FG, ABV, IBU and colour. That makes style classification an unusually accessible place to start with machine learning, because you can measure first and assemble a training set from records you already keep.

## What a classifier is genuinely good for
Three jobs stand out. First, trueness-to-type QC: a classifier flags when a batch's specs have drifted away from its declared style, catching, say, an IPA that has crept down in bitterness or up in colour before it ships. Second, competition and cellar sorting: with thousands of entries, a model can pre-sort beers into likely categories and flag mislabelled entries for a human steward. Third, recipe tagging: an unlabelled recipe database can be auto-tagged so brewers can search "show me the saisons" without manual curation.

A simple model goes a long way here. Logistic regression or a small decision-tree ensemble trained on a few hundred labelled examples will separate the well-defined styles cleanly. The value is not algorithmic sophistication; it is having clean, consistently measured features and an honest, well-curated set of labels.

## A generative-AI angle: explaining the boundary
The predictive label is only half the story. A more useful tool wraps the classifier in a language model that explains *why* a beer sits where it does. Ask "why is this recipe between an American pale ale and a session IPA?" and the assistant can point to the specific features driving the ambiguity: "Your IBU of 38 and colour of 8 EBC fit a pale ale, but the dry-hop rate and 4.4% ABV pull it toward a session IPA." That turns a bare probability into a teaching moment a brewer or judge can act on, while keeping the human in charge of the final call.

## Where it breaks
Styles overlap and blur, and the guidelines are deliberately fuzzy. The boundary between many adjacent categories is a matter of intent and sensory character, not a clean line in IBU space. Hybrid and experimental beers fit nowhere by design. Specs alone also miss the aroma and flavour descriptors that often define a style, so two beers with identical numbers can belong to different categories. And the labels in your training set carry their own human bias, since they reflect how brewers chose to enter their beers, not ground truth.

The deepest limit is the same as everywhere in brewing: the model classifies measurable inputs, not taste. Trueness-to-type on paper is not the same as a beer being a good example of its style, and only a calibrated panel settles that.

## The bottom line
Classifying beer styles from OG, FG, ABV, IBU and colour is a clean, accessible machine-learning task that pays off in QC, competition sorting and recipe tagging. A generative layer can explain why a beer straddles two styles. But styles are fuzzy and specs are not flavour, so use the label as a prompt for human judgement rather than a substitute for it.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.* Related: [Predicting beer colour from a recipe]({{ '/2021/predicting-beer-colour-recipe/' | relative_url }})

## Frequently asked questions

**What features does a beer-style classifier use?**
Mostly the measurable specs that style guidelines like BJCP define: original and final gravity, ABV, IBU, and colour in SRM or EBC, often with ingredient flags like hop variety or malt type. The model maps those numbers to a style label.

**Why does my beer get classified as two different styles?**
Because style guidelines overlap. An American pale ale and a session IPA share much of the same OG, IBU and colour space, so a beer near the boundary genuinely sits between two labels, and a good classifier reports both with probabilities.

**Can a classifier judge whether my beer is good?**
No. It judges trueness-to-type, which is whether your beer matches its declared style on paper. Quality, balance and flavour are a separate question that only a calibrated sensory panel can answer.
