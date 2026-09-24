---
layout: post
title: "Cask Inventory as Data Engineering: SCD2 Positions, Regauge Events and Angel's Share as a Derived Number"
image: /assets/og/cask-inventory-data-engineering-scd2.png
description: "Part 4 of The Still and the Model. A cask lives in the warehouse for twelve years or more, moves, gets sampled and regauged, and loses spirit every year. Model its attributes as slowly changing dimensions, its life as events, and angel's share as a calculation, so any question about any cask on any date has one answer."
date: 2026-08-06 09:00:00 -0700
updated: 2026-08-06
tags: [distilling-maturation, still-and-model, data-engineering, data-modeling, generative-ai]
faq:
  - q: "What is an SCD2 table and why use it for casks?"
    a: "A type 2 slowly changing dimension keeps every version of a record with the dates it was valid, instead of overwriting it. For casks, that means every warehouse position, owner and status a cask has ever had stays in the table with its dates. You can ask where a cask was in March 2019 and get an answer, which matters for microclimate analysis, audits and customer queries."
  - q: "How should angel's share be calculated in a cask inventory?"
    a: "As a derived number, never a stored one. Take the litres of absolute alcohol at filling, subtract the alcohol at the latest regauge and any recorded samples or withdrawals, and what is left is the loss. Stored as a field, angel's share goes stale and hides sampling. Derived from events, it is always current and explainable."
  - q: "Can a GenAI assistant answer questions about maturing stock?"
    a: "Yes, if it answers through governed queries rather than raw tables. Give it tools such as cask_history, position_on and alcohol_balance, backed by the event and SCD2 tables, and it can answer questions like which casks from a given fill have lost more than usual, with every figure coming from the query."
---

**Short answer: a whisky cask can sit in the warehouse for twelve years or more, and in that time it moves, gets sampled, is regauged and quietly loses spirit to the air. If the inventory stores only the cask's current position and current volume, most of that history is gone. Model the attributes that change slowly (position, owner, status) as a type 2 slowly changing dimension, record everything that happens to the cask as an event, and calculate angel's share from the events instead of storing it. Then "where was this cask in 2019?" and "how much has it really lost?" each have one answer, and a GenAI assistant can answer them without guessing.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="An illustrative twelve-year timeline for one cask. Filled in 2014 with 250 litres at 63.5 percent, 158.75 litres of absolute alcohol, in warehouse 1. Moved to warehouse 3 in 2016. Sampled in 2019. Regauged in 2020. Moved again in 2022. Regauged in 2026 at 205 litres and 60.8 percent, 124.64 litres of absolute alcohol. Angel's share is derived as about 34 litres of absolute alcohol, roughly 2 percent a year.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">ONE CASK, TWELVE YEARS OF EVENTS (ILLUSTRATIVE)</text>
<g font-family="sans-serif">
<line x1="70" y1="150" x2="930" y2="150" stroke="#4db6a2" stroke-width="3"/>
<circle cx="70" cy="150" r="9" fill="#06483f"/>
<text x="70" y="120" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">2014 fill</text>
<text x="70" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">250 L at 63.5%</text>
<text x="70" y="198" text-anchor="middle" font-size="10.5" fill="#4a6b64">158.75 LAA</text>
<circle cx="213" cy="150" r="7" fill="#4db6a2"/>
<text x="213" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2016 move</text>
<text x="213" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">W1 to W3</text>
<circle cx="427" cy="150" r="7" fill="#4db6a2"/>
<text x="427" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2019 sample</text>
<text x="427" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">recorded draw</text>
<circle cx="498" cy="150" r="7" fill="#4db6a2"/>
<text x="518" y="100" text-anchor="middle" font-size="11.5" fill="#06483f">2020 regauge</text>
<circle cx="643" cy="150" r="7" fill="#4db6a2"/>
<text x="643" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2022 move</text>
<text x="643" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">W3 to W5</text>
<circle cx="930" cy="150" r="9" fill="#06483f"/>
<text x="915" y="120" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">2026 regauge</text>
<text x="915" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">205 L at 60.8%</text>
<text x="915" y="198" text-anchor="middle" font-size="10.5" fill="#4a6b64">124.64 LAA</text>
<rect x="250" y="222" width="500" height="44" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="500" y="249" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ff4081">derived loss about 34 LAA, roughly 2% a year</text>
<rect x="40" y="282" width="920" height="36" rx="10" fill="#06483f"/>
<text x="500" y="305" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">ANGEL'S SHARE IS A QUERY OVER THE EVENTS, NOT A FIELD SOMEONE UPDATES</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative cask. Litres of absolute alcohol (LAA) are bulk litres times strength. In a full balance, samples such as the 2019 draw are subtracted before anything is called angel's share.</figcaption>
</figure>

Ask a warehouse manager where cask 14-0387 is and they will tell you in seconds. Ask where it was in the summer of 2019, when a group of casks from that fill picked up an unexpected note, and the answer usually involves a paper ledger, a retired colleague and a lot of goodwill.

The [previous posts in this series]({{ '/2026/llm-copilot-still-operator/' | relative_url }}) lived on the still house floor. This one moves into the warehouse, where the timescale is years instead of hours, and where the data model decides whether history survives.

## Two kinds of change

A cask changes in two different ways, and they need two different structures.

**Attributes that change occasionally:** warehouse, bay and tier; owner (for casks held for customers); status (maturing, earmarked, disgorged); cask type after a re-rack. These are facts about the cask that hold for a period, then change.

**Things that happen to it:** filling, moving, sampling, regauging, topping up, re-racking into a new cask, disgorging. These are events with a date, a quantity and a person.

Most cask systems store the first kind as current values and the second as, at best, a comments field. Both lose history.

## SCD2: every version, with its dates

A type 2 slowly changing dimension keeps every version of an attribute instead of overwriting it. Each row carries the date it became true and the date it stopped:

```sql
-- cask_position_scd2: one row per period the cask sat in one place
-- cask_id | warehouse | bay | tier | valid_from | valid_to   | is_current
-- 14-0387 | W1        | A   | 2    | 2014-05-12 | 2016-09-03 | false
-- 14-0387 | W3        | C   | 1    | 2016-09-03 | 2022-04-18 | false
-- 14-0387 | W5        | B   | 3    | 2022-04-18 | 9999-12-31 | true

SELECT warehouse, bay, tier
FROM   cask_position_scd2
WHERE  cask_id = '14-0387'
  AND  DATE '2019-07-01' >= valid_from
  AND  DATE '2019-07-01' <  valid_to;
```

That one query answers the 2019 question. It also makes microclimate analysis possible: join positions over time to the warehouse temperature and humidity logs, and every cask gets its own lived climate history, which is what the [rackhouse microclimate post]({{ '/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}) needs as input. Without SCD2, every cask appears to have spent twelve years wherever it happens to be today.

The pipeline to maintain it is standard: each time a move is recorded, close the current row and open a new one. dbt snapshots, Delta `MERGE` and Fabric pipelines all do this with a few lines of configuration.

## Events: the cask's own ledger

Everything that changes the cask's contents is an event, recorded the same way the [wine cellar ledger]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }}) records movements:

- **fill**: bulk litres, strength, LAA, spirit batch, cask type
- **sample**: volume drawn, purpose
- **regauge**: bulk litres, strength, LAA, method (dip or weight)
- **re-rack**: from cask, to cask, volume
- **disgorge**: volume and strength out to vatting

Regauges deserve a note. Casks are often gauged by weight rather than by dip: gross weight minus the cask's tare, divided by the density at the measured strength, gives bulk litres. That calculation depends on a density table for ethanol and water at 20 degrees C, and on the tare weight recorded at filling. If either is missing or wrong, every regauge of that cask is wrong in the same direction. Store the gross weight, the tare and the strength on the event, not just the resulting volume, so the calculation can be checked and redone.

## Angel's share as a derived number

With events in place, angel's share stops being a field somebody updates and becomes a calculation:

> loss = LAA at fill - LAA at latest regauge - LAA drawn in samples and withdrawals

For the illustrative cask above: filled with 250 litres at 63.5%, which is 158.75 LAA. Twelve years later it regauges at 205 litres and 60.8%, which is 124.64 LAA. Leaving the small 2019 sample aside for simplicity, the loss is about 34 LAA, or 21.5% over twelve years, roughly 2% a year compounded. That is in the range often quoted for Scotch in a cool, damp warehouse. A warm climate loses far more, and strength can even rise rather than fall where water evaporates faster than alcohol.

Two things make the derived version better than a stored one. It is always current: a new regauge updates it without anyone remembering to. And it is honest about samples: a cask that looks thirsty because the blending team kept drawing from it shows its samples as samples, not as evaporation. The [angel's share forecasting post]({{ '/2024/forecasting-whiskey-angels-share/' | relative_url }}) covers modelling the loss. This is the data it should be modelled from.

## Putting a GenAI assistant on top

With SCD2 positions and a cask event ledger, the questions people actually ask become queries, and queries can become tools for a GenAI assistant:

- `cask_history(cask_id)`: every event and position, in order
- `position_on(cask_id, date)`: the SCD2 lookup above
- `alcohol_balance(fill_batch)`: fill LAA, current LAA, samples, derived loss per cask

Asked "which casks from the May 2014 fill have lost more than their neighbours?", the assistant calls `alcohol_balance`, compares each cask with the median for its fill and warehouse, and lists the outliers with their positions over time. Every number comes from a query. The model's job is to understand the question, call the right tools and explain the answer in plain words. The [semantic layer post]({{ '/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) in the wine series makes the case for why it must not see raw tables.

## Where this breaks

**Twelve years of history rarely starts clean.** The first decade of most cask inventories is a mix of paper, old systems and spreadsheets. Migrate what you can as events with a clear source, start SCD2 from an opening position per cask, and mark the migrated history as lower confidence rather than pretending it is as good as the new.

**Regauges are infrequent and noisy.** A cask regauged twice in twelve years gives two data points for its loss. Differences between casks of a few percent may be measurement, not maturation.

**Tare weights go missing.** A cask with no recorded tare cannot be regauged by weight with any accuracy. Treat a missing tare as a data quality defect and flag it on day one, not in year ten.

**Duty records are separate.** Bonded warehouse records answer to the excise authority and have their own rules. The analytic inventory should reconcile to them, not replace them.

## The bottom line

A cask is a twelve-year record, and most inventories keep only its last page. Keep every position with its dates, record every event with its quantities, and derive angel's share rather than storing it. Then the questions that matter, about climate, loss, sampling and audits, have one answer each, and a GenAI assistant can find it through governed tools instead of improvising. The spirit is patient. The data model should be too.

Next in the series: [a GenAI blending assistant with the maths done in code]({{ '/2026/genai-whisky-blending-assistant-lp/' | relative_url }}). For choosing which casks to use, see [AI for Cask Selection and Maturing-Stock Inventory]({{ '/2024/ai-cask-selection-inventory/' | relative_url }}). The full list is on [The Still and the Model series page]({{ '/series/still-and-model/' | relative_url }}).

## Frequently asked questions

**What is an SCD2 table and why use it for casks?**
A type 2 slowly changing dimension keeps every version of a record with the dates it was valid, instead of overwriting it. For casks, that means every warehouse position, owner and status a cask has ever had stays in the table with its dates. You can ask where a cask was in March 2019 and get an answer, which matters for microclimate analysis, audits and customer queries.

**How should angel's share be calculated in a cask inventory?**
As a derived number, never a stored one. Take the litres of absolute alcohol at filling, subtract the alcohol at the latest regauge and any recorded samples or withdrawals, and what is left is the loss. Stored as a field, angel's share goes stale and hides sampling. Derived from events, it is always current and explainable.

**Can a GenAI assistant answer questions about maturing stock?**
Yes, if it answers through governed queries rather than raw tables. Give it tools such as cask_history, position_on and alcohol_balance, backed by the event and SCD2 tables, and it can answer questions like which casks from a given fill have lost more than usual, with every figure coming from the query.
