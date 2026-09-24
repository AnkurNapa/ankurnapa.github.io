---
layout: post
lang: de
title: "Die Roadmap für KI in OpEx und wo sie bricht: Daten zuerst, Piloten nach Verlustwert, ehrlicher ROI und der AGI-Hype"
image: /assets/og/ai-opex-roadmap-where-it-breaks-agi-hype.png
description: "Teil 8 von KI für Operational Excellence in Getränkebetrieben. Wie man KI in einem Getränkebetrieb in die richtige Reihenfolge bringt: zuerst die Datengrundlagen, Piloten nach dem Wert des Verlusts ausgewählt, ROI gegen eine Baseline gemessen, Change Management in der Produktion und ein klarer Blick darauf, was das Gerede über AGI ändern sollte und was nicht. Schließt die Reihe ab."
date: 2026-09-23 09:00:00 -0700
updated: 2026-09-23
permalink: /de/2026/ai-opex-roadmap-where-it-breaks-agi-hype/
tags: [brewing-science, ai-opex, ai-strategy, operational-excellence, generative-ai]
faq:
  - q: "Wo sollte ein Getränkebetrieb mit KI anfangen?"
    a: "Bei den Datengrundlagen: verlässliche Stillstandscodes, MES, Historian, CMMS und LIMS über gemeinsame Anlagen- und Chargenschlüssel verbunden, und abgestimmte Definitionen für OEE und die sechs großen Verluste. Dann einen Piloten für den Verlust mit dem höchsten Wert auswählen, auf der niedrigsten KI-Stufe, die ihn lösen kann. Generative KI und Agenten kommen danach, auf denselben Daten."
  - q: "Wie misst man den ROI eines KI-Projekts im Werk?"
    a: "Gegen eine Baseline, zuerst in physischen Einheiten. Den Verlust vor dem Piloten erfassen, den Piloten durchführen und die Veränderung in Minuten, Flaschen, Kilowattstunden oder Litern messen, idealerweise gegen eine vergleichbare Linie ohne die Änderung. Erst am Ende in Geld umrechnen und alle Kosten mitzählen, einschließlich der Datenarbeit und der Zeit der Leute."
  - q: "Sollte ein Werk auf AGI warten, bevor es in KI investiert?"
    a: "Nein. AGI existiert nicht, niemand kann sagen, wann oder ob es sie geben wird, und jedes nützliche KI-Projekt hängt heute von sauberen Daten, verbundenen Systemen und klaren Freigaben ab. Genau das bräuchte auch jedes künftige System. Warten kostet die Verluste, die man in der Zwischenzeit hätte zurückholen können."
---

**Kurze Antwort: Die Reihenfolge zählt mehr als die Technologie. Erstens die Datengrundlagen in Ordnung bringen: Stillstandscodes, denen die Leute vertrauen, Historian, MES, CMMS und LIMS verbunden und eine abgestimmte Definition der OEE. Zweitens einen Piloten nach dem Wert des Verlusts auswählen, auf der niedrigsten KI-Stufe, die ihn lösen kann. Auf einer illustrativen Linie mit 300.000 Flaschen pro Schicht ist ein OEE-Punkt 3.000 Flaschen pro Schicht und bei drei Schichten rund 2,7 Millionen im Jahr. Drittens gegen eine Baseline in physischen Einheiten messen, bevor irgendjemand in Geld umrechnet. Viertens generative KI für die Texte des Werks ergänzen und Agenten, die entwerfen, nicht handeln. Und AGI als Nachricht zum Verfolgen behandeln, nicht als Grund zum Warten.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Eine Roadmap in vier Phasen für KI in einem Getränkebetrieb, illustrative Zeitplanung über etwa ein Jahr. Phase 1, Grundlagen: Stillstandscodes, verbundene Systeme, OEE-Definitionen. Phase 2, ein Pilot mit klassischer KI, ausgewählt nach Verlustwert, etwa vorausschauende Instandhaltung oder Anomalieerkennung. Phase 3, generative KI für Texte: Schichtübergaben, SOP-Antworten, Unterstützung bei der Ursachenanalyse. Phase 4, ein Agent auf Autonomiestufe 2, der Arbeitsaufträge und Umstellungspläne entwirft. Darunter läuft ein durchgehendes Band: gegen eine Baseline messen und die Produktion mitnehmen.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">EINE ROADMAP, DIE MIT DATEN BEGINNT UND MIT AGENTEN ENDET (ILLUSTRATIVE ZEITPLANUNG)</text>
<g font-family="sans-serif">
<rect x="40" y="60" width="215" height="150" rx="10" fill="#06483f"/>
<text x="147" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">1. Grundlagen</text>
<text x="147" y="108" text-anchor="middle" font-size="10.5" fill="#cfe6df">Monate 0 bis 3</text>
<text x="147" y="140" text-anchor="middle" font-size="10.5" fill="#ffffff">vertrauenswürdige Stillstandscodes</text>
<text x="147" y="160" text-anchor="middle" font-size="10.5" fill="#ffffff">MES, Historian, CMMS verbunden</text>
<text x="147" y="180" text-anchor="middle" font-size="10.5" fill="#ffffff">eine OEE-Definition</text>
<rect x="270" y="60" width="215" height="150" rx="10" fill="#00695c"/>
<text x="377" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">2. Pilot mit klassischer KI</text>
<text x="377" y="108" text-anchor="middle" font-size="10.5" fill="#cfe6df">Monate 3 bis 6</text>
<text x="377" y="140" text-anchor="middle" font-size="10.5" fill="#ffffff">nach Verlustwert ausgewählt</text>
<text x="377" y="160" text-anchor="middle" font-size="10.5" fill="#ffffff">vorausschauende Instandhaltung</text>
<text x="377" y="180" text-anchor="middle" font-size="10.5" fill="#ffffff">oder Anomalieerkennung auf SPC</text>
<rect x="500" y="60" width="215" height="150" rx="10" fill="#4db6a2"/>
<text x="607" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">3. GenAI für Texte</text>
<text x="607" y="108" text-anchor="middle" font-size="10.5" fill="#06483f">Monate 6 bis 9</text>
<text x="607" y="140" text-anchor="middle" font-size="10.5" fill="#06483f">Schichtübergaben</text>
<text x="607" y="160" text-anchor="middle" font-size="10.5" fill="#06483f">SOP-Antworten mit Quellen</text>
<text x="607" y="180" text-anchor="middle" font-size="10.5" fill="#06483f">Hilfe bei der Ursachenanalyse</text>
<rect x="730" y="60" width="230" height="150" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="845" y="88" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">4. Agent auf L2</text>
<text x="845" y="108" text-anchor="middle" font-size="10.5" fill="#4a6b64">Monate 9 bis 12</text>
<text x="845" y="140" text-anchor="middle" font-size="10.5" fill="#06483f">entwirft Arbeitsaufträge</text>
<text x="845" y="160" text-anchor="middle" font-size="10.5" fill="#06483f">entwirft Umstellungspläne</text>
<text x="845" y="180" text-anchor="middle" font-size="10.5" fill="#06483f">ein Mensch gibt frei</text>
<rect x="40" y="226" width="920" height="40" rx="10" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="500" y="251" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2e9e7c">DURCHGEHEND: GEGEN EINE BASELINE MESSEN &#183; DIE PRODUKTION MITNEHMEN</text>
<text x="500" y="298" text-anchor="middle" font-size="11" fill="#4a6b64">AGI ist keine Phase dieser Roadmap &#183; alles hier funktioniert ohne sie</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Illustrative Zeitplanung für einen Standort. Entscheidend ist die Reihenfolge: Jede Phase steht auf der vorherigen.</figcaption>
</figure>

Ich habe mehr KI-Projekte in Werken stocken als scheitern sehen. Selten sterben sie an einem schlechten Modell. Sie sterben im vierten Monat, wenn das Team feststellt, dass die Stillstandscodes unbrauchbar sind, das Instandhaltungssystem andere Anlagennamen verwendet als das MES und sich niemand einig ist, was als geplanter Stillstand zählt. Das Modell ist fertig und wartet auf Daten, die nie von selbst gekommen wären.

Dies ist der letzte Beitrag der Reihe **KI für Operational Excellence in Getränkebetrieben**. Die ersten sieben haben das Vokabular aufgebaut: die [KI-Leiter]({{ '/de/2026/what-is-ai-ladder-rules-to-agi-beverage-plant/' | relative_url }}), [LLMs]({{ '/de/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}), [Agenten]({{ '/de/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}), [OEE]({{ '/de/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}), [klassische KI]({{ '/de/2026/classic-ai-opex-predictive-maintenance-soft-sensors-spc/' | relative_url }}), [generative KI]({{ '/de/2026/genai-opex-shift-handover-sop-rag-root-cause/' | relative_url }}) und [agentische KI]({{ '/de/2026/agentic-ai-opex-oee-agent-cmms-guardrails/' | relative_url }}) in der Produktion. Dieser bringt sie in eine Reihenfolge.

## Phase 1: zuerst die Datengrundlagen

Nichts Späteres auf der Roadmap funktioniert ohne sie, also kommen sie zuerst, auch wenn sie sich am wenigsten spannend vor einem Vorstand präsentieren lassen:

- **Stillstandscodes, denen die Leute vertrauen.** Automatische Stillstandserkennung aus der SPS, dazu eine kurze Liste von Gründen, die auf die sechs großen Verluste abbilden. Mit den Bedienern testen, nicht nur mit den Ingenieuren.
- **Verbundene Systeme.** MES, Historian, CMMS und LIMS über gemeinsame Schlüssel verknüpft: dieselben Anlagen-IDs, dieselben Chargen- oder Auftragsnummern, dieselbe Uhr. Das ist meist die größte Aufgabe auf der Liste.
- **Eine Definition der OEE.** Was als geplante Zeit zählt, welche Idealleistung für jedes Produkt und Format gilt, schriftlich festgehalten und veröffentlicht.
- **Ein Ort für die Daten.** Ein Lakehouse oder Warehouse auf der IT-Seite, gespeist aus einer DMZ-Replik, in dem das Datenmodell aufgebaut werden kann, ohne das Steuerungsnetz anzufassen.

Es ist dieselbe Lektion wie bei der [Weingut-Datenarbeit im Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}): Definitionen und Datenmodell kommen vor jedem Assistenten.

## Phase 2: einen Piloten nach dem Wert des Verlusts auswählen

Sind die Verluste gemessen, wird die Wahl des Piloten zur Rechenaufgabe, nicht zur Frage der Begeisterung. Für jeden Kandidaten vier Fragen stellen:

1. **Wie viel ist er wert?** Verlorene Minuten oder Flaschen pro Woche, mal dem, was eine Flasche oder eine Minute für Sie wert ist.
2. **Sind die Daten bereit?** Gibt es das Signal, in der richtigen Frequenz, verknüpft mit dem Stillstandsprotokoll?
3. **Was ist die niedrigste Stufe, die ihn beheben kann?** Eine Regel, SPC, ein Modell, generative KI oder ein Agent.
4. **Was passiert, wenn es falsch ist?** Ein falscher Vorschlag bei einer Umstellung ist billig. Eine falsche Entscheidung am Pasteur ist es nicht.

Größenordnungen schärfen den Blick. Auf der illustrativen Füllerlinie aus Beitrag 4 liegt die Idealleistung bei 300.000 Flaschen pro Schicht. Ein OEE-Punkt sind 3.000 Flaschen pro Schicht. Bei drei Schichten an 300 Tagen sind das 2,7 Millionen Flaschen im Jahr. Mit Ihrem eigenen Deckungsbeitrag pro Flasche multipliziert, wissen Sie, was ein Punkt Verbesserung wert ist, bevor Sie irgendetwas ausgegeben haben.

Der Pilot ist meist klassische KI: vorausschauende Instandhaltung an der Anlage hinter dem größten Ausfallverlust oder Anomalieerkennung am Prozess hinter dem größten Qualitätsverlust. Er sollte eng gefasst sein: eine Linie, eine Anlagenfamilie, ein Verlust.

## Phase 3: generative KI für die Texte des Werks

Sobald eine verlässliche Datenschicht steht, hat generative KI etwas, worauf sie aufbauen kann. Schichtübergaben, entworfen aus Stillstandsprotokoll und Notizen, SOP-Antworten mit Quellenangaben, Unterstützung bei der Ursachenanalyse, die Vorschläge macht und nie Schlüsse zieht. Solche Anwendungen verbreiten sich meist schnell, weil die Leute die gesparte Zeit in jeder Schicht spüren. Sie legen auch verbleibende Datenprobleme schnell offen, denn eine Übergabe auf Basis schlechter Stillstandscodes liest sich offensichtlich falsch.

## Phase 4: ein Agent, der entwirft

Erst jetzt ergibt ein Agent Sinn: der OEE-Verlust-Agent aus Beitrag 7, auf Autonomiestufe 2, der replizierte Daten liest und Arbeitsaufträge und Umstellungspläne zur Freigabe durch einen Menschen entwirft, mit protokolliertem Tool-Aufruf und ohne Weg zur Prozesssteuerung. Er baut auf allem Vorherigen auf: den Stillstandscodes, um Verluste zu ordnen, den verbundenen Systemen, um einen Stillstand mit einer Anlage zu verknüpfen, und der Übergabe, um zu berichten, was er getan hat.

## Ehrlicher ROI

KI-Projekte in Werken neigen zu großzügiger Rechnung. Ein paar Gewohnheiten halten sie ehrlich:

- **Die Baseline messen, bevor es losgeht.** Vier bis acht Wochen des Verlusts, wie er ist, erfasst auf dieselbe Weise, wie er danach erfasst wird.
- **Zuerst in physischen Einheiten zählen.** Minuten, Flaschen, Kilowattstunden, Liter Wasser, Kilogramm verlorenes Produkt. Erst am Ende in Geld umrechnen, gemeinsam mit dem Controlling.
- **Wo möglich einen Vergleich nutzen.** Eine ähnliche Linie ohne den Piloten zeigt, wie viel der Veränderung von der Saison, dem Produktmix oder einem neuen Schichtleiter kam.
- **Alle Kosten mitzählen.** Lizenzen und Rechenleistung, ja, aber auch das Data Engineering, die Zeit der Bediener in Designsitzungen und die laufende Pflege der Modelle.
- **Dem ganzen Team Anerkennung geben.** Oft kommt der größte Gewinn aus der Bereinigung der Stillstandscodes in Phase 1, nicht aus dem Modell in Phase 2. Das auch so sagen.

## Change Management in der Produktion

Die Technik ist der einfache Teil. Menschen entscheiden, ob irgendetwas davon funktioniert:

- **Mit den Bedienern gestalten.** Sie wissen, welche Stillstandscodes Unsinn sind und welche Alarme alle ignorieren. Von der ersten Woche an einbeziehen.
- **Nie zum Schuldzuweisen verwenden.** Wird die Übergabezusammenfassung oder der Verlust-Agent zum Werkzeug, um Schuldige zu finden, werden die Daten innerhalb eines Monats schlechter.
- **Einen Verantwortlichen in der Produktion benennen.** Ein Produktionsmeister, nicht nur das Datenteam, verantwortet jedes Werkzeug und kann es abschalten.
- **Für die Fehlerbilder schulen.** Den Leuten beibringen, dass das Modell überzeugt falsch liegen kann und dass das Prüfen der Quelle oder der Belege zur Arbeit gehört.

## AGI-Hype und Wirklichkeit

Alle paar Monate gibt es eine Schlagzeile, AGI sei nahe, und jemand fragt in einer Werksbesprechung, ob es sich lohnt, jetzt zu investieren, oder ob man auf die Systeme warten sollte, die alles erledigen werden. Die ehrliche Antwort hat drei Teile.

AGI existiert heute nicht. Niemand kann verlässlich sagen, wann oder ob es sie geben wird. Und jedes nützliche System dieser Reihe, vom Schwingungsmodell bis zum Arbeitsauftrags-Agenten, hängt von sauberen Daten, verbundenen Systemen, klaren Definitionen und Freigabeprozessen ab. Eine künftige allgemeine Intelligenz bräuchte genau dieselben Dinge, um in einem Werk Vertrauen zu verdienen. Die Grundlagen sind nicht verschwendet, was auch immer passiert. Warten dagegen hat bekannte Kosten: jede Schicht mit Verlusten, die man hätte zurückholen können.

## Wo das bricht

**Phase 1 dauert länger als geplant.** Systeme verbinden und Codes bereinigen dauert immer länger. Die Zeit schützen und dem Druck widerstehen, direkt zur Demo zu springen.

**Piloten, die nie skalieren.** Ein Pilot auf einer Linie, der einen Data Scientist braucht, um am Laufen zu bleiben, erreicht die anderen fünf Linien nicht. Die zweite Linie von Anfang an in den Plan aufnehmen.

**ROI-Behauptungen, die sich nicht prüfen lassen.** Lassen sich die Einsparungen eines Anbieters nicht auf eine gemessene Veränderung gegenüber einer Baseline zurückführen, sind sie als Marketing zu behandeln.

**Autonomie schleicht sich ein.** Nach einem guten Jahr auf Stufe 2 wird Druck entstehen, den Agenten selbstständig handeln zu lassen. Das bewusst entscheiden, nach den Kosten eines Fehlers, und die Prozesssteuerung heraushalten.

## Das Fazit

KI für Operational Excellence in einem Getränkebetrieb ist eine Abfolge, kein Einkauf. Zuerst die Grundlagen, dann ein Pilot, ausgewählt nach dem Wert des Verlusts, auf der niedrigsten Stufe, die funktioniert, dann generative KI für die Texte des Werks, dann ein Agent, der zur Freigabe durch Menschen entwirft. Gegen eine Baseline in Flaschen und Minuten messen, die Produktion mitnehmen und nicht auf AGI warten. Die Verluste stehen heute an der Linie, und fast alles, was man braucht, um sie zurückzuholen, ebenfalls.

Damit schließt die Reihe. Die vollständige Liste steht auf der [Reihenseite]({{ '/series/ai-operational-excellence/' | relative_url }}). Für die Weingut-Version der Datengrundlagen siehe [The Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}); für Grundlagen in der Brennerei [AI Foundations for Distillers]({{ '/series/distilling-ai-foundations/' | relative_url }}); und für die Spirituosen- und Bierseite von GenAI und Data Engineering [The Still and the Model]({{ '/series/still-and-model/' | relative_url }}) und [The Brewer's Agent]({{ '/series/brewers-agent/' | relative_url }}).

## Häufig gestellte Fragen

**Wo sollte ein Getränkebetrieb mit KI anfangen?**
Bei den Datengrundlagen: verlässliche Stillstandscodes, MES, Historian, CMMS und LIMS über gemeinsame Anlagen- und Chargenschlüssel verbunden, und abgestimmte Definitionen für OEE und die sechs großen Verluste. Dann einen Piloten für den Verlust mit dem höchsten Wert auswählen, auf der niedrigsten KI-Stufe, die ihn lösen kann. Generative KI und Agenten kommen danach, auf denselben Daten.

**Wie misst man den ROI eines KI-Projekts im Werk?**
Gegen eine Baseline, zuerst in physischen Einheiten. Den Verlust vor dem Piloten erfassen, den Piloten durchführen und die Veränderung in Minuten, Flaschen, Kilowattstunden oder Litern messen, idealerweise gegen eine vergleichbare Linie ohne die Änderung. Erst am Ende in Geld umrechnen und alle Kosten mitzählen, einschließlich der Datenarbeit und der Zeit der Leute.

**Sollte ein Werk auf AGI warten, bevor es in KI investiert?**
Nein. AGI existiert nicht, niemand kann sagen, wann oder ob es sie geben wird, und jedes nützliche KI-Projekt hängt heute von sauberen Daten, verbundenen Systemen und klaren Freigaben ab. Genau das bräuchte auch jedes künftige System. Warten kostet die Verluste, die man in der Zwischenzeit hätte zurückholen können.
