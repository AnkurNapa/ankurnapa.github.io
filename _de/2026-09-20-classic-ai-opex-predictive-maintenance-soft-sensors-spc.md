---
layout: post
lang: de
title: "Klassische KI für OpEx: Predictive Maintenance, Soft Sensors und Anomalieerkennung auf Basis von SPC"
image: /assets/og/classic-ai-opex-predictive-maintenance-soft-sensors-spc.png
description: "Teil 5 von KI für Operational Excellence in Getränkebetrieben. Das maschinelle Lernen, das sich in Getränkebetrieben bereits auszahlt: Predictive Maintenance an Füllern und Pasteuren, Soft Sensors für das, was sich inline nicht messen lässt, multivariate Anomalieerkennung auf Basis von SPC sowie Energie und Wasser pro Hektoliter gegen eine faire Baseline."
date: 2026-09-20 09:00:00 -0700
updated: 2026-09-20
permalink: /de/2026/classic-ai-opex-predictive-maintenance-soft-sensors-spc/
tags: [brewing-science, ai-opex, machine-learning, predictive-maintenance, operational-excellence]
faq:
  - q: "Welche Daten braucht man für Predictive Maintenance an einem Füller oder Pasteur?"
    a: "Zustandsdaten der Anlage, etwa Vibration, Motorstrom, Temperaturen und Drücke, in sinnvoller Auflösung in einem Historian gespeichert, dazu eine Instandhaltungshistorie aus dem CMMS, die festhält, was wann ausgefallen ist. Ohne Ausfallaufzeichnungen lässt sich abnormales Verhalten zwar erkennen, aber nicht lernen, wie weit im Voraus sich ein Ausfall ankündigt."
  - q: "Ersetzt maschinelles Lernen die statistische Prozesslenkung?"
    a: "Nein. SPC bleibt die einfache, prüfbare Baseline für einzelne Größen wie Füllmenge oder PU. Maschinelles Lernen ergänzt eine Ebene für Muster über viele Signale gleichzeitig, die keine einzelne Regelkarte zeigt. Wenn ein Modell SPC bei einem Problem nicht schlägt, nimm SPC."
  - q: "Wie verfolgt man Energie und Wasser pro Hektoliter fair?"
    a: "Den tatsächlichen Verbrauch mit einer Baseline vergleichen, die seine Treiber berücksichtigt: produziertes Volumen, Produkt- und Gebindemix sowie Außentemperatur. Eine einfache Regressions-Baseline, wie sie in Energiemanagementnormen verwendet wird, zeigt, ob eine Woche wirklich gut war oder nur ausgelastet. Die Lücke zwischen Ist und Baseline ist die Zahl, nach der man handelt."
---

**Kurze Antwort: Schon vor der generativen KI gab es in Getränkebetrieben reichlich maschinelles Lernen, das sich bezahlt gemacht hat, und das tut es bis heute. Predictive Maintenance überwacht Vibration und Stromaufnahme an Füllern, Pasteurpumpen und Transporteuren und warnt Tage vor einem Ausfall. Soft Sensors schätzen Werte, die sich inline nicht messen lassen, aus denen, die sich messen lassen. Multivariate Anomalieerkennung findet Muster über Dutzende Signale, die keine einzelne Regelkarte zeigt, mit SPC als Baseline darunter. Und Energie und Wasser pro Hektoliter sagen erst etwas aus, wenn man sie gegen eine Baseline stellt, die weiß, wie ausgelastet man war. Nichts davon ist neu. Alles hängt an den Datengrundlagen aus dem vorigen Beitrag.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Ein Schichtenmodell für klassische KI in einem Getränkebetrieb. Unten die Datenquellen: Historian, MES-Stillstandsprotokoll, CMMS und LIMS. Darüber die Baseline-Ebene aus Regeln und SPC: Verriegelungen, PU-Berechnung, Regelkarten für die Füllmenge. Darüber die Ebene des maschinellen Lernens mit vier Anwendungen: Predictive Maintenance an Füller und Pasteur, Soft Sensors, multivariate Anomalieerkennung sowie Energie- und Wasser-Baselines. Ganz oben handeln Menschen: Planer, Bediener und Ingenieure. Ein Hinweis besagt, dass maschinelles Lernen die Baseline-Ebene ergänzt und nie ersetzt.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">KLASSISCHE KI IM GETRÄNKEBETRIEB: ML AUF DER BASELINE</text>
<g font-family="sans-serif">
<rect x="40" y="50" width="920" height="44" rx="9" fill="#06483f"/>
<text x="500" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">MENSCHEN HANDELN: Planer, Bediener, Ingenieure</text>
<rect x="40" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="150" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">Predictive Maintenance</text>
<text x="150" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">Füller, Pasteur, Transporteure</text>
<rect x="273" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="383" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">Soft Sensors</text>
<text x="383" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">das Ungemessene schätzen</text>
<rect x="506" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="616" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">multivariate Anomalien</text>
<text x="616" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">viele Signale gleichzeitig</text>
<rect x="740" y="106" width="220" height="70" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="850" y="134" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">Energie &amp; Wasser</text>
<text x="850" y="153" text-anchor="middle" font-size="10.5" fill="#4a6b64">pro hl, gegen eine Baseline</text>
<rect x="40" y="188" width="920" height="50" rx="9" fill="#4db6a2"/>
<text x="500" y="210" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">BASELINE: Regeln und SPC</text>
<text x="500" y="228" text-anchor="middle" font-size="10.5" fill="#06483f">Verriegelungen &#183; PU-Berechnung &#183; Regelkarten für Füllmenge und CO2</text>
<rect x="40" y="250" width="920" height="44" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="500" y="277" text-anchor="middle" font-size="11.5" fill="#06483f">DATEN: Historian &#183; MES-Stillstandsprotokoll &#183; CMMS &#183; LIMS</text>
<text x="500" y="318" text-anchor="middle" font-size="11" fill="#4a6b64">maschinelles Lernen setzt eine Ebene auf die Baseline &#183; es ersetzt sie nie</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Vier Anwendungen des klassischen maschinellen Lernens, jede gestützt auf Regeln, SPC und verknüpfte Daten.</figcaption>
</figure>

Wenn im Jahr 2026 jemand "KI im Betrieb" hört, denkt er an einen Chatbot. Die KI, die in Getränkebetrieben im letzten Jahrzehnt Geld gespart hat, sieht überhaupt nicht wie ein Chatbot aus. Es ist ein Modell, das die Vibration an einer Pasteurpumpe beobachtet, eine Regression, die einen Laborwert vorhersagt, eine Karte, die um 4 Uhr morgens ein ungewöhnliches Muster markiert. Sie ist unauffällig, konkret und messbar, und genau deshalb funktioniert sie.

Dies ist der fünfte Beitrag der Serie. Der [vorige Beitrag]({{ '/de/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}) hat OEE, die sechs großen Verluste und die Frage behandelt, wo die Daten liegen. Dieser hier deckt die Sprosse des maschinellen Lernens auf der [KI-Leiter]({{ '/de/2026/what-is-ai-ladder-rules-to-agi-beverage-plant/' | relative_url }}) ab, mit vier Anwendungen, die sich verlässlich auszahlen.

## Predictive Maintenance an Füllern und Pasteuren

Störungen sind der erste der sechs großen Verluste und meist der schmerzhafteste, weil sie ohne Vorwarnung kommen und oft mitten im Lauf. Predictive Maintenance versucht, diese Vorwarnung zu liefern.

Die Daten haben zwei Seiten:

- **Zustandssignale** der Anlage: Vibration an Pumpen- und Motorlagern, Motorstrom, Temperaturen, Drücke, Zyklenzähler. Bei einem Tunnelpasteur sind die Umwälzpumpen, die Sprühbalken und die Wärmetauscher die üblichen Kandidaten. Bei einem Füller der Hauptantrieb, die Vakuumpumpe und die Ventile.
- **Ausfallhistorie** aus dem CMMS: was ausgefallen ist, wann, und was getan wurde.

Mit beidem kann ein Modell lernen, wie die Signale in den Tagen vor früheren Ausfällen aussahen, und dasselbe Muster frühzeitig melden. Ohne Ausfallhistorie lässt sich trotzdem etwas Sinnvolles tun: lernen, wie der Normalzustand aussieht, und Abweichungen davon melden. Das ist anomaliebasierte Instandhaltung, und dort sollten die meisten Betriebe anfangen, denn saubere Ausfallaufzeichnungen sind selten.

Der Nutzen liegt nicht in der Vorhersage selbst. Er liegt darin, aus einer ungeplanten Störung eine geplante Reparatur während eines vorgesehenen Stillstands zu machen. Die Verpackungsseite habe ich ausführlicher in [Predictive Maintenance für Füller und Verschließer]({{ '/de/2024/predictive-maintenance-filler-seamer/' | relative_url }}) behandelt.

## Soft Sensors: schätzen, was sich inline nicht messen lässt

Ein Soft Sensor schätzt einen Wert, der sich nur schwer oder langsam direkt messen lässt, aus Signalen, die sich leicht messen lassen.

Es hilft zu sehen, wo die Leiter beginnt. Pasteurisationseinheiten sind eine Berechnung, kein Modell. Nach der üblichen Konvention ergibt eine Minute bei 60 Grad C 1 PU (Pasteurisiereinheit), und jedes Grad darüber multipliziert die Rate mit etwa 1,393. Eine Minute bei 62 Grad ergibt also etwa 1,94 PU, zehn Minuten dort etwa 19,4. Das ist Physik und eine Regel, auf der untersten Sprosse, und dort sollte es auch bleiben.

Die Variante mit maschinellem Lernen kommt ins Spiel, wo die Physik unvollständig ist. Entscheidend sind die PU, die das Produkt im Gebinde tatsächlich erhalten hat. Gemessen wird die Sprühwassertemperatur in jeder Zone. Ein Soft Sensor, trainiert auf Daten aus Testläufen mit einem mitlaufenden Temperaturlogger, kann die Temperatur im Gebinde und damit die PU für jedes Gebinde schätzen, nicht nur für die Testgebinde. Nach ähnlichen Prinzipien lassen sich gelöstes CO2 oder Sauerstoffaufnahme zwischen Laborproben schätzen, oder der Restextrakt einer Gärung zwischen zwei Dichtemessungen.

Die Regel für Soft Sensors: Sie schätzen, die Referenzmethode bestätigt. Sie sagen dir, wo du hinschauen und wann du Proben ziehen sollst, nicht, was freigegeben wird.

## Anomalieerkennung auf Basis von SPC

SPC, aus dem vorigen Beitrag, ist hervorragend darin, jeweils eine Größe zu überwachen: Füllmenge, Kronkorkenverschluss, PU. Der blinde Fleck sind Muster, die sich erst über mehrere Signale zusammen zeigen. Ein leicht erhöhter Kesseldruck am Füller, eine leicht niedrige Produkttemperatur und ein leicht abweichender CO2-Wert können jeweils innerhalb ihrer Eingriffsgrenzen liegen und zusammen doch einen Prozess beschreiben, der sich verändert hat.

Multivariate Anomalieerkennung schließt diese Lücke. Die Methoden reichen von den altbewährten (Hauptkomponentenanalyse mit einer Hotelling-T-Quadrat-Karte, seit Jahrzehnten in der Prozessindustrie im Einsatz) bis zu neueren wie Isolation Forests oder Autoencodern. Sie lernen den normalen Zusammenhang zwischen vielen Signalen und melden, wenn er bricht.

Zwei praktische Regeln:

- **SPC als Baseline behalten.** Es ist einfach, prüfbar und genießt Vertrauen. Anomalieerkennung ist eine zweite Ebene, und wenn sie in deinem Prozess nichts findet, was SPC übersieht, brauchst du sie nicht.
- **Ein Alarmbudget festlegen.** Jede Anomaliemeldung kostet jemandes Aufmerksamkeit. Ein Modell, das zwanzig Dinge pro Schicht meldet, wird ab Mittwoch ignoriert. Stimme es auf eine Handvoll hochwertiger Meldungen ab, jede mit den Signalen, die sie ausgelöst haben.

## Energie und Wasser pro Hektoliter, gegen eine faire Baseline

Jeder Getränkebetrieb verfolgt Energie und Wasser pro Hektoliter, und viele finden die Zahlen frustrierend. Eine gute Woche sieht oft schlecht aus und eine schlechte gut, weil sich die Kennzahl mit Volumen, Produktmix, Gebindemix, Reinigungsplänen und dem Wetter bewegt.

Die Lösung ist eine Baseline, die diese Treiber kennt. Eine Regression etwa der wöchentlichen Wärmeenergie gegen das abgefüllte Volumen, den Anteil an Mehrwegglas (mit seiner Flaschenreinigungsmaschine) und die Außentemperatur liefert für jede Woche einen Erwartungswert. Die Zahl, auf die man schaut, ist die Lücke zwischen Ist und Erwartung, nicht die rohe Kennzahl. Energiemanagementnormen nutzen genau diesen Ansatz, und es ist maschinelles Lernen der bescheidensten Art.

Sobald die Baseline steht, greifen die Anomaliemethoden von oben: Eine Woche, eine Schicht oder ein CIP-Zyklus, der deutlich mehr verbraucht als erwartet, wird gemeldet und erklärt. Mein früherer Beitrag zur [CIP-Optimierung bei Wasser und Chemikalien]({{ '/de/2026/cip-optimisation-water-chemicals-ai/' | relative_url }}) führt die CIP-Seite weiter, und [Energie und Versorgung in der Brauerei]({{ '/de/2024/ai-brewery-energy-utilities-optimization/' | relative_url }}) behandelt die Versorgungsseite.

## Wo das an Grenzen stößt

**Ausfalldaten sind dünn.** Eine gut gewartete Pumpe fällt vielleicht einmal in mehreren Jahren aus. Das ist großartig für den Betrieb und schlecht für das Training eines Modells. Ähnliche Anlagen zusammenfassen, mit Anomalieerkennung beginnen und in die Vorhersage hineinwachsen.

**Sensoren driften und werden getauscht.** Ein Vibrationssensor, der bei einer Reparatur ersetzt wurde, kann wie eine plötzliche Veränderung der Anlage aussehen. Sensortausche als Ereignisse erfassen, sonst lernt das Modell den Instandhaltungskalender statt der Maschine.

**Soft Sensors altern.** Ein Soft Sensor, der vor einer Pasteurüberholung trainiert wurde, kann danach falsch liegen. Regelmäßig gegen die Referenzmethode prüfen und neu trainieren, wenn er driftet.

**Baselines können echte Verbesserungen verstecken.** Wird die Baseline jeden Monat neu trainiert, wird eine echte Einsparung langsam zum neuen Normalzustand und verschwindet aus dem Bericht. Die Baseline für einen festgelegten Zeitraum einfrieren, so wie es Energienormen tun.

## Das Fazit

Das maschinelle Lernen, das sich in Getränkebetrieben auszahlt, ist nicht glamourös. Es überwacht Pumpen, schätzt, was sich inline nicht messen lässt, erkennt Muster über Signale hinweg, die SPC allein nicht sieht, und bewertet Energie und Wasser gegen eine faire Baseline. Jede Anwendung steht auf Regeln und SPC darunter und darunter wiederum auf verknüpften, sauberen Daten. Wer das richtig macht, gibt den generativen und agentischen Ebenen in den nächsten beiden Beiträgen ein solides Fundament.

Als Nächstes: [generative KI für OpEx]({{ '/de/2026/genai-opex-shift-handover-sop-rag-root-cause/' | relative_url }}), wo der Text des Betriebs nutzbar wird. Speziell zu Stillständen an Verpackungslinien siehe [Stillstände an Verpackungslinien vorhersagen und OEE steigern]({{ '/de/2024/packaging-line-oee-downtime-prediction/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Häufig gestellte Fragen

**Welche Daten braucht man für Predictive Maintenance an einem Füller oder Pasteur?**
Zustandsdaten der Anlage, etwa Vibration, Motorstrom, Temperaturen und Drücke, in sinnvoller Auflösung in einem Historian gespeichert, dazu eine Instandhaltungshistorie aus dem CMMS, die festhält, was wann ausgefallen ist. Ohne Ausfallaufzeichnungen lässt sich abnormales Verhalten zwar erkennen, aber nicht lernen, wie weit im Voraus sich ein Ausfall ankündigt.

**Ersetzt maschinelles Lernen die statistische Prozesslenkung?**
Nein. SPC bleibt die einfache, prüfbare Baseline für einzelne Größen wie Füllmenge oder PU. Maschinelles Lernen ergänzt eine Ebene für Muster über viele Signale gleichzeitig, die keine einzelne Regelkarte zeigt. Wenn ein Modell SPC bei einem Problem nicht schlägt, nimm SPC.

**Wie verfolgt man Energie und Wasser pro Hektoliter fair?**
Den tatsächlichen Verbrauch mit einer Baseline vergleichen, die seine Treiber berücksichtigt: produziertes Volumen, Produkt- und Gebindemix sowie Außentemperatur. Eine einfache Regressions-Baseline, wie sie in Energiemanagementnormen verwendet wird, zeigt, ob eine Woche wirklich gut war oder nur ausgelastet. Die Lücke zwischen Ist und Baseline ist die Zahl, nach der man handelt.
