---
layout: post
title: "Lot Genealogy as a Graph: Recursive Queries and a Recall Agent Built on MCP Tools"
image: /assets/og/wine-lot-genealogy-graph-recall-agent.png
description: "Part 4 of The Cellar Ledger. Which bottles contain fruit from block 7, and how much? Model the cellar as a graph of lots and volume-weighted movements, trace it with a recursive query, and put a GenAI agent in front of it through MCP tools that do the maths so the model does not have to."
date: 2026-07-07 09:00:00 -0700
updated: 2026-07-07
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, traceability]
faq:
  - q: "How do you trace a wine blend back to the vineyard block?"
    a: "Treat every lot as a node and every movement as an edge carrying a volume. When wine moves into a vessel, the new composition is the volume-weighted mix of what was there and what arrived. A recursive query walks the edges backwards from a bottling lot to its sources, or forwards from a vineyard block to every lot and bottling that contains it, multiplying the shares along the way."
  - q: "Do you need a graph database for winery traceability?"
    a: "Usually not. A winery has thousands of movements a year, not billions, and a recursive common table expression in the lakehouse or warehouse you already run handles that comfortably. A graph database becomes worth it when you have many sites, very long barrel histories, or you want graph algorithms beyond tracing."
  - q: "What does MCP add to a winery recall agent?"
    a: "MCP, the Model Context Protocol, is a standard way to give a language model a set of tools. For a recall agent, the tools are trace_back, trace_forward and bottling_status, each running a tested query. The model decides which tool to call and writes up the result, but every share and volume comes from the tool, not from the model's own arithmetic."
---

**Short answer: when a grower phones to say block 7 may have a residue problem, the question is which bottles contain block 7 fruit, and in what share. If the cellar is recorded as a graph of lots and volume-weighted movements, that is a recursive query that runs in seconds. Put a GenAI agent in front of it through a few MCP tools (trace back, trace forward, bottling status) and a winemaker can ask the question in plain English and get an answer with every percentage computed by tested code. The agent writes the recall memo. It never decides the recall.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A lot genealogy graph. Block 7 fruit goes into tank A at 10,000 litres, 100 percent block 7. 3,000 litres of tank A move into tank B, which already held 7,000 litres of block 9, so tank B becomes 30 percent block 7. 5,000 litres of tank B are blended with 5,000 litres of tank C, which is block 12, to make bottling lot D at 15 percent block 7. Tracing forward from block 7 therefore reaches bottling lot D at 15 percent.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">TRACE FORWARD FROM BLOCK 7: SHARES MULTIPLY ALONG THE EDGES</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="150" height="56" rx="9" fill="#06483f"/>
<text x="105" y="85" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">block 7</text>
<text x="105" y="103" text-anchor="middle" font-size="10.5" fill="#cfe6df">flagged by grower</text>
<rect x="30" y="160" width="150" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="105" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">block 9</text>
<rect x="30" y="250" width="150" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="105" y="275" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">block 12</text>
<rect x="250" y="60" width="170" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="335" y="84" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">tank A &#183; 10,000 L</text>
<text x="335" y="102" text-anchor="middle" font-size="10.5" fill="#00695c">100% block 7</text>
<rect x="490" y="140" width="190" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="585" y="164" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">tank B &#183; 10,000 L</text>
<text x="585" y="182" text-anchor="middle" font-size="10.5" fill="#00695c">30% block 7</text>
<rect x="490" y="250" width="190" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="585" y="274" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">tank C &#183; 5,000 L</text>
<text x="585" y="292" text-anchor="middle" font-size="10.5" fill="#4a6b64">0% block 7</text>
<rect x="770" y="190" width="200" height="66" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="870" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">bottling lot D</text>
<text x="870" y="238" text-anchor="middle" font-size="14" font-weight="700" fill="#ff4081">15% block 7</text>
<line x1="180" y1="88" x2="250" y2="88" stroke="#4db6a2" stroke-width="2"/>
<line x1="420" y1="100" x2="490" y2="155" stroke="#4db6a2" stroke-width="2"/>
<text x="470" y="118" text-anchor="middle" font-size="10" fill="#4a6b64">3,000 L</text>
<line x1="180" y1="188" x2="490" y2="170" stroke="#4db6a2" stroke-width="2"/>
<text x="330" y="172" text-anchor="middle" font-size="10" fill="#4a6b64">7,000 L</text>
<line x1="180" y1="278" x2="490" y2="278" stroke="#4db6a2" stroke-width="2"/>
<line x1="680" y1="175" x2="770" y2="215" stroke="#4db6a2" stroke-width="2"/>
<text x="728" y="185" text-anchor="middle" font-size="10" fill="#4a6b64">5,000 L</text>
<line x1="680" y1="278" x2="770" y2="235" stroke="#4db6a2" stroke-width="2"/>
<text x="728" y="272" text-anchor="middle" font-size="10" fill="#4a6b64">5,000 L</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">3,000 of 10,000 litres makes tank B 30% block 7. Half of tank D comes from B, so D is 15%. The maths is simple. Doing it across a cellar by hand is not.</figcaption>
</figure>

It is a Tuesday in September and a grower phones. A spray on block 7 may have gone on inside the withholding period. Nobody knows yet whether it matters, but the winery needs to know, today, where that fruit went. Which tanks? Which blends? Which bottlings, and which of those have already shipped?

In most wineries that becomes a two-day job with a stack of work orders and a spreadsheet. It does not need to be. The [movement ledger]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }}) from earlier in this series already holds every answer. It just needs to be read as a graph.

## The cellar is a graph already

Every lot of wine is a node. Every movement is an edge with a volume on it. Fruit from a block goes into a tank. Part of that tank goes into another tank that already holds something else. Two tanks are blended into a third, which is bottled.

When wine moves into a vessel, the new composition is a volume-weighted average:

> new share = (volume already there x its share + volume arriving x its share) / total volume

In the figure, tank B held 7,000 litres of block 9 and received 3,000 litres of block 7, so it is 30% block 7. Bottling lot D takes 5,000 litres from B and 5,000 from C, so it is 15% block 7. That is the whole mechanism. It just has to be applied to every movement in the right order, which is exactly what computers are for and exactly what people in a hurry get wrong.

## The recursive query

You do not need a graph database for this. A winery has thousands of movements a year, and a recursive common table expression in the warehouse you already run walks them comfortably.

```sql
WITH RECURSIVE forward AS (
  SELECT to_lot AS lot_id, share AS source_share, 1 AS depth
  FROM   lot_edges
  WHERE  from_lot = 'BLOCK-07-2025'
  UNION ALL
  SELECT e.to_lot, f.source_share * e.share, f.depth + 1
  FROM   forward f
  JOIN   lot_edges e ON e.from_lot = f.lot_id
  WHERE  f.depth < 30
)
SELECT lot_id, SUM(source_share) AS block7_share
FROM   forward
GROUP  BY lot_id;
```

Here `share` on each edge is the fraction of the destination lot that came from the source lot, computed once in the silver layer from the ledger volumes. Walk the edges forwards from a block and multiply the shares along the way: that gives every downstream lot and how much of the block it contains. Walk them backwards from a bottling lot and you get its full recipe, down to vineyard blocks.

The depth limit is not decoration. Barrel programmes with years of topping create long chains, and a stray loop from a data-entry error will otherwise run until the warehouse gives up.

## The same query proves the label

Genealogy is not only for bad days. The same composition answers the question the marketing team asks every vintage: can this blend carry the label we want?

The thresholds vary by market. In the EU, a variety or vintage on the label generally needs at least 85% of the wine to qualify. In the US, a varietal name needs 75% in most cases, an AVA needs 85%, and a vintage date needs 95% when an AVA is named and 85% otherwise. Those percentages are exactly what a backwards trace produces: share of the lot by variety, by vintage and by origin. Put the rules for your markets in a small table and a check can tell you, before the artwork is printed, whether a blend clears them and by how much.

## Putting a GenAI agent in front of it

A winemaker should not have to write a recursive CTE while the grower is still on the phone. This is a good job for an agent, if the agent is built so it cannot get the numbers wrong.

The Model Context Protocol (MCP) is the standard way to give a language model a set of tools in 2026. For traceability, three tools are enough:

- **`trace_forward(source, min_share)`** returns every lot and bottling containing a block or lot, with shares above a threshold.
- **`trace_back(lot)`** returns the full composition of a lot by block, variety and vintage.
- **`bottling_status(lot)`** returns cases produced, on hand and shipped, and to whom.

Each tool is a tested query. The agent's job is to understand the question, call the right tools in the right order and write up what they return. Asked "where did block 7 go, and has any of it shipped?", it calls `trace_forward`, then `bottling_status` for each bottling it finds, and produces a short memo: two tanks still in the cellar, one bottling at 15% block 7 with 400 cases shipped to three distributors, and the list of those distributors.

A few rules keep it trustworthy:

1. **Read-only tools.** The agent can look but not move wine or change records. Holds and recalls are actions a person takes.
2. **Numbers come from tool output only.** The memo quotes the shares and case counts the tools returned. If the model computes a figure itself, that is a bug in the prompt.
3. **Test it with mock recalls.** Many food and drink regimes expect you to trace one step back and one step forward, and good wineries run mock recall drills. Turn the last few drills into a test set with known answers and run the agent against them whenever anything changes.

The difference is time. A recall question that used to take two days of paperwork takes a few minutes, and the winemaker spends those minutes checking the answer instead of assembling it.

## Where this breaks

**Composition assumes perfect mixing.** The maths treats a tank as uniform. A tank that was topped without being stirred, or drawn from before a blend was mixed, is not. For recall purposes, assume the worst case and trace with generous thresholds.

**Topping creates dust.** Years of topping barrels from mixed sources leaves thousands of tiny fractions: 0.2% of this, 0.05% of that. Decide on a threshold below which a source is reported but not chased, and state it in the memo.

**The graph is only as good as the ledger.** One unrecorded transfer breaks the chain, and the trace will say block 7 stopped at tank B when it did not. The adjustment events from the [loss map]({{ '/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}) are a good early warning of where the chain is weak.

**The agent must not decide.** Whether to hold stock, notify distributors or recall is a judgement with legal and commercial weight. The agent gathers the facts fast. A person signs the decision.

## The bottom line

Every blend is a graph, whether or not the winery records it as one. Store the movements with their volumes, calculate composition once in the pipeline, and a recursive query answers the hardest question a grower can ask. Wrap those queries as MCP tools and a GenAI agent can answer it in plain English, with every percentage coming from code you have tested. The model makes the answer quick to reach. The ledger is what makes it right.

Next in the series: [excise returns as data contracts]({{ '/2026/wine-excise-returns-data-contracts-genai/' | relative_url }}), where the same ledger has to reconcile to the taxman. Blending from the other direction, choosing components to hit a target, is covered in [AI for Wine Blending Optimisation]({{ '/2024/ai-wine-blending-optimization/' | relative_url }}). The full list is on the [Cellar Ledger series page]({{ '/series/cellar-ledger/' | relative_url }}).

## Frequently asked questions

**How do you trace a wine blend back to the vineyard block?**
Treat every lot as a node and every movement as an edge carrying a volume. When wine moves into a vessel, the new composition is the volume-weighted mix of what was there and what arrived. A recursive query walks the edges backwards from a bottling lot to its sources, or forwards from a vineyard block to every lot and bottling that contains it, multiplying the shares along the way.

**Do you need a graph database for winery traceability?**
Usually not. A winery has thousands of movements a year, not billions, and a recursive common table expression in the lakehouse or warehouse you already run handles that comfortably. A graph database becomes worth it when you have many sites, very long barrel histories, or you want graph algorithms beyond tracing.

**What does MCP add to a winery recall agent?**
MCP, the Model Context Protocol, is a standard way to give a language model a set of tools. For a recall agent, the tools are trace_back, trace_forward and bottling_status, each running a tested query. The model decides which tool to call and writes up the result, but every share and volume comes from the tool, not from the model's own arithmetic.
