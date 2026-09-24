---
layout: page
title: "The Cellar Ledger: Data Engineering and GenAI for Wineries"
permalink: /series/cellar-ledger/
description: "A 6-part series on the data engineering and GenAI work under a winery's numbers: a semantic layer so the chatbot gives one answer, an event-sourced cellar ledger, a loss map pipeline, lot genealogy with a recall agent on MCP tools, excise returns as data contracts, and an honest look at why ten vintages is ten rows. By Ankur Napa."
---

Every winery now gets offered a chatbot for its data. Most of them will give confident answers on top of numbers nobody has defined, volumes people can edit and blends nobody can trace. This series is about the layer underneath: the data model and pipelines that make GenAI in a winery worth trusting, and the places where even a good foundation runs out.

Each post takes one number the cellar runs on, shows the data engineering that makes it reliable, and then puts a language model or an agent on top in the one role it is actually good at.

## The series

1. **[Ask the Chatbot for the Alcohol, Get Three Answers: GenAI Needs a Semantic Layer]({{ '/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }})**: why text-to-SQL assistants amplify undefined metrics, the real Brix to alcohol conversion, and instrument-aware bronze, silver and gold layers.
2. **[Event-Sourcing the Cellar: Why Winery Volumes Should Be Derived, Never Stored]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }})**: an append-only movement ledger in the lakehouse, and why agents should propose but never write.
3. **[The Loss Map: A Medallion Pipeline, Anomaly Flags and an LLM That Drafts the Variance Note]({{ '/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }})**: known loss versus the unexplained residual, robust statistics, and an LLM that writes but never calculates.
4. **[Lot Genealogy as a Graph: Recursive Queries and a Recall Agent Built on MCP Tools]({{ '/2026/wine-lot-genealogy-graph-recall-agent/' | relative_url }})**: volume-weighted composition, label thresholds, and a recall agent whose every percentage comes from tested code.
5. **[Excise Returns as Data Contracts: Tests Reconcile, the LLM Drafts, a Person Signs]({{ '/2026/wine-excise-returns-data-contracts-genai/' | relative_url }})**: the balance equation per tax class, nightly contract tests, and where GenAI helps with the messy text.
6. **[Where Winery AI Breaks: Ten Vintages Is Ten Rows]({{ '/2026/where-winery-ai-breaks-ten-vintages-ten-rows/' | relative_url }})**: small data, a moving climate, and what foundation models, synthetic data and LLMs can and cannot fix.

Read them in order, since each builds on the ledger from the one before. Every post is tagged [#cellar-ledger]({{ '/tags/' | relative_url }}#cellar-ledger). For the analytics argument that comes before this one, see [Process Intelligence for Wineries]({{ '/series/process-intelligence-wine/' | relative_url }}), and for the full wine catalogue, the [Winemaking &amp; AI track]({{ '/tracks/winemaking-ai/' | relative_url }}).
