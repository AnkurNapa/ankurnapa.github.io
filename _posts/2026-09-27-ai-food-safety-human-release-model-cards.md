---
layout: post
title: "When the Model Touches Food Safety: Flag-Only Release Gates, Abstain Thresholds and Model Cards for Beer, Whisky and Wine"
image: /assets/og/ai-food-safety-human-release-model-cards.png
description: "Part 4 of Responsible AI for Beer, Whisky and Wine. Reliability and safety in practice: AI may rank risk and raise flags, but a person releases the batch and validated methods stay on the HACCP critical control points. Worked through soft sensors, mycotoxin and gushing risk in malt, methanol and the spirit cut, and SO2 and Brett in wine, with a model card, an abstain threshold, drift monitoring and a release gate where the model can block but never release."
date: 2026-09-27 09:00:00 -0700
updated: 2026-09-27
tags: [brewing-science, rai-beverage, food-safety, model-cards, mlops]
faq:
  - q: "Can an AI model release a batch of beer, whisky or wine?"
    a: "No. A model can rank risk, flag a batch for extra testing or hold it, but release is a human decision backed by validated measurements. The simplest way to enforce that is in the data model: the model's output can only move a batch towards hold, never towards release, and the release step requires a named person and a lab result."
  - q: "What is an abstain threshold?"
    a: "It is the point at which a model says it does not know. If the inputs fall outside what the model was trained on, a sensor is stale, or the prediction interval is too wide, the model returns no answer and the batch goes to the normal lab route. An abstaining model is honest. A model that always answers will sometimes be confidently wrong on exactly the batches that matter."
  - q: "Should AI decide the heads and tails cut in a distillery?"
    a: "No. A soft sensor can help a stillman see the transition coming and suggest when to check, but the cut is a safety decision because methanol and other heads compounds must stay within the legal limit in your market. The stillman makes the cut on the still, and the lab confirms the spirit before it goes to cask or bottle."
---

**Short answer: in food safety, a model is allowed to worry, not to approve. It can rank batches by risk, predict a gravity or an ABV between lab samples, flag a malt lot for mycotoxin testing, warn that the heads are running long, or say a wine is heading towards Brett. It cannot release anything. Release belongs to a named person with a validated measurement, and the critical control points in your HACCP plan stay on the methods you validated. The data model enforces this: the model's output can only push a batch towards hold. Around that sit three habits that make the model trustworthy enough to listen to: a model card that says what it was trained on and where it fails, an abstain threshold so it says "I don't know" instead of guessing, and drift monitoring so you notice when the barley, the yeast or the sensor has changed under it.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 390" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A one-way release gate. On the left, a model reads sensor, lab and supplier data and returns one of three outputs: abstain, flag, or no concern. Abstain and flag both route the batch to hold and extra testing. No concern routes the batch to the normal lab route, not to release. Release sits on the right behind a gate that needs two things: a validated lab result within specification and a named person signing off. A crossed-out arrow from the model straight to release shows that the model has no path to release. Along the bottom, three supports: a model card, an abstain threshold and drift monitoring.">
<rect width="1000" height="390" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE MODEL CAN HOLD A BATCH &#183; ONLY A PERSON CAN RELEASE IT</text>
<g font-family="sans-serif">
<rect x="30" y="56" width="220" height="200" rx="9" fill="#06483f"/>
<text x="140" y="82" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">RISK MODEL</text>
<text x="48" y="112" font-size="10.5" fill="#cfe6df">soft sensor &#183; gravity, ABV</text>
<text x="48" y="136" font-size="10.5" fill="#cfe6df">malt lot &#183; mycotoxin risk</text>
<text x="48" y="160" font-size="10.5" fill="#cfe6df">spirit run &#183; heads trend</text>
<text x="48" y="184" font-size="10.5" fill="#cfe6df">wine &#183; SO2 and Brett risk</text>
<text x="48" y="222" font-size="10.5" font-weight="700" fill="#ffffff">outputs: abstain,</text>
<text x="48" y="240" font-size="10.5" font-weight="700" fill="#ffffff">flag or no concern</text>
<rect x="300" y="56" width="230" height="90" rx="9" fill="#f0f6f5" stroke="#ff4081" stroke-width="2"/>
<text x="415" y="84" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">HOLD + EXTRA TESTS</text>
<text x="318" y="110" font-size="10.5" fill="#06483f">abstain or flag lands here</text>
<text x="318" y="130" font-size="10.5" fill="#06483f">batch cannot move on</text>
<rect x="300" y="166" width="230" height="90" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="415" y="194" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">NORMAL LAB ROUTE</text>
<text x="318" y="220" font-size="10.5" fill="#06483f">no concern lands here</text>
<text x="318" y="240" font-size="10.5" fill="#06483f">still tested, not skipped</text>
<line x1="250" y1="120" x2="300" y2="101" stroke="#ff4081" stroke-width="2.5"/>
<line x1="250" y1="190" x2="300" y2="211" stroke="#2e9e7c" stroke-width="2.5"/>
<rect x="690" y="56" width="280" height="200" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="2"/>
<text x="830" y="84" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">RELEASE GATE</text>
<text x="710" y="116" font-size="10.5" fill="#06483f">1. validated lab result</text>
<text x="728" y="134" font-size="10.5" fill="#06483f">within specification</text>
<text x="710" y="164" font-size="10.5" fill="#06483f">2. named person signs off</text>
<text x="710" y="194" font-size="10.5" fill="#06483f">3. no open hold on the batch</text>
<text x="710" y="232" font-size="10.5" font-weight="700" fill="#2e9e7c">released &#183; audit logged</text>
<line x1="530" y1="211" x2="690" y2="170" stroke="#2e9e7c" stroke-width="2.5"/>
<text x="560" y="182" font-size="10" fill="#2e9e7c">lab + person</text>
<path d="M140 256 C140 300 600 300 690 240" fill="none" stroke="#ff4081" stroke-width="2.5" stroke-dasharray="5 4"/>
<line x1="430" y1="282" x2="450" y2="302" stroke="#ff4081" stroke-width="3"/>
<line x1="450" y1="282" x2="430" y2="302" stroke="#ff4081" stroke-width="3"/>
<text x="470" y="300" font-size="10" font-weight="700" fill="#ff4081">no path from model to release</text>
<rect x="30" y="320" width="300" height="56" rx="9" fill="#f0f6f5"/>
<text x="180" y="344" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">MODEL CARD</text>
<text x="180" y="362" text-anchor="middle" font-size="10" fill="#4a6b64">trained on what, fails where</text>
<rect x="350" y="320" width="300" height="56" rx="9" fill="#f0f6f5"/>
<text x="500" y="344" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">ABSTAIN THRESHOLD</text>
<text x="500" y="362" text-anchor="middle" font-size="10" fill="#4a6b64">out of range means no answer</text>
<rect x="670" y="320" width="300" height="56" rx="9" fill="#f0f6f5"/>
<text x="820" y="344" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">DRIFT MONITORING</text>
<text x="820" y="362" text-anchor="middle" font-size="10" fill="#4a6b64">new barley, new yeast, new sensor</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A one-way gate. Every model output moves a batch towards more scrutiny or leaves it on the normal route. None of them move it towards release.</figcaption>
</figure>

Every brewer has a story about the reading that looked fine. The inline density meter said the beer was at terminal gravity, the tank was due to crash, and a sample on the bench said otherwise because the meter had a film of yeast on it. Nobody got hurt. The beer spent two more days in the tank. That is the good version of the story, and it is the good version because a person pulled a sample.

Now put a model in that loop. It is faster than the meter, cheaper than the lab and right most of the time. The temptation is obvious: if it is right 98 percent of the time, why keep testing? This post is about why, and about the small amount of engineering that lets you use the model without ever having to answer that question under pressure.

[Part 1]({{ '/2026/responsible-ai-beverage-principles-use-case-register/' | relative_url }}) put food safety models at the top of the use-case register. This is the reliability and safety principle made concrete.

## The rule: models flag, people release

In a brewery, distillery or winery, "release" means a batch leaves your control: to package, to cask, to trade, to someone's glass. Your HACCP plan names the critical control points on the way, pasteurisation units, the spirit cut, sulphite additions, allergen and foreign-body controls, and ties each one to a validated method and a limit.

A model can sit beside those points. It should not replace them. The distinction I use is simple:

- **A model may worry.** It can rank batches by risk, raise a flag, ask for an extra test, or put a hold on.
- **A model may not approve.** It can never be the reason a batch moves forward.

This is not distrust of machine learning. It is how safety systems are built anyway. A pressure relief valve can open a vessel. It cannot decide the vessel is fine and skip the inspection.

## Four places the model earns its keep

**Soft sensors for gravity and ABV.** A model that predicts gravity from temperature, CO2 evolution and time, between lab samples, is genuinely useful. It spots a stuck ferment a day early and tells you which tank to sample first. I have written about [soft sensors with proactive bands on a spirit safe]({{ '/2026/soft-sensors-proactive-bands-spirit-safe/' | relative_url }}), and the same idea works in the fermenter. What it cannot do is sign off the ABV on a label. Declared strength needs a validated measurement.

**Mycotoxin and gushing risk in malt.** A model can take harvest weather, region, supplier history and the malt certificate and rank incoming lots by [risk of Fusarium, mycotoxins and gushing]({{ '/2026/forecasting-mycotoxin-gushing-risk-malting/' | relative_url }}). That is exactly how you should spend a testing budget: test the top of the list first, more often. A low-risk score is a reason to test less often, never a reason to stop testing, and never a substitute for the supplier's certificate.

**Methanol and the spirit cut.** In pot still distillation the stillman cuts from heads to hearts to tails. Heads carry the most volatile compounds, and methanol has to stay within the legal limit in your market. A soft sensor can show the transition coming from vapour temperature and flow, and suggest when to nose and check. The cut itself stays with the stillman on the still, and the lab confirms the new-make spirit before it goes to cask. A model that "decides the cut" and is wrong once is not a data science problem. It is a recall.

**SO2 and Brett in wine.** A model that watches free SO2 trend, pH, temperature and barrel history can warn that a lot is drifting towards the conditions where Brettanomyces takes hold, before 4-EP shows up on the nose. That is a good reason to measure, adjust and [test for faults]({{ '/2024/detecting-wine-faults-brett-va-tca/' | relative_url }}). Sulphite additions and the labelling that goes with them stay on measured values.

In every case the model makes the humans faster and better aimed. In no case does it remove a measurement from the path to release.

## Enforce it in the data model, not the meeting

A rule that lives in a slide gets broken on the busiest Friday of the year. A rule that lives in the database does not. The lazy, reliable pattern: the model writes into a risk table, holds are created from it automatically, and the release function checks for a lab result and a human signature. There is no column the model can write that makes release easier.

```sql
-- The model can only insert into model_risk. It has no grant on batch_release.
CREATE TABLE model_risk (
    batch_id      TEXT NOT NULL,
    model_id      TEXT NOT NULL,
    model_version TEXT NOT NULL,
    output        TEXT NOT NULL CHECK (output IN ('abstain','flag','no_concern')),
    score         NUMERIC,
    reason        TEXT,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Abstain and flag both create a hold. No model output removes one.
-- A hold stays open until a person clears it after it was raised.
CREATE VIEW open_holds AS
SELECT h.batch_id, h.source, h.reason, h.created_at
FROM (
    SELECT batch_id, model_id AS source, reason, created_at
    FROM model_risk WHERE output IN ('abstain','flag')
    UNION ALL
    SELECT batch_id, 'manual', reason, created_at FROM manual_holds
) h
WHERE NOT EXISTS (
    SELECT 1 FROM cleared_holds c
    WHERE c.batch_id = h.batch_id AND c.cleared_at > h.created_at
);

-- Release: a validated lab result in spec, a named person, and no open hold.
-- Note what is missing: nothing here reads model_risk.output = 'no_concern'.
INSERT INTO batch_release (batch_id, released_by, lab_result_id, released_at)
SELECT :batch_id, :user_id, l.lab_result_id, now()
FROM lab_results l
WHERE l.batch_id = :batch_id
  AND l.method_validated = TRUE
  AND l.within_spec = TRUE
  AND NOT EXISTS (SELECT 1 FROM open_holds h WHERE h.batch_id = :batch_id)
  AND :user_id IN (SELECT user_id FROM release_authorised_users);
```

Clearing a hold is also a human act, written to `cleared_holds` with a name and a reason. The model can flag the same batch again tomorrow. It cannot un-flag it.

## The model card: what it knows and where it fails

A model card is a short document that travels with the model. It is the answer to "why should I believe this?" that a quality manager can read in two minutes. Keep it in the repository next to the code and version it with every retrain.

The numbers below are illustrative, not from a real brewery.

```yaml
model_id: ferm-gravity-soft-sensor
version: 2.3.0
owner: quality-data            # a team, with a named lead
purpose: >
  Predict present gravity (degrees Plato) between lab samples for ale and lager
  fermentations in 20 to 60 hl cylindroconical tanks, to prioritise sampling.
not_for:
  - declaring ABV on labels or duty returns
  - deciding when to crash, transfer or release without a lab sample
  - fermentations with fruit, lactose or other adjuncts over 10 percent of the grist
training_data:
  period: 2023-01 to 2026-06
  fermentations: 1840
  yeast_strains: [house_ale_1, house_lager_2]
  excluded: runs with missing temperature logs (212)
performance:
  mae_plato: 0.21              # on held-out 2026 fermentations
  p95_abs_error_plato: 0.55
  worse_on: first 18 hours after pitching; high-gravity worts above 16 Plato
abstain_when:
  - any input outside the training range
  - temperature tag older than 15 minutes
  - prediction interval wider than 0.8 Plato
  - yeast strain not in training_data.yeast_strains
drift_checks:
  - weekly: residuals against lab samples, alert if rolling MAE over 0.35
  - per malt lot: compare wort composition to training distribution
  - on any sensor replacement or recalibration: shadow mode for 10 fermentations
review: every 6 months, or on any change of yeast, recipe family or sensor
```

The `not_for` list is the most important part and the one most often left blank. Write down the uses you are ruling out, so nobody discovers them later in a meeting where the model is already doing them.

## Abstain thresholds: teaching the model to say "I don't know"

Most models always return a number. That is the dangerous default. A model trained on two yeast strains will happily predict gravity for a third. A model trained on summer barley will score a wet-harvest lot as confidently as a dry one. The number looks the same either way.

An abstain threshold turns "out of its depth" into an explicit output. Check the inputs against the training ranges, check sensor freshness, check the width of the prediction interval, and if any fails, return `abstain`. In the release gate above, abstain means hold, so the batch goes to the lab. Nothing is lost except a little time.

The metric to watch is the abstain rate. A few percent is healthy. Near zero means the thresholds are too loose. A sudden jump usually means something changed upstream: a new malt supplier, a recalibrated probe, a recipe the model has never seen.

## Drift monitoring: the barley changed and nobody told the model

Beverage processes drift for honest reasons. Barley changes with every harvest. Yeast is a living population that shifts over generations. Sensors foul and get replaced. Grapes from one vintage are not grapes from the next. A model that was accurate last year can be quietly wrong this year while every dashboard stays green.

Three checks cover most of it:

1. **Residuals against lab truth.** You still take lab samples, so compare them to what the model predicted. A rising error is the plainest drift alarm there is.
2. **Input distributions.** Compare this month's inputs with the training data. A shift in wort composition or harvest weather tells you the model is about to extrapolate.
3. **Change events.** New sensor, new yeast generation policy, new supplier: run the model in shadow mode, predicting but not flagging, until the residuals settle.

## Where this breaks

**Alert fatigue.** A model that flags a third of batches will be ignored by the end of the month, and ignored flags are worse than no flags. Tune for precision on the flags that matter, and report the flag rate alongside the catch rate.

**"No concern" becomes "skip the test".** It starts with a busy week and one skipped sample on a low-risk batch. The gate above never reads `no_concern`, but a lab schedule can. Keep the sampling plan independent of the model, or change it only through the same change control as your HACCP plan.

**The model card goes stale.** The card says two yeast strains; the brewery now uses four. Tie the card to the retrain pipeline so a new version cannot deploy without a new card.

**Validation is a real process.** If you ever want a model to become part of a validated method, that is a formal validation exercise under your food safety system, with its own evidence. It is not a data science sprint with a good R-squared.

**Human sign-off can become a rubber stamp.** Show the person releasing the batch the lab result, not the model score. If they only see the green tick from the model, you have automated release with an extra click.

## The bottom line

In food safety the model's job is to worry well. It can rank, predict between samples, flag and hold, and done properly it makes the lab faster and better aimed. It never releases. Build that into the data model so the rule survives the busiest week: model outputs can only push a batch towards hold, release needs a validated result and a named person, and clearing a hold is a human act. Around it, keep a model card that says what the model is not for, an abstain threshold so it admits when it is out of its depth, and drift checks for the barley, yeast and sensors that change under it. The model sees the density curve. The brewer sees the yeast film on the meter. The batch goes out on what the brewer sees.

Next: [whose palate did the model learn?]({{ '/2026/sensory-ai-bias-tasting-note-hallucination-evals/' | relative_url }}) For the wider picture of what AI can and cannot do in a brewery, see [The Honest Limits of AI in Brewing]({{ '/2026/the-honest-limits-of-ai-in-brewing/' | relative_url }}). The full list is on the [series page]({{ '/series/responsible-ai-beverage/' | relative_url }}).

## Frequently asked questions

**Can an AI model release a batch of beer, whisky or wine?**
No. A model can rank risk, flag a batch for extra testing or hold it, but release is a human decision backed by validated measurements. The simplest way to enforce that is in the data model: the model's output can only move a batch towards hold, never towards release, and the release step requires a named person and a lab result.

**What is an abstain threshold?**
It is the point at which a model says it does not know. If the inputs fall outside what the model was trained on, a sensor is stale, or the prediction interval is too wide, the model returns no answer and the batch goes to the normal lab route. An abstaining model is honest. A model that always answers will sometimes be confidently wrong on exactly the batches that matter.

**Should AI decide the heads and tails cut in a distillery?**
No. A soft sensor can help a stillman see the transition coming and suggest when to check, but the cut is a safety decision because methanol and other heads compounds must stay within the legal limit in your market. The stillman makes the cut on the still, and the lab confirms the spirit before it goes to cask or bottle.
