---
layout: post
lang: de
title: "Was agentische KI ist: Werkzeuge, die Schleife aus Planen, Handeln und Beobachten, MCP und fünf Autonomiestufen"
image: /assets/og/what-is-agentic-ai-tools-mcp-autonomy-levels.png
description: "Teil 3 von KI für Operational Excellence in Getränkebetrieben. Ein Agent ist ein Sprachmodell, das Werkzeuge nutzen und mehrere Schritte auf ein Ziel hin gehen kann. Wie die Schleife funktioniert, was Werkzeuge und MCP sind, was Gedächtnis bedeutet, und eine Autonomieleiter mit fünf Stufen (L0 bis L4), um zu entscheiden, wie viel ein Betrieb einen Agenten allein machen lassen sollte."
date: 2026-09-18 09:00:00 -0700
updated: 2026-09-18
permalink: /de/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/
tags: [brewing-science, ai-opex, ai-basics, agentic-ai, generative-ai]
faq:
  - q: "Was ist der Unterschied zwischen einem Chatbot und einem KI-Agenten?"
    a: "Ein Chatbot beantwortet eine Nachricht mit einer Antwort aus dem, was er bereits hat. Ein Agent bekommt ein Ziel und eine Reihe von Werkzeugen und arbeitet dann in einer Schleife: Er plant einen Schritt, ruft ein Werkzeug auf, etwa eine Datenbankabfrage, sieht sich das Ergebnis an und entscheidet über den nächsten Schritt, bis er eine Antwort hat oder einen Menschen braucht. Das Modell ist von derselben Art; erst die Werkzeuge und die Schleife machen es zum Agenten."
  - q: "Was ist MCP bei agentischer KI?"
    a: "MCP, das Model Context Protocol, ist ein offener Standard, um Sprachmodelle mit Werkzeugen und Datenquellen zu verbinden. Statt für jedes Modell und jedes System eine eigene Integration zu schreiben, baut man einmal einen MCP-Server, etwa für das Instandhaltungssystem, und jeder MCP-fähige Assistent kann dessen Werkzeuge nutzen. Der Server beschreibt, was jedes Werkzeug tut, welche Eingaben es braucht und was es zurückgibt."
  - q: "Wie viel Autonomie sollte ein KI-Agent in einem Getränkebetrieb haben?"
    a: "Die Autonomie sollte zu den Kosten eines Fehlers passen. Daten lesen und Entwürfe schreiben ist risikoarm, das dürfen Agenten frei tun. Alles, was einen Datensatz ändert, sollte der Agent vorschlagen und ein Mensch freigeben. Alles, was die Prozesssteuerung berührt, etwa einen Sollwert oder eine SPS, sollte vollständig außerhalb der Reichweite eines Agenten bleiben."
---

**Kurze Antwort: Ein Agent ist ein Sprachmodell mit Werkzeugen und einer Schleife. Du gibst ihm ein Ziel, etwa "finde heraus, warum Linie 2 letzte Nacht 40 Minuten verloren hat". Es plant einen Schritt, ruft ein Werkzeug auf (das Stillstandsprotokoll der Linie abfragen), sieht sich das Ergebnis an, entscheidet über den nächsten Schritt (im Instandhaltungssystem nach dieser Anlage sehen) und macht weiter, bis es eine Antwort hat oder einen Menschen braucht. MCP ist der Standardstecker, der Modelle mit diesen Werkzeugen verbindet. Gedächtnis lässt es Kontext zwischen Schritten und Sitzungen mitnehmen. Die wichtige Designfrage ist nicht, wie klug der Agent ist, sondern wie viel er allein tun darf. Ich nutze eine Leiter mit fünf Stufen, L0 bis L4, und in der Produktion sollten die meisten Agenten auf L1 oder L2 leben.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 360" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Links: die Agentenschleife. Ein Ziel speist einen Planungsschritt, dann Handeln durch Aufruf eines Werkzeugs, dann Beobachten des Ergebnisses, was zurück zum Planen führt, bis der Agent antwortet oder einen Menschen fragt. Als Werkzeuge sind das Stillstandsprotokoll, das Instandhaltungssystem und die SOP-Bibliothek aufgeführt, angebunden über MCP. Rechts: eine Autonomieleiter von L0 bis L4. L0, kein Agent. L1, liest und erklärt. L2, entwirft Aktionen, die ein Mensch freigibt. L3, handelt in engen Grenzen, ein Mensch kann ein Veto einlegen. L4, handelt allein, ein Mensch überwacht. L1 und L2 sind als Standard für die Produktion hervorgehoben, und ein Hinweis sagt, dass Schreibzugriffe auf die Prozesssteuerung nicht auf der Leiter stehen.">
<rect width="1000" height="360" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">WIE EIN AGENT ARBEITET UND WIE VIEL ER TUN DARF</text>
<g font-family="sans-serif">
<rect x="40" y="56" width="120" height="44" rx="9" fill="#06483f"/>
<text x="100" y="83" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">Ziel</text>
<rect x="200" y="56" width="120" height="44" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="83" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">planen</text>
<rect x="200" y="136" width="120" height="44" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="163" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">handeln</text>
<rect x="200" y="216" width="120" height="44" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="243" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">beobachten</text>
<line x1="160" y1="78" x2="200" y2="78" stroke="#4db6a2" stroke-width="2"/>
<line x1="260" y1="100" x2="260" y2="136" stroke="#4db6a2" stroke-width="2"/>
<line x1="260" y1="180" x2="260" y2="216" stroke="#4db6a2" stroke-width="2"/>
<path d="M200 238 C150 238 150 78 200 78" fill="none" stroke="#4db6a2" stroke-width="2"/>
<line x1="320" y1="158" x2="360" y2="158" stroke="#4db6a2" stroke-width="2"/>
<rect x="360" y="120" width="150" height="80" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.5"/>
<text x="435" y="140" text-anchor="middle" font-size="10.5" font-weight="700" fill="#00695c">Werkzeuge über MCP</text>
<text x="435" y="158" text-anchor="middle" font-size="10" fill="#4a6b64">Stillstandsprotokoll</text>
<text x="435" y="173" text-anchor="middle" font-size="10" fill="#4a6b64">Instandhaltungssystem</text>
<text x="435" y="188" text-anchor="middle" font-size="10" fill="#4a6b64">SOP-Bibliothek</text>
<text x="260" y="290" text-anchor="middle" font-size="10.5" fill="#4a6b64">Schleife bis zur Antwort, oder Mensch fragen</text>
<text x="755" y="58" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">AUTONOMIELEITER</text>
<rect x="560" y="70" width="390" height="36" rx="7" fill="#ffffff" stroke="#4a6b64" stroke-width="1.2"/>
<text x="575" y="93" font-size="11" fill="#4a6b64"><tspan font-weight="700">L4</tspan> handelt allein, ein Mensch überwacht</text>
<rect x="560" y="112" width="390" height="36" rx="7" fill="#ffffff" stroke="#4a6b64" stroke-width="1.2"/>
<text x="575" y="135" font-size="11" fill="#4a6b64"><tspan font-weight="700">L3</tspan> handelt in engen Grenzen, ein Mensch hat ein Veto</text>
<rect x="560" y="154" width="390" height="36" rx="7" fill="#00695c"/>
<text x="575" y="177" font-size="11" fill="#ffffff"><tspan font-weight="700">L2</tspan> entwirft Aktionen, ein Mensch gibt frei</text>
<rect x="560" y="196" width="390" height="36" rx="7" fill="#00695c"/>
<text x="575" y="219" font-size="11" fill="#ffffff"><tspan font-weight="700">L1</tspan> liest Daten und erklärt</text>
<rect x="560" y="238" width="390" height="36" rx="7" fill="#f0f6f5" stroke="#00695c" stroke-width="1.2"/>
<text x="575" y="261" font-size="11" fill="#06483f"><tspan font-weight="700">L0</tspan> kein Agent, Menschen erledigen es</text>
<text x="755" y="296" text-anchor="middle" font-size="10.5" font-weight="700" fill="#00695c">Standard in der Produktion: L1 und L2</text>
<rect x="40" y="312" width="910" height="36" rx="9" fill="#06483f"/>
<text x="495" y="335" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">SPS- UND SCADA-SCHREIBZUGRIFFE STEHEN NICHT AUF DIESER LEITER &#183; AGENTEN BERÜHREN NIE DIE PROZESSSTEUERUNG</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die Schleife macht es zum Agenten. Die Leiter macht es sicher, einen im Betrieb laufen zu lassen.</figcaption>
</figure>

Die Nachtschicht auf Linie 2 hat 40 Minuten verloren. In der Morgenbesprechung fragt jemand, warum. Normalerweise dauert die Antwort eine halbe Stunde: das Stillstandsprotokoll öffnen, die langen Stillstände finden, die Anlage im Instandhaltungssystem nachschlagen, prüfen, ob sie schon früher ausgefallen ist, die Schichtnotizen lesen und dann alles zusammensetzen.

Ein Chatbot kann das nicht. Er kann nur aus dem antworten, was du ihm einfügst. Ein **Agent** kann es, weil er jedes Teil selbst holen kann. Dieser Beitrag, der dritte der Serie, erklärt, wie. Der [vorherige Beitrag]({{ '/de/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}) hat behandelt, was ein Sprachmodell ist. Ein Agent ist dasselbe Modell mit zwei Ergänzungen: Werkzeugen und einer Schleife.

## Werkzeuge: was ein Agent erreichen kann

Ein **Werkzeug** ist eine Funktion, die das Modell aufrufen darf. Sie hat einen Namen, eine Beschreibung in einfacher Sprache, definierte Eingaben und eine definierte Ausgabe. Für einen Betrieb könnten nützliche Werkzeuge sein:

- `get_line_stops(line, start, end)` liefert jeden Stillstand mit Dauer, Störcode und Anlage
- `get_asset_history(asset_id)` liefert frühere Arbeitsaufträge und Ausfälle aus dem Instandhaltungssystem
- `search_sop(query)` liefert die relevanten SOP-Passagen mit Abschnittsnummern
- `get_shift_notes(line, shift)` liefert, was die Bediener aufgeschrieben haben

Das Modell führt nie direkt SQL gegen die Instandhaltungsdatenbank aus. Es fordert ein Werkzeug per Namen mit einigen Eingaben an, gewöhnliche Software führt eine getestete Abfrage aus, und das Ergebnis kommt als Text zurück. Diese Trennung ist die wichtigste Sicherheitseigenschaft eines Agenten. Das Modell entscheidet, **was** nachgeschlagen wird. Der Code entscheidet, **wie**, und was erlaubt ist.

## Die Schleife: planen, handeln, beobachten

Mit verfügbaren Werkzeugen arbeitet das Modell in einer Schleife:

1. **Planen.** Ausgehend vom Ziel und dem bisherigen Wissen den nächsten Schritt festlegen. "Zuerst die langen Stillstände auf Linie 2 von letzter Nacht finden."
2. **Handeln.** Ein Werkzeug aufrufen. `get_line_stops("L2", "22:00", "06:00")`.
3. **Beobachten.** Das Ergebnis lesen. Sechs Stillstände, vier davon am Leimwerk der Etikettiermaschine, insgesamt 31 Minuten.
4. **Wiederholen.** Den nächsten Schritt mit der neuen Information planen. "Die Instandhaltungshistorie des Leimwerks prüfen." Und so weiter.

Die Schleife endet, wenn der Agent genug für eine Antwort hat oder an etwas stößt, das er nicht allein entscheiden sollte, und an einen Menschen übergibt. Für die Frage zu Linie 2 könnte ein guter Agent so abschließen: Der größte Teil der 40 Minuten war das Leimwerk der Etikettiermaschine, vier Stillstände mit demselben Störcode; derselbe Fehler taucht letzten Monat in zwei Arbeitsaufträgen auf; die Schichtnotizen erwähnen die Leimtemperatur; der SOP-Abschnitt zum Anfahren des Leimwerks ist 6.3.

Das ist keine Magie. Es ist die halbstündige Handarbeit in einer Minute, mit jedem Schritt sichtbar.

## MCP: der Standardstecker

Bis vor Kurzem hieß ein Modell mit einem Werkzeug zu verbinden, für jedes Modell und jedes System eigenen Code zu schreiben. Das **Model Context Protocol (MCP)**, ein offener Standard, den Anthropic Ende 2024 veröffentlicht hat und der seitdem breit übernommen wurde, löst das. Man baut einmal einen MCP-Server, etwa für das Instandhaltungssystem. Er beschreibt seine Werkzeuge auf standardisierte Weise. Jeder Assistent, der MCP spricht, kann sie dann nutzen.

Für einen Betrieb liegt der praktische Nutzen in der Zuständigkeit. Das Instandhaltungsteam kann den MCP-Server für das Instandhaltungssystem verantworten und genau entscheiden, welche Werkzeuge er anbietet. Das Qualitätsteam kann den für das LIMS verantworten. Steht ein Werkzeug nicht auf dem Server, kann kein Agent es nutzen, egal welches Modell darüber sitzt.

## Gedächtnis: was der Agent mitnimmt

Sprachmodelle erinnern sich zwischen Gesprächen an nichts. Agenten ergänzen Gedächtnis in zwei Formen:

- **Arbeitsgedächtnis** ist das Kontextfenster während einer Aufgabe: das Ziel, jeder Werkzeugaufruf und jedes Ergebnis. Deshalb weiß der Agent bei Schritt vier, was er bei Schritt eins gefunden hat.
- **Langzeitgedächtnis** ist alles, was außerhalb des Modells gespeichert und später wieder gelesen wird: Notizen aus früheren Untersuchungen, eine Liste bekannter wiederkehrender Fehler, die Vorlieben eines Nutzers.

Langzeitgedächtnis ist mächtig und braucht dieselbe Sorgfalt wie jeder andere Datensatz. Wenn ein Agent sich an eine falsche Schlussfolgerung vom letzten Monat "erinnert", verwendet er sie selbstsicher wieder. Behandle gespeichertes Gedächtnis wie ein Dokument: datiert, mit Quelle und korrigierbar.

## Fünf Autonomiestufen

Die Frage, die im Betrieb am meisten zählt, ist nicht "wie klug ist der Agent?". Sie lautet "was darf er ohne Menschen tun?". Ich nutze eine einfache Leiter mit fünf Stufen:

- **L0: kein Agent.** Menschen erledigen die Aufgabe von Hand.
- **L1: liest und erklärt.** Der Agent kann Daten abfragen und eine Antwort oder Zusammenfassung schreiben. Er ändert nichts.
- **L2: entwirft, ein Mensch gibt frei.** Der Agent bereitet eine Aktion vor, etwa einen Arbeitsauftrag, einen Umstellplan oder eine E-Mail, und ein Mensch gibt sie frei, bevor etwas passiert.
- **L3: handelt in engen Grenzen, ein Mensch hat ein Veto.** Der Agent führt risikoarme Aktionen selbst aus, innerhalb fester Grenzen, mit Protokoll und einer Möglichkeit, sie rückgängig zu machen. Ein Beispiel ist die Nachbestellung eines Verbrauchsmaterials innerhalb eines vereinbarten Budgets.
- **L4: handelt allein, ein Mensch überwacht.** Der Agent führt eine Aufgabe von Anfang bis Ende aus, und Menschen prüfen seine Arbeit hinterher.

In der Produktion eines Getränkebetriebs sollten die meisten Agenten lange auf **L1 und L2** leben. Lesen und Entwerfen liefern den Großteil des Nutzens zu einem Bruchteil des Risikos. L3 ist nur für enge, umkehrbare, kostengünstige Aktionen. Und eine Kategorie steht ganz außerhalb der Leiter: Nichts, was ein Agent tut, sollte auf eine SPS, ein SCADA-System oder einen Prozesssollwert schreiben. Die Prozesssteuerung bleibt bei ingenieurmäßig ausgelegten Steuerungssystemen und Menschen. Beitrag 7 behandelt diese Leitplanken im Detail.

## Human in the Loop, richtig gemacht

"Human in the Loop" ist leicht gesagt und leicht schlecht gemacht. Ein Freigabeschritt, bei dem ein müder Planer am Schichtende vierzig Entwürfe durchklickt, ist keine Aufsicht. Es ist ein Stempel.

Ein paar Gewohnheiten machen es echt:

- Zu jedem Entwurf die Belege zeigen: welche Werkzeugaufrufe, welche Daten, welcher SOP-Abschnitt.
- Entwürfe wenige und konkret halten. Ein Agent, der einen guten Arbeitsauftrag entwirft, ist nützlicher als einer, der zehn mittelmäßige entwirft.
- Verfolgen, wie oft Menschen die Entwürfe des Agenten ändern oder ablehnen. Eine sinkende Änderungsquote ist gut. Eine Änderungsquote von null heißt meist, dass niemand liest.

## Wo es bricht

**Agenten können sich im Kreis drehen oder abschweifen.** Ein schlecht abgegrenzter Agent ruft Werkzeuge vielleicht immer wieder auf oder verfolgt eine irrelevante Spur. Setze Grenzen für Schritte, Zeit und Kosten, und mache "Ich brauche einen Menschen" zu einer akzeptablen Antwort.

**Werkzeugergebnisse können Anweisungen enthalten.** Ein Agent liest Text aus Protokollen, Notizen und Dokumenten. Steht darin "ignoriere die vorherigen Anweisungen", folgt ein nachlässiger Aufbau dem vielleicht. Das nennt man Prompt Injection. Behandle alles, was ein Werkzeug zurückgibt, als Daten, nie als Befehl, und halte schreibende Werkzeuge hinter Freigaben.

**Die Kette ist nur so gut wie die Daten.** Ein Agent, der ein Stillstandsprotokoll voller Störcodes "Sonstiges" liest, liefert eine selbstsichere Zusammenfassung von "Sonstiges". Agenten machen gute Daten schneller nutzbar. Schlechte Daten machen sie nicht besser.

**Autonomie schleicht sich ein.** Sobald ein Agent auf L2 gut funktioniert, entsteht Druck, die Freigabe zu überspringen. Lege die Stufe bewusst fest, nach den Kosten eines Fehlers, und schreib sie auf.

## Das Fazit

Ein Agent ist ein Sprachmodell mit Werkzeugen und einer Schleife. Er plant, handelt über ein Werkzeug, beobachtet das Ergebnis und wiederholt das, und so erledigt er das Zusammensuchen und Gegenprüfen, das früher eine halbe Stunde vom Morgen eines Schichtleiters gefressen hat. MCP ist der Standardweg, ihn an Betriebssysteme anzubinden, wobei der Verantwortliche jedes Systems entscheidet, welche Werkzeuge es gibt. Gedächtnis macht ihn über Schritte und Sitzungen hinweg nützlich. Autonomie ist eine Entscheidung, und in einem Getränkebetrieb ist der vernünftige Standard L1 und L2: lesen, erklären und entwerfen, mit einem Menschen, der freigibt, und einer Prozesssteuerung außer Reichweite.

Als Nächstes: [Grundlagen der Operational Excellence für Datenleute]({{ '/de/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}), denn ein Agent ist nur nützlich, wenn er die richtigen Verluste jagt. Ein durchgerechnetes Beispiel für MCP-Werkzeuge bei einem Rückruf in einer Weinkellerei steht in [Chargengenealogie als Graph]({{ '/de/2026/wine-lot-genealogy-graph-recall-agent/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist der Unterschied zwischen einem Chatbot und einem KI-Agenten?**
Ein Chatbot beantwortet eine Nachricht mit einer Antwort aus dem, was er bereits hat. Ein Agent bekommt ein Ziel und eine Reihe von Werkzeugen und arbeitet dann in einer Schleife: Er plant einen Schritt, ruft ein Werkzeug auf, etwa eine Datenbankabfrage, sieht sich das Ergebnis an und entscheidet über den nächsten Schritt, bis er eine Antwort hat oder einen Menschen braucht. Das Modell ist von derselben Art; erst die Werkzeuge und die Schleife machen es zum Agenten.

**Was ist MCP bei agentischer KI?**
MCP, das Model Context Protocol, ist ein offener Standard, um Sprachmodelle mit Werkzeugen und Datenquellen zu verbinden. Statt für jedes Modell und jedes System eine eigene Integration zu schreiben, baut man einmal einen MCP-Server, etwa für das Instandhaltungssystem, und jeder MCP-fähige Assistent kann dessen Werkzeuge nutzen. Der Server beschreibt, was jedes Werkzeug tut, welche Eingaben es braucht und was es zurückgibt.

**Wie viel Autonomie sollte ein KI-Agent in einem Getränkebetrieb haben?**
Die Autonomie sollte zu den Kosten eines Fehlers passen. Daten lesen und Entwürfe schreiben ist risikoarm, das dürfen Agenten frei tun. Alles, was einen Datensatz ändert, sollte der Agent vorschlagen und ein Mensch freigeben. Alles, was die Prozesssteuerung berührt, etwa einen Sollwert oder eine SPS, sollte vollständig außerhalb der Reichweite eines Agenten bleiben.
