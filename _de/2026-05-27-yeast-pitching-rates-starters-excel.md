---
layout: post
lang: de
title: "Hefe-Anstellraten und Starter in Excel"
image: /assets/og/yeast-pitching-rates-starters-excel.png
description: "Dimensioniere deine Hefe richtig in einer Tabellenkalkulation: benötigte Zellen nach Stammwürze und Volumen, Vitalitätsverfall nach Packungsalter, benötigte Packungen und ein einfaches Starter-Wachstumsmodell mit durchgerechneten Beispielen."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
permalink: /de/2026/yeast-pitching-rates-starters-excel/
tags: [brewing-science, excel, yeast, fermentation]
faq:
  - q: "Wie berechne ich, wie viel Hefe ich anstellen muss?"
    a: "Benötigte Zellen (in Milliarden) = Anstellrate × Volumen in Litern × Stammwürze in °Plato, wobei die Rate bei etwa 0,75 Millionen Zellen pro mL pro °P für Ales und 1,5 für Lager liegt. In Excel ist das =rate*litres*plato, also braucht ein 23-L-Ale bei 12 °P 0,75×23×12 ≈ 207 Milliarden Zellen."
  - q: "Wie verändert sich die Hefevitalität mit dem Alter?"
    a: "Flüssighefe verliert rund 21 % Vitalität pro Monat, etwa 0,7 % pro Tag ab ihrem Herstellungsdatum. Modelliere es als =MAX(0,100-0.7*days)/100, um den überlebenden Anteil zu erhalten, und multipliziere dann die Zellzahl der Packung damit, um herauszufinden, wie viele lebende Zellen du wirklich anstellst."
  - q: "Wie groß muss mein Hefestarter sein?"
    a: "Schätze die Endzellzahl als =MIN(starter_litres*200, viable_cells_pitched + 140*starter_litres) Milliarden. Der erste Term ist die Dichte, bei der ein gerührter Starter sättigt (~200 Milliarden/L); der zweite ist ein Wachstum von etwa 1,4 Milliarden neuen Zellen pro Gramm der ~100 g/L Extrakt im Starter."
---

**Kurze Antwort: Die Anstellrate sind drei Multiplikationen und die Vitalität ist eine Subtraktion. Benötigte Zellen (Milliarden) = Rate × Liter × °Plato; lebende Zellen in einer alternden Packung = Packungszahl × (1 − 0,007 × Tage); und ein gerührter Starter endet nahe MIN(Volumen × 200, angestellt + 140 × Volumen) Milliarden Zellen. Setze die in ein Blatt und du hörst auf, zu wenig anzustellen — der mit Abstand häufigste vermeidbare Gärfehler.**

Das nimmt Anwendungsfall 13 aus der Säule [20 Brauberechnungen in Excel]({{ '/de/2026/advanced-brewing-calculations-excel/' | relative_url }}) und ergänzt die zwei Dinge, die entscheiden, ob du das Ziel tatsächlich triffst: die echte Zellzahl einer alternden Packung und wie stark ein Starter wächst. Es passt zur datengetriebenen Sicht auf [Hefevitalität und -lebenskraft]({{ '/de/2023/predicting-yeast-viability-vitality/' | relative_url }}).

## Schritt 1 — wie viele Zellen das Bier braucht

Das Ziel ist eine Anstellrate in Millionen Zellen pro Milliliter pro Grad Plato: etwa 0,75 für Ales, 1,5 für Lager, höher für starke Biere. Multipliziere es aus:

`cells_billion = rate * litres * plato`  →  `=B2*B3*B4`

Ein 23-L-Ale bei 12 °P braucht `0.75*23*12 = 207` Milliarden Zellen. Dieselbe Würze als Lager braucht `1.5*23*12 = 414` Milliarden — weshalb Lager so oft einen Starter oder mehrere Packungen brauchen.

## Schritt 2 — wie viele Zellen du tatsächlich hast

Eine frische Flüssigpackung enthält ~100 Milliarden Zellen, aber sie verliert Vitalität mit rund 21 % pro Monat, etwa 0,7 % pro Tag ab dem darauf aufgedruckten Datum. Also zählt die lebende Zahl:

`viability = MAX(0,100-0.7*days)/100`
`live_cells = packs * 100 * viability`

Eine vor 45 Tagen aufgedruckte Packung liegt bei `100-0.7*45 = 68.5%` Vitalität — also liefern zwei Packungen `2*100*0.685 = 137` Milliarden lebende Zellen, deutlich unter selbst dem Ale-Ziel. Der Verfall unten ist der Grund, warum „sie ist erst ein paar Wochen alt" nicht dasselbe ist wie genug Hefe.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 620 340" width="100%" style="max-width:620px;height:auto" role="img" aria-label="Hefevitalität, die etwa linear von 100 Prozent bei der Herstellung auf etwa 16 Prozent nach 120 Tagen abfällt">
<rect x="0" y="0" width="620" height="340" fill="#fdfbf7"/>
<text x="320" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Flüssighefe-Vitalität vs. Packungsalter</text>
<g stroke="#e0d8cc" stroke-width="1"><line x1="60" y1="170" x2="560" y2="170"/></g>
<g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="40" x2="60" y2="300"/><line x1="60" y1="300" x2="560" y2="300"/></g>
<polyline points="60,40 185,94.6 310,149.2 435,203.8 560,258.4" fill="none" stroke="#b45309" stroke-width="3"/>
<circle cx="310" cy="149.2" r="5" fill="#7a1f3d"/>
<text x="318" y="143" font-family="sans-serif" font-size="12" fill="#7a1f3d">60 Tage ≈ 58%</text>
<g font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle">
<text x="60" y="318">0</text><text x="185" y="318">30</text><text x="310" y="318">60</text><text x="435" y="318">90</text><text x="560" y="318">120</text>
<text x="320" y="338">Tage seit Herstellung</text>
</g>
<g font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="end">
<text x="52" y="44">100%</text><text x="52" y="174">50%</text><text x="52" y="304">0%</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Rund 0,7 % Verlust pro Tag. Setze das Alter deiner Packung in =MAX(0,100-0.7*days)/100 ein, bevor du der Zellzahl auf dem Etikett vertraust.</figcaption>
</figure>

## Schritt 3 — den Starter dimensionieren, um die Lücke zu schließen

Wenn die lebenden Zellen unter dem Ziel liegen, lässt ein Starter mehr wachsen. Ein gerührter 1.040er-Starter trägt etwa 100 g Extrakt pro Liter und sättigt nahe 200 Milliarden Zellen pro Liter; das Wachstum läuft bei rund 1,4 Milliarden neuen Zellen pro Gramm Extrakt. Kombiniere die Obergrenze und das Wachstum:

`ending_cells = MIN(starter_litres*200, live_cells + 140*starter_litres)`

Von den 137 Milliarden lebenden Zellen oben endet ein 2-L-Starter bei `MIN(2*200, 137+140*2) = MIN(400,417) = 400` Milliarden — bequem über dem Ale-Ziel und ins Lager-Territorium hinein. Füge eine Spalte für Gramm Trockenmalzextrakt (`starter_litres*100`) hinzu, damit deine Einkaufsliste aus demselben Blatt herausfällt.

## Wo das Modell ungenau wird

Zwei ehrliche Grenzen. Erstens, **das Wachstum hängt von Belüftung und Bewegung ab** — der Wert von 1,4 pro Gramm setzt eine Rührplatte oder häufiges Schütteln voraus; ein stehender Starter wächst weit weniger, und diese Formeln überschätzen ihn dann. Zweitens, **eine Zählung ist eine Schätzung, bis du sie misst**; der einzige Weg, deine Zelldichte wirklich zu kennen, ist ein Hämozytometer und ein Mikroskop oder ein gemessenes Anstellen aus einer Suspension. Nutze das Blatt, um in die richtige Größenordnung zu kommen und gewohnheitsmäßiges Unteranstellen zu beenden, nicht um eine Genauigkeit auf drei signifikante Stellen zu behaupten, die die Biologie nicht einhält.

## Das Fazit

Drei Formeln verwandeln „eine Packung anstellen und hoffen" in eine dimensionierte Entscheidung: benötigte Zellen aus Stammwürze und Volumen, lebende Zellen nach Vitalitätsverfall und die Endzahl aus einem Starter. Baue sie einmal, gib das Datum auf der Packung ein, und du fängst das Unteranstellen ab, bevor es zu einer langsamen, esterlastigen oder steckengebliebenen Gärung wird — nicht danach.

## Häufig gestellte Fragen

**Wie berechne ich, wie viel Hefe ich anstellen muss?**
Benötigte Zellen (in Milliarden) = Anstellrate × Volumen in Litern × Stammwürze in °Plato, wobei die Rate bei etwa 0,75 Millionen Zellen pro mL pro °P für Ales und 1,5 für Lager liegt. In Excel ist das =rate*litres*plato, also braucht ein 23-L-Ale bei 12 °P 0,75×23×12 ≈ 207 Milliarden Zellen.

**Wie verändert sich die Hefevitalität mit dem Alter?**
Flüssighefe verliert rund 21 % Vitalität pro Monat, etwa 0,7 % pro Tag ab ihrem Herstellungsdatum. Modelliere es als =MAX(0,100-0.7*days)/100, um den überlebenden Anteil zu erhalten, und multipliziere dann die Zellzahl der Packung damit, um herauszufinden, wie viele lebende Zellen du wirklich anstellst.

**Wie groß muss mein Hefestarter sein?**
Schätze die Endzellzahl als =MIN(starter_litres*200, viable_cells_pitched + 140*starter_litres) Milliarden. Der erste Term ist die Dichte, bei der ein gerührter Starter sättigt (~200 Milliarden/L); der zweite ist ein Wachstum von etwa 1,4 Milliarden neuen Zellen pro Gramm der ~100 g/L Extrakt im Starter.

*Teil des [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }})-Tracks.*
