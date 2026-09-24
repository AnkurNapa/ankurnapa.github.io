---
layout: post
title: "Classic AI for OpEx: Predictive Maintenance, Soft Sensors and Anomaly Detection on Top of SPC"
image: /assets/og/classic-ai-opex-predictive-maintenance-soft-sensors-spc.png
description: "Part 5 of AI for Operational Excellence in Beverage Plants. The machine learning that already pays in beverage plants: predictive maintenance on fillers and pasteurisers, soft sensors for what you cannot measure in line, multivariate anomaly detection layered on SPC, and energy and water per hectolitre against a fair baseline."
date: 2026-09-20 09:00:00 -0700
updated: 2026-09-20
tags: [brewing-science, ai-opex, machine-learning, predictive-maintenance, operational-excellence]
faq:
  - q: "What data do you need for predictive maintenance on a filler or pasteuriser?"
    a: "Condition data from the asset, such as vibration, motor current, temperatures and pressures, stored at a useful frequency in a historian, and a maintenance history from the CMMS that records what failed and when. Without failure records you can still detect abnormal behaviour, but you cannot learn how far ahead a failure is coming."
  - q: "Does machine learning replace statistical process control?"
    a: "No. SPC stays as the simple, auditable baseline for single variables, such as fill volume or PU. Machine learning adds a layer for patterns across many signals at once that no single control chart shows. If a model cannot beat SPC on a problem, use SPC."
  - q: "How do you track energy and water per hectolitre fairly?"
    a: "Compare actual use against a baseline that accounts for what drives it: volume produced, product and pack mix, and ambient temperature. A simple regression baseline, of the kind used in energy management standards, shows whether a week was genuinely good or just busy. The gap between actual and baseline is the number to act on."
---

**Short answer: before generative AI, there was already plenty of machine learning that paid its way in beverage plants, and it still does. Predictive maintenance watches the vibration and current on fillers, pasteuriser pumps and conveyors and warns days before a failure. Soft sensors estimate values you cannot measure in line, from the ones you can. Multivariate anomaly detection catches patterns across dozens of signals that no single control chart shows, with SPC kept underneath as the baseline. And energy and water per hectolitre only mean something against a baseline that knows how busy you were. None of this is new. All of it depends on the data foundations from the previous post.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A layered stack for classic AI in a beverage plant. At the bottom, data sources: historian, MES stop log, CMMS and LIMS. Above that, the baseline layer of rules and SPC: interlocks, PU calculation, control charts on fill volume. Above that, the machine learning layer with four uses: predictive maintenance on filler and pasteuriser, soft sensors, multivariate anomaly detection, and energy and water baselines. At the top, people act: planners, operators and engineers. A note says machine learning adds to the baseline layer and never replaces it.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">CLASSIC AI IN A BEVERAGE PLANT: ML ON TOP OF THE BASELINE</text>
<g font-family="sans-serif">
<rect x="40" y="50" width="920" height="44" rx="9" fill="#06483f"/>
<text x="500" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">PEOPLE ACT: planners, operators, engineers</text>
<rect x="40" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="150" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">predictive maintenance</text>
<text x="150" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">filler, pasteuriser, conveyors</text>
<rect x="273" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="383" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">soft sensors</text>
<text x="383" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">estimate the unmeasured</text>
<rect x="506" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="616" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">multivariate anomalies</text>
<text x="616" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">many signals at once</text>
<rect x="740" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="850" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">energy &amp; water</text>
<text x="850" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">per hl, against a baseline</text>
<rect x="40" y="188" width="920" height="50" rx="9" fill="#4db6a2"/>
<text x="500" y="210" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">BASELINE: rules and SPC</text>
<text x="500" y="228" text-anchor="middle" font-size="10.5" fill="#06483f">interlocks &#183; PU calculation &#183; control charts on fill volume and CO2</text>
<rect x="40" y="250" width="920" height="44" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="500" y="277" text-anchor="middle" font-size="11.5" fill="#06483f">DATA: historian &#183; MES stop log &#183; CMMS &#183; LIMS</text>
<text x="500" y="318" text-anchor="middle" font-size="11" fill="#4a6b64">machine learning adds a layer on top of the baseline &#183; it never replaces it</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Four uses of classic machine learning, each standing on rules, SPC and joined data.</figcaption>
</figure>

When people hear "AI in the plant" in 2026, they picture a chatbot. The AI that has been saving money in beverage plants for the last decade looks nothing like a chatbot. It is a model watching vibration on a pasteuriser pump, a regression predicting a lab value, a chart that flags an odd pattern at 4 a.m. It is quiet, specific and measurable, which is exactly why it works.

This is the fifth post in the series. The [previous post]({{ '/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}) set out OEE, the six big losses and where the data lives. This one covers the machine learning rung of the [AI ladder]({{ '/2026/what-is-ai-ladder-rules-to-agi-beverage-plant/' | relative_url }}) in four uses that reliably pay.

## Predictive maintenance on fillers and pasteurisers

Breakdowns are the first of the six big losses and usually the most painful, because they arrive without warning and often mid-run. Predictive maintenance tries to give that warning.

The data is two-sided:

- **Condition signals** from the asset: vibration on pump and motor bearings, motor current, temperatures, pressures, cycle counts. On a tunnel pasteuriser, the circulation pumps, the spray headers and the heat exchangers are the usual candidates. On a filler, the main drive, the vacuum pump and the valves.
- **Failure history** from the CMMS: what failed, when, and what was done.

With both, a model can learn what the signals looked like in the days before past failures and flag the same pattern early. Without failure history, you can still do something useful: learn what normal looks like and flag drift from it. That is anomaly-based maintenance, and it is where most plants should start, because clean failure records are rare.

The payoff is not the prediction itself. It is turning an unplanned breakdown into a planned repair during a scheduled stop. I went into the packaging side in more depth in [Predictive Maintenance for Fillers and Seamers]({{ '/2024/predictive-maintenance-filler-seamer/' | relative_url }}).

## Soft sensors: estimating what you cannot measure in line

A soft sensor estimates a value that is hard or slow to measure directly, from signals that are easy to measure.

It helps to see where the ladder starts. Pasteurisation units are a calculation, not a model. By the usual convention, one minute at 60 degrees C is 1 PU, and each degree above that multiplies the rate by about 1.393. So a minute at 62 degrees gives about 1.94 PU, and ten minutes there about 19.4. That is physics and a rule, on the bottom rung, and it should stay there.

The machine learning version comes in where the physics is incomplete. The PU that matters is the one the product inside the pack received. What you measure is the spray water temperature in each zone. A soft sensor trained on data from test runs with a travelling temperature logger can estimate the in-pack temperature, and so the PU, for every pack, not just the test ones. Similar ideas estimate dissolved CO2 or oxygen pickup between lab samples, or a fermentation's remaining extract between gravity readings.

The rule for soft sensors: they estimate, the reference method confirms. They tell you where to look and when to sample, not what to release.

## Anomaly detection on top of SPC

SPC, from the previous post, is excellent at watching one variable at a time: fill volume, crown crimp, PU. Its blind spot is patterns that only show across several signals together. A filler bowl pressure that is slightly high, a product temperature that is slightly low and a CO2 reading that is slightly off may each be inside their control limits while together describing a process that has changed.

Multivariate anomaly detection covers that gap. Methods range from the long-established (principal component analysis with a Hotelling T squared chart, used in process industries for decades) to newer ones such as isolation forests or autoencoders. They learn the normal relationship between many signals and flag when it breaks.

Two practical rules:

- **Keep SPC as the baseline.** It is simple, auditable and trusted. Anomaly detection is a second layer, and if it cannot find anything SPC misses on your process, you do not need it.
- **Budget the alarms.** Every anomaly flag costs someone's attention. A model that flags twenty things a shift will be ignored by Wednesday. Tune it to a handful of high-quality flags, each with the signals that drove it.

## Energy and water per hectolitre, against a fair baseline

Every beverage plant tracks energy and water per hectolitre, and many find the numbers frustrating. A good week often looks bad and a bad week good, because the ratio moves with volume, product mix, pack mix, cleaning schedules and the weather.

The fix is a baseline that knows about those drivers. A regression of, say, weekly thermal energy against volume packed, the share of returnable glass (with its bottle washer) and ambient temperature gives an expected value for each week. The number to watch is the gap between actual and expected, not the raw ratio. Energy management standards use exactly this approach, and it is machine learning of the most modest kind.

Once the baseline exists, the anomaly methods above apply: a week, a shift or a CIP cycle that uses far more than expected gets flagged and explained. My earlier post on [CIP optimisation for water and chemicals]({{ '/2026/cip-optimisation-water-chemicals-ai/' | relative_url }}) takes the CIP end of this further, and [brewery energy and utilities]({{ '/2024/ai-brewery-energy-utilities-optimization/' | relative_url }}) covers the utility side.

## Where this breaks

**Failure data is thin.** A well-maintained pump may fail once in several years. That is great for the plant and terrible for training a model. Pool similar assets, start with anomaly detection and grow into prediction.

**Sensors drift and get replaced.** A vibration sensor swapped during a repair can look like a sudden change in the asset. Record sensor changes as events, or the model will learn the maintenance calendar instead of the machine.

**Soft sensors age.** A soft sensor trained before a pasteuriser rebuild may be wrong after it. Check it against the reference method on a schedule and retrain when it drifts.

**Baselines can hide real improvement.** If the baseline is retrained every month, a genuine saving slowly becomes the new normal and disappears from the report. Freeze the baseline for a defined period, the way energy standards do.

## The bottom line

The machine learning that pays in beverage plants is not glamorous. It watches pumps, estimates what cannot be measured in line, spots patterns across signals that SPC cannot see alone, and judges energy and water against a fair baseline. Each use stands on rules and SPC underneath, and on joined, clean data below that. Get these right and the generative and agentic layers in the next two posts have something solid to stand on.

Next: [generative AI for OpEx]({{ '/2026/genai-opex-shift-handover-sop-rag-root-cause/' | relative_url }}), where the text of the plant becomes useful. For packaging-line downtime in particular, see [Predicting Packaging Line Downtime and Lifting OEE]({{ '/2024/packaging-line-oee-downtime-prediction/' | relative_url }}). The full list is on the [series page]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Frequently asked questions

**What data do you need for predictive maintenance on a filler or pasteuriser?**
Condition data from the asset, such as vibration, motor current, temperatures and pressures, stored at a useful frequency in a historian, and a maintenance history from the CMMS that records what failed and when. Without failure records you can still detect abnormal behaviour, but you cannot learn how far ahead a failure is coming.

**Does machine learning replace statistical process control?**
No. SPC stays as the simple, auditable baseline for single variables, such as fill volume or PU. Machine learning adds a layer for patterns across many signals at once that no single control chart shows. If a model cannot beat SPC on a problem, use SPC.

**How do you track energy and water per hectolitre fairly?**
Compare actual use against a baseline that accounts for what drives it: volume produced, product and pack mix, and ambient temperature. A simple regression baseline, of the kind used in energy management standards, shows whether a week was genuinely good or just busy. The gap between actual and baseline is the number to act on.
