---
layout: post
title: "Ask the Chatbot for the Alcohol, Get Three Answers: GenAI Needs a Semantic Layer"
image: /assets/og/genai-winery-semantic-layer-potential-alcohol.png
description: "Part 1 of The Cellar Ledger. A chat-with-your-data assistant asked for potential alcohol at a winery returns three different numbers, because the conversion lives in three spreadsheets. Why text-to-SQL agents amplify undefined metrics, and how a governed semantic layer, instrument-aware pipelines and a small eval set fix it."
date: 2026-06-22 09:00:00 -0700
updated: 2026-06-22
tags: [winemaking, cellar-ledger, generative-ai, data-engineering, semantic-layer]
faq:
  - q: "Why does a chat-with-your-data assistant give different answers to the same question?"
    a: "Usually because the metric is not defined anywhere the assistant can see. A text-to-SQL agent writes a query against whatever columns look plausible. If potential alcohol is calculated in three workbooks with three different factors, the agent picks one, and a slightly different prompt picks another. The fix is to define the metric once in a governed semantic layer and point the assistant at that, not at raw tables."
  - q: "What should a winery put in its semantic layer first?"
    a: "The numbers people argue about: potential alcohol, residual sugar, volume on hand, loss, and yield per tonne. Each gets one definition, stated parameters such as the sugar-to-alcohol yield figure, and a named owner. Those are also the questions a GenAI assistant will be asked most, so they are where a wrong answer does the most damage."
  - q: "How do you test a GenAI data assistant before the winemaker uses it?"
    a: "Write twenty or so real questions the cellar asks, with answers a person has checked by hand, and run them every time the model, prompt or semantic model changes. Score exact match on the numbers. It is a small evaluation set, and it catches most regressions before a winemaker does."
---

**Short answer: if you put a GenAI assistant on top of winery data without a governed metric layer, it will answer "what is the potential alcohol on the Shiraz lots?" with whichever of your three hidden conversion factors it happens to find. At 24 Brix those factors disagree by 1.7 points of alcohol, which is wider than a label tolerance. The model is not the problem. The undefined metric is. Define potential alcohol once, with its parameters in the open, build the pipeline so every reading carries its instrument, point the assistant at the semantic layer instead of raw tables, and test it with twenty questions the cellar actually asks.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Two paths from the same question. On the top path, a GenAI assistant queries three spreadsheets directly and returns 13.2, 14.2 and 14.9 percent potential alcohol. On the bottom path, raw readings flow into a bronze table, then a silver table that adds instrument and fermentation phase, then one governed potential alcohol metric in the semantic layer, and the assistant returns a single answer, 14.2 percent, with its method stated.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">SAME QUESTION, TWO ARCHITECTURES</text>
<g font-family="sans-serif">
<text x="40" y="60" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">WITHOUT A SEMANTIC LAYER</text>
<rect x="40" y="72" width="170" height="60" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="125" y="98" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">GenAI assistant</text>
<text x="125" y="116" text-anchor="middle" font-size="10.5" fill="#4a6b64">text-to-SQL</text>
<line x1="210" y1="102" x2="290" y2="102" stroke="#4db6a2" stroke-width="2"/>
<rect x="290" y="72" width="380" height="60" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="480" y="98" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">harvest.xlsx &#183; lab.xlsx &#183; labels.xlsx</text>
<text x="480" y="116" text-anchor="middle" font-size="10.5" fill="#4a6b64">&#215;0.55, &#215;0.59, &#215;0.62 buried in cells</text>
<line x1="670" y1="102" x2="740" y2="102" stroke="#4db6a2" stroke-width="2"/>
<rect x="740" y="72" width="220" height="60" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="850" y="98" text-anchor="middle" font-size="14" font-weight="700" fill="#ff4081">13.2 / 14.2 / 14.9%</text>
<text x="850" y="116" text-anchor="middle" font-size="10.5" fill="#4a6b64">depends on the prompt</text>
<text x="40" y="170" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">WITH A SEMANTIC LAYER</text>
<rect x="40" y="182" width="170" height="66" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="125" y="208" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">bronze</text>
<text x="125" y="226" text-anchor="middle" font-size="10.5" fill="#4a6b64">raw readings, as taken</text>
<line x1="210" y1="215" x2="240" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="240" y="182" width="190" height="66" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="335" y="208" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">silver</text>
<text x="335" y="226" text-anchor="middle" font-size="10.5" fill="#4a6b64">+ instrument, + ferment phase</text>
<line x1="430" y1="215" x2="460" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="460" y="182" width="220" height="66" rx="9" fill="#06483f"/>
<text x="570" y="208" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">semantic layer</text>
<text x="570" y="226" text-anchor="middle" font-size="10.5" fill="#cfe6df">one potential_alcohol, one owner</text>
<line x1="680" y1="215" x2="740" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="740" y="182" width="220" height="66" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="850" y="208" text-anchor="middle" font-size="14" font-weight="700" fill="#2e9e7c">14.2%</text>
<text x="850" y="226" text-anchor="middle" font-size="10.5" fill="#4a6b64">method and parameters cited</text>
<rect x="40" y="276" width="920" height="44" rx="10" fill="#06483f"/>
<text x="500" y="303" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">THE MODEL IS NOT THE PROBLEM &#183; THE UNDEFINED METRIC IS</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">An assistant pointed at spreadsheets finds whichever factor it reaches first. Pointed at a governed metric, it can only find one.</figcaption>
</figure>

A winemaker types into the new data assistant: "What's the potential alcohol on the Shiraz lots?" It answers in two seconds, with a tidy table. The assistant is right, in the sense that the number exists somewhere. It is also wrong, because the lab's workbook would have said something else, and the label artwork file something else again.

Nobody in that building made a mistake. Somebody typed a conversion factor into a cell years ago, the cell got copied into the next vintage's workbook, and now three versions of the same metric live in three files. A person knows which file to trust. A text-to-SQL agent does not. This is the first post in **The Cellar Ledger**, a series on the data engineering and GenAI work that sits under a winery's numbers, and it starts with the number everyone uses and nobody has defined.

## Why GenAI makes an old problem louder

Every chat-with-your-data product on the market in 2026 works roughly the same way. You ask a question in English. The assistant reads some description of your data, writes a query, runs it and summarises the result. Power BI Copilot, Databricks AI/BI Genie and Snowflake Cortex Analyst all follow this pattern, and all three read a semantic model or a set of curated instructions first if you give them one.

If you do not give them one, they read the tables. And a table column called `pot_alc` tells the model nothing about which factor produced it.

Two things then go wrong at once:

- **The answer is unstable.** Rephrase the question slightly and the agent may join a different table, pick a different column and return a different number, with the same confident tone.
- **The answer looks authoritative.** A spreadsheet with a wrong number looks like a spreadsheet. A chatbot with a wrong number looks like the system. People check spreadsheets. They mostly do not check the chatbot.

The old problem was three people working from three wines. The new problem is that the assistant sends each person whichever of the three wines the prompt happened to reach.

## The metric underneath: what the conversion really is

To define potential alcohol once, you have to know what the rules of thumb are hiding. Brix times 0.55, 0.59 or 0.62 is a shortcut for a four-step calculation, and each step is a parameter someone should own.

**1. Brix to density.** Degrees Brix is grams of sucrose per 100 grams of solution, weight for weight. A standard polynomial for sucrose solutions gives a specific gravity of about 1.101 at 24 Brix.

**2. Dissolved solids per litre.** Brix times SG times 10. For our must, about 264 g/L.

**3. Subtract what is not sugar.** Grape must is glucose and fructose plus acids, minerals and phenolics. The non-sugar solids are typically somewhere around 20 to 30 g/L in ripe fruit. Take 25 and you have about 239 g/L of fermentable sugar.

**4. Sugar to alcohol.** In theory, one glucose molecule gives two of ethanol and two of CO2, so about 15.4 g/L of sugar makes 1% alcohol by volume. Real yeast builds cells, makes glycerol and loses some ethanol with the gas, so working figures sit higher. The EU uses 16.83 g/L per 1% vol. 239 divided by 16.83 is 14.2%.

Written as a function, the whole thing is short:

```python
def potential_alcohol(brix, non_sugar_gl=25.0, yield_gl_per_pct=16.83):
    sg = 1 + brix / (258.6 - (brix / 258.2) * 227.1)
    sugar_gl = brix * sg * 10 - non_sugar_gl
    return sugar_gl / yield_gl_per_pct
```

The point is not the code. It is that `non_sugar_gl` and `yield_gl_per_pct` are now named, visible and owned. The shortcut factors hide both, which is why they disagree.

It matters because tolerances are measured in single points. In the US, a wine at or under 14% may be labelled within 1.5 points of the truth, and above 14% within 1 point, and the label may not cross the 14% line because the excise rate changes there. A 1.7 point spread across the building is bigger than the tolerance it has to stay inside.

## The data engineering fix: instrument-aware layers

Defining the metric is half of it. The other half is making sure the inputs mean what the metric assumes. This is where a lot of winery data breaks before any AI gets near it.

A refractometer is fine in the vineyard. Once fermentation starts, alcohol raises the refractive index, so a refractometer overstates the remaining sugar, more so as the wine gets drier. A hydrometer measures density, and ethanol is lighter than water, so a dry red reads about minus 1 to minus 2 Brix. Both are correct readings of what the instrument measures. Both become wrong the moment a pipeline stores them in one column called `brix`.

A simple medallion layout handles this without heroics:

- **Bronze** keeps every reading exactly as taken: value, unit, instrument, who, when, which tank. Nothing is converted and nothing is thrown away.
- **Silver** adds context the pipeline can derive: the fermentation phase (pre-inoculation, active, dry) from the tank's own events, and a flag on any refractometer reading taken after inoculation. Hydrometer readings mid-ferment are renamed to what they are, density, and allowed to go negative.
- **Gold and the semantic layer** hold the governed metrics. `potential_alcohol` only reads pre-inoculation sugar readings. Once a finished lot has a measured alcohol from the lab, a separate `alcohol_measured` takes over and the prediction retires for that lot.

Put a data contract on the bronze table that rejects a reading with no instrument. It is one line of validation, and it is the line that stops the next vintage's ambiguity at the door instead of in a board report.

## Pointing the assistant at the right layer

With the metric defined, the GenAI part becomes much less exciting, which is what you want. Three settings do most of the work:

1. **Restrict the assistant to the semantic model.** Do not give it the raw tables at all. If it can only see `potential_alcohol` as a measure, it cannot invent a fourth version.
2. **Write the instructions like a cellar manual.** Most of these tools accept plain-text instructions. Use them for the domain facts the model cannot guess: "Brix after inoculation is density, not sugar", "alcohol on a finished lot comes from `alcohol_measured`", "volumes are in litres at 20 degrees C".
3. **Make it cite the method.** Ask for the metric name and its parameters under every answer. A winemaker who sees "potential alcohol, EU yield 16.83 g/L, non-sugar 25 g/L" can argue with the assumption instead of with the number.

## A twenty-question eval set

The last step is the one teams skip. Before anyone relies on the assistant, write down twenty or so questions the cellar actually asks, with answers someone has checked by hand. "Potential alcohol on lot 24-SH-03." "Which tanks are still above 5 Brix?" "Measured alcohol on last year's Viognier." Run the set every time the model, the prompt or the semantic model changes, and score exact numeric matches.

It is a small file. It is also the only honest answer to "can we trust the chatbot?" You do not trust it. You test it, the same way the lab tests a new instrument against a reference before it goes into use.

Here is the bonus. Every finished lot gives you a pair: starting sugar and measured alcohol. A few vintages of those pairs, by variety, let you fit your own yield figure to your fruit, your yeast and your cellar. That is the first genuinely useful model in the building, and it only exists because the pipeline kept both numbers.

## Where this breaks

**The non-sugar estimate is still a guess.** It moves with variety, ripeness, rot and press fraction. A stated default is better than a hidden one, but measure it on a few musts each year and treat it as provisional.

**A semantic layer does not fix bad sampling.** Juice from the sunny end of one row does not describe a block. No metric definition corrects the bucket.

**Instructions drift.** The plain-text guidance you give the assistant is configuration. Version it, review changes, and re-run the eval set when it changes, or it quietly becomes the fourth spreadsheet.

**Rules vary by market.** The US tolerance figures above are the ones I know best. Check the market you sell into before you build a labelling check on them.

## The bottom line

The chatbot gave three answers because the winery had three answers. GenAI did not create that problem. It just stopped hiding it. Define the metric once with its parameters in the open, keep every reading with its instrument, let the assistant see only the governed layer, and hold it to a small set of checked questions. Then the two-second answer is worth having.

For the wider argument about why winery dashboards lose the cellar's trust, see [Why Power BI Dashboards Die in Wineries]({{ '/2026/why-power-bi-dashboards-fail-wineries/' | relative_url }}). What a model can do with a clean fermentation curve is in [AI for Wine Fermentation Control]({{ '/2024/ai-wine-fermentation-control/' | relative_url }}). Next in this series: [event-sourcing the cellar]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }}), the data model that makes volumes add up. The full list is on the [Cellar Ledger series page]({{ '/series/cellar-ledger/' | relative_url }}).

## Frequently asked questions

**Why does a chat-with-your-data assistant give different answers to the same question?**
Usually because the metric is not defined anywhere the assistant can see. A text-to-SQL agent writes a query against whatever columns look plausible. If potential alcohol is calculated in three workbooks with three different factors, the agent picks one, and a slightly different prompt picks another. The fix is to define the metric once in a governed semantic layer and point the assistant at that, not at raw tables.

**What should a winery put in its semantic layer first?**
The numbers people argue about: potential alcohol, residual sugar, volume on hand, loss, and yield per tonne. Each gets one definition, stated parameters such as the sugar-to-alcohol yield figure, and a named owner. Those are also the questions a GenAI assistant will be asked most, so they are where a wrong answer does the most damage.

**How do you test a GenAI data assistant before the winemaker uses it?**
Write twenty or so real questions the cellar asks, with answers a person has checked by hand, and run them every time the model, prompt or semantic model changes. Score exact match on the numbers. It is a small evaluation set, and it catches most regressions before a winemaker does.
