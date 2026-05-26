---
layout: post
title: "Marketing Mix Modeling: What Really Drives Beer Volume"
image: /assets/og/marketing-mix-modeling-beer.png
description: "Marketing mix modeling for beer brands — a framework for understanding which spend drives volume and which is just noise."
date: 2025-03-20
updated: 2025-03-20
tags: [marketing, marketing-analytics, mmm]
faq:
  - q: "What is marketing mix modeling and why does it matter for beer?"
    a: "Marketing mix modeling (MMM) is a statistical technique that decomposes sales volume into contributions from each marketing and trade lever — media spend, promotions, distribution changes, pricing, and external factors like weather or seasonality. For beer, where volume swings dramatically by season and occasion, understanding the true contribution of each lever is essential to avoid misattributing summer gains to a media campaign that merely ran at the same time."
  - q: "How much data does a brewery need to run a marketing mix model?"
    a: "A reliable MMM typically requires at least two to three years of weekly sales data alongside corresponding spend, pricing, and distribution records. Smaller independent breweries with limited historical data can run simpler regression-based versions, but the confidence intervals widen significantly below 18 months of data. Starting data collection now — even imperfectly — is better than waiting for the ideal dataset."
  - q: "What is the biggest mistake breweries make when interpreting MMM results?"
    a: "The most common error is treating the model's historical coefficients as a forward-looking planning tool without accounting for diminishing returns. A TV or digital channel that showed strong returns at a particular spend level will not necessarily deliver the same return at double the investment. Any MMM output should be paired with a response-curve analysis before budget decisions are made."
---

**Short answer:** For most beer brands, the top three volume drivers are distribution gains, price promotion depth, and seasonal baseline — not media. Marketing mix modeling makes this visible so that budget can flow to what actually moves product, rather than what feels strategic in a planning deck.

---

Every beer brand has a theory about what drives volume. Sales teams credit their relationship work. Brand teams credit the latest campaign. Trade marketing credits the display programme. Marketing mix modeling replaces these competing narratives with a single decomposed view of actual contribution. The discomfort it produces is usually proportional to its value.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="The operating loop this post describes"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">THE OPERATING LOOP</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Marketing Mix Modeling: What Really Drives Beer Volume</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Measure</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">data in</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analyse</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">find the signal</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Decide</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">choose</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Act</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">change the floor</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">repeat</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">The operating loop this post describes: measure, analyse, decide, act — then repeat.</figcaption>
</figure>

## What MMM Actually Measures

At its core, a marketing mix model is a multivariate regression that isolates the incremental contribution of each input variable to a dependent variable — typically volume sold or revenue. For a beer brand the input variables typically include:

- **Media spend by channel** (broadcast, digital, out-of-home, audio)
- **Trade promotions** (price reduction depth, feature frequency, display spend)
- **Distribution** (weighted or numeric distribution changes)
- **Pricing** (base price and shelf price)
- **External variables** (temperature, sporting events, holidays, competitive activity)
- **Baseline** (the volume the brand would sell with no marketing at all)

The model separates these contributions statistically. The baseline figure — often 60–75% of total volume for established brands — tends to surprise executives who believe their brand is more marketing-driven than it actually is.

## The Beer-Specific Complications

Beer presents three modeling challenges that generic MMM frameworks underweight.

**Seasonality is extreme.** A warm-weather surge in lager volume can dwarf any media effect. If the model does not properly control for temperature and daylight hours, it will misattribute warm-summer gains to whatever media happened to run in Q2.

**Distribution drives disproportionate volume.** Gaining or losing a major grocery chain account or a prominent tap handle can move volume by multiples that no media budget can match. Distribution should be modeled as a separate lever, not baked into a generic "all other" term.

**NA beer requires a separate model or a carefully specified sub-model.** Non-alcoholic beer buyers respond to different occasions and triggers. Lumping NA SKUs into a total-portfolio model masks the distinct dynamics of the fastest-growing segment. Breweries with meaningful NA volume should model it separately or build sub-category interaction terms.

## Reading the Output: Three Questions to Ask

Once a model is built, three questions separate useful insight from a beautiful chart that collects dust.

**What is the marginal ROI on my next dollar by channel?** The model produces response curves that show how return per dollar changes as spend increases. Most brands discover that one or two channels are operating well above their efficient frontier — they are spending into steeply diminishing returns without knowing it.

**What happens to volume if I cut promotion depth?** For many beer brands, deep price promotions are the largest single driver of incremental volume — and also the most margin-destructive. The model can quantify the volume/margin trade-off of a 5% reduction in average promotional depth.

**What is the halo effect of brand media on trade performance?** Some media channels drive consumers into stores primed to respond to a display. MMM can estimate this interaction effect, which is routinely undervalued when channels are evaluated in isolation.

## The Craft Brewery Adaptation

National MMM frameworks require data at a scale that many independent breweries cannot match. A practical adaptation for regional and craft operators: run a simplified two-variable model using weekly POS scan data from a key retail partner alongside documented promotion dates and depth. Even a rough decomposition of "promo volume" versus "baseline volume" is more useful than intuition alone.

For NA beer specifically, tracking the month-over-month baseline trend is particularly valuable. A rising baseline in NA suggests organic category adoption; a flat baseline despite heavy promotion indicates that the brand is buying volume rather than building it.

See also: [Attribution: Connecting Spend to the Tap Handle]({{ '/2025/marketing-attribution-beverage/' | relative_url }}) for the last-touch versus multi-touch tension that MMM is designed to resolve.

## Where This Approach Breaks

MMM is a retrospective tool. It tells you what drove volume in the past, under past competitive conditions, at past spend levels. Applying the model's coefficients directly to a market with a new competitor, a new distribution footprint, or a significantly different consumer context risks systematic over- or under-estimation. Models should be re-estimated annually at minimum, and after any major structural change to the brand or category.

*Part of the Marketing track — [browse all]({{ '/tags/' | relative_url }}#marketing).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="How much each channel contributes — the longer the bar, the bigger the effect."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">CONTRIBUTION</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Marketing Mix Modeling: What Really Drives Beer Volume</text><text x="60" y="109" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Channel A</text><rect x="180" y="90" width="300" height="26" rx="4" fill="#b45309"/><text x="60" y="153" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Channel B</text><rect x="180" y="134" width="230" height="26" rx="4" fill="#b45309"/><text x="60" y="197" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Channel C</text><rect x="180" y="178" width="150" height="26" rx="4" fill="#b45309"/><text x="60" y="241" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Channel D</text><rect x="180" y="222" width="90" height="26" rx="4" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">How much each channel contributes — the longer the bar, the bigger the effect.</figcaption>
</figure>

## Frequently asked questions

**What is marketing mix modeling and why does it matter for beer?**
Marketing mix modeling (MMM) is a statistical technique that decomposes sales volume into contributions from each marketing and trade lever — media spend, promotions, distribution changes, pricing, and external factors like weather or seasonality. For beer, where volume swings dramatically by season and occasion, understanding the true contribution of each lever is essential to avoid misattributing summer gains to a media campaign that merely ran at the same time.

**How much data does a brewery need to run a marketing mix model?**
A reliable MMM typically requires at least two to three years of weekly sales data alongside corresponding spend, pricing, and distribution records. Smaller independent breweries with limited historical data can run simpler regression-based versions, but the confidence intervals widen significantly below 18 months of data. Starting data collection now — even imperfectly — is better than waiting for the ideal dataset.

**What is the biggest mistake breweries make when interpreting MMM results?**
The most common error is treating the model's historical coefficients as a forward-looking planning tool without accounting for diminishing returns. A TV or digital channel that showed strong returns at a particular spend level will not necessarily deliver the same return at double the investment. Any MMM output should be paired with a response-curve analysis before budget decisions are made.
