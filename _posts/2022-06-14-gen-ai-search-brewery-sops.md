---
layout: post
title: "Knowledge Search Over Brewery SOPs With Gen AI"
image: /assets/og/gen-ai-search-brewery-sops.png
description: "How retrieval-augmented LLMs let brewery staff ask plain-language questions over SOPs, batch records, and manuals with cited answers — and what to watch."
date: 2022-06-14
updated: 2022-06-14
tags: [brewing-science, generative-ai, knowledge]
faq:
  - q: "What is retrieval-augmented generation, in plain terms?"
    a: "It is a setup where the language model first retrieves the most relevant passages from your own documents — SOPs, batch records, manuals — and then answers using only those passages, with citations back to the source. The retrieval step grounds the model in your reality instead of its general training."
  - q: "Can it still hallucinate?"
    a: "Yes, though grounding reduces it sharply. If the answer is not in your documents, or the retrieval pulls the wrong passage, the model can still produce something confident and wrong. That is why every answer must cite its source so a person can verify it before acting."
  - q: "What governance does this need?"
    a: "Source control and access permissions, primarily. You need one authoritative version of each document so the model is not quoting a superseded SOP, and you need permission rules so staff only get answers from documents they are cleared to see. Without that, the tool becomes a fast way to spread outdated or restricted information."
---

**Short answer: a retrieval-augmented LLM lets staff ask plain-language questions over your SOPs, batch records, and manuals and get cited answers — the strongest genuine gen-AI use a brewery has.** The knowledge already exists; it is just scattered across PDFs, shared drives, and a few people's memories. This is the use case that fixes that.

## The scattered-knowledge problem
Ask a new cellar hand "what's the CIP spec for FV3?" and the honest answer is often a hunt: the right SOP is in one folder, an exception note is in a batch record, and the definitive word lives with whoever wrote the procedure. Multiply that across hundreds of documents and a dozen procedures and you have a real drag on every shift. Knowledge that exists but cannot be found quickly may as well not exist.

Retrieval-augmented generation tackles this directly. Staff ask a plain-language question; the system retrieves the most relevant passages from your own document set; the LLM composes an answer from those passages and cites them. The citation is the crucial part — it turns the model from an oracle you have to trust into an assistant you can check. "The CIP spec for FV3 is X, per SOP-CIP-04, section 3" is something a person can verify in seconds.

## Measure first: ground it in your real documents
Unlike the other applications in this track, the "data" here is your written knowledge, and the same discipline applies: get the source material in order before you switch anything on. That means knowing which documents are authoritative, removing or clearly archiving superseded versions, and structuring access so the retrieval has clean material to draw from. The broader argument for sorting your data foundation first applies just as much here — see [building a brewery data foundation for AI]({{ '/2024/building-brewery-data-foundation-ai/' | relative_url }}).

A retrieval system is only as trustworthy as the corpus behind it. Point it at a folder of duplicated, half-revised PDFs and it will faithfully cite the wrong one. The unglamorous prep — deduplicating, versioning, tidying — is what makes the clever part work.

## Where it breaks
Be clear-eyed about three risks. First, hallucination. Grounding reduces it sharply but never to zero; if the answer is not in your documents, or retrieval grabs the wrong passage, the model can still sound confident and be wrong. Citations are the mitigation, which is why an answer without a verifiable source should not be trusted.

Second, source control. If two versions of an SOP exist, the model may quote the obsolete one, and a fast, fluent answer from a superseded procedure is more dangerous than no answer at all. Third, access permissions. Batch records and some procedures are sensitive; the system must respect who is allowed to see what, or it becomes a frictionless leak. None of these are reasons not to do it — they are reasons to govern it properly.

## A practical gen-AI angle
This post *is* the gen-AI angle, so the concrete framing is worth stating plainly: deploy it as an internal, governed assistant, not a public chatbot. Restrict it to vetted documents, require citations on every answer, enforce access rules, and keep a single authoritative version of each SOP. Done that way, a question that used to take ten minutes of folder-diving takes ten seconds, and the answer points straight at the procedure it came from.

## The bottom line
Knowledge search over SOPs and batch records is the most compelling gen-AI use in a brewery because the value is immediate and the knowledge already exists — it just needs finding. The price of admission is governance: authoritative sources, version control, access permissions, and mandatory citations to keep hallucination in check. Tidy the corpus first, ground every answer, and you turn scattered documents into something staff can actually query.

*Part of the [Brewing Science & AI]({{ '/tracks/brewing-science-ai/' | relative_url }}) track.*

## Frequently asked questions

**What is retrieval-augmented generation, in plain terms?**
It is a setup where the language model first retrieves the most relevant passages from your own documents — SOPs, batch records, manuals — and then answers using only those passages, with citations back to the source. The retrieval step grounds the model in your reality instead of its general training.

**Can it still hallucinate?**
Yes, though grounding reduces it sharply. If the answer is not in your documents, or the retrieval pulls the wrong passage, the model can still produce something confident and wrong. That is why every answer must cite its source so a person can verify it before acting.

**What governance does this need?**
Source control and access permissions, primarily. You need one authoritative version of each document so the model is not quoting a superseded SOP, and you need permission rules so staff only get answers from documents they are cleared to see. Without that, the tool becomes a fast way to spread outdated or restricted information.
