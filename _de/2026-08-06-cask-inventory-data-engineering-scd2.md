---
layout: post
lang: de
title: "Fassbestand als Data Engineering: SCD2-Lagerplätze, Nachvermessungen und Angels' Share als abgeleitete Größe"
image: /assets/og/cask-inventory-data-engineering-scd2.png
description: "Teil 4 von The Still and the Model. Ein Fass liegt zwölf Jahre oder länger im Lagerhaus, wird umgelagert, beprobt und nachvermessen und verliert jedes Jahr Destillat. Modelliere seine Attribute als langsam veränderliche Dimensionen, sein Leben als Ereignisse und den Angels' Share als Berechnung, dann hat jede Frage zu jedem Fass an jedem Datum genau eine Antwort."
date: 2026-08-06 09:00:00 -0700
updated: 2026-08-06
permalink: /de/2026/cask-inventory-data-engineering-scd2/
tags: [distilling-maturation, still-and-model, data-engineering, data-modeling, generative-ai]
faq:
  - q: "Was ist eine SCD2-Tabelle, und warum nutzt man sie für Fässer?"
    a: "Eine langsam veränderliche Dimension vom Typ 2 bewahrt jede Version eines Datensatzes mit den Daten, an denen sie gültig war, statt sie zu überschreiben. Bei Fässern heißt das: Jeder Lagerplatz, jeder Eigentümer und jeder Status, den ein Fass je hatte, bleibt mit seinen Daten in der Tabelle. Man kann fragen, wo ein Fass im März 2019 lag, und bekommt eine Antwort. Das zählt für Mikroklimaanalysen, Prüfungen und Kundenanfragen."
  - q: "Wie sollte der Angels' Share in einem Fassbestand berechnet werden?"
    a: "Als abgeleitete Größe, nie als gespeicherte. Nimm die Liter reinen Alkohols bei der Befüllung, ziehe den Alkohol der letzten Nachvermessung sowie alle erfassten Proben und Entnahmen ab, und der Rest ist der Verlust. Als Feld gespeichert, veraltet der Angels' Share und verdeckt Probenahmen. Aus Ereignissen abgeleitet, ist er immer aktuell und nachvollziehbar."
  - q: "Kann ein GenAI-Assistent Fragen zum reifenden Bestand beantworten?"
    a: "Ja, wenn er über kontrollierte Abfragen antwortet statt über Rohtabellen. Gib ihm Tools wie cask_history, position_on und alcohol_balance, gestützt auf die Ereignis- und SCD2-Tabellen, dann kann er Fragen beantworten wie etwa, welche Fässer einer bestimmten Befüllung mehr als üblich verloren haben. Jede Zahl stammt dabei aus der Abfrage."
---

**Kurze Antwort: Ein Whiskyfass kann zwölf Jahre oder länger im Lagerhaus liegen, und in dieser Zeit wird es umgelagert, beprobt, nachvermessen und verliert still und leise Destillat an die Luft. Speichert der Bestand nur den aktuellen Lagerplatz und das aktuelle Volumen, ist der größte Teil dieser Geschichte verloren. Modelliere die Attribute, die sich langsam ändern (Lagerplatz, Eigentümer, Status), als langsam veränderliche Dimension vom Typ 2, erfasse alles, was mit dem Fass passiert, als Ereignis, und berechne den Angels' Share aus den Ereignissen, statt ihn zu speichern. Dann haben "Wo lag dieses Fass 2019?" und "Wie viel hat es wirklich verloren?" jeweils genau eine Antwort, und ein GenAI-Assistent kann sie beantworten, ohne zu raten.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Eine beispielhafte Zeitachse über zwölf Jahre für ein Fass. 2014 befüllt mit 250 Litern bei 63.5 Prozent, 158.75 Liter reiner Alkohol, in Lagerhaus 1. 2016 in Lagerhaus 3 umgelagert. 2019 beprobt. 2020 nachvermessen. 2022 erneut umgelagert. 2026 nachvermessen mit 205 Litern bei 60.8 Prozent, 124.64 Liter reiner Alkohol. Der Angels' Share ergibt sich rechnerisch zu etwa 34 Litern reinen Alkohols, rund 2 Prozent pro Jahr.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">EIN FASS, ZWÖLF JAHRE EREIGNISSE (BEISPIEL)</text>
<g font-family="sans-serif">
<line x1="70" y1="150" x2="930" y2="150" stroke="#4db6a2" stroke-width="3"/>
<circle cx="70" cy="150" r="9" fill="#06483f"/>
<text x="70" y="120" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">2014 Befüllung</text>
<text x="70" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">250 L bei 63,5%</text>
<text x="70" y="198" text-anchor="middle" font-size="10.5" fill="#4a6b64">158,75 LAA</text>
<circle cx="213" cy="150" r="7" fill="#4db6a2"/>
<text x="213" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2016 Umlagerung</text>
<text x="213" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">W1 nach W3</text>
<circle cx="427" cy="150" r="7" fill="#4db6a2"/>
<text x="427" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2019 Probe</text>
<text x="427" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">erfasste Entnahme</text>
<circle cx="498" cy="150" r="7" fill="#4db6a2"/>
<text x="518" y="100" text-anchor="middle" font-size="11.5" fill="#06483f">2020 Nachvermessung</text>
<circle cx="643" cy="150" r="7" fill="#4db6a2"/>
<text x="643" y="120" text-anchor="middle" font-size="11.5" fill="#06483f">2022 Umlagerung</text>
<text x="643" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">W3 nach W5</text>
<circle cx="930" cy="150" r="9" fill="#06483f"/>
<text x="915" y="120" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">2026 Nachvermessung</text>
<text x="915" y="182" text-anchor="middle" font-size="10.5" fill="#4a6b64">205 L bei 60,8%</text>
<text x="915" y="198" text-anchor="middle" font-size="10.5" fill="#4a6b64">124,64 LAA</text>
<rect x="250" y="222" width="500" height="44" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="500" y="249" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ff4081">abgeleiteter Verlust etwa 34 LAA, rund 2% pro Jahr</text>
<rect x="40" y="282" width="920" height="36" rx="10" fill="#06483f"/>
<text x="500" y="305" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">DER ANGELS' SHARE IST EINE ABFRAGE ÜBER DIE EREIGNISSE, KEIN FELD, DAS JEMAND PFLEGT</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Beispielfass. Liter reinen Alkohols (LAA) sind Volumenliter mal Alkoholstärke. In einer vollständigen Bilanz werden Proben wie die Entnahme von 2019 abgezogen, bevor irgendetwas als Angels' Share gilt.</figcaption>
</figure>

Frag eine Lagerleiterin, wo Fass 14-0387 liegt, und sie sagt es dir in Sekunden. Frag, wo es im Sommer 2019 lag, als eine Gruppe von Fässern aus dieser Befüllung eine unerwartete Note entwickelte, und die Antwort erfordert meist ein Papierbuch, einen pensionierten Kollegen und viel guten Willen.

Die [vorherigen Beiträge dieser Serie]({{ '/de/2026/llm-copilot-still-operator/' | relative_url }}) spielten im Brennhaus. Dieser zieht ins Lagerhaus um, wo die Zeitskala Jahre statt Stunden beträgt und wo das Datenmodell darüber entscheidet, ob die Geschichte erhalten bleibt.

## Zwei Arten von Veränderung

Ein Fass verändert sich auf zwei verschiedene Weisen, und die brauchen zwei verschiedene Strukturen.

**Attribute, die sich gelegentlich ändern:** Lagerhaus, Reihe und Ebene; Eigentümer (bei Fässern, die für Kunden gelagert werden); Status (in Reifung, reserviert, entleert); Fasstyp nach einem Umfüllen. Das sind Fakten über das Fass, die für einen Zeitraum gelten und sich dann ändern.

**Dinge, die mit ihm passieren:** Befüllen, Umlagern, Beproben, Nachvermessen, Auffüllen, Umfüllen in ein neues Fass, Entleeren. Das sind Ereignisse mit einem Datum, einer Menge und einer Person.

Die meisten Fasssysteme speichern die erste Art als aktuelle Werte und die zweite bestenfalls als Kommentarfeld. Beides verliert Geschichte.

## SCD2: jede Version, mit ihren Daten

Eine langsam veränderliche Dimension vom Typ 2 bewahrt jede Version eines Attributs, statt sie zu überschreiben. Jede Zeile trägt das Datum, ab dem sie galt, und das Datum, an dem sie endete:

```sql
-- cask_position_scd2: one row per period the cask sat in one place
-- cask_id | warehouse | bay | tier | valid_from | valid_to   | is_current
-- 14-0387 | W1        | A   | 2    | 2014-05-12 | 2016-09-03 | false
-- 14-0387 | W3        | C   | 1    | 2016-09-03 | 2022-04-18 | false
-- 14-0387 | W5        | B   | 3    | 2022-04-18 | 9999-12-31 | true

SELECT warehouse, bay, tier
FROM   cask_position_scd2
WHERE  cask_id = '14-0387'
  AND  DATE '2019-07-01' >= valid_from
  AND  DATE '2019-07-01' <  valid_to;
```

Diese eine Abfrage beantwortet die Frage nach 2019. Sie macht auch Mikroklimaanalysen möglich: Verknüpfe die Lagerplätze über die Zeit mit den Temperatur- und Feuchteprotokollen des Lagerhauses, und jedes Fass bekommt seine eigene erlebte Klimageschichte. Genau die braucht der [Beitrag zum Mikroklima im Lagerhaus]({{ '/de/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}) als Eingabe. Ohne SCD2 scheint jedes Fass zwölf Jahre dort verbracht zu haben, wo es heute zufällig liegt.

Die Pipeline, die das pflegt, ist Standard: Bei jeder erfassten Umlagerung wird die aktuelle Zeile geschlossen und eine neue geöffnet. dbt-Snapshots, Delta `MERGE` und Fabric-Pipelines erledigen das mit wenigen Zeilen Konfiguration.

## Ereignisse: das eigene Kontobuch des Fasses

Alles, was den Inhalt des Fasses verändert, ist ein Ereignis, erfasst auf dieselbe Weise, wie das [Kellerbuch im Weingut]({{ '/de/2026/event-sourced-cellar-records-winery/' | relative_url }}) Bewegungen erfasst:

- **fill**: Volumenliter, Alkoholstärke, LAA, Destillatcharge, Fasstyp
- **sample**: entnommenes Volumen, Zweck
- **regauge**: Volumenliter, Alkoholstärke, LAA, Methode (Peilung oder Wägung)
- **re-rack**: Quellfass, Zielfass, Volumen
- **disgorge**: Volumen und Alkoholstärke hinaus in den Verschnitt

Nachvermessungen verdienen eine Anmerkung. Fässer werden oft per Wägung statt per Peilung vermessen: Bruttogewicht minus Leergewicht des Fasses, geteilt durch die Dichte bei der gemessenen Alkoholstärke, ergibt die Volumenliter. Diese Rechnung hängt an einer Dichtetabelle für Ethanol und Wasser bei 20 Grad C und am Leergewicht, das bei der Befüllung erfasst wurde. Fehlt eines davon oder ist es falsch, ist jede Nachvermessung dieses Fasses in dieselbe Richtung falsch. Speichere Bruttogewicht, Leergewicht und Alkoholstärke am Ereignis, nicht nur das resultierende Volumen, damit sich die Rechnung prüfen und wiederholen lässt.

## Angels' Share als abgeleitete Größe

Sind die Ereignisse vorhanden, ist der Angels' Share kein Feld mehr, das jemand pflegt, sondern eine Berechnung:

> Verlust = LAA bei Befüllung - LAA bei letzter Nachvermessung - LAA aus Proben und Entnahmen

Für das Beispielfass oben: befüllt mit 250 Litern bei 63,5%, das sind 158,75 LAA. Zwölf Jahre später ergibt die Nachvermessung 205 Liter bei 60,8%, das sind 124,64 LAA. Lässt man die kleine Probe von 2019 der Einfachheit halber beiseite, beträgt der Verlust etwa 34 LAA, also 21,5% über zwölf Jahre, rund 2% pro Jahr mit Zinseszinseffekt. Das liegt in dem Bereich, der oft für Scotch in einem kühlen, feuchten Lagerhaus genannt wird. In warmem Klima geht deutlich mehr verloren, und die Alkoholstärke kann sogar steigen statt fallen, wo Wasser schneller verdunstet als Alkohol.

Zwei Dinge machen die abgeleitete Variante besser als eine gespeicherte. Sie ist immer aktuell: Eine neue Nachvermessung aktualisiert sie, ohne dass jemand daran denken muss. Und sie ist ehrlich bei Proben: Ein Fass, das durstig wirkt, weil das Blending-Team ständig daraus gezogen hat, weist seine Proben als Proben aus, nicht als Verdunstung. Der [Beitrag zur Prognose des Angels' Share]({{ '/de/2024/forecasting-whiskey-angels-share/' | relative_url }}) behandelt die Modellierung des Verlusts. Dies hier sind die Daten, auf denen sie beruhen sollte.

## Ein GenAI-Assistent obendrauf

Mit SCD2-Lagerplätzen und einem Ereignisbuch pro Fass werden die Fragen, die Menschen tatsächlich stellen, zu Abfragen, und Abfragen können zu Tools für einen GenAI-Assistenten werden:

- `cask_history(cask_id)`: jedes Ereignis und jeder Lagerplatz, in Reihenfolge
- `position_on(cask_id, date)`: die SCD2-Abfrage von oben
- `alcohol_balance(fill_batch)`: LAA bei Befüllung, aktuelle LAA, Proben, abgeleiteter Verlust pro Fass

Auf die Frage "Welche Fässer aus der Befüllung vom Mai 2014 haben mehr verloren als ihre Nachbarn?" ruft der Assistent `alcohol_balance` auf, vergleicht jedes Fass mit dem Median seiner Befüllung und seines Lagerhauses und listet die Ausreißer mit ihren Lagerplätzen über die Zeit auf. Jede Zahl stammt aus einer Abfrage. Die Aufgabe des Modells ist, die Frage zu verstehen, die richtigen Tools aufzurufen und die Antwort in klaren Worten zu erklären. Der [Beitrag zum semantischen Layer]({{ '/de/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) in der Wein-Serie begründet, warum es keine Rohtabellen sehen darf.

## Wo das bricht

**Zwölf Jahre Geschichte beginnen selten sauber.** Das erste Jahrzehnt der meisten Fassbestände ist eine Mischung aus Papier, Altsystemen und Tabellenkalkulationen. Migriere, was du kannst, als Ereignisse mit klarer Quelle, starte SCD2 mit einem Anfangslagerplatz pro Fass und kennzeichne die migrierte Geschichte als weniger verlässlich, statt so zu tun, als sei sie so gut wie die neue.

**Nachvermessungen sind selten und verrauscht.** Ein Fass, das in zwölf Jahren zweimal nachvermessen wurde, liefert zwei Datenpunkte für seinen Verlust. Unterschiede von wenigen Prozent zwischen Fässern können Messfehler sein, keine Reifung.

**Leergewichte gehen verloren.** Ein Fass ohne erfasstes Leergewicht lässt sich per Wägung nicht genau nachvermessen. Behandle ein fehlendes Leergewicht als Datenqualitätsmangel und markiere es am ersten Tag, nicht im zehnten Jahr.

**Steueraufzeichnungen sind getrennt.** Aufzeichnungen des Steuerlagers stehen gegenüber der Zollbehörde in der Pflicht und folgen eigenen Regeln. Der analytische Bestand sollte mit ihnen abgeglichen werden, sie aber nicht ersetzen.

## Das Fazit

Ein Fass ist eine Akte über zwölf Jahre, und die meisten Bestände bewahren nur ihre letzte Seite. Bewahre jeden Lagerplatz mit seinen Daten, erfasse jedes Ereignis mit seinen Mengen und leite den Angels' Share ab, statt ihn zu speichern. Dann haben die Fragen, auf die es ankommt, zu Klima, Verlust, Proben und Prüfungen, jeweils eine Antwort, und ein GenAI-Assistent findet sie über kontrollierte Tools, statt zu improvisieren. Das Destillat ist geduldig. Das Datenmodell sollte es auch sein.

Als Nächstes in der Serie: [ein GenAI-Blending-Assistent, bei dem die Mathematik im Code steckt]({{ '/de/2026/genai-whisky-blending-assistant-lp/' | relative_url }}). Zur Auswahl der Fässer siehe [KI für Fassauswahl und Bestand an reifendem Whisky]({{ '/de/2024/ai-cask-selection-inventory/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite The Still and the Model]({{ '/series/still-and-model/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist eine SCD2-Tabelle, und warum nutzt man sie für Fässer?**
Eine langsam veränderliche Dimension vom Typ 2 bewahrt jede Version eines Datensatzes mit den Daten, an denen sie gültig war, statt sie zu überschreiben. Bei Fässern heißt das: Jeder Lagerplatz, jeder Eigentümer und jeder Status, den ein Fass je hatte, bleibt mit seinen Daten in der Tabelle. Man kann fragen, wo ein Fass im März 2019 lag, und bekommt eine Antwort. Das zählt für Mikroklimaanalysen, Prüfungen und Kundenanfragen.

**Wie sollte der Angels' Share in einem Fassbestand berechnet werden?**
Als abgeleitete Größe, nie als gespeicherte. Nimm die Liter reinen Alkohols bei der Befüllung, ziehe den Alkohol der letzten Nachvermessung sowie alle erfassten Proben und Entnahmen ab, und der Rest ist der Verlust. Als Feld gespeichert, veraltet der Angels' Share und verdeckt Probenahmen. Aus Ereignissen abgeleitet, ist er immer aktuell und nachvollziehbar.

**Kann ein GenAI-Assistent Fragen zum reifenden Bestand beantworten?**
Ja, wenn er über kontrollierte Abfragen antwortet statt über Rohtabellen. Gib ihm Tools wie cask_history, position_on und alcohol_balance, gestützt auf die Ereignis- und SCD2-Tabellen, dann kann er Fragen beantworten wie etwa, welche Fässer einer bestimmten Befüllung mehr als üblich verloren haben. Jede Zahl stammt dabei aus der Abfrage.
