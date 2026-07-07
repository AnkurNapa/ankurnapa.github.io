---
layout: post
lang: de
title: "Ein Dashboard für Wein-DTC- und Rebsorten-Verkäufe in Tableau"
image: /assets/og/tableau-wine-dtc-varietal-sales-dashboard.png
description: "Baue ein Tableau-Weinverkaufs-Dashboard, das DTC und Distribution vergleicht, Verkäufe nach Rebsorte, Region und Jahrgang aufschlüsselt, mit Club-Bindung und einer Marktkarte."
date: 2023-05-14
updated: 2023-05-14
permalink: /de/2023/tableau-wine-dtc-varietal-sales-dashboard/
tags: [winemaking, tableau, sales]
faq:
  - q: "Was sollte ein Weinverkaufs-Dashboard in Tableau abdecken?"
    a: "Direct-to-Consumer-Kanäle — Cellar Door, Club und E-Commerce — gegenüber der Distribution, dazu Verkäufe aufgeschlüsselt nach Rebsorte, Region und Jahrgang sowie die Club-Bindung im Zeitverlauf. Eine Marktkarte fügt die geografische Sicht hinzu."
  - q: "Wie vergleiche ich DTC- und Distributionsmargen in Tableau?"
    a: "Bringe beide Kanäle mit einem konsistenten Kanalfeld in eine Quelle und baue dann ein berechnetes Feld für die Marge je Kanal. Ein Balken im Direktvergleich macht die Margenlücke zwischen DTC und Distribution offensichtlich."
  - q: "Kann Tableau Weinverkäufe nach Jahrgang prognostizieren?"
    a: "Die eingebaute Prognose mit exponentieller Glättung gibt einen groben Trend, aber Jahrgangsmengen sind endlich und saisonal, also behandle sie als Anhaltspunkt. Für echte Planung modelliere die Nachfrage extern und visualisiere das Ergebnis."
---

**Kurze Antwort: Ein Weinverkaufs-Dashboard funktioniert, wenn es DTC gegen Distribution stellt, Umsatz nach Rebsorte, Region und Jahrgang aufschlüsselt und die Club-Bindung verfolgt — sodass du siehst, woher die Marge wirklich kommt.** Vereinbare die Kanaldefinitionen, bevor du baust, sonst ist der Vergleich bedeutungslos.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für Ein Dashboard für Wein-DTC- und Rebsorten-Verkäufe in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Ein Dashboard für Wein-DTC- und Rebsorten-Verkäufe in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Kennzahlen-Highlights oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerschneiden.</figcaption>
</figure>

## Definiere zuerst Kanäle und Marge
Die Messen-zuerst-Frage lautet: „Welcher Kanal und welcher Wein verdienen tatsächlich Geld?" DTC und Distribution verhalten sich überhaupt nicht gleich — Cellar Door, Club und E-Commerce tragen eine weit höhere Marge als ein Distributorenverkauf, aber geringeres Volumen. Die erste Aufgabe ist also ein sauberes Kanalfeld und eine Margenberechnung je Kanal, abgestimmt mit demjenigen, dem die Zahlen gehören. Rebsorte, Region und Jahrgang sind deine Dimensionen; Umsatz, Einheiten, Marge und Club-Bindung sind deine Kennzahlen.

Verkaufsdaten kommen meist aus mehr als einem System — einer E-Commerce-Plattform, einem Club-Tool, einem Distributorenbericht — daher ist Tableau Prep unverzichtbar, um sie in einer Quelle mit konsistenten Feldern für Kanal, Rebsorte und Jahrgang zu vereinen. Verbinde dich als aktualisierter Extract; Verkäufe brauchen selten einen Live-Feed.

## Baue die Kanal- und Marktansichten
Führe mit einem Vergleich DTC gegen Distribution: Umsatz und Marge nebeneinander, sodass die margenstarke DTC-Geschichte gegen die mengenstarke Distributionsgeschichte sichtbar wird. Eine FIXED-Berechnung der Detailebene — `{FIXED [Varietal], [Vintage] : SUM([Revenue])}` — lässt dich Aufschlüsselungen nach Rebsorte und Jahrgang bauen, die unabhängig von anderen Filtern stabil bleiben.

Füge eine Marktkarte mit geografischen Rollen hinzu, sodass Distributions- und E-Commerce-Verkäufe nach Region erscheinen, dimensioniert nach Umsatz und gefärbt nach Marge — nützlich, um zu erkennen, wo eine Rebsorte verkauft wird. Verfolge die Club-Bindung als Kohorte oder einfache Bindungskurve nach Beitrittsmonat. Filteraktionen binden alles zusammen: Klicke auf eine Rebsorte, und jede Ansicht fließt auf diesen Wein um, mit Sicherheit auf Zeilenebene, sodass ein Regionalmanager nur sein Gebiet sieht.

## Lass Pulse die Zahlen beobachten, die sich bewegen
Setze Tableau Pulse auf Club-Bindung und DTC-Umsatz, und es sendet einen Digest in natürlicher Sprache, wenn sich etwas verschiebt — „Club-Bindung in diesem Quartal um zwei Punkte gesunken" — bevor es in einem Monatsbericht auftaucht. Einstein Copilot kann einem Nicht-Analysten helfen, in einfacher Sprache zu fragen „welche Rebsorte ist letztes Quartal im DTC am schnellsten gewachsen" und ein Diagramm zurückzubekommen.

## Wo es bricht
Die ehrlichen Grenzen betreffen Daten und Stichprobengröße. Kanaldaten leben in Silos, und ein Distributoren-Abverkaufsbericht kann deinen DTC-Verkäufen Wochen hinterherhinken, sodass der Vergleich nie perfekt gleichzeitig ist — sei im Titel klar, welche Kanäle aktuell sind. Kleine Weingüter stoßen außerdem auf Kleinstichprobenprobleme: Eine Club-Kohorte von vierzig Mitgliedern erzeugt eine Bindungskurve, die bei einer Handvoll Kündigungen wild schwankt, also überinterpretiere sie nicht. Und die eingebaute Prognose weiß nicht, dass ein Jahrgang fast ausverkauft ist; sie wird Verkäufe von Wein projizieren, der nicht mehr existiert.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall ist."><rect x="0" y="0" width="720" height="310" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Ein Dashboard für Wein-DTC- und Rebsorten-Verkäufe in Tableau</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#00695c" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reichweite · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#00695c" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interesse · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#00695c" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Probe · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#00695c" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Gewinn · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall ist.</figcaption>
</figure>

## Das Fazit
Ein Tableau-Weinverkaufs-Dashboard verbindet Kanäle: DTC gegen Distribution, Umsatz nach Rebsorte, Region und Jahrgang, Club-Bindung und eine Marktkarte, wobei Pulse die Kennzahlen markiert, die sich bewegen. Definiere zuerst Kanäle und Marge, achte auf die Silos und kleinen Stichproben und behandle die eingebaute Prognose als Hinweis statt als Plan.

*Teil des Tracks [Winemaking & AI]({{ '/de/tracks/winemaking-ai/' | relative_url }}).* Verwandt: [ein Dashboard für Keller- und Barrique-Reife-Bestand in Tableau]({{ '/de/2023/tableau-wine-cellar-barrel-ageing-dashboard/' | relative_url }}).

## Häufig gestellte Fragen

**Was sollte ein Weinverkaufs-Dashboard in Tableau abdecken?**
Direct-to-Consumer-Kanäle — Cellar Door, Club und E-Commerce — gegenüber der Distribution, dazu Verkäufe aufgeschlüsselt nach Rebsorte, Region und Jahrgang sowie die Club-Bindung im Zeitverlauf. Eine Marktkarte fügt die geografische Sicht hinzu.

**Wie vergleiche ich DTC- und Distributionsmargen in Tableau?**
Bringe beide Kanäle mit einem konsistenten Kanalfeld in eine Quelle und baue dann ein berechnetes Feld für die Marge je Kanal. Ein Balken im Direktvergleich macht die Margenlücke zwischen DTC und Distribution offensichtlich.

**Kann Tableau Weinverkäufe nach Jahrgang prognostizieren?**
Die eingebaute Prognose mit exponentieller Glättung gibt einen groben Trend, aber Jahrgangsmengen sind endlich und saisonal, also behandle sie als Anhaltspunkt. Für echte Planung modelliere die Nachfrage extern und visualisiere das Ergebnis.
