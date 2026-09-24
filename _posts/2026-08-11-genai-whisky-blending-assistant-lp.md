---
layout: post
title: "A GenAI Blending Assistant With the Maths Done in Code: LP for the Vatting, Density Tables for the Water"
image: /assets/og/genai-whisky-blending-assistant-lp.png
description: "Part 5 of The Still and the Model. A language model can talk a blender through a vatting, but it should never do the sums. Cask selection is a linear programme, reduction to bottling strength needs ethanol-water contraction maths, and the age statement is a rule, not an average. The LLM calls the tools and explains the answer."
date: 2026-08-11 09:00:00 -0700
updated: 2026-08-11
tags: [distilling-maturation, still-and-model, generative-ai, optimisation, blending]
faq:
  - q: "Why can't you just subtract volumes to work out how much water to add to whisky?"
    a: "Because ethanol and water contract when mixed. Reducing 1,000 litres at 63.5% to 40% needs about 605 litres of water, not the 587.5 litres simple volume arithmetic suggests, and adding only 587.5 litres leaves the spirit at about 40.4%. The correct method works in mass using density tables at 20 degrees C, then confirms with a measurement."
  - q: "Can an LLM choose casks for a whisky blend?"
    a: "It should not choose them directly. Cask selection is an optimisation problem with hard constraints, such as volume, sensory targets and the age of the youngest whisky, and a linear programming solver handles it exactly. The LLM's job is to turn the blender's request into solver inputs, call the solver and explain the result."
  - q: "How does an age statement work in a whisky blend?"
    a: "In Scotch whisky and under EU rules, the age on the label is the age of the youngest whisky in the bottle. It is not an average. A blending tool must exclude every cask younger than the claim, however attractive its cost or flavour, and the optimiser should enforce that as a hard rule."
---

**Short answer: GenAI is a good interface for a blender and a poor calculator. Cask selection is a linear programme: hit a volume and sensory targets at the lowest value of stock used, with the age statement as a hard rule because the label states the youngest whisky, not the average. Reducing to bottling strength needs ethanol-water contraction maths: 1,000 litres at 63.5% needs about 605 litres of water to reach 40%, not 587.5. Put both calculations in tested code, expose them as tools, and let the language model do what it is good at: understand the request, call the tools and explain the answer in plain words.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The blending assistant architecture. A blender asks for a 12 year old vatting of 300 litres of absolute alcohol with a sherry character score of at least 6. The LLM calls two tools. The cask selection solver returns 94 litres of absolute alcohol from cask A, 130 from cask B and 76 from cask C, and excludes cask D because it is 10 years old. The reduction tool says 1,000 litres at 63.5 percent needs 604.9 litres of water to reach 40 percent, and that the naive 587.5 litres would leave it at 40.4 percent. The LLM then explains the result.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE LLM ASKS, THE TOOLS CALCULATE (ILLUSTRATIVE)</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="250" height="100" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="155" y="86" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">blender asks</text>
<text x="155" y="108" text-anchor="middle" font-size="10.5" fill="#4a6b64">12 year old vatting,</text>
<text x="155" y="125" text-anchor="middle" font-size="10.5" fill="#4a6b64">300 LAA, sherry score &#8805; 6,</text>
<text x="155" y="142" text-anchor="middle" font-size="10.5" fill="#4a6b64">lowest stock value used</text>
<line x1="280" y1="110" x2="340" y2="110" stroke="#4db6a2" stroke-width="2"/>
<rect x="340" y="75" width="160" height="70" rx="12" fill="#06483f"/>
<text x="420" y="106" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">LLM</text>
<text x="420" y="126" text-anchor="middle" font-size="10.5" fill="#cfe6df">calls tools, explains</text>
<line x1="500" y1="100" x2="560" y2="80" stroke="#4db6a2" stroke-width="2"/>
<line x1="500" y1="125" x2="560" y2="200" stroke="#4db6a2" stroke-width="2"/>
<rect x="560" y="50" width="410" height="100" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="765" y="74" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">select_casks() &#183; linear programme</text>
<text x="765" y="96" text-anchor="middle" font-size="11" fill="#06483f">A 94 LAA &#183; B 130 LAA &#183; C 76 LAA</text>
<text x="765" y="116" text-anchor="middle" font-size="11" fill="#06483f">sherry score 6.0, value 415</text>
<text x="765" y="136" text-anchor="middle" font-size="11" fill="#ff4081">D excluded: 10 years old</text>
<rect x="560" y="165" width="410" height="100" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="765" y="189" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">reduction_water() &#183; density tables</text>
<text x="765" y="211" text-anchor="middle" font-size="11" fill="#06483f">1,000 L at 63.5% to 40%: 604.9 L water</text>
<text x="765" y="231" text-anchor="middle" font-size="11" fill="#06483f">final 1,587.5 L, 635 LAA</text>
<text x="765" y="251" text-anchor="middle" font-size="11" fill="#ff4081">naive 587.5 L leaves it at 40.4%</text>
<rect x="30" y="286" width="940" height="40" rx="10" fill="#06483f"/>
<text x="500" y="311" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">EVERY NUMBER COMES FROM A TOOL &#183; THE MODEL NEVER DOES THE SUMS</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative stock and values. Both tools are ordinary, tested code. The language model is the interface.</figcaption>
</figure>

A blender asks a GenAI assistant how much water to add to take 1,000 litres of cask-strength spirit at 63.5% down to 40%. The assistant answers instantly: 587.5 litres. It shows its working, and the working is tidy. It is also wrong, and the error is not a rounding problem. It is chemistry that nobody told the model about.

This post is about building a blending assistant that cannot make that mistake, because it never does arithmetic at all. The [cask inventory]({{ '/2026/cask-inventory-data-engineering-scd2/' | relative_url }}) from the previous post supplies the stock. The maths lives in tools. The model talks.

## The water problem: why volumes do not add

Take 1,000 litres at 63.5% ABV. It holds 635 litres of absolute alcohol. At 40%, those 635 litres of alcohol make 635 / 0.40 = 1,587.5 litres of spirit. So the obvious answer is to add 587.5 litres of water.

The trouble is that ethanol and water shrink when mixed. The molecules pack more tightly together than either liquid does alone, so 1,000 litres of spirit plus 587.5 litres of water gives less than 1,587.5 litres. The strength ends up above target, about 40.4% in this case.

The correct method works in mass, which is conserved, using the density of ethanol-water mixtures at 20 degrees C:

```python
def reduction_water(vol_l, abv_in, abv_out, rho20):
    # rho20(abv) -> density in kg/L at 20 C, from the official alcoholometric tables
    laa = vol_l * abv_in / 100
    vol_out = laa / (abv_out / 100)
    mass_in = vol_l * rho20(abv_in)
    mass_out = vol_out * rho20(abv_out)
    return (mass_out - mass_in) / rho20(0)   # litres of water at 20 C
```

With densities of about 0.901 kg/L at 63.5% and 0.948 kg/L at 40%, the answer is roughly 605 litres of water, not 587.5. The missing 17 litres is the contraction.

Does 0.4% matter? The label tolerance for spirit strength under EU rules is 0.3% vol, and duty is paid on alcohol. Over-strength gives spirit away. Overshooting the other way is worse: in the UK and EU, whisky below 40% cannot be sold as whisky at all. That is why real reductions are done in stages, with demineralised water, and finished by measuring the strength with a density meter rather than trusting any calculation, however good.

## Cask selection is a linear programme

Choosing casks for a vatting is an optimisation problem in plain clothes. A simple version:

- **Decision:** how many litres of absolute alcohol to draw from each eligible cask.
- **Objective:** use the lowest total value of stock, so the most precious older casks are kept for where they matter.
- **Constraints:** the total alcohol target; each cask's available alcohol; sensory targets as weighted averages (for example, a sherry character score of at least 6 across the vatting); and the age rule.

A linear programming solver (SciPy, OR-Tools, or the one in your planning tool) solves this exactly in milliseconds. In the illustrative example, with a 12-year-old A cask (value 1.0 per LAA, sherry 3), a 14-year-old B (1.3, sherry 7) and an 18-year-old C (2.0, sherry 8), the cheapest vatting of 300 LAA with a sherry score of 6 takes 94 LAA from A, all 130 from B and 76 from C, for a stock value of 415.

## The age statement is a rule, not an average

Now add cask D: 10 years old, lovely sherry character (score 9), cheap at 0.8 per LAA. Let the solver use it and the cost drops to 302.5, a quarter less. It takes D in full and much less of the older stock.

It is also illegal for a 12-year-old label. Under the Scotch Whisky Regulations and EU rules, the age statement is the age of the youngest whisky in the bottle. It is not an average of the ages, however it is weighted. A tool that computes an average age and checks it against 12 will happily approve this vatting.

This is exactly the kind of domain rule a language model gets wrong in a conversation, and a solver gets right only if someone encodes it. So the age rule is not a constraint in the maths. It is a filter on which casks are allowed into the problem at all, applied in code before the solver ever runs.

## Where the LLM fits

With the calculations in tools, the language model has a useful and safe job:

1. **Turn the request into inputs.** "Something like last year's 12, a bit more sherry, 300 LAA, don't touch the 25-year-olds" becomes a target, constraints and an exclusion list. The assistant shows the inputs back for confirmation before running anything.
2. **Call the tools.** `select_casks` for the vatting, `reduction_water` for the reduction, `cask_history` from the inventory for anything the blender asks about a specific cask.
3. **Explain the result.** Why cask B was used in full (it is the cheapest way to lift the sherry score), why D was excluded (age), and what would change if the sherry target moved to 5.
4. **Never produce a number itself.** Every figure in the explanation comes from a tool output. If the blender asks a quantitative question the tools cannot answer, the assistant says so.

The blender stays the decision-maker, and the nose stays the final test. The [blending consistency post]({{ '/2024/ai-whiskey-blending-consistency/' | relative_url }}) covers matching a house style from sensory and chemical data. This post is about making sure the arithmetic around it is never the weak link.

## Where this breaks

**Sensory scores are not linear.** The solver treats a vatting's sherry score as the weighted average of its casks. Flavour does not always blend that politely: one assertive cask can dominate far beyond its share. Treat the optimum as a starting recipe for a sample vatting, not as the final blend.

**Density tables must be the official ones.** The sketch above is only as good as `rho20`. For duty and labelling, use the official alcoholometric tables (OIML R22 or your authority's equivalent) and a calibrated instrument, not an approximation someone typed in.

**Blending strengths also contracts a little.** Mixing two spirits of different strengths shrinks slightly too, so the vatting's volume is not exactly the sum of the casks. For casks of similar strength the effect is small, but work in alcohol and measure the result.

**Stock values are a policy choice.** Minimising stock value encodes a view of which casks matter most. Get that view from the people who own the maturing inventory, and let them change it.

## The bottom line

A language model will answer a blending question in fluent, confident sentences, including the ones that break chemistry or the law. Keep it away from the sums. Put cask selection in a solver, with the age statement as a hard filter. Put reduction in code that uses density tables and conserves mass. Then let the model do the part it is genuinely good at: understanding what the blender meant, calling the right tools and explaining the answer. The model sees the numbers. The blender tastes the vatting.

Next, and last, in the series: [where distillery AI breaks]({{ '/2026/where-distillery-ai-breaks/' | relative_url }}). For the sensory side of blending in a dashboard, see [the whisky blending and sensory dashboard]({{ '/2023/tableau-whisky-blending-sensory-dashboard/' | relative_url }}). The full list is on [The Still and the Model series page]({{ '/series/still-and-model/' | relative_url }}).

## Frequently asked questions

**Why can't you just subtract volumes to work out how much water to add to whisky?**
Because ethanol and water contract when mixed. Reducing 1,000 litres at 63.5% to 40% needs about 605 litres of water, not the 587.5 litres simple volume arithmetic suggests, and adding only 587.5 litres leaves the spirit at about 40.4%. The correct method works in mass using density tables at 20 degrees C, then confirms with a measurement.

**Can an LLM choose casks for a whisky blend?**
It should not choose them directly. Cask selection is an optimisation problem with hard constraints, such as volume, sensory targets and the age of the youngest whisky, and a linear programming solver handles it exactly. The LLM's job is to turn the blender's request into solver inputs, call the solver and explain the result.

**How does an age statement work in a whisky blend?**
In Scotch whisky and under EU rules, the age on the label is the age of the youngest whisky in the bottle. It is not an average. A blending tool must exclude every cask younger than the claim, however attractive its cost or flavour, and the optimiser should enforce that as a hard rule.
