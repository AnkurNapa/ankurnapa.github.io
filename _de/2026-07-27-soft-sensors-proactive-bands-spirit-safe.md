---
layout: post
lang: de
title: "Soft Sensoren und proaktive Bänder statt Alarmen am Spirit Safe"
image: /assets/og/soft-sensors-proactive-bands-spirit-safe.png
description: "Teil 2 von The Still and the Model. Die Destillatstärke zwischen den Aräometerablesungen aus Temperaturen und Durchfluss schätzen, jeden Brennlauf mit einem Band aus guten Läufen vergleichen und Drift melden, solange noch Zeit zum Handeln bleibt. Warum das besser ist als ein weiterer fester Alarm auf einem Panel, das der Bediener längst zu ignorieren gelernt hat."
date: 2026-07-27 09:00:00 -0700
updated: 2026-07-27
permalink: /de/2026/soft-sensors-proactive-bands-spirit-safe/
tags: [distilling-maturation, still-and-model, soft-sensors, machine-learning, data-engineering]
faq:
  - q: "Was ist ein Soft Sensor in einer Brennerei?"
    a: "Ein Soft Sensor schätzt etwas, das man nicht kontinuierlich messen kann, etwa die Destillatstärke, aus Größen, die man messen kann, etwa Dampftemperatur, Blasentemperatur, Druck und Durchfluss. Er wird an einer echten Messung nachkalibriert, zum Beispiel am Aräometer im Spirit Safe, sobald eine vorliegt. Er füllt die Lücken zwischen den Ablesungen; die Referenz ersetzt er nicht."
  - q: "Was ist ein proaktives Band bei einem Brennlauf?"
    a: "Eine Hüllkurve aus den eigenen guten Brennläufen der Brennerei, die zeigt, wo Stärke, Temperatur oder Durchfluss in jeder Phase eines Laufs normalerweise liegen. Ein neuer Lauf wird laufend mit dem Band verglichen. Sobald er beginnt, das Band zu verlassen, erfährt der Bediener das früh, oft lange bevor ein fester Alarmgrenzwert überschritten wird."
  - q: "Warum ignorieren Bediener in Brennereien Alarme?"
    a: "Weil es zu viele sind und die meisten kein Eingreifen erfordern. Leitfäden zum Alarmmanagement wie EEMUA 191 und ISA-18.2 behandeln eine Alarmflut als eigenes Sicherheitsproblem. Jeder Störalarm lehrt den Bediener, dass man Alarme quittieren und vergessen kann, und genau das ist die falsche Lektion, wenn ein echter kommt."
---

**Kurze Antwort: Das Aräometer im Spirit Safe ist die Wahrheit, aber es wird mit dem Auge abgelesen und nicht jede Minute. Zwischen den Ablesungen kann ein Soft Sensor die Stärke aus Dampf- und Blasentemperatur, Druck und Durchfluss schätzen und sich jedes Mal nachkalibrieren, wenn der Brennmeister abliest. Vergleiche die Schätzung mit einem Band aus den eigenen guten Brennläufen der Brennerei, indiziert nach dem Fortschritt des Laufs statt nach der Uhrzeit, und du erkennst einen driftenden Lauf früh, solange sich noch nachsteuern lässt. Ein fester Alarm für zu niedrige Stärke sagt dir dasselbe zwanzig Minuten später, auf einem Panel, das der Bediener schon stummzuschalten gelernt hat.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Ein Banddiagramm für einen Feinbrand. Die horizontale Achse zeigt den Anteil des gewonnenen Füllalkohols, die vertikale Achse die Destillatstärke. Ein schattiertes Band aus guten Läufen fällt nach rechts ab. Ein normaler Lauf bleibt darin. Ein driftender Lauf verlässt den unteren Rand des Bands etwa in der Mitte des Laufs, wo eine pinke Markierung zeigt, dass das Band ihn meldet. Denselben festen Alarm für niedrige Stärke überschreitet der Lauf erst viel später, wo eine zweite Markierung zeigt, dass der Alarm auslöst.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DAS BAND SIEHT DIE DRIFT VOR DEM ALARM (BEISPIEL)</text>
<g font-family="sans-serif">
<line x1="100" y1="280" x2="910" y2="280" stroke="#4a6b64" stroke-width="1"/>
<line x1="100" y1="60" x2="100" y2="280" stroke="#4a6b64" stroke-width="1"/>
<text x="505" y="302" text-anchor="middle" font-size="10.5" fill="#4a6b64">Anteil des gewonnenen Füllalkohols &#8594;</text>
<text x="88" y="170" text-anchor="middle" font-size="10.5" fill="#4a6b64" transform="rotate(-90 88 170)">Stärke am Safe</text>
<polygon points="100,80 300,100 500,130 700,175 900,235 900,265 700,205 500,160 300,128 100,105" fill="#f0f6f5" stroke="#4db6a2" stroke-width="1"/>
<polyline points="100,92 300,114 500,145 700,190 900,250" fill="none" stroke="#06483f" stroke-width="2.5"/>
<polyline points="100,92 300,118 400,140 500,172 600,200 700,228" fill="none" stroke="#ff4081" stroke-width="2.5"/>
<line x1="100" y1="225" x2="900" y2="225" stroke="#4a6b64" stroke-width="1.5" stroke-dasharray="6 5"/>
<text x="905" y="219" text-anchor="end" font-size="10.5" fill="#4a6b64">fester Alarm für niedrige Stärke</text>
<circle cx="450" cy="156" r="7" fill="none" stroke="#ff4081" stroke-width="2.5"/>
<text x="450" y="196" text-anchor="middle" font-size="11" font-weight="700" fill="#ff4081">Band meldet hier</text>
<circle cx="690" cy="225" r="7" fill="none" stroke="#06483f" stroke-width="2.5"/>
<text x="690" y="252" text-anchor="middle" font-size="11" font-weight="700" fill="#06483f">Alarm löst hier aus</text>
<text x="230" y="76" font-size="10.5" fill="#00695c">Band aus guten Läufen</text>
<text x="780" y="170" font-size="10.5" fill="#06483f">normaler Lauf</text>
<rect x="40" y="312" width="920" height="24" rx="6" fill="#06483f"/>
<text x="500" y="329" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">GLEICHER LAUF, GLEICHE DATEN &#183; NUR EINES LÄSST ZEIT ZUM HANDELN</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Beispielhafter Verlauf. Das Band entsteht aus deinen eigenen guten Läufen, und die x-Achse ist der Fortschritt des Laufs, nicht die Uhrzeit.</figcaption>
</figure>

An einer Feinbrandblase wird die wichtigste Zahl im ganzen Gebäude durch Glas abgelesen. Der Brennmeister schaut auf das Aräometer, das im Spirit Safe schwimmt, korrigiert die Temperatur und schreibt den Wert auf. Diese Ablesung ist die Referenz. Sie erfolgt aber auch nur in Abständen, durch einen Menschen, der vier andere Dinge zu tun hat, und in einer vollen Schicht werden die Abstände zwischen den Ablesungen größer.

Der [vorige Beitrag]({{ '/de/2026/physics-informed-digital-twin-pot-still/' | relative_url }}) hat einen Zwilling gebaut, der weiß, wohin ein Lauf gehen sollte. In diesem geht es darum, einen laufenden Brand gegen diese Erwartung zu beobachten, ohne den Stapel an Alarmen zu vergrößern, die niemand liest.

## Der Soft Sensor: Stärke zwischen den Ablesungen

Ein Soft Sensor schätzt etwas, das man nicht kontinuierlich messen kann, aus Größen, die man messen kann. An einer Pot Still liegen die nützlichen Eingangsgrößen in den meisten Historians bereits vor:

- **Temperatur der Flüssigkeit in der Blase.** Bei gegebenem Druck folgt die Siedetemperatur von Ethanol und Wasser der Zusammensetzung der Flüssigkeit in der Blase.
- **Dampftemperatur am Geistrohr oder Kolonnenkopf.** Sie folgt der Zusammensetzung des austretenden Dampfes.
- **Luftdruck.** Siedepunkte verschieben sich mit dem Wetter. Eine kräftige Wetterfront kann sie um mehrere Zehntelgrad verschieben, und das reicht, um eine naive Schätzung zu täuschen.
- **Destillatfluss und kumulierte Menge**, um zu wissen, wie weit der Lauf fortgeschritten ist.

Eine physikbasierte Schätzung aus den Gleichgewichtsdaten, korrigiert mit den angepassten Parametern aus dem Zwilling, liefert alle paar Sekunden einen Stärkewert. Dann kommt der Teil, der sie vertrauenswürdig macht: Jedes Mal, wenn der Brennmeister das Aräometer abliest, vergleicht der Soft Sensor seine Schätzung mit der Ablesung und korrigiert seinen Bias. Die Ablesung bleibt die Referenz. Der Soft Sensor füllt die Lücken dazwischen, und seine Abweichung gegenüber der letzten Ablesung wird direkt daneben angezeigt, damit niemand vergisst, welche Zahl gemessen und welche geschätzt ist.

Das Data Engineering ist überschaubar, aber es zählt. Speichere die Aräometerablesungen mit Zeitstempel, Temperatur und der Person, die abgelesen hat, auf derselben Zeitachse wie die Historian-Tags. Ein Soft Sensor, der seine Schätzung nicht minutengenau mit der Ablesung abgleichen kann, kann sich nicht nachkalibrieren.

## Das Band: mit guten Läufen vergleichen, nicht mit einem Grenzwert

Ein fester Alarm stellt eine einzige Frage: Ist die Stärke unter X gefallen? Bis das der Fall ist, driftet der Lauf schon eine Weile.

Ein Band stellt eine bessere Frage: Verhält sich dieser Lauf an dieser Stelle so wie unsere guten Läufe? So baut man eines:

1. **Die guten Läufe auswählen.** Die letzten dreißig oder fünfzig Läufe, bei denen sich das Team einig ist, dass sie gut gelaufen sind, auf derselben Brennblase und mit demselben Fülltyp.
2. **Nach Fortschritt indizieren, nicht nach Zeit.** Läufe dauern je nach Wärmezufuhr und Füllmenge unterschiedlich lang. Trage jeden Lauf gegen den Anteil des bereits gewonnenen Füllalkohols auf, aus der Bilanz des Zwillings, damit alle Läufe auf derselben Skala liegen.
3. **Median und eine robuste Streuung bilden**, an jedem Schritt (mittlere absolute Abweichung statt Standardabweichung, damit ein einzelner Ausreißer das Band nicht für alle verbreitert).
4. **Den laufenden Brand kontinuierlich vergleichen** und ihn melden, wenn er das Band verlässt oder schneller darauf zusteuert, als es ein guter Lauf je getan hat.

Im Beispieldiagramm verlässt der driftende Lauf das Band ein Drittel des Weges, bevor der feste Alarm auslösen würde. Diese Lücke ist der nützliche Teil. Sie ist die Zeit, um den Dampf zu prüfen, auf das Kühlwasser des Kondensators zu schauen oder früher als geplant das Aräometer abzulesen.

Bänder funktionieren nicht nur für die Stärke. Austrittstemperatur am Kondensator, Dampfmenge und Destillatfluss bekommen jeweils ein eigenes Band. Ein Lauf, der bei zwei davon gleichzeitig driftet, ist deutlich interessanter als einer, der bei einem den Rand streift.

## Warum weniger Alarme das Ziel sind

Zum Alarmmanagement gibt es eine ganze Fachliteratur, und ihre zentrale Erkenntnis ist unbequem: Mehr Alarme machen Anlagen unsicherer. Leitfäden wie EEMUA 191 und ISA-18.2 zielen im stationären Betrieb auf ungefähr einen Alarm alle zehn Minuten pro Bediener und behandeln Fluten darüber als eigenständiges Problem. Jeder Alarm, der auslöst und kein Eingreifen erfordert, lehrt den Bediener, dass man Alarme quittieren und vergessen kann.

Das Band soll Alarme also ersetzen, nicht zu ihnen hinzukommen. Eine gute Regel für eine Brennerei, die das einführt:

- **Sicherheitsalarme und Verriegelungen genau so lassen, wie sie sind.** Überdruck, Übertemperatur und Dampfdetektion sind keine Analytics-Probleme.
- **Die Störalarme im Prozess abschaffen**, die das Band abdeckt, einen nach dem anderen, sobald das Band gezeigt hat, dass es dieselben Ereignisse früher erkennt.
- **Bandmeldungen beratend und leise halten.** Ein Farbwechsel und ein Hinweis auf dem Bedienbildschirm, keine Hupe.
- **Jede Meldung in den ersten Monaten wöchentlich prüfen.** Ein Band, das zu oft meldet, ist zu eng. Eines, das nie meldet, ist zu weit.

## Wo das an Grenzen stößt

**Das Band lernt deine Gewohnheiten, gute wie schlechte.** Waren die guten Läufe alle etwas zu schnell, macht das Band zu schnell zur Normalität. Wähle die Referenzläufe bewusst aus und baue das Band neu, wenn sich der Prozess gewollt ändert.

**Soft Sensoren driften zwischen den Ablesungen.** Ein verschmutzter Temperaturfühler oder eine geänderte Dampfversorgung verschiebt die Schätzung, und das Band kann eine echte Drift nicht von einem schlechten Fühler unterscheiden. Deshalb bleibt die Aräometerablesung die Referenz, und deshalb steht die Abweichung des Soft Sensors dagegen immer auf dem Bildschirm.

**Anfang und Ende des Laufs sind am schwierigsten.** Beim Vorlauf und im Ausklang des Laufs ist das Gleichgewichtsmodell am schwächsten, und dort verlassen sich Bediener am stärksten auf Nase und Erfahrung. Setze Bänder für die Mitte des Laufs ein, wo sich die Physik gut verhält.

**Den Schnitt setzt es nicht.** Ein Band sagt dir, dass ein Lauf ungewöhnlich ist. Es sagt dir nicht, wo du für das Aroma schneiden sollst. Das bleibt beim Brennmeister, wie der [Beitrag zu den Schnittpunkten]({{ '/de/2024/predicting-distillation-cut-points-ai/' | relative_url }}) argumentiert.

## Das Fazit

Das Aräometer im Spirit Safe ist die Wahrheit, und es wird von einem Menschen in Abständen abgelesen. Ein Soft Sensor füllt die Lücken und bleibt ehrlich, weil er sich an jeder Ablesung nachkalibriert. Ein Band aus deinen eigenen guten Läufen zeigt Drift, solange noch Zeit zum Handeln bleibt, und es erlaubt dir, Alarme abzuschaffen, statt neue hinzuzufügen. Das Ziel ist keine klügere Hupe. Es ist ein ruhigeres Panel, auf dem die wenigen verbleibenden Signale einen Blick wert sind.

Als Nächstes in der Serie: [ein LLM-Copilot für den Brennblasenbediener]({{ '/de/2026/llm-copilot-still-operator/' | relative_url }}), der dieselben Daten liest und nie einen Sollwert anfasst. Zu den Sensoren selbst siehe [IoT in der Brennerei]({{ '/de/2026/iot-in-the-distillery-sensors-process/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite von The Still and the Model]({{ '/series/still-and-model/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist ein Soft Sensor in einer Brennerei?**
Ein Soft Sensor schätzt etwas, das man nicht kontinuierlich messen kann, etwa die Destillatstärke, aus Größen, die man messen kann, etwa Dampftemperatur, Blasentemperatur, Druck und Durchfluss. Er wird an einer echten Messung nachkalibriert, zum Beispiel am Aräometer im Spirit Safe, sobald eine vorliegt. Er füllt die Lücken zwischen den Ablesungen; die Referenz ersetzt er nicht.

**Was ist ein proaktives Band bei einem Brennlauf?**
Eine Hüllkurve aus den eigenen guten Brennläufen der Brennerei, die zeigt, wo Stärke, Temperatur oder Durchfluss in jeder Phase eines Laufs normalerweise liegen. Ein neuer Lauf wird laufend mit dem Band verglichen. Sobald er beginnt, das Band zu verlassen, erfährt der Bediener das früh, oft lange bevor ein fester Alarmgrenzwert überschritten wird.

**Warum ignorieren Bediener in Brennereien Alarme?**
Weil es zu viele sind und die meisten kein Eingreifen erfordern. Leitfäden zum Alarmmanagement wie EEMUA 191 und ISA-18.2 behandeln eine Alarmflut als eigenes Sicherheitsproblem. Jeder Störalarm lehrt den Bediener, dass man Alarme quittieren und vergessen kann, und genau das ist die falsche Lektion, wenn ein echter kommt.
