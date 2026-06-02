---
layout: post
lang: de
title: "Sudhausausbeute und Ausbeute-Abgleich in Excel"
image: /assets/og/brewhouse-efficiency-yield-excel.png
description: "Trenne Umwandlungs-, Läuter- und Sudhausausbeute in einem Excel-Blatt, gleiche vorhergesagte gegen tatsächliche Stammwürze ab und diagnostiziere genau, wo dein Extrakt verloren geht."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
permalink: /de/2026/brewhouse-efficiency-yield-excel/
tags: [brewing-science, excel, efficiency, quality-control]
faq:
  - q: "Wie berechne ich die Sudhausausbeute in Excel?"
    a: "Sudhausausbeute = gesammelte Stammwürzepunkte ÷ maximal mögliche Punkte. In Excel: =((OG-1)*1000*gallons)/SUMPRODUCT(weights,PPGs). Für 5,5 Gallonen bei OG 1.050 gegen 370 potenzielle Punkte sind das (50×5,5)/370 ≈ 74 %."
  - q: "Was ist der Unterschied zwischen Umwandlungs- und Läuterausbeute?"
    a: "Die Umwandlungsausbeute ist, wie viel der Stärke des Getreides die Maische in Zucker verwandelte (typischerweise ~95 %). Die Läuterausbeute ist, wie viel dieses Zuckers du tatsächlich in die Pfanne gespült hast. Die Sudhausausbeute ist beides miteinander multipliziert, sodass eine niedrige Zahl dir sagt, welche Stufe du beheben musst."
  - q: "Warum kam meine Stammwürze niedrig heraus?"
    a: "Spalte den Fehlbetrag auf: Wenn die Umwandlungsausbeute niedrig ist, verdächtige Schrotung, Maische-pH oder Rastzeit; wenn die Läuterausbeute niedrig ist, verdächtige das Anschwänzen, die Treberabsorption oder Toträume. Vorhergesagte gegen tatsächliche Punkte in einem Blatt abzugleichen weist dich auf die richtige Ursache, statt dich raten zu lassen."
---

**Kurze Antwort: Ausbeute ist eine Division, auf drei Arten gemacht. Sudhausausbeute = gesammelte Punkte ÷ potenzielle Punkte; Umwandlungsausbeute = wie viel Stärke zu Zucker wurde; und Läuterausbeute = gesammelt ÷ umgewandelt. Weil Sudhaus = Umwandlung × Läuter, sagt dir ihr Aufspalten in Excel, ob eine niedrige OG ein Maische-Problem oder ein Anschwänz-Problem ist — statt dich raten zu lassen.**

Dies ist der Tiefgang zu den Anwendungsfällen 2 und 3 aus der Säule [20 Brauberechnungen in Excel]({{ '/de/2026/advanced-brewing-calculations-excel/' | relative_url }}): nicht nur die Ausbeute messen, sondern sie zerlegen, um das Leck zu finden. Es ist das praktische Pendant zur [Analytik der Sudhaus-Ausbeuteverluste]({{ '/de/2023/brewhouse-yield-loss-analytics/' | relative_url }}) und schließt direkt an [Maischeausbeute und Extraktausbeute]({{ '/de/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}) an.

## Schritt 1 — potenzielle und gesammelte Punkte

Der maximale Extrakt ist das Potenzial der Schüttung: das Gewicht jedes Malzes mal seinen Punkten pro Pfund pro Gallone. Der gesammelte Extrakt ist, was du tatsächlich bekommen hast, aus gemessener OG und Volumen:

`potential =SUMPRODUCT(weights,PPGs)`   (10 lb Pale × 37 = 370)
`collected =(OG-1)*1000*gallons`        (50 × 5,5 = 275)
`brewhouse_eff =collected/potential`     (275 / 370 = 74 %)

Diese 74 % sind die Schlagzeile — aber sie sagen nicht, *wohin* die fehlenden 26 % gegangen sind.

## Schritt 2 — Umwandlung von Läuter trennen

Die Umwandlungsausbeute ist, wie vollständig die Maische Stärke zu Zucker verwandelte (eine fein geschrotete, gut gerastete Maische mit korrektem pH erreicht ~95 %). Die Läuterausbeute ist, wie viel dieses Zuckers du herausgespült hast. Sie verketten sich:

`after_conversion =potential*conv_eff`   (370 × 0,95 = 351,5)
`lauter_eff =collected/after_conversion` (275 / 351,5 = 78 %)

Unsere 74 % Sudhausausbeute sind also 95 % Umwandlung × 78 % Läuter. Das Wasserfalldiagramm macht die beiden Verluste nebeneinander sichtbar.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 700 360" width="100%" style="max-width:700px;height:auto" role="img" aria-label="Ausbeute-Wasserfall: 370 potenzielle Punkte verlieren 18,5 an die Umwandlung und 76,5 an das Läutern, übrig bleiben 275 gesammelt">
<rect x="0" y="0" width="700" height="360" fill="#fdfbf7"/>
<text x="350" y="26" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Wohin der Extrakt geht (Stammwürzepunkte)</text>
<g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="40" x2="60" y2="320"/><line x1="60" y1="320" x2="660" y2="320"/></g>
<g stroke="#6b6258" stroke-width="1" stroke-dasharray="4 3">
<line x1="160" y1="61" x2="190" y2="61"/><line x1="280" y1="73.95" x2="310" y2="73.95"/>
<line x1="400" y1="73.95" x2="430" y2="73.95"/><line x1="520" y1="127.5" x2="550" y2="127.5"/>
</g>
<rect x="70" y="61" width="90" height="259" fill="#b45309"/>
<rect x="190" y="61" width="90" height="12.95" fill="#7a1f3d"/>
<rect x="310" y="73.95" width="90" height="246.05" fill="#a9743a"/>
<rect x="430" y="73.95" width="90" height="53.55" fill="#7a1f3d"/>
<rect x="550" y="127.5" width="90" height="192.5" fill="#b45309"/>
<g font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17" text-anchor="middle">
<text x="115" y="53">370</text><text x="235" y="55">−18,5</text><text x="355" y="66">351,5</text><text x="475" y="66">−76,5</text><text x="595" y="120">275</text>
</g>
<g font-family="sans-serif" font-size="11.5" fill="#6b6258" text-anchor="middle">
<text x="115" y="338">Potenzial</text><text x="235" y="338">Umwandlung</text><text x="355" y="338">Umgewandelt</text><text x="475" y="338">Läuterverlust</text><text x="595" y="338">Gesammelt</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Die Maische verliert kaum etwas (95 % Umwandlung); das eigentliche Leck ist das Läutern — Zucker, der in der Treberabsorption und im Totraum zurückbleibt.</figcaption>
</figure>

## Schritt 3 — abgleichen und diagnostizieren

Füge eine Zelle „vorhergesagte OG" aus deiner *erwarteten* Sudhausausbeute hinzu und vergleiche sie mit dem Ist:

`predicted_OG =1+(potential*expected_eff)/(gallons*1000)`

Wenn das Ist zu kurz kommt, sagt dir die Aufspaltung, wo du suchen sollst. **Niedrige Umwandlung** (die Maische machte weniger Zucker, als sie sollte) weist auf Schrotungsgröbe, Maische-pH, Rasttemperatur oder -zeit. **Niedriges Läutern** (du hast den Zucker gemacht, ihn aber nicht gesammelt) weist auf die Anschwänztechnik, die Treberabsorption oder den Totraum von Pfanne/Bottich — dieselben Verluste, die du im [Maischewasser-Rechner]({{ '/de/2026/mash-water-temperature-calculator-excel/' | relative_url }}) dimensioniert hast. Ein Blatt, und eine verfehlte OG wird zu einer benannten Ursache.

## Wo die Zerlegung unscharf wird

Zwei ehrliche Vorbehalte. Erstens **ist die Umwandlungsausbeute schwer direkt zu messen** ohne einen Feinschrot-Labortest oder eine Vorderwürze-Stammwürzemessung, sodass die meisten Brauer ~95 % annehmen und den Rest dem Läutern zuschreiben; wenn deine echte Umwandlung schlecht ist, wird das Blatt fälschlich das Anschwänzen beschuldigen. Eine Stammwürzemessung der Vorderwürze ist die billige Behebung — sie spaltet die beiden tatsächlich auf. Zweitens **sind PPG-Werte nominal** — Mälzer veröffentlichen das Potenzial unter Laborbedingungen, und dein tatsächlicher Extrakt hängt von der spezifischen Charge ab, also behandle die Ausbeutezahl als in-sich-konsistent statt als universelle Note. Verfolge sie über die Sude, und der *Trend* ist es, der eine driftende Mühle oder einen müden Läuterbottich auffängt.

## Das Fazit

Ausbeute ist eine Division, aber sie auf drei Arten zu machen — Sudhaus, Umwandlung, Läuter — verwandelt „meine OG war wieder niedrig" in „meine Läuterausbeute ist gesunken, prüf den Schrotspalt". Gleiche bei jedem Sud vorhergesagt gegen Ist ab, und das Blatt hört auf, eine Bewertungstafel zu sein, und wird zu einer Diagnose.

## Häufig gestellte Fragen

**Wie berechne ich die Sudhausausbeute in Excel?**
Sudhausausbeute = gesammelte Stammwürzepunkte ÷ maximal mögliche Punkte. In Excel: =((OG-1)*1000*gallons)/SUMPRODUCT(weights,PPGs). Für 5,5 Gallonen bei OG 1.050 gegen 370 potenzielle Punkte sind das (50×5,5)/370 ≈ 74 %.

**Was ist der Unterschied zwischen Umwandlungs- und Läuterausbeute?**
Die Umwandlungsausbeute ist, wie viel der Stärke des Getreides die Maische in Zucker verwandelte (typischerweise ~95 %). Die Läuterausbeute ist, wie viel dieses Zuckers du tatsächlich in die Pfanne gespült hast. Die Sudhausausbeute ist beides miteinander multipliziert, sodass eine niedrige Zahl dir sagt, welche Stufe du beheben musst.

**Warum kam meine Stammwürze niedrig heraus?**
Spalte den Fehlbetrag auf: Wenn die Umwandlungsausbeute niedrig ist, verdächtige Schrotung, Maische-pH oder Rastzeit; wenn die Läuterausbeute niedrig ist, verdächtige das Anschwänzen, die Treberabsorption oder Toträume. Vorhergesagte gegen tatsächliche Punkte in einem Blatt abzugleichen weist dich auf die richtige Ursache, statt dich raten zu lassen.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).*
