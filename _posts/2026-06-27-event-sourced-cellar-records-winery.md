---
layout: post
title: "Event-Sourcing the Cellar: Why Winery Volumes Should Be Derived, Never Stored"
image: /assets/og/event-sourced-cellar-records-winery.png
description: "Part 2 of The Cellar Ledger. When tank volumes are an editable field, losses disappear without a reason. An append-only movement ledger in the lakehouse makes every balance a calculation, gives an AI agent real provenance to explain, and keeps the agent from ever overwriting the truth."
date: 2026-06-27 09:00:00 -0700
updated: 2026-06-27
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, data-modeling]
faq:
  - q: "What is event sourcing in a winery data model?"
    a: "Instead of storing each tank's volume as a field that people edit, you store every movement as an immutable event: receipt, transfer, topping, racking, blend, filtration, bottling, sample, loss. The volume in any vessel at any moment is the sum of the events up to that moment. Nothing is overwritten, so every litre has a history."
  - q: "How do you handle a dip reading that disagrees with the book volume?"
    a: "Record the dip as an observation, not as a new volume. If it differs from the calculated balance, the difference becomes its own adjustment event with a required reason, such as evaporation, topping not recorded or meter error. The book is corrected by an event, never by an edit, so the gap stays visible and explainable."
  - q: "Should an AI agent be allowed to update winery inventory?"
    a: "It should be allowed to propose, not to write. Let the agent read the movement ledger and draft a movement or an adjustment with its reasoning attached, then have a person approve it before it is appended. Because the ledger is append-only, even an approved mistake is fixed with a reversing event and never disappears."
---

**Short answer: most winery systems store a tank's volume as a number people can edit. When the dip disagrees with the book, someone types the new figure in, and the difference vanishes with no reason attached. Event-sourcing the cellar means storing every movement as an append-only event and calculating every balance from them. The book then explains itself, a GenAI agent has real history to reason over instead of guessing, and the rule "agents propose, people approve" becomes easy to enforce because nothing can be overwritten.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Two ways of recording tank 12. On the left, a state table holds a single volume field that someone edited from 4,980 to 4,920 litres, and the 60 litres are gone without a reason. On the right, a movement ledger lists events: received 5,000 litres, topped 40 litres from barrel, sampled 2 litres, racked out 58 litres of lees, dip observation 4,920 litres, then a gauge adjustment of minus 60 litres with the reason recorded. The balance is the sum of the events.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">TANK 12: STORED STATE VS DERIVED STATE</text>
<g font-family="sans-serif">
<text x="210" y="58" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">EDITABLE FIELD</text>
<rect x="40" y="72" width="340" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="210" y="106" text-anchor="middle" font-size="12" fill="#06483f">tank_12.volume_l</text>
<text x="210" y="140" text-anchor="middle" font-size="22" font-weight="700" fill="#06483f">4,980 &#8594; 4,920</text>
<text x="210" y="172" text-anchor="middle" font-size="11" fill="#ff4081">60 L gone, no reason, no history</text>
<text x="700" y="58" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">APPEND-ONLY MOVEMENT LEDGER</text>
<rect x="440" y="72" width="520" height="190" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<g font-size="11.5" fill="#06483f">
<text x="460" y="98">receive &#183; from press 3</text><text x="940" y="98" text-anchor="end">+5,000</text>
<text x="460" y="122">top &#183; from barrel B-17</text><text x="940" y="122" text-anchor="end">+40</text>
<text x="460" y="146">sample &#183; lab</text><text x="940" y="146" text-anchor="end">&#8722;2</text>
<text x="460" y="170">rack &#183; lees to lees tank</text><text x="940" y="170" text-anchor="end">&#8722;58</text>
<text x="460" y="194" fill="#4a6b64">observe &#183; dip reads 4,920 (book 4,980)</text><text x="940" y="194" text-anchor="end" fill="#4a6b64">0</text>
<text x="460" y="218" fill="#00695c" font-weight="700">adjust &#183; reason: barrel topping from tank 12 not logged</text><text x="940" y="218" text-anchor="end" fill="#00695c" font-weight="700">&#8722;60</text>
</g>
<line x1="460" y1="232" x2="940" y2="232" stroke="#4db6a2" stroke-width="1"/>
<text x="460" y="252" font-size="12" font-weight="700" fill="#06483f">balance = sum of events</text><text x="940" y="252" text-anchor="end" font-size="12" font-weight="700" fill="#06483f">4,920</text>
<rect x="40" y="276" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="301" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">SAME CLOSING NUMBER &#183; ONLY ONE OF THEM CAN TELL YOU WHY</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Both books end at 4,920 litres. The ledger is the only one that can answer the auditor, or the agent.</figcaption>
</figure>

Tank 12 should hold 4,980 litres. The cellar hand dips it and reads 4,920. The system has a volume field, so they type in 4,920 and carry on with their morning. That is a perfectly reasonable thing to do on a busy day. It also means 60 litres of wine have now left the winery's records with no reason, no date of loss and no way to find out later.

Multiply that by a hundred vessels and a harvest's worth of topping, racking and blending, and you get the familiar end-of-year hunt for missing wine. The [first post in this series]({{ '/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) was about a metric that was never defined. This one is about a quantity that was never allowed to have a history.

## Stored state versus derived state

Most cellar software, and nearly every cellar spreadsheet, stores **state**: the current volume in each vessel. Movements happen, and someone updates the state to match. The movement itself is either recorded somewhere else or not at all.

Event sourcing turns that round. You store the **movements**, and you never store the volume. Every change to the cellar is an event:

- receive (from the press, a truck, another site)
- transfer and blend (vessel to vessel, with lot composition)
- top, rack, filter, fine
- sample and lab use
- bottle (out to finished goods)
- observe (a dip or gauge reading, which changes nothing by itself)
- adjust (the gap between observed and calculated, with a required reason)

The volume in any vessel at any moment is a query: the sum of every event up to that time. Nobody edits it because there is nothing to edit.

```sql
SELECT vessel_id,
       SUM(signed_volume_l_20c) AS volume_l
FROM   cellar_movements
WHERE  event_ts <= :as_of
GROUP  BY vessel_id;
```

Change `:as_of` and you have the cellar at the end of any day in the last five years. That is the query every excise return, every audit and every "where did the Grenache go" conversation actually wants.

## The detail that catches everyone: litres at what temperature?

Notice the column name above: litres at 20 degrees C. Wine expands as it warms, at something like 0.02 to 0.03 percent per degree. A 5,000 litre tank read at 10 degrees and again at 20 degrees differs by roughly 10 to 15 litres with no wine going anywhere.

In a stored-state system, that difference turns up as a mystery loss or gain the first warm week of spring. In an event model, every observation carries its temperature, the pipeline corrects it to the reference temperature before comparing it to the book, and the thermal wobble never becomes an adjustment. It is a small thing. It is also the sort of thing that makes a cellar master stop trusting the system in their first month.

## Building it in the lakehouse

None of this needs exotic tooling. An append-only table in whatever lakehouse you already run (Delta in Fabric or Databricks, Iceberg in Snowflake) does the job. A few rules keep it honest:

1. **Append only, enforced.** Grant insert but not update or delete on the movement table. Corrections are reversing events: a minus 500 to cancel a wrong plus 500, then the right one. The mistake stays visible, which is the point.
2. **Reasons are mandatory on adjustments.** A data contract rejects an adjust event with an empty reason. "Unknown" is allowed. Blank is not.
3. **Capture at the source if you can.** If a winery system already exists, change data capture (Debezium, Fabric mirroring or the vendor's own feed) can turn its updates into events, so you are not asking the cellar to learn a new app during harvest.
4. **Snapshot for speed, never for truth.** A nightly balance table is fine for dashboards. It is rebuilt from the events and never edited.

Lakehouse time travel is sometimes offered as a shortcut. It is not the same thing. Time travel shows you what the table looked like. An event ledger tells you what happened in the cellar. Only the second one answers why.

## Why this matters for GenAI

This is where the old-fashioned data model pays for the new-fashioned tools.

**An agent can only explain what was recorded.** Ask a GenAI assistant "why is tank 12 down 60 litres?" On a stored-state system, it has two volume snapshots and nothing in between, so it either says it does not know or, worse, invents a plausible story about evaporation. On a movement ledger, it reads the events, finds the adjustment and quotes the reason with the operator and timestamp. Same model, same prompt. The difference is entirely in the data.

**Agents should propose, never write.** The obvious next step is to let an agent do data entry: read the cellar work order and log the movements. That is useful and a bit frightening. The append-only design makes it safe to try. The agent drafts events into a pending table with its reasoning attached ("work order 4417 says top B-17 from tank 12, 40 L"). A person approves them, and only then are they appended. If an approved event turns out wrong, it gets reversed like any other. Nothing the agent does can quietly overwrite the book.

**Tool calls get simple.** If you expose the cellar to an agent through a small set of tools, the event model tells you exactly what they are: `balance(vessel, as_of)`, `history(vessel, from, to)`, `propose_movement(...)`. There is no `set_volume`. The missing tool is the safety feature.

## Where this breaks

**It is only as complete as the recording.** If topping during a busy week goes on a whiteboard and never into the system, the ledger will show an adjustment every time. That is still better than silence, because the adjustment reasons tell you where the recording habit is weak, but it does not invent the missing events.

**Flow meters and dips disagree.** A transfer measured by a flow meter and the same transfer measured by dipping both vessels will not match exactly. Decide which is the reference for which movement type and record the other as an observation.

**Harvest is chaos.** During crush, events arrive late and out of order. The model has to accept backdated events with a recorded entry time as well as an event time, or the cellar will simply stop using it until November.

**Migration is not free.** Moving from a stored-state system means starting from an opening balance event per vessel. History before that date stays as unexplained as it always was.

## The bottom line

A volume you can edit is a volume that can lose its story. A volume you calculate from movements keeps it. The event ledger is an old idea (it is how accountants have kept books for centuries), and it happens to be exactly what a GenAI agent needs: real provenance to explain, and a hard wall against rewriting the past. The wine was always moving. The data model just has to admit it.

Next in the series: [the loss map]({{ '/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}), where these events become a waterfall from crush to bottle and an LLM drafts the variance note. For the sensors that feed these events, see [IoT in the Winery]({{ '/2026/iot-in-the-winery-sensors-process/' | relative_url }}). The full list is on the [Cellar Ledger series page]({{ '/series/cellar-ledger/' | relative_url }}).

## Frequently asked questions

**What is event sourcing in a winery data model?**
Instead of storing each tank's volume as a field that people edit, you store every movement as an immutable event: receipt, transfer, topping, racking, blend, filtration, bottling, sample, loss. The volume in any vessel at any moment is the sum of the events up to that moment. Nothing is overwritten, so every litre has a history.

**How do you handle a dip reading that disagrees with the book volume?**
Record the dip as an observation, not as a new volume. If it differs from the calculated balance, the difference becomes its own adjustment event with a required reason, such as evaporation, topping not recorded or meter error. The book is corrected by an event, never by an edit, so the gap stays visible and explainable.

**Should an AI agent be allowed to update winery inventory?**
It should be allowed to propose, not to write. Let the agent read the movement ledger and draft a movement or an adjustment with its reasoning attached, then have a person approve it before it is appended. Because the ledger is append-only, even an approved mistake is fixed with a reversing event and never disappears.
