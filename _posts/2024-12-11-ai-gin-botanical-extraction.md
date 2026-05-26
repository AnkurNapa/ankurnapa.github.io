---
layout: post
title: "AI for Gin Botanical Extraction and Recipe Consistency"
image: /assets/og/ai-gin-botanical-extraction.png
description: "How AI models maceration, vapour infusion and the cut, and compensates for botanical lot variability to keep a gin recipe consistent batch after batch."
date: 2024-12-11
updated: 2024-12-11
tags: [distilling-maturation, spirits, flavor]
faq:
  - q: "Why does the same gin recipe taste different batch to batch?"
    a: "Botanicals are natural products; juniper, citrus peel and coriander vary in potency by harvest and lot, so a fixed recipe extracts a moving target. Compensating for that variability is the consistency challenge."
  - q: "Can AI adjust a botanical bill automatically?"
    a: "It can propose adjustments when a lot's potency shifts, but a distiller should approve them and the sensory result confirms whether the batch is on profile."
  - q: "Does AI help with the spirit cut in gin?"
    a: "Yes. The cut still decides what flavour carries through, so modelling cut points alongside extraction helps keep the botanical character consistent."
---

**Short answer: AI can model botanical extraction and adjust the recipe to offset lot-to-lot variability, keeping your gin consistent — with the still operator and the sensory panel making the final call.** Nature varies; the recipe should flex to meet it.

## Consistency is the real challenge in gin
Most gin is not aged, so there is no maturation to smooth things out — the flavour comes almost entirely from botanicals extracted in the still. Juniper is essential, joined by coriander, citrus peel, angelica, orris, and others, drawn out by maceration in the spirit or by vapour infusion as alcohol vapour passes through a botanical basket. The trouble is that botanicals are agricultural. A new lot of juniper or lemon peel can be stronger or weaker, oilier or drier, than the last. Run a fixed recipe against a shifting input and the gin drifts, even when you have changed nothing. Holding the profile steady despite that is the distiller's standing problem.

## Measure first: characterise the botanicals and the run
The starting point is data, not modelling. Characterise each incoming botanical lot — moisture, essential-oil content where you can measure it, supplier, harvest, and a quick sensory check. Then capture the process: maceration time and temperature, charge weights, vapour-infusion conditions, and the cut points that decide what carries through to the heart. Tie those inputs to the outcome — analytical markers of the key aromatics and, crucially, sensory panel scores against your house profile. With that record you can see which input swings actually move the flavour and by how much, rather than blaming a batch on a vague off day.

## The model: compensating for lot variability
Once extraction is characterised, a model predicts how a given set of botanicals and process settings will land against the target profile. The practical payoff is compensation: when a juniper lot arrives 15% more potent, the model proposes a trimmed charge or an adjusted maceration to bring the batch back on profile before you distil, not after. A generative recipe assistant makes this usable on the floor — feed it the new lot's potency and your target, and it drafts an adjusted botanical bill with the reasoning ("reduce juniper by X, lift citrus peel slightly to rebalance brightness, hold the cut") for the distiller to approve. It turns a guess-and-redistil cycle into a considered first attempt.

## Where it breaks
The limits are inherent to the craft. Botanical variation is natural and not fully captured by a few lab numbers — two lots with the same oil content can still behave differently. Sensory remains the arbiter; the panel, not the model, decides whether a batch is on profile, and a distiller's nose often catches what the instruments miss. And many gin producers are small-batch, so the data is thin and a model can overfit to a handful of runs. Treat the assistant as a faster way to a good first cut, validated by tasting, not as a hands-off autopilot.

## The bottom line
Gin consistency is a fight against natural botanical variability, and AI is well placed to help you compensate by adjusting the recipe before you distil. Characterise the botanicals and the run, model the extraction, and let a generative assistant draft the adjusted bill. The cut and the sensory panel still decide — but you waste fewer batches getting there.

*Part of the [Distilling & Maturation]({{ '/tracks/distilling-maturation/' | relative_url }}) track.* Related: [Predicting distillation cut points with AI]({{ '/2024/predicting-distillation-cut-points-ai/' | relative_url }}).

## Frequently asked questions

**Why does the same gin recipe taste different batch to batch?**
Botanicals are natural products; juniper, citrus peel and coriander vary in potency by harvest and lot, so a fixed recipe extracts a moving target. Compensating for that variability is the consistency challenge.

**Can AI adjust a botanical bill automatically?**
It can propose adjustments when a lot's potency shifts, but a distiller should approve them and the sensory result confirms whether the batch is on profile.

**Does AI help with the spirit cut in gin?**
Yes. The cut still decides what flavour carries through, so modelling cut points alongside extraction helps keep the botanical character consistent.
