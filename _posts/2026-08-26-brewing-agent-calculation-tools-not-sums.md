---
layout: post
title: "An Agent That Calls Calculation Tools Instead of Doing Sums"
image: /assets/og/brewing-agent-calculation-tools-not-sums.png
description: "Part 2 of The Brewer's Agent. Give a brewing assistant tools for gravity, attenuation, ABV and IBU, and make it name the method every time. Worked examples show why: the same beer is 64.9% attenuated on one scale and 78.6% on another, and three IBU models give 34, 45 and 46 for one hop addition."
date: 2026-08-26 09:00:00 -0700
updated: 2026-08-26
tags: [brewing-science, brewers-agent, generative-ai, tool-use, brewing-calculations]
faq:
  - q: "Why should a brewing AI assistant use tools for calculations?"
    a: "Because language models are unreliable at multi-step arithmetic and brewing formulas carry unit and temperature conventions that are easy to mix up. A tool is ordinary tested code: it takes inputs in stated units, applies one documented method and returns the result with that method named. The model decides which tool to call and explains the answer."
  - q: "What is the difference between real and apparent degree of fermentation?"
    a: "Apparent attenuation compares original extract with the apparent extract a hydrometer reads in the finished beer, which alcohol drags down because it is lighter than water. Real attenuation uses the true remaining extract. On the same beer the apparent figure is always higher, here 78.6% against 64.9%, so a number without its scale is ambiguous."
  - q: "Which IBU formula is correct, Tinseth or Rager?"
    a: "Neither is correct in general. They are empirical fits to different data, and for a 60-minute addition in a 13 degrees Plato wort they differ by roughly a third. Pick one for your brewery, calibrate it against measured bitterness from a lab, and have the tool report which model it used."
---

**Short answer: the most useful thing you can do for a brewing assistant is take arithmetic away from it. Give the agent a small set of tools (gravity conversion, attenuation, alcohol, bitterness), each one ordinary tested code that works in base units and returns its method with its result. The agent picks the tool and explains the answer. The two worked examples below show why the method has to travel with the number: one beer reads 64.9% attenuated on the real scale and 78.6% on the apparent scale, and three respected IBU models give 34, 45 and 46 for the same hop addition.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Two worked examples. On the left, one beer at 13.0 degrees Plato original extract shows real degree of fermentation 64.9 percent and apparent degree of fermentation 78.6 percent, a gap of 13.7 points on the same beer. On the right, one hop addition of 30 grams at 10 percent alpha acid in 20 litres, boiled 60 minutes, gives 33.8 IBU by Tinseth, 45.7 by Rager and 45.2 by a first-order kinetic model.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">SAME BEER, DIFFERENT NUMBERS: WHY THE METHOD TRAVELS WITH THE RESULT</text>
<g font-family="sans-serif">
<text x="245" y="60" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">ATTENUATION, ONE BEER (13.0 &#176;P)</text>
<rect x="60" y="90" width="260" height="36" rx="5" fill="#4db6a2"/>
<text x="70" y="113" font-size="12" font-weight="700" fill="#06483f">real (RDF)</text>
<text x="330" y="113" font-size="13" font-weight="700" fill="#06483f">64.9%</text>
<rect x="60" y="140" width="314" height="36" rx="5" fill="#06483f"/>
<text x="70" y="163" font-size="12" font-weight="700" fill="#ffffff">apparent (ADF)</text>
<text x="384" y="163" font-size="13" font-weight="700" fill="#06483f">78.6%</text>
<text x="245" y="208" text-anchor="middle" font-size="11" fill="#ff4081" font-weight="700">13.7 points apart, same tank</text>
<text x="745" y="60" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">IBU, ONE HOP ADDITION</text>
<text x="745" y="76" text-anchor="middle" font-size="10" fill="#4a6b64">30 g at 10% alpha, 20 L, 60 min</text>
<rect x="560" y="90" width="203" height="36" rx="5" fill="#4db6a2"/>
<text x="570" y="113" font-size="12" font-weight="700" fill="#06483f">Tinseth</text>
<text x="773" y="113" font-size="13" font-weight="700" fill="#06483f">33.8</text>
<rect x="560" y="140" width="274" height="36" rx="5" fill="#4db6a2"/>
<text x="570" y="163" font-size="12" font-weight="700" fill="#06483f">Rager</text>
<text x="844" y="163" font-size="13" font-weight="700" fill="#06483f">45.7</text>
<rect x="560" y="190" width="271" height="36" rx="5" fill="#4db6a2"/>
<text x="570" y="213" font-size="12" font-weight="700" fill="#06483f">kinetic model</text>
<text x="841" y="213" font-size="13" font-weight="700" fill="#06483f">45.2</text>
<rect x="40" y="258" width="920" height="54" rx="10" fill="#06483f"/>
<text x="500" y="282" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">NONE OF THESE NUMBERS IS WRONG &#183; EACH IS MEANINGLESS WITHOUT ITS METHOD</text>
<text x="500" y="300" text-anchor="middle" font-size="10.5" fill="#cfe6df">computed with tested code in base units; IBU figures are wort estimates before cellar losses</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">An assistant that says "attenuation is 78%" or "about 40 IBU" without a method has not answered the question.</figcaption>
</figure>

A brewer asks the assistant: "What attenuation did batch 212 get?" The honest answer is another question: which attenuation? A lab report will usually give real degree of fermentation. A homebrewer, or a sales sheet, will usually mean apparent. On the beer in the figure, those are 64.9% and 78.6%. Same tank, same day, same sample.

A language model left to itself will pick one, silently, and might do the conversion in its head on the way. The [first post in this series]({{ '/2026/rag-brewing-literature-without-hallucinated-maths/' | relative_url }}) argued that retrieval should supply the knowledge and code should supply the numbers. This post builds the code.

## What a tool is

In current agent frameworks (the Claude and OpenAI APIs, the Model Context Protocol, most orchestration libraries), a tool is a function the model can ask to run. You describe it with a name, a purpose and a schema for its inputs. The model decides when to call it and with what arguments. Your code runs it and hands back the result.

A brewing toolset does not need to be big. Five tools cover most questions:

- **`gravity_convert`**: specific gravity to degrees Plato and back, at a stated temperature basis.
- **`attenuation`**: real and apparent degree of fermentation from original, real and apparent extract.
- **`alcohol`**: alcohol by weight and by volume from original extract and RDF.
- **`bitterness`**: IBU for a hop addition, with the model named as an argument.
- **`unit_convert`**: litres, hectolitres, barrels, kilograms, pounds, with no guessing.

Here is what one looks like to the model:

```json
{
  "name": "bitterness",
  "description": "Estimate IBU in wort for one hop addition. Returns the value and the model used.",
  "input_schema": {
    "type": "object",
    "properties": {
      "hop_mass_g": {"type": "number"},
      "alpha_acid_pct": {"type": "number"},
      "volume_l": {"type": "number"},
      "boil_min": {"type": "number"},
      "wort_plato": {"type": "number"},
      "model": {"type": "string", "enum": ["tinseth", "rager", "kinetic"]}
    },
    "required": ["hop_mass_g", "alpha_acid_pct", "volume_l", "boil_min", "wort_plato", "model"]
  }
}
```

The `model` field is required on purpose, which means the assistant cannot ask for "the IBU". It has to ask for the Tinseth IBU or the Rager IBU. That one design choice does more for accuracy than any prompt.

## Worked example 1: the attenuation scale trap

Take a lager at 13.0 degrees Plato original extract, fermented to a real degree of fermentation of 64.9%.

The alcohol tool uses Balling's convention (each gram of alcohol consumes about 2.0665 grams of extract) to get a real extract of 4.77% and an alcohol of 4.27% by weight. To get from weight to volume, it needs the density of the finished beer, which depends on both the remaining extract and the alcohol together, so it uses a fitted model of beer density rather than a shortcut. That gives a specific gravity of about 1.0109 and an alcohol of **5.46% ABV**.

The attenuation tool then works out what a hydrometer would read in that beer. Alcohol is lighter than water, so the hydrometer reads an apparent extract of about 2.78 degrees Plato, well below the real 4.77. Apparent degree of fermentation compares original extract with that reading: **78.6%**. Real degree of fermentation compares it with the true remaining extract: **64.9%**.

Both numbers are right. They measure different things. A brewer comparing this beer to a yeast supplier's datasheet, which quotes apparent attenuation, and to the lab report, which quotes real, will see a 13.7 point gap and wonder what went wrong. Nothing went wrong. Somebody dropped the label.

A good tool returns both, named:

```text
attenuation(og_plato=13.0, rdf_pct=64.9)
  -> real_df_pct: 64.9, apparent_df_pct: 78.6,
     real_extract_plato: 4.77, apparent_extract_plato: 2.78,
     method: "Balling 2.0665; beer SG from extract-alcohol density model; 20/20 C"
```

## Worked example 2: three honest IBU numbers

Now a hop addition: 30 grams of a 10% alpha acid hop, boiled for 60 minutes in 20 litres of that 13.0 degrees Plato wort (specific gravity about 1.0525).

- **Tinseth** gives about 22.5% utilisation and **33.8 IBU**.
- **Rager** gives about 30.4% utilisation and **45.7 IBU**.
- A **first-order kinetic model** of alpha acid isomerisation and degradation (the Malowicki and Shellhammer rate constants at boiling point, with a gravity correction) gives about 30.1% of alpha acid isomerised in the wort and **45.2 IBU**.

Three published, widely used methods. A spread of about 12 IBU, roughly a third, on a single addition. Swap to a 15-minute addition and the order flips: Tinseth gives 11.2% utilisation and Rager 8.1%.

None of these is the truth. They are empirical models fitted to different data, and every one of them is an estimate in the wort before cellar and packaging losses take their share. The truth is what a lab measures in the finished beer. What matters for an assistant is that it never reports "about 40 IBU" as if that settled anything. It reports "45.7 IBU by Rager, wort estimate", and a brewer who calibrates against Tinseth knows immediately to discount it.

If you want to see these models side by side in a spreadsheet, the [IBU recipe builder in Excel]({{ '/2026/ibu-recipe-builder-excel/' | relative_url }}) walks through Tinseth for multiple additions, and [predicting hop bitterness with machine learning]({{ '/2023/predicting-hop-bitterness-ibu/' | relative_url }}) covers calibrating against measured values.

## The rules that make the agent trustworthy

1. **No arithmetic in prose.** The system prompt says any number derived from other numbers must come from a tool call. Test it by asking questions that tempt the model to shortcut, and fail any answer with a computed figure and no tool call behind it.
2. **Base units inside, display units outside.** Tools work in kilograms, litres and degrees Plato at a stated temperature. Conversion to pounds, barrels or specific gravity happens once, at the edge.
3. **The method is part of the output.** Every tool returns the method, constants and temperature basis it used, and the agent repeats them in the answer.
4. **Tools are tested like any other code.** Each tool has unit tests against published worked examples. The attenuation example above is one of them: if the tool stops returning 4.77 real extract and 4.27 alcohol for that input, the build fails.
5. **Ask before assuming.** If the brewer says "attenuation" or "gravity" without a scale, the agent asks which one, or answers with both.

## Where this breaks

**Tools encode choices.** Choosing Balling's constant, a density model or a utilisation model is a technical decision. The tool makes it consistent, not correct. Document the choices and let a brewer who knows better change them.

**Bad inputs still give bad outputs.** A tool fed an original extract that was read at the wrong temperature returns a precisely wrong answer. The agent should ask where the numbers came from when they look out of range.

**The agent can call the wrong tool.** A model can pick `alcohol` when it needed `attenuation`, or pass Plato where specific gravity was expected. Strict schemas with units in the field names, and a test set of real questions, catch most of it.

**Tools do not replace the lab.** Every figure here is a calculation from other measurements. Bitterness in particular should be measured, and the calculated value treated as a planning estimate.

## The bottom line

An assistant that does sums in its head will eventually give a brewer a wrong number in a confident voice. An assistant that calls tools gives the same number every time, with the method attached. The examples here are not edge cases: real and apparent attenuation sit 13.7 points apart on an ordinary lager, and three standard IBU models spread by a third on a single hop addition. Let the model choose the tool and explain the result. Let tested code do the maths.

Next in the series: [malt aroma wheels as vectors]({{ '/2026/malt-aroma-wheels-as-vectors-similarity-search/' | relative_url }}). The full list is on [The Brewer's Agent series page]({{ '/series/brewers-agent/' | relative_url }}).

## Frequently asked questions

**Why should a brewing AI assistant use tools for calculations?**
Because language models are unreliable at multi-step arithmetic and brewing formulas carry unit and temperature conventions that are easy to mix up. A tool is ordinary tested code: it takes inputs in stated units, applies one documented method and returns the result with that method named. The model decides which tool to call and explains the answer.

**What is the difference between real and apparent degree of fermentation?**
Apparent attenuation compares original extract with the apparent extract a hydrometer reads in the finished beer, which alcohol drags down because it is lighter than water. Real attenuation uses the true remaining extract. On the same beer the apparent figure is always higher, here 78.6% against 64.9%, so a number without its scale is ambiguous.

**Which IBU formula is correct, Tinseth or Rager?**
Neither is correct in general. They are empirical fits to different data, and for a 60-minute addition in a 13 degrees Plato wort they differ by roughly a third. Pick one for your brewery, calibrate it against measured bitterness from a lab, and have the tool report which model it used.
