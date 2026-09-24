---
layout: post
lang: de
title: "Partie-Genealogie als Graph: rekursive Abfragen und ein Rückruf-Agent auf Basis von MCP-Tools"
image: /assets/og/wine-lot-genealogy-graph-recall-agent.png
description: "Teil 4 von The Cellar Ledger. Welche Flaschen enthalten Trauben aus Parzelle 7, und wie viel davon? Den Keller als Graph aus Partien und volumengewichteten Bewegungen modellieren, ihn mit einer rekursiven Abfrage verfolgen und einen GenAI-Agenten über MCP-Tools davorsetzen, die das Rechnen übernehmen, damit das Modell es nicht muss."
date: 2026-07-07 09:00:00 -0700
updated: 2026-07-07
permalink: /de/2026/wine-lot-genealogy-graph-recall-agent/
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, traceability]
faq:
  - q: "Wie verfolgt man einen Weinverschnitt bis zur Weinbergsparzelle zurück?"
    a: "Jede Partie wird als Knoten behandelt und jede Bewegung als Kante, die ein Volumen trägt. Wenn Wein in ein Gebinde fließt, ist die neue Zusammensetzung die volumengewichtete Mischung aus dem, was schon darin war, und dem, was hinzukam. Eine rekursive Abfrage läuft die Kanten rückwärts von einer Abfüllpartie zu ihren Quellen oder vorwärts von einer Weinbergsparzelle zu jeder Partie und Abfüllung, die sie enthält, und multipliziert dabei die Anteile."
  - q: "Braucht man für die Rückverfolgbarkeit im Weingut eine Graphdatenbank?"
    a: "Meist nicht. Ein Weingut hat Tausende Bewegungen im Jahr, nicht Milliarden, und eine rekursive Common Table Expression im Lakehouse oder Warehouse, das ohnehin läuft, bewältigt das problemlos. Eine Graphdatenbank lohnt sich erst bei vielen Standorten, sehr langen Fasshistorien oder wenn man Graphalgorithmen jenseits der Rückverfolgung braucht."
  - q: "Was bringt MCP einem Rückruf-Agenten im Weingut?"
    a: "MCP, das Model Context Protocol, ist ein Standardweg, einem Sprachmodell eine Reihe von Tools zu geben. Für einen Rückruf-Agenten sind das trace_back, trace_forward und bottling_status, die jeweils eine getestete Abfrage ausführen. Das Modell entscheidet, welches Tool es aufruft, und schreibt das Ergebnis auf, aber jeder Anteil und jedes Volumen stammt aus dem Tool, nicht aus der eigenen Arithmetik des Modells."
---

**Kurze Antwort: Wenn ein Traubenlieferant anruft und sagt, dass Parzelle 7 ein Rückstandsproblem haben könnte, lautet die Frage, welche Flaschen Trauben aus Parzelle 7 enthalten und zu welchem Anteil. Ist der Keller als Graph aus Partien und volumengewichteten Bewegungen erfasst, ist das eine rekursive Abfrage, die in Sekunden läuft. Setzt man über ein paar MCP-Tools (Rückverfolgung, Vorwärtsverfolgung, Abfüllstatus) einen GenAI-Agenten davor, kann ein Kellermeister die Frage in normaler Sprache stellen und bekommt eine Antwort, in der jeder Prozentwert von getestetem Code berechnet wurde. Der Agent schreibt das Rückruf-Memo. Über den Rückruf entscheidet er nie.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Ein Genealogie-Graph der Partien. Trauben aus Parzelle 7 gehen mit 10.000 Litern in Tank A, zu 100 Prozent Parzelle 7. 3.000 Liter aus Tank A fließen in Tank B, der bereits 7.000 Liter aus Parzelle 9 enthielt, sodass Tank B zu 30 Prozent aus Parzelle 7 besteht. 5.000 Liter aus Tank B werden mit 5.000 Litern aus Tank C, der aus Parzelle 12 stammt, zur Abfüllpartie D verschnitten, die zu 15 Prozent aus Parzelle 7 besteht. Die Vorwärtsverfolgung ab Parzelle 7 erreicht daher Abfüllpartie D mit 15 Prozent.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">VORWÄRTSVERFOLGUNG AB PARZELLE 7: ANTEILE MULTIPLIZIEREN SICH ENTLANG DER KANTEN</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="150" height="56" rx="9" fill="#06483f"/>
<text x="105" y="85" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">Parzelle 7</text>
<text x="105" y="103" text-anchor="middle" font-size="10.5" fill="#cfe6df">vom Lieferanten gemeldet</text>
<rect x="30" y="160" width="150" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="105" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Parzelle 9</text>
<rect x="30" y="250" width="150" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="105" y="275" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Parzelle 12</text>
<rect x="250" y="60" width="170" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="335" y="84" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Tank A &#183; 10.000 L</text>
<text x="335" y="102" text-anchor="middle" font-size="10.5" fill="#00695c">100% Parzelle 7</text>
<rect x="490" y="140" width="190" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="585" y="164" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Tank B &#183; 10.000 L</text>
<text x="585" y="182" text-anchor="middle" font-size="10.5" fill="#00695c">30% Parzelle 7</text>
<rect x="490" y="250" width="190" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="585" y="274" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Tank C &#183; 5.000 L</text>
<text x="585" y="292" text-anchor="middle" font-size="10.5" fill="#4a6b64">0% Parzelle 7</text>
<rect x="770" y="190" width="200" height="66" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="870" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Abfüllpartie D</text>
<text x="870" y="238" text-anchor="middle" font-size="14" font-weight="700" fill="#ff4081">15% Parzelle 7</text>
<line x1="180" y1="88" x2="250" y2="88" stroke="#4db6a2" stroke-width="2"/>
<line x1="420" y1="100" x2="490" y2="155" stroke="#4db6a2" stroke-width="2"/>
<text x="470" y="118" text-anchor="middle" font-size="10" fill="#4a6b64">3.000 L</text>
<line x1="180" y1="188" x2="490" y2="170" stroke="#4db6a2" stroke-width="2"/>
<text x="330" y="172" text-anchor="middle" font-size="10" fill="#4a6b64">7.000 L</text>
<line x1="180" y1="278" x2="490" y2="278" stroke="#4db6a2" stroke-width="2"/>
<line x1="680" y1="175" x2="770" y2="215" stroke="#4db6a2" stroke-width="2"/>
<text x="728" y="185" text-anchor="middle" font-size="10" fill="#4a6b64">5.000 L</text>
<line x1="680" y1="278" x2="770" y2="235" stroke="#4db6a2" stroke-width="2"/>
<text x="728" y="272" text-anchor="middle" font-size="10" fill="#4a6b64">5.000 L</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">3.000 von 10.000 Litern machen Tank B zu 30% Parzelle 7. Die Hälfte von Partie D stammt aus B, also ist D zu 15% Parzelle 7. Die Rechnung ist einfach. Sie für einen ganzen Keller von Hand zu machen, ist es nicht.</figcaption>
</figure>

Es ist ein Dienstag im September, und ein Traubenlieferant ruft an. Eine Spritzung auf Parzelle 7 könnte innerhalb der Wartezeit erfolgt sein. Noch weiß niemand, ob das relevant ist, aber das Weingut muss heute wissen, wohin diese Trauben gegangen sind. In welche Tanks? In welche Verschnitte? In welche Abfüllungen, und welche davon sind schon ausgeliefert?

In den meisten Weingütern wird daraus eine Zwei-Tage-Aufgabe mit einem Stapel Arbeitsaufträgen und einer Tabelle. Das muss nicht sein. Das [Bewegungsjournal]({{ '/de/2026/event-sourced-cellar-records-winery/' | relative_url }}) aus einem früheren Teil dieser Serie enthält bereits jede Antwort. Man muss es nur als Graph lesen.

## Der Keller ist bereits ein Graph

Jede Weinpartie ist ein Knoten. Jede Bewegung ist eine Kante mit einem Volumen daran. Trauben aus einer Parzelle gehen in einen Tank. Ein Teil dieses Tanks geht in einen anderen Tank, der schon etwas anderes enthält. Zwei Tanks werden zu einem dritten verschnitten, der abgefüllt wird.

Wenn Wein in ein Gebinde fließt, ist die neue Zusammensetzung ein volumengewichteter Mittelwert:

> neuer Anteil = (vorhandenes Volumen x sein Anteil + zufließendes Volumen x sein Anteil) / Gesamtvolumen

In der Abbildung enthielt Tank B 7.000 Liter aus Parzelle 9 und erhielt 3.000 Liter aus Parzelle 7, also besteht er zu 30% aus Parzelle 7. Abfüllpartie D nimmt 5.000 Liter aus B und 5.000 aus C, also besteht sie zu 15% aus Parzelle 7. Das ist der ganze Mechanismus. Er muss nur auf jede Bewegung in der richtigen Reihenfolge angewendet werden, und genau dafür gibt es Computer, und genau das machen Menschen unter Zeitdruck falsch.

## Die rekursive Abfrage

Dafür braucht man keine Graphdatenbank. Ein Weingut hat Tausende Bewegungen im Jahr, und eine rekursive Common Table Expression im Warehouse, das ohnehin läuft, arbeitet sie problemlos ab.

```sql
WITH RECURSIVE forward AS (
  SELECT to_lot AS lot_id, share AS source_share, 1 AS depth
  FROM   lot_edges
  WHERE  from_lot = 'BLOCK-07-2025'
  UNION ALL
  SELECT e.to_lot, f.source_share * e.share, f.depth + 1
  FROM   forward f
  JOIN   lot_edges e ON e.from_lot = f.lot_id
  WHERE  f.depth < 30
)
SELECT lot_id, SUM(source_share) AS block7_share
FROM   forward
GROUP  BY lot_id;
```

Dabei ist `share` an jeder Kante der Anteil der Zielpartie, der aus der Quellpartie stammt, einmal in der Silver-Schicht aus den Volumina des Journals berechnet. Läuft man die Kanten vorwärts von einer Parzelle und multipliziert die Anteile unterwegs, erhält man jede nachgelagerte Partie und wie viel von der Parzelle sie enthält. Läuft man sie rückwärts von einer Abfüllpartie, erhält man ihre vollständige Rezeptur bis hinunter zu den Weinbergsparzellen.

Die Tiefenbegrenzung ist keine Dekoration. Fassprogramme mit jahrelangem Auffüllen erzeugen lange Ketten, und eine versehentliche Schleife durch einen Eingabefehler läuft sonst, bis das Warehouse aufgibt.

## Dieselbe Abfrage belegt das Etikett

Genealogie ist nicht nur etwas für schlechte Tage. Dieselbe Zusammensetzung beantwortet die Frage, die das Marketing jeden Jahrgang stellt: Darf dieser Verschnitt das gewünschte Etikett tragen?

Die Schwellenwerte hängen vom Markt ab. In der EU müssen für die Angabe einer Rebsorte oder eines Jahrgangs auf dem Etikett in der Regel mindestens 85% des Weins die Bedingung erfüllen. In den USA braucht ein Rebsortenname in den meisten Fällen 75%, eine AVA 85% und eine Jahrgangsangabe 95%, wenn eine AVA genannt ist, sonst 85%. Genau diese Prozentwerte liefert eine Rückverfolgung: den Anteil der Partie nach Rebsorte, Jahrgang und Herkunft. Legt man die Regeln der eigenen Märkte in einer kleinen Tabelle ab, kann eine Prüfung schon vor dem Druck der Etiketten sagen, ob ein Verschnitt sie erfüllt und mit welchem Abstand.

## Ein GenAI-Agent davor

Ein Kellermeister sollte keine rekursive CTE schreiben müssen, während der Lieferant noch am Telefon ist. Das ist eine gute Aufgabe für einen Agenten, sofern er so gebaut ist, dass er die Zahlen nicht falsch machen kann.

Das Model Context Protocol (MCP) ist 2026 der Standardweg, einem Sprachmodell eine Reihe von Tools zu geben. Für die Rückverfolgbarkeit reichen drei Tools:

- **`trace_forward(source, min_share)`** liefert jede Partie und Abfüllung, die eine Parzelle oder Partie enthält, mit Anteilen oberhalb eines Schwellenwerts.
- **`trace_back(lot)`** liefert die vollständige Zusammensetzung einer Partie nach Parzelle, Rebsorte und Jahrgang.
- **`bottling_status(lot)`** liefert produzierte, vorrätige und ausgelieferte Kartons und an wen.

Jedes Tool ist eine getestete Abfrage. Die Aufgabe des Agenten ist, die Frage zu verstehen, die richtigen Tools in der richtigen Reihenfolge aufzurufen und aufzuschreiben, was sie zurückgeben. Auf die Frage "Wohin ist Parzelle 7 gegangen, und ist davon schon etwas ausgeliefert?" ruft er `trace_forward` auf, dann `bottling_status` für jede gefundene Abfüllung, und erstellt ein kurzes Memo: zwei Tanks noch im Keller, eine Abfüllung mit 15% Parzelle 7, davon 400 Kartons an drei Händler ausgeliefert, und die Liste dieser Händler.

Ein paar Regeln halten das vertrauenswürdig:

1. **Nur lesende Tools.** Der Agent kann schauen, aber keinen Wein bewegen und keine Datensätze ändern. Sperren und Rückrufe sind Handlungen, die ein Mensch vornimmt.
2. **Zahlen kommen nur aus der Tool-Ausgabe.** Das Memo zitiert die Anteile und Kartonzahlen, die die Tools geliefert haben. Rechnet das Modell selbst eine Zahl aus, ist das ein Fehler im Prompt.
3. **Mit Probe-Rückrufen testen.** Viele Regelwerke für Lebensmittel und Getränke verlangen, einen Schritt zurück und einen Schritt vorwärts verfolgen zu können, und gute Weingüter üben Probe-Rückrufe. Die letzten Übungen werden zu einem Testsatz mit bekannten Antworten, gegen den der Agent bei jeder Änderung läuft.

Der Unterschied ist die Zeit. Eine Rückruffrage, die früher zwei Tage Papierarbeit bedeutete, dauert ein paar Minuten, und der Kellermeister verbringt diese Minuten damit, die Antwort zu prüfen, statt sie zusammenzusuchen.

## Wo das an Grenzen stößt

**Die Zusammensetzung setzt perfekte Durchmischung voraus.** Die Rechnung behandelt einen Tank als homogen. Ein Tank, der aufgefüllt, aber nicht gerührt wurde, oder aus dem gezogen wurde, bevor ein Verschnitt durchmischt war, ist es nicht. Für Rückrufzwecke vom ungünstigsten Fall ausgehen und mit großzügigen Schwellenwerten verfolgen.

**Auffüllen erzeugt Staub.** Jahre des Auffüllens von Fässern aus gemischten Quellen hinterlassen Tausende winziger Anteile: 0,2% hiervon, 0,05% davon. Einen Schwellenwert festlegen, unterhalb dessen eine Quelle gemeldet, aber nicht weiterverfolgt wird, und ihn im Memo angeben.

**Der Graph ist nur so gut wie das Journal.** Ein nicht erfasster Transfer unterbricht die Kette, und die Verfolgung behauptet dann, Parzelle 7 sei bei Tank B stehen geblieben, obwohl das nicht stimmt. Die Korrekturbuchungen aus der [Verlustkarte]({{ '/de/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}) sind ein gutes Frühwarnsignal dafür, wo die Kette schwach ist.

**Der Agent darf nicht entscheiden.** Ob Ware gesperrt, Händler informiert oder zurückgerufen wird, ist ein Urteil mit rechtlichem und wirtschaftlichem Gewicht. Der Agent trägt die Fakten schnell zusammen. Die Entscheidung unterschreibt ein Mensch.

## Das Fazit

Jeder Verschnitt ist ein Graph, ob das Weingut ihn so erfasst oder nicht. Die Bewegungen mit ihren Volumina speichern, die Zusammensetzung einmal in der Pipeline berechnen, und eine rekursive Abfrage beantwortet die schwierigste Frage, die ein Lieferant stellen kann. Verpackt man diese Abfragen als MCP-Tools, kann ein GenAI-Agent sie in normaler Sprache beantworten, wobei jeder Prozentwert aus getestetem Code stammt. Das Modell macht die Antwort schnell erreichbar. Das Journal macht sie richtig.

Als Nächstes in der Serie: [Verbrauchsteuererklärungen als Datenverträge]({{ '/de/2026/wine-excise-returns-data-contracts-genai/' | relative_url }}), wo dasselbe Journal mit dem Finanzamt abgestimmt werden muss. Verschneiden aus der anderen Richtung, also Komponenten so zu wählen, dass ein Ziel erreicht wird, behandelt [KI für die Optimierung von Weinverschnitten]({{ '/de/2024/ai-wine-blending-optimization/' | relative_url }}). Die vollständige Liste steht auf der [Seite zur Serie Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}).

## Häufig gestellte Fragen

**Wie verfolgt man einen Weinverschnitt bis zur Weinbergsparzelle zurück?**
Jede Partie wird als Knoten behandelt und jede Bewegung als Kante, die ein Volumen trägt. Wenn Wein in ein Gebinde fließt, ist die neue Zusammensetzung die volumengewichtete Mischung aus dem, was schon darin war, und dem, was hinzukam. Eine rekursive Abfrage läuft die Kanten rückwärts von einer Abfüllpartie zu ihren Quellen oder vorwärts von einer Weinbergsparzelle zu jeder Partie und Abfüllung, die sie enthält, und multipliziert dabei die Anteile.

**Braucht man für die Rückverfolgbarkeit im Weingut eine Graphdatenbank?**
Meist nicht. Ein Weingut hat Tausende Bewegungen im Jahr, nicht Milliarden, und eine rekursive Common Table Expression im Lakehouse oder Warehouse, das ohnehin läuft, bewältigt das problemlos. Eine Graphdatenbank lohnt sich erst bei vielen Standorten, sehr langen Fasshistorien oder wenn man Graphalgorithmen jenseits der Rückverfolgung braucht.

**Was bringt MCP einem Rückruf-Agenten im Weingut?**
MCP, das Model Context Protocol, ist ein Standardweg, einem Sprachmodell eine Reihe von Tools zu geben. Für einen Rückruf-Agenten sind das trace_back, trace_forward und bottling_status, die jeweils eine getestete Abfrage ausführen. Das Modell entscheidet, welches Tool es aufruft, und schreibt das Ergebnis auf, aber jeder Anteil und jedes Volumen stammt aus dem Tool, nicht aus der eigenen Arithmetik des Modells.
