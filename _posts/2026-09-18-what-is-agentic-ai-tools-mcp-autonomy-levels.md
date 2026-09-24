---
layout: post
title: "What Agentic AI Is: Tools, the Plan-Act-Observe Loop, MCP and Five Levels of Autonomy"
image: /assets/og/what-is-agentic-ai-tools-mcp-autonomy-levels.png
description: "Part 3 of AI for Operational Excellence in Beverage Plants. An agent is a language model that can use tools and take several steps towards a goal. How the loop works, what tools and MCP are, what memory means, and a five-level autonomy ladder (L0 to L4) for deciding how much a plant should let an agent do on its own."
date: 2026-09-18 09:00:00 -0700
updated: 2026-09-18
tags: [brewing-science, ai-opex, ai-basics, agentic-ai, generative-ai]
faq:
  - q: "What is the difference between a chatbot and an AI agent?"
    a: "A chatbot answers one message with one reply from what it already has. An agent is given a goal and a set of tools, then works in a loop: it plans a step, calls a tool such as a database query, looks at the result and decides the next step, until it has an answer or needs a person. The model is the same kind; the tools and the loop make it an agent."
  - q: "What is MCP in agentic AI?"
    a: "MCP, the Model Context Protocol, is an open standard for connecting language models to tools and data sources. Instead of writing a custom integration for every model and every system, you build an MCP server once for, say, your maintenance system, and any MCP-capable assistant can use its tools. It describes what each tool does, what inputs it takes and what it returns."
  - q: "How much autonomy should an AI agent have in a beverage plant?"
    a: "Match autonomy to the cost of a mistake. Reading data and drafting are low risk, so agents can do them freely. Anything that changes a record should be proposed by the agent and approved by a person. Anything that touches process control, such as a setpoint or a PLC, should stay out of an agent's reach entirely."
---

**Short answer: an agent is a language model with tools and a loop. You give it a goal, such as "find out why line 2 lost 40 minutes last night". It plans a step, calls a tool (query the line stop log), looks at the result, decides the next step (check the maintenance system for that asset) and keeps going until it has an answer or needs a person. MCP is the standard plug that connects models to those tools. Memory lets it carry context between steps and sessions. The important design question is not how clever the agent is, it is how much it may do alone. I use a five-level ladder, L0 to L4, and on a plant floor most agents should live at L1 or L2.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 360" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Left: the agent loop. A goal feeds a plan step, then act by calling a tool, then observe the result, which loops back to plan until the agent answers or asks a person. Tools listed are the line stop log, the maintenance system and the SOP library, connected through MCP. Right: an autonomy ladder from L0 to L4. L0, no agent. L1, reads and explains. L2, drafts actions a person approves. L3, acts within tight limits, a person can veto. L4, acts alone and a person monitors. L1 and L2 are highlighted as the plant floor default, and a note says process control writes stay off the ladder.">
<rect width="1000" height="360" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">HOW AN AGENT WORKS, AND HOW MUCH IT MAY DO</text>
<g font-family="sans-serif">
<rect x="40" y="56" width="120" height="44" rx="9" fill="#06483f"/>
<text x="100" y="83" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">goal</text>
<rect x="200" y="56" width="120" height="44" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="83" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">plan</text>
<rect x="200" y="136" width="120" height="44" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="163" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">act</text>
<rect x="200" y="216" width="120" height="44" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="243" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">observe</text>
<line x1="160" y1="78" x2="200" y2="78" stroke="#4db6a2" stroke-width="2"/>
<line x1="260" y1="100" x2="260" y2="136" stroke="#4db6a2" stroke-width="2"/>
<line x1="260" y1="180" x2="260" y2="216" stroke="#4db6a2" stroke-width="2"/>
<path d="M200 238 C150 238 150 78 200 78" fill="none" stroke="#4db6a2" stroke-width="2"/>
<line x1="320" y1="158" x2="360" y2="158" stroke="#4db6a2" stroke-width="2"/>
<rect x="360" y="120" width="150" height="80" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.5"/>
<text x="435" y="140" text-anchor="middle" font-size="10.5" font-weight="700" fill="#00695c">tools via MCP</text>
<text x="435" y="158" text-anchor="middle" font-size="10" fill="#4a6b64">line stop log</text>
<text x="435" y="173" text-anchor="middle" font-size="10" fill="#4a6b64">maintenance system</text>
<text x="435" y="188" text-anchor="middle" font-size="10" fill="#4a6b64">SOP library</text>
<text x="260" y="290" text-anchor="middle" font-size="10.5" fill="#4a6b64">loop until answered, or ask a person</text>
<text x="755" y="58" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">AUTONOMY LADDER</text>
<rect x="560" y="70" width="390" height="36" rx="7" fill="#ffffff" stroke="#4a6b64" stroke-width="1.2"/>
<text x="575" y="93" font-size="11" fill="#4a6b64"><tspan font-weight="700">L4</tspan> acts alone, a person monitors</text>
<rect x="560" y="112" width="390" height="36" rx="7" fill="#ffffff" stroke="#4a6b64" stroke-width="1.2"/>
<text x="575" y="135" font-size="11" fill="#4a6b64"><tspan font-weight="700">L3</tspan> acts within tight limits, a person can veto</text>
<rect x="560" y="154" width="390" height="36" rx="7" fill="#00695c"/>
<text x="575" y="177" font-size="11" fill="#ffffff"><tspan font-weight="700">L2</tspan> drafts actions, a person approves</text>
<rect x="560" y="196" width="390" height="36" rx="7" fill="#00695c"/>
<text x="575" y="219" font-size="11" fill="#ffffff"><tspan font-weight="700">L1</tspan> reads data and explains</text>
<rect x="560" y="238" width="390" height="36" rx="7" fill="#f0f6f5" stroke="#00695c" stroke-width="1.2"/>
<text x="575" y="261" font-size="11" fill="#06483f"><tspan font-weight="700">L0</tspan> no agent, people do it</text>
<text x="755" y="296" text-anchor="middle" font-size="10.5" font-weight="700" fill="#00695c">plant floor default: L1 and L2</text>
<rect x="40" y="312" width="910" height="36" rx="9" fill="#06483f"/>
<text x="495" y="335" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">PLC AND SCADA WRITES ARE NOT ON THIS LADDER &#183; AGENTS NEVER TOUCH PROCESS CONTROL</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The loop is what makes it an agent. The ladder is what makes it safe to run one in a plant.</figcaption>
</figure>

The night shift on line 2 lost 40 minutes. In the morning meeting, someone asks why. Normally the answer takes half an hour: open the line stop log, find the long stops, look up the asset in the maintenance system, check whether it has failed before, read the shift notes, then piece it together.

A chatbot cannot do that. It can only answer from what you paste into it. An **agent** can, because it can go and fetch each piece itself. This post, the third in the series, explains how. The [previous post]({{ '/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}) covered what a language model is. An agent is the same model with two additions: tools and a loop.

## Tools: what an agent can reach

A **tool** is a function the model is allowed to call. It has a name, a description in plain language, defined inputs and a defined output. For a plant, useful tools might be:

- `get_line_stops(line, start, end)` returns every stop with duration, fault code and asset
- `get_asset_history(asset_id)` returns past work orders and failures from the maintenance system
- `search_sop(query)` returns the relevant SOP passages with section numbers
- `get_shift_notes(line, shift)` returns what the operators wrote

The model never runs SQL against the maintenance database directly. It asks for a tool by name with some inputs, ordinary software runs a tested query and the result comes back as text. That separation is the most important safety property an agent has. The model decides **what** to look up. Code decides **how**, and what is allowed.

## The loop: plan, act, observe

With tools available, the model works in a loop:

1. **Plan.** Given the goal and what it knows so far, decide the next step. "First, find the long stops on line 2 last night."
2. **Act.** Call a tool. `get_line_stops("L2", "22:00", "06:00")`.
3. **Observe.** Read the result. Six stops, four of them the labeller glue unit, 31 minutes in total.
4. **Repeat.** Plan the next step with the new information. "Check the glue unit's maintenance history." And so on.

The loop ends when the agent has enough to answer, or when it reaches something it should not decide alone and hands over to a person. For the line 2 question, a good agent might finish with: most of the 40 minutes was the labeller glue unit, four stops with the same fault code; the same fault appears in two work orders last month; the shift notes mention glue temperature; the SOP section on glue unit start-up is 6.3.

That is not magic. It is the half-hour manual job done in a minute, with every step visible.

## MCP: the standard plug

Until recently, connecting a model to a tool meant writing custom code for each model and each system. The **Model Context Protocol (MCP)**, an open standard released by Anthropic in late 2024 and since adopted widely, fixes that. You build an MCP server once for, say, the maintenance system. It describes its tools in a standard way. Any assistant that speaks MCP can then use them.

For a plant, the practical benefit is ownership. The maintenance team can own the MCP server for the maintenance system and decide exactly which tools it exposes. The quality team can own the one for the LIMS. If a tool is not on the server, no agent can use it, whichever model sits on top.

## Memory: what the agent carries

Language models remember nothing between conversations. Agents add memory in two forms:

- **Working memory** is the context window during a task: the goal, each tool call and each result. It is why the agent knows, at step four, what it found at step one.
- **Long-term memory** is anything stored outside the model and read back later: notes from past investigations, a list of known recurring faults, a user's preferences.

Long-term memory is powerful and needs the same care as any other record. If an agent "remembers" a wrong conclusion from last month, it will reuse it with confidence. Treat stored memory like a document: dated, sourced and open to correction.

## Five levels of autonomy

The question that matters most in a plant is not "how smart is the agent?". It is "what may it do without a person?". I use a simple five-level ladder:

- **L0: no agent.** People do the task by hand.
- **L1: reads and explains.** The agent can query data and write an answer or summary. It changes nothing.
- **L2: drafts, a person approves.** The agent prepares an action, such as a work order, a changeover plan or an email, and a person approves it before anything happens.
- **L3: acts within tight limits, a person can veto.** The agent takes low-risk actions itself, within fixed limits, with a log and a way to reverse them. Reordering a consumable within an agreed budget is an example.
- **L4: acts alone, a person monitors.** The agent runs a task end to end and people review its work afterwards.

On a beverage plant floor, most agents should live at **L1 and L2** for a long time. Reading and drafting deliver most of the value at a fraction of the risk. L3 is for narrow, reversible, low-cost actions only. And one category sits off the ladder entirely: nothing an agent does should write to a PLC, a SCADA system or a process setpoint. Process control stays with engineered control systems and people. Post 7 covers these guardrails in detail.

## Human in the loop, done properly

"Human in the loop" is easy to say and easy to do badly. An approval step where a tired planner clicks "approve" on forty drafts at the end of a shift is not oversight. It is a rubber stamp.

A few habits make it real:

- Show the evidence with every draft: which tool calls, which data, which SOP section.
- Keep drafts few and specific. An agent that drafts one good work order is more useful than one that drafts ten mediocre ones.
- Track how often people change or reject the agent's drafts. A falling edit rate is good. A zero edit rate usually means nobody is reading.

## Where this breaks

**Agents can loop or wander.** A poorly scoped agent may call tools over and over or chase an irrelevant lead. Set limits on steps, time and cost, and make "I need a person" an acceptable answer.

**Tool results can carry instructions.** An agent reads text from logs, notes and documents. If that text says "ignore previous instructions", a careless setup may follow it. This is called prompt injection. Treat everything a tool returns as data, never as a command, and keep write tools behind approvals.

**The chain is only as good as the data.** An agent that reads a line stop log full of "other" fault codes will produce a confident summary of "other". Agents make good data faster to use. They do not make bad data better.

**Autonomy creeps.** Once an agent works well at L2, there is pressure to skip the approval. Decide the level on purpose, by the cost of a mistake, and write it down.

## The bottom line

An agent is a language model with tools and a loop. It plans, acts through a tool, observes the result and repeats, which lets it do the fetching and cross-checking that used to eat half an hour of a supervisor's morning. MCP is the standard way to connect it to plant systems, with each system's owner deciding which tools exist. Memory makes it useful across steps and sessions. Autonomy is a choice, and in a beverage plant the sensible default is L1 and L2: read, explain and draft, with a person approving and process control out of reach.

Next: [operational excellence basics for data people]({{ '/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}), because an agent is only useful if it is chasing the right losses. A worked example of MCP tools for a winery recall is in [Lot Genealogy as a Graph]({{ '/2026/wine-lot-genealogy-graph-recall-agent/' | relative_url }}). The full list is on the [series page]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Frequently asked questions

**What is the difference between a chatbot and an AI agent?**
A chatbot answers one message with one reply from what it already has. An agent is given a goal and a set of tools, then works in a loop: it plans a step, calls a tool such as a database query, looks at the result and decides the next step, until it has an answer or needs a person. The model is the same kind; the tools and the loop make it an agent.

**What is MCP in agentic AI?**
MCP, the Model Context Protocol, is an open standard for connecting language models to tools and data sources. Instead of writing a custom integration for every model and every system, you build an MCP server once for, say, your maintenance system, and any MCP-capable assistant can use its tools. It describes what each tool does, what inputs it takes and what it returns.

**How much autonomy should an AI agent have in a beverage plant?**
Match autonomy to the cost of a mistake. Reading data and drafting are low risk, so agents can do them freely. Anything that changes a record should be proposed by the agent and approved by a person. Anything that touches process control, such as a setpoint or a PLC, should stay out of an agent's reach entirely.
