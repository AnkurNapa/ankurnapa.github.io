---
layout: post
lang: de
title: "Einen IBU-Rezeptbaukasten in Excel bauen (Tinseth, Mehrfachgabe)"
image: /assets/og/ibu-recipe-builder-excel.png
description: "Ein Mehrfachgaben-IBU-Rechner in Excel: Tinseth-Ausnutzung je Hopfengabe, Gesamtbittere, das BU:GU-Balanceverhältnis, Hopfensubstitution und Skalierung auf eine Ziel-IBU."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
permalink: /de/2026/ibu-recipe-builder-excel/
tags: [brewing-science, excel, hops, recipe-formulation]
faq:
  - q: "Wie berechne ich die Gesamt-IBU für mehrere Hopfengaben in Excel?"
    a: "Gib jeder Gabe eine Zeile mit ihren Gramm, Alphasäure-% und Kochzeit, berechne die Tinseth-IBU je Zeile und summiere dann die Zeilen. Je Zeile: utilisation =(1.65*0.000125^(OG-1))*((1-EXP(-0.04*time))/4.15), und IBU =utilisation*((AA/100)*grams*1000)/litres. Die Gesamt-IBU ist einfach =SUM() der Zeilen."
  - q: "Was ist das BU:GU-Verhältnis?"
    a: "BU:GU ist die Gesamt-IBU geteilt durch die Stammwürze-Punkte ((OG−1)×1000). Es misst Bittere gegen Malzsüße, erfasst also die wahrgenommene Balance besser als IBU allein. Grob: unter 0,4 ist malzig, ~0,5 ausgewogen, 0,7–0,8 hopfig und 1,0+ ist IPA-Terrain. In Excel: =IBU/((OG-1)*1000)."
  - q: "Wie skaliere ich Hopfen, um eine Ziel-IBU zu treffen?"
    a: "Ermittle die berechnete IBU deines Rezepts und multipliziere dann jedes Hopfengewicht mit Ziel ÷ berechnet. Wenn das Blatt 33 IBU sagt und du 40 willst, skaliere mit 40/33 = 1,21, sodass eine 28-g-Gabe etwa 34 g wird. Die Verhältnisse zwischen den Gaben bleiben gleich, nur die Summen bewegen sich."
---

**Kurze Antwort: Ein IBU-Baukasten ist eine Tinseth-Formel, eine Tabelle von Hopfengaben hinabkopiert und summiert. Jede Zeile berechnet die Ausnutzung aus Kochzeit und Würze, multipliziert mit der Alphasäure-Konzentration und summiert sich zu deiner Bittere; teile durch die Würze-Punkte für das BU:GU-Balanceverhältnis und multipliziere die Gewichte mit Ziel÷berechnet, um eine Zahl zu treffen. Alles in einfachem Excel.**

Das erweitert die Anwendungsfälle 10 und 11 aus dem Pfeiler [20 Brauberechnungen in Excel]({{ '/de/2026/advanced-brewing-calculations-excel/' | relative_url }}) von einer einzelnen Gabe zu einem vollständigen Rezept mit Bitter-, Aroma-, Geruchs- und Whirlpool-Hopfen. Es ist die transparente Version dessen, was hinter [Hopfenbittere vorhersagen]({{ '/de/2023/predicting-hop-bitterness-ibu/' | relative_url }}) steckt.

## Schritt 1 — eine Zeile pro Gabe

Lege eine Tabelle an: Gramm, Alphasäure-%, Kochzeit. Setze das Chargenvolumen (Liter) und die OG in feste Zellen, die du mit `$` referenzieren kannst. Die Tinseth-IBU für jede Zeile sind zwei Faktoren — Ausnutzung (wie viel isomerisiert, aus Zeit und Würze) und Konzentration (wie viel Alphasäure du hinzugefügt hast):

`utilisation =(1.65*0.000125^($OG-1))*((1-EXP(-0.04*time))/4.15)`
`IBU =utilisation*((AA/100)*grams*1000)/$litres`

Kopiere es jede Zeile hinab. Dann summiere: `=SUM(IBU_column)`.

Durchgerechnetes Beispiel, 23 L bei OG 1,050:

| Gabe | g | AA% | min | IBU |
|---|---|---|---|---|
| Bitterhopfung | 28 | 6.4 | 60 | 18.0 |
| Aromahopfung | 28 | 6.4 | 15 | 8.9 |
| Whirlpool | 28 | 6.4 | 10* | 6.5 |
| **Gesamt** | | | | **33.4** |

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 620 340" width="100%" style="max-width:620px;height:auto" role="img" aria-label="Balkendiagramm des IBU-Beitrags je Hopfengabe: die 60-Minuten-Gabe dominiert">
<rect x="0" y="0" width="620" height="340" fill="#fdfbf7"/>
<text x="320" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#1c1a17">IBU-Beitrag je Gabe (jeweils dieselben 28 g)</text>
<g stroke="#1c1a17" stroke-width="1.5"><line x1="80" y1="40" x2="80" y2="300"/><line x1="80" y1="300" x2="560" y2="300"/></g>
<rect x="120" y="66" width="90" height="234" fill="#b45309"/>
<rect x="270" y="184.3" width="90" height="115.7" fill="#a9743a"/>
<rect x="420" y="215.5" width="90" height="84.5" fill="#8a5a2b"/>
<g font-family="sans-serif" font-size="13" font-weight="700" fill="#1c1a17" text-anchor="middle">
<text x="165" y="58">18.0</text><text x="315" y="176">8.9</text><text x="465" y="207">6.5</text>
</g>
<g font-family="sans-serif" font-size="12.5" fill="#6b6258" text-anchor="middle">
<text x="165" y="318">60 min</text><text x="315" y="318">15 min</text><text x="465" y="318">Whirlpool</text>
</g>
<text x="36" y="170" font-family="sans-serif" font-size="12" fill="#6b6258" text-anchor="middle" transform="rotate(-90 36 170)">IBU</text>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Identische Gewichte, sehr unterschiedliche Bittere: Die 60-Minuten-Gabe leistet mehr als die anderen beiden zusammen. *Whirlpool als 10-Minuten-Äquivalent modelliert — siehe den Vorbehalt.</figcaption>
</figure>

## Schritt 2 — das Balanceverhältnis und das Ziel

IBU allein sagt dir nicht, wie ein Bier schmeckt — 40 IBU sind aggressiv in einem 1,040er Bitter und mild in einem 1,080er Double IPA. Das BU:GU-Verhältnis behebt das, indem es Bittere durch Malz teilt:

`=total_IBU/(($OG-1)*1000)`

Unser Beispiel: `33.4/50 = 0,67` — ein deutlich hopfenbetontes Pale Ale. Unter 0,4 liest sich malzig, ~0,5 ausgewogen, 1,0+ ist IPA-Terrain.

Um ein Ziel zu treffen, skaliere: `scale_factor =target_IBU/calculated_IBU`, dann multipliziere jedes Gewicht damit. Willst du 40 aus 33,4? `40/33.4 = 1,20`, sodass jede Gabe um 20 % wächst und die Balance zwischen ihnen erhalten bleibt.

## Wo die Schätzung am weichsten ist

Zwei ehrliche Grenzen. Erstens: **Whirlpool- und Hopstand-Gaben sind die am wenigsten vorhersagbaren** — Tinseth wurde an rollende Kochungen angepasst, daher isomerisiert ein unterhalb des Siedepunkts liegender Whirlpool weiter, aber mit einer Rate, die die Formel nicht modelliert. Ihn als kurze „äquivalente Kochzeit" zu behandeln (hier 10 Minuten) ist ein brauchbarer Behelf, keine Physik; wenn du Hopfen 30 Minuten heiß stehen lässt, landet die echte Bittere irgendwo zwischen null und einer 10-Minuten-Kochung, und nur das Verkosten deiner eigenen Anlage kalibriert es. Zweitens: **Trockenhopfung trägt im Wesentlichen keine IBU bei**, obwohl sie intensiv bitter riecht — lass sie im Blatt bei null und vertraue deiner Nase, nicht der Zahl. Die Summe ist ein verlässlicher *relativer* Leitfaden und ein guter absoluter für Kochgaben; behandle späte und Trockenhopfen als Aroma, separat kalkuliert.

## Das Fazit

Kopiere eine Tinseth-Formel eine Tabelle von Gaben hinab, summiere sie, teile durch die Würze-Punkte, und du hast einen rezepttauglichen Bittererechner mit einem Balanceverhältnis und einem Ein-Zellen-Skalierer. Er trifft Kochgaben punktgenau; setze nur ein Sternchen bei Whirlpool und Trockenhopfen, wo die Chemie der Formel davonläuft.

## Häufig gestellte Fragen

**Wie berechne ich die Gesamt-IBU für mehrere Hopfengaben in Excel?**
Gib jeder Gabe eine Zeile mit ihren Gramm, Alphasäure-% und Kochzeit, berechne die Tinseth-IBU je Zeile und summiere dann die Zeilen. Je Zeile: utilisation =(1.65*0.000125^(OG-1))*((1-EXP(-0.04*time))/4.15), und IBU =utilisation*((AA/100)*grams*1000)/litres. Die Gesamt-IBU ist einfach =SUM() der Zeilen.

**Was ist das BU:GU-Verhältnis?**
BU:GU ist die Gesamt-IBU geteilt durch die Stammwürze-Punkte ((OG−1)×1000). Es misst Bittere gegen Malzsüße, erfasst also die wahrgenommene Balance besser als IBU allein. Grob: unter 0,4 ist malzig, ~0,5 ausgewogen, 0,7–0,8 hopfig und 1,0+ ist IPA-Terrain. In Excel: =IBU/((OG-1)*1000).

**Wie skaliere ich Hopfen, um eine Ziel-IBU zu treffen?**
Ermittle die berechnete IBU deines Rezepts und multipliziere dann jedes Hopfengewicht mit Ziel ÷ berechnet. Wenn das Blatt 33 IBU sagt und du 40 willst, skaliere mit 40/33 = 1,21, sodass eine 28-g-Gabe etwa 34 g wird. Die Verhältnisse zwischen den Gaben bleiben gleich, nur die Summen bewegen sich.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).*
