---
layout: post
lang: de
title: "Eine Distributoren-Scorecard in Tableau erstellen"
image: /assets/og/tableau-distributor-scorecard.png
description: "Erstelle eine gewichtete Distributoren-Scorecard in Tableau mit berechneten Feldern, Rang, Hervorhebungsaktionen und Explain Data — und vermeide die Manipulationsfallen."
date: 2023-03-21
updated: 2023-03-21
permalink: /de/2023/tableau-distributor-scorecard/
tags: [sales-intelligence, tableau, analytics]
faq:
  - q: "Welche Kennzahlen gehören auf eine Distributoren-Scorecard?"
    a: "Die drei dauerhaften sind Distributionsbreite (wie viele Zielkunden gelistet sind), Velocity (Verkaufsrate pro Kunde) und Compliance (ob Bestellungen, Zahlungen und Berichte die vereinbarten Konditionen einhalten). Füge Preis- oder Display-Umsetzung nur hinzu, wenn du sie konsistent messen kannst."
  - q: "Wie erstelle ich einen gewichteten Score in Tableau?"
    a: "Normalisiere jede Kennzahl mit einem berechneten Feld auf eine gemeinsame Skala von 0–100, multipliziere sie mit ihrer Gewichtung und summiere die Komponenten. Halte die Gewichtungen in Parametern, damit Prüfer sie sehen und anpassen können, statt sie in der Formel zu vergraben."
  - q: "Kann Tableau erklären, warum ein Distributor schlecht abgeschnitten hat?"
    a: "Explain Data kann die Dimensionen und Datensätze aufdecken, die am stärksten mit einer ungewöhnlichen Markierung verbunden sind, was ein nützlicher Ausgangspunkt ist. Es ist ein statistischer Hinweis, kein Urteil, also behandle es als Anstoß für ein menschliches Gespräch."
---

**Kurze Antwort: Eine Distributoren-Scorecard ist nur so fair wie die Gewichtungen dahinter, also baue diese Gewichtungen offen und lass Tableau das Ranking, Hervorheben und Erklären übernehmen.** Eine Scorecard verwandelt ein weitläufiges Partnernetzwerk in eine gerankte Liste, auf die ein Regionalleiter in einem vierteljährlichen Geschäftsreview reagieren kann — vorausgesetzt, die Mathematik ist vertretbar.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für „Eine Distributoren-Scorecard in Tableau erstellen“"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Eine Distributoren-Scorecard in Tableau erstellen</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Kennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerschneiden.</figcaption>
</figure>

## Definiere die Kennzahl vor dem Visual

Ein Score ist ein Modell, kein Diagramm, also gestalte ihn auch so. Wähle eine kleine Menge an Kennzahlen, die wirklich Ergebnisse treiben und die du über jeden Distributor hinweg sauber messen kannst: Distributionsbreite, Velocity und Compliance. Widerstehe dem Drang, ein Dutzend Vanity-Kennzahlen anzubauen; jede, die du hinzufügst, verwässert das Signal und lädt zu Streitigkeiten ein.

Normalisiere jede Kennzahl vor der Gewichtung auf dieselbe Skala, denn rohe Werte lassen sich nicht kombinieren — Gebinde pro Kunde und prozentuale Compliance leben in unterschiedlichen Einheiten. Eine einfache Min-Max-Berechnung funktioniert:

`( SUM([Velocity]) - WINDOW_MIN(SUM([Velocity])) ) / ( WINDOW_MAX(SUM([Velocity])) - WINDOW_MIN(SUM([Velocity])) ) * 100`

Kombiniere dann die normalisierten Komponenten mit Gewichtungen, die in Parametern gehalten werden: `[w_dist] * [Dist Score] + [w_vel] * [Vel Score] + [w_comp] * [Comp Score]`. Die Gewichtungen als Parameter offenzulegen ist die wichtigste einzelne Designentscheidung — es macht das Modell prüfbar und erlaubt einem skeptischen Vertriebsleiter, das Ranking während des Meetings unter seinen eigenen Annahmen neu zu berechnen.

## Ranken, hervorheben und erklären

Verwende Tableaus `RANK()`-Tabellenberechnung, um Distributoren zu ordnen, und präsentiere das Ergebnis als horizontales Balkendiagramm, sortiert nach Gesamtscore, mit den gewichteten Komponenten gestapelt, sodass ein Betrachter nicht nur den Rang sieht, sondern auch seine Zusammensetzung. Ein Distributor, der wegen starker Velocity, aber schwacher Compliance 72 erreicht, ist ein ganz anderes Gespräch als einer, der 72 umgekehrt erreicht.

Hervorhebungsaktionen verbinden das Dashboard zu einem Ganzen. Das Überfahren oder Anklicken eines Distributors hebt seine Zeile über jedes verknüpfte Arbeitsblatt hinweg hervor — seinen Trend, seine Kundenliste, sein Compliance-Detail — sodass die ganze Geschichte mit der Auswahl mitgeht, statt den Nutzer zum erneuten Filtern zu zwingen. Wenn eine Markierung daneben aussieht, klicke mit der rechten Maustaste und führe Explain Data aus: Tableau modelliert den erwarteten Wert und deckt die Datensätze oder Dimensionen auf, die am stärksten mit der Abweichung verbunden sind. Das könnte auf eine säumige Kette hinweisen, die die Compliance nach unten zieht. Behandle es als Spur zum Untersuchen, nicht als Schluss; Explain Data beschreibt die Daten, es kennt deinen kommerziellen Kontext nicht.

## Wo es bricht

Das tiefste Risiko ist nicht technisch, es ist verhaltensbedingt. Jeder Score, den du veröffentlichst, wird zum Ziel, und Ziele werden manipuliert. Gewichte Velocity zu stark, und ein Distributor jagt vielleicht schnell drehenden SKUs hinterher, während er dein Premium-Sortiment verstauben lässt. Belohne allein die Distributionsbreite, und du bekommst Alibi-Platzierungen ohne Verkaufsrate. Goodharts Gesetz gilt voll: Wenn eine Kennzahl zum Ziel wird, hört sie auf, eine gute Kennzahl zu sein. Überprüfe die Gewichtungen regelmäßig und achte auf Verhalten, das den Score statt das Geschäft optimiert.

Die zweite Grenze ist die Fairness über ungleiche Partner hinweg. Eine Scorecard, die Gebietsgröße, Kundenmix oder Verweildauer ignoriert, bestraft einen Distributor für einen Markt, den er geerbt hat, statt für eine Leistung, die er kontrolliert. Vergleiche wo möglich Gleiches mit Gleichem — segmentiere nach Markttyp — statt einen ländlichen Großhändler gegen ein Metropolen-Kraftpaket auf einer absoluten Skala zu ranken. Und wie immer rankt Tableau treu auch schmutzige Daten; ein fehlender Compliance-Feed wird als Null gelesen, nicht als „unbekannt", sofern du Nullwerte nicht bewusst behandelst.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall ist."><rect x="0" y="0" width="720" height="310" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Eine Distributoren-Scorecard in Tableau erstellen</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#00695c" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reichweite · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#00695c" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interesse · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#00695c" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Test · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#00695c" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Gewinn · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall ist.</figcaption>
</figure>

## Das Fazit

Eine gute Distributoren-Scorecard normalisiert ein paar ehrliche Kennzahlen, gewichtet sie transparent über Parameter und nutzt Rang- und Hervorhebungsaktionen, um das Ranking navigierbar zu machen. Explain Data beschleunigt die Diagnose, ersetzt aber nicht die Ermessensentscheidung. Schütze dich vor Manipulation, indem du Gewichtungen erneut prüfst und fair segmentierst, und denke daran, dass das Modell ein Gesprächsanstoß ist, nicht das letzte Wort.

*Teil des Tracks [Sales Intelligence]({{ '/de/tracks/sales-intelligence/' | relative_url }}).* Verwandt: [Ein Depletions- und Sell-Through-Dashboard in Tableau]({{ '/de/2023/tableau-depletions-sell-through-dashboard/' | relative_url }}).

## Häufig gestellte Fragen

**Welche Kennzahlen gehören auf eine Distributoren-Scorecard?**
Die drei dauerhaften sind Distributionsbreite (wie viele Zielkunden gelistet sind), Velocity (Verkaufsrate pro Kunde) und Compliance (ob Bestellungen, Zahlungen und Berichte die vereinbarten Konditionen einhalten). Füge Preis- oder Display-Umsetzung nur hinzu, wenn du sie konsistent messen kannst.

**Wie erstelle ich einen gewichteten Score in Tableau?**
Normalisiere jede Kennzahl mit einem berechneten Feld auf eine gemeinsame Skala von 0–100, multipliziere sie mit ihrer Gewichtung und summiere die Komponenten. Halte die Gewichtungen in Parametern, damit Prüfer sie sehen und anpassen können, statt sie in der Formel zu vergraben.

**Kann Tableau erklären, warum ein Distributor schlecht abgeschnitten hat?**
Explain Data kann die Dimensionen und Datensätze aufdecken, die am stärksten mit einer ungewöhnlichen Markierung verbunden sind, was ein nützlicher Ausgangspunkt ist. Es ist ein statistischer Hinweis, kein Urteil, also behandle es als Anstoß für ein menschliches Gespräch.
