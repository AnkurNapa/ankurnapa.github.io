---
layout: post
lang: de
title: "Verbrauchsteuererklärungen als Datenverträge: Tests stimmen ab, das LLM entwirft, ein Mensch unterschreibt"
image: /assets/og/wine-excise-returns-data-contracts-genai.png
description: "Teil 5 von The Cellar Ledger. Die Verbrauchsteuererklärung eines Weinguts ist eine Bilanzgleichung je Steuerklasse. Ihre Eingangsdaten als Datenvertrag behandeln, die Gleichung jede Nacht in der Pipeline testen und GenAI dort einsetzen, wo sie hier gut ist: unordentliche Entnahmenotizen klassifizieren, Erläuterungen entwerfen und den richtigen Absatz in den Leitlinien finden."
date: 2026-07-12 09:00:00 -0700
updated: 2026-07-12
permalink: /de/2026/wine-excise-returns-data-contracts-genai/
tags: [winemaking, cellar-ledger, data-engineering, generative-ai, compliance]
faq:
  - q: "Was ist ein Datenvertrag im Kontext eines Weinguts?"
    a: "Eine schriftliche, durchgesetzte Vereinbarung darüber, was ein Datensatz enthalten muss. Für die Verbrauchsteuer könnte der Vertrag über das Bewegungsjournal festlegen, dass jede Entnahme eine Steuerklasse, eine Art des Bestimmungsorts und einen gemessenen Alkoholgehalt hat und dass der Anfangsbestand jedes Monats dem Endbestand des Vormonats entspricht. Die Pipeline testet diese Regeln und hält fehlerhafte Datensätze auf, bevor sie die Erklärung erreichen."
  - q: "Kann ein LLM eine Verbrauchsteuererklärung für Wein ausfüllen?"
    a: "Die Zahlen sollte es nicht ausfüllen. Die Werte stammen aus getesteten Abfragen über das Journal. Nützlich ist ein LLM rund um die Erklärung: Freitextnotizen zu Entnahmen in Kategorien einordnen, die Erläuterung für einen ungewöhnlichen Verlust entwerfen und den passenden Absatz in den Leitlinien finden, den ein Mensch dann liest. Eine namentlich benannte Person prüft und unterschreibt jede Erklärung."
  - q: "Warum verursachen Steuerklassen bei Wein Abstimmungsprobleme?"
    a: "Weil eine Partie die Klasse wechseln kann, ohne das Gebäude zu verlassen. In den USA wird Stillwein zum Beispiel in Stufen nach Alkoholgehalt besteuert, mit einer Grenze bei 16 Prozent. Ein Verschnitt, eine Aufspritung oder ein korrigierter Laborwert kann eine Partie über diese Grenze schieben, und wird der Wechsel nicht als Ereignis erfasst, geht die Bilanz je Klasse nicht mehr auf."
---

**Kurze Antwort: Eine Verbrauchsteuererklärung ist eine Bilanzgleichung je Steuerklasse: Anfangsbestand plus Erzeugung und Zugänge, minus Entnahmen und Verluste, ergibt den Endbestand. Wird diese Gleichung am Monatsende von Hand in ein Formular übertragen, zeigt sich jeder Fehler im ungünstigsten Moment. Behandelt man die Eingangsdaten der Erklärung als Datenvertrag über das Bewegungsjournal und testet die Gleichung jede Nacht in der Pipeline, wird die Erklärung zu einer Abfrage, die ihre Prüfungen schon bestanden hat. GenAI hilft an den Rändern: unordentliche Entnahmenotizen sortieren, die Erläuterung für einen auffälligen Verlust entwerfen und den richtigen Absatz in den Leitlinien finden. Die Zahlen erzeugt sie nicht, und sie unterschreibt nicht.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Die Verbrauchsteuer-Bilanzgleichung für eine Steuerklasse: Anfangsbestand, plus Erzeugung und Zugänge, minus versteuerte Entnahmen, minus Abgänge unter Steueraussetzung oder in den Export, minus Verluste, ergibt den Endbestand. Darunter drei nächtliche Tests aus dem Datenvertrag: Der Anfangsbestand entspricht dem Endbestand des Vormonats, die Gleichung geht je Klasse auf null auf, und jeder Klassenwechsel wird als Ereignis erfasst. Ein Banner sagt, dass die Erklärung eine Abfrage ist, die ihre Tests bereits bestanden hat.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">EINE STEUERKLASSE, EINE GLEICHUNG, JEDE NACHT GETESTET</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="130" height="64" rx="9" fill="#06483f"/>
<text x="95" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">Anfangs-</text>
<text x="95" y="108" text-anchor="middle" font-size="10" fill="#cfe6df">bestand</text>
<text x="177" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">+</text>
<rect x="195" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="260" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">erzeugt</text>
<text x="260" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">&amp; zugegangen</text>
<text x="342" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="360" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="425" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">entnommen</text>
<text x="425" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">versteuert</text>
<text x="507" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="525" y="60" width="130" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="590" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">steuerfrei</text>
<text x="590" y="108" text-anchor="middle" font-size="10" fill="#4a6b64">&amp; Export</text>
<text x="672" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">&#8722;</text>
<rect x="690" y="60" width="110" height="64" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="745" y="98" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Verluste</text>
<text x="817" y="98" text-anchor="middle" font-size="20" font-weight="700" fill="#00695c">=</text>
<rect x="835" y="60" width="130" height="64" rx="9" fill="#06483f"/>
<text x="900" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">End-</text>
<text x="900" y="108" text-anchor="middle" font-size="10" fill="#cfe6df">bestand</text>
<text x="500" y="160" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">TESTS AUS DEM DATENVERTRAG</text>
<rect x="30" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="180" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; Anfang = letzter Endbestand</text>
<text x="180" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">keine stillen Änderungen zwischen Monaten</text>
<rect x="350" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="500" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; Gleichung geht auf 0 auf</text>
<text x="500" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">je Steuerklasse, je Monat</text>
<rect x="670" y="175" width="300" height="64" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="820" y="203" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">&#10003; Klassenwechsel sind Ereignisse</text>
<text x="820" y="222" text-anchor="middle" font-size="10.5" fill="#4a6b64">ein Verschnitt über 16% wird erfasst</text>
<rect x="30" y="262" width="940" height="42" rx="10" fill="#06483f"/>
<text x="500" y="288" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">DIE ERKLÄRUNG IST EINE ABFRAGE, DIE IHRE TESTS SCHON BESTANDEN HAT</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Dieselbe Gleichung, die der Zollbeamte prüft, getestet von der Pipeline jede Nacht statt von einem Menschen am Monatsende.</figcaption>
</figure>

Es ist der zweite Arbeitstag des Monats, und die Verbrauchsteuererklärung ist fällig. Jemand öffnet die Erklärung des Vormonats, öffnet das Kellersystem und beginnt, Zahlen ins Formular zu übertragen. Der Anfangsbestand passt nicht zum Endbestand des Vormonats. Jemand hat zwischendurch ein Tankvolumen geändert. Die nächsten drei Stunden gehen dafür drauf, herauszufinden, welches, während die Frist näher rückt.

Das ist der unspektakulärste Beitrag der Serie und womöglich der nützlichste. Jedes Weingut, das Steuern zahlt, lebt damit, und die meisten lösen es mit einem Menschen und einem Taschenrechner. Das [Bewegungsjournal]({{ '/de/2026/event-sourced-cellar-records-winery/' | relative_url }}) und die [Verlustkarte]({{ '/de/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}) haben den Großteil der Arbeit schon erledigt. Dieser Beitrag ergänzt die Regeln, die die Erklärung vertrauenswürdig machen, bevor jemand das Formular öffnet.

## Die Erklärung ist eine Bilanzgleichung

Egal in welchem Land: Die Verbrauchsteuererklärung eines Weinguts läuft für jede Steuerklasse auf dieselbe Identität hinaus:

> Anfangsbestand + Erzeugung und Zugänge - versteuerte Entnahmen - Abgänge unter Steueraussetzung oder in den Export - Verluste = Endbestand

In den USA ist das der monatliche Report of Wine Premises Operations, aufgeschlüsselt nach Steuerklasse. In der EU laufen Beförderungen unter Steueraussetzung über EMCS. In Indien hat jede bundesstaatliche Verbrauchsteuerbehörde ihre eigenen Register und Formate. Die Formulare unterscheiden sich. Die Arithmetik nicht.

Das ist eine gute Nachricht für ein Datenteam, denn eine Identität lässt sich in einer Pipeline testen.

## Die Falle der Steuerklassen

Der heikle Teil ist das "je Steuerklasse". Wein wird in Stufen besteuert. In den USA ist Stillwein mit bis zu 16% Alkohol eine Klasse, über 16 bis 21% eine andere, über 21 bis 24% eine weitere, Schaumwein und kohlensäurehaltiger Wein sind getrennt. Andere Märkte ziehen ihre eigenen Grenzen.

Eine Partie kann die Klasse wechseln, ohne das Gebäude zu verlassen. Verschneidet man eine Partie mit 15,8% mit einer mit 16,6%, kann das Ergebnis je nach Volumen auf beiden Seiten von 16% liegen. Wird aufgespritet, springt eine Partie die Klasse. Wird ein Laborwert korrigiert, liegt eine Partie, die im Vormonat unter 16% gemeldet wurde, plötzlich darüber.

Werden diese Wechsel nicht erfasst, geht die Gleichung je Klasse nicht mehr auf, und niemand weiß, warum. Also wird der Klassenwechsel selbst zu einem Ereignis im Journal: Partie 24-SH-03 wechselt an diesem Datum mit diesem Volumen wegen dieses Verschnitts von Klasse A nach Klasse B. Das ist auch der Grund, warum der [erste Beitrag dieser Serie]({{ '/de/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}) darauf bestand, den vorhergesagten Alkohol durch den gemessenen zu ersetzen. Eine Steuerklasse, die auf einer Faustformel beruht, ist ein Problem, das nur auf einen Prüfer wartet.

## Den Datenvertrag schreiben

Ein Datenvertrag ist eine schriftliche Vereinbarung darüber, was ein Datensatz enthalten muss, durchgesetzt von der Pipeline statt von guten Vorsätzen. Für die Verbrauchsteuer ist der Vertrag über das Bewegungsjournal kurz:

1. **Jede Entnahme hat eine Steuerklasse, eine Art des Bestimmungsorts und einen gemessenen Alkoholgehalt.** Versteuert, unter Steueraussetzung, Export, Probe, vernichtet. Eine Entnahme ohne Bestimmungsort wird abgewiesen.
2. **Jeder Klassenwechsel ist ein Ereignis.** Überschreitet der gemessene Alkohol einer Partie eine Klassengrenze, erwartet die Pipeline ein Klassenwechsel-Ereignis und meldet, wenn es fehlt.
3. **Anfangsbestand gleich letzter Endbestand.** Für jede Klasse, jeden Monat. Dieser eine Test fängt jede stille Änderung ab.
4. **Die Identität geht auf null auf.** Je Klasse, je Monat, innerhalb einer Toleranz, die mit der Buchhaltung abgestimmt ist. Ein Rest ungleich null blockiert die Erklärung, bis jemand ihn erklärt.
5. **Keine negativen Bestände.** Eine Klasse mit negativem Endvolumen bedeutet, dass ein Ereignis fehlt oder falsch klassifiziert ist.

In der Praxis sind das eine Handvoll Tests in dem, was ohnehin im Einsatz ist: dbt-Tests, Great Expectations, Datenqualitätsregeln in Fabric oder einfache SQL-Assertions, die den nächtlichen Job scheitern lassen. Die wichtige Entscheidung ist, sie **jede Nacht** laufen zu lassen, nicht am Monatsende. Ein Test, der am 14. fehlschlägt, lässt zwei Wochen Zeit, den Datensatz zu korrigieren, solange sich die Leute noch erinnern, was passiert ist. Ein Test, der am 2. fehlschlägt, beschert einen schlechten Morgen.

Datensätze, die durchfallen, landen mit der verletzten Regel in einer Quarantänetabelle, nicht im Nirgendwo. Das Kellerteam sieht eine kurze Liste von Dingen, die zu korrigieren sind. Die Erklärung sieht sie erst, wenn sie korrigiert sind.

## Wo GenAI tatsächlich hilft

Wenn die Zahlen von getesteten Abfragen kommen, sind die nützlichen Aufgaben für ein Sprachmodell diejenigen mit unordentlichem Text.

**Entnahmenotizen klassifizieren.** Mitarbeiter schreiben Dinge wie "2 Kt. zur Sonntagsverkostung", "Bruch, Palette runtergefallen" oder "Probe für Messe". Daraus müssen Kategorien werden: Probe, Verkostungsraum, Bruch, vernichtet. Ein Modell klassifiziert das gut, mit einem Konfidenzwert, und schickt alles Unsichere an einen Menschen. Eine kleine Aufgabe, die jeden Monat Stunden spart.

**Die Erläuterungen entwerfen.** Ist ein Verlust größer als üblich, braucht die Erklärung oder die interne Akte eine Notiz, warum. Das Modell entwirft sie aus den Zahlen der Verlustkarte und den Korrekturgründen, nach demselben Muster wie die [Abweichungsnotiz]({{ '/de/2026/winery-loss-map-medallion-pipeline-genai/' | relative_url }}): SQL liefert jede Zahl, das Modell schreibt die Worte drumherum.

**Den richtigen Absatz finden.** Verbrauchsteuer-Leitlinien sind lang und werden oft aktualisiert. Ein Retrieval-Assistent über die veröffentlichten Leitlinien der Behörde, der den Absatz zitiert und verlinkt, spart echte Zeit, wenn eine Frage aufkommt: "Wie behandeln wir Wein, der zum Auffüllen in einem anderen Steuerlager verwendet wird?". Er ist ein Bibliothekar. Den Absatz liest trotzdem ein Mensch, und er trifft die Entscheidung.

**Dem Beamten antworten.** Fragt ein Zollbeamter, warum sich der Bestand einer Klasse verändert hat, kann ein Agent mit Lesezugriff auf das Journal die genauen Ereignisse, Daten und Bearbeiter heraussuchen und eine Antwort mit den angehängten Zeilen entwerfen. Die Antwort geht raus, nachdem ein Mensch sie geprüft hat.

Was er nicht darf: die Erklärung ausfüllen, das Recht auslegen oder entscheiden, wie eine Bewegung in einer Grauzone zu behandeln ist. Das sind Urteile mit rechtlichem Gewicht, und sie gehören zu einer namentlich benannten Person.

## Wo das an Grenzen stößt

**Regeln unterscheiden sich und ändern sich.** Steuerklassen, zulässige Verluste und Meldeformate variieren von Land zu Land und in Indien von Bundesstaat zu Bundesstaat. Der Vertrag muss die eigenen Regeln abbilden, von jemandem geprüft, der sie kennt, und bei Änderungen aktualisiert werden.

**Verträge, die den Monatsabschluss blockieren, werden umgangen.** Stoppt ein fehlschlagender Test die Erklärung am 2. ohne Ausweg, findet jemand einen Weg drumherum. Die Tests nächtlich laufen lassen und den Quarantäne-Pfad so gestalten, dass das Korrigieren eines Datensatzes einfacher ist, als die Pipeline zu umgehen.

**Zulässiger Verlust ist eine regulatorische Frage, keine statistische.** Die Verlustkarte kann zeigen, dass ein Verlust ungewöhnlich ist. Ob er im Rahmen dessen liegt, was die Behörde erlaubt, und ob er steuerpflichtig ist, entscheiden die Regeln und die Person, die unterschreibt.

**Retrieval kann den falschen Absatz liefern.** Veraltete Leitlinien im Index oder ein Absatz, der nah dran, aber nicht ganz einschlägig ist, werden mit großer Sicherheit zurückgegeben. Den Index aktuell halten und immer die Quelle lesen.

## Das Fazit

Die Verbrauchsteuererklärung ist der eine Bericht, bei dem jede Zahl von jemandem außerhalb des Unternehmens geprüft wird. Das macht sie zum besten Ort, um mit dem Abschreiben von Zahlen von Hand aufzuhören. Die Regeln der Erklärung als Datenvertrag aufschreiben, sie jede Nacht testen, und der Monatsabschluss wird zur Durchsicht statt zur Suche. GenAI dort einsetzen, wo das Chaos aus Text besteht, Notizen sortieren und Erläuterungen entwerfen, und die Zahlen und die Unterschrift bei Menschen und getestetem Code lassen.

Als Nächstes und zum Abschluss der Serie: [wo KI im Weingut an Grenzen stößt]({{ '/de/2026/where-winery-ai-breaks-ten-vintages-ten-rows/' | relative_url }}) und warum zehn Jahrgänge nur zehn Zeilen sind. Die vollständige Liste steht auf der [Seite zur Serie Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist ein Datenvertrag im Kontext eines Weinguts?**
Eine schriftliche, durchgesetzte Vereinbarung darüber, was ein Datensatz enthalten muss. Für die Verbrauchsteuer könnte der Vertrag über das Bewegungsjournal festlegen, dass jede Entnahme eine Steuerklasse, eine Art des Bestimmungsorts und einen gemessenen Alkoholgehalt hat und dass der Anfangsbestand jedes Monats dem Endbestand des Vormonats entspricht. Die Pipeline testet diese Regeln und hält fehlerhafte Datensätze auf, bevor sie die Erklärung erreichen.

**Kann ein LLM eine Verbrauchsteuererklärung für Wein ausfüllen?**
Die Zahlen sollte es nicht ausfüllen. Die Werte stammen aus getesteten Abfragen über das Journal. Nützlich ist ein LLM rund um die Erklärung: Freitextnotizen zu Entnahmen in Kategorien einordnen, die Erläuterung für einen ungewöhnlichen Verlust entwerfen und den passenden Absatz in den Leitlinien finden, den ein Mensch dann liest. Eine namentlich benannte Person prüft und unterschreibt jede Erklärung.

**Warum verursachen Steuerklassen bei Wein Abstimmungsprobleme?**
Weil eine Partie die Klasse wechseln kann, ohne das Gebäude zu verlassen. In den USA wird Stillwein zum Beispiel in Stufen nach Alkoholgehalt besteuert, mit einer Grenze bei 16 Prozent. Ein Verschnitt, eine Aufspritung oder ein korrigierter Laborwert kann eine Partie über diese Grenze schieben, und wird der Wechsel nicht als Ereignis erfasst, geht die Bilanz je Klasse nicht mehr auf.
