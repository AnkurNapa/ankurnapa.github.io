---
layout: post
lang: de
title: "Bieraroma vorhersagen durch Stapeln von Malz-Aromarädern"
image: /assets/og/predicting-beer-flavour-malt-coa-flavour-wheels.png
description: "Gib jedem Malz sein Aromarad, skaliere es nach seinem Anteil an der Schüttung, summiere die Räder und verankere das Ergebnis im COA. Ein gewichteter Summen-Fingerabdruck des Bieraromas — und die Wahrnehmungsphysik, die es nicht vortäuschen kann."
date: 2026-05-28 09:00:00 -0700
updated: 2026-05-28
permalink: /de/2026/predicting-beer-flavour-malt-coa-flavour-wheels/
tags: [brewing-science, malting, flavour, data-science]
faq:
  - q: "Kann man das Bieraroma allein aus Malzdaten vorhersagen?"
    a: "Teilweise. Der malzbedingte Teil des Aromas — brotig, Biskuit, karamellig, nussig, Toffee, Röstaroma, Kaffee — lässt sich annähern, indem man das Aromarad jedes Malzes nimmt, es nach dem Extraktanteil dieses Malzes skaliert und die Räder zu einem Fingerabdruck summiert, verankert durch das Analysezertifikat. Aber Hopfen, Wasser, Hefe und Gärung fügen Aroma hinzu und wandeln es um, was die Schüttung nicht vorhersagen kann, daher prognostizieren Malzdaten den Malzcharakter, nicht das ganze Bier."
  - q: "Was ist ein Malz-Aromarad?"
    a: "Ein Malz-Aromarad, wie die von Weyermann veröffentlichten, bildet den sensorischen Charakter eines Malzes auf eine Reihe von Deskriptoren ab — brotig, Honig, karamellig, nussig, Toffee, Kaffee, Schokolade, Röstaroma — meist mit einer Intensität für jeden. Es verwandelt ein Malz in einen Vektor von Aromanoten, die du vergleichen, verschneiden und mit Sorgfalt addieren kannst."
  - q: "Warum ist Bieraroma nicht einfach die Summe seiner Malze?"
    a: "Weil Wahrnehmung nicht-linear ist. Noten maskieren einander, Intensitäten sättigen, statt sich zu addieren, und ein kleiner Prozentsatz Röst- oder Crystal-Malz kann weit über sein Gewicht hinaus dominieren. Eine gewichtete Summe von Aromarädern ist eine nützliche erste Näherung, aber sie muss gegen ein echtes Verkostungspanel kalibriert werden, um Maskierung und Sättigung zu korrigieren."
---

**Kurze Antwort: ja, für die Malzhälfte des Aromas — und nur als kalibrierte Näherung. Gib jedem Malz sein Aromarad (Weyermann und andere veröffentlichen sie), skaliere jedes Rad nach dem Extraktanteil dieses Malzes, lege die Räder übereinander und summiere sie zu einem einzigen Fingerabdruck, und verankere dann das Ganze am Analysezertifikat. Das sagt den malzbedingten Charakter des Bieres voraus — die Achse brotig, karamellig, nussig, Toffee, Röstaroma — erstaunlich gut. Was es nicht kann, ist die Hopfen-, Wasser-, Hefe- und Gärungsaromen hinzuzufügen, von denen die Schüttung nichts weiß, und es kann keine naive Summe sein: Wahrnehmung maskiert und sättigt, daher muss das gestapelte Rad gegen ein echtes Verkostungspanel kalibriert werden, bevor du ihm traust.**

Es ist eine wirklich gute Idee und ein alter Brauerinstinkt, explizit gemacht. Ein Mälzer betrachtet eine Schüttung — 80 % Pilsner, 15 % Münchner, 5 % Caramel — und schmeckt das Bier bereits halb vor. Das Aromarad verwandelt diesen Instinkt in Arithmetik: Jedes Malz wird zu einem Vektor von Noten mit Intensitäten, und ein Rezept wird zu einer gewichteten Summe dieser Vektoren. Der Trick ist zu wissen, wie weit genau diese Arithmetik trägt, bevor die Chemie des Sudhauses übernimmt.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 290" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Ein Radar-Aromarad mit zwei dünnen Malz-Polygonen und einem fetten Polygon des vorhergesagten Biers, neben einer Legende, die jedes Malz nach seinem Extraktanteil skaliert und summiert zeigt">
<rect x="0" y="0" width="760" height="290" fill="#ffffff"/>
<text x="380" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#06483f">Staple die Malzräder, gewichtet nach Extraktanteil</text>
<!-- radar grid hexagon -->
<polygon points="210,55 292,103 292,197 210,245 128,197 128,103" fill="none" stroke="#d8e6e1" stroke-width="1"/>
<polygon points="210,103 251,127 251,174 210,197 169,174 169,127" fill="none" stroke="#dcede8" stroke-width="1"/>
<line x1="210" y1="150" x2="210" y2="55" stroke="#dcede8" stroke-width="1"/>
<line x1="210" y1="150" x2="292" y2="103" stroke="#dcede8" stroke-width="1"/>
<line x1="210" y1="150" x2="292" y2="197" stroke="#dcede8" stroke-width="1"/>
<line x1="210" y1="150" x2="210" y2="245" stroke="#dcede8" stroke-width="1"/>
<line x1="210" y1="150" x2="128" y2="197" stroke="#dcede8" stroke-width="1"/>
<line x1="210" y1="150" x2="128" y2="103" stroke="#dcede8" stroke-width="1"/>
<!-- axis labels -->
<text x="210" y="46" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#4a6b64">Brotig</text>
<text x="300" y="100" text-anchor="start" font-family="sans-serif" font-size="10" fill="#4a6b64">Karamell</text>
<text x="300" y="205" text-anchor="start" font-family="sans-serif" font-size="10" fill="#4a6b64">Röstaroma</text>
<text x="210" y="262" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#4a6b64">Nussig</text>
<text x="120" y="205" text-anchor="end" font-family="sans-serif" font-size="10" fill="#4a6b64">Honig</text>
<text x="120" y="100" text-anchor="end" font-family="sans-serif" font-size="10" fill="#4a6b64">Fruchtig</text>
<!-- malt A: pilsner (amber, thin) -->
<polygon points="210,65 226,141 214,152 210,174 181,167 194,141" fill="none" stroke="#00695c" stroke-width="1.5"/>
<!-- malt B: caramel/munich (maroon, thin) -->
<polygon points="210,112 276,112 226,160 210,202 161,179 185,136" fill="none" stroke="#06483f" stroke-width="1.5"/>
<!-- predicted beer (ink, bold) -->
<polygon points="210,84 255,124 222,157 210,188 173,171 189,138" fill="#06483f" fill-opacity="0.07" stroke="#06483f" stroke-width="2.5"/>
<!-- legend / arithmetic -->
<text x="440" y="70" font-family="sans-serif" font-size="12" font-weight="700" fill="#06483f">Rezept → Fingerabdruck</text>
<line x1="440" y1="100" x2="470" y2="100" stroke="#00695c" stroke-width="2"/>
<text x="478" y="104" font-family="sans-serif" font-size="11" fill="#06483f">Pilsner · 80 % Extrakt</text>
<line x1="440" y1="124" x2="470" y2="124" stroke="#06483f" stroke-width="2"/>
<text x="478" y="128" font-family="sans-serif" font-size="11" fill="#06483f">CaraMunich · 15 %</text>
<text x="478" y="150" font-family="sans-serif" font-size="11" fill="#4a6b64">( + 5 % Röstmalz → Röst-Spitze )</text>
<line x1="440" y1="170" x2="470" y2="170" stroke="#06483f" stroke-width="2.5"/>
<text x="478" y="174" font-family="sans-serif" font-size="11" font-weight="700" fill="#06483f">Σ gewichtet = vorhergesagter Malzcharakter</text>
<text x="440" y="214" font-family="sans-serif" font-size="11" fill="#4a6b64">Dann am COA verankern (Farbe, Kolbach,</text>
<text x="440" y="230" font-family="sans-serif" font-size="11" fill="#4a6b64">FAN) und gegen dein Panel kalibrieren.</text>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Jedes Malz ist ein Polygon auf dem Aromarad. Skaliere nach Extraktanteil, summiere zum fetten Fingerabdruck, verankere es im Zertifikat — korrigiere dann mit echten Verkostungs-Scores für Maskierung und Sättigung.</figcaption>
</figure>

## Das Malz als Vektor, das Rezept als Summe

Ein Malz-Aromarad — die Art, die [Weyermann](https://www.weyermann.de) für sein Sortiment veröffentlicht — ist genau die Struktur, die ein Modell will: eine feste Reihe von Deskriptoren (brotig, Honig, Biskuit, karamellig, Toffee, nussig, Kaffee, Schokolade, Röstaroma) mit einer Intensität auf jedem. Das macht ein Malz zu einem Vektor. Eine Schüttung ist dann eine gewichtete Kombination dieser Vektoren, und das natürliche erste Modell ist ein lineares: Multipliziere das Rad jedes Malzes mit seinem **Extraktanteil** — nicht seiner Masse, denn ein extraktreiches Basismalz und ein ertragsarmes Röstmalz tragen Zucker, und damit Aroma, je Kilogramm ungleich bei — und addiere die Räder zusammen. Lege die Polygone übereinander, und die summierte Umrisslinie ist dein vorhergesagter Malz-Fingerabdruck. Es ist ehrlich, transparent und in einer Tabellenkalkulation berechenbar, bevor irgendein maschinelles Lernen beteiligt ist.

## Warum das COA es verankern muss

Ein Aromarad ist eine Beschreibung eines Malz*typs*; das [Analysezertifikat]({{ '/de/2026/genai-copilot-malt-certificate-analysis/' | relative_url }}) beschreibt die *Partie vor dir*, und die beiden müssen kombiniert werden. Farbe (EBC) skaliert die Röst- und Karamellachsen — eine dunkler-als-Spezifikation-Crystal-Partie schiebt Toffee Richtung verbrannt. Der Kolbach-Index und der freie Aminostickstoff formen die brotigen und würzigen Noten und speisen die [Gärung, die die Hefe später umwandeln wird]({{ '/de/2026/ai-optimised-kilning-malt/' | relative_url }}). Die Darrintensität bewegt ein Malz entlang seines eigenen Rades von brotig hin zu Biskuit und nussig. Die Pipeline ist also: Starte vom veröffentlichten Rad für jedes Malz, *korrigiere* jeden Vektor anhand des COA dieser Partie, dann gewichte und summiere. Ohne das COA sagt das Modell die Absicht des Rezepts voraus; mit ihm sagt das Modell die Charge voraus.

## Wo die Wahrnehmung die Arithmetik bricht

Sei deutlich über die Decke, denn hier führt eine naive Summe in die Irre. **Aromawahrnehmung ist nicht-linear.** Noten maskieren einander — Röstaroma und Kaffee werden eine zarte Honignote begraben, die die Arithmetik immer noch in voller Höhe zeigt. Intensitäten sättigen, statt sich zu addieren — zwei Karamellmalze ergeben nicht das doppelte Karamell, sie ergeben ein Plateau. Und kleine Anteile dominieren: 3 % eines dunklen Röstmalzes oder eines scharfen Crystal können das Bier weit über ihre 3 % Gewicht hinaus definieren, genau das Gegenteil dessen, was eine lineare Summe vorhersagt. Deshalb kann das gestapelte Rad nicht linear bleiben. Die Lösung ist, die Gewichtung auf Ergebnissen zu trainieren: Sammle deine eigenen Sude, jeden mit seiner Schüttung, seinen Malz-COAs und einem **Verkostungspanel-Score** auf denselben Deskriptoren, und passe ein Modell an, das die Maskierungs- und Sättigungskorrekturen lernt — eine nicht-lineare Regression, die den Eingang des gestapelten Rades auf den panelgemessenen Ausgang abbildet. Die Radsumme ist das Merkmal; das Panel ist die Wahrheit.

## Was die Schüttung schlicht nicht wissen kann

Die größere Ehrlichkeit: Malz sagt die Malzhälfte des Bieres voraus und nicht mehr. Hopfen bringt Bittere, Aroma und ganze Aromadimensionen, für die die Schüttung keine Achse hat. Wasserchemie verschiebt die wahrgenommene Bittere und Rösthärte. Und **Hefe und Gärung sind Aromafabriken** — Ester, Phenole, Schwefel, die Trockenheit des Vergärungsgrads —, die den Malz-Fingerabdruck in einem Hefeweizen oder einem Brett-Bier völlig überschwemmen und ihn in einem sauberen Lager kaum berühren können. Ein Malz-Modell ist daher ein Modul, nicht der ganze Motor: Es prognostiziert den malzbedingten Charakter genau und sollte mit Hopfen- und Gärungsmodellen für das fertige Bier kombiniert werden. Es ist außerdem, wie jede Malzvorhersage, nur so gut wie der Partiendurchschnitt — ein COA [kann eine schlecht gelöste Fraktion verbergen]({{ '/de/2026/predicting-malt-modification-germination/' | relative_url }}), die das Rad nie sieht.

## Das Fazit

Malz-Aromaräder zu stapeln, gewichtet nach Extraktanteil und verankert am Analysezertifikat, ist ein realer und nützlicher Weg, das malzbedingte Aroma eines Bieres vorherzusagen — und ein schöner, weil er den Instinkt des Mälzers explizit und überprüfbar macht. Bau es in zwei Schichten: eine transparente lineare Summe der Räder als Baseline, die jeder lesen kann, dann ein Kalibrierungsmodell, trainiert auf deinen eigenen Verkostungspanel-Scores, um die Maskierung und Sättigung zu korrigieren, auf der die Wahrnehmung besteht. Halte es bescheiden über den Umfang — es sagt das Korn voraus, nicht den Hopfen, das Wasser oder die Hefe — und es wird zu einem wirklich guten Rezeptgestaltungs- und Qualitätswerkzeug. Behandle es als das ganze Bier, und es wird deine interessantesten Chargen selbstbewusst fehlschmecken.

## Häufig gestellte Fragen

**Kann man das Bieraroma allein aus Malzdaten vorhersagen?**
Teilweise. Der malzbedingte Teil des Aromas — brotig, Biskuit, karamellig, nussig, Toffee, Röstaroma, Kaffee — lässt sich annähern, indem man das Aromarad jedes Malzes nimmt, es nach dem Extraktanteil dieses Malzes skaliert und die Räder zu einem Fingerabdruck summiert, verankert durch das Analysezertifikat. Aber Hopfen, Wasser, Hefe und Gärung fügen Aroma hinzu und wandeln es um, was die Schüttung nicht vorhersagen kann, daher prognostizieren Malzdaten den Malzcharakter, nicht das ganze Bier.

**Was ist ein Malz-Aromarad?**
Ein Malz-Aromarad, wie die von Weyermann veröffentlichten, bildet den sensorischen Charakter eines Malzes auf eine Reihe von Deskriptoren ab — brotig, Honig, karamellig, nussig, Toffee, Kaffee, Schokolade, Röstaroma — meist mit einer Intensität für jeden. Es verwandelt ein Malz in einen Vektor von Aromanoten, die du vergleichen, verschneiden und mit Sorgfalt addieren kannst.

**Warum ist Bieraroma nicht einfach die Summe seiner Malze?**
Weil Wahrnehmung nicht-linear ist. Noten maskieren einander, Intensitäten sättigen, statt sich zu addieren, und ein kleiner Prozentsatz Röst- oder Crystal-Malz kann weit über sein Gewicht hinaus dominieren. Eine gewichtete Summe von Aromarädern ist eine nützliche erste Näherung, aber sie muss gegen ein echtes Verkostungspanel kalibriert werden, um Maskierung und Sättigung zu korrigieren.

*Teil des [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }})-Tracks.*
