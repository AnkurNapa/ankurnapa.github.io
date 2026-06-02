---
layout: post
lang: de
title: "Computer Vision für Traubensortierung und Krankheitserkennung im Weinberg"
image: /assets/og/computer-vision-grape-sorting-disease.png
description: "Wie Computer Vision Trauben am Annahmeplatz sortiert und Weinbergkrankheiten aus Drohnen- und Handybildern erkennt — schneller und konsistenter als manuell, mit ehrlichen Grenzen bei Beleuchtung und Randfällen."
date: 2024-12-05
updated: 2024-12-05
permalink: /de/2024/computer-vision-grape-sorting-disease/
tags: [winemaking, viticulture, computer-vision]
faq:
  - q: "Was können optische Traubensortierer tatsächlich aussortieren?"
    a: "Fremdmaterial außer Trauben (MOG) wie Blätter, Stiele und Steine, dazu unreife und faule Beeren — am Annahmeplatz, schneller und konsistenter als eine manuelle Sortierlinie."
  - q: "Kann Computer Vision Weinbergkrankheiten erkennen?"
    a: "Ja, bei sichtbaren Krankheiten. Drohnen- und Handybilder können Echten und Falschen Mehltau sowie Botrytis markieren und die Begehung lenken, aber sie können den Erreger nicht bestätigen — das tun weiterhin Labor- oder Expertenprüfungen."
  - q: "Ersetzt Computer Vision Menschen im Weinberg und Keller?"
    a: "Nein. Es übernimmt das repetitive, mengenstarke Hinschauen — Sortieren und Begehen — konsistenter als ein müder Mensch, aber Urteilsvermögen, Behandlungsentscheidungen und Laborbestätigung bleiben bei den Menschen."
---

**Kurze Antwort: Computer Vision verdient seinen Platz beim repetitiven Hinschauen — schlechte Beeren am Annahmeplatz aussortieren und Krankheiten über den Weinberg hinweg erkennen — schneller und konsistenter als Menschen, aber es bestätigt nichts von allein.** Vision ist das reifste KI-Werkzeug im Wein, weil die Aufgabe konkret ist: gut von schlecht unterscheiden, reif von faul, gesund von krank.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Weinproduktionsablauf steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Computer Vision für Traubensortierung und Krankheitserkennung im Weinberg</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ernte</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mahlen / Pressen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Reifung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Flasche</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Weinproduktionsablauf steht, von Anfang bis Ende.</figcaption>
</figure>

## Zwei Aufgaben, die Vision gut erledigt
Die erste ist das Sortieren. Optische Sortierer am Annahmeplatz weisen Fremdmaterial außer Trauben zurück — MOG, also Blätter, Stiele, Steine und die gelegentliche Schnecke — zusammen mit unreifen und faulen Beeren, bevor sie die Presse erreichen. Ein Kamera-und-Luftdüsen-System trifft tausende Annehmen/Zurückweisen-Entscheidungen pro Minute, und anders als eine menschliche Sortierlinie wird es nicht müde, abgelenkt oder langsamer, je weiter die Nacht voranschreitet. Diese Konsistenz schützt direkt die Weinqualität, denn eine Handvoll fauler Beeren kann einen Tank verderben.

Die zweite ist die Krankheits- und Ertragsarbeit im Weinberg. Drohnen- und Handybilder können Echten Mehltau, Falschen Mehltau und Botrytis von der Laubwand aus erkennen, und dieselben Vision-Pipelines zählen Beeren und Trauben, um Ertragsschätzungen zu speisen. Statt jede Reihe abzugehen, bekommt ein Winzer eine Karte, wo er hinschauen muss. Das knüpft direkt an [KI für die Ertragsprognose im Weinberg]({{ '/de/2024/ai-vineyard-yield-forecasting/' | relative_url }}) an, wo Traubenzählungen eine Kerneingabe sind.

## Erst messen: Bilder sind auch Daten
Computer Vision ist nach wie vor eine Data-Science-Disziplin, und die Daten hier sind Bilder. Ein Sortierer oder ein Begehungsmodell ist nur so gut wie die beschrifteten Beispiele, aus denen es gelernt hat — Beeren als reif, unreif, faul gekennzeichnet; Laubwandbereiche als gesund, Mehltau, Botrytis gekennzeichnet. Die Merkmale, an denen sich das Modell orientiert, sind Farbe, Form und Textur, was bedeutet, dass die Bildbedingungen enorm wichtig sind: die Beleuchtung am Annahmeplatz, Winkel und Höhe der Drohne, die Auflösung des Handys. Bau den beschrifteten Satz wo möglich aus deinen eigenen Früchten und deinen eigenen Parzellen, denn ein Modell, das auf dem Weinberg eines anderen bei anderem Licht trainiert wurde, überträgt sich schlecht.

Die praktische Botschaft ist dieselbe wie überall sonst in diesem Track: erst messen. Erfasse konsistente Bilder, beschrifte sie sorgfältig, und das Modell hat etwas Solides zum Lernen.

## Wo es scheitert
Beleuchtung und Trainingsverzerrung sind die alltäglichen Fehlermodi. Ein bei Tageslicht kalibrierter Sortierer kann unter hartem Nachtschicht-Licht falsch urteilen; ein Krankheitsmodell, das auf der Laubwand einer Sorte trainiert wurde, kann bei einer anderen stolpern. Randfälle beißen — sonnenverbrannte Beeren, Staub, Schatten, eine ungewöhnliche Fäule — weil das Modell nur kennt, was ihm gezeigt wurde. Die Kosten sind ebenfalls real: Optische Sortierer und Drohnenprogramme sind eine Investition, die ein kleiner Erzeuger gegen Handsortierung und das Abgehen der Reihen abwägen muss. Und die harte Grenze: Vision sieht Symptome, nicht Ursachen. Es kann einen Bereich markieren, der wie Mehltau aussieht, aber den Erreger zu bestätigen braucht weiterhin ein Labor oder ein erfahrenes Auge. Behandle die Ausgabe des Modells als das, wo man hinschauen und was man aussortieren soll, nicht als Diagnose oder Behandlungsentscheidung.

## Wie generative KI hineinpasst
Der aufkommende generative Blickwinkel ist das Vision-Language-Modell, das Bilder in einen geschriebenen Begehungsbericht verwandelt. Statt einem Winzer einen Ordner voller Drohnenbilder zu reichen, schreibt das System: „Parzelle 5, Nordende — gehäufte Laubwandbereiche, konsistent mit Echtem Mehltau über etwa 0,4 ha; geringere Vigor an den westlichen Reihen; empfehle Ground-Truthing und vorrangige Behandlung hier vor der prognostizierten warmen, feuchten Phase." Es markiert die Parzellen, die Aufmerksamkeit brauchen, ordnet sie, und entwirft den Hinweis, sodass die Maßnahme dokumentiert ist — während es trotzdem einen Menschen zur Bestätigung hinausschickt, bevor jemand spritzt. Derselbe Ansatz kann einen Sortierlauf oder einen Traubenzähldurchgang zusammenfassen. Die generative Schicht verbessert nicht, was die Kamera sieht; sie macht das, was die Kamera sieht, handhabbar.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein Vision-Modell lokalisiert und beschriftet Merkmale in jedem Bild und bewertet sie dann."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">COMPUTER VISION</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Computer Vision für Traubensortierung und Krankheitserkennung im Weinberg</text><rect x="80" y="80" width="360" height="180" rx="6" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><rect x="120" y="120" width="110" height="90" fill="none" stroke="#5b7a1f" stroke-width="2.5"/><rect x="270" y="150" width="120" height="70" fill="none" stroke="#b45309" stroke-width="2.5"/><text x="120" y="114" font-family="sans-serif" font-size="11" font-weight="700" fill="#5b7a1f">ok</text><text x="270" y="144" font-family="sans-serif" font-size="11" font-weight="700" fill="#b45309">markiert</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="450" y1="170" x2="500" y2="170"/><polygon points="500,163 512,170 500,177" stroke="none"/></g><rect x="525" y="140" width="150" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600" y="176" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17">Label + Score</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein Vision-Modell lokalisiert und beschriftet Merkmale in jedem Bild und bewertet sie dann.</figcaption>
</figure>

## Das Fazit
Computer Vision ist die produktionsreifste KI im Keller und Weinberg, weil es eine konkrete Aufgabe erledigt — Früchte sortieren und Krankheiten begehen — konsistenter als müde Menschen. Aber es hängt von guten Bildern ab, es scheitert bei Beleuchtung und Randfällen, und es bestätigt nichts: Es sagt dir, wo du hinschauen und was du aussortieren sollst, und gibt das Urteil dann an Menschen und das Labor zurück.

*Teil des Tracks [Weinbereitung & KI]({{ '/de/tracks/winemaking-ai/' | relative_url }}).* Verwandt: [KI für die Ertragsprognose im Weinberg]({{ '/de/2024/ai-vineyard-yield-forecasting/' | relative_url }}).

## Häufig gestellte Fragen

**Was können optische Traubensortierer tatsächlich aussortieren?**
Fremdmaterial außer Trauben (MOG) wie Blätter, Stiele und Steine, dazu unreife und faule Beeren — am Annahmeplatz, schneller und konsistenter als eine manuelle Sortierlinie.

**Kann Computer Vision Weinbergkrankheiten erkennen?**
Ja, bei sichtbaren Krankheiten. Drohnen- und Handybilder können Echten und Falschen Mehltau sowie Botrytis markieren und die Begehung lenken, aber sie können den Erreger nicht bestätigen — das tun weiterhin Labor- oder Expertenprüfungen.

**Ersetzt Computer Vision Menschen im Weinberg und Keller?**
Nein. Es übernimmt das repetitive, mengenstarke Hinschauen — Sortieren und Begehen — konsistenter als ein müder Mensch, aber Urteilsvermögen, Behandlungsentscheidungen und Laborbestätigung bleiben bei den Menschen.
