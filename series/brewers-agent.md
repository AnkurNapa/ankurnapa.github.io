---
layout: page
title: "The Brewer's Agent: GenAI and Data Engineering for Brewing"
permalink: /series/brewers-agent/
description: "A 6-part series on building GenAI tools for brewing that a brewer can trust: RAG that cites its source, an agent that calls calculation tools, malt aroma wheels as vectors, scraping and trend-mining 250 homebrew recipes, evals for a brewing assistant, and what 1,000 beverage-AI companies are actually building. By Ankur Napa."
---

A brewing assistant that sounds right is easy to build. One that is right, and can show you why, takes more work: retrieval that cites the page, tools that do the maths in base units, data that has been cleaned and checked, and tests that run every time something changes.

This series builds that stack one layer at a time, with brewing science as the worked example throughout. Every number in it was computed with tested code, and every post has a section on where the approach breaks.

## The series

1. **[RAG Over the Brewing Literature Without Hallucinated Maths]({{ '/2026/rag-brewing-literature-without-hallucinated-maths/' | relative_url }})**: chunking formulas with their units, hybrid search for brewing acronyms, mandatory citations, and why arithmetic leaves the model.
2. **[An Agent That Calls Calculation Tools Instead of Doing Sums]({{ '/2026/brewing-agent-calculation-tools-not-sums/' | relative_url }})**: a small brewing toolset, the real versus apparent attenuation trap, and three IBU models that disagree by a third.
3. **[Malt Aroma Wheels as Vectors: Similarity Search and the Blend That Averaging Hides]({{ '/2026/malt-aroma-wheels-as-vectors-similarity-search/' | relative_url }})**: 51 digitised wheels, why raw cosine flatters everything, hybrid filters, and potency-weighted blending.
4. **[Scraping and Trend-Mining 250 Public Homebrew Recipes]({{ '/2026/scraping-trend-mining-250-homebrew-recipes/' | relative_url }})**: polite scraping, parsing traps, base units, regex versus LLM, and what the recipes said.
5. **[Evals for a Brewing Assistant]({{ '/2026/evals-for-a-brewing-assistant/' | relative_url }})**: golden questions written by brewers, numeric tolerances, refusals tested on purpose, and the limits of LLM-as-judge.
6. **[What 1,000 Beverage-AI Companies Are Actually Building]({{ '/2026/what-1000-beverage-ai-companies-are-building/' | relative_url }})**: a counted, graded dataset, and why the foundation matters more than the GenAI on top.

Read them in order, since each builds on the one before. Every post is tagged [#brewers-agent]({{ '/tags/' | relative_url }}#brewers-agent). The wine companion is [The Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}), and the full brewing catalogue is on the [Brewing Science &amp; AI track]({{ '/tracks/brewing-science-ai/' | relative_url }}).
