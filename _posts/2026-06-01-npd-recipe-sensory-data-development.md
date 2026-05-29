---
layout: post
title: "Crunching Recipe and Sensory Data: How I Sped Up Beer Development"
image: /assets/og/npd-recipe-sensory-data-development.png
description: "Developing a new beer means closing the gap between a target flavour and what comes out of the pilot kettle. Here's how AI and sensory analytics cut the number of trial brews it took me to get there."
date: 2026-06-01
updated: 2026-06-01
tags: [beer-npd, brewing-science, sensory-analysis, machine-learning]
faq:
  - q: "Can AI design a beer recipe?"
    a: "AI can propose recipe and process adjustments and predict their likely effect on measurable outcomes like bitterness, colour and attenuation. It cannot taste, so it narrows the trials a brewer runs rather than replacing the brewer's palate or judgement."
  - q: "How does data reduce the number of trial brews?"
    a: "By learning the relationship between recipe and process inputs and the resulting analytical and sensory outputs from past batches, a model can rank the most promising next trial — so you converge on the target in fewer pilot brews instead of one-factor-at-a-time."
  - q: "Why does sensory panel data need so much cleaning?"
    a: "Tasters drift, scales are used differently, and a handful of panellists can swing a small panel. Calibrating tasters and accounting for that variance is what makes the data trustworthy enough to model — skip it and you model noise."
---

**Short answer: once a concept survived screening, my job was to close the gap between a target flavour brief and what actually came out of the pilot kettle. The slow way is trial-and-error — brew, taste, tweak, repeat. AI and sensory analytics let me learn from every past batch at once, so I converged on the target in fewer trial brews. The model proposes; the panel still tastes.** Here's how the development loop tightened.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 380" width="100%" style="max-width:760px;height:auto" role="img" aria-label="The beer development loop: brew a pilot, measure analytical and sensory data, compare to the target spec, let a model propose the next recipe tweak, and repeat until it converges."><rect x="0" y="0" width="760" height="380" fill="#fdfbf7"/><text x="380" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">THE DEVELOPMENT LOOP</text><g font-family="sans-serif"><rect x="300" y="60" width="160" height="56" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="380" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1c1a17">Pilot brew</text><text x="380" y="103" text-anchor="middle" font-size="11.5" fill="#6b6258">recipe + process</text><rect x="560" y="160" width="170" height="56" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="645" y="184" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1c1a17">Measure</text><text x="645" y="203" text-anchor="middle" font-size="11.5" fill="#6b6258">IBU · EBC · sensory</text><rect x="300" y="262" width="160" height="56" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="380" y="286" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1c1a17">Compare</text><text x="380" y="305" text-anchor="middle" font-size="11.5" fill="#6b6258">vs target brief</text><rect x="30" y="160" width="170" height="56" rx="8" fill="#7a1f3d" opacity="0.92"/><text x="115" y="184" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fdfbf7">Model proposes</text><text x="115" y="203" text-anchor="middle" font-size="11.5" fill="#f7ece0">next tweak</text></g><g fill="none" stroke="#b45309" stroke-width="2.2"><path d="M460 88 Q610 96 632 156"/><path d="M600 216 Q520 285 462 290"/><path d="M300 290 Q160 285 150 218"/><path d="M118 160 Q150 96 298 88"/></g><g fill="#b45309"><polygon points="628,150 638,158 626,162"/><polygon points="466,286 456,294 460,282"/><polygon points="156,222 146,214 152,210"/><polygon points="296,84 304,94 292,94"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Every trip round the loop is a real brew. The point of the data is to need fewer of them.</figcaption>
</figure>

## The brief is a flavour; the kettle speaks in numbers

A development brief reads like a sentence: *a crisp, sessionable lager, low bitterness, clean finish, pale straw colour.* The brewhouse answers in measurements — original gravity, attenuation, IBU, EBC colour, and the ester and higher-alcohol profile that fermentation throws off. Bridging those two languages is the whole job of development, and it is fundamentally a data problem.

For years I bridged it one factor at a time: change the hop addition, brew it, taste it, write it down. It works, but each loop is a real pilot brew measured in weeks. Developing a dozen beers that way, you spend most of your life waiting for fermentation.

## Letting past batches teach the next one

The shift was treating every pilot I had ever brewed as training data. Each batch is already a controlled experiment — recorded recipe and process inputs on one side, analytical and sensory outputs on the other. Pooled together, that history holds the relationship between what you do and what you get.

A model trained on it does something a single brewer's memory can't: it weighs hundreds of past batches at once and ranks the next trial most likely to hit the brief. It won't [design the recipe from scratch]({{ '/2026/can-ai-design-a-beer-recipe/' | relative_url }}) — but pointed at "get this bitterness down without thinning the body," it narrows a dozen plausible tweaks to the two worth brewing. Fewer loops, same target.

The honest precondition is the data science underneath it. Process logs had to be complete and consistent; "measure first, model second" is not a slogan when a missing mash temperature quietly breaks the prediction.

## The sensory data is the hard part

Analytical numbers are easy — instruments are repeatable. Sensory data is where development lives and dies, and it is gloriously messy. Tasters drift over a session, use scales differently, and on a small panel two strong opinions can swing the mean. Before any of it could be modelled, the panel had to be [calibrated and the variance understood]({{ '/2024/ai-sensory-panel-taster-calibration/' | relative_url }}) — otherwise you are modelling noise and calling it flavour.

Once the panel data was trustworthy, [digitising the tasting sheets]({{ '/2024/digitising-beer-tasting-panels-ai-power-bi/' | relative_url }}) let me track how a recipe's profile moved trial to trial instead of relying on scribbled notes. This is also where generative AI earns a place today: when a panel splits — half tasting an off-note, half not — an LLM can scan the comments and surface the descriptor language that separates the two camps, and draft the first version of the tasting notes for review. It explains the disagreement; it never resolves it. Only the panel does that.

## Where it breaks

A model is confident exactly where it has seen data, and naïve everywhere else. Push a recipe outside the range of past batches — a new hop variety, an unusual adjunct, a fermentation temperature you've never run — and the prediction is extrapolation dressed as fact. It learns the routine well and the genuinely novel poorly, which is awkward, because novelty is the point of development.

And it cannot taste. It can predict that bitterness will land near the target; it cannot tell you the beer is *boring*. The numbers can all be on-brief and the beer still not worth launching. That gap between "meets spec" and "worth drinking" is exactly the part of brewing no model touches.

## The bottom line

Recipe and sensory analytics didn't replace the trial brew — they made me run fewer of them. By learning from every batch I'd ever recorded, the data pointed at the next trial most likely to hit the brief, and digitised sensory tracking told me honestly whether I was getting closer. That turned development from a slow march into a guided search. But the model proposes and the panel disposes: the palate, and the judgement of whether a beer is actually good, stayed human. Next, the part of NPD that humbles everyone — making the pilot survive the jump to full scale.

*Beer NPD with Data — Part 2 of 3. [Full series]({{ '/series/beer-npd/' | relative_url }}) · [Previous: which beer to make]({{ '/2026/npd-which-beer-to-make-data/' | relative_url }}) · [Next: scaling pilot to production →]({{ '/2026/npd-scale-up-pilot-to-production-data/' | relative_url }})*

## Frequently asked questions

**Can AI design a beer recipe?**
AI can propose recipe and process adjustments and predict their likely effect on measurable outcomes like bitterness, colour and attenuation. It cannot taste, so it narrows the trials a brewer runs rather than replacing the brewer's palate or judgement.

**How does data reduce the number of trial brews?**
By learning the relationship between recipe and process inputs and the resulting analytical and sensory outputs from past batches, a model can rank the most promising next trial — so you converge on the target in fewer pilot brews instead of one-factor-at-a-time.

**Why does sensory panel data need so much cleaning?**
Tasters drift, scales are used differently, and a handful of panellists can swing a small panel. Calibrating tasters and accounting for that variance is what makes the data trustworthy enough to model — skip it and you model noise.
