---
layout: post
lang: de
title: "Ein Karbonisierungsrechner in Excel: Speisezucker, PSI und Leitungsabgleich"
image: /assets/og/carbonation-calculator-excel.png
description: "Karbonisiere Bier mit Sicherheit in Excel: Speisezucker aus dem Rest-CO2, der Keg-Druck für jedes Zielvolumen und jede Temperatur sowie ein einfacher Abgleich der Schankleitungslänge."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
permalink: /de/2026/carbonation-calculator-excel/
tags: [brewing-science, excel, carbonation, packaging]
faq:
  - q: "Wie berechne ich Speisezucker in Excel?"
    a: "Zuerst das Rest-CO2, das das Bier bereits hält: =3.0378-0.050062*T+0.00026555*T^2 mit T als der wärmsten Temperatur, die es sah, in °F. Dann Traubenzucker in Gramm =(target_volumes - residual)*litres*4.0. Für Haushaltszucker multipliziere das Ergebnis mit 0.91."
  - q: "Welcher Druck karbonisiert Bier auf ein Zielvolumen?"
    a: "Setze den Keg-Druck (psi Überdruck) =(volumes+0.003342)/(0.01821+0.090115*EXP(-(T-32)/43.11))-14.695, wobei T die Ausschanktemperatur in °F ist. Für 2.5 Volumen bei 38 °F ergibt das etwa 11 psi. Kälteres Bier hält CO2 leichter, daher braucht es weniger Druck."
  - q: "Wie lang sollte eine Schankleitung sein?"
    a: "Gleiche die Leitung so ab, dass ihr Widerstand dem Keg-Druck entspricht: Länge in Fuß ≈ (keg_psi − rise×0.5 − 1) ÷ Widerstand, wobei eine 3/16-Zoll-Leitung etwa 2,2 psi/ft hat und rise die Höhe bis zum Hahn ist. Bei 11 psi und 3 ft Steigung sind das ungefähr 4 ft Leitung für einen sauberen, langsamen Ausschank."
---

**Kurze Antwort: Karbonisierung sind drei kleine Formeln. Speisezucker = (Ziel − Rest-CO2) × Liter × 4,0 Gramm Traubenzucker; Keg-Druck = (Volumen + 0,003342) ÷ (0,01821 + 0,090115·e^(−(T−32)/43,11)) − 14,695 psi; und abgeglichene Leitungslänge ≈ (Keg-psi − Steigung − 1) ÷ 2,2 Fuß. Setze sie in Excel, und du füllst auf Flasche und Keg nach einer Zahl ab statt nach Gefühl.**

Das ist die Vertiefung zu Anwendungsfall 17 aus der Säule [20 Brauberechnungen in Excel]({{ '/de/2026/advanced-brewing-calculations-excel/' | relative_url }}), die sowohl die Flaschen-Speisung als auch die Zwangskarbonisierung abdeckt, plus den Leitungsabgleich, der entscheidet, ob es tatsächlich gut ausschenkt. Sie verbindet sich mit der Datenseite in [Karbonisierungs- und Ausschankkonsistenz]({{ '/de/2022/predicting-carbonation-dispense-consistency/' | relative_url }}).

## Speisezucker für Flaschen

Bier hält bereits etwas gelöstes CO2, festgelegt durch die wärmste Temperatur, die es erreichte. Dieser Rest geht zuerst von deinem Ziel ab:

`residual =3.0378-0.050062*T+0.00026555*T^2`   (T in °F)
`corn_sugar_g =(target_vols-residual)*litres*4.0`

Beispiel: Bier, das bei 68 °F lag, Ziel 2,4 Volumen, 23 L → Rest `0.86`, Zucker `(2.4-0.86)*23*4.0 ≈ 141 g` Traubenzucker. Stattdessen mit Haushaltszucker speisen? Multipliziere mit 0,91. Der mit Abstand größte Fehler hier ist, den Rest-Term zu vergessen und ein warm gereiftes Bier zu Überschäumern überzuspeisen.

## Druck der Zwangskarbonisierung

Beim Kegging entfällt der Zucker — du setzt einen Druck und lässt das Bier ins Gleichgewicht kommen. Löse die Karbonisierungsbeziehung nach dem Überdruck bei deiner Ausschanktemperatur:

`=(vols+0.003342)/(0.01821+0.090115*EXP(-(T-32)/43.11))-14.695`

Beispiel: 2,5 Volumen bei 38 °F → etwa **11 psi**. Das Diagramm zeigt, warum du nicht einen Druck setzen und vergessen kannst: Je kälter das Bier, desto weniger Druck braucht es, um dasselbe CO2 zu halten.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 620 340" width="100%" style="max-width:620px;height:auto" role="img" aria-label="Diagramm zur Zwangskarbonisierung: Keg-Druck steigt mit der Temperatur für 2,0, 2,5 und 3,0 Volumen CO2">
<rect x="0" y="0" width="620" height="340" fill="#fdfbf7"/>
<text x="320" y="26" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Keg-Druck für eine Zielkarbonisierung</text>
<g stroke="#e0d8cc" stroke-width="1"><line x1="60" y1="170" x2="560" y2="170"/></g>
<g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="40" x2="60" y2="300"/><line x1="60" y1="300" x2="560" y2="300"/></g>
<polyline points="60,255 310,224 560,189" fill="none" stroke="#8a5a2b" stroke-width="3"/>
<polyline points="60,207 310,168 560,124" fill="none" stroke="#b45309" stroke-width="3"/>
<polyline points="60,159 310,112 560,60" fill="none" stroke="#7a1f3d" stroke-width="3"/>
<g font-family="sans-serif" font-size="12" font-weight="700">
<text x="566" y="189" fill="#8a5a2b">2.0 vol</text><text x="566" y="124" fill="#b45309">2.5 vol</text><text x="566" y="60" fill="#7a1f3d">3.0 vol</text>
</g>
<g font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle">
<text x="60" y="318">34 °F</text><text x="310" y="318">42 °F</text><text x="560" y="318">50 °F</text>
<text x="310" y="338">Ausschanktemperatur</text>
</g>
<g font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="end">
<text x="52" y="44">26</text><text x="52" y="174">13</text><text x="52" y="304">0</text></g>
<text x="22" y="170" font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle" transform="rotate(-90 22 170)">psi (Überdruck)</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Jede Linie ist ein Zielvolumen; der Druck steigt mit der Temperatur. Setze den Druck für deine Kühlschranktemperatur, nicht für eine generische Zahl.</figcaption>
</figure>

## Leitungsabgleich

Setze den richtigen Druck, und der Ausschank kann trotzdem schäumen, wenn die Leitung zu kurz ist, um ihn abzubauen. Gleiche die Leitung so ab, dass ihr Widerstand ungefähr dem Keg-Druck entspricht, unter Berücksichtigung des Anstiegs zum Hahn:

`length_ft =(keg_psi - rise_ft*0.5 - 1)/2.2`

(Eine 3/16-Zoll-Leitung hat ~2,2 psi/ft; 1 psi bleibt für die Ausschankgeschwindigkeit.) Bei 11 psi mit 3 ft Steigung: `(11 - 1.5 - 1)/2.2 ≈ 4 ft`. Zu kurz, und es schäumt; viel zu lang, und es schenkt langsam aus — die Formel bringt dich in den richtigen Bereich, von dem aus du kürzt.

## Wo es einen Plausibilitätscheck braucht

Zwei ehrliche Vorbehalte. Erstens: **Das Rest-CO2 setzt voraus, dass das Bier bei dieser Temperatur vollständig im Gleichgewicht war** — ein Bier, das kurz warm hochschoss, oder eines, das noch ausgast, wird nicht passen; speise im Zweifel ans untere Ende und lass die Reifung den Job zu Ende bringen. Zweitens: **Der Leitungswiderstand ist nominal** — echte Schläuche variieren nach Bohrung, Marke und Temperatur, und der Wert von 2,2 psi/ft ist ein Ausgangspunkt, kein Evangelium; rechne damit, nach den ersten Ausschänken einen Zoll oder zwei zu kürzen. Die Formeln nehmen das Rätselraten aus dem *Ziel*; deine Sinne schließen die letzten paar Prozent.

## Das Fazit

Drei Formeln decken die gesamte Karbonisierungsfrage ab: wie viel Zucker zu speisen, welchen Druck zu setzen und wie lang die Leitung zu schneiden ist. Baue sie einmal, und du karbonisierst nach einer Zahl — keine Überschäumer mehr, keine schalen Kegs, keine reinen Schaum-Ausschänke, die du erst im Nachhinein diagnostizieren kannst.

## Häufig gestellte Fragen

**Wie berechne ich Speisezucker in Excel?**
Zuerst das Rest-CO2, das das Bier bereits hält: =3.0378-0.050062*T+0.00026555*T^2 mit T als der wärmsten Temperatur, die es sah, in °F. Dann Traubenzucker in Gramm =(target_volumes - residual)*litres*4.0. Für Haushaltszucker multipliziere das Ergebnis mit 0.91.

**Welcher Druck karbonisiert Bier auf ein Zielvolumen?**
Setze den Keg-Druck (psi Überdruck) =(volumes+0.003342)/(0.01821+0.090115*EXP(-(T-32)/43.11))-14.695, wobei T die Ausschanktemperatur in °F ist. Für 2.5 Volumen bei 38 °F ergibt das etwa 11 psi. Kälteres Bier hält CO2 leichter, daher braucht es weniger Druck.

**Wie lang sollte eine Schankleitung sein?**
Gleiche die Leitung so ab, dass ihr Widerstand dem Keg-Druck entspricht: Länge in Fuß ≈ (keg_psi − rise×0.5 − 1) ÷ Widerstand, wobei eine 3/16-Zoll-Leitung etwa 2,2 psi/ft hat und rise die Höhe bis zum Hahn ist. Bei 11 psi und 3 ft Steigung sind das ungefähr 4 ft Leitung für einen sauberen, langsamen Ausschank.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).*
