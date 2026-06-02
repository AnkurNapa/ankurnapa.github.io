---
layout: post
lang: de
title: "Qualitätskontroll-Charts für das Brauen in Tableau"
image: /assets/og/tableau-qc-control-charts-brewing.png
description: "Erstelle statistische Prozessregelkarten für die Brauerei-QC in Tableau mit Referenzbändern, Kontrollgrenzen und Explain Data für außer Kontrolle geratene Punkte."
date: 2023-01-21
updated: 2023-01-21
permalink: /de/2023/tableau-qc-control-charts-brewing/
tags: [brewing-science, tableau, quality-control]
faq:
  - q: "Wie zeichne ich Kontrollgrenzen in ein Tableau-Diagramm ein?"
    a: "Berechne den Prozessmittelwert und die Standardabweichung als feste Werte aus einer stabilen Basisperiode und füge dann Referenzlinien oder ein Referenzband beim Mittelwert plus und minus drei Standardabweichungen hinzu. Tableau erzeugt keine Kontrollgrenzen für dich; du lieferst sie als berechnete Felder oder Konstanten."
  - q: "Welche Brauparameter eignen sich für eine SPC-Karte?"
    a: "Jeder messbare, wiederholte Parameter mit einem stabilen Zielwert: Stammwürze und Endvergärungsgrad, pH, Diacetyl, gelöster Sauerstoff und Abfüllfüllstände sind alle gute Kandidaten. Der Parameter braucht genug konsistente Historie, um sinnvolle Grenzen zu setzen."
  - q: "Bedeutet ein außer Kontrolle geratener Punkt, dass etwas kaputt ist?"
    a: "Es bedeutet, dass der Wert relativ zu deiner Basislinie statistisch ungewöhnlich ist, was eine Untersuchung rechtfertigt. Es ist ein Signal, kein Urteil — die Korrelation mit einer Ursache muss erst von Menschen festgestellt werden, die den Prozess kennen."
---

**Kurze Antwort: Eine Kontrollkarte in Tableau ist eine Zeitreihe mit ehrlichen, angeschraubten Grenzen.** Das Diagramm ist einfach; die Disziplin besteht darin, Grenzen aus einer wirklich stabilen Basislinie zu definieren und dem Drang zu widerstehen, auf gewöhnliches Rauschen zu reagieren.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für Qualitätskontroll-Charts für das Brauen in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Qualitätskontroll-Charts für das Brauen in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Kennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerlegen.</figcaption>
</figure>

## Das Datenmodell hinter einer Kontrollkarte
Die statistische Prozessregelung (SPC) erkennt, wenn ein Prozess über seine normale Streuung hinaus driftet. In einer Brauerei bedeutet das, Parameter wie Stammwürze, pH, Diacetyl oder Füllvolumen Probe für Probe zu verfolgen und zu fragen: Ist dieser Punkt Teil der normalen Streuung oder ein Signal?

Bevor irgendetwas gezeichnet wird, lege die Granularität fest. Eine Zeile pro Messung, getaggt mit dem Parameter, dem Sud oder der Füllung, dem Zeitstempel und idealerweise dem Probenahmepunkt. Wenn das sauber ist, sind deine berechneten "zuerst messen"-Felder einfach: der Prozessmittelwert und die Standardabweichung, berechnet aus einem gewählten Basisfenster — nicht aus allen Daten und schon gar nicht live neu berechnet, wenn neue Punkte eintreffen, denn dann verbreitert die heutige Drift still ihre eigenen Grenzen.

Das ist dieselbe QC-Denkweise, die anspruchsvollere Arbeit untermauert; für die KI-Erweiterung davon siehe [KI-Qualitätskontrolle beim Brauen]({{ '/de/2026/ai-quality-control-in-brewing/' | relative_url }}).

## Das Diagramm in Tableau bauen
Trage deinen Parameter auf einer kontinuierlichen Zeitachse auf. Füge dann die Grenzen hinzu. Der sauberste Ansatz sind berechnete Felder, die den Basismittelwert sowie die obere und untere Kontrollgrenze bei Mittelwert ± drei Standardabweichungen enthalten, dargestellt als **Referenzlinien** mit einem schattierten **Referenzband** dazwischen. Ein zweites Band bei ± zwei Standardabweichungen liefert dir Warnzonen, falls du Western-Electric-Regeln willst.

Verwende ein berechnetes Feld, um jeden Punkt außerhalb der Grenzen zu markieren, und eine Farbkodierung, damit diese Punkte rot herausstechen. Ein Parameter lässt den Nutzer zwischen QC-Variablen wechseln — heute Stammwürze, morgen Diacetyl — und nutzt dasselbe Arbeitsblatt wieder. Filter- und Hervorhebungsaktionen lassen einen Analysten auf einen außer Kontrolle geratenen Punkt klicken und in den dahinterliegenden Sud eintauchen.

Auf der KI-Ebene ist Tableaus **Explain Data** (jetzt Teil der Einstein-Copilot-Familie) hier wirklich praktisch: Wähle eine verdächtige Markierung aus und es liefert statistische Erklärungen — welche zugrunde liegenden Felder am meisten dazu beitragen, dass dieser Wert heraussticht. Es ist ein schneller Weg, Hypothesen zu generieren, und eine generative KI-Zusammenfassung kann daraus eine lesbare Notiz für die Schichtübergabe machen. Behandle beides als Ausgangspunkt für die Untersuchung, niemals als Schlussfolgerung.

## Wo es bricht
Kontrollkarten setzen eine stabile, gut charakterisierte Basislinie voraus. Wenn du Grenzen während einer chaotischen Inbetriebnahmephase oder quer über einen Rezeptwechsel setzt, sind die Grenzen bedeutungslos und das Diagramm wird entweder ständig falschen Alarm schlagen oder bei echten Problemen schweigen. Berechne Grenzen nur neu, wenn sich der Prozess wirklich ändert, und dokumentiere, wann du es getan hast.

Die zweite Falle ist, Korrelation mit Ursache zu verwechseln. Explain Data wird dir bereitwillig sagen, dass ein Feld mit einem Ausreißer "assoziiert" ist; das ist nicht dasselbe, wie dass dieses Feld ihn verursacht. Ein hoher Diacetyl-Wert, der mit einem bestimmten Tank korreliert, kann der Tank sein, oder die Hefegeneration, oder die Probenahmemethode — Tableau kann dir nicht sagen, welches. Und entscheidend: SPC sagt dir, *dass* sich etwas geändert hat, nicht, *ob das Bier gut ist*. Das braucht weiterhin das Labor und das Panel.

Schließlich ist ein außer Kontrolle geratener Punkt eine Aufforderung hinzuschauen, kein Fehlerbericht. Auf jedes Signal überzureagieren — "Tampering" — fügt Streuung hinzu, statt sie zu entfernen.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">REGELKREIS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Qualitätskontroll-Charts für das Brauen in Tableau</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Regler</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Aktuator</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Prozess</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">Rückkopplung</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen.</figcaption>
</figure>

## Das Fazit
Eine Tableau-Kontrollkarte ist eines der wertvollsten Dashboards mit dem geringsten Aufwand, das eine Brauerei bauen kann: eine saubere Zeitreihe, aus der Basislinie abgeleitete Grenzen als Referenzbänder und eine Markierung für Punkte, die sie durchbrechen. Explain Data beschleunigt die Suche nach dem Warum, aber die Basislinien-Disziplin und das menschliche Urteil sind das, was es vertrauenswürdig macht.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [KI-Qualitätskontrolle beim Brauen]({{ '/de/2026/ai-quality-control-in-brewing/' | relative_url }}).

## Häufig gestellte Fragen

**Wie zeichne ich Kontrollgrenzen in ein Tableau-Diagramm ein?**
Berechne den Prozessmittelwert und die Standardabweichung als feste Werte aus einer stabilen Basisperiode und füge dann Referenzlinien oder ein Referenzband beim Mittelwert plus und minus drei Standardabweichungen hinzu. Tableau erzeugt keine Kontrollgrenzen für dich; du lieferst sie als berechnete Felder oder Konstanten.

**Welche Brauparameter eignen sich für eine SPC-Karte?**
Jeder messbare, wiederholte Parameter mit einem stabilen Zielwert: Stammwürze und Endvergärungsgrad, pH, Diacetyl, gelöster Sauerstoff und Abfüllfüllstände sind alle gute Kandidaten. Der Parameter braucht genug konsistente Historie, um sinnvolle Grenzen zu setzen.

**Bedeutet ein außer Kontrolle geratener Punkt, dass etwas kaputt ist?**
Es bedeutet, dass der Wert relativ zu deiner Basislinie statistisch ungewöhnlich ist, was eine Untersuchung rechtfertigt. Es ist ein Signal, kein Urteil — die Korrelation mit einer Ursache muss erst von Menschen festgestellt werden, die den Prozess kennen.
