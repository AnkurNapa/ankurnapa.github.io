---
layout: post
title: "Which Beer Should We Make Next? How I Let the Data Decide"
image: /assets/og/npd-which-beer-to-make-data.png
description: "Developing beers for AB InBev, SABMiller and United Breweries meant crunching consumer and market data to choose what to brew — here's how AI and analytics shaped the front end of new product development."
date: 2026-05-27
updated: 2026-05-27
tags: [beer-npd, new-product-development, consumer-insight, data-science]
faq:
  - q: "Can AI decide which new beer to develop?"
    a: "Not decide — narrow. AI and analytics are excellent at ranking a long list of ideas against consumer, market and sales data so you develop the few with real demand behind them. The final call still belongs to people who know the brand and the market."
  - q: "What data do you need before developing a new beer?"
    a: "Retail scan and depletion data, consumer panel and survey responses, category and competitor trends, and your own historical launch performance. The quality of the front-end decision is capped by the quality of this data, not the cleverness of the model."
  - q: "Why do most new beers fail despite market research?"
    a: "Because surveys capture what people say, not what they buy, and because a confident model trained on thin or biased data will still rank a dud highly. The data tells you where demand is plausible; it cannot guarantee a launch."
---

**Short answer: in the years I spent developing beers for AB InBev, SABMiller and United Breweries, the hardest question was never how to brew — it was which beer to brew at all. AI and analytics didn't answer that for me, but they turned a wall of consumer surveys, retail scan data and sales history into a ranked shortlist I could actually act on. The data narrows the field; people still make the call.** Here's how the front end of new product development really works.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="An NPD funnel: many raw data sources feed a screening model that narrows dozens of ideas down to the few worth brewing."><rect x="0" y="0" width="1000" height="320" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">THE NPD FRONT END</text><g font-family="sans-serif"><rect x="20" y="60" width="200" height="44" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="120" y="87" text-anchor="middle" font-size="13" fill="#06483f">Retail scan &amp; depletions</text><rect x="20" y="116" width="200" height="44" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="120" y="143" text-anchor="middle" font-size="13" fill="#06483f">Consumer panels</text><rect x="20" y="172" width="200" height="44" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="120" y="199" text-anchor="middle" font-size="13" fill="#06483f">Category &amp; competitor trends</text><rect x="20" y="228" width="200" height="44" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="120" y="255" text-anchor="middle" font-size="13" fill="#06483f">Past launch performance</text></g><polygon points="300,70 560,120 560,200 300,250" fill="#06483f" opacity="0.12" stroke="#06483f" stroke-width="1.5"/><text x="430" y="155" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#06483f">screen &amp; score</text><text x="430" y="176" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">rank ideas</text><g font-family="sans-serif"><rect x="640" y="100" width="160" height="50" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="720" y="130" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">3–5 concepts</text><rect x="640" y="170" width="160" height="50" rx="6" fill="#ffffff" stroke="#4a6b64" stroke-width="1.2" stroke-dasharray="4 3"/><text x="720" y="200" text-anchor="middle" font-size="12" fill="#4a6b64">dozens parked</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="220" y1="138" x2="296" y2="150"/><polygon points="296,145 303,150 296,155" stroke="none"/></g><g fill="#06483f" stroke="#06483f" stroke-width="2"><line x1="560" y1="135" x2="636" y2="125"/><polygon points="636,120 643,125 636,130" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">The front end of NPD: many noisy data sources, one screening model, a short list worth brewing.</figcaption>
</figure>

## The room was full of opinions, not evidence

Every new-product meeting I sat in started the same way: a dozen ideas on a whiteboard, each championed by someone senior who was sure theirs was the winner. A stronger wheat beer. A low-bitterness lager for new drinkers. A festive seasonal. Everyone had a hunch; nobody had a way to compare them.

That is the real problem at the front end of [new product development]({{ '/2025/forecasting-new-products-na-beer/' | relative_url }}). You cannot brew twelve beers to full scale to find out which one sells — each pilot costs weeks and money. You have to choose before you brew, and for years that choice was made on seniority and gut feel.

## What I actually crunched

The data existed; it was just scattered and messy. My job became pulling it into one place and making it comparable. Three streams mattered most:

- **Retail scan and depletion data** — what was actually selling, by style, pack and region, and which segments were growing quarter on quarter. This is the closest thing to truth, because it records what people *bought*, not what they *said*.
- **Consumer research** — panels, surveys, and taste-test scores. Useful, but I learned to weight it carefully: stated preference and shopping behaviour are different animals.
- **Our own launch history** — every beer we had released, what we forecast, and what it did. This was the most honest teacher, because it showed where our optimism had been wrong before.

The data-science part was unglamorous and decisive: cleaning inconsistent SKU names, aligning regions, and shaping it all into features I could score. Measure first, model second — the model is only ever as good as the table you feed it.

## From a wall of numbers to a ranked shortlist

Once the data was clean, the analytics were almost simple. I scored each idea against demand signals: was its segment growing, was there white space competitors hadn't filled, did similar past launches succeed? A clustering model on consumer data helped me [segment drinkers]({{ '/2025/white-space-analytics-na-beer/' | relative_url }}) into groups that a single average had been hiding — and one of those groups was clearly under-served.

This is where generative AI now changes the rhythm of that work. Today I'd point a language model at the messy free-text in survey responses and competitor reviews and have it summarise the recurring themes in minutes — work that used to take me days of reading. I treat its summary as a lead to verify, never as a finding, but it turns reading into triage.

The output was never "make this beer." It was a ranked shortlist of three to five concepts with the evidence attached. That is exactly the right altitude for a model: narrow the field, then hand it to people.

## Where it breaks

I have to be honest about the failures, because the front end is where over-confidence is most expensive.

The data predicts the routine well and the rare well almost never. A model trained on existing styles is blind to a genuinely new category — it had no way to see the non-alcoholic wave coming, because there was no history of it to learn from. Surveys flattered ideas that flopped at the shelf. And thin data is dangerous: feed a flexible model a handful of past launches and it will rank a dud highly with total confidence, the same trap I hit in my [first demand-forecasting project]({{ '/2026/my-first-ai-project-beer-demand-forecasting/' | relative_url }}). The data tells you where demand is *plausible*. It cannot promise a hit.

## The bottom line

The front end of NPD is a filtering problem, and that is what AI and analytics are genuinely good at: taking a noisy, contradictory pile of consumer and market data and turning it into a defensible shortlist. It replaced "the loudest person in the room" with "the evidence on the table" — and that alone made the beers I went on to develop better bets. But the data narrows; it does not decide. The judgement that picks the winner from the shortlist still belongs to people who know the brand and the drinker.

*Beer NPD with Data — Part 1 of 3. [See the full series]({{ '/series/beer-npd/' | relative_url }}) · [Next: crunching recipe and sensory data →]({{ '/2026/npd-recipe-sensory-data-development/' | relative_url }})*

## Frequently asked questions

**Can AI decide which new beer to develop?**
Not decide — narrow. AI and analytics are excellent at ranking a long list of ideas against consumer, market and sales data so you develop the few with real demand behind them. The final call still belongs to people who know the brand and the market.

**What data do you need before developing a new beer?**
Retail scan and depletion data, consumer panel and survey responses, category and competitor trends, and your own historical launch performance. The quality of the front-end decision is capped by the quality of this data, not the cleverness of the model.

**Why do most new beers fail despite market research?**
Because surveys capture what people say, not what they buy, and because a confident model trained on thin or biased data will still rank a dud highly. The data tells you where demand is plausible; it cannot guarantee a launch.
