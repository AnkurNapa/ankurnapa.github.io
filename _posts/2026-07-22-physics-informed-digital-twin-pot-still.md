---
layout: post
title: "A Physics-Informed Digital Twin of a Pot Still: Why Pure ML Twins Drift"
image: /assets/og/physics-informed-digital-twin-pot-still.png
description: "Part 1 of The Still and the Model. A batch pot still follows the Rayleigh equation, and alcohol in must equal alcohol out. Why a purely data-driven twin quietly breaks that law, and how a hybrid model, with physics for the structure and run data for a few fitted parameters, stays honest."
date: 2026-07-22 09:00:00 -0700
updated: 2026-07-22
tags: [distilling-maturation, still-and-model, digital-twin, machine-learning, data-engineering]
faq:
  - q: "What is a physics-informed digital twin of a still?"
    a: "It is a model whose structure comes from the physics of distillation, such as the Rayleigh equation and vapour-liquid equilibrium, with a small number of parameters fitted from the distillery's own run data. The physics guarantees things like alcohol conservation. The data tunes the model to this particular still, its heat input and its condenser."
  - q: "Why does a purely data-driven still twin drift?"
    a: "A machine learning model trained only on past runs learns correlations, not laws. It can predict heads, hearts and feints volumes that add up to more alcohol than was charged, and it has no idea what to do when the charge strength or heat input moves outside the range it was trained on. Nothing in its structure stops it breaking conservation."
  - q: "What data do you need to fit a hybrid pot still model?"
    a: "For each run: charge volume and strength, heat input or steam flow over time, distillate flow and strength at the spirit safe, and the cut times. A few dozen well-recorded runs are usually enough to fit the handful of parameters a hybrid model needs, because the physics does most of the work."
---

**Short answer: a batch pot still obeys two rules a data scientist cannot negotiate with. The Rayleigh equation describes how the pot and the vapour change as the run goes on, and the alcohol you charge must equal the alcohol you collect across heads, hearts, feints and residue. A digital twin built only from machine learning on past runs knows neither rule, so it drifts the moment conditions change and can predict fractions that contain more alcohol than went in. Build the twin the other way round: physics for the structure, run data for a few fitted parameters. It needs less data, it extrapolates sensibly, and it cannot invent spirit.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="An illustrative spirit still run. A charge of 10,000 litres of low wines at 22 percent holds 2,200 litres of absolute alcohol. The hybrid twin splits it into heads 60, hearts 1,050, feints 1,070 and residue 20, which sums to 2,200. A pure machine learning twin predicts heads 60, hearts 1,120, feints 1,110 and residue 20, which sums to 2,310, more alcohol than was charged.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">ALCOHOL IN MUST EQUAL ALCOHOL OUT (ILLUSTRATIVE RUN, LITRES OF ABSOLUTE ALCOHOL)</text>
<g font-family="sans-serif">
<rect x="40" y="110" width="200" height="90" rx="10" fill="#06483f"/>
<text x="140" y="140" text-anchor="middle" font-size="12" fill="#cfe6df">charge</text>
<text x="140" y="166" text-anchor="middle" font-size="20" font-weight="700" fill="#ffffff">2,200 LAA</text>
<text x="140" y="187" text-anchor="middle" font-size="10.5" fill="#cfe6df">10,000 L at 22%</text>
<line x1="240" y1="155" x2="300" y2="100" stroke="#4db6a2" stroke-width="2"/>
<line x1="240" y1="155" x2="300" y2="220" stroke="#4db6a2" stroke-width="2"/>
<text x="310" y="62" font-size="11" font-weight="700" letter-spacing="1" fill="#2e9e7c">HYBRID TWIN</text>
<rect x="300" y="72" width="660" height="56" rx="9" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="2"/>
<text x="330" y="106" font-size="12" fill="#06483f">heads 60 &#183; hearts 1,050 &#183; feints 1,070 &#183; residue 20</text>
<text x="940" y="106" text-anchor="end" font-size="15" font-weight="700" fill="#2e9e7c">= 2,200 &#10003;</text>
<text x="310" y="172" font-size="11" font-weight="700" letter-spacing="1" fill="#ff4081">PURE ML TWIN</text>
<rect x="300" y="182" width="660" height="56" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="330" y="216" font-size="12" fill="#06483f">heads 60 &#183; hearts 1,120 &#183; feints 1,110 &#183; residue 20</text>
<text x="940" y="216" text-anchor="end" font-size="15" font-weight="700" fill="#ff4081">= 2,310 &#10007;</text>
<rect x="40" y="272" width="920" height="42" rx="10" fill="#06483f"/>
<text x="500" y="298" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">A TWIN THAT CAN INVENT 110 LITRES OF ALCOHOL IS NOT A TWIN</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative figures. Each fraction on its own looks plausible. Only the sum gives the pure ML twin away.</figcaption>
</figure>

Every distillery that starts a digital twin project gets the same pitch: feed a model a few years of run data, and it will predict the run. Heads volume, hearts volume, cut times, all learned. The demo on last year's runs looks excellent. Then the charge comes in a point and a half stronger than usual, or the steam supply changes after a boiler repair, and the twin starts saying things the stillman knows are nonsense.

This is the first post in **The Still and the Model**, a series on the data engineering and GenAI under a distillery's numbers. It starts with the twin, because the twin is where the gap between a model that fits data and a model that respects physics shows up first.

## What a pot still actually does

A batch pot still is a textbook case, and the textbook has had the answer for more than a century. As the charge boils, the vapour is richer in alcohol than the liquid it leaves, so the pot gets steadily weaker and the distillate strength falls through the run. Lord Rayleigh wrote down the relationship in 1902: over each small slice of the run, the alcohol leaving in the vapour equals the alcohol lost from the pot.

In code, one step of that is almost embarrassingly short:

```python
def rayleigh_step(W, x, dW, vle, eff):
    # W: moles in pot, x: alcohol mole fraction in pot, dW: moles boiled off
    y = x + eff * (vle(x) - x)        # vapour composition, eff fitted from runs
    x_new = (W * x - y * dW) / (W - dW)
    return W - dW, x_new, y
```

`vle(x)` is the vapour-liquid equilibrium for ethanol and water, which comes from published data, not from your runs. `eff` is how close your particular still, with its reflux from the neck, lyne arm angle and condenser, gets to that equilibrium. And notice the conservation built in: alcohol in the pot before the step equals alcohol in the pot after plus alcohol in the vapour. The model cannot break it, because the maths does not allow it.

A real still adds reflux, heat input changes and a copper surface that matters for flavour, so a production twin carries a few more terms. The shape stays the same: known physics, and a handful of parameters that describe your still.

## Why a pure ML twin drifts

A machine learning model trained on past runs does something quite different. It learns that, on the runs it has seen, a charge like this tended to produce a hearts cut like that. That is a correlation, and correlations have two weaknesses on a still.

**They do not conserve anything.** Predict heads, hearts and feints with three separate models, or one model with three outputs, and nothing forces them to add up. In the illustrative run above, each predicted fraction is within its historical range. Together they contain 110 litres of absolute alcohol that was never in the charge. On a dashboard, nobody adds them up. In an excise reconciliation, somebody will.

**They do not extrapolate.** The runs in the training set cover the charge strengths, heat inputs and fill levels the distillery happened to use. Change one of them and the model is guessing. The physics model is not: the Rayleigh equation does not care whether the charge is 21% or 24%, it just runs.

The deeper problem is that a pure data twin gets less trustworthy exactly when it is most needed, on the unusual run.

## The hybrid: physics for structure, data for parameters

The approach that works is a hybrid, sometimes called grey-box modelling. The physics sets the structure: mass and alcohol balances, Rayleigh, vapour-liquid equilibrium, a simple heat balance. Run data fits the few numbers the physics cannot know:

- **the enrichment efficiency** of this still (`eff` above),
- **the effective heat input** for a given steam valve position or burner setting,
- **the condenser and safe lag**, the delay between vapour leaving the pot and spirit reaching the hydrometer.

Three or four parameters, fitted to a few dozen well-recorded runs, will usually track a real still closely. A pure ML twin needs far more runs to reach the same accuracy inside the training range, and it is still lost outside it.

There is a place for machine learning in the hybrid: modelling the residual, the gap between what the physics predicts and what the still did. If the residual has a pattern (it drifts with ambient temperature, or after each CIP), a small model can learn it. The difference is that the ML is correcting a sound model, not replacing it.

## The data engineering underneath

A twin is only as good as its run records, and this is where most distilleries find out what they have been logging:

1. **Charge volume and strength, measured.** Not the planned charge. The strength at 20 degrees C, from a hydrometer or density meter, recorded with the instrument.
2. **Heat input as a time series.** Steam flow or valve position every few seconds, from the historian, not a setting written on the run sheet.
3. **Distillate flow and strength at the spirit safe.** Enough readings to draw the strength curve, including the cut times with who made them.
4. **Every fraction, measured.** Heads, hearts and feints volumes and strengths at the end of the run, so the alcohol balance can be checked for every run.

That last item gives you a data quality test for free. For every run, charge alcohol minus the sum of the fractions should sit close to zero. A run that misses by 5% is not a modelling problem. It is a meter, a hydrometer or a recording problem, and it should be fixed before that run is used to fit anything. The [cellar ledger in the wine series]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }}) makes the same argument for volumes: record the movements, and let the balances check themselves.

## What the twin is for

With a trustworthy twin, the useful things are fairly modest:

- **Forecast the run** from the charge: expected cut times and fraction volumes, so the stillman and the planner see the same numbers.
- **Test a change on the model first.** A different charge strength or heat profile can be run on the twin before it is run on the still.
- **Spot a run that is not behaving like the physics says it should.** That is the subject of [the next post]({{ '/2026/soft-sensors-proactive-bands-spirit-safe/' | relative_url }}).

What it does not do is choose the cut. The cut is a sensory and commercial decision that the [cut points post]({{ '/2024/predicting-distillation-cut-points-ai/' | relative_url }}) covers in detail. The twin tells you where the run is heading. The stillman still decides where it stops.

## Where this breaks

**Congeners are not ethanol.** Rayleigh with ethanol-water equilibrium tracks alcohol well. Esters, higher alcohols and the sulphur compounds copper removes behave differently, and those are the compounds that decide flavour. A twin that tracks strength is not a twin of flavour.

**Equilibrium data has limits.** Published vapour-liquid data is for clean ethanol and water. Low wines carry other volatiles, and at the very start and end of a run the simple model is least accurate. Fit and judge the twin on the middle of the run.

**Fitted parameters drift.** Copper thins, heating surfaces foul, a condenser gets replaced. Refit the parameters on a schedule and watch them over time. A parameter that moves steadily is telling you about the still, not about the model.

**Bad records make a confident bad twin.** If charge strengths are planned rather than measured, the twin fits to fiction and reports it with two decimal places.

## The bottom line

A still is one of the few places in a drinks business where the physics is fully known and the data is patchy. That is exactly backwards from what pure machine learning wants. Use the physics for the structure, so alcohol is conserved and the model behaves on runs it has not seen. Use the data for the few parameters that make it your still. The model sees the run log. The stillman sees the copper and the steam and the odd charge. A hybrid twin is the version that respects both.

For the sensors that feed a twin, see [IoT in the Distillery]({{ '/2026/iot-in-the-distillery-sensors-process/' | relative_url }}). The full list is on [The Still and the Model series page]({{ '/series/still-and-model/' | relative_url }}).

## Frequently asked questions

**What is a physics-informed digital twin of a still?**
It is a model whose structure comes from the physics of distillation, such as the Rayleigh equation and vapour-liquid equilibrium, with a small number of parameters fitted from the distillery's own run data. The physics guarantees things like alcohol conservation. The data tunes the model to this particular still, its heat input and its condenser.

**Why does a purely data-driven still twin drift?**
A machine learning model trained only on past runs learns correlations, not laws. It can predict heads, hearts and feints volumes that add up to more alcohol than was charged, and it has no idea what to do when the charge strength or heat input moves outside the range it was trained on. Nothing in its structure stops it breaking conservation.

**What data do you need to fit a hybrid pot still model?**
For each run: charge volume and strength, heat input or steam flow over time, distillate flow and strength at the spirit safe, and the cut times. A few dozen well-recorded runs are usually enough to fit the handful of parameters a hybrid model needs, because the physics does most of the work.
