---
layout: post
lang: de
title: "Malz-Aromaräder als Vektoren: Ähnlichkeitssuche und die Mischung, die der Mittelwert versteckt"
image: /assets/og/malt-aroma-wheels-as-vectors-similarity-search.png
description: "Teil 3 von The Brewer's Agent. Wandle veröffentlichte Malz-Aromaräder in Vektoren aus 22 Zahlen um, und du kannst nach Ersatzmalzen suchen und den Charakter einer Schüttung vorhersagen. Echte Zahlen aus 51 digitalisierten Weyermann-Rädern zeigen die Fallen: Der rohe Kosinus hält jedes Malz für ähnlich, Varianten fallen auf einen Vektor zusammen, und ein einfacher Mittelwert versteckt 10% Röstmalz."
date: 2026-08-31 09:00:00 -0700
updated: 2026-08-31
permalink: /de/2026/malt-aroma-wheels-as-vectors-similarity-search/
tags: [brewing-science, brewers-agent, embeddings, vector-search, malting]
faq:
  - q: "Kann man mit Vektorähnlichkeit ein Ersatzmalz finden?"
    a: "Ja, mit Sorgfalt. Wandle das Aromarad jedes Malzes in einen Vektor aus Deskriptor-Intensitäten um und vergleiche die Vektoren, um nahe Treffer zu finden. Zentriere die Vektoren zuerst auf das durchschnittliche Malz, denn die rohe Kosinus-Ähnlichkeit bewertet fast jedes Paar als ähnlich, und filtere nach Farbe und Extrakt als harten Bedingungen, damit der Aroma-Treffer kein Malz mit falscher Farbe vorschlagen kann."
  - q: "Warum unterschätzt das Mitteln von Aromavektoren Spezialmalze?"
    a: "Weil ein starker Minderheitscharakter von der Masse des Basismalzes verdünnt wird. Bei einer Schüttung aus 90% Pilsner und 10% Röstmalz setzt ein einfacher massengewichteter Mittelwert Kaffee auf 0,4 auf einer Skala von 0 bis 5, während Brauer wissen, dass 10% eines dunklen Röstmalzes deutlich wahrnehmbar sind. Ein Modell, das nach Aromastärke gewichtet und den stärksten Beitrag durchscheinen lässt, kommt auf etwa 2,6."
  - q: "Gehören Malz-Aromavektoren in eine Vektordatenbank?"
    a: "Bei ein paar Dutzend Malzen nicht. Eine Tabelle und ein paar Zeilen Code reichen. Eine Vektordatenbank lohnt sich, wenn du viele Quellen kombinierst, etwa Hunderte Malze, Hopfendeskriptoren und Verkostungsnotizen als Text-Embeddings, und über alle hinweg gefiltert suchen musst."
---

**Kurze Antwort: Ein Malz-Aromarad ist bereits ein Vektor. Zweiundzwanzig Deskriptoren mit Werten von 0 bis 5, von Kaffee über Honig bis Biskuit, sind 22 Zahlen pro Malz, und sobald du die hast, kannst du nach Ersatzmalzen suchen und den Charakter einer Schüttung abschätzen. Die echten Zahlen aus 51 digitalisierten Rädern zeigen drei Fallen. Die rohe Kosinus-Ähnlichkeit bewertet fast jedes Malz als ähnlich (Median 0,91), also zentriere die Vektoren zuerst. Malzvarianten, die sich ein veröffentlichtes Rad teilen, fallen auf einen Vektor zusammen, also müssen Farbe und Extrakt aus der Spezifikation kommen. Und ein einfacher Mittelwert aus 90% Pilsner und 10% CARAFA Special setzt Kaffee auf 0,4 von 5, was jeder Brauer für falsch hält.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Zwei Befunde aus 51 digitalisierten Malz-Aromarädern. Links liegt die Kosinus-Ähnlichkeit zwischen Pilsner Malz und CARAFA Special Typ 2 auf rohen Vektoren bei 0,82, was Ähnlichkeit nahelegt, und nach dem Zentrieren auf das durchschnittliche Malz bei minus 0,66, was sie korrekt als Gegensätze zeigt. Der Median des rohen Kosinus über alle Malzpaare liegt bei 0,91. Rechts liegt bei einer Schüttung aus 90 Prozent Pilsner und 10 Prozent CARAFA Special Typ 2 die Kaffeenote bei einfacher Massenmittelung bei 0,4 von 5 und bei nach Aromastärke gewichteter Überlagerung bei 2,6 von 5.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">51 MALZRÄDER ALS VEKTOREN: ZWEI DINGE, DIE DIE NAIVE MATHEMATIK FALSCH MACHT</text>
<g font-family="sans-serif">
<text x="245" y="62" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">PILSNER vs CARAFA SPECIAL 2: ÄHNLICHKEIT</text>
<rect x="40" y="80" width="200" height="90" rx="10" fill="#f0f6f5" stroke="#ff4081" stroke-width="2"/>
<text x="140" y="112" text-anchor="middle" font-size="12" fill="#4a6b64">roher Kosinus</text>
<text x="140" y="148" text-anchor="middle" font-size="28" font-weight="700" fill="#ff4081">0.82</text>
<rect x="260" y="80" width="200" height="90" rx="10" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="2"/>
<text x="360" y="112" text-anchor="middle" font-size="12" fill="#4a6b64">zentrierter Kosinus</text>
<text x="360" y="148" text-anchor="middle" font-size="28" font-weight="700" fill="#2e9e7c">&#8722;0.66</text>
<text x="250" y="200" text-anchor="middle" font-size="11" fill="#06483f">Median des rohen Kosinus über alle Paare: 0.91</text>
<text x="250" y="218" text-anchor="middle" font-size="11" fill="#06483f">alles wirkt ähnlich, bis du das Durchschnittsmalz abziehst</text>
<text x="745" y="62" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">90% PILSNER + 10% CARAFA SPECIAL 2: KAFFEE (0 BIS 5)</text>
<rect x="560" y="90" width="30" height="34" rx="4" fill="#ff4081"/>
<text x="600" y="113" font-size="12" font-weight="700" fill="#06483f">0.4 einfacher Massenmittelwert</text>
<rect x="560" y="140" width="195" height="34" rx="4" fill="#06483f"/>
<text x="765" y="163" font-size="12" font-weight="700" fill="#06483f">2.6 nach Stärke gewichtet</text>
<text x="745" y="205" text-anchor="middle" font-size="11" fill="#06483f">CARAFA allein erreicht 4 für Kaffee, Pilsner 0</text>
<text x="745" y="223" text-anchor="middle" font-size="11" fill="#06483f">der Mittelwert begräbt die Note, die ein Brauer schmeckt</text>
<rect x="40" y="262" width="920" height="50" rx="10" fill="#06483f"/>
<text x="500" y="285" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">EIN VEKTOR IST EIN GUTER ANFANG &#183; IN DIE MATHEMATIK DARÜBER GEHÖRT DAS BRAUWISSEN</text>
<text x="500" y="302" text-anchor="middle" font-size="10.5" fill="#cfe6df">berechnet aus Vektoren mit 22 Deskriptoren, digitalisiert aus veröffentlichten Weyermann-Würze-Aromarädern</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Zwei Zahlen, die vernünftig aussehen und falsch sind, und die zwei kleinen Änderungen, die sie korrigieren.</figcaption>
</figure>

Weyermann veröffentlicht für die meisten seiner Malze ein Aromarad: einen Kreis aus Deskriptoren (Kaffee, Kakao, brotig, Honig, Toffee, Trockenfrüchte und so weiter), jeder mit einer Intensität bewertet. Brauer lesen damit jeweils ein Malz. Staple sie, und du hast etwas Interessanteres: eine Tabelle, in der jedes Malz eine Zeile aus Zahlen ist. In der Sprache der GenAI ist das ein Embedding, nur eines, das ein Mensch lesen kann.

Ich habe 51 dieser Räder in Vektoren mit 22 Deskriptoren auf einer Skala von 0 bis 5 digitalisiert, während ich ein kleines offenes Werkzeug gebaut habe, um damit zu experimentieren. Der frühere Beitrag über das [Stapeln von Malz-Aromarädern]({{ '/de/2026/predicting-beer-flavour-malt-coa-flavour-wheels/' | relative_url }}) hat dafür argumentiert, eine Schüttung als gewichtete Summe zu behandeln. In diesem geht es darum, was passiert, wenn man Vektorsuche und Mischung auf diesen Zahlen richtig macht, und wo die naive Version still scheitert.

## Ein Rad ist ein Vektor

Jedes Malz wird zu einer Zeile wie dieser, gekürzt auf ein paar Deskriptoren:

| Malz | Kaffee | Zartbitterschokolade | brotig | Honig | Toffee | ... |
|---|---|---|---|---|---|---|
| Pilsner Malt | 0.0 | 1.0 | 2.0 | 1.0 | 1.5 | ... |
| CARAFA Special Type 2 | 4.0 | 3.0 | 4.0 | 1.5 | 2.5 | ... |

Leg ein paar Dutzend davon in eine Tabelle, und zwei nützliche Fragen werden zu Einzeilern. Welches Malz ist diesem am ähnlichsten? Und wie riecht diese Schüttung?

Das sind dieselben Operationen, die ein RAG-System auf Text-Embeddings ausführt, Ähnlichkeitssuche und Kombination, nur haben die Dimensionen hier Namen. Das macht Malz zu einem sehr guten Ort, um zu lernen, wie sich Vektormathematik verhält, denn du kannst jedes Ergebnis gegen das prüfen, was ein Brauer weiß.

## Falle 1: Der rohe Kosinus hält jedes Malz für ähnlich

Die Kosinus-Ähnlichkeit ist der Standardweg, Vektoren zu vergleichen. Sie misst den Winkel zwischen ihnen, ohne die Länge zu beachten, und reicht von 1 (gleiche Richtung) bis minus 1 (entgegengesetzt).

Auf den rohen Radvektoren liegt der Median der Kosinus-Ähnlichkeit über alle Malzpaare bei **0,91**. Pilsner Malz und CARAFA Special Typ 2, ein helles Basismalz und ein entspelztes Röstmalz, kommen auf **0,82**. Nach diesem Maß sind sie enge Verwandte.

Der Grund ist einfach. Jedes Rad hat eine Grundlinie aus niedrigen Werten bei den meisten Deskriptoren: ein bisschen brotig, ein bisschen süß, ein bisschen Honig. Alle Vektoren zeigen ungefähr in dieselbe Richtung, weil sie diesen Boden teilen. Der Kosinus sieht den gemeinsamen Boden und übersieht den Unterschied darüber.

Die Lösung ist, die Vektoren zu **zentrieren**: Zieh vor dem Vergleich von jedem das Durchschnittsmalz ab. Jetzt beschreibt jeder Vektor, wie sich ein Malz von einem typischen Malz unterscheidet. Pilsner gegen CARAFA Special 2 fällt auf **minus 0,66**, korrekt entgegengesetzt. Pilsner gegen Münchner Typ 1 landet bei 0,44, verwandt, aber verschieden, was ungefähr dem entspricht, was ein Brauer sagen würde.

Dasselbe passiert mit Text-Embeddings in RAG-Systemen, wo es Anisotropie heißt: Alles ballt sich in einer Ecke des Raums, und die Werte sehen höher aus, als sie sein sollten. Mit Malz ist es viel leichter zu sehen.

## Falle 2: Varianten fallen auf einen Vektor zusammen

Von den 51 Malzen gibt es nur **40 verschiedene Vektoren**. Weyermann veröffentlicht ein Rad für mehrere Malze einer Familie, also teilen sich CARAMUNICH Typ 1, 2 und 3 ein Rad, ebenso die drei CARAFA-Special-Typen. Ihre Kosinus-Ähnlichkeit untereinander ist exakt 1,0.

Das ist kein Datenfehler. Es ist das, was die Quelle sagt. Es bedeutet aber, dass eine reine Aromasuche nach "etwas wie CARAMUNICH Typ 2" bereitwillig Typ 1 oder Typ 3 als perfekte Treffer liefert, obwohl die Familie von 80 bis 160 EBC reicht und Typ 2 bei 110 bis 130 liegt. CARAFA Special umfasst 800 bis 1.500 EBC auf einem gemeinsamen Rad. Die Vektoren enthalten Aroma. Sie enthalten weder Farbe noch Extrakt noch Enzymaktivität.

Die Suche nach Ersatz muss also **hybrid** sein: zuerst harte Filter auf die Spezifikation (Farbbereich, Extrakt, maximaler Anteil), dann Vektorähnlichkeit, um den Rest zu ranken. Das ist genau das Muster für RAG über Dokumente, wo man nach Metadaten wie Datum oder Quelle filtert, bevor man nach Bedeutung rankt. Reine Vektorsuche liefert in beiden Fällen selbstsicheren Unsinn, wenn das, worauf es ankommt, nicht im Vektor steht.

## Falle 3: Der Mittelwert versteckt das Spezialmalz

Jetzt die Mischung. Das naheliegende Modell für eine Schüttung ist ein massengewichteter Mittelwert: 90% Pilsner, 10% CARAFA Special 2, also ist jeder Deskriptor 0,9 mal der Wert von Pilsner plus 0,1 mal der Wert von CARAFA.

Für Kaffee ergibt das **0,4 von 5**. Pilsner hat keinen und CARAFA hat 4, also sagt der Mittelwert: ein schwacher Hauch. Jeder Brauer, der 10% eines dunklen Röstmalzes in ein Bier gegeben hat, weiß, dass das kein schwacher Hauch ist. Kleine Anteile starker Malze wirken weit über ihr Gewicht hinaus.

Ein besseres Modell tut zwei Dinge. Es gewichtet jedes Malz nach einer **Aromastärke** und nach seinem Anteil (Röstmalze gelten als um ein Mehrfaches stärker als Basismalze), und es lässt den stärksten Einzelbeitrag durchscheinen, statt ihn wegzumitteln. Mit der Kalibrierung, die ich verwendet habe, kommt Kaffee auf etwa **2,6**, deutlich präsent, während eine Schüttung aus 100% Pilsner weiterhin das eigene Rad von Pilsner reproduziert.

Die Konstanten in diesem Modell sind Ermessensentscheidungen, so eingestellt, dass einzelne Malze ihr eigenes Rad reproduzieren und vertraute Schüttungen auf dem Papier ungefähr richtig schmecken. Das ist der ehrliche Status: eine vernünftige Struktur mit kalibrierten Stellschrauben, kein Naturgesetz.

## Wo GenAI hineinpasst

Hier sollte die Vektormathematik in einfachem Code bleiben, und das Sprachmodell übernimmt das Reden:

- **Eine Vorhersage erklären.** Mit dem gemischten Vektor und den wichtigsten Beiträgen zu jeder Note schreibt ein LLM die Zusammenfassung im Stil einer Verkostungsnotiz: "Röstaromen führen, Kaffee und Zartbitterschokolade vom CARAFA, brotiges Malz darunter". Es beschreibt Zahlen, die es bekommen hat. Es erfindet keine.
- **Freitext auf Deskriptoren abbilden.** Brauer beschreiben Malze mit eigenen Worten. Ein LLM kann "röstig, ein bisschen wie Vollkornkekse" auf die Achsen Biskuit und brotig abbilden, sodass eine Textanfrage die numerischen Vektoren durchsuchen kann.
- **Mit Text-Embeddings verbinden.** Verkostungsnotizen, Lieferantenbeschreibungen und Wettbewerbs-Feedback lassen sich als Text einbetten und neben den numerischen Rädern durchsuchen. Dort fängt eine Vektordatenbank an, sich zu lohnen. Für 51 Malze allein reichen eine Tabelle und ein paar Zeilen Code völlig.

## Wo das an Grenzen stößt

**Die Räder beschreiben Würze, nicht Bier.** Die veröffentlichten Räder gelten für eine Kongresswürze oder das ganze Korn. Gärung, Hopfung und Zeit verändern, was im Glas ankommt. Jede Vorhersage daraus betrifft den Beitrag des Malzes, nicht das fertige Bier.

**Ein Rad zu digitalisieren ist selbst eine Messung.** Intensitäten von einer gedruckten Grafik abzulesen, per Auge oder mit einem Bildmodell, bringt einen Fehler von vielleicht einem halben Punkt pro Deskriptor. Behandle die Vektoren als Näherung.

**Wahrnehmung ist nicht linear.** Aromen maskieren, verstärken und unterdrücken sich gegenseitig. Keine gewichtete Summe erfasst das vollständig, deshalb ist das Stärkemodell eine Kalibrierung und keine Herleitung.

**Kein offizielles Produkt.** Vektoren, die aus veröffentlichtem Material einer Mälzerei abgeleitet sind, sind eine unabhängige Lesart davon. Sie sind nicht von der Mälzerei autorisiert und sollten auch nicht so dargestellt werden.

## Das Fazit

Malz-Aromaräder sind ein Geschenk für alle, die Vektorsuche lernen, weil jede Dimension einen Namen hat, den ein Brauer versteht. Sie zeigen auch die üblichen Fallen ganz offen: Der rohe Kosinus schmeichelt allem, Vektoren enthalten nur, was man hineinlegt, und Mittelwerte begraben starke Minderheiten. Zentriere vor dem Vergleichen, filtere nach Spezifikation vor dem Ranken, gewichte nach Stärke vor dem Mischen, und lass das Sprachmodell die Zahlen erklären, statt sie zu erfinden.

Als Nächstes in der Serie: [250 öffentliche Hobbybrau-Rezepte scrapen und nach Trends durchsuchen]({{ '/de/2026/scraping-trend-mining-250-homebrew-recipes/' | relative_url }}). Zum Schwesterproblem beim Hopfen siehe [KI für Hopfenaroma-Profile und intelligenten Ersatz]({{ '/de/2023/ai-hop-aroma-profiling-substitution/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite von The Brewer's Agent]({{ '/series/brewers-agent/' | relative_url }}).

## Häufig gestellte Fragen

**Kann man mit Vektorähnlichkeit ein Ersatzmalz finden?**
Ja, mit Sorgfalt. Wandle das Aromarad jedes Malzes in einen Vektor aus Deskriptor-Intensitäten um und vergleiche die Vektoren, um nahe Treffer zu finden. Zentriere die Vektoren zuerst auf das durchschnittliche Malz, denn die rohe Kosinus-Ähnlichkeit bewertet fast jedes Paar als ähnlich, und filtere nach Farbe und Extrakt als harten Bedingungen, damit der Aroma-Treffer kein Malz mit falscher Farbe vorschlagen kann.

**Warum unterschätzt das Mitteln von Aromavektoren Spezialmalze?**
Weil ein starker Minderheitscharakter von der Masse des Basismalzes verdünnt wird. Bei einer Schüttung aus 90% Pilsner und 10% Röstmalz setzt ein einfacher massengewichteter Mittelwert Kaffee auf 0,4 auf einer Skala von 0 bis 5, während Brauer wissen, dass 10% eines dunklen Röstmalzes deutlich wahrnehmbar sind. Ein Modell, das nach Aromastärke gewichtet und den stärksten Beitrag durchscheinen lässt, kommt auf etwa 2,6.

**Gehören Malz-Aromavektoren in eine Vektordatenbank?**
Bei ein paar Dutzend Malzen nicht. Eine Tabelle und ein paar Zeilen Code reichen. Eine Vektordatenbank lohnt sich, wenn du viele Quellen kombinierst, etwa Hunderte Malze, Hopfendeskriptoren und Verkostungsnotizen als Text-Embeddings, und über alle hinweg gefiltert suchen musst.
