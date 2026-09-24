---
layout: post
lang: de
title: "Event Sourcing im Keller: Warum Volumen im Weingut berechnet und nie gespeichert werden sollten"
image: /assets/og/event-sourced-cellar-records-winery.png
description: "Teil 2 von The Cellar Ledger. Wenn Tankvolumen ein editierbares Feld sind, verschwinden Verluste ohne Begründung. Ein Append-only-Bewegungsjournal im Lakehouse macht jeden Bestand zu einer Berechnung, gibt einem KI-Agenten echte Herkunftsdaten zum Erklären und hindert ihn daran, jemals die Wahrheit zu überschreiben."
date: 2026-06-27 09:00:00 -0700
updated: 2026-06-27
permalink: /de/2026/event-sourced-cellar-records-winery/
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, data-modeling]
faq:
  - q: "Was ist Event Sourcing in einem Datenmodell für Weingüter?"
    a: "Statt das Volumen jedes Tanks als Feld zu speichern, das Menschen bearbeiten, speicherst du jede Bewegung als unveränderliches Ereignis: Eingang, Umpumpen, Auffüllen, Abstich, Verschnitt, Filtration, Abfüllung, Probe, Verlust. Das Volumen in einem Gebinde zu einem beliebigen Zeitpunkt ist die Summe der Ereignisse bis zu diesem Zeitpunkt. Nichts wird überschrieben, also hat jeder Liter eine Geschichte."
  - q: "Wie geht man mit einer Peilung um, die nicht zum Buchvolumen passt?"
    a: "Die Peilung als Beobachtung erfassen, nicht als neues Volumen. Weicht sie vom berechneten Bestand ab, wird die Differenz zu einem eigenen Korrekturereignis mit Pflichtbegründung, etwa Verdunstung, nicht erfasstes Auffüllen oder Messfehler. Das Buch wird durch ein Ereignis korrigiert, nie durch eine Bearbeitung, sodass die Lücke sichtbar und erklärbar bleibt."
  - q: "Sollte ein KI-Agent den Bestand eines Weinguts ändern dürfen?"
    a: "Er sollte vorschlagen dürfen, nicht schreiben. Lass den Agenten das Bewegungsjournal lesen und eine Bewegung oder Korrektur samt Begründung entwerfen, und lass einen Menschen sie freigeben, bevor sie angehängt wird. Weil das Journal nur Anhängen erlaubt, wird selbst ein freigegebener Fehler durch ein Stornoereignis korrigiert und verschwindet nie."
---

**Kurze Antwort: Die meisten Systeme in Weingütern speichern das Volumen eines Tanks als Zahl, die Menschen bearbeiten können. Passt die Peilung nicht zum Buch, tippt jemand den neuen Wert ein, und die Differenz verschwindet ohne Begründung. Event Sourcing im Keller heißt, jede Bewegung als Ereignis in einem Journal zu speichern, das nur Anhängen erlaubt, und jeden Bestand daraus zu berechnen. Dann erklärt sich das Buch selbst, ein GenAI-Agent hat echte Historie zum Schlussfolgern statt zu raten, und die Regel 'Agenten schlagen vor, Menschen geben frei' lässt sich leicht durchsetzen, weil nichts überschrieben werden kann.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Zwei Arten, Tank 12 zu erfassen. Links hält eine Zustandstabelle ein einziges Volumenfeld, das jemand von 4.980 auf 4.920 Liter geändert hat, und die 60 Liter sind ohne Begründung weg. Rechts listet ein Bewegungsjournal Ereignisse: 5.000 Liter eingegangen, 40 Liter aus Fass aufgefüllt, 2 Liter Probe, 58 Liter Trub abgestochen, Peilung 4.920 Liter, dann eine Messkorrektur von minus 60 Litern mit erfasster Begründung. Der Bestand ist die Summe der Ereignisse.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">TANK 12: GESPEICHERTER VS. BERECHNETER ZUSTAND</text>
<g font-family="sans-serif">
<text x="210" y="58" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">EDITIERBARES FELD</text>
<rect x="40" y="72" width="340" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="210" y="106" text-anchor="middle" font-size="12" fill="#06483f">tank_12.volume_l</text>
<text x="210" y="140" text-anchor="middle" font-size="22" font-weight="700" fill="#06483f">4.980 &#8594; 4.920</text>
<text x="210" y="172" text-anchor="middle" font-size="11" fill="#ff4081">60 L weg, kein Grund, keine Historie</text>
<text x="700" y="58" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">APPEND-ONLY-BEWEGUNGSJOURNAL</text>
<rect x="440" y="72" width="520" height="190" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<g font-size="11.5" fill="#06483f">
<text x="460" y="98">Eingang &#183; von Presse 3</text><text x="940" y="98" text-anchor="end">+5.000</text>
<text x="460" y="122">Auffüllen &#183; aus Fass B-17</text><text x="940" y="122" text-anchor="end">+40</text>
<text x="460" y="146">Probe &#183; Labor</text><text x="940" y="146" text-anchor="end">&#8722;2</text>
<text x="460" y="170">Abstich &#183; Trub in Trubtank</text><text x="940" y="170" text-anchor="end">&#8722;58</text>
<text x="460" y="194" fill="#4a6b64">Beobachtung &#183; Peilung 4.920 (Buch 4.980)</text><text x="940" y="194" text-anchor="end" fill="#4a6b64">0</text>
<text x="460" y="218" fill="#00695c" font-weight="700">Korrektur &#183; Grund: Fassauffüllung aus Tank 12 nicht erfasst</text><text x="940" y="218" text-anchor="end" fill="#00695c" font-weight="700">&#8722;60</text>
</g>
<line x1="460" y1="232" x2="940" y2="232" stroke="#4db6a2" stroke-width="1"/>
<text x="460" y="252" font-size="12" font-weight="700" fill="#06483f">Bestand = Summe der Ereignisse</text><text x="940" y="252" text-anchor="end" font-size="12" font-weight="700" fill="#06483f">4.920</text>
<rect x="40" y="276" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="301" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">GLEICHER ENDBESTAND &#183; NUR EINER KANN DIR SAGEN, WARUM</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Beide Bücher enden bei 4.920 Litern. Nur das Journal kann dem Prüfer antworten, oder dem Agenten.</figcaption>
</figure>

Tank 12 sollte 4.980 Liter enthalten. Der Kellermitarbeiter peilt ihn und liest 4.920. Das System hat ein Volumenfeld, also tippt er 4.920 ein und macht mit seinem Vormittag weiter. An einem vollen Tag ist das völlig vernünftig. Es bedeutet aber auch, dass 60 Liter Wein die Aufzeichnungen des Weinguts verlassen haben, ohne Begründung, ohne Verlustdatum und ohne Möglichkeit, es später herauszufinden.

Multipliziere das mit hundert Gebinden und einer ganzen Ernte voller Auffüllen, Abstiche und Verschnitte, und du landest bei der bekannten Suche nach fehlendem Wein zum Jahresende. Im [ersten Beitrag dieser Serie]({{ '/de/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) ging es um eine Kennzahl, die nie definiert wurde. In diesem geht es um eine Menge, die nie eine Geschichte haben durfte.

## Gespeicherter versus berechneter Zustand

Die meiste Kellersoftware und fast jede Kellertabelle speichert **Zustand**: das aktuelle Volumen in jedem Gebinde. Bewegungen passieren, und jemand passt den Zustand an. Die Bewegung selbst wird entweder woanders festgehalten oder gar nicht.

Event Sourcing dreht das um. Du speicherst die **Bewegungen** und nie das Volumen. Jede Veränderung im Keller ist ein Ereignis:

- Eingang (von der Presse, einem Lkw, einem anderen Standort)
- Umpumpen und Verschnitt (von Gebinde zu Gebinde, mit Partiezusammensetzung)
- Auffüllen, Abstich, Filtration, Schönung
- Probe und Laborverbrauch
- Abfüllung (Abgang in Fertigware)
- Beobachtung (eine Peilung oder Messung, die für sich nichts verändert)
- Korrektur (die Lücke zwischen beobachtetem und berechnetem Wert, mit Pflichtbegründung)

Das Volumen in einem Gebinde zu einem beliebigen Zeitpunkt ist eine Abfrage: die Summe aller Ereignisse bis zu diesem Zeitpunkt. Niemand bearbeitet es, weil es nichts zu bearbeiten gibt.

```sql
SELECT vessel_id,
       SUM(signed_volume_l_20c) AS volume_l
FROM   cellar_movements
WHERE  event_ts <= :as_of
GROUP  BY vessel_id;
```

Ändere `:as_of`, und du hast den Keller am Ende jedes beliebigen Tages der letzten fünf Jahre. Genau diese Abfrage wollen jede Verbrauchsteuererklärung, jede Prüfung und jedes Gespräch der Art 'Wo ist der Grenache hin?' eigentlich haben.

## Das Detail, über das alle stolpern: Liter bei welcher Temperatur?

Achte auf den Spaltennamen oben: Liter bei 20 Grad C. Wein dehnt sich beim Erwärmen aus, um etwa 0,02 bis 0,03 Prozent pro Grad. Ein 5.000-Liter-Tank, einmal bei 10 Grad und einmal bei 20 Grad gemessen, unterscheidet sich um rund 10 bis 15 Liter, ohne dass Wein irgendwohin gegangen ist.

In einem System mit gespeichertem Zustand taucht diese Differenz in der ersten warmen Frühlingswoche als rätselhafter Verlust oder Gewinn auf. In einem Ereignismodell trägt jede Beobachtung ihre Temperatur, die Pipeline rechnet sie vor dem Abgleich mit dem Buch auf die Referenztemperatur um, und das thermische Schwanken wird nie zur Korrektur. Das ist eine Kleinigkeit. Es ist aber genau die Art von Kleinigkeit, bei der ein Kellermeister im ersten Monat aufhört, dem System zu vertrauen.

## Umsetzung im Lakehouse

Nichts davon braucht exotische Werkzeuge. Eine Append-only-Tabelle in dem Lakehouse, das du ohnehin betreibst (Delta in Fabric oder Databricks, Iceberg in Snowflake), erledigt die Aufgabe. Ein paar Regeln halten sie ehrlich:

1. **Nur Anhängen, technisch durchgesetzt.** Vergib auf der Bewegungstabelle Insert-Rechte, aber keine Update- oder Delete-Rechte. Korrekturen sind Stornoereignisse: ein Minus 500, um ein falsches Plus 500 aufzuheben, dann das richtige. Der Fehler bleibt sichtbar, und genau darum geht es.
2. **Begründungen sind bei Korrekturen Pflicht.** Ein Datenvertrag lehnt ein Korrekturereignis mit leerer Begründung ab. 'Unbekannt' ist erlaubt. Leer nicht.
3. **Wenn möglich an der Quelle erfassen.** Gibt es bereits ein Weingutssystem, kann Change Data Capture (Debezium, Fabric Mirroring oder der eigene Feed des Anbieters) dessen Updates in Ereignisse umwandeln, sodass du den Keller nicht bittest, mitten in der Ernte eine neue App zu lernen.
4. **Snapshots für Geschwindigkeit, nie für die Wahrheit.** Eine nächtliche Bestandstabelle ist für Dashboards in Ordnung. Sie wird aus den Ereignissen neu aufgebaut und nie bearbeitet.

Time Travel im Lakehouse wird manchmal als Abkürzung angeboten. Es ist nicht dasselbe. Time Travel zeigt dir, wie die Tabelle aussah. Ein Ereignisjournal sagt dir, was im Keller passiert ist. Nur Letzteres beantwortet das Warum.

## Warum das für GenAI wichtig ist

Hier zahlt sich das altmodische Datenmodell für die neumodischen Werkzeuge aus.

**Ein Agent kann nur erklären, was erfasst wurde.** Frag einen GenAI-Assistenten 'Warum fehlen in Tank 12 sechzig Liter?' In einem System mit gespeichertem Zustand hat er zwei Volumen-Snapshots und nichts dazwischen, also sagt er entweder, dass er es nicht weiß, oder, schlimmer, er erfindet eine plausible Geschichte über Verdunstung. Mit einem Bewegungsjournal liest er die Ereignisse, findet die Korrektur und zitiert die Begründung mit Bediener und Zeitstempel. Gleiches Modell, gleicher Prompt. Der Unterschied liegt vollständig in den Daten.

**Agenten sollten vorschlagen, nie schreiben.** Der naheliegende nächste Schritt ist, einen Agenten die Datenerfassung übernehmen zu lassen: den Kellerarbeitsauftrag lesen und die Bewegungen buchen. Das ist nützlich und ein wenig beängstigend. Das Append-only-Design macht es sicher, das auszuprobieren. Der Agent legt Ereignisentwürfe samt Begründung in einer Warteschlange ab ('Arbeitsauftrag 4417 sagt: B-17 aus Tank 12 auffüllen, 40 L'). Ein Mensch gibt sie frei, und erst dann werden sie angehängt. Stellt sich ein freigegebenes Ereignis als falsch heraus, wird es wie jedes andere storniert. Nichts, was der Agent tut, kann das Buch still überschreiben.

**Tool-Aufrufe werden einfach.** Stellst du den Keller einem Agenten über einen kleinen Satz von Tools bereit, sagt dir das Ereignismodell genau, welche das sind: `balance(vessel, as_of)`, `history(vessel, from, to)`, `propose_movement(...)`. Es gibt kein `set_volume`. Das fehlende Tool ist das Sicherheitsmerkmal.

## Wo das an Grenzen stößt

**Es ist nur so vollständig wie die Erfassung.** Landet das Auffüllen in einer hektischen Woche auf einem Whiteboard und nie im System, zeigt das Journal jedes Mal eine Korrektur. Das ist immer noch besser als Schweigen, denn die Korrekturbegründungen zeigen dir, wo die Erfassungsgewohnheit schwach ist, aber die fehlenden Ereignisse erfindet es nicht.

**Durchflussmesser und Peilungen widersprechen sich.** Ein Umpumpen, gemessen mit einem Durchflussmesser, und dasselbe Umpumpen, gemessen durch Peilen beider Gebinde, stimmen nicht exakt überein. Lege fest, welcher Wert für welchen Bewegungstyp die Referenz ist, und erfasse den anderen als Beobachtung.

**Die Ernte ist Chaos.** Während der Lese kommen Ereignisse spät und in falscher Reihenfolge an. Das Modell muss rückdatierte Ereignisse mit einer erfassten Buchungszeit zusätzlich zur Ereigniszeit akzeptieren, sonst hört der Keller bis November einfach auf, es zu nutzen.

**Die Migration ist nicht umsonst.** Der Wechsel von einem System mit gespeichertem Zustand bedeutet, mit einem Eröffnungsbestandsereignis pro Gebinde zu beginnen. Die Historie vor diesem Datum bleibt so unerklärt, wie sie immer war.

## Das Fazit

Ein Volumen, das man bearbeiten kann, ist ein Volumen, das seine Geschichte verlieren kann. Ein Volumen, das man aus Bewegungen berechnet, behält sie. Das Ereignisjournal ist eine alte Idee (so führen Buchhalter seit Jahrhunderten ihre Bücher), und es ist zufällig genau das, was ein GenAI-Agent braucht: echte Herkunft zum Erklären und eine harte Wand gegen das Umschreiben der Vergangenheit. Der Wein war immer in Bewegung. Das Datenmodell muss es nur zugeben.

Als Nächstes in der Serie: [die Verlustkarte]({{ '/de/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}), in der diese Ereignisse zu einem Wasserfall von der Traubenannahme bis zur Flasche werden und ein LLM die Abweichungsnotiz entwirft. Zu den Sensoren, die diese Ereignisse speisen, siehe [IoT im Weingut]({{ '/de/2026/iot-in-the-winery-sensors-process/' | relative_url }}). Die vollständige Liste steht auf der [Seite zur Cellar-Ledger-Serie]({{ '/series/cellar-ledger/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist Event Sourcing in einem Datenmodell für Weingüter?**
Statt das Volumen jedes Tanks als Feld zu speichern, das Menschen bearbeiten, speicherst du jede Bewegung als unveränderliches Ereignis: Eingang, Umpumpen, Auffüllen, Abstich, Verschnitt, Filtration, Abfüllung, Probe, Verlust. Das Volumen in einem Gebinde zu einem beliebigen Zeitpunkt ist die Summe der Ereignisse bis zu diesem Zeitpunkt. Nichts wird überschrieben, also hat jeder Liter eine Geschichte.

**Wie geht man mit einer Peilung um, die nicht zum Buchvolumen passt?**
Die Peilung als Beobachtung erfassen, nicht als neues Volumen. Weicht sie vom berechneten Bestand ab, wird die Differenz zu einem eigenen Korrekturereignis mit Pflichtbegründung, etwa Verdunstung, nicht erfasstes Auffüllen oder Messfehler. Das Buch wird durch ein Ereignis korrigiert, nie durch eine Bearbeitung, sodass die Lücke sichtbar und erklärbar bleibt.

**Sollte ein KI-Agent den Bestand eines Weinguts ändern dürfen?**
Er sollte vorschlagen dürfen, nicht schreiben. Lass den Agenten das Bewegungsjournal lesen und eine Bewegung oder Korrektur samt Begründung entwerfen, und lass einen Menschen sie freigeben, bevor sie angehängt wird. Weil das Journal nur Anhängen erlaubt, wird selbst ein freigegebener Fehler durch ein Stornoereignis korrigiert und verschwindet nie.
