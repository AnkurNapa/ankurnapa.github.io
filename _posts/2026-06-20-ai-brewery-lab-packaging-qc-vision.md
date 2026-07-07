---
layout: post
title: "Machine Vision on the Packaging Line"
image: /assets/og/ai-brewery-lab-packaging-qc-vision.png
description: "Inline machine vision on the brewery packaging line: fill-level checks with SPC to catch drift, crown-seal and label-defect inspection, washed-bottle grading, and pasteurisation-unit modelling from tunnel temperatures."
date: 2026-06-20 09:00:00 -0700
updated: 2026-06-20
tags: [brewing-science, brewery-lab-ai, computer-vision, packaging, quality-control]
faq:
  - q: "Can computer vision reliably check fill levels on a fast packaging line?"
    a: "Yes, within limits. A camera under fixed lighting can read fill height or volume on every container at line speed, far more consistently than a manual spot check on a handful of packs an hour. The value comes from feeding those readings into a statistical process control chart so you catch a filler drifting toward under- or over-fill before it crosses spec, not from the single-pack pass or fail. The catch is that vision needs stable lighting and fixturing on a wet, reflective line, and a missed defect at line speed ships at scale, so the system needs monitoring, not blind trust."
  - q: "How does AI inspect crown seals and labels?"
    a: "As image classification. A camera photographs each bottle neck and a trained classifier grades the crown crimp as sound or suspect from the seal geometry; a second station grades the label for placement, skew, wrinkle, and condensate. It is the same looking-closely job a line inspector does, done on every container without fatigue. It flags suspect packs for a human or a reject gate; it does not replace the periodic secure-seal and torque tests that remain the reference for pack integrity."
  - q: "Can AI calculate pasteurisation units on the line?"
    a: "It can model them. Pasteurisation units accumulate from time and temperature through the tunnel, so a model reading the zone temperatures can estimate PU delivered to each pack and flag under- or over-pasteurised product in real time. That model is only as trustworthy as the temperature instrumentation feeding it: a drifted or badly placed probe gives a confident PU number that is wrong, so the tunnel data logger and periodic PU verification stay the arbiter."
---

**Short answer: the packaging line is where machine vision earns its keep most obviously, because the work is already visual: a line inspector watching fills, squinting at crown crimps, catching a skewed label, pulling washed bottles for a residue check. A camera under fixed lighting does that looking on every single container at line speed instead of a handful per hour, and the durable win comes when those readings feed a statistical process control chart that flags a filler or a labeller drifting toward spec before it crosses it. Pasteurisation is the same story in temperature rather than pixels: model the units delivered from the tunnel zones and flag the under- and over-cooked packs live. None of it replaces the secure-seal test, the reference PU verification, or the release call, and a vision system that misses a defect fails silently and at scale, so every station buys inspection coverage at the price of a monitoring burden. This is part five of the [brewery-lab AI series]({{ '/2026/ai-brewery-lab-what-is-real/' | relative_url }}); the previous post covered [microbiology risk triage]({{ '/2026/ai-brewery-lab-microbiology-risk-triage/' | relative_url }}).**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A packaging conveyor with four inline camera stations, each inspecting one check as containers pass: fill height and volume, crown crimp seal integrity, label placement and wrinkle, and washed-bottle cleanliness. Each station feeds a shared statistical process control chart that flags a drift trend in real time. A maroon banner underneath notes the tradeoff: inline vision runs at line speed, so a missed defect fails silently and monitoring is mandatory.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE PACKAGING LINE: FOUR INLINE VISION STATIONS FEEDING ONE SPC CHART</text>
<g font-family="sans-serif">
<rect x="40" y="150" width="920" height="26" rx="4" fill="#cfe6df" stroke="#00695c" stroke-width="1.2"/>
<text x="500" y="168" text-anchor="middle" font-size="10.5" fill="#4a6b64">conveyor &#183; containers move at line speed &#8594;</text>
<rect x="52" y="58" width="200" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="152" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">FILL CHECK</text>
<text x="152" y="102" text-anchor="middle" font-size="10.5" fill="#4a6b64">height &amp; volume</text>
<text x="152" y="122" text-anchor="middle" font-size="10.5" font-weight="700" fill="#00695c">under / over-fill</text>
<rect x="272" y="58" width="200" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="372" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">CROWN SEAL</text>
<text x="372" y="102" text-anchor="middle" font-size="10.5" fill="#4a6b64">crimp geometry</text>
<text x="372" y="122" text-anchor="middle" font-size="10.5" font-weight="700" fill="#00695c">sound / suspect</text>
<rect x="492" y="58" width="200" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="592" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">LABEL QC</text>
<text x="592" y="102" text-anchor="middle" font-size="10.5" fill="#4a6b64">skew, wrinkle, bond</text>
<text x="592" y="122" text-anchor="middle" font-size="10.5" font-weight="700" fill="#00695c">defect grade</text>
<rect x="712" y="58" width="200" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="812" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">WASH INSPECT</text>
<text x="812" y="102" text-anchor="middle" font-size="10.5" fill="#4a6b64">residue, carry-over</text>
<text x="812" y="122" text-anchor="middle" font-size="10.5" font-weight="700" fill="#00695c">clean / reject</text>
<line x1="152" y1="138" x2="152" y2="150" stroke="#00695c" stroke-width="1.5"/>
<line x1="372" y1="138" x2="372" y2="150" stroke="#00695c" stroke-width="1.5"/>
<line x1="592" y1="138" x2="592" y2="150" stroke="#00695c" stroke-width="1.5"/>
<line x1="812" y1="138" x2="812" y2="150" stroke="#00695c" stroke-width="1.5"/>
<rect x="52" y="196" width="500" height="90" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="72" y="218" font-size="11" font-weight="700" fill="#06483f">SPC CONTROL CHART &#183; every reading, every pack</text>
<line x1="72" y1="262" x2="532" y2="262" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/>
<polyline points="72,258 132,256 192,259 252,252 312,248 372,244 432,238 492,232" fill="none" stroke="#00695c" stroke-width="2"/>
<circle cx="492" cy="232" r="4" fill="#06483f"/>
<text x="500" y="228" font-size="10" font-weight="700" fill="#06483f">DRIFT</text>
<text x="72" y="278" font-size="9.5" fill="#4a6b64">flags the trend before it crosses spec, not the single bad pack</text>
<rect x="572" y="196" width="340" height="90" rx="9" fill="#06483f"/>
<text x="742" y="228" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">INLINE VISION RUNS AT LINE SPEED</text>
<text x="742" y="250" text-anchor="middle" font-size="10" fill="#cfe6df">a missed defect fails silently and ships at scale</text>
<text x="742" y="268" text-anchor="middle" font-size="10" fill="#cfe6df">monitoring is mandatory, not optional</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Four inline stations, one control chart. Vision buys inspection coverage on every pack, at the price of a monitoring burden.</figcaption>
</figure>

The packaging hall is the loudest, wettest, fastest room in the brewery, and it is where a defect is cheapest to catch and most expensive to miss. A short-fill that slips through is a consumer complaint and a duty question; a bad crown is a flat pack or a burst bottle; a skewed label is a rejected pallet at the retailer. Historically this is guarded by a line inspector pulling samples every so often and a QC bench running secure-seal and fill checks on a schedule. That sampling leaves long gaps between checks, and the work, looking closely at a repetitive thing, over and over, under fatigue, is exactly the shape machine vision fits. The point of this post is not that cameras replace the QC bench. It is that they turn a handful of spot checks per hour into a reading on every container, and that the reading is only worth having if you do something statistical with it.

## Fill level: vision plus SPC, not pass/fail

Start with fills, because it is the clearest case. A camera positioned after the filler reads fill height, or estimates fill volume, on every container going past. On its own that is a better version of the manual spot check: more packs seen, no fatigue, consistent judgement. But the real value is upstream of the pass or fail. Feed every fill reading into a statistical process control chart and you stop watching for the single out-of-spec pack and start watching the trend: a filling head slowly drifting low, a valve beginning to hang, the mean creeping toward the lower limit shift by shift. SPC catches drift while the packs are still in spec, which is the whole game: you adjust the filler before it makes bad product, instead of finding the bad product after the fact. Manual spot checks cannot do this; a handful of readings an hour is far too sparse to see a slow trend. Vision makes the data dense enough for SPC to be honest, and SPC turns the dense data into an early warning. Neither half is worth much without the other.

## Crown crimp: an image classifier for seal integrity

Seal integrity is the next inline check. A camera photographs each bottle neck and a trained classifier grades the crown crimp from its geometry, the skirt, the pleats, the seat on the glass, as sound or suspect. This is straightforward image classification, and it is a good fit precisely because a bad crimp looks different in ways a model can learn from labelled examples of good and failed seals. The station flags suspect bottles to a reject gate or a human, on every container rather than the sample the inspector happens to pull. What it does not do is measure seal force. The periodic secure-seal and crown-removal-torque tests on the QC bench remain the reference for pack integrity; the vision classifier is a dense inline screen that catches the obvious failures early and points the bench at anything questionable. Treat it as triage for seals, not as the seal test.

## Label QC: grading application defects, and predicting adhesion failures

Labels carry a long list of defects, and most of them are visual. A vision station grades label application on every pack for placement and skew, wrinkle and creasing, bubbling, tears, and condensate obscuring the print: the same defects a line inspector grades by eye, scored consistently and continuously. Ice-proof, tack, bond, and removal behaviour are the harder, slower properties, the ones that show up as labels lifting at the neck in the cold store or peeling in the ice bucket, and those are not fully readable from a single inline image. But there is a soft-sensor angle worth taking seriously: adhesion failures correlate with glue application and ambient conditions, so a model fed glue temperature and coverage, bottle-surface condition, and line humidity can predict when adhesion is drifting toward failure and prompt a check before a run of poorly bonded labels leaves the line. The inline camera grades what has already been applied; the adhesion model warns about conditions that will cause failures you cannot yet see. Both sit on top of the periodic peel and soak tests, which stay the reference for bond performance.

## Washed-bottle inspection: vision instead of the manual pull

Returnable and refilled lines add a bottle-washer, and the washed-bottle checks are pure looking: label carry-over from the previous fill, caustic or detergent residue, residual liquid left in the bottle, and general cleanliness before filling. The traditional method is an inspector pulling washed bottles and checking them by hand, sometimes with a methylene-blue rinse to grade wash efficiency by residual alkali. Vision moves the routine part of this inline: a camera inspects every washed bottle for carry-over labels, residue, and residual liquid and rejects the failures, instead of a person grading a sample. It is the same triage pattern as the crown station: dense inline screening on every container, with the methylene-blue and periodic laboratory wash-efficiency checks kept as the reference method that the vision screen does not replace. The win is coverage and consistency on a check that is tedious to do by hand and easy to under-sample when the line is running hard.

## Pasteurisation units: modelling PU from the tunnel

Tunnel pasteurisation is a temperature problem, not a pixel problem, but it is the same modelling idea. Pasteurisation units accumulate from the time a pack spends at each temperature through the tunnel zones, so a model reading the zone temperatures can estimate the PU delivered to each pack and flag product that is under-pasteurised (a stability and spoilage risk) or over-pasteurised, which costs flavour and energy. Done live, this turns PU from a value you verify occasionally into a value you monitor on every pack, catching a cold zone or a stalled tunnel while the affected product is still identifiable. The same cycle-driven modelling applies to the wash and pasteuriser chemistry: detergent and caustic deplete predictably with cycle count and load, so a model can predict when a bath is approaching the concentration where cleaning or wash efficiency falls off and time the top-up before quality drops rather than after. In both cases the model is scheduling and flagging around a physical process; it is not measuring the outcome.

## Where this breaks

Every station above buys coverage at a cost, and the costs are specific. **Vision needs a stable world on an unstable line.** Cameras want fixed lighting and consistent fixturing, and the packaging hall is fast, wet, and reflective: spray, condensation, glare off wet glass, and vibration all degrade a model that looked fine in a trial. The environment is the project as much as the model is. **A silent miss ships at scale.** This is the packaging version of the whole series' warning: a vision station that mis-grades a fill or a seal fails quietly and at line speed, so a drifted or fooled model does not stop the line; it passes bad product by the pallet. Inline inspection replaces a sampling gap with a monitoring burden; it does not remove the need to watch. **PU models are only as good as their probes.** A pasteurisation-unit model reading drifted or badly placed temperature sensors gives a confident, precise, wrong PU number, so the tunnel data logger and periodic PU verification stay the arbiter, not the model. **Edge cases need retraining.** A new label stock, a new bottle shape, a different crown supplier, or a fresh glue formulation is out-of-distribution for a model trained on the old ones, and grading quietly degrades until someone retrains on the new normal. None of these are reasons not to deploy vision on the line. They are the reasons it needs an owner.

## The bottom line

The packaging line is the strongest home for machine vision in the brewery lab because the work was always visual and always under-sampled. Cameras read fills, crowns, labels, and washed bottles on every container instead of a handful an hour, and the durable win is not the single pass/fail; it is feeding dense readings into SPC so you catch a filler or a labeller drifting before it makes bad product. Pasteurisation and bath chemistry are the same instinct in temperature and cycle count: model the process, flag the outliers live, top up before quality drops. What none of it does is replace the secure-seal test, the reference PU verification, the peel and soak tests, or the release decision, and because a missed defect on a fast line fails silently and at scale, every station is a monitoring commitment, not a set-and-forget install. Build it on stable lighting and fixturing, keep the reference checks as the arbiter, and retrain when the label stock or bottle changes. If you are standing this up, the [brewery data foundation]({{ '/2024/building-brewery-data-foundation-ai/' | relative_url }}) matters more than the camera. Next in the series, [sensory and the QA system]({{ '/2026/ai-brewery-lab-sensory-qa-system/' | relative_url }}): taster notes as data, predictive calibration, and deviation triage.

## Frequently asked questions

**Can computer vision reliably check fill levels on a fast packaging line?**
Yes, within limits. A camera under fixed lighting can read fill height or volume on every container at line speed, far more consistently than a manual spot check on a handful of packs an hour. The value comes from feeding those readings into a statistical process control chart so you catch a filler drifting toward under- or over-fill before it crosses spec, not from the single-pack pass or fail. The catch is that vision needs stable lighting and fixturing on a wet, reflective line, and a missed defect at line speed ships at scale, so the system needs monitoring, not blind trust.

**How does AI inspect crown seals and labels?**
As image classification. A camera photographs each bottle neck and a trained classifier grades the crown crimp as sound or suspect from the seal geometry; a second station grades the label for placement, skew, wrinkle, and condensate. It is the same looking-closely job a line inspector does, done on every container without fatigue. It flags suspect packs for a human or a reject gate; it does not replace the periodic secure-seal and torque tests that remain the reference for pack integrity.

**Can AI calculate pasteurisation units on the line?**
It can model them. Pasteurisation units accumulate from time and temperature through the tunnel, so a model reading the zone temperatures can estimate PU delivered to each pack and flag under- or over-pasteurised product in real time. That model is only as trustworthy as the temperature instrumentation feeding it: a drifted or badly placed probe gives a confident PU number that is wrong, so the tunnel data logger and periodic PU verification stay the arbiter.
