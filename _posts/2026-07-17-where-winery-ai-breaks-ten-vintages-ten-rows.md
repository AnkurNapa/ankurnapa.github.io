---
layout: post
title: "Where Winery AI Breaks: Ten Vintages Is Ten Rows"
image: /assets/og/where-winery-ai-breaks-ten-vintages-ten-rows.png
description: "Part 6 of The Cellar Ledger. A brewery brews hundreds of batches a year. A winery gets one vintage. Why models that predict vintage outcomes overfit, where winery data is actually rich, and what time-series foundation models, synthetic data and LLMs can and cannot do about a small-data problem."
date: 2026-07-17 09:00:00 -0700
updated: 2026-07-17
tags: [winemaking, cellar-ledger, machine-learning, generative-ai, data-strategy]
faq:
  - q: "Why is machine learning harder in a winery than in a brewery?"
    a: "Because the unit of learning is often the vintage, and a winery gets one a year. Ten years of history gives ten rows per block for questions like harvest date, yield or quality score, while a brewery making hundreds of batches a year has thousands. Models trained on ten rows mostly memorise the past rather than learn from it."
  - q: "Can synthetic data or a foundation model fix a small winery dataset?"
    a: "Not on its own. Synthetic data made from your ten vintages contains no information your ten vintages did not already have. Time-series foundation models can give a reasonable zero-shot forecast of a curve, such as a fermentation, but they know nothing about your vineyard. Both are useful inside a sound design, and neither creates the missing history."
  - q: "Where does AI genuinely work in a winery?"
    a: "Where the data is rich within a single season: fermentation curves from every tank, sensor streams from the cellar, berry sampling through ripening, and free text such as tasting notes and cellar logs. Models that learn the dynamics of a ferment, or an LLM that reads the logs, have hundreds or thousands of examples a year to work with."
---

**Short answer: most of the AI pitched to wineries tries to predict a vintage outcome, such as harvest date, yield or a quality score, and a winery gets one vintage a year. Ten years of history is ten rows per block. Models trained on that mostly memorise, and the climate those ten years came from is already changing. The data is rich inside a season, though: every tank's fermentation curve, every sensor, every berry sample and every cellar note. Build the AI there, pool across blocks where you must predict across years, and be very sceptical of anything that claims a foundation model, synthetic data or an LLM has made ten rows into a thousand.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Three horizontal bars comparing ten years of training examples. A brewery brewing 300 batches a year has 3,000 batch rows. A winery with 120 fermentations a year has 1,200 fermentation curves. The same winery has 10 vintage rows per block for questions like harvest date or yield. The 10 row bar is tiny and highlighted in pink.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">TEN YEARS OF HISTORY, COUNTED IN TRAINING EXAMPLES (ILLUSTRATIVE)</text>
<g font-family="sans-serif">
<text x="40" y="80" font-size="12" font-weight="700" fill="#06483f">brewery batches</text>
<text x="40" y="97" font-size="10.5" fill="#4a6b64">300 a year</text>
<rect x="260" y="66" width="600" height="34" rx="6" fill="#06483f"/>
<text x="872" y="89" font-size="13" font-weight="700" fill="#06483f">3,000</text>
<text x="40" y="150" font-size="12" font-weight="700" fill="#06483f">winery fermentations</text>
<text x="40" y="167" font-size="10.5" fill="#4a6b64">120 tanks a year, within season</text>
<rect x="260" y="136" width="240" height="34" rx="6" fill="#4db6a2"/>
<text x="512" y="159" font-size="13" font-weight="700" fill="#06483f">1,200</text>
<text x="40" y="220" font-size="12" font-weight="700" fill="#06483f">winery vintages</text>
<text x="40" y="237" font-size="10.5" fill="#4a6b64">per block, for harvest date or yield</text>
<rect x="260" y="206" width="4" height="34" rx="1" fill="#ff4081"/>
<text x="276" y="229" font-size="13" font-weight="700" fill="#ff4081">10</text>
<rect x="40" y="266" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="291" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">BUILD THE AI WHERE THE ROWS ARE &#183; BE HONEST WHERE THEY ARE NOT</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Same winery, same ten years. The data is rich within a season and thin across them.</figcaption>
</figure>

A vendor shows a winery a model that predicts the optimal harvest date for each block. The demo looks good. The accuracy chart looks better. Then someone asks how many vintages it was trained on, and the answer is eleven.

Eleven harvests is eleven rows per block. A brewery doing 300 batches a year collects more examples of a fermentation in two weeks than that winery collects harvest dates in a decade. This is not a criticism of the vendor or the winery. It is the shape of the business, and it is the reason a lot of winery AI looks brilliant in a demo and ordinary in the second season.

This is the last post in **The Cellar Ledger**. The first five were about building the data foundation. This one is about what you can honestly build on top of it.

## Why ten rows fool you

With ten rows and a handful of features (growing degree days, rainfall, a few berry measurements), almost any model can fit the past closely. That is the problem. A close fit to ten points is mostly memory. The model has learned which year was which, not how the vineyard works.

Three things make it worse in wine:

- **The climate is moving.** The ten years in the training set are not a fair sample of the next ten. A warming trend means the next vintage is, by design, outside the range the model has seen.
- **The vineyard changes.** Vines age, blocks are replanted, irrigation and canopy practice change. A block's tenth vintage is not the same block as its first.
- **The target is soft.** Harvest date is partly a decision, shaped by the weather forecast, picking crews and tank space. Quality scores are a panel's judgement. Training a model to predict a decision reproduces the old decisions, habits and all.

The honest way to test such a model is leave-one-vintage-out: train on nine years, predict the tenth, repeat for each year. Even that has a catch. Ten folds give you a noisy estimate of the error itself, so a model that looks slightly better than the winemaker's rule of thumb may not be better at all.

## Where the rows actually are

The good news is that a winery is not short of data. It is short of vintages. Inside each season there is plenty:

- **Fermentation curves.** Every tank is its own fermentation, with density and temperature logged several times a day. A winery with 120 ferments a year has 1,200 curves after ten years, each with hundreds of points. That is enough to learn what a healthy ferment looks like and to flag a sluggish one early, which is what the [fermentation control post]({{ '/2024/ai-wine-fermentation-control/' | relative_url }}) covers.
- **Sensor streams.** Tank temperatures, cellar humidity, barrel room conditions. Continuous data, good for anomaly detection and soft sensors.
- **Berry sampling through ripening.** Weekly Brix, acid and pH per block across the season. Not enough to predict the outcome of a vintage from scratch, but enough to track this season's ripening curve against the last few.
- **Text.** Tasting notes, cellar logs, work orders, adjustment reasons. Years of it, mostly unread. This is where large language models genuinely shine.

The pattern: models that learn the **dynamics within a season** have real data. Models that learn the **outcome across seasons** mostly do not.

## Making the most of thin data

When you do need to predict across vintages, a few techniques help more than a bigger model.

**Pool across blocks.** A hierarchical (mixed-effects) model shares information between blocks while still letting each block differ. Forty blocks times ten vintages is not four hundred independent rows, but it is a lot better than ten.

**Start from the science.** Phenology models based on heat accumulation, the same growing degree day logic behind [ripeness prediction]({{ '/2024/predicting-grape-ripeness-harvest-date/' | relative_url }}), bring decades of viticulture research with them. Let the data adjust a sound model instead of asking it to discover botany from ten points.

**Predict the season, not the vintage.** Instead of predicting harvest date in April, update a ripening forecast each week as berry samples arrive. Each week's sample is a new row, and the forecast only has to reach a few weeks ahead.

**Use regional and public data.** Weather station records, regional harvest reports and satellite vegetation indices cover more years and more vineyards than any one winery's records.

## What the new tools can and cannot do

The obvious question in 2026 is whether the latest generation of AI changes this. Partly.

**Time-series foundation models** (models such as Chronos or TimesFM, pretrained on huge numbers of unrelated series) can forecast a curve they have never seen, zero-shot. For a fermentation curve, that is useful: a reasonable forecast of the next two days from the first three, with no training on your data. For a vintage outcome, they have nothing to work with. They know what curves look like in general. They do not know your vineyard.

**Synthetic data** is often offered as the fix for small data. It cannot be. Synthetic vintages generated from your ten real vintages contain no information those ten did not already have. They can help test a pipeline or stress-test a model against extreme scenarios, but they do not teach the model anything new about grapes.

**LLMs** are brilliant with the text: summarising ten years of cellar logs, clustering tasting-note language, answering questions over your SOPs, drafting reports, all covered earlier in this series. Asked to predict a harvest date, an LLM will produce one, in a confident sentence. It will not have learned anything from your data to get there. That is the one to watch for in a demo.

## Where this breaks

**Big producers are different.** A group with dozens of estates and hundreds of blocks has far more rows, and cross-vintage models become more reasonable. The ten-row problem is sharpest for a single estate.

**Within-season models can still fail on new conditions.** A fermentation model trained on ten normal vintages may not recognise the stress patterns of a heatwave harvest it has never seen. Rich data within seasons does not remove the need to watch for unusual years.

**Pooling assumes the blocks are alike enough.** Share information between a cool hillside block and a hot valley floor and the model may pull both towards an average that fits neither. The structure of the pooling is a viticultural decision as much as a statistical one.

**Winemaker judgement is also trained on few vintages.** A winemaker with twenty harvests has twenty rows too, though they come with a great deal of context a model does not have. The goal is to give that judgement better evidence, not to pretend either side has big data.

## The bottom line

Winery AI breaks when it treats a vintage like a batch. Ten years is ten rows, the climate is moving, and a close fit to the past is mostly memory. Build models where the data is rich, inside the season: fermentation curves, sensors, berry sampling and years of unread text. Where you must predict across vintages, pool across blocks, start from the science and update weekly. New tools help with curves and with text. None of them turns ten rows into a thousand, and anyone who says otherwise should be asked how many vintages they trained on.

That closes **The Cellar Ledger**. It started with [a chatbot giving three answers]({{ '/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) and ends here, and the thread through all six posts is the same: GenAI is only as trustworthy as the data model beneath it. The full series is on the [Cellar Ledger series page]({{ '/series/cellar-ledger/' | relative_url }}), and the wider wine catalogue is on the [Winemaking &amp; AI track]({{ '/tracks/winemaking-ai/' | relative_url }}).

## Frequently asked questions

**Why is machine learning harder in a winery than in a brewery?**
Because the unit of learning is often the vintage, and a winery gets one a year. Ten years of history gives ten rows per block for questions like harvest date, yield or quality score, while a brewery making hundreds of batches a year has thousands. Models trained on ten rows mostly memorise the past rather than learn from it.

**Can synthetic data or a foundation model fix a small winery dataset?**
Not on its own. Synthetic data made from your ten vintages contains no information your ten vintages did not already have. Time-series foundation models can give a reasonable zero-shot forecast of a curve, such as a fermentation, but they know nothing about your vineyard. Both are useful inside a sound design, and neither creates the missing history.

**Where does AI genuinely work in a winery?**
Where the data is rich within a single season: fermentation curves from every tank, sensor streams from the cellar, berry sampling through ripening, and free text such as tasting notes and cellar logs. Models that learn the dynamics of a ferment, or an LLM that reads the logs, have hundreds or thousands of examples a year to work with.
