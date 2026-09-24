---
layout: post
title: "What GenAI and LLMs Actually Are: Tokens, Context, Hallucination and RAG, Explained Through a CIP Log"
image: /assets/og/what-is-genai-llm-tokens-rag-cip-log.png
description: "Part 2 of AI for Operational Excellence in Beverage Plants. How a large language model really works, from tokens and the context window to next-token prediction, why it hallucinates, when to use retrieval (RAG) versus fine-tuning, and what multimodal models add, all worked through one CIP log and one SOP."
date: 2026-09-17 09:00:00 -0700
updated: 2026-09-17
tags: [brewing-science, ai-opex, ai-basics, generative-ai, cip]
faq:
  - q: "What is a large language model in simple terms?"
    a: "A large language model is a neural network trained on a huge amount of text to predict the next piece of text, one token at a time. Because it has seen so much language, it can write, summarise, translate and answer questions. It does not look facts up unless you give it a way to, and it has no built-in sense of whether what it writes is true."
  - q: "Why do LLMs hallucinate?"
    a: "Because they are built to produce the most plausible next words, not the correct ones. When the answer is not in the text they were given, they fill the gap with something that sounds right. Ask about a CIP caustic concentration without supplying your SOP and you will get a typical industry value, stated with confidence, that may not be yours."
  - q: "Should a plant use RAG or fine-tuning?"
    a: "For facts that live in documents, such as SOPs, specifications and maintenance manuals, use retrieval (RAG): the system finds the relevant passage and hands it to the model with the question, so answers cite your own documents and update when the documents do. Fine-tuning changes the model's style or teaches it a task format. It is a poor way to store facts that change."
---

**Short answer: a large language model is a very good predictor of the next word. It reads text as tokens, holds a limited amount of it in a context window, and writes one token at a time, choosing what is most plausible. That is why it is fluent and also why it hallucinates: plausible is not the same as true. Ask it whether last night's CIP on fermenter 7 met spec and, without your SOP, it will compare against a typical industry value and sound certain. Give it the SOP clause and the log lines through retrieval (RAG) and it can answer against your own standard, with a citation. That one design choice is most of what matters in a plant.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Two answers to the question: did the CIP on fermenter 7 meet spec? On the top path, the question goes straight to the language model, which answers from general training that 1.8 percent caustic at 78 degrees is within typical ranges, so yes. On the bottom path, a retrieval step first pulls the plant SOP clause requiring 2.0 percent caustic at 80 degrees for 20 minutes and the matching log lines, and the model answers no, below the SOP on concentration, temperature and time, citing SOP section 4.2.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">"DID LAST NIGHT'S CIP ON FV-7 MEET SPEC?" (ILLUSTRATIVE)</text>
<g font-family="sans-serif">
<text x="40" y="62" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">MODEL ALONE</text>
<rect x="40" y="74" width="200" height="60" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="140" y="100" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">question</text>
<text x="140" y="118" text-anchor="middle" font-size="10.5" fill="#4a6b64">+ pasted log line</text>
<line x1="240" y1="104" x2="320" y2="104" stroke="#4db6a2" stroke-width="2"/>
<rect x="320" y="74" width="200" height="60" rx="9" fill="#06483f"/>
<text x="420" y="100" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">LLM</text>
<text x="420" y="118" text-anchor="middle" font-size="10.5" fill="#cfe6df">general training only</text>
<line x1="520" y1="104" x2="600" y2="104" stroke="#4db6a2" stroke-width="2"/>
<rect x="600" y="74" width="360" height="60" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="780" y="100" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">"Yes, 1.8% at 78 C is within typical ranges."</text>
<text x="780" y="118" text-anchor="middle" font-size="10.5" fill="#4a6b64">plausible, confident, not your standard</text>
<text x="40" y="178" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">WITH RETRIEVAL (RAG)</text>
<rect x="40" y="190" width="200" height="72" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="140" y="216" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">retriever</text>
<text x="140" y="234" text-anchor="middle" font-size="10.5" fill="#4a6b64">SOP 4.2 + FV-7 log lines</text>
<text x="140" y="250" text-anchor="middle" font-size="10.5" fill="#4a6b64">2.0% NaOH, 80 C, 20 min</text>
<line x1="240" y1="226" x2="320" y2="226" stroke="#4db6a2" stroke-width="2"/>
<rect x="320" y="196" width="200" height="60" rx="9" fill="#06483f"/>
<text x="420" y="222" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">LLM</text>
<text x="420" y="240" text-anchor="middle" font-size="10.5" fill="#cfe6df">answers from supplied text</text>
<line x1="520" y1="226" x2="600" y2="226" stroke="#4db6a2" stroke-width="2"/>
<rect x="600" y="196" width="360" height="60" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="780" y="222" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2e9e7c">"No. Below SOP 4.2 on all three limits."</text>
<text x="780" y="240" text-anchor="middle" font-size="10.5" fill="#4a6b64">cites the clause and the log lines</text>
<rect x="40" y="284" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="309" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">SAME MODEL &#183; THE DIFFERENCE IS WHAT YOU PUT IN FRONT OF IT</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative values. The model without the SOP is not lying. It is guessing well, which is worse.</figcaption>
</figure>

Here is a line from an imaginary CIP log on a fermenter, the kind every brewery, winery and distillery produces by the thousand:

```
02:14 | FV-07 | CAUSTIC STEP START | NaOH 1.8% | SUPPLY 78.0 C
02:31 | FV-07 | CAUSTIC STEP END | DURATION 17 MIN
```

Paste that into a chatbot and ask whether the clean met spec. You will almost certainly get a confident "yes": caustic in the 1 to 2 percent range at around 75 to 85 degrees C is typical for a CIP, and 17 minutes sounds fine. Now suppose your SOP says 2.0 percent at 80 degrees for at least 20 minutes. The clean failed on all three counts, and the chatbot just told you it passed.

The [first post in this series]({{ '/2026/what-is-ai-ladder-rules-to-agi-beverage-plant/' | relative_url }}) put generative AI on the ladder. This one opens it up, because once you see how a language model works, that wrong answer stops being mysterious.

## Tokens: how the model reads

A language model does not read letters or whole words. It reads **tokens**, chunks of text that are often a word, part of a word or a symbol. "Caustic" might be one token. "NaOH" might be two or three. As a rough rule for English, a thousand tokens is about 750 words.

Tokens matter for two practical reasons. Costs and limits are counted in tokens, and numbers are split into tokens in odd ways. "78.0" may become several pieces. That is one reason language models are unreliable at arithmetic: they are not working with the number, they are working with fragments of its text.

## The context window: what the model can see

The **context window** is everything the model can see at once: your question, any documents you paste in, the conversation so far and its own answer. In 2026, leading models accept hundreds of thousands of tokens and some go past a million. That sounds like enough to paste in every SOP in the plant.

It is not quite that simple. Models pay uneven attention across a very long context, and details in the middle of a long document are easier to miss. And the context is temporary. When the conversation ends, the model remembers nothing. It has not learned your SOP. It read it once.

## Next-token prediction: how the model writes

At its core, a large language model does one thing: given the tokens so far, it predicts which token is most likely to come next. Then it adds that token and does it again. A whole answer is hundreds of those predictions in a row.

It learned to make those predictions by training on an enormous amount of text. That is where its general knowledge comes from. It has read thousands of documents about CIP, so it knows the typical caustic range. It has never read your SOP, so it cannot know your standard unless you show it.

## Hallucination: why the confident wrong answer happens

Put those pieces together and hallucination becomes obvious. The model is built to produce the most plausible continuation. When the true answer is in front of it, plausible and true usually line up. When it is not, the model still produces something plausible, because that is the only thing it knows how to do. There is no internal alarm that says "I do not have this information".

That is why the CIP answer came out as "yes". The most plausible text, given what the model had seen in training, was that 1.8 percent at 78 degrees is a normal clean. It did not check your standard because it had no standard to check.

Hallucination can be reduced, never removed. The main lever is not a better model. It is giving the model the right text.

## RAG: giving the model the right text

**Retrieval-augmented generation**, or RAG, is the standard fix. Before the model answers, a retrieval step searches your own documents (SOPs, specifications, maintenance manuals, past incident reports) and puts the most relevant passages into the context along with the question. The model is instructed to answer from those passages and to cite them.

Asked again with RAG, the system retrieves SOP section 4.2 and the FV-7 log lines. The model now answers: the caustic step was below the SOP minimum on strength, temperature and duration, see section 4.2. Same model, different inputs, different answer.

Two refinements make it trustworthy in a plant:

- **Cite everything.** Every answer names the document and section it came from, so an operator can open the SOP and check.
- **Let code do the comparison.** A model can read "2.0 percent minimum" from the SOP. Whether 1.8 is below 2.0 is a job for a line of code, not a language model. The best systems extract the limits and the readings, and let ordinary software compare them.

I wrote an earlier post on [searching brewery SOPs with GenAI]({{ '/2022/gen-ai-search-brewery-sops/' | relative_url }}). The idea has not changed. The models have just become good enough that the retrieval quality is now the weak link.

## Fine-tuning: a different tool

**Fine-tuning** means training an existing model a bit further on your own examples. People often assume it is how you teach a model your SOPs. It is usually the wrong tool for that.

Fine-tuning is good at changing how a model behaves: the format of its answers, the tone of a handover, how it classifies a type of line stop. It is poor at storing facts that change, because the facts are baked into the model's weights with no citation and no easy update. When the SOP is revised, a RAG system reads the new version tomorrow. A fine-tuned model keeps quoting the old one until you retrain it.

A useful rule: RAG for knowledge, fine-tuning for behaviour, and most plants never need the second.

## Multimodal: when the input is not text

Many current models are **multimodal**: they accept images, and some accept audio, as well as text. On a plant floor, that opens some useful doors. An operator photographs a gauge, a fault screen on an HMI or a handwritten batch sheet, and the model reads it. A maintenance technician photographs a nameplate and gets the right manual section.

The same rules apply. A model reading a photo of a gauge can misread it, and it will report its misreading with the same confidence. Use it to capture and draft, then confirm the numbers.

## Where this breaks

**Retrieval can fetch the wrong passage.** If the SOP for the bright beer tanks and the SOP for the fermenters are nearly identical, the retriever may pull the wrong one. The citation is what lets a person catch it.

**Documents are often out of date.** RAG makes the model exactly as current as your document library. An unrevised SOP produces confidently outdated answers.

**Numbers remain risky.** Even with the right text, a model may misread a table or round a value. Where a decision rests on a number, the number should come from a system of record or a calculation, not from the model's prose.

**The model sounds the same when it is wrong.** There is no change in tone between a correct and an invented answer. Training people to check the citation is as important as building the system.

## The bottom line

A language model predicts plausible text one token at a time. It knows what is typical and nothing about your plant unless you show it. That makes it fluent, useful and prone to confident mistakes. RAG closes most of the gap by putting your own SOPs and logs in front of the model and making it cite them. Fine-tuning changes behaviour, not knowledge. And when the answer is a number that matters, let code check it.

Next: [what agentic AI is]({{ '/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}), when a model stops answering questions and starts using tools. For the distillery take on these basics, see [What Is Generative AI? The Difference That Matters for Distillers]({{ '/2026/what-is-generative-ai-distillers/' | relative_url }}). How the same idea underpins a winery's data assistant is in [the Cellar Ledger series]({{ '/series/cellar-ledger/' | relative_url }}).

## Frequently asked questions

**What is a large language model in simple terms?**
A large language model is a neural network trained on a huge amount of text to predict the next piece of text, one token at a time. Because it has seen so much language, it can write, summarise, translate and answer questions. It does not look facts up unless you give it a way to, and it has no built-in sense of whether what it writes is true.

**Why do LLMs hallucinate?**
Because they are built to produce the most plausible next words, not the correct ones. When the answer is not in the text they were given, they fill the gap with something that sounds right. Ask about a CIP caustic concentration without supplying your SOP and you will get a typical industry value, stated with confidence, that may not be yours.

**Should a plant use RAG or fine-tuning?**
For facts that live in documents, such as SOPs, specifications and maintenance manuals, use retrieval (RAG): the system finds the relevant passage and hands it to the model with the question, so answers cite your own documents and update when the documents do. Fine-tuning changes the model's style or teaches it a task format. It is a poor way to store facts that change.
