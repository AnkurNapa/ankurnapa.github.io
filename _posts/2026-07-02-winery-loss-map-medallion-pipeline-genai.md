---
layout: post
title: "The Loss Map: A Medallion Pipeline, Anomaly Flags and an LLM That Drafts the Variance Note"
image: /assets/og/winery-loss-map-medallion-pipeline-genai.png
description: "Part 3 of The Cellar Ledger. Every winery loses wine between crush and bottle. Build the loss map as a bronze, silver and gold pipeline over the movement ledger, flag unusual stages with robust statistics, and let an LLM draft the monthly variance note without ever doing the arithmetic."
date: 2026-07-02 09:00:00 -0700
updated: 2026-07-02
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, anomaly-detection]
faq:
  - q: "How much wine does a winery lose between crush and bottle?"
    a: "It varies a lot with style, press regime, barrel time and cellar humidity, so treat any single number with caution. The more useful figure is your own: the loss per stage per lot, calculated from recorded movements, and the unexplained residual left over. That residual is the part worth chasing."
  - q: "What anomaly detection works for winery loss data?"
    a: "Simple, robust statistics usually beat complex models here. Compare each lot's loss rate at a stage with the median for the same stage and vessel type, scaled by the median absolute deviation, and flag the outliers. There is rarely enough data for a deep model, and a robust z-score is easy for a cellar master to check by hand."
  - q: "Can an LLM write the monthly loss variance report?"
    a: "It can draft it, provided it never calculates. Run the numbers in SQL, pass the results and the recorded adjustment reasons to the model, and have it write the commentary around those fixed figures. A person reviews and signs. The model is good at turning a table and twenty reason codes into readable paragraphs, and bad at arithmetic."
---

**Short answer: a winery that crushes 100 tonnes of red fruit might press 72,000 litres and bottle 63,500. The 8,500 litres in between are mostly known losses: lees, racking, evaporation, filtration, bottling. The part that matters is what is left after you account for those, the unexplained residual. Build the loss map as a medallion pipeline on top of the movement ledger, flag unusual stages with robust statistics rather than a fancy model, and let an LLM draft the variance note from the query results. The model writes the words. SQL does the sums.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A waterfall chart for an illustrative 100 tonne red vintage. It starts at 72,000 litres pressed, then steps down for gross lees 2,900 litres, racking 1,100, barrel evaporation 2,000, topping and samples 400, filtration 700, bottling 500, and an unexplained residual of 900 litres highlighted in pink, ending at 63,500 litres bottled. The vertical axis starts at 60,000 litres.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">LOSS MAP: 100 TONNES OF RED, CRUSH TO BOTTLE (ILLUSTRATIVE)</text>
<g font-family="sans-serif">
<line x1="60" y1="260" x2="960" y2="260" stroke="#4a6b64" stroke-width="1"/>
<text x="60" y="52" font-size="10" fill="#4a6b64">axis starts at 60,000 L</text>
<rect x="70" y="70" width="64" height="190" fill="#06483f"/>
<text x="102" y="64" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">72,000</text>
<rect x="170" y="70" width="64" height="45.9" fill="#4db6a2"/>
<text x="202" y="130" text-anchor="middle" font-size="11" fill="#06483f">&#8722;2,900</text>
<rect x="270" y="115.9" width="64" height="17.4" fill="#4db6a2"/>
<text x="302" y="148" text-anchor="middle" font-size="11" fill="#06483f">&#8722;1,100</text>
<rect x="370" y="133.3" width="64" height="31.7" fill="#4db6a2"/>
<text x="402" y="180" text-anchor="middle" font-size="11" fill="#06483f">&#8722;2,000</text>
<rect x="470" y="165" width="64" height="6.3" fill="#4db6a2"/>
<text x="502" y="186" text-anchor="middle" font-size="11" fill="#06483f">&#8722;400</text>
<rect x="570" y="171.3" width="64" height="11.1" fill="#4db6a2"/>
<text x="602" y="197" text-anchor="middle" font-size="11" fill="#06483f">&#8722;700</text>
<rect x="670" y="182.4" width="64" height="7.9" fill="#4db6a2"/>
<text x="702" y="205" text-anchor="middle" font-size="11" fill="#06483f">&#8722;500</text>
<rect x="770" y="190.3" width="64" height="14.3" fill="#ff4081"/>
<text x="802" y="220" text-anchor="middle" font-size="11" font-weight="700" fill="#ff4081">&#8722;900</text>
<rect x="870" y="204.6" width="64" height="55.4" fill="#06483f"/>
<text x="902" y="198" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">63,500</text>
<g font-size="10" fill="#4a6b64" text-anchor="middle">
<text x="102" y="278">pressed</text>
<text x="202" y="278">gross lees</text>
<text x="302" y="278">racking</text>
<text x="402" y="278">barrel</text><text x="402" y="291">evaporation</text>
<text x="502" y="278">topping</text><text x="502" y="291">&amp; samples</text>
<text x="602" y="278">filtration</text>
<text x="702" y="278">bottling</text>
<text x="802" y="278" fill="#ff4081" font-weight="700">unexplained</text>
<text x="902" y="278">bottled</text>
</g>
<rect x="40" y="304" width="920" height="30" rx="8" fill="#06483f"/>
<text x="500" y="324" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">7,600 L OF KNOWN LOSS &#183; 900 L NOBODY CAN EXPLAIN &#183; CHASE THE PINK BAR</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative figures, not benchmarks. Your own stages, from your own ledger, are the only numbers that count.</figcaption>
</figure>

At the end of every vintage somebody asks the same question: we pressed this much, we bottled that much, where did the rest go? The honest answer is usually "lees, evaporation and a lot of small things", said with a shrug. That shrug hides two very different kinds of loss. Most of it is the normal cost of making wine. A small slice is wine the winery cannot account for, and that slice is where the money, the excise questions and the process problems live.

The [previous post]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }}) built the movement ledger. This one turns it into a loss map, adds a light layer of anomaly detection, and hands the monthly write-up to an LLM on a short leash.

## Known loss versus unexplained loss

Some loss is wine the winery chose to give up, with a recorded reason:

- **Gross lees** after fermentation and the first racking, often a few percent of volume.
- **Racking losses** each time wine moves off sediment.
- **Barrel evaporation**, which depends heavily on cellar humidity and temperature, and runs to a few percent a year.
- **Topping and samples**, small but constant.
- **Filtration and bottling**, the dead volume in hoses, filters and the filler bowl.

Everything else is the residual: inputs, minus outputs, minus every recorded loss. In the illustrative vintage above, 7,600 litres of loss has a reason and 900 litres does not. Nine hundred litres of finished red is more than a thousand bottles. It is worth an afternoon.

The residual is never zero. Meters disagree, dips have error, temperature moves volumes about. The goal is not zero. The goal is a residual small enough and stable enough that when it jumps, you notice.

## The pipeline: bronze, silver, gold

A loss map is a data engineering problem before it is an analytics one. The medallion pattern fits it well.

**Bronze** is the movement ledger itself, untouched: every receive, transfer, rack, top, filter, bottle, observe and adjust event, with volumes corrected to 20 degrees C.

**Silver** classifies each movement into a stage and a loss category. A rack event that sends 58 litres to the lees tank becomes "loss: gross lees, stage: post-ferment, lot 24-SH-03". Lees that are later filtered and recovered come back as a recovery event, so they are not double-counted as lost. This is where most of the domain logic lives, and where a cellar master should review the rules, because the mapping from event type to loss category is a set of opinions about the process.

**Gold** is one row per lot, per stage, per vintage: volume in, volume out, known loss by category, and the residual. It feeds the waterfall, the dashboard and, as we will see, the language model.

```sql
SELECT lot_id, stage,
       SUM(volume_in_l)  AS vol_in,
       SUM(volume_out_l) AS vol_out,
       SUM(known_loss_l) AS known_loss,
       SUM(volume_in_l) - SUM(volume_out_l) - SUM(known_loss_l) AS residual_l
FROM   silver_lot_stage_movements
GROUP  BY lot_id, stage;
```

It is one query. The hard work is in silver, in getting the categories right.

## Anomaly flags: boring statistics on purpose

Once the gold table exists, the natural next request is "use AI to find the problems". Resist the urge to reach for a deep model. A winery has maybe a few hundred lots a year and a handful of vintages of clean history. That is not enough data to train anything elaborate, and the cellar master needs to be able to check the flag by hand.

A robust z-score does the job:

1. For each stage and vessel type (say, racking from 5,000 litre stainless), take the median loss rate across lots.
2. Measure how spread out the rates are with the median absolute deviation, which ignores the odd extreme value instead of being dragged by it.
3. Flag any lot whose loss rate sits more than about three scaled deviations from the median.

That flags the one tank that lost 4% at racking when its siblings lost 1.5%, and it ignores the vintage-wide shift that every tank shared. It is not glamorous. It explains itself in one sentence, which matters more.

Barrel evaporation deserves its own treatment. It depends on where the barrel sits, so group by cellar zone and position if you record it. The [rackhouse microclimate post]({{ '/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}) covers the same physics from the whisky side.

## The LLM drafts the variance note

Every month someone writes a paragraph or two for the operations review: loss this month, how it compares, what happened. It takes an hour and it is dull. This is a good job for a language model, as long as you set it up so it cannot get the numbers wrong.

The pattern that works:

1. **SQL does every calculation.** The gold table, the month-on-month changes, the flagged lots, the top adjustment reasons by volume. All of it is computed before the model sees anything.
2. **The model gets the results as structured input.** A small JSON block of figures, the list of flagged lots, and the free-text reasons operators typed on their adjustment events.
3. **The model writes prose around fixed figures.** Ask it to use only the numbers it was given and to name the source row for each claim. Better still, have it return the note with placeholders that code fills from the JSON, so no number is ever typed by the model.
4. **It groups the operators' reasons.** Twenty adjustment notes that say "topping not logged", "topped B-row, forgot", "topping, missed" become one line: "most of the residual traces to unlogged barrel topping in the B row". This is where the model genuinely earns its keep. It reads messy human text well.
5. **A person edits and signs.** The note goes out under the winemaker's name, not the model's.

What you should not do is hand the model the raw ledger and ask what went wrong this month. It will add up columns in its head, and it will be confidently off by a few hundred litres.

## Where this breaks

**The residual absorbs every measurement error.** A drifting flow meter shows up as unexplained loss. So does a dip stick read at the wrong temperature. Before you treat the residual as missing wine, check the instruments.

**The silver rules are opinions.** Whether lees wine counts as lost or as a recoverable by-product changes the map. Write the rules down and have the cellar master sign them off, or two people will read the same waterfall two ways.

**Loss targets change behaviour.** If people are judged on the pink bar, the pink bar will shrink by being recorded as something else. Use the map to find process problems, not to grade the cellar crew.

**The LLM can still mislead in words.** Even with fixed numbers, a model can frame a normal month as a problem or wave away a real one. That is why the flags come from statistics and the model only describes them.

## The bottom line

Every winery loses wine. The question is how much of that loss comes with a reason. A pipeline over the movement ledger splits known loss from the residual. Robust statistics point at the stage and lot that changed. A language model turns the figures and the cellar's own notes into a paragraph someone is happy to sign. None of those three steps is exotic, and together they turn the end-of-vintage shrug into a short list of tanks to look at.

Next in the series: [lot genealogy as a graph]({{ '/2026/wine-lot-genealogy-graph-recall-agent/' | relative_url }}), where the same ledger answers "which bottles contain block 7?". For the cellar and barrel view in Tableau, see [the barrel-ageing dashboard]({{ '/2023/tableau-wine-cellar-barrel-ageing-dashboard/' | relative_url }}). The full list is on the [Cellar Ledger series page]({{ '/series/cellar-ledger/' | relative_url }}).

## Frequently asked questions

**How much wine does a winery lose between crush and bottle?**
It varies a lot with style, press regime, barrel time and cellar humidity, so treat any single number with caution. The more useful figure is your own: the loss per stage per lot, calculated from recorded movements, and the unexplained residual left over. That residual is the part worth chasing.

**What anomaly detection works for winery loss data?**
Simple, robust statistics usually beat complex models here. Compare each lot's loss rate at a stage with the median for the same stage and vessel type, scaled by the median absolute deviation, and flag the outliers. There is rarely enough data for a deep model, and a robust z-score is easy for a cellar master to check by hand.

**Can an LLM write the monthly loss variance report?**
It can draft it, provided it never calculates. Run the numbers in SQL, pass the results and the recorded adjustment reasons to the model, and have it write the commentary around those fixed figures. A person reviews and signs. The model is good at turning a table and twenty reason codes into readable paragraphs, and bad at arithmetic.
