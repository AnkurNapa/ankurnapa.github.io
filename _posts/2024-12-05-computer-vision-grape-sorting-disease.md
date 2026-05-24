---
layout: post
title: "Computer Vision for Grape Sorting and Vineyard Disease Detection"
image: /assets/og/computer-vision-grape-sorting-disease.png
description: "How computer vision sorts grapes at the crush pad and spots vineyard disease from drone and phone imagery — faster and more consistent than manual, with honest limits on lighting and edge cases."
date: 2024-12-05
updated: 2024-12-05
tags: [winemaking, viticulture, computer-vision]
faq:
  - q: "What can optical grape sorters actually reject?"
    a: "Material other than grapes (MOG) like leaves, stems, and stones, plus unripe and rotten berries — at the crush pad, faster and more consistently than a manual sorting line."
  - q: "Can computer vision detect vineyard disease?"
    a: "Yes, for visible diseases. Drone and phone imagery can flag powdery and downy mildew and botrytis and direct scouting, but it cannot confirm the pathogen — lab or expert checks still do that."
  - q: "Does computer vision replace people in the vineyard and cellar?"
    a: "No. It handles the repetitive, high-volume looking — sorting and scouting — more consistently than a tired human, but judgement, treatment decisions, and lab confirmation stay with people."
---

**Short answer: computer vision earns its place doing the repetitive looking — rejecting bad berries at the crush pad and spotting disease across the vineyard — faster and more consistently than people, but it confirms nothing on its own.** Vision is the most mature AI tool in wine because the task is concrete: tell good from bad, ripe from rotten, healthy from diseased.

## Two jobs vision does well
The first is sorting. Optical sorters at the crush pad reject material other than grapes — MOG, meaning leaves, stems, stones, and the odd snail — along with unripe and rotten berries, before they reach the press. A camera-and-air-jet system makes thousands of accept/reject calls a minute, and unlike a human sorting line it does not get tired, distracted, or slower as the night wears on. That consistency directly protects wine quality, because a handful of rotten berries can taint a tank.

The second is in-vineyard disease and yield work. Drone and phone imagery can detect powdery mildew, downy mildew, and botrytis from the canopy, and the same vision pipelines count berries and bunches to feed yield estimates. Instead of walking every row, a viticulturist gets a map of where to look. That ties directly into [AI for vineyard yield forecasting]({{ '/2024/ai-vineyard-yield-forecasting/' | relative_url }}), where bunch counts are a core input.

## Measure first: images are data too
Computer vision is still a data-science discipline, and the data here is images. A sorter or a scouting model is only as good as the labelled examples it learned from — berries tagged ripe, unripe, rotten; canopy patches tagged healthy, mildew, botrytis. The features the model keys on are colour, shape, and texture, which means image conditions matter enormously: the lighting at the crush pad, the angle and altitude of the drone, the resolution of the phone. Build the labelled set from your own fruit and your own blocks where you can, because a model trained on someone else's vineyard in different light will transfer poorly.

The practical message is the same as everywhere else in this track: measure first. Capture consistent imagery, label it carefully, and the model has something solid to learn.

## Where it breaks
Lighting and training bias are the everyday failure modes. A sorter calibrated in daylight can misjudge under harsh night-shift lighting; a disease model trained on one variety's canopy may stumble on another. Edge cases bite — sunburnt berries, dust, shade, an unusual rot — because the model only knows what it was shown. Cost is real too: optical sorters and drone programmes are an investment that a small producer has to weigh against hand-sorting and walking the rows. And the hard limit: vision sees symptoms, not causes. It can flag a patch that looks like mildew, but confirming the pathogen still needs a lab or an experienced eye. Treat the model's output as where to look and what to reject, not as a diagnosis or a treatment decision.

## How generative AI fits in
The emerging generative angle is the vision-language model that turns imagery into a written scouting report. Rather than handing a viticulturist a folder of drone images, the system writes: "Block 5, north end — clustered canopy patches consistent with powdery mildew across roughly 0.4 ha; lower vigour on the western rows; recommend ground-truthing and prioritising treatment here before the forecast warm, humid spell." It flags the blocks that need attention, ranks them, and drafts the note so the action is on record — while still sending a human out to confirm before anyone sprays. The same approach can summarise a sorting run or a bunch-count pass. The generative layer does not improve what the camera sees; it makes what the camera sees actionable.

## The bottom line
Computer vision is the most production-ready AI in the cellar and vineyard because it does a concrete job — sorting fruit and scouting disease — more consistently than tired humans. But it depends on good imagery, it breaks on lighting and edge cases, and it confirms nothing: it tells you where to look and what to reject, then hands judgement back to people and the lab.

*Part of the [Winemaking & AI]({{ '/tracks/winemaking-ai/' | relative_url }}) track.* Related: [AI for vineyard yield forecasting]({{ '/2024/ai-vineyard-yield-forecasting/' | relative_url }}).

## Frequently asked questions

**What can optical grape sorters actually reject?**
Material other than grapes (MOG) like leaves, stems, and stones, plus unripe and rotten berries — at the crush pad, faster and more consistently than a manual sorting line.

**Can computer vision detect vineyard disease?**
Yes, for visible diseases. Drone and phone imagery can flag powdery and downy mildew and botrytis and direct scouting, but it cannot confirm the pathogen — lab or expert checks still do that.

**Does computer vision replace people in the vineyard and cellar?**
No. It handles the repetitive, high-volume looking — sorting and scouting — more consistently than a tired human, but judgement, treatment decisions, and lab confirmation stay with people.
