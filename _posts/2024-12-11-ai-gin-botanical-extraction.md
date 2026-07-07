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

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Where this sits in the whiskey production flow, start to finish."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUCTION FLOW</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">AI for Gin Botanical Extraction and Recipe Consistency</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mash</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ferment</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Distil</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mature</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Bottle</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Where this sits in the whiskey production flow, start to finish.</figcaption>
</figure>

## Consistency is the real challenge in gin
Most gin is not aged, so there is no maturation to smooth things out — the flavour comes almost entirely from botanicals extracted in the still. Juniper is essential, joined by coriander, citrus peel, angelica, orris, and others, drawn out by maceration in the spirit or by vapour infusion as alcohol vapour passes through a botanical basket. The trouble is that botanicals are agricultural. A new lot of juniper or lemon peel can be stronger or weaker, oilier or drier, than the last. Run a fixed recipe against a shifting input and the gin drifts, even when you have changed nothing. Holding the profile steady despite that is the distiller's standing problem.

## Measure first: characterise the botanicals and the run
The starting point is data, not modelling. Characterise each incoming botanical lot — moisture, essential-oil content where you can measure it, supplier, harvest, and a quick sensory check. Then capture the process: maceration time and temperature, charge weights, vapour-infusion conditions, and the cut points that decide what carries through to the heart. Tie those inputs to the outcome — analytical markers of the key aromatics and, crucially, sensory panel scores against your house profile. With that record you can see which input swings actually move the flavour and by how much, rather than blaming a batch on a vague off day.

## The model: compensating for lot variability
Once extraction is characterised, a model predicts how a given set of botanicals and process settings will land against the target profile. The practical payoff is compensation: when a juniper lot arrives 15% more potent, the model proposes a trimmed charge or an adjusted maceration to bring the batch back on profile before you distil, not after. A generative recipe assistant makes this usable on the floor — feed it the new lot's potency and your target, and it drafts an adjusted botanical bill with the reasoning ("reduce juniper by X, lift citrus peel slightly to rebalance brightness, hold the cut") for the distiller to approve. It turns a guess-and-redistil cycle into a considered first attempt.

## Where it breaks
The limits are inherent to the craft. Botanical variation is natural and not fully captured by a few lab numbers — two lots with the same oil content can still behave differently. Sensory remains the arbiter; the panel, not the model, decides whether a batch is on profile, and a distiller's nose often catches what the instruments miss. And many gin producers are small-batch, so the data is thin and a model can overfit to a handful of runs. Treat the assistant as a faster way to a good first cut, validated by tasting, not as a hands-off autopilot.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="A closed control loop: measure, compute, actuate — then feed the result back."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">CONTROL LOOP</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">AI for Gin Botanical Extraction and Recipe Consistency</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Controller</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Actuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Process</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">feedback</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">A closed control loop: measure, compute, actuate — then feed the result back.</figcaption>
</figure>

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
