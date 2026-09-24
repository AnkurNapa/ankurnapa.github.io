---
layout: post
title: "Soft Sensors and Proactive Bands Instead of Alarms at the Spirit Safe"
image: /assets/og/soft-sensors-proactive-bands-spirit-safe.png
description: "Part 2 of The Still and the Model. Estimate distillate strength between hydrometer readings from temperatures and flow, compare every run with a band built from good runs, and flag drift while there is still time to act. Why this beats another fixed alarm on a panel the operator has learned to ignore."
date: 2026-07-27 09:00:00 -0700
updated: 2026-07-27
tags: [distilling-maturation, still-and-model, soft-sensors, machine-learning, data-engineering]
faq:
  - q: "What is a soft sensor in a distillery?"
    a: "A soft sensor estimates something you cannot measure continuously, such as distillate strength, from things you can, such as vapour temperature, pot temperature, pressure and flow. It is recalibrated against a real measurement, like the spirit safe hydrometer, whenever one is taken. It fills the gaps between readings; it does not replace the reference."
  - q: "What is a proactive band on a still run?"
    a: "It is an envelope built from the distillery's own good runs, showing where strength, temperature or flow normally sit at each stage of a run. A new run is compared with the band continuously. When it starts to leave the band, the operator is told early, often well before any fixed alarm threshold is crossed."
  - q: "Why do distillery operators ignore alarms?"
    a: "Because there are too many of them and most do not need action. Alarm management guidance such as EEMUA 191 and ISA-18.2 treats a flood of alarms as a safety problem in itself. Each nuisance alarm teaches the operator that alarms can be acknowledged and forgotten, which is exactly the wrong lesson when a real one arrives."
---

**Short answer: the hydrometer in the spirit safe is the truth, but it is read by eye and not every minute. Between readings, a soft sensor can estimate strength from vapour and pot temperatures, pressure and flow, and recalibrate each time the stillman takes a reading. Compare the estimate with a band built from the distillery's own good runs, indexed by how far through the run you are rather than by clock time, and you flag a drifting run early, while there is still time to adjust. A fixed low-strength alarm tells you the same thing twenty minutes later, on a panel the operator has already learned to silence.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A band chart for a spirit run. The horizontal axis is the share of charge alcohol recovered, the vertical axis is distillate strength. A shaded band built from good runs slopes downwards. A normal run stays inside it. A drifting run leaves the lower edge of the band around the middle of the run, where a pink marker says the band flags it. The same run only crosses a fixed low-strength alarm line much later, where a second marker says the alarm fires.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE BAND SEES THE DRIFT BEFORE THE ALARM DOES (ILLUSTRATIVE)</text>
<g font-family="sans-serif">
<line x1="100" y1="280" x2="910" y2="280" stroke="#4a6b64" stroke-width="1"/>
<line x1="100" y1="60" x2="100" y2="280" stroke="#4a6b64" stroke-width="1"/>
<text x="505" y="302" text-anchor="middle" font-size="10.5" fill="#4a6b64">share of charge alcohol recovered &#8594;</text>
<text x="88" y="170" text-anchor="middle" font-size="10.5" fill="#4a6b64" transform="rotate(-90 88 170)">strength at the safe</text>
<polygon points="100,80 300,100 500,130 700,175 900,235 900,265 700,205 500,160 300,128 100,105" fill="#f0f6f5" stroke="#4db6a2" stroke-width="1"/>
<polyline points="100,92 300,114 500,145 700,190 900,250" fill="none" stroke="#06483f" stroke-width="2.5"/>
<polyline points="100,92 300,118 400,140 500,172 600,200 700,228" fill="none" stroke="#ff4081" stroke-width="2.5"/>
<line x1="100" y1="225" x2="900" y2="225" stroke="#4a6b64" stroke-width="1.5" stroke-dasharray="6 5"/>
<text x="905" y="219" text-anchor="end" font-size="10.5" fill="#4a6b64">fixed low-strength alarm</text>
<circle cx="450" cy="156" r="7" fill="none" stroke="#ff4081" stroke-width="2.5"/>
<text x="450" y="196" text-anchor="middle" font-size="11" font-weight="700" fill="#ff4081">band flags here</text>
<circle cx="690" cy="225" r="7" fill="none" stroke="#06483f" stroke-width="2.5"/>
<text x="690" y="252" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">alarm fires here</text>
<text x="230" y="76" font-size="10.5" fill="#00695c">band from good runs</text>
<text x="780" y="170" font-size="10.5" fill="#06483f">normal run</text>
<rect x="40" y="312" width="920" height="24" rx="6" fill="#06483f"/>
<text x="500" y="329" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">SAME RUN, SAME DATA &#183; ONE OF THEM LEAVES TIME TO ACT</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative shape. The band is built from your own good runs, and the x axis is progress through the run, not the clock.</figcaption>
</figure>

On a spirit still, the most important number in the building is read through glass. The stillman looks at the hydrometer floating in the spirit safe, corrects for temperature and writes it down. That reading is the reference. It is also periodic, taken by a person who has four other things to do, and on a busy shift the gap between readings grows.

The [previous post]({{ '/2026/physics-informed-digital-twin-pot-still/' | relative_url }}) built a twin that knows where a run should go. This one is about watching a live run against that expectation, without adding to the pile of alarms nobody reads.

## The soft sensor: strength between readings

A soft sensor estimates something you cannot measure continuously from things you can. On a pot still, the useful inputs are already on most historians:

- **Pot liquid temperature.** At a given pressure, the boiling temperature of ethanol and water tracks the composition of the liquid in the pot.
- **Vapour temperature at the lyne arm or column head.** This tracks the composition of the vapour leaving.
- **Barometric pressure.** Boiling points move with the weather. A strong front can shift them by several tenths of a degree, which is enough to fool a naive estimate.
- **Distillate flow and cumulative volume**, to know how far through the run you are.

A physics-based estimate from the equilibrium data, corrected by the fitted parameters from the twin, gives strength every few seconds. Then comes the part that makes it trustworthy: every time the stillman takes a hydrometer reading, the soft sensor compares its estimate with the reading and corrects its bias. The reading stays the reference. The soft sensor fills the gaps between readings, and its error against the last reading is displayed next to it, so nobody forgets which number is measured and which is estimated.

The data engineering is small but it matters. Store the hydrometer readings with their timestamp, temperature and the person who took them, in the same timeline as the historian tags. A soft sensor that cannot line up its estimate with the reading, to the minute, cannot recalibrate.

## The band: compare with good runs, not with a threshold

A fixed alarm asks one question: has strength fallen below X? By the time it has, the run has been drifting for a while.

A band asks a better question: is this run behaving like our good runs did at this point? To build one:

1. **Pick the good runs.** The last thirty or fifty runs that the team agrees went well, on the same still and the same charge type.
2. **Index them by progress, not time.** Runs vary in length with heat input and charge size. Plot each run against the share of charge alcohol already collected, from the twin's balance, so every run is on the same scale.
3. **Take the median and a robust spread** at each step (median absolute deviation rather than standard deviation, so one odd run does not widen the band for everyone).
4. **Compare the live run continuously** and flag it when it leaves the band, or is heading out of it faster than a good run ever did.

In the illustrative chart, the drifting run leaves the band a third of the way before the fixed alarm would fire. That gap is the useful part. It is the time to check the steam, look at the condenser water or take an early hydrometer reading.

Bands work for more than strength. Condenser outlet temperature, steam flow and distillate flow each get their own band. A run that drifts on two of them at once is far more interesting than one that brushes the edge of one.

## Why fewer alarms is the goal

Alarm management has a whole literature, and its central finding is uncomfortable: more alarms make plants less safe. Guidance such as EEMUA 191 and ISA-18.2 aims for something like one alarm every ten minutes per operator in steady operation, and treats floods above that as a problem in their own right. Every alarm that fires and needs no action teaches the operator that alarms can be acknowledged and forgotten.

So the band should replace alarms, not join them. A good rule for a distillery rolling this out:

- **Keep safety alarms and interlocks exactly as they are.** High pressure, high temperature and vapour detection are not analytics problems.
- **Retire the nuisance process alarms** the band covers, one at a time, once the band has shown it catches the same events earlier.
- **Make band flags advisory and quiet.** A colour change and a note on the operator screen, not a horn.
- **Review every flag weekly** for the first few months. A band that flags too often is too narrow. One that never flags is too wide.

## Where this breaks

**The band learns your habits, good and bad.** If the good runs were all a little too fast, the band makes too fast normal. Choose the reference runs deliberately, and rebuild the band when the process changes on purpose.

**Soft sensors drift between readings.** A fouled temperature probe or a changed steam supply shifts the estimate, and the band cannot tell a real drift from a bad probe. That is why the hydrometer reading stays the reference and why the soft sensor's error against it is always on screen.

**Start and end of run are hardest.** Foreshots and the tail of the run are where the equilibrium model is weakest and where operators rely most on nose and experience. Use bands for the middle of the run, where the physics is well behaved.

**It does not make the cut.** A band tells you a run is unusual. It does not tell you where to cut for flavour. That stays with the stillman, as the [cut points post]({{ '/2024/predicting-distillation-cut-points-ai/' | relative_url }}) argues.

## The bottom line

The spirit safe hydrometer is the truth, and it is read by a person at intervals. A soft sensor fills the gaps and stays honest by recalibrating against every reading. A band built from your own good runs shows drift while there is still time to act, and it lets you retire alarms instead of adding them. The goal is not a smarter horn. It is a quieter panel where the few signals that remain are worth looking at.

Next in the series: [an LLM copilot for the still operator]({{ '/2026/llm-copilot-still-operator/' | relative_url }}), which reads the same data and never touches a setpoint. For the sensors themselves, see [IoT in the Distillery]({{ '/2026/iot-in-the-distillery-sensors-process/' | relative_url }}). The full list is on [The Still and the Model series page]({{ '/series/still-and-model/' | relative_url }}).

## Frequently asked questions

**What is a soft sensor in a distillery?**
A soft sensor estimates something you cannot measure continuously, such as distillate strength, from things you can, such as vapour temperature, pot temperature, pressure and flow. It is recalibrated against a real measurement, like the spirit safe hydrometer, whenever one is taken. It fills the gaps between readings; it does not replace the reference.

**What is a proactive band on a still run?**
It is an envelope built from the distillery's own good runs, showing where strength, temperature or flow normally sit at each stage of a run. A new run is compared with the band continuously. When it starts to leave the band, the operator is told early, often well before any fixed alarm threshold is crossed.

**Why do distillery operators ignore alarms?**
Because there are too many of them and most do not need action. Alarm management guidance such as EEMUA 191 and ISA-18.2 treats a flood of alarms as a safety problem in itself. Each nuisance alarm teaches the operator that alarms can be acknowledged and forgotten, which is exactly the wrong lesson when a real one arrives.
