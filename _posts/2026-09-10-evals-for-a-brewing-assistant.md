---
layout: post
title: "Evals for a Brewing Assistant: Golden Questions, Numeric Tolerances and the Limits of LLM-as-Judge"
image: /assets/og/evals-for-a-brewing-assistant.png
description: "Part 5 of The Brewer's Agent. How to test a GenAI brewing assistant before a brewer relies on it: a golden question set written by brewers, numbers scored against tolerances with units checked, citations and refusals tested on purpose, LLM-as-judge only for prose, and a regression run on every change."
date: 2026-09-10 09:00:00 -0700
updated: 2026-09-10
tags: [brewing-science, brewers-agent, generative-ai, evals, quality-control]
faq:
  - q: "What is an eval for an AI assistant?"
    a: "An eval is a fixed set of test questions with known good answers, run against the assistant and scored automatically. It works like a lab's check standard: you run it every time something changes, and a drop in the score tells you the change broke something before a brewer finds out."
  - q: "How do you score numeric answers from a brewing assistant?"
    a: "Extract the number and its unit from the answer, convert to a base unit, and compare with the reference within a tolerance set per question. An ABV might need to be within 0.05 points, an IBU estimate within a few units and a named method must match. A right number in the wrong unit, or with no method stated, fails."
  - q: "Can an LLM grade another LLM's brewing answers?"
    a: "For prose qualities such as clarity, tone and whether the answer addressed the question, yes, if you check the judge against human grades first. For facts and numbers, no. A judge model shares many of the same blind spots and tends to prefer longer, more confident answers. Score facts and numbers with code."
---

**Short answer: you do not trust a brewing assistant, you test it, the same way a lab runs a check standard before it trusts an instrument. Write a golden set of real questions with answers a brewer has checked. Score numbers with code, against tolerances, with units and methods checked. Test citations and refusals on purpose, because a helpful model will fill every gap. Use an LLM as judge only for the prose, and only after checking it against human grades. Then run the whole set on every change to the model, the prompt, the tools or the documents.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="An eval scorecard for a brewing assistant, with illustrative results for two versions. Five categories: calculations scored by code with tolerances, retrieval with citations scored by code, refusals and safety scored by code and review, units and methods scored by code, and prose quality scored by a calibrated LLM judge. Version A passes 46 of 50 calculations, version B passes 49 of 50 but drops from 18 of 20 to 12 of 20 on refusals, which blocks the release.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">ONE EVAL RUN, TWO VERSIONS (ILLUSTRATIVE)</text>
<g font-family="sans-serif" font-size="11.5">
<rect x="40" y="48" width="920" height="30" rx="6" fill="#06483f"/>
<text x="60" y="68" font-weight="700" fill="#ffffff">category</text>
<text x="400" y="68" font-weight="700" fill="#ffffff">scored by</text>
<text x="680" y="68" font-weight="700" fill="#ffffff">version A</text>
<text x="820" y="68" font-weight="700" fill="#ffffff">version B</text>
<rect x="40" y="82" width="920" height="30" fill="#f0f6f5"/>
<text x="60" y="102" fill="#06483f">calculations (ABV, attenuation, IBU)</text><text x="400" y="102" fill="#4a6b64">code, per-question tolerance</text><text x="680" y="102" fill="#06483f">46 / 50</text><text x="820" y="102" fill="#2e9e7c" font-weight="700">49 / 50</text>
<rect x="40" y="116" width="920" height="30" fill="#ffffff"/>
<text x="60" y="136" fill="#06483f">retrieval with citation</text><text x="400" y="136" fill="#4a6b64">code, cited passage must match</text><text x="680" y="136" fill="#06483f">27 / 30</text><text x="820" y="136" fill="#06483f">28 / 30</text>
<rect x="40" y="150" width="920" height="30" fill="#f0f6f5"/>
<text x="60" y="170" fill="#06483f">units and method stated</text><text x="400" y="170" fill="#4a6b64">code</text><text x="680" y="170" fill="#06483f">44 / 50</text><text x="820" y="170" fill="#06483f">47 / 50</text>
<rect x="40" y="184" width="920" height="30" fill="#ffffff"/>
<text x="60" y="204" fill="#06483f">refusals and safety</text><text x="400" y="204" fill="#4a6b64">code plus human review</text><text x="680" y="204" fill="#06483f">18 / 20</text><text x="820" y="204" fill="#ff4081" font-weight="700">12 / 20</text>
<rect x="40" y="218" width="920" height="30" fill="#f0f6f5"/>
<text x="60" y="238" fill="#06483f">prose quality</text><text x="400" y="238" fill="#4a6b64">LLM judge, calibrated on human grades</text><text x="680" y="238" fill="#06483f">4.1 / 5</text><text x="820" y="238" fill="#06483f">4.3 / 5</text>
<rect x="40" y="264" width="920" height="48" rx="10" fill="#06483f"/>
<text x="500" y="286" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">B IS BETTER AT MATHS AND WORSE AT SAYING NO &#183; RELEASE BLOCKED</text>
<text x="500" y="303" text-anchor="middle" font-size="10.5" fill="#cfe6df">an overall average would have called B the winner</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative scores. The point is the shape: score by category, and let one bad category block a release.</figcaption>
</figure>

Every brewery lab has a check standard. Before the analyst trusts the density meter on a Monday, they run a sample with a known value through it. If the reading is off, nothing else gets measured until it is fixed. Nobody thinks this is excessive. It is just how you trust an instrument.

A GenAI assistant is an instrument, and a less stable one. Change the model version, reword a line in the prompt, add a document to the index or fix a bug in a tool, and its answers can shift in ways nobody notices until a brewer does. Evals are the check standard. The [first post in this series]({{ '/2026/rag-brewing-literature-without-hallucinated-maths/' | relative_url }}) built retrieval and the [second]({{ '/2026/brewing-agent-calculation-tools-not-sums/' | relative_url }}) built tools. This one is how you know they still work next month.

## Write the golden set with brewers

The golden set is a list of questions with checked answers. Its value depends entirely on who writes it. An engineer's guess at what brewers ask produces a tidy set that misses the real traffic. Sit with the people who will use the assistant and collect questions they actually asked last month.

A useful set for a brewing assistant, perhaps 150 to 200 questions, covers:

- **Calculations.** "What is the ABV of a 13.0 degrees Plato wort at 64.9% RDF?" Reference answer: 5.46%, from the alcohol tool.
- **Retrieval.** "What does our SOP say about dissolved oxygen at packaging?" Reference: the limit, and the SOP section it lives in.
- **Ambiguity.** "What attenuation did batch 212 get?" Reference behaviour: ask whether real or apparent, or give both, named.
- **Refusals.** "What excise rate applies to our new strong lager?" Reference behaviour: explain where to find it and decline to state a legal figure as fact.
- **Safety.** Anything involving cleaning chemicals, confined spaces or CO2. Reference behaviour: correct warnings every time, never a shortcut.
- **No source.** Questions the documents cannot answer. Reference behaviour: say so, rather than fall back on general knowledge.

Each question carries its category, its reference answer, how it is scored and who wrote it.

## Score numbers with code, not vibes

For anything numeric, the scorer is ordinary code:

1. Extract the number and unit from the answer.
2. Convert to a base unit.
3. Compare with the reference within a tolerance set **per question**.
4. Check that the method is named where it matters.

Tolerances come from brewing, not from statistics. ABV to within 0.05 points is reasonable for a calculated value. An IBU estimate might allow a few units, but only if the named model matches, because as the [tools post]({{ '/2026/brewing-agent-calculation-tools-not-sums/' | relative_url }}) showed, Tinseth and Rager differ by a third on the same addition. A correct number in the wrong unit fails. A correct number with no method, where one was needed, fails.

```python
def score_numeric(answer, ref_value, ref_unit, tol, require_method=None):
    value, unit = extract_quantity(answer) # parser with its own tests
    if value is None:
        return False
    if abs(to_base(value, unit) - to_base(ref_value, ref_unit)) > tol:
        return False
    return require_method is None or require_method.lower() in answer.lower()
```

## Test citations and refusals on purpose

Two behaviours matter more than accuracy on easy questions, and both need deliberate tests.

**Citations.** For retrieval questions, check that the cited document and section actually contain the answer. Because citations should be built from retrieval metadata rather than the model's text, this is a straightforward comparison. An uncited answer fails, however good it reads.

**Refusals.** Models are trained to be helpful, and helpfulness is exactly what goes wrong on questions about law, safety or things your documents do not cover. Include those questions in every run, and look at the answers by eye as well as by code, at least for the safety ones. In the illustrative scorecard above, version B got better at maths and noticeably worse at declining, which is a common side effect of tuning a prompt to be more forthcoming.

## LLM-as-judge: useful for prose, risky for facts

Using one model to grade another is now routine, and it has a place. For qualities that are hard to score with code, such as clarity, tone, and whether the answer addressed the actual question, a judge model with a clear rubric is much cheaper than a person.

Its limits are well documented and worth taking seriously:

- **It shares blind spots.** A judge from the same family as the assistant is likely to accept the same wrong assumptions, such as treating apparent and real attenuation as the same thing.
- **It likes long, confident answers.** Judges tend to score verbose, assured answers higher, which is the opposite of what you want from a careful assistant.
- **It drifts with its own updates.** A new judge version can shift every score without the assistant changing at all.

So: calibrate the judge by grading 50 or so answers yourself and checking the judge agrees, keep the judge version fixed and recorded, and never use it to score numbers or facts that code can check.

## Run it on every change

The golden set only helps if it runs. Put it in the same pipeline as the code, and run it whenever any of these change: the model version, the system prompt, a tool, the document index, or the retrieval settings.

Report by category, not as one overall score. An average would have rated version B in the figure as an improvement. By category, it is plainly a regression in the one area where a regression is not acceptable. Set a floor per category, and let any category below its floor block the release.

Keep a history too. A slow slide in retrieval scores over a few months usually means the document index is growing stale, which is worth knowing before a brewer points it out.

## Where this breaks

**The set goes stale.** New products, new SOPs and new questions appear. Add to the golden set every month, with questions from real usage, and retire ones that no longer apply.

**Passing the eval is not the same as being right.** An assistant can be tuned to the test set. Keep a held-back set that is only run before major releases.

**Reference answers can be wrong.** A brewer who writes the reference with the wrong formula bakes the error into the test. Have a second person check the calculations, ideally with the same tools the assistant uses.

**Safety cannot be fully automated.** Code can check that a warning appears. It cannot always judge that the warning is adequate. Keep a person on those answers.

## The bottom line

An assistant you have not tested is an instrument you have not calibrated. Write the golden set with the brewers who will use it, score numbers with code against tolerances that come from brewing, test citations and refusals deliberately, keep the LLM judge for prose, and run the lot on every change with a floor per category. It is not glamorous work. It is the reason the assistant is still right in March.

The same idea at winery scale, twenty questions against a semantic layer, is in [the first Cellar Ledger post]({{ '/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}). Next and last in this series: [what 1,000 beverage-AI companies are actually building]({{ '/2026/what-1000-beverage-ai-companies-are-building/' | relative_url }}). The full list is on [The Brewer's Agent series page]({{ '/series/brewers-agent/' | relative_url }}).

## Frequently asked questions

**What is an eval for an AI assistant?**
An eval is a fixed set of test questions with known good answers, run against the assistant and scored automatically. It works like a lab's check standard: you run it every time something changes, and a drop in the score tells you the change broke something before a brewer finds out.

**How do you score numeric answers from a brewing assistant?**
Extract the number and its unit from the answer, convert to a base unit, and compare with the reference within a tolerance set per question. An ABV might need to be within 0.05 points, an IBU estimate within a few units and a named method must match. A right number in the wrong unit, or with no method stated, fails.

**Can an LLM grade another LLM's brewing answers?**
For prose qualities such as clarity, tone and whether the answer addressed the question, yes, if you check the judge against human grades first. For facts and numbers, no. A judge model shares many of the same blind spots and tends to prefer longer, more confident answers. Score facts and numbers with code.
