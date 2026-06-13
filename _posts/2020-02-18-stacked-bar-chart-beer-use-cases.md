---
layout: post
title: "The Stacked Bar Chart in Brewing: Three Beer Use Cases"
image: /assets/og/stacked-bar-chart-beer-use-cases.png
description: "When the question is composition — what makes up the total — the stacked bar chart shows the parts and the whole at once. Three beer use cases (channel mix, cost-per-hectolitre build-up, volume by style over time) and the 100% variant."
date: 2020-02-18 09:00:00 -0700
updated: 2020-02-18
tags: [brewing-science, beer-chart-guide, data-visualization, commercial-planning, financial-planning-analytics]
faq:
  - q: "When should a brewery use a stacked bar chart?"
    a: "When you care about composition — the parts that make up a total — and the total itself. Channel mix within total volume, the cost components that build up cost per hectolitre, or volume by style across several months. The stack shows both the whole (bar height) and the split (segments). Use the 100% stacked variant when only the proportions matter, not the totals."
  - q: "What is the weakness of a stacked bar chart?"
    a: "Only the bottom segment shares a common baseline, so the middle and top segments are hard to compare across bars — their start points float. If comparing one particular component across categories is the main goal, pull it out into its own bar chart or use a line. Too many segments also turns the stack into an unreadable ribbon."
  - q: "What is a 100% stacked bar chart used for in beer?"
    a: "Showing proportions when the totals don't matter or distract — channel mix as a percentage by month, package-format share by region. Every bar is the same height (100%) and only the segment proportions vary, making it easy to see a mix shifting over time, like off-premise gaining share against on-premise."
---

**Short answer: the stacked bar chart shows composition — the parts that build a total — and the total at once. In a brewery it answers "what's the mix": channel split within total volume, the cost components inside cost-per-hectolitre, style mix across months. Its weakness is that only the bottom segment sits on a shared baseline, so floating middle segments are hard to compare across bars. When only proportions matter, use the 100% stacked variant; when one component is the real question, pull it into its own chart.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="A stacked bar chart of monthly volume split into three channels, each bar showing the total height and the channel composition."><rect width="1000" height="240" fill="#fdfbf7"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">STACKED BAR — PARTS AND WHOLE TOGETHER</text><line x1="80" y1="200" x2="940" y2="200" stroke="#6b6258"/><g font-family="sans-serif" font-size="10"><rect x="150" y="150" width="70" height="50" fill="#b45309"/><rect x="150" y="116" width="70" height="34" fill="#8a5a2b"/><rect x="150" y="92" width="70" height="24" fill="#cbb89a"/><text x="185" y="216" text-anchor="middle" fill="#6b6258">Jan</text><rect x="320" y="142" width="70" height="58" fill="#b45309"/><rect x="320" y="104" width="70" height="38" fill="#8a5a2b"/><rect x="320" y="84" width="70" height="20" fill="#cbb89a"/><text x="355" y="216" text-anchor="middle" fill="#6b6258">Feb</text><rect x="490" y="132" width="70" height="68" fill="#b45309"/><rect x="490" y="98" width="70" height="34" fill="#8a5a2b"/><rect x="490" y="80" width="70" height="18" fill="#cbb89a"/><text x="525" y="216" text-anchor="middle" fill="#6b6258">Mar</text><rect x="660" y="122" width="70" height="78" fill="#b45309"/><rect x="660" y="92" width="70" height="30" fill="#8a5a2b"/><rect x="660" y="76" width="70" height="16" fill="#cbb89a"/><text x="695" y="216" text-anchor="middle" fill="#6b6258">Apr</text></g><g font-family="sans-serif" font-size="10"><rect x="800" y="80" width="12" height="12" fill="#b45309"/><text x="818" y="90" fill="#6b6258">off-prem</text><rect x="800" y="100" width="12" height="12" fill="#8a5a2b"/><text x="818" y="110" fill="#6b6258">on-prem</text><rect x="800" y="120" width="12" height="12" fill="#cbb89a"/><text x="818" y="130" fill="#6b6258">e-comm</text></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Bar height is the total; segments are the mix. The bottom segment is the only one easy to compare across bars.</figcaption>
</figure>

Part of [The Brewer's Chart Field Guide]({{ '/series/beer-chart-guide/' | relative_url }}). Where the [grouped bar]({{ '/2020/grouped-bar-chart-beer-use-cases/' | relative_url }}) compares series against each other, the stacked bar shows them adding up to a whole.

## When to reach for it

Reach for a stacked bar when **composition** is the point and the **total** still matters. The whole is the bar's height; the parts are its segments. If totals don't matter and only proportions do, use the **100% stacked** variant, where every bar is full height and only the split varies.

## Use case 1 — Channel mix within total volume

Monthly volume split into off-premise, on-premise and e-commerce. You see total volume growing *and* the mix shifting — the off-premise base, the on-premise recovery. A 100% version makes a share shift (e-commerce creeping up) even clearer.

## Use case 2 — Cost-per-hectolitre build-up

Stack malt, hops, packaging, energy and labour into the [cost per hectolitre]({{ '/2023/tableau-cogs-per-hectolitre-dashboard/' | relative_url }}). One bar per brand or per quarter shows both the total cost and which component drives it — the financial planner's favourite view.

## Use case 3 — Volume by style over time

Stack styles within each month's total. The total trend and the changing style mix appear together — your IPA growing its slice while the total holds. (When comparing *one* style across months is the goal, pull it onto its own [line]({{ '/2020/line-chart-beer-use-cases/' | relative_url }}).)

## Where this breaks

**Floating segments don't compare** — only the bottom segment shares a baseline; to compare a middle component across bars, extract it. **Too many segments** — more than five or six becomes a ribbon; group the tail into "other." **Total vs proportion confusion** — decide whether totals matter; if not, the 100% variant is clearer and less misleading.

## The bottom line

The stacked bar shows parts and whole together — channel mix, cost build-up, style mix over time — with the total as bar height and composition as segments. Use the 100% variant when only proportions matter, keep segments few, and pull a component out when comparing it across bars is the real question. Next, the part-to-whole chart to use sparingly: the [pie and donut]({{ '/2020/pie-donut-chart-beer-use-cases/' | relative_url }}).

## Frequently asked questions

**When should a brewery use a stacked bar chart?**
When you care about composition — the parts that make up a total — and the total itself. Channel mix within total volume, the cost components that build up cost per hectolitre, or volume by style across several months. The stack shows both the whole (bar height) and the split (segments). Use the 100% stacked variant when only the proportions matter, not the totals.

**What is the weakness of a stacked bar chart?**
Only the bottom segment shares a common baseline, so the middle and top segments are hard to compare across bars — their start points float. If comparing one particular component across categories is the main goal, pull it out into its own bar chart or use a line. Too many segments also turns the stack into an unreadable ribbon.

**What is a 100% stacked bar chart used for in beer?**
Showing proportions when the totals don't matter or distract — channel mix as a percentage by month, package-format share by region. Every bar is the same height (100%) and only the segment proportions vary, making it easy to see a mix shifting over time, like off-premise gaining share against on-premise.
