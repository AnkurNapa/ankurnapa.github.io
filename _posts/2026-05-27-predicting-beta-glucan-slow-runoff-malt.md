---
layout: post
title: "Predicting Slow Runoff From the Malt Before It Reaches Your Mill"
image: /assets/og/predicting-beta-glucan-slow-runoff-malt.png
description: "Under-modified malt hides the high beta-glucan that slows lautering and filtration. How a model reads the malt certificate to flag runoff risk — and why a lot average can still fool you."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
tags: [brewing-science, malting, lautering, machine-learning]
faq:
  - q: "What causes slow runoff in the brewhouse?"
    a: "The usual culprit is high beta-glucan from under-modified malt. Beta-glucan is a gummy cell-wall polysaccharide; when malt is under-modified it survives into the mash, raises wort viscosity and binds the lauter bed or filter, giving slow or stuck runoff and lost extract."
  - q: "Can you predict beta-glucan and viscosity from the malt certificate?"
    a: "Partly. The certificate's modification, friability, homogeneity and measured beta-glucan and viscosity correlate with runoff behaviour, so a model trained on your past brews can rank a lot's runoff risk. But the certificate is a lot average and cannot see an under-modified fraction that drives most stuck mashes."
  - q: "How do you fix a high-beta-glucan malt?"
    a: "Give the mash a beta-glucanase rest around 45°C to let enzymes break down the gum, mill a little coarser, and avoid over-running the lauter. Catching the risk before brew day lets you build the rest into the mash schedule rather than firefighting a stuck runoff."
---

**Short answer: yes, partly — and the value is in the timing. The malt certificate of analysis carries the signals that predict slow runoff (modification, friability, homogeneity, beta-glucan and wort viscosity), so a model trained on your own brews can rank an incoming lot's runoff risk before it ever reaches the mill. That lets you build a beta-glucanase rest into the mash schedule instead of firefighting a stuck lauter at 6 a.m. What it cannot do is see the under-modified pocket hiding inside a healthy-looking lot average — which is what causes most stuck mashes.**

A stuck or crawling runoff is one of the most expensive things that happens in a brewhouse: it stalls the brew day, hurts extract and often traces straight back to the malt. The frustrating part is that the warning is sitting in the certificate the day the malt arrives — if you read it the right way.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 250" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Scatter of malt beta-glucan against lauter time showing a rising trend and a high-risk zone">
<rect x="0" y="0" width="760" height="250" fill="#fdfbf7"/>
<text x="380" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Malt beta-glucan vs. lauter time</text>
<line x1="80" y1="210" x2="710" y2="210" stroke="#6b6258" stroke-width="1.5"/>
<line x1="80" y1="50" x2="80" y2="210" stroke="#6b6258" stroke-width="1.5"/>
<text x="395" y="240" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#6b6258">beta-glucan (mg/L) →</text>
<text x="46" y="130" font-family="sans-serif" font-size="11" fill="#6b6258" transform="rotate(-90 46,130)">lauter time →</text>
<rect x="470" y="50" width="240" height="160" fill="#7a1f3d" fill-opacity="0.08"/>
<text x="590" y="68" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="#7a1f3d">high-risk zone</text>
<line x1="80" y1="195" x2="710" y2="80" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4"/>
<g fill="#1c1a17">
<circle cx="130" cy="190" r="5"/><circle cx="175" cy="185" r="5"/><circle cx="215" cy="178" r="5"/><circle cx="265" cy="170" r="5"/><circle cx="305" cy="160" r="5"/><circle cx="355" cy="150" r="5"/><circle cx="415" cy="140" r="5"/>
</g>
<g fill="#7a1f3d">
<circle cx="520" cy="120" r="5"/><circle cx="560" cy="100" r="5"/><circle cx="620" cy="95" r="5"/><circle cx="660" cy="75" r="5"/>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Runoff time climbs with beta-glucan, but the spread is wide — viscosity and homogeneity sharpen the prediction. The model ranks risk; it does not promise a stuck mash.</figcaption>
</figure>

## Why beta-glucan slows the lauter

Beta-glucan is the gummy polysaccharide that makes up much of the barley endosperm cell wall. Good [modification during germination]({{ '/2026/predicting-malt-modification-germination/' | relative_url }}) breaks it down with beta-glucanase; when modification is short, the beta-glucan survives into the mash, where it dissolves, raises wort viscosity and forms a gel that blinds the lauter bed or mash filter. The result is slow or stuck runoff, poor extract recovery and a long brew day. The certificate flags the risk through high beta-glucan (mg/L), high viscosity (mPa·s), low friability and patchy homogeneity — but each on its own is a weak signal, which is exactly the kind of multi-feature problem a model handles better than a single threshold.

## Reading runoff risk off the certificate

Treat it as ranking, not prophecy. Train a model on pairs of *malt certificate* and *what the runoff actually did* — lauter time, differential pressure, whether you had to rake or recirculate, final extract. The certificate features (beta-glucan, viscosity, friability, homogeneity, fine–coarse extract difference) become the inputs; the runoff outcome is the label. The model then scores each new lot: *this delivery sits in the top decile for runoff risk — schedule a beta-glucanase rest.* This is squarely the data-science discipline of measure-first: the model is only as good as your habit of logging lauter performance against the lot that caused it. Most brewhouses have the certificates and never join them to the runoff records — that join is the whole project.

## A copilot that reads the certificate

The generative-AI layer turns a dense PDF into a decision. A copilot grounded in the lot's extracted numbers and your spec can read the certificate, say in plain language "beta-glucan is 220 mg/L and viscosity 1.65 — above your stuck-mash threshold; recommend a 20-minute rest at 45°C and a coarser mill gap," and draft that straight into the brew sheet. It can compare the lot to the last five of the same malt and surface the one time a similar certificate gave you trouble. The model ranks the risk; the copilot explains it and writes the mash schedule. It pairs naturally with [predicting lauter and wort separation]({{ '/2023/predicting-lauter-wort-separation/' | relative_url }}) on the brewhouse side.

## Where the average lies

The honest limit is structural: a certificate is a *lot average*. A consignment can show acceptable mean beta-glucan while hiding a poorly modified fraction — a few sacks, one corner of a silo — and that pocket is what actually stalls a mash. A model trained on averages inherits the blind spot and will cheerfully pass the lot that ruins your Tuesday. Sampling matters as much as modelling. Add to that the brewhouse's own variability — mill gap, mash thickness, rake depth, sparge rate all move runoff independently of the malt — and you have a prediction that ranks risk usefully but never guarantees an outcome. Use it to decide *whether to insert the rest*, not to promise the lauter will fly.

## The bottom line

You can predict slow runoff from the malt, but as a risk ranking, not a verdict. Join your certificates to your lauter records, let a model flag the high-risk lots, and let a copilot turn that flag into a beta-glucanase rest on the brew sheet. Then respect what the average hides: sample well, keep the brewhouse variables steady, and treat a clean certificate as reassurance, not a guarantee.

## Frequently asked questions

**What causes slow runoff in the brewhouse?**
The usual culprit is high beta-glucan from under-modified malt. Beta-glucan is a gummy cell-wall polysaccharide; when malt is under-modified it survives into the mash, raises wort viscosity and binds the lauter bed or filter, giving slow or stuck runoff and lost extract.

**Can you predict beta-glucan and viscosity from the malt certificate?**
Partly. The certificate's modification, friability, homogeneity and measured beta-glucan and viscosity correlate with runoff behaviour, so a model trained on your past brews can rank a lot's runoff risk. But the certificate is a lot average and cannot see an under-modified fraction that drives most stuck mashes.

**How do you fix a high-beta-glucan malt?**
Give the mash a beta-glucanase rest around 45°C to let enzymes break down the gum, mill a little coarser, and avoid over-running the lauter. Catching the risk before brew day lets you build the rest into the mash schedule rather than firefighting a stuck runoff.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*
