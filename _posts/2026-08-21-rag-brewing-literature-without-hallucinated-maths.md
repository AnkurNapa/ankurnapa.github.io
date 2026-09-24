---
layout: post
title: "RAG Over the Brewing Literature Without Hallucinated Maths"
image: /assets/og/rag-brewing-literature-without-hallucinated-maths.png
description: "Part 1 of The Brewer's Agent. Retrieval-augmented generation is good at finding what the brewing literature says and bad at doing what it says. How to chunk formulas and tables, why brewing needs hybrid search, why every answer needs a citation, and why the arithmetic goes to a tool."
date: 2026-08-21 09:00:00 -0700
updated: 2026-08-21
tags: [brewing-science, brewers-agent, generative-ai, rag, data-engineering]
faq:
  - q: "What is RAG and why use it for brewing knowledge?"
    a: "Retrieval-augmented generation means the model looks up passages from your own documents before it answers, and answers from those passages. For brewing, that keeps answers tied to the textbooks, papers and lab methods you trust, instead of whatever the model half-remembers from the internet, and it lets every answer cite its source."
  - q: "Can a RAG system calculate ABV or IBU correctly?"
    a: "It can find the right formula, but it should not do the sums. Language models are unreliable at multi-step arithmetic, and brewing formulas have unit and temperature conventions that are easy to mix up. Retrieve the formula for the explanation and send the numbers to a tested calculation tool."
  - q: "How should brewing documents be chunked for retrieval?"
    a: "Keep formulas, their variable definitions and their units in one chunk, and keep tables whole with their headers and footnotes. Store metadata such as the temperature basis and units with each chunk. Splitting on a fixed number of characters routinely separates a formula from the line that says what its symbols mean."
---

**Short answer: RAG is very good at finding what the brewing literature says and quite bad at doing what it says. Point it at your textbooks, papers and lab methods, chunk them so a formula never gets separated from its units, use hybrid search because brewing is full of abbreviations that embeddings blur, and make every answer cite the passage it came from. Then take the arithmetic away from the model entirely. It retrieves the formula for the explanation. A tested tool computes the number.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A brewing question enters a pipeline. Hybrid retrieval combines keyword search and vector search over chunked textbooks, papers and lab methods, then a reranker picks the best passages. The language model writes the explanation with citations. Any numbers in the question are sent on a separate branch to a calculation tool, which returns the computed value with its method and units. A banner says retrieve the knowledge, compute the numbers.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">TWO PATHS FOR ONE QUESTION: WORDS FROM RETRIEVAL, NUMBERS FROM TOOLS</text>
<g font-family="sans-serif">
<rect x="30" y="110" width="160" height="70" rx="9" fill="#06483f"/>
<text x="110" y="140" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">brewer's question</text>
<text x="110" y="160" text-anchor="middle" font-size="10.5" fill="#cfe6df">"ABV at 13 &#176;P, 64.9% RDF?"</text>
<line x1="190" y1="130" x2="240" y2="85" stroke="#4db6a2" stroke-width="2"/>
<line x1="190" y1="160" x2="240" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="240" y="55" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="340" y="81" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">hybrid retrieval</text>
<text x="340" y="99" text-anchor="middle" font-size="10.5" fill="#4a6b64">keyword + vector, then rerank</text>
<line x1="440" y1="86" x2="480" y2="86" stroke="#4db6a2" stroke-width="2"/>
<rect x="480" y="55" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="580" y="81" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">LLM explains</text>
<text x="580" y="99" text-anchor="middle" font-size="10.5" fill="#4a6b64">from passages, with citations</text>
<rect x="240" y="185" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="340" y="211" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">calculation tool</text>
<text x="340" y="229" text-anchor="middle" font-size="10.5" fill="#4a6b64">tested code, base units</text>
<line x1="440" y1="216" x2="480" y2="216" stroke="#4db6a2" stroke-width="2"/>
<rect x="480" y="185" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="580" y="211" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">5.46% ABV</text>
<text x="580" y="229" text-anchor="middle" font-size="10.5" fill="#4a6b64">method and units returned</text>
<line x1="680" y1="86" x2="740" y2="140" stroke="#4db6a2" stroke-width="2"/>
<line x1="680" y1="216" x2="740" y2="165" stroke="#4db6a2" stroke-width="2"/>
<rect x="740" y="115" width="230" height="66" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="855" y="142" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">answer</text>
<text x="855" y="162" text-anchor="middle" font-size="10.5" fill="#4a6b64">explained, cited, computed</text>
<rect x="30" y="270" width="940" height="38" rx="10" fill="#06483f"/>
<text x="500" y="294" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">RETRIEVE THE KNOWLEDGE &#183; COMPUTE THE NUMBERS &#183; NEVER THE OTHER WAY ROUND</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The model and the calculator each get the job they are good at. The brewer gets one answer with a source and a method.</figcaption>
</figure>

Ask a general chatbot how to work out the alcohol in a beer from its original extract and real degree of fermentation. You will get a confident paragraph and a formula. Sometimes it is the right formula. Sometimes it is the homebrew shortcut that works on specific gravity, dressed up with Plato numbers it was never meant for. Either way, the number at the end has been worked out in the model's head, and that is where the trouble starts.

This is the first post in **The Brewer's Agent**, a series on building GenAI tools for brewing that a brewer can actually trust. It picks up where [The Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}) left off in the winery: the model is only as good as the data and the tools underneath it.

## What RAG actually does

Retrieval-augmented generation is a simple idea. Before the model answers, a search step pulls the most relevant passages from a collection you control. The model then answers from those passages rather than from memory.

For a brewery, that collection might be:

- a few textbooks and the chapters people actually use
- published papers on hop chemistry, mashing and fermentation
- your own lab methods and SOPs
- supplier specifications and certificates of analysis

The payoff is not that the model gets cleverer. It is that the answer comes from a document you chose, and the answer can tell you which one. A brewer can open the page and check. That habit, checking the source, is the whole safety system.

## Chunking: where brewing documents break

Documents are split into chunks before they are indexed, and most RAG failures in technical fields start right here.

The default approach splits text every thousand or so characters. Brewing literature is full of formulas followed by a line explaining the symbols, the units and the temperature basis. Split in the wrong place and one chunk holds the formula while the next holds "where OG is in degrees Plato at 20/20 degrees C". The model retrieves the first and guesses the second.

Rules that fix most of it:

1. **Keep a formula with its definitions.** Split on section boundaries, not character counts, and treat an equation plus the paragraph after it as one unit.
2. **Keep tables whole.** A hop utilisation table without its header row is a list of numbers. Store the whole table, headers, footnotes and all, as one chunk even if it is long.
3. **Put the conventions in metadata.** Store the units, the temperature basis and the source edition alongside each chunk. Plato at 20/20 degrees C and specific gravity at 60/60 degrees F are not interchangeable, and the model needs to see which one it is holding.
4. **Parent retrieval for long derivations.** Index small chunks for precise matching, but hand the model the whole section they came from.

## Hybrid search, because brewing speaks in acronyms

Vector search finds passages with similar meaning. That is great for "why does my lager taste of cooked sweetcorn" landing on DMS. It is less good for terms where one letter matters.

RDF and ADF are two different measures of attenuation, and on the same beer they can be more than ten points apart. To an embedding model they look almost identical: short, capitalised, about fermentation. A keyword search (BM25 or similar) treats them as the different words they are.

So run both and merge the results, then let a reranker put the most relevant passages first. Most vector databases and search services now support this out of the box. It is the single cheapest improvement you can make to a technical RAG system.

## Retrieval for knowledge, tools for arithmetic

Here is the rule this whole series rests on. **The model may explain a formula. It may not evaluate one.**

Take the question in the figure. A 13.0 degrees Plato wort fermented to a real degree of fermentation of 64.9%. What is the ABV?

Done properly, that goes through Balling's relationship between extract consumed and alcohol produced, gives a real extract of about 4.77% and an alcohol of about 4.27% by weight, then converts weight to volume using the beer's own density. The answer is 5.46% ABV. Every step has a constant with four decimal places and a unit convention attached.

A language model asked to do that in its head will often get close. Close is the problem. It will occasionally drop a step, use the wrong density or swap weight for volume, and it will present 4.3% with exactly the same confidence as 5.46%. Nothing in the prose tells you which answer you got.

The fix is architectural, not a better prompt. The retrieval step supplies the explanation: what RDF is, why weight and volume differ, where the constants come from. A calculation tool, ordinary tested code, supplies the number. The [next post]({{ '/2026/brewing-agent-calculation-tools-not-sums/' | relative_url }}) builds those tools. For this one, the point is that the RAG system should route the arithmetic out, and say so in the answer: "computed by the ABV tool from OG and RDF".

## Citations are the feature

Every answer should carry its sources: the document, the section and ideally the page. Make it a hard requirement in the system prompt and check it in testing. An answer with no citation should be treated as a failed answer, however good it sounds.

Two small things make citations far more useful:

- **Show the passage, not only the title.** A brewer glancing at the quoted paragraph will spot a wrong edition or a homebrew source faster than any automated check.
- **Say when nothing was found.** If retrieval returns nothing relevant, the right answer is "I do not have a source for that", not a fluent guess from general knowledge. Test that behaviour on purpose, because models are trained to be helpful and will fill the gap if you let them.

## Where this breaks

**Your corpus has opinions.** Textbooks disagree on hop utilisation, homebrew sources use shortcuts that commercial labs would not, and older editions carry superseded methods. RAG faithfully retrieves whichever passage matches best. Curate the collection, tag the source type, and prefer your own lab methods where they exist.

**Scanned PDFs lose the maths.** OCR turns subscripts, Greek letters and fractions into noise. A formula that reads "E = P/100" in the book may come out as "E - Pl100". Check the extracted text for your most-used formulas by eye before you trust the index.

**Copyright still applies.** Indexing a textbook for internal use is one thing. Letting the model quote long passages to people outside the company is another. Know what licence covers the documents you index.

**Citations can be fabricated too.** A model can produce a reference that looks right and was never retrieved. Build the citation from the retrieval metadata in code, not from the model's text.

## The bottom line

RAG turns a pile of brewing literature into something you can ask questions of, and the answers point back to the page. That is genuinely useful. What it does not do is make the model good at arithmetic, and brewing is mostly arithmetic with conventions attached. Chunk so formulas keep their units, search with keywords as well as meaning, insist on citations, and send every number to a tool. The model reads the book. The calculator does the sums.

For the wider picture of what AI is doing in breweries right now, see [What AI in Beer Actually Looks Like in 2026]({{ '/2026/what-ai-in-beer-actually-looks-like-2026/' | relative_url }}). The full list is on [The Brewer's Agent series page]({{ '/series/brewers-agent/' | relative_url }}).

## Frequently asked questions

**What is RAG and why use it for brewing knowledge?**
Retrieval-augmented generation means the model looks up passages from your own documents before it answers, and answers from those passages. For brewing, that keeps answers tied to the textbooks, papers and lab methods you trust, instead of whatever the model half-remembers from the internet, and it lets every answer cite its source.

**Can a RAG system calculate ABV or IBU correctly?**
It can find the right formula, but it should not do the sums. Language models are unreliable at multi-step arithmetic, and brewing formulas have unit and temperature conventions that are easy to mix up. Retrieve the formula for the explanation and send the numbers to a tested calculation tool.

**How should brewing documents be chunked for retrieval?**
Keep formulas, their variable definitions and their units in one chunk, and keep tables whole with their headers and footnotes. Store metadata such as the temperature basis and units with each chunk. Splitting on a fixed number of characters routinely separates a formula from the line that says what its symbols mean.
