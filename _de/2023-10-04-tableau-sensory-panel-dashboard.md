---
layout: post
lang: de
title: "Ein Dashboard für Sensorik-Panel-Ergebnisse in Tableau"
image: /assets/og/tableau-sensory-panel-dashboard.png
description: "Baue ein Sensorik-Panel-Dashboard in Tableau: Attributbewertungen, Übereinstimmung und Varianz der Prüfer, Sortentreue-Radardiagramme und Pulse-Drift-Zusammenfassungen."
date: 2023-10-04
updated: 2023-10-04
permalink: /de/2023/tableau-sensory-panel-dashboard/
tags: [brewing-science, tableau, sensory]
faq:
  - q: "Wie zeige ich, ob die Prüfer übereinstimmen?"
    a: "Trage die Streuung der Bewertungen je Attribut auf — einen Boxplot oder die Standardabweichung über die Prüfer — neben dem Mittelwert. Eine breite Streuung bei einem Attribut bedeutet geringe Übereinstimmung und ein Panel, das bei diesem Deskriptor möglicherweise eine Neukalibrierung braucht."
  - q: "Was ist ein Sortentreue-Diagramm?"
    a: "Es vergleicht die mittleren Bewertungen des Panels für ein Bier mit dem Zielprofil für diesen Stil oder diese Marke, Attribut für Attribut. Ein Radar- oder Netzdiagramm, das Ist gegen Ziel überlagert, macht jede Abweichung vom beabsichtigten Charakter auf einen Blick deutlich."
  - q: "Kann KI das Verkostungspanel ersetzen?"
    a: "Nein. Tableau und KI können Paneldaten visualisieren, überwachen und zusammenfassen, und Instrumente können einige Verbindungen messen, aber keines verkostet das Bier. Das kalibrierte menschliche Panel ist das Messinstrument; das Dashboard meldet nur, was es erfasst hat."
---

**Kurze Antwort: Ein Sensorik-Dashboard macht die Ausgabe eines geschulten Panels lesbar, aber es ersetzt das Panel nie.** Tableau ist brillant darin, Attributbewertungen, Übereinstimmung und Sortentreue zu zeigen — solange du dich daran erinnerst, dass das Panel selbst das Instrument ist und die Daten nur so gut wie ihre Kalibrierung sind.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für ein Dashboard für Sensorik-Panel-Ergebnisse in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Ein Dashboard für Sensorik-Panel-Ergebnisse in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Schlüsselkennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerschneiden.</figcaption>
</figure>

## Das Panel als Instrument behandeln
Ein Sensorik-Panel ist ein Messinstrument aus Menschen. Wie jedes Instrument erzeugt es Daten — Attribut-Intensitätsbewertungen, Fehlaroma-Bewertungen, Gesamtakzeptanz — und wie jedes Instrument hat es Präzision und Drift. Ein Sensorik-Dashboard existiert, um sowohl das Bier als auch das Instrument zu überwachen.

Das Datenmodell ist eine Zeile pro Prüfer pro Probe pro Attribut pro Sitzung: wer verkostet hat, was, wann, welcher Deskriptor, welche Bewertung. Mit dieser Granularität ergeben sich deine „Erst messen"-Berechnungsfelder ganz natürlich — mittlere Bewertung je Attribut, Standardabweichung über die Prüfer (Übereinstimmung) und Abweichung je Prüfer vom Panelmittel (Kalibrierung). Bringe dieses Modell richtig hin, und du kannst das Bier *und* die Menschen, die es bewerten, analysieren.

Die ergänzende Frage, die Prüfer überhaupt kalibriert zu halten, wird in [KI-Kalibrierung der Sensorik-Panel-Verkoster]({{ '/de/2024/ai-sensory-panel-taster-calibration/' | relative_url }}) behandelt; dieser Beitrag setzt voraus, dass du die Daten hast und sie sehen willst.

## Die Ansichten aufbauen
Drei Ansichten tragen den Großteil des Werts.

Erstens, **Attributprofil**: Stelle die Panelmittel-Intensität für jeden Deskriptor als Balken oder Linie dar — Bitterkeit, fruchtige Ester, Diacetyl, Adstringenz —, sodass du den Charakter des Biers lesen kannst. Zweitens, **Übereinstimmung und Varianz**: ein Boxplot je Attribut oder ein Standardabweichungsmaß, das offenlegt, wo das Panel auseinandergeht. Enge Boxen bedeuten ein sicheres, kalibriertes Urteil; eine ausufernde Box bei „Diacetyl" markiert einen Deskriptor, für den das Panel keine gemeinsame Referenz hat. Drittens, **Sortentreue**: ein Radar-/Netzdiagramm, das das Panelmittel gegen das Marken- oder Stilziel überlagert, Attribut für Attribut, sodass jede Abweichung vom beabsichtigten Profil unverkennbar ist.

Füge eine Prüferansicht hinzu — die Abweichung jedes Verkosters vom Panelmittel über die Zeit —, um einen driftenden oder zu hart bewertenden Prüfer zu erkennen, bevor er die Ergebnisse verzerrt. Parameter lassen dich zwischen Produkten oder Sitzungen umschalten; Hervorhebungsaktionen lassen dich ein Attribut anklicken und es bis zu einzelnen Bewertungen zurückverfolgen.

Auf der KI-Seite kann **Tableau Pulse** die Sortentreue-Kennzahl je Marke überwachen und eine Zusammenfassung pushen, wenn ein Bier über Sitzungen hinweg beginnt, von seinem Zielprofil abzudriften — ein nützliches Frühwarnsignal, dass sich etwas im Prozess oder im Panel verändert hat. Eine Generative-KI-Schicht kann eine lesbare Sitzungszusammenfassung aus den Bewertungen entwerfen. Beide sind Berichtshilfen, keine Verkoster.

## Wo es scheitert
Die harte Grenze ist unverblümt: KI und Tableau verkosten nicht. Sie visualisieren Zahlen, die ein menschliches Panel erzeugt hat. Wenn das Panel falsch kalibriert ist, rendert das Dashboard die Fehlkalibrierung in schönem Detail und nennt es Daten. Ein Radardiagramm aus Unsinn ist immer noch Unsinn.

Sensorikdaten sind außerdem verrauscht und klein. Du arbeitest nicht mit Tausenden von Sensormesswerten, sondern mit einer Handvoll geschulter Gaumen und ein paar Sitzungen, sodass scheinbare „Drift" einfach ein Prüfer mit Erkältung oder eine knifflige Probe sein kann. Widerstehe der Überinterpretation kleiner Bewegungen; genau das ist die Art von Variation, die eine Kontrollkarten-Denkweise, von der QC-Seite geliehen, dir abzuwerten hilft. Und während Instrumente einige flüchtige Stoffe messen können, erfassen sie nicht die integrierte Wahrnehmung der Geschmacksbalance, die der ganze Sinn des Panels ist.

Behandle das Dashboard als Weg, dein Instrument ehrlich und deine Biere im Profil zu halten — nicht als Ersatz für die Verkostung selbst.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Das Modell sortiert jede Probe anhand ihrer gemessenen Merkmale in eine Klasse."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">KLASSIFIZIERUNG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Ein Dashboard für Sensorik-Panel-Ergebnisse in Tableau</text><rect x="120" y="120" width="150" height="120" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="195" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#00695c">Klasse A</text><circle cx="145" cy="145" r="6" fill="#00695c"/><circle cx="177" cy="145" r="6" fill="#00695c"/><circle cx="209" cy="145" r="6" fill="#00695c"/><rect x="330" y="120" width="150" height="120" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="405" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#2e9e7c">Klasse B</text><circle cx="355" cy="145" r="6" fill="#2e9e7c"/><circle cx="387" cy="145" r="6" fill="#2e9e7c"/><circle cx="419" cy="145" r="6" fill="#2e9e7c"/><circle cx="451" cy="145" r="6" fill="#2e9e7c"/><rect x="540" y="120" width="150" height="120" rx="8" fill="#f0f6f5" stroke="#06483f" stroke-width="1.5"/><text x="615" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Klasse C</text><circle cx="565" cy="145" r="6" fill="#06483f"/><circle cx="597" cy="145" r="6" fill="#06483f"/><circle cx="629" cy="145" r="6" fill="#06483f"/><circle cx="661" cy="145" r="6" fill="#06483f"/><circle cx="565" cy="175" r="6" fill="#06483f"/><text x="360" y="92" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">neue Probe → in die am besten passende Klasse sortiert</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Das Modell sortiert jede Probe anhand ihrer gemessenen Merkmale in eine Klasse.</figcaption>
</figure>

## Das Fazit
Ein Tableau-Sensorik-Dashboard verwandelt verstreute Panelbewertungen in drei klare Geschichten: wie das Bier schmeckt, wie sehr das Panel übereinstimmt und wie sortentreu das Bier ist. Pulse kann auf Drift achten und Generative KI kann den Bericht entwerfen, aber das kalibrierte menschliche Panel bleibt das Instrument. Das Dashboard berichtet über die Verkostung; es führt sie nicht durch.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [KI-Kalibrierung der Sensorik-Panel-Verkoster]({{ '/de/2024/ai-sensory-panel-taster-calibration/' | relative_url }}).

## Häufig gestellte Fragen

**Wie zeige ich, ob die Prüfer übereinstimmen?**
Trage die Streuung der Bewertungen je Attribut auf — einen Boxplot oder die Standardabweichung über die Prüfer — neben dem Mittelwert. Eine breite Streuung bei einem Attribut bedeutet geringe Übereinstimmung und ein Panel, das bei diesem Deskriptor möglicherweise eine Neukalibrierung braucht.

**Was ist ein Sortentreue-Diagramm?**
Es vergleicht die mittleren Bewertungen des Panels für ein Bier mit dem Zielprofil für diesen Stil oder diese Marke, Attribut für Attribut. Ein Radar- oder Netzdiagramm, das Ist gegen Ziel überlagert, macht jede Abweichung vom beabsichtigten Charakter auf einen Blick deutlich.

**Kann KI das Verkostungspanel ersetzen?**
Nein. Tableau und KI können Paneldaten visualisieren, überwachen und zusammenfassen, und Instrumente können einige Verbindungen messen, aber keines verkostet das Bier. Das kalibrierte menschliche Panel ist das Messinstrument; das Dashboard meldet nur, was es erfasst hat.
