---
layout: post
lang: de
title: "Die Verlustkarte: Eine Medallion-Pipeline, Anomalie-Markierungen und ein LLM, das die Abweichungsnotiz entwirft"
image: /assets/og/winery-loss-map-medallion-pipeline-genai.png
description: "Teil 3 von The Cellar Ledger. Jedes Weingut verliert Wein zwischen Traubenannahme und Flasche. Baue die Verlustkarte als Bronze-, Silver- und Gold-Pipeline über dem Bewegungsjournal, markiere auffällige Stufen mit robuster Statistik und lass ein LLM die monatliche Abweichungsnotiz entwerfen, ohne dass es je selbst rechnet."
date: 2026-07-02 09:00:00 -0700
updated: 2026-07-02
permalink: /de/2026/winery-loss-map-medallion-pipeline-genai/
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, anomaly-detection]
faq:
  - q: "Wie viel Wein verliert ein Weingut zwischen Traubenannahme und Flasche?"
    a: "Das schwankt stark mit Stil, Pressregime, Fasslagerzeit und Kellerfeuchte, daher ist jede Einzelzahl mit Vorsicht zu genießen. Aussagekräftiger ist deine eigene Zahl: der Verlust pro Stufe und Partie, berechnet aus erfassten Bewegungen, und der unerklärte Rest, der übrig bleibt. Diesem Rest lohnt es sich nachzugehen."
  - q: "Welche Anomalieerkennung funktioniert für Verlustdaten im Weingut?"
    a: "Einfache, robuste Statistik schlägt hier meist komplexe Modelle. Vergleiche die Verlustrate jeder Partie in einer Stufe mit dem Median derselben Stufe und desselben Gebindetyps, skaliert mit der mittleren absoluten Abweichung vom Median, und markiere die Ausreißer. Für ein tiefes Modell gibt es selten genug Daten, und einen robusten z-Wert kann ein Kellermeister leicht von Hand nachprüfen."
  - q: "Kann ein LLM den monatlichen Verlustabweichungsbericht schreiben?"
    a: "Es kann ihn entwerfen, solange es nie rechnet. Berechne die Zahlen in SQL, übergib die Ergebnisse und die erfassten Korrekturbegründungen an das Modell und lass es den Kommentar um diese festen Zahlen herum schreiben. Ein Mensch prüft und zeichnet ab. Das Modell ist gut darin, aus einer Tabelle und zwanzig Begründungscodes lesbare Absätze zu machen, und schlecht im Rechnen."
---

**Kurze Antwort: Ein Weingut, das 100 Tonnen rote Trauben verarbeitet, presst vielleicht 72.000 Liter und füllt 63.500 ab. Die 8.500 Liter dazwischen sind größtenteils bekannte Verluste: Trub, Abstiche, Verdunstung, Filtration, Abfüllung. Entscheidend ist, was übrig bleibt, nachdem diese erfasst sind: der unerklärte Rest. Baue die Verlustkarte als Medallion-Pipeline über dem Bewegungsjournal, markiere auffällige Stufen mit robuster Statistik statt mit einem ausgefallenen Modell und lass ein LLM die Abweichungsnotiz aus den Abfrageergebnissen entwerfen. Das Modell schreibt die Worte. SQL rechnet die Summen.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Ein Wasserfalldiagramm für einen beispielhaften Rotweinjahrgang mit 100 Tonnen. Es beginnt bei 72.000 Litern gepresst und fällt dann stufenweise: Grobtrub 2.900 Liter, Abstiche 1.100, Fassverdunstung 2.000, Auffüllen und Proben 400, Filtration 700, Abfüllung 500 und ein unerklärter Rest von 900 Litern, pink hervorgehoben, und endet bei 63.500 Litern abgefüllt. Die senkrechte Achse beginnt bei 60.000 Litern.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">VERLUSTKARTE: 100 TONNEN ROT, TRAUBE BIS FLASCHE (BEISPIEL)</text>
<g font-family="sans-serif">
<line x1="60" y1="260" x2="960" y2="260" stroke="#4a6b64" stroke-width="1"/>
<text x="60" y="52" font-size="10" fill="#4a6b64">Achse beginnt bei 60.000 L</text>
<rect x="70" y="70" width="64" height="190" fill="#06483f"/>
<text x="102" y="64" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">72.000</text>
<rect x="170" y="70" width="64" height="45.9" fill="#4db6a2"/>
<text x="202" y="130" text-anchor="middle" font-size="11" fill="#06483f">&#8722;2.900</text>
<rect x="270" y="115.9" width="64" height="17.4" fill="#4db6a2"/>
<text x="302" y="148" text-anchor="middle" font-size="11" fill="#06483f">&#8722;1.100</text>
<rect x="370" y="133.3" width="64" height="31.7" fill="#4db6a2"/>
<text x="402" y="180" text-anchor="middle" font-size="11" fill="#06483f">&#8722;2.000</text>
<rect x="470" y="165" width="64" height="6.3" fill="#4db6a2"/>
<text x="502" y="186" text-anchor="middle" font-size="11" fill="#06483f">&#8722;400</text>
<rect x="570" y="171.3" width="64" height="11.1" fill="#4db6a2"/>
<text x="602" y="197" text-anchor="middle" font-size="11" fill="#06483f">&#8722;700</text>
<rect x="670" y="182.4" width="64" height="7.9" fill="#4db6a2"/>
<text x="702" y="205" text-anchor="middle" font-size="11" fill="#06483f">&#8722;500</text>
<rect x="770" y="190.3" width="64" height="14.3" fill="#ff4081"/>
<text x="802" y="220" text-anchor="middle" font-size="11" font-weight="700" fill="#ff4081">&#8722;900</text>
<rect x="870" y="204.6" width="64" height="55.4" fill="#06483f"/>
<text x="902" y="198" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">63.500</text>
<g font-size="10" fill="#4a6b64" text-anchor="middle">
<text x="102" y="278">gepresst</text>
<text x="202" y="278">Grobtrub</text>
<text x="302" y="278">Abstiche</text>
<text x="402" y="278">Fass-</text><text x="402" y="291">verdunstung</text>
<text x="502" y="278">Auffüllen</text><text x="502" y="291">&amp; Proben</text>
<text x="602" y="278">Filtration</text>
<text x="702" y="278">Abfüllung</text>
<text x="802" y="278" fill="#ff4081" font-weight="700">unerklärt</text>
<text x="902" y="278">abgefüllt</text>
</g>
<rect x="40" y="304" width="920" height="30" rx="8" fill="#06483f"/>
<text x="500" y="324" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">7.600 L BEKANNTER VERLUST &#183; 900 L, DIE NIEMAND ERKLÄREN KANN &#183; DEM PINKEN BALKEN NACHGEHEN</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Beispielzahlen, keine Benchmarks. Nur deine eigenen Stufen aus deinem eigenen Journal zählen.</figcaption>
</figure>

Am Ende jedes Jahrgangs stellt jemand dieselbe Frage: Wir haben so viel gepresst, so viel abgefüllt, wo ist der Rest geblieben? Die ehrliche Antwort lautet meist 'Trub, Verdunstung und viele Kleinigkeiten', begleitet von einem Achselzucken. Dieses Achselzucken verdeckt zwei sehr unterschiedliche Arten von Verlust. Das meiste davon sind die normalen Kosten der Weinbereitung. Ein kleiner Anteil ist Wein, über den das Weingut keine Rechenschaft ablegen kann, und genau in diesem Anteil stecken das Geld, die Verbrauchsteuerfragen und die Prozessprobleme.

Der [vorherige Beitrag]({{ '/de/2026/event-sourced-cellar-records-winery/' | relative_url }}) hat das Bewegungsjournal aufgebaut. Dieser macht daraus eine Verlustkarte, ergänzt eine leichte Schicht Anomalieerkennung und übergibt den monatlichen Bericht an ein LLM an der kurzen Leine.

## Bekannter versus unerklärter Verlust

Manche Verluste sind Wein, den das Weingut bewusst aufgegeben hat, mit erfasster Begründung:

- **Grobtrub** nach der Gärung und dem ersten Abstich, oft einige Prozent des Volumens.
- **Abstichverluste** jedes Mal, wenn Wein vom Bodensatz gezogen wird.
- **Fassverdunstung**, die stark von Kellerfeuchte und Temperatur abhängt und einige Prozent pro Jahr erreicht.
- **Auffüllen und Proben**, klein, aber ständig.
- **Filtration und Abfüllung**, das Totvolumen in Schläuchen, Filtern und dem Füllerkessel.

Alles andere ist der Rest: Eingänge minus Ausgänge minus jeder erfasste Verlust. Im Beispieljahrgang oben haben 7.600 Liter Verlust eine Begründung und 900 Liter nicht. Neunhundert Liter fertiger Rotwein sind mehr als tausend Flaschen. Das ist einen Nachmittag wert.

Der Rest ist nie null. Messgeräte widersprechen sich, Peilungen haben Fehler, Temperatur verschiebt Volumen. Das Ziel ist nicht null. Das Ziel ist ein Rest, der klein und stabil genug ist, dass du es merkst, wenn er springt.

## Die Pipeline: Bronze, Silver, Gold

Eine Verlustkarte ist ein Data-Engineering-Problem, bevor sie ein Analytics-Problem ist. Das Medallion-Muster passt gut dazu.

**Bronze** ist das Bewegungsjournal selbst, unverändert: jedes Ereignis für Eingang, Umpumpen, Abstich, Auffüllen, Filtration, Abfüllung, Beobachtung und Korrektur, mit auf 20 Grad C korrigierten Volumen.

**Silver** ordnet jede Bewegung einer Stufe und einer Verlustkategorie zu. Ein Abstichereignis, das 58 Liter in den Trubtank schickt, wird zu 'Verlust: Grobtrub, Stufe: nach der Gärung, Partie 24-SH-03'. Trub, der später filtriert und zurückgewonnen wird, kommt als Rückgewinnungsereignis zurück, damit er nicht doppelt als Verlust zählt. Hier steckt der Großteil der Fachlogik, und hier sollte ein Kellermeister die Regeln prüfen, denn die Zuordnung von Ereignistyp zu Verlustkategorie ist eine Sammlung von Meinungen über den Prozess.

**Gold** ist eine Zeile pro Partie, Stufe und Jahrgang: Volumen rein, Volumen raus, bekannter Verlust nach Kategorie und der Rest. Sie speist den Wasserfall, das Dashboard und, wie wir sehen werden, das Sprachmodell.

```sql
SELECT lot_id, stage,
       SUM(volume_in_l)  AS vol_in,
       SUM(volume_out_l) AS vol_out,
       SUM(known_loss_l) AS known_loss,
       SUM(volume_in_l) - SUM(volume_out_l) - SUM(known_loss_l) AS residual_l
FROM   silver_lot_stage_movements
GROUP  BY lot_id, stage;
```

Es ist eine einzige Abfrage. Die harte Arbeit steckt in Silver, darin, die Kategorien richtig hinzubekommen.

## Anomalie-Markierungen: absichtlich langweilige Statistik

Sobald die Gold-Tabelle existiert, lautet die naheliegende nächste Bitte: 'Finde die Probleme mit KI.' Widerstehe dem Drang, zu einem tiefen Modell zu greifen. Ein Weingut hat vielleicht ein paar hundert Partien im Jahr und eine Handvoll Jahrgänge mit sauberer Historie. Das reicht nicht, um etwas Aufwendiges zu trainieren, und der Kellermeister muss die Markierung von Hand nachprüfen können.

Ein robuster z-Wert erledigt das:

1. Nimm für jede Stufe und jeden Gebindetyp (etwa Abstich aus 5.000-Liter-Edelstahltanks) die mediane Verlustrate über alle Partien.
2. Miss die Streuung der Raten mit der mittleren absoluten Abweichung vom Median, die einzelne Extremwerte ignoriert, statt sich von ihnen ziehen zu lassen.
3. Markiere jede Partie, deren Verlustrate mehr als etwa drei skalierte Abweichungen vom Median entfernt liegt.

Das markiert den einen Tank, der beim Abstich 4% verloren hat, während seine Geschwister 1,5% verloren, und ignoriert die jahrgangsweite Verschiebung, die alle Tanks gemeinsam hatten. Es ist nicht glamourös. Es erklärt sich in einem Satz, und das zählt mehr.

Die Fassverdunstung verdient eine eigene Behandlung. Sie hängt davon ab, wo das Fass liegt, also gruppiere nach Kellerzone und Position, wenn du diese erfasst. Der [Beitrag zum Mikroklima im Lagerhaus]({{ '/de/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}) behandelt dieselbe Physik von der Whisky-Seite.

## Das LLM entwirft die Abweichungsnotiz

Jeden Monat schreibt jemand ein, zwei Absätze für die Betriebsbesprechung: Verlust in diesem Monat, wie er sich vergleicht, was passiert ist. Das dauert eine Stunde und ist öde. Das ist eine gute Aufgabe für ein Sprachmodell, solange du es so aufsetzt, dass es die Zahlen nicht falsch bekommen kann.

Das Muster, das funktioniert:

1. **SQL übernimmt jede Berechnung.** Die Gold-Tabelle, die Veränderungen zum Vormonat, die markierten Partien, die wichtigsten Korrekturbegründungen nach Volumen. Alles wird berechnet, bevor das Modell irgendetwas sieht.
2. **Das Modell bekommt die Ergebnisse als strukturierte Eingabe.** Einen kleinen JSON-Block mit Zahlen, die Liste der markierten Partien und die Freitextbegründungen, die Bediener zu ihren Korrekturereignissen eingetippt haben.
3. **Das Modell schreibt Text um feste Zahlen herum.** Verlange, dass es nur die übergebenen Zahlen verwendet und für jede Aussage die Quellzeile nennt. Noch besser: Lass es die Notiz mit Platzhaltern zurückgeben, die Code aus dem JSON befüllt, sodass das Modell nie eine Zahl selbst tippt.
4. **Es gruppiert die Begründungen der Bediener.** Zwanzig Korrekturnotizen wie 'Auffüllen nicht gebucht', 'B-Reihe aufgefüllt, vergessen', 'Auffüllen, verpasst' werden zu einer Zeile: 'Der Großteil des Rests geht auf nicht gebuchtes Fassauffüllen in der B-Reihe zurück.' Hier verdient sich das Modell wirklich seinen Platz. Es liest unordentlichen menschlichen Text gut.
5. **Ein Mensch bearbeitet und zeichnet ab.** Die Notiz geht unter dem Namen der Winzerin raus, nicht unter dem des Modells.

Was du nicht tun solltest: dem Modell das rohe Journal geben und fragen, was diesen Monat schiefgelaufen ist. Es wird Spalten im Kopf addieren und dabei selbstsicher um ein paar hundert Liter danebenliegen.

## Wo das an Grenzen stößt

**Der Rest schluckt jeden Messfehler.** Ein driftender Durchflussmesser taucht als unerklärter Verlust auf. Ebenso ein Peilstab, der bei der falschen Temperatur abgelesen wurde. Bevor du den Rest als fehlenden Wein behandelst, prüfe die Messgeräte.

**Die Silver-Regeln sind Meinungen.** Ob Trubwein als Verlust oder als rückgewinnbares Nebenprodukt zählt, verändert die Karte. Schreib die Regeln auf und lass sie vom Kellermeister abzeichnen, sonst lesen zwei Leute denselben Wasserfall auf zwei Arten.

**Verlustziele verändern Verhalten.** Werden Menschen am pinken Balken gemessen, schrumpft der pinke Balken, indem Verluste als etwas anderes gebucht werden. Nutze die Karte, um Prozessprobleme zu finden, nicht um die Kellermannschaft zu benoten.

**Das LLM kann trotzdem mit Worten in die Irre führen.** Selbst mit festen Zahlen kann ein Modell einen normalen Monat als Problem darstellen oder ein echtes Problem abtun. Deshalb kommen die Markierungen aus der Statistik, und das Modell beschreibt sie nur.

## Das Fazit

Jedes Weingut verliert Wein. Die Frage ist, wie viel dieses Verlusts eine Begründung hat. Eine Pipeline über dem Bewegungsjournal trennt bekannten Verlust vom Rest. Robuste Statistik zeigt auf die Stufe und Partie, die sich verändert hat. Ein Sprachmodell macht aus den Zahlen und den eigenen Notizen des Kellers einen Absatz, den jemand gern abzeichnet. Keiner dieser drei Schritte ist exotisch, und zusammen verwandeln sie das Achselzucken am Jahrgangsende in eine kurze Liste von Tanks, die man sich ansehen sollte.

Als Nächstes in der Serie: [Partiengenealogie als Graph]({{ '/de/2026/wine-lot-genealogy-graph-recall-agent/' | relative_url }}), in dem dasselbe Journal die Frage 'Welche Flaschen enthalten Parzelle 7?' beantwortet. Für die Keller- und Fassansicht in Tableau siehe [das Dashboard zur Fassreifung]({{ '/de/2023/tableau-wine-cellar-barrel-ageing-dashboard/' | relative_url }}). Die vollständige Liste steht auf der [Seite zur Cellar-Ledger-Serie]({{ '/series/cellar-ledger/' | relative_url }}).

## Häufig gestellte Fragen

**Wie viel Wein verliert ein Weingut zwischen Traubenannahme und Flasche?**
Das schwankt stark mit Stil, Pressregime, Fasslagerzeit und Kellerfeuchte, daher ist jede Einzelzahl mit Vorsicht zu genießen. Aussagekräftiger ist deine eigene Zahl: der Verlust pro Stufe und Partie, berechnet aus erfassten Bewegungen, und der unerklärte Rest, der übrig bleibt. Diesem Rest lohnt es sich nachzugehen.

**Welche Anomalieerkennung funktioniert für Verlustdaten im Weingut?**
Einfache, robuste Statistik schlägt hier meist komplexe Modelle. Vergleiche die Verlustrate jeder Partie in einer Stufe mit dem Median derselben Stufe und desselben Gebindetyps, skaliert mit der mittleren absoluten Abweichung vom Median, und markiere die Ausreißer. Für ein tiefes Modell gibt es selten genug Daten, und einen robusten z-Wert kann ein Kellermeister leicht von Hand nachprüfen.

**Kann ein LLM den monatlichen Verlustabweichungsbericht schreiben?**
Es kann ihn entwerfen, solange es nie rechnet. Berechne die Zahlen in SQL, übergib die Ergebnisse und die erfassten Korrekturbegründungen an das Modell und lass es den Kommentar um diese festen Zahlen herum schreiben. Ein Mensch prüft und zeichnet ab. Das Modell ist gut darin, aus einer Tabelle und zwanzig Begründungscodes lesbare Absätze zu machen, und schlecht im Rechnen.
