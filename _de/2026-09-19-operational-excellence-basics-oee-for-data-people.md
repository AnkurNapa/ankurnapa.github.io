---
layout: post
lang: de
title: "Grundlagen der Operational Excellence für Datenleute: OEE, die sechs großen Verluste, SPC und wo die Betriebsdaten liegen"
image: /assets/og/operational-excellence-basics-oee-for-data-people.png
description: "Teil 4 von KI für Operational Excellence in Getränkebetrieben. Vor jeder KI die Sprache des Betriebs: OEE mit einem durchgerechneten Beispiel an einer Abfülllinie, die sechs großen Verluste, TPM, die Verschwendungsarten des Lean, statistische Prozesslenkung und die ISA-95-Karte, wo die Daten tatsächlich liegen (Historian, MES, CMMS, LIMS, ERP)."
date: 2026-09-19 09:00:00 -0700
updated: 2026-09-19
permalink: /de/2026/operational-excellence-basics-oee-for-data-people/
tags: [brewing-science, ai-opex, operational-excellence, packaging, data-engineering]
faq:
  - q: "Wie berechnet man die OEE an einer Flaschenabfülllinie?"
    a: "OEE ist Verfügbarkeit mal Leistung mal Qualität. Verfügbarkeit ist die Laufzeit geteilt durch die geplante Produktionszeit. Leistung ist die tatsächliche Stückzahl geteilt durch das, was die Linie in dieser Laufzeit bei ihrer Idealrate hergestellt hätte. Qualität ist die Zahl der Gutteile geteilt durch die Gesamtstückzahl. Eine Linie mit 90 Prozent Verfügbarkeit, 83,3 Prozent Leistung und 98 Prozent Qualität hat eine OEE von 73,5 Prozent."
  - q: "Was sind die sechs großen Verluste der OEE?"
    a: "Ausfälle sowie Rüst- oder Umstellverluste mindern die Verfügbarkeit. Kurzstillstände und reduzierte Geschwindigkeit mindern die Leistung. Prozessfehler und Anlaufausschuss mindern die Qualität. Jede verlorene Minute einem dieser sechs zuzuordnen ist der erste Schritt jedes Verbesserungsprogramms und der erste Datensatz, den jedes KI-Projekt in einem Betrieb braucht."
  - q: "Wo liegen die Produktionsdaten in einem Getränkebetrieb?"
    a: "Sie sind über die ISA-95-Ebenen verteilt. Sensor- und SPS-Daten liegen auf den Steuerungsebenen und werden in einem Historian gespeichert. Fertigungsaufträge, Linienstillstände und Chargenprotokolle liegen meist in einem MES. Die Instandhaltungshistorie steht im CMMS, Laborergebnisse im LIMS und Aufträge, Bestände und Kosten im ERP. Die meisten KI-Projekte verbringen ihre ersten Monate damit, diese Systeme zusammenzuführen."
---

**Kurze Antwort: Operational Excellence in einem Getränkebetrieb beruht auf wenigen Ideen, die jeder Datenmensch kennen sollte, bevor er KI anfasst. Die OEE (Verfügbarkeit mal Leistung mal Qualität) macht aus einer Schicht eine Zahl und, nützlicher, eine Liste von Verlusten, die man benennen kann. An einer beispielhaften Abfülllinie mit 40.000 Flaschen pro Stunde ergeben 90 Prozent Verfügbarkeit, 83,3 Prozent Leistung und 98 Prozent Qualität eine OEE von 73,5 Prozent: 79.500 Flaschen, die in einer einzigen Schicht nicht hergestellt wurden. Die sechs großen Verluste sagen, wo sie geblieben sind. TPM, Lean und SPC sind die Methoden, mit denen Betriebe sie schon heute zurückholen. Und die Daten für all das sind über fünf Systeme verstreut, weshalb KI-Projekte in Betrieben überwiegend Datenprojekte sind.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Ein OEE-Wasserfall für eine beispielhafte Schicht an einer Abfülllinie. Die Linie könnte in 450 Minuten geplanter Zeit bei ihrer Idealrate von 40.000 pro Stunde 300.000 Flaschen herstellen. Der Verfügbarkeitsverlust von 45 Minuten Stillstand kostet 30.000 Flaschen. Der Leistungsverlust durch langsames Fahren und Kurzstillstände kostet 45.000 Flaschen. Der Qualitätsverlust kostet 4.500 ausgeschleuste Flaschen. Es bleiben 220.500 Gutflaschen, das sind 73,5 Prozent OEE. Die senkrechte Achse beginnt bei 200.000 Flaschen.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">EINE SCHICHT AN EINER ABFÜLLLINIE, IN FLASCHEN (BEISPIEL)</text>
<g font-family="sans-serif">
<line x1="60" y1="250" x2="960" y2="250" stroke="#4a6b64" stroke-width="1"/>
<text x="60" y="52" font-size="10" fill="#4a6b64">Achse beginnt bei 200.000 Flaschen</text>
<rect x="80" y="70" width="120" height="180" fill="#06483f"/>
<text x="140" y="64" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">300.000</text>
<rect x="260" y="70" width="120" height="54" fill="#4db6a2"/>
<text x="320" y="142" text-anchor="middle" font-size="12" fill="#06483f">&#8722;30.000</text>
<rect x="440" y="124" width="120" height="81" fill="#4db6a2"/>
<text x="500" y="223" text-anchor="middle" font-size="12" fill="#06483f">&#8722;45.000</text>
<rect x="620" y="205" width="120" height="8.1" fill="#ff4081"/>
<text x="680" y="232" text-anchor="middle" font-size="12" fill="#ff4081">&#8722;4.500</text>
<rect x="800" y="213.1" width="120" height="36.9" fill="#06483f"/>
<text x="860" y="205" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">220.500</text>
<g font-size="10.5" fill="#4a6b64" text-anchor="middle">
<text x="140" y="268">Idealausstoß in</text><text x="140" y="282">geplanter Zeit</text>
<text x="320" y="268">Verfügbarkeitsverlust</text><text x="320" y="282">45 min Stillstand</text>
<text x="500" y="268">Leistungsverlust</text><text x="500" y="282">langsam, Kurzstillstände</text>
<text x="680" y="268">Qualitätsverlust</text><text x="680" y="282">Ausschuss</text>
<text x="860" y="268">Gutflaschen</text><text x="860" y="282">73,5% OEE</text>
</g>
<rect x="40" y="298" width="920" height="32" rx="8" fill="#06483f"/>
<text x="500" y="319" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">V = 90% &#183; L = 83,3% &#183; Q = 98% &#183; OEE = 73,5% &#183; 79.500 FLASCHEN NICHT HERGESTELLT</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Beispielschicht. Der größte Balken ist oft die Leistung, der Verlust, den niemand aufschreibt, weil die Linie nie wirklich stand.</figcaption>
</figure>

Datenleute, die in einen Getränkebetrieb kommen, fragen gern nach "den Daten" und bauen dann ein Modell. Die Leute aus dem Betrieb sehen dabei meist mit höflicher Geduld zu, denn der Betrieb hat bereits eine Sprache für Verbesserung, und das Modell spricht sie nicht.

Dies ist der vierte Beitrag der Serie und die Brücke zwischen den KI-Grundlagen der ersten drei und den Anwendungen der letzten vier. Wer aus der Datenwelt kommt, findet hier das Vokabular des Betriebs. Wer aus dem Betrieb kommt, findet hier, wie man es dem eigenen Datenteam erklärt.

## OEE: eine Zahl, drei Fragen

Die Gesamtanlageneffektivität (Overall Equipment Effectiveness) stellt für eine Linie in einem Zeitraum drei Fragen:

- **Verfügbarkeit:** Wie viel der geplanten Laufzeit sind wir tatsächlich gelaufen?
- **Leistung:** Wie nah an der Idealrate sind wir gefahren, während wir liefen?
- **Qualität:** Wie viel von dem, was wir hergestellt haben, war gut?

Die OEE ist das Produkt der drei. Hier eine beispielhafte Schicht an einem Füller mit einer Nennleistung von 40.000 Flaschen pro Stunde:

```python
planned_min = 450 # 8 h shift less a 30 min planned break
stops_min = 20 + 15 + 10 # changeover overrun, filler jams, labeller faults
run_min = planned_min - stops_min # 405
ideal_per_min = 40_000 / 60 # 666.7 bottles a minute
total, good = 225_000, 220_500 # 4,500 rejects

availability = run_min / planned_min # 0.900
performance = total / (run_min * ideal_per_min) # 0.833
quality = good / total # 0.980
oee = availability * performance * quality # 0.735
```

73,5 Prozent. Für sich genommen ist die Zahl nicht sehr nützlich. Wichtig ist, dass dieselbe Rechnung in Flaschen zeigt, wohin die Verluste gegangen sind. Bei Idealrate hätte die Linie in 450 Minuten 300.000 Flaschen herstellen können. Sie hat 220.500 gute hergestellt. Von den 79.500 fehlenden gingen 30.000 durch Stillstände verloren, 45.000 durch langsames oder stockendes Fahren und 4.500 durch Ausschuss.

Der größte Balken ist die Leistung, und das ist häufig so. Eine Linie, die läuft, nur langsam, oder die jeweils für zwanzig Sekunden anhält, taucht selten in irgendwelchen Notizen auf. Genau dort liegen aber viele leichte Gewinne.

Oft hört man 85 Prozent als "Weltklasse". Nimm das als Faustregel, nicht als Standard. Die OEE hängt davon ab, wie man geplante Zeit und Idealrate definiert, und zwei Betriebe mit unterschiedlichen Definitionen können ihre Zahlen nicht vergleichen. Vergleiche eine Linie mit sich selbst über die Zeit.

## Die sechs großen Verluste

Total Productive Maintenance, kurz TPM, sortiert jede verlorene Minute in sechs Kategorien, zwei für jeden Teil der OEE:

| OEE-Faktor | Verlust | Beispiel an einer Getränkelinie |
|---|---|---|
| Verfügbarkeit | Ausfälle | Ventilausfall am Füller, Störung am Verschließer |
| Verfügbarkeit | Rüsten und Umstellen | Etiketten- oder Gebindewechsel, Sortenwechsel mit Spülung |
| Leistung | Kurzstillstände und Leerlauf | Flaschenstau am Einlaufstern, ein Sensor liest falsch |
| Leistung | Reduzierte Geschwindigkeit | Etikettiermaschine läuft langsam, weil sie bei voller Leistung Probleme macht |
| Qualität | Prozessfehler | Unterfüllungen, schiefe Etiketten, schlechte Verschlüsse |
| Qualität | Anlaufausschuss | Produktverlust zu Beginn eines Laufs oder nach einem Stillstand |

Diese Tabelle ist der wichtigste Datensatz in jedem KI-Projekt im Betrieb. Werden Linienstillstände mit sinnvollen Grundcodes erfasst, die sich diesen sechs zuordnen lassen, wird fast jede Idee im Rest dieser Serie möglich. Ist die Hälfte der Stillstände als "Sonstiges" codiert, ist es keine.

## TPM, Lean und SPC in je einem Absatz

**TPM** ist die Instandhaltungsseite der OpEx: Bediener, die ihre eigenen Anlagen grundlegend pflegen, geplante Instandhaltung auf Basis von Zustand und Historie und ein stetiger Fokus darauf, die sechs Verluste zu beseitigen. Hier gehört die vorausschauende Instandhaltung hin.

**Lean** zielt darauf, Verschwendung aus dem gesamten Fluss zu entfernen. Die klassische Liste der Verschwendungsarten (Transport, Bestände, Bewegung, Warten, Überproduktion, Überbearbeitung und Fehler, oft ergänzt um ungenutzte Fähigkeiten als achte) ist eine nützliche Brille für eine Abfüllhalle. Eine Palette leerer Dosen, die zwei Tage wartet, ist Bestand. Ein Bediener, der für jedes Chargenblatt zu einem weit entfernten Drucker läuft, ist Bewegung.

**SPC**, die statistische Prozesslenkung, beobachtet, ob sich ein Prozess normal verhält. Eine Regelkarte zeigt etwa das Füllvolumen über die Zeit, mit Grenzen, die aus der eigenen Streuung des Prozesses berechnet sind. Punkte außerhalb der Grenzen oder ungewöhnliche Punktfolgen innerhalb davon signalisieren, dass sich etwas verändert hat. SPC steuert die Getränkequalität seit Jahrzehnten still im Hintergrund, und sie ist die Messlatte, die jede KI-Anomalieerkennung schlagen muss.

## Wo die Daten liegen

Das ISA-95-Modell beschreibt die Ebenen eines Fertigungsbetriebs und ist eine gute Karte dafür, wo deine Daten liegen:

- **Ebenen 0 bis 2, der Prozess und seine Steuerung.** Sensoren, SPS, SCADA und HMIs. Die Messwerte werden meist in einem **Historian** gespeichert: Temperaturen, Drücke, Durchflüsse, Geschwindigkeiten und Zählerstände, Sekunde für Sekunde.
- **Ebene 3, Fertigungsbetrieb.** Das **MES** enthält Fertigungsaufträge, Linienzustände, Stillstandsgründe und Chargenprotokolle. Das **CMMS** enthält Instandhaltungsaufträge und die Anlagenhistorie. Das **LIMS** enthält Laborergebnisse.
- **Ebene 4, Unternehmensplanung.** Das **ERP** enthält Aufträge, Bestände, Kosten und den Produktionsplan.

Die meisten Betriebe haben alle fünf, und wenige haben sie verbunden. Die Stillstandsereignisse des Füllers liegen im MES, seine Schwingungsdaten im Historian, seine Reparaturhistorie im CMMS und seine Ausschussproben im LIMS. Um die Frage "Warum hat Linie 2 40 Minuten verloren?" aus dem [vorherigen Beitrag]({{ '/de/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}) zu beantworten, braucht man mindestens drei davon.

Das ist der ehrliche Grund, warum KI-Projekte in Betrieben länger dauern als erwartet. Das Modell braucht ein paar Wochen. Die Systeme verbinden, die Definitionen abstimmen und die Stillstandscodes bereinigen braucht ein paar Monate. Es ist dieselbe Lektion wie bei den [Datengrundlagen der Weinkellerei im Cellar Ledger]({{ '/de/2026/event-sourced-cellar-records-winery/' | relative_url }}): Das Datenmodell kommt zuerst.

## Wo es bricht

**Die OEE lässt sich schönrechnen.** Ändere, was als geplante Zeit zählt, oder senke die Idealrate, und die OEE steigt, ohne dass eine einzige Flasche mehr entsteht. Lege die Definitionen fest und veröffentliche sie.

**Stillstandscodes sind nur so gut wie die Person, die sie um 3 Uhr morgens eingibt.** Zu viele Codes, und die Bediener wählen den ersten. Zu wenige, und alles ist "Sonstiges". Automatische Stillstandserkennung aus der SPS plus eine kurze, gut gewählte Liste von Gründen funktioniert besser als beides.

**Durchschnitte verstecken die Verluste.** Eine Wochen-OEE von 75 Prozent kann eine furchtbare Schicht und mehrere gute verbergen. Schau dir die Verteilung an, nach Schicht, nach Produkt und nach Gebinde.

**SPC-Grenzen müssen aus einem stabilen Prozess stammen.** Berechnest du die Eingriffsgrenzen aus einer Phase, in der der Prozess außer Kontrolle war, erklärt die Regelkarte das Chaos zur Normalität.

## Das Fazit

Die OEE zerlegt eine Schicht in Verfügbarkeit, Leistung und Qualität und dann in Flaschen, die man zählen kann. Die sechs großen Verluste sagen, wo sie geblieben sind. TPM, Lean und SPC sind die Mittel, mit denen Betriebe schon immer gegengehalten haben, und die Daten dafür liegen in einem Historian, einem MES, einem CMMS, einem LIMS und einem ERP, die selten miteinander sprechen. Jede KI-Idee im Rest dieser Serie steht auf diesem Fundament. Stimmen die Stillstandscodes und sind die Systeme verbunden, wird der KI-Teil zum leichten Teil.

Als Nächstes: [klassische KI für OpEx]({{ '/de/2026/classic-ai-opex-predictive-maintenance-soft-sensors-spc/' | relative_url }}), vorausschauende Instandhaltung, Soft Sensors und Anomalieerkennung auf Basis von SPC. Für die Tableau-Sicht auf die Linien-OEE siehe [OEE der Abfülllinie in Tableau visualisieren]({{ '/de/2023/tableau-packaging-line-oee-dashboard/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Häufig gestellte Fragen

**Wie berechnet man die OEE an einer Flaschenabfülllinie?**
OEE ist Verfügbarkeit mal Leistung mal Qualität. Verfügbarkeit ist die Laufzeit geteilt durch die geplante Produktionszeit. Leistung ist die tatsächliche Stückzahl geteilt durch das, was die Linie in dieser Laufzeit bei ihrer Idealrate hergestellt hätte. Qualität ist die Zahl der Gutteile geteilt durch die Gesamtstückzahl. Eine Linie mit 90 Prozent Verfügbarkeit, 83,3 Prozent Leistung und 98 Prozent Qualität hat eine OEE von 73,5 Prozent.

**Was sind die sechs großen Verluste der OEE?**
Ausfälle sowie Rüst- oder Umstellverluste mindern die Verfügbarkeit. Kurzstillstände und reduzierte Geschwindigkeit mindern die Leistung. Prozessfehler und Anlaufausschuss mindern die Qualität. Jede verlorene Minute einem dieser sechs zuzuordnen ist der erste Schritt jedes Verbesserungsprogramms und der erste Datensatz, den jedes KI-Projekt in einem Betrieb braucht.

**Wo liegen die Produktionsdaten in einem Getränkebetrieb?**
Sie sind über die ISA-95-Ebenen verteilt. Sensor- und SPS-Daten liegen auf den Steuerungsebenen und werden in einem Historian gespeichert. Fertigungsaufträge, Linienstillstände und Chargenprotokolle liegen meist in einem MES. Die Instandhaltungshistorie steht im CMMS, Laborergebnisse im LIMS und Aufträge, Bestände und Kosten im ERP. Die meisten KI-Projekte verbringen ihre ersten Monate damit, diese Systeme zusammenzuführen.
