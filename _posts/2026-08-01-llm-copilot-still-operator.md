---
layout: post
title: "An LLM Copilot for the Still Operator: RAG Over SOPs, Read-Only Tools, No Setpoints"
image: /assets/og/llm-copilot-still-operator.png
description: "Part 3 of The Still and the Model. What a GenAI copilot on the still house floor should and should not do: answer from controlled SOPs and run logs with citations, read live values through read-only tools, write the shift handover, and never touch a setpoint, an interlock or a cut."
date: 2026-08-01 09:00:00 -0700
updated: 2026-08-01
tags: [distilling-maturation, still-and-model, generative-ai, rag, ai-agents]
faq:
  - q: "What can an LLM copilot do for a distillery operator?"
    a: "It can answer procedure questions from the controlled SOPs with the paragraph cited, search past run logs for similar situations, read live process values through read-only tools, and draft the shift handover from the historian and the operator's notes. It saves time on finding and writing, which is a large part of a shift."
  - q: "Should an AI copilot be allowed to change still setpoints?"
    a: "No. The copilot should have no write tools at all. Setpoints, interlocks and cut decisions stay with the operator and the control system. The simplest safety design is the tool that does not exist: if the model cannot call set_setpoint, no prompt can make it."
  - q: "How do you stop a still-house copilot giving wrong procedure answers?"
    a: "Point retrieval only at the current controlled versions of SOPs, make the model quote and link the paragraph it used, refuse when no source is found, and test it against a set of real operator questions with checked answers before and after every change. The operator reads the source before acting on anything safety-related."
---

**Short answer: a still-house copilot is worth building if it does the reading and writing that eats a shift, and nothing else. Point it at the controlled SOPs and years of run logs, make it cite the paragraph it used, give it read-only tools for live values from the historian, and have it draft the handover at the end of the shift. Give it no write tools at all. Setpoints, interlocks and cuts stay with the operator and the control system. The safest tool on a still is the one the model was never given.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="An LLM copilot in the centre. On the left, its sources: controlled SOPs, run logs and shift notes through retrieval, and live historian values through read-only tools named get_value, get_trend and get_run_summary. On the right, its outputs: answers with the SOP paragraph cited, a draft shift handover, and a draft deviation note for a person to complete. At the bottom, a crossed-out tool named set_setpoint, with the message that setpoints, interlocks and cuts stay with the operator.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">A COPILOT THAT READS AND WRITES WORDS, NEVER SETPOINTS</text>
<g font-family="sans-serif">
<rect x="30" y="56" width="270" height="90" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="165" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">retrieval</text>
<text x="165" y="102" text-anchor="middle" font-size="10.5" fill="#4a6b64">controlled SOPs (current versions)</text>
<text x="165" y="120" text-anchor="middle" font-size="10.5" fill="#4a6b64">run logs &#183; shift notes</text>
<rect x="30" y="160" width="270" height="90" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="165" y="186" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">read-only tools</text>
<text x="165" y="206" text-anchor="middle" font-size="10.5" fill="#4a6b64">get_value &#183; get_trend</text>
<text x="165" y="224" text-anchor="middle" font-size="10.5" fill="#4a6b64">get_run_summary</text>
<line x1="300" y1="101" x2="400" y2="140" stroke="#4db6a2" stroke-width="2"/>
<line x1="300" y1="205" x2="400" y2="170" stroke="#4db6a2" stroke-width="2"/>
<rect x="400" y="110" width="200" height="90" rx="12" fill="#06483f"/>
<text x="500" y="150" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">LLM copilot</text>
<text x="500" y="172" text-anchor="middle" font-size="10.5" fill="#cfe6df">answers, cites, drafts</text>
<line x1="600" y1="140" x2="700" y2="85" stroke="#4db6a2" stroke-width="2"/>
<line x1="600" y1="155" x2="700" y2="155" stroke="#4db6a2" stroke-width="2"/>
<line x1="600" y1="170" x2="700" y2="225" stroke="#4db6a2" stroke-width="2"/>
<rect x="700" y="60" width="270" height="50" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="90" text-anchor="middle" font-size="11.5" fill="#06483f">answer + SOP paragraph cited</text>
<rect x="700" y="130" width="270" height="50" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="160" text-anchor="middle" font-size="11.5" fill="#06483f">draft shift handover</text>
<rect x="700" y="200" width="270" height="50" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="230" text-anchor="middle" font-size="11.5" fill="#06483f">draft deviation note</text>
<rect x="30" y="272" width="940" height="44" rx="10" fill="#06483f"/>
<text x="180" y="299" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ff4081" text-decoration="line-through">set_setpoint()</text>
<text x="600" y="299" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">SETPOINTS, INTERLOCKS AND CUTS STAY WITH THE OPERATOR</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Everything on the left is read. Everything on the right is a draft. The missing tool at the bottom is the safety design.</figcaption>
</figure>

It is six in the morning at shift change. The night operator has a page of notes, a run that went a bit slow around two o'clock, and a steam trap that was hissing. The day operator gets five minutes of handover, half of it spent finding which run number was the slow one. Later that morning a trainee asks how the feints receiver changeover is done after a CIP, and the answer lives in an SOP nobody can find on the shared drive.

None of that is a control problem. It is a reading and writing problem, and reading and writing is what large language models are genuinely good at. This post is about a copilot for that job, and about the one thing it must never be able to do.

## What the copilot is for

Four jobs, in rough order of value:

**1. Procedure questions, answered from the source.** Retrieval-augmented generation (RAG) over the controlled SOPs: the operator asks in plain words, the copilot finds the relevant paragraph, answers and quotes it with the document number and version. If it cannot find a source, it says so rather than improvising.

**2. "Has this happened before?"** Years of run logs and shift notes are a record of every odd run and what fixed it. Semantic search over them turns "slow run after the boiler trip, strength dropping early" into a list of similar past runs and what the operator wrote at the time. This is often the most useful thing on the list, and it is buried text that nobody reads today.

**3. The shift handover.** At the end of the shift the copilot pulls the runs from the historian, the band flags from the [soft sensor post]({{ '/2026/soft-sensors-proactive-bands-spirit-safe/' | relative_url }}), the operator's notes and any open work orders, and drafts a one-page handover. The operator edits it and signs it. The day shift gets a consistent summary instead of whatever the night shift had energy to write at 5:45.

**4. Drafting the paperwork.** Deviation notes, near-miss reports and maintenance requests start from a draft that already has the run number, the timestamps and the values attached.

## The tools: read-only by design

For the copilot to talk about the live plant it needs data, and the clean way to provide it in 2026 is a small set of tools (usually exposed over MCP) that sit on top of the historian:

```text
get_value(tag)                      -> current value, unit, timestamp, quality
get_trend(tag, from, to)            -> time series, downsampled
get_run_summary(still, run_id)      -> charge, cuts, fractions, alcohol balance
search_run_logs(query, still)       -> matching notes with run ids
```

Every tool reads. None of them writes. There is no `set_setpoint`, no `acknowledge_alarm`, no `open_valve`. This is not a guideline in the prompt, which a clever enough prompt can talk its way round. It is the absence of the capability. A model cannot call a tool that does not exist.

The historian connection itself should be read-only at the network and account level too, for the same reason. The control system has its own safety layer, its interlocks and its engineers, and a language model has no business anywhere near it.

## Making the answers trustworthy

A copilot that sounds sure and is wrong about a procedure is worse than no copilot. A few rules do most of the work:

1. **Only current, controlled documents in the index.** When an SOP is revised, the old version comes out of retrieval on the same day. Superseded procedures in the index are the most common way these systems give confidently wrong answers.
2. **Cite or refuse.** Every procedural answer quotes the paragraph and links the document. No source, no answer.
3. **Numbers from tools, never from the model.** If the operator asks what the condenser outlet temperature is, the copilot calls `get_value` and reports what came back, with its timestamp. It does not estimate.
4. **A real eval set.** Collect fifty questions operators actually asked, with answers checked by the shift leader, and run them every time the model, the prompt or the document index changes. Score it. It is the only honest answer to "is it good enough?".

## Where this breaks

**Safety-critical questions need the source, not the summary.** For anything involving isolation, confined space, hot work or ethanol vapour, the copilot's job is to open the right SOP, not to paraphrase it. Make that a hard rule in the design and in training.

**Run logs are messy and sometimes wrong.** Semantic search will happily find a note from 2021 that says "fixed by increasing steam", and that may have been the wrong fix. Past notes are leads, not instructions.

**Handover drafts can smooth over problems.** A tidy summary can make an uneasy night sound routine. The operator who lived the shift must edit and sign it, and the draft should list band flags and open issues explicitly rather than summarising them away.

**People will trust it more over time.** The better it gets, the less anyone checks. That is the argument for keeping the eval set running forever, not just at launch.

## The bottom line

The still house has a reading and writing problem hiding inside its operating problem: procedures nobody can find, run logs nobody reads and handovers written half asleep. A language model is good at exactly that. Give it the controlled documents, the logs and read-only tools, make it cite, test it with real questions, and it will save the shift real time. Give it nothing that writes. The operator runs the still. The copilot runs the paperwork.

For the wider view of the Anthropic tools in a distillery, see [Claude AI and Claude Code for Distilleries]({{ '/2026/claude-ai-claude-code-for-distilleries/' | relative_url }}). The same propose-never-write rule appears in the wine series, in [event-sourcing the cellar]({{ '/2026/event-sourced-cellar-records-winery/' | relative_url }}). Next in this series: [cask inventory as data engineering]({{ '/2026/cask-inventory-data-engineering-scd2/' | relative_url }}). The full list is on [The Still and the Model series page]({{ '/series/still-and-model/' | relative_url }}).

## Frequently asked questions

**What can an LLM copilot do for a distillery operator?**
It can answer procedure questions from the controlled SOPs with the paragraph cited, search past run logs for similar situations, read live process values through read-only tools, and draft the shift handover from the historian and the operator's notes. It saves time on finding and writing, which is a large part of a shift.

**Should an AI copilot be allowed to change still setpoints?**
No. The copilot should have no write tools at all. Setpoints, interlocks and cut decisions stay with the operator and the control system. The simplest safety design is the tool that does not exist: if the model cannot call set_setpoint, no prompt can make it.

**How do you stop a still-house copilot giving wrong procedure answers?**
Point retrieval only at the current controlled versions of SOPs, make the model quote and link the paragraph it used, refuse when no source is found, and test it against a set of real operator questions with checked answers before and after every change. The operator reads the source before acting on anything safety-related.
