---
layout: post
title: "Scraping and Trend-Mining 250 Public Homebrew Recipes: Regex Where You Can, LLM Where You Must"
image: /assets/og/scraping-trend-mining-250-homebrew-recipes.png
description: "Part 4 of The Brewer's Agent. A small data engineering project on 250 recently shared homebrew recipes: polite scraping, the parsing traps, normalising to base units, when regex beats an LLM and when it does not, a consistency check the data failed 12 times, and what the recipes actually say about 2025 and 2026 brewing."
date: 2026-09-05 09:00:00 -0700
updated: 2026-09-05
tags: [brewing-science, brewers-agent, data-engineering, generative-ai, recipe-design]
faq:
  - q: "Is it acceptable to scrape public homebrew recipe sites?"
    a: "Only within the site's terms and robots.txt, at a gentle request rate, and for analysis rather than republishing. Scrape pages that are public without logging in, identify yourself, cache what you fetch so you never hit a page twice, and publish aggregate findings instead of copying people's recipes."
  - q: "Should I use an LLM or regular expressions to parse recipe data?"
    a: "Use regular expressions and plain parsing for structured fields such as gravity, bitterness and amounts, because they are fast, free and exact. Use an LLM for the messy parts, such as resolving hop and yeast names that are spelled several ways, and validate its output against a list of known varieties."
  - q: "What did 250 recent homebrew recipes show about trends?"
    a: "American IPA was the most shared style with 26 recipes, Citra and Cascade were almost level as the most used hops at 84 and 83 uses, and two clean American ale yeasts carried nearly a quarter of all recipes. Hazy and New England IPA was the clearest modern trend with 13 recipes. It is one site's recent feed, so treat it as a signal, not a census."
---

**Short answer: 250 recently shared homebrew recipes make a good small data engineering project, and most of the work is not the scraping. It is the parsing: stats printed two to a line, amounts like "7 lbs 14.00 oz", custom ingredients marked with an asterisk, and one hop spelled three ways. Parse the structured fields with plain code, normalise everything to base units, use an LLM only for resolving messy names, and check the data against itself (12 recipes had an ABV that did not match their own gravities). What came out: American IPA leads, Citra and Cascade are neck and neck, and hazy IPA is the trend that is actually moving.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A pipeline for 250 homebrew recipes. Polite scrape of public pages into a raw cache, then parse structured fields with regex, then normalise to base units such as kilograms, litres and grams per litre, then resolve messy hop and yeast names with an LLM checked against a known list, then run consistency checks, where 12 recipes had an ABV that disagreed with their own gravities by more than 0.3 points, then aggregate trends. Headline results: American IPA 26 recipes, Citra 84 uses, Cascade 83 uses, hazy IPA 13 recipes.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">250 RECIPES, SIX STEPS, ONE PART THAT NEEDS AN LLM</text>
<g font-family="sans-serif">
<rect x="20" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="94" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">polite scrape</text>
<text x="94" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">public pages, cached</text>
<rect x="183" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="257" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">parse</text>
<text x="257" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">regex on labels</text>
<rect x="346" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="420" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">normalise</text>
<text x="420" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">kg, L, g/L, &#176;P</text>
<rect x="509" y="60" width="148" height="80" rx="9" fill="#06483f"/>
<text x="583" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">resolve names</text>
<text x="583" y="112" text-anchor="middle" font-size="10" fill="#cfe6df">LLM + known list</text>
<rect x="672" y="60" width="148" height="80" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="746" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">check</text>
<text x="746" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">12 ABV mismatches</text>
<rect x="835" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="909" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">aggregate</text>
<text x="909" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">trends, not copies</text>
<g font-size="11" fill="#06483f">
<rect x="20" y="170" width="230" height="70" rx="9" fill="#f0f6f5"/>
<text x="135" y="198" text-anchor="middle" font-weight="700">American IPA</text><text x="135" y="220" text-anchor="middle">26 recipes, top style</text>
<rect x="266" y="170" width="230" height="70" rx="9" fill="#f0f6f5"/>
<text x="381" y="198" text-anchor="middle" font-weight="700">Citra 84 &#183; Cascade 83</text><text x="381" y="220" text-anchor="middle">hop uses, neck and neck</text>
<rect x="512" y="170" width="230" height="70" rx="9" fill="#f0f6f5"/>
<text x="627" y="198" text-anchor="middle" font-weight="700">2 ale yeasts</text><text x="627" y="220" text-anchor="middle">58 of 250 recipes</text>
<rect x="758" y="170" width="225" height="70" rx="9" fill="#f0f6f5"/>
<text x="870" y="198" text-anchor="middle" font-weight="700">Hazy / NEIPA</text><text x="870" y="220" text-anchor="middle">13 recipes, the mover</text>
</g>
<rect x="20" y="268" width="963" height="46" rx="10" fill="#06483f"/>
<text x="500" y="296" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">THE SCRAPE TAKES AN HOUR &#183; THE PARSING TAKES THE WEEKEND</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Counts from the 250 most recently shared recipes on one public site, pulled in mid-2026. A signal from one community, not a census of brewing.</figcaption>
</figure>

Every brewer who writes code eventually wants to know what everyone else is brewing. Recipe-sharing sites publish thousands of recipes in the open, and it is tempting to pull the lot and ask a language model what the trends are. I did a smaller, more careful version: the 250 most recently shared recipes on one public site. It turned out to be a neat, complete data engineering exercise, with one place where an LLM genuinely helps and several where it would have made things worse.

## Scrape politely, or not at all

Before any code, three checks:

1. **Read robots.txt and the terms of use.** If the site says no, the project stops there.
2. **Public pages only.** No logging in to scrape other people's content, no working round paywalls.
3. **Analysis, not republishing.** People shared these recipes with their community. Publishing aggregate counts is fair. Reposting their recipes wholesale is not.

Then keep the footprint small: a real user agent with a contact address, one request every couple of seconds, and a local cache so every page is fetched exactly once. The newest-first listing pages held about 20 recipes each, so 250 recipes was a dozen listing pages and 250 detail pages. That is an hour at a gentle pace. Nobody's server should notice you.

## The parsing traps

This is where the time went. Recipe pages are written for people, and people do not need consistent formatting.

**Stats two to a line.** The page printed "Batch Size: 5.00 gal" and "Style: American IPA" on the same line with no separator. Splitting on lines gives nonsense. The fix is to anchor on the labels themselves and read up to the next known label.

**Mixed-unit amounts.** Grain amounts came as "7 lbs 14.00 oz", "12.00 oz" or "3 lbs". In the 250 recipes, 529 grain lines used pounds and ounces together, 276 ounces only and 189 pounds only. A parser that reads the first number and the first unit gets 7 pounds and silently loses 14 ounces.

**Custom ingredients.** Brewers who define their own ingredient get it prefixed with an asterisk. Leave the asterisk on and "*Safale US-05" and "Safale US-05" count as two yeasts.

**Stray whitespace.** Double spaces inside names split one hop into two in any count. Collapse whitespace before you aggregate anything.

**The type is in the title.** Whether a recipe is all-grain or extract was the last word of the title line, not a field. For the record, 243 of the 250 were all-grain.

## Normalise to base units, once

Every amount was converted on the way in: grain to kilograms, hops to grams, volumes to litres, and hop rates to grams per litre so a 5-gallon homebrew and a 20-litre one can be compared. Gravities stayed as the site gave them (specific gravity), with a Plato column derived by a tested conversion.

This is the same rule as [the calculation tools in part 2]({{ '/2026/brewing-agent-calculation-tools-not-sums/' | relative_url }}): base units inside, display units at the edge. Converting in one place, in code with tests, means a trend chart never quietly mixes ounces and grams.

## Regex where you can, LLM where you must

It is now easy to throw each page at a language model and ask for JSON. For this job that would have been slower, more expensive and less accurate for most of the fields.

**Structured fields: plain code.** Original gravity, final gravity, ABV, IBU, colour, amounts and boil times sit next to fixed labels. Regular expressions extract them exactly, for free, in milliseconds. An LLM would occasionally round a number, drop a decimal or "helpfully" convert a unit.

**Names: this is where the LLM earns its place.** Hop and yeast names are a mess. In this sample, "Amarillo Gold" (49 uses) and "Amarillo" (27) are the same hop sold under two names, and "Fuggle" and "Fuggles" split 16 and 16. Yeasts appear under a lab code, a brand name or a nickname. Resolving those is fuzzy matching with domain knowledge, which language models do well.

The safe way to use it: give the model the raw name and a list of known varieties, ask it to pick one or say "unknown", and never accept a name that is not on the list. The model maps. The list decides.

For the published counts I actually left Amarillo and Amarillo Gold separate and said so, because merging them is a judgement and the reader should see it. That is a choice worth making visible rather than burying in a pipeline.

## Check the data against itself

Scraped data carries its own errors, and brewing data has a built-in check: ABV should follow from original and final gravity. Using the common homebrew approximation (the gravity drop times 131.25), 12 of the 250 recipes gave an ABV more than 0.3 points away from what their own gravities imply.

That does not mean 12 brewers made mistakes. Recipe software offers more than one ABV formula, some brewers edit the figure by hand, and some recipes are templates with stale numbers. What it means is that you should not trust the ABV column blindly, and a trend chart of ABV should be built from the gravities with one stated formula.

## What the 250 recipes said

With the caveat that this is one site's recent feed:

- **Styles:** American IPA led with 26 recipes, then American Pale Ale with 18. Saison, Blonde Ale, Witbier and Session IPA tied on 10 each. The community is IPA-led but far from IPA-only.
- **Hops:** Citra (84 uses) and Cascade (83) are almost level. Centennial, Amarillo, Magnum, Saaz and Simcoe follow. The classic American C-hops still dominate over newer varieties.
- **Yeast:** two clean American ale strains carried 58 recipes between them, nearly a quarter of the sample.
- **What is moving:** hazy and New England IPA, 13 recipes by name or style, well ahead of any other newer style. Newer hazy strains are appearing but still rare.
- **Typical beer:** median original gravity 1.055, median ABV 5.6%, median bitterness about 33 IBU.

None of that will surprise anyone who judges at homebrew competitions. That is fine. The value is in having it as data you can rerun next quarter and compare, not in a revelation.

## Where this breaks

**One site is one community.** People who share recipes publicly are not all brewers. Commercial breweries are absent, and some styles are overrepresented because their brewers like to share.

**Recent is not representative.** A newest-first feed over a few months catches seasonal brewing. Rerun it in winter and stouts will rise.

**Names are still judgement calls.** Merging spellings, grouping hazy and NEIPA, deciding whether "Session IPA" is its own style: every one of those decisions changes a count. Publish the rules with the results.

**Terms change.** A site that allows polite crawling today may not tomorrow. Check again before each rerun.

## The bottom line

The scraping was the easy hour. The weekend went on stats printed two to a line, pounds-and-ounces amounts, asterisks and one hop with three names, and that is normal for any real data engineering job. Parse structured fields with plain code, normalise once in tested functions, use an LLM for the fuzzy names with a list it must choose from, and check the data against its own physics. Then the trend chart is worth looking at.

Earlier on this blog: [Can AI Design a Beer Recipe?]({{ '/2026/can-ai-design-a-beer-recipe/' | relative_url }}) looked at generation. This post was about the data a generator would need. Next in the series: [evals for a brewing assistant]({{ '/2026/evals-for-a-brewing-assistant/' | relative_url }}). The full list is on [The Brewer's Agent series page]({{ '/series/brewers-agent/' | relative_url }}).

## Frequently asked questions

**Is it acceptable to scrape public homebrew recipe sites?**
Only within the site's terms and robots.txt, at a gentle request rate, and for analysis rather than republishing. Scrape pages that are public without logging in, identify yourself, cache what you fetch so you never hit a page twice, and publish aggregate findings instead of copying people's recipes.

**Should I use an LLM or regular expressions to parse recipe data?**
Use regular expressions and plain parsing for structured fields such as gravity, bitterness and amounts, because they are fast, free and exact. Use an LLM for the messy parts, such as resolving hop and yeast names that are spelled several ways, and validate its output against a list of known varieties.

**What did 250 recent homebrew recipes show about trends?**
American IPA was the most shared style with 26 recipes, Citra and Cascade were almost level as the most used hops at 84 and 83 uses, and two clean American ale yeasts carried nearly a quarter of all recipes. Hazy and New England IPA was the clearest modern trend with 13 recipes. It is one site's recent feed, so treat it as a signal, not a census.
