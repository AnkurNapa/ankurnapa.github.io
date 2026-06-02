---
layout: post
lang: de
title: "Rechner für Maischewasser und -temperatur in Excel"
image: /assets/og/mash-water-temperature-calculator-excel.png
description: "Ermittle Einmaischtemperatur, Maische- und Nachgusswassermengen, Schüttungsaufnahme und den gesamten Wasserbedarf in einem Excel-Blatt — mit einer Wasserbilanz, die zeigt, wohin jeder Liter geht."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
permalink: /de/2026/mash-water-temperature-calculator-excel/
tags: [brewing-science, excel, mashing, water-volumes]
faq:
  - q: "Wie berechne ich die Einmaischwassertemperatur metrisch?"
    a: "Einmaischtemperatur Tw = (0,41/R)(T2 − T1) + T2, wobei R das Wasser-zu-Schüttung-Verhältnis in Litern pro Kilogramm ist, T1 die Schüttungstemperatur und T2 die Ziel-Maischetemperatur, alles in °C. In Excel: =(0.41/B2)*(B4-B3)+B4. Für imperiale Einheiten (qt/lb, °F) nutze die Konstante 0,2 statt 0,41."
  - q: "Wie viel Wasser nimmt die Schüttung in der Maische auf?"
    a: "Geschrotetes Malz hält rund 1 Liter pro Kilogramm zurück (etwa 0,125 Gallonen pro Pfund). Multipliziere dein Schüttungsgewicht mit diesem Wert, um das Wasser zu erhalten, das es nie in die Pfanne schafft, und addiere es dann zu deiner Nachguss-Berechnung, damit du dein Vorderwürzevolumen trotzdem triffst."
  - q: "Wie ermittle ich die Nachgusswassermenge?"
    a: "Gesamter Wasserbedarf = Vorderwürzevolumen + Schüttungsaufnahme + Toträume des Maischebottichs, wobei Vorderwürzevolumen = ins Gärgefäß + Trubverlust + Verdampfung. Das Nachgusswasser ist dann das Gesamtwasser minus Maischewasser. Baue es als kleine Kette von Additionen in Excel, und der Nachgusswert fällt automatisch heraus."
---

**Kurze Antwort: Die Maischewasserplanung ist eine Temperaturformel und eine Volumenkette. Einmaischtemperatur = (0,41/R)(T2 − T1) + T2 metrisch; und Gesamtwasser = Vorderwürze + Schüttungsaufnahme + Totraum, mit Nachguss = Gesamt − Maische. Lege diese in Excel an, und du triffst sowohl deine Maischetemperatur als auch dein Vorderwürzevolumen beim ersten Versuch, bei jedem Sud.**

Das baut die Anwendungsfälle 5, 7 und 8 aus dem Pfeiler [20 Brauberechnungen in Excel]({{ '/de/2026/advanced-brewing-calculations-excel/' | relative_url }}) zu einem einzigen Wasser-und-Temperatur-Planer aus. Die Volumina richtig zu treffen ist auch die halbe Miete bei der [Maische-Effizienz]({{ '/de/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}) — verfehle deine Volumina, und deine Würze verfehlt auch.

## Schritt 1 — Einmaischtemperatur

Kalte Schüttung zieht das Gemisch nach unten, also muss die Brauflüssigkeit heißer hinein als deine Zielrast. Mit R als Wasser-zu-Schüttung-Verhältnis (L/kg), T1 als Schüttungstemperatur und T2 als Ziel-Maischetemperatur (°C):

`=(0.41/B2)*(B4-B3)+B4`

Beispiel: R = 3,0 L/kg, Schüttung bei 18 °C, Ziel 66 °C → `(0.41/3.0)*(66-18)+66 = 72,6 °C`. (Du arbeitest in qt/lb und °F? Tausche die 0,41 gegen 0,2.)

## Schritt 2 — die Volumenkette

Baue die Volumina vom Gärgefäß rückwärts auf, denn das ist die Zahl, die dich tatsächlich interessiert. Setze jeden Verlust in seine eigene Zelle:

- **Maischewasser** = Schüttung × Verhältnis → `=B2*B3` (4,5 kg × 3,0 = 13,5 L)
- **Schüttungsaufnahme** = Schüttung × 1,0 L/kg → `=B2*1.0` (4,5 L — Wasser, das nie die Pfanne erreicht)
- **Vorderwürze** = ins Gärgefäß + Trubverlust + Verdampfung → `=B5+B6+B7` (19 + 2 + 4 = 25 L)
- **Gesamtwasser** = Vorderwürze + Aufnahme + Totraum → `=25+4.5+1.0` (30,5 L)
- **Nachgusswasser** = Gesamt − Maische → `=B_total-B_mash` (30,5 − 13,5 = 17 L)

Jetzt lässt das Ändern eines einzelnen Verlusts — ein längeres Kochen, ein tieferes Treberbett, eine andere Chargengröße — das ganze Blatt neu durchfließen, und dein Nachgussvolumen aktualisiert sich mit.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 200" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Wasserbilanz-Balken, der zeigt, wie sich 30,5 Liter auf Gärgefäß, Trub, Verdampfung, Schüttungsaufnahme und Totraum aufteilen">
<rect x="0" y="0" width="760" height="200" fill="#fdfbf7"/>
<text x="380" y="30" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">Wohin 30,5 L Brauwasser gehen</text>
<rect x="60" y="60" width="398.6" height="44" fill="#b45309"/>
<rect x="458.6" y="60" width="42" height="44" fill="#7a1f3d"/>
<rect x="500.6" y="60" width="83.9" height="44" fill="#a9743a"/>
<rect x="584.5" y="60" width="94.4" height="44" fill="#8a5a2b"/>
<rect x="678.9" y="60" width="21" height="44" fill="#6b6258"/>
<text x="259" y="88" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#fdfbf7">ins Gärgefäß 19 L</text>
<g font-family="sans-serif" font-size="12.5" fill="#1c1a17">
<rect x="60" y="135" width="14" height="14" fill="#b45309"/><text x="80" y="147">Ins Gärgefäß — 19 L</text>
<rect x="250" y="135" width="14" height="14" fill="#7a1f3d"/><text x="270" y="147">Trub-/Kühlerverlust — 2 L</text>
<rect x="470" y="135" width="14" height="14" fill="#a9743a"/><text x="490" y="147">Verdampfung — 4 L</text>
<rect x="60" y="160" width="14" height="14" fill="#8a5a2b"/><text x="80" y="172">Schüttungsaufnahme — 4,5 L</text>
<rect x="250" y="160" width="14" height="14" fill="#6b6258"/><text x="270" y="172">Totraum Maischebottich — 1 L</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Nur ~62 % des Wassers, das du erhitzt, landen als Bier. Der Rest wird aufgenommen, verdampft oder zurückgelassen — was genau der Grund ist, warum die Nachgussmenge es berücksichtigen muss.</figcaption>
</figure>

## Schritt 3 — Stufenmaischen und Abmaischen

Bei einer Stufenmaische braucht jeder Anstieg eine Zugabe kochenden Wassers (oder eine Dekoktion). Aufguss mit kochendem Wasser in Litern, mit G als Schüttung (kg), Wm als bereits in der Maische befindlichem Wasser (L), T in °C und Aufgusswasser bei 100 °C:

`=(T2-T1)*(0.41*G+Wm)/(100-T2)`

Stapele eine Zeile pro Stufe — Eiweißrast über Verzuckerung bis Abmaischen — und das Blatt sagt dir, wie viel kochendes Wasser jeder Sprung kostet und ob du den Bottich zum Überlaufen bringst, bevor du dort ankommst.

## Wo die Zahlen driften

Zwei ehrliche Vorbehalte. Erstens: **Aufnahme und Totraum sind Anlagenkonstanten, die du einmal messen musst** — 1 L/kg und der wahre Totraum deines Bottichs variieren je nach Schrot, Senkbodenbauweise und Schüttung; braue einmal, gleiche die tatsächliche Vorderwürze gegen das Blatt ab und korrigiere die Konstanten. Zweitens: **Verdampfung ist eine Rate, keine feste Größe** — sie hängt von der Pfannengeometrie, dem Deckel und davon ab, wie stark du kochst, daher wird eine von der Anlage eines anderen geliehene Zahl auf deiner falsch sein. Die Struktur des Blatts ist universell; die drei Konstanten (Aufnahme, Totraum, Verdampfungsrate) gehören allein dir, und ein einziger gemessener Sud kalibriert sie.

## Das Fazit

Eine Temperaturformel und eine fünfzeilige Volumenkette geben dir Einmaischtemperatur, Maischewasser, Nachgusswasser und Gesamtwasser in einem Blatt, das in dem Moment neu durchfließt, in dem du einen Verlust änderst. Kalibriere die drei Anlagenkonstanten einmal aus einem echten Sud, und du beendest sowohl das kalte Einmaischen als auch die „Wo ist mein Vorderwürzevolumen hin"-Überraschung.

## Häufig gestellte Fragen

**Wie berechne ich die Einmaischwassertemperatur metrisch?**
Einmaischtemperatur Tw = (0,41/R)(T2 − T1) + T2, wobei R das Wasser-zu-Schüttung-Verhältnis in Litern pro Kilogramm ist, T1 die Schüttungstemperatur und T2 die Ziel-Maischetemperatur, alles in °C. In Excel: =(0.41/B2)*(B4-B3)+B4. Für imperiale Einheiten (qt/lb, °F) nutze die Konstante 0,2 statt 0,41.

**Wie viel Wasser nimmt die Schüttung in der Maische auf?**
Geschrotetes Malz hält rund 1 Liter pro Kilogramm zurück (etwa 0,125 Gallonen pro Pfund). Multipliziere dein Schüttungsgewicht mit diesem Wert, um das Wasser zu erhalten, das es nie in die Pfanne schafft, und addiere es dann zu deiner Nachguss-Berechnung, damit du dein Vorderwürzevolumen trotzdem triffst.

**Wie ermittle ich die Nachgusswassermenge?**
Gesamter Wasserbedarf = Vorderwürzevolumen + Schüttungsaufnahme + Toträume des Maischebottichs, wobei Vorderwürzevolumen = ins Gärgefäß + Trubverlust + Verdampfung. Das Nachgusswasser ist dann das Gesamtwasser minus Maischewasser. Baue es als kleine Kette von Additionen in Excel, und der Nachgusswert fällt automatisch heraus.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).*
