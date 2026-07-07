---
layout: post
lang: de
title: "Welches Bier sollen wir als Nächstes machen? Wie ich die Daten entscheiden ließ"
image: /assets/og/npd-which-beer-to-make-data.png
description: "Biere für AB InBev, SABMiller und United Breweries zu entwickeln bedeutete, Verbraucher- und Marktdaten zu verarbeiten, um zu wählen, was gebraut wird — so prägten KI und Analytik das vordere Ende der Neuproduktentwicklung."
date: 2026-05-27
updated: 2026-05-27
permalink: /de/2026/npd-which-beer-to-make-data/
tags: [beer-npd, new-product-development, consumer-insight, data-science]
faq:
  - q: "Kann KI entscheiden, welches neue Bier entwickelt wird?"
    a: "Nicht entscheiden — eingrenzen. KI und Analytik sind hervorragend darin, eine lange Liste von Ideen gegen Verbraucher-, Markt- und Verkaufsdaten zu ordnen, sodass du die wenigen entwickelst, hinter denen echte Nachfrage steht. Die endgültige Entscheidung gehört weiterhin Menschen, die die Marke und den Markt kennen."
  - q: "Welche Daten brauchst du, bevor du ein neues Bier entwickelst?"
    a: "Einzelhandels-Scan- und Abverkaufsdaten, Verbraucherpanel- und Umfrageantworten, Kategorie- und Wettbewerbertrends sowie deine eigene historische Launch-Performance. Die Qualität der Vorab-Entscheidung ist durch die Qualität dieser Daten begrenzt, nicht durch die Cleverness des Modells."
  - q: "Warum scheitern die meisten neuen Biere trotz Marktforschung?"
    a: "Weil Umfragen erfassen, was Menschen sagen, nicht was sie kaufen, und weil ein selbstbewusstes, auf dünnen oder verzerrten Daten trainiertes Modell trotzdem einen Flop hoch einstufen wird. Die Daten sagen dir, wo Nachfrage plausibel ist; sie können keinen Launch garantieren."
---

**Kurze Antwort: In den Jahren, in denen ich Biere für AB InBev, SABMiller und United Breweries entwickelte, war die schwierigste Frage nie, wie man braut — sondern welches Bier man überhaupt brauen sollte. KI und Analytik beantworteten das nicht für mich, aber sie verwandelten eine Wand aus Verbraucherumfragen, Einzelhandels-Scandaten und Verkaufshistorie in eine geordnete Shortlist, auf die ich tatsächlich handeln konnte. Die Daten grenzen das Feld ein; Menschen treffen weiterhin die Entscheidung.** So funktioniert das vordere Ende der Neuproduktentwicklung wirklich.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Ein NPD-Trichter: viele Rohdatenquellen speisen ein Screening-Modell, das Dutzende Ideen auf die wenigen brauenswerten eingrenzt."><rect x="0" y="0" width="1000" height="320" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DAS VORDERE ENDE DER NPD</text><g font-family="sans-serif"><rect x="20" y="60" width="200" height="44" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="120" y="87" text-anchor="middle" font-size="13" fill="#06483f">Einzelhandels-Scan &amp; Abverkäufe</text><rect x="20" y="116" width="200" height="44" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="120" y="143" text-anchor="middle" font-size="13" fill="#06483f">Verbraucherpanels</text><rect x="20" y="172" width="200" height="44" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="120" y="199" text-anchor="middle" font-size="13" fill="#06483f">Kategorie- &amp; Wettbewerbertrends</text><rect x="20" y="228" width="200" height="44" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="120" y="255" text-anchor="middle" font-size="13" fill="#06483f">Frühere Launch-Performance</text></g><polygon points="300,70 560,120 560,200 300,250" fill="#06483f" opacity="0.12" stroke="#06483f" stroke-width="1.5"/><text x="430" y="155" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#06483f">screenen &amp; bewerten</text><text x="430" y="176" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">Ideen ordnen</text><g font-family="sans-serif"><rect x="640" y="100" width="160" height="50" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="720" y="130" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">3–5 Konzepte</text><rect x="640" y="170" width="160" height="50" rx="6" fill="#ffffff" stroke="#4a6b64" stroke-width="1.2" stroke-dasharray="4 3"/><text x="720" y="200" text-anchor="middle" font-size="12" fill="#4a6b64">Dutzende geparkt</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="220" y1="138" x2="296" y2="150"/><polygon points="296,145 303,150 296,155" stroke="none"/></g><g fill="#06483f" stroke="#06483f" stroke-width="2"><line x1="560" y1="135" x2="636" y2="125"/><polygon points="636,120 643,125 636,130" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Das vordere Ende der NPD: viele verrauschte Datenquellen, ein Screening-Modell, eine kurze brauenswerte Liste.</figcaption>
</figure>

## Der Raum war voll mit Meinungen, nicht mit Belegen

Jedes Neuproduktmeeting, in dem ich saß, begann gleich: ein Dutzend Ideen an einem Whiteboard, jede von jemandem Ranghohen verfochten, der sicher war, dass seine der Gewinner sei. Ein stärkeres Weißbier. Ein bitterarmes Lager für neue Trinker. Ein festliches Saisonbier. Jeder hatte ein Bauchgefühl; niemand hatte eine Möglichkeit, sie zu vergleichen.

Das ist das eigentliche Problem am vorderen Ende der [Neuproduktentwicklung]({{ '/de/2025/forecasting-new-products-na-beer/' | relative_url }}). Man kann nicht zwölf Biere in voller Größe brauen, um herauszufinden, welches sich verkauft — jeder Pilotsud kostet Wochen und Geld. Man muss wählen, bevor man braut, und jahrelang wurde diese Wahl nach Dienstrang und Bauchgefühl getroffen.

## Was ich tatsächlich verarbeitete

Die Daten existierten; sie waren nur verstreut und unordentlich. Meine Aufgabe wurde, sie an einen Ort zu ziehen und vergleichbar zu machen. Drei Ströme zählten am meisten:

- **Einzelhandels-Scan- und Abverkaufsdaten** — was sich tatsächlich verkaufte, nach Stil, Gebinde und Region, und welche Segmente Quartal für Quartal wuchsen. Das kommt der Wahrheit am nächsten, weil es aufzeichnet, was Menschen *kauften*, nicht was sie *sagten*.
- **Verbraucherforschung** — Panels, Umfragen und Verkostungs-Scores. Nützlich, aber ich lernte, sie sorgfältig zu gewichten: erklärte Präferenz und Einkaufsverhalten sind verschiedene Tiere.
- **Unsere eigene Launch-Historie** — jedes Bier, das wir veröffentlicht hatten, was wir prognostizierten und was es tat. Das war der ehrlichste Lehrer, weil es zeigte, wo unser Optimismus zuvor falsch gelegen hatte.

Der Data-Science-Teil war unglamourös und entscheidend: inkonsistente SKU-Namen bereinigen, Regionen abgleichen und das Ganze in Merkmale formen, die ich bewerten konnte. Erst messen, dann modellieren — das Modell ist immer nur so gut wie die Tabelle, die du ihm fütterst.

## Von einer Wand aus Zahlen zu einer geordneten Shortlist

Sobald die Daten sauber waren, war die Analytik fast einfach. Ich bewertete jede Idee gegen Nachfragesignale: Wuchs ihr Segment, gab es Weißraum, den Wettbewerber nicht gefüllt hatten, waren ähnliche frühere Launches erfolgreich? Ein Clustering-Modell auf Verbraucherdaten half mir, [Trinker zu segmentieren]({{ '/de/2025/white-space-analytics-na-beer/' | relative_url }}) in Gruppen, die ein einzelner Durchschnitt verborgen hatte — und eine dieser Gruppen war klar unterversorgt.

Hier verändert generative KI nun den Rhythmus dieser Arbeit. Heute würde ich ein Sprachmodell auf den unordentlichen Freitext in Umfrageantworten und Wettbewerberrezensionen richten und es die wiederkehrenden Themen in Minuten zusammenfassen lassen — Arbeit, die mich früher Tage des Lesens kostete. Ich behandle seine Zusammenfassung als zu verifizierende Spur, nie als Befund, aber es verwandelt Lesen in Triage.

Das Ergebnis war nie „mach dieses Bier". Es war eine geordnete Shortlist von drei bis fünf Konzepten mit angehängten Belegen. Das ist genau die richtige Flughöhe für ein Modell: das Feld eingrenzen, dann an Menschen übergeben.

## Wo es bricht

Ich muss ehrlich über die Fehlschläge sein, denn das vordere Ende ist dort, wo Übervertrauen am teuersten ist.

Die Daten sagen das Routinemäßige gut voraus und das Seltene fast nie. Ein auf bestehenden Stilen trainiertes Modell ist blind für eine wirklich neue Kategorie — es hatte keine Möglichkeit, die alkoholfreie Welle kommen zu sehen, weil es keine Historie davon gab, aus der es lernen konnte. Umfragen schmeichelten Ideen, die am Regal floppten. Und dünne Daten sind gefährlich: Füttere einem flexiblen Modell eine Handvoll vergangener Launches, und es wird einen Flop mit völliger Selbstsicherheit hoch einstufen — dieselbe Falle, in die ich bei meinem [ersten Nachfrageprognose-Projekt]({{ '/de/2026/my-first-ai-project-beer-demand-forecasting/' | relative_url }}) tappte. Die Daten sagen dir, wo Nachfrage *plausibel* ist. Sie können keinen Treffer versprechen.

## Das Fazit

Das vordere Ende der NPD ist ein Filterproblem, und genau darin sind KI und Analytik wirklich gut: einen verrauschten, widersprüchlichen Haufen Verbraucher- und Marktdaten zu nehmen und in eine verteidigbare Shortlist zu verwandeln. Es ersetzte „die lauteste Person im Raum" durch „die Belege auf dem Tisch" — und das allein machte die Biere, die ich daraufhin entwickelte, zu besseren Wetten. Aber die Daten grenzen ein; sie entscheiden nicht. Das Urteil, das den Gewinner aus der Shortlist wählt, gehört weiterhin Menschen, die die Marke und den Trinker kennen.

*Beer NPD with Data — Teil 1 von 3. [Die vollständige Serie ansehen]({{ '/de/series/beer-npd/' | relative_url }}) · [Weiter: Rezept- und sensorische Daten verarbeiten →]({{ '/de/2026/npd-recipe-sensory-data-development/' | relative_url }})*

## Häufig gestellte Fragen

**Kann KI entscheiden, welches neue Bier entwickelt wird?**
Nicht entscheiden — eingrenzen. KI und Analytik sind hervorragend darin, eine lange Liste von Ideen gegen Verbraucher-, Markt- und Verkaufsdaten zu ordnen, sodass du die wenigen entwickelst, hinter denen echte Nachfrage steht. Die endgültige Entscheidung gehört weiterhin Menschen, die die Marke und den Markt kennen.

**Welche Daten brauchst du, bevor du ein neues Bier entwickelst?**
Einzelhandels-Scan- und Abverkaufsdaten, Verbraucherpanel- und Umfrageantworten, Kategorie- und Wettbewerbertrends sowie deine eigene historische Launch-Performance. Die Qualität der Vorab-Entscheidung ist durch die Qualität dieser Daten begrenzt, nicht durch die Cleverness des Modells.

**Warum scheitern die meisten neuen Biere trotz Marktforschung?**
Weil Umfragen erfassen, was Menschen sagen, nicht was sie kaufen, und weil ein selbstbewusstes, auf dünnen oder verzerrten Daten trainiertes Modell trotzdem einen Flop hoch einstufen wird. Die Daten sagen dir, wo Nachfrage plausibel ist; sie können keinen Launch garantieren.
