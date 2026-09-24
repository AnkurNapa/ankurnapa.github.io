---
layout: post
title: "Operational Excellence Basics for Data People: OEE, the Six Big Losses, SPC and Where Plant Data Lives"
image: /assets/og/operational-excellence-basics-oee-for-data-people.png
description: "Part 4 of AI for Operational Excellence in Beverage Plants. Before any AI, the language of the plant: OEE with a worked filler-line example, the six big losses, TPM, the lean wastes, statistical process control, and the ISA-95 map of where the data actually sits (historian, MES, CMMS, LIMS, ERP)."
date: 2026-09-19 09:00:00 -0700
updated: 2026-09-19
tags: [brewing-science, ai-opex, operational-excellence, packaging, data-engineering]
faq:
  - q: "How do you calculate OEE on a bottling line?"
    a: "OEE is availability times performance times quality. Availability is run time divided by planned production time. Performance is the actual count divided by what the line would make at its ideal rate during that run time. Quality is good units divided by total units. A line with 90 percent availability, 83.3 percent performance and 98 percent quality has an OEE of 73.5 percent."
  - q: "What are the six big losses in OEE?"
    a: "Breakdowns and setup or changeover losses reduce availability. Small stops and reduced speed reduce performance. Process defects and start-up rejects reduce quality. Mapping every minute of lost time to one of these six is the first step in any improvement programme, and the first dataset any AI project in a plant needs."
  - q: "Where does production data live in a beverage plant?"
    a: "It is spread across the ISA-95 levels. Sensor and PLC data sits at the control levels and is stored in a historian. Production orders, line stops and batch records usually live in an MES. Maintenance history is in the CMMS, lab results in the LIMS, and orders, stock and costs in the ERP. Most AI projects spend their first months joining these together."
---

**Short answer: operational excellence in a beverage plant runs on a few ideas that every data person should know before touching AI. OEE (availability times performance times quality) turns a shift into one number and, more usefully, into losses you can name. On an illustrative filler line making 40,000 bottles an hour, 90 percent availability, 83.3 percent performance and 98 percent quality give 73.5 percent OEE: 79,500 bottles not made in a single shift. The six big losses say where they went. TPM, lean and SPC are the methods plants already use to get them back. And the data for all of it is scattered across five systems, which is why AI projects in plants are mostly data projects.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="An OEE waterfall for one illustrative shift on a filler line. The line could make 300,000 bottles in 450 minutes of planned time at its ideal rate of 40,000 an hour. Availability loss of 45 minutes of stops costs 30,000 bottles. Performance loss from running slow and small stops costs 45,000 bottles. Quality loss costs 4,500 rejected bottles. 220,500 good bottles remain, which is 73.5 percent OEE. The vertical axis starts at 200,000 bottles.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">ONE SHIFT ON A FILLER LINE, IN BOTTLES (ILLUSTRATIVE)</text>
<g font-family="sans-serif">
<line x1="60" y1="250" x2="960" y2="250" stroke="#4a6b64" stroke-width="1"/>
<text x="60" y="52" font-size="10" fill="#4a6b64">axis starts at 200,000 bottles</text>
<rect x="80" y="70" width="120" height="180" fill="#06483f"/>
<text x="140" y="64" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">300,000</text>
<rect x="260" y="70" width="120" height="54" fill="#4db6a2"/>
<text x="320" y="142" text-anchor="middle" font-size="12" fill="#06483f">&#8722;30,000</text>
<rect x="440" y="124" width="120" height="81" fill="#4db6a2"/>
<text x="500" y="223" text-anchor="middle" font-size="12" fill="#06483f">&#8722;45,000</text>
<rect x="620" y="205" width="120" height="8.1" fill="#ff4081"/>
<text x="680" y="232" text-anchor="middle" font-size="12" fill="#ff4081">&#8722;4,500</text>
<rect x="800" y="213.1" width="120" height="36.9" fill="#06483f"/>
<text x="860" y="205" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">220,500</text>
<g font-size="10.5" fill="#4a6b64" text-anchor="middle">
<text x="140" y="268">ideal output in</text><text x="140" y="282">planned time</text>
<text x="320" y="268">availability loss</text><text x="320" y="282">45 min of stops</text>
<text x="500" y="268">performance loss</text><text x="500" y="282">slow running, small stops</text>
<text x="680" y="268">quality loss</text><text x="680" y="282">rejects</text>
<text x="860" y="268">good bottles</text><text x="860" y="282">73.5% OEE</text>
</g>
<rect x="40" y="298" width="920" height="32" rx="8" fill="#06483f"/>
<text x="500" y="319" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">A = 90% &#183; P = 83.3% &#183; Q = 98% &#183; OEE = 73.5% &#183; 79,500 BOTTLES NOT MADE</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative shift. The biggest bar is often performance, the loss nobody writes down because the line never actually stopped.</figcaption>
</figure>

Data people arriving in a beverage plant tend to ask for "the data" and then build a model. Plant people tend to watch this happen with polite patience, because the plant already has a language for improvement, and the model does not speak it.

This is the fourth post in the series and the bridge between the AI basics in the first three and the applications in the last four. If you come from data, this is the plant's vocabulary. If you come from the plant, it is how to explain it to your data team.

## OEE: one number, three questions

Overall equipment effectiveness asks three questions about a line in a period:

- **Availability:** of the time we planned to run, how much did we actually run?
- **Performance:** while running, how close to the ideal rate did we go?
- **Quality:** of what we made, how much was good?

OEE is the three multiplied together. Here is an illustrative shift on a filler rated at 40,000 bottles an hour:

```python
planned_min = 450 # 8 h shift less a 30 min planned break
stops_min = 20 + 15 + 10 # changeover overrun, filler jams, labeller faults
run_min = planned_min - stops_min # 405
ideal_per_min = 40_000 / 60 # 666.7 bottles a minute
total, good = 225_000, 220_500 # 4,500 rejects

availability = run_min / planned_min # 0.900
performance = total / (run_min * ideal_per_min) # 0.833
quality = good / total # 0.980
oee = availability * performance * quality # 0.735
```

73.5 percent. The number on its own is not very useful. What matters is that the same calculation, done in bottles, tells you where the losses went. At its ideal rate over 450 minutes, the line could have made 300,000 bottles. It made 220,500 good ones. Of the 79,500 missing, 30,000 were lost to stops, 45,000 to running slowly or stuttering, and 4,500 to rejects.

The biggest bar is performance, and that is common. A line that is running, just slowly, or stopping for twenty seconds at a time, rarely makes it into anyone's notes. It is also where a lot of the easy gains are.

You will often hear 85 percent quoted as "world class". Treat it as a rule of thumb, not a standard. OEE depends on how you define planned time and ideal rate, and two plants that define them differently cannot compare their numbers. Compare a line with itself over time.

## The six big losses

Total productive maintenance, or TPM, sorts every lost minute into six buckets, two for each part of OEE:

| OEE factor | Loss | Beverage line example |
|---|---|---|
| Availability | Breakdowns | Filler valve failure, seamer fault |
| Availability | Setup and changeover | Label or pack format change, flavour change with a flush |
| Performance | Small stops and idling | Bottle jams at the starter wheel, a sensor misread |
| Performance | Reduced speed | Running the labeller slow because it misbehaves at full rate |
| Quality | Process defects | Low fills, crooked labels, poor crimps |
| Quality | Start-up rejects | Product lost at the start of a run or after a stop |

This table is the most important dataset in any plant AI project. If line stops are recorded with sensible reason codes that map to these six, almost every idea in the rest of this series becomes possible. If half the stops are coded "other", none of them is.

## TPM, lean and SPC in one paragraph each

**TPM** is the maintenance side of OpEx: operators doing basic care of their own equipment, planned maintenance based on condition and history, and a steady focus on eliminating the six losses. It is where predictive maintenance fits.

**Lean** is about removing waste from the whole flow. The classic list of wastes (transport, inventory, motion, waiting, overproduction, over-processing and defects, with unused skills often added as an eighth) is a useful lens for a packaging hall. A pallet of empty cans waiting two days is inventory. An operator walking to a distant printer for every batch sheet is motion.

**SPC**, statistical process control, watches whether a process is behaving normally. A control chart plots, say, fill volume over time with limits calculated from the process's own variation. Points outside the limits, or unusual runs of points inside them, signal that something has changed. SPC has quietly run beverage quality for decades, and it is the baseline any AI anomaly detection has to beat.

## Where the data lives

The ISA-95 model describes the layers of a manufacturing plant, and it is a good map of where your data sits:

- **Levels 0 to 2, the process and its control.** Sensors, PLCs, SCADA and HMIs. The readings are usually stored in a **historian**: temperatures, pressures, flows, speeds and counts, second by second.
- **Level 3, manufacturing operations.** The **MES** holds production orders, line states, stop reasons and batch records. The **CMMS** holds maintenance work orders and asset history. The **LIMS** holds lab results.
- **Level 4, business planning.** The **ERP** holds orders, stock, costs and the production plan.

Most plants have all five and few have them joined. The filler's stop events are in the MES, its vibration in the historian, its repair history in the CMMS and its reject samples in the LIMS. Answering "why did line 2 lose 40 minutes?", the question from the [previous post]({{ '/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}), needs at least three of them.

That is the honest reason AI projects in plants take longer than expected. The model is a few weeks. Joining the systems, agreeing the definitions and cleaning the stop codes is a few months. It is the same lesson as the [winery data foundations in the Cellar Ledger]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }}): the data model comes first.

## Where this breaks

**OEE can be gamed.** Change what counts as planned time, or lower the ideal rate, and OEE rises without a single extra bottle. Fix the definitions and publish them.

**Stop codes are only as good as the person entering them at 3 a.m.** Too many codes and operators pick the first one. Too few and everything is "other". Automatic stop detection from the PLC plus a short, well-chosen reason list works better than either.

**Averages hide the losses.** A weekly OEE of 75 percent can hide one terrible shift and several good ones. Look at the distribution, by shift, by product and by format.

**SPC limits must come from a stable process.** Calculate control limits from a period when the process was out of control and the chart will call chaos normal.

## The bottom line

OEE turns a shift into availability, performance and quality, and then into bottles you can count. The six big losses say where they went. TPM, lean and SPC are how plants have always fought back, and the data to support them lives in a historian, an MES, a CMMS, a LIMS and an ERP that rarely talk to each other. Every AI idea in the rest of this series stands on that foundation. Get the stop codes right and the systems joined, and the AI part becomes the easy bit.

Next: [classic AI for OpEx]({{ '/2026/classic-ai-opex-predictive-maintenance-soft-sensors-spc/' | relative_url }}), predictive maintenance, soft sensors and anomaly detection on top of SPC. For the Tableau view of line OEE, see [Visualising Packaging-Line OEE in Tableau]({{ '/2023/tableau-packaging-line-oee-dashboard/' | relative_url }}). The full list is on the [series page]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Frequently asked questions

**How do you calculate OEE on a bottling line?**
OEE is availability times performance times quality. Availability is run time divided by planned production time. Performance is the actual count divided by what the line would make at its ideal rate during that run time. Quality is good units divided by total units. A line with 90 percent availability, 83.3 percent performance and 98 percent quality has an OEE of 73.5 percent.

**What are the six big losses in OEE?**
Breakdowns and setup or changeover losses reduce availability. Small stops and reduced speed reduce performance. Process defects and start-up rejects reduce quality. Mapping every minute of lost time to one of these six is the first step in any improvement programme, and the first dataset any AI project in a plant needs.

**Where does production data live in a beverage plant?**
It is spread across the ISA-95 levels. Sensor and PLC data sits at the control levels and is stored in a historian. Production orders, line stops and batch records usually live in an MES. Maintenance history is in the CMMS, lab results in the LIMS, and orders, stock and costs in the ERP. Most AI projects spend their first months joining these together.
