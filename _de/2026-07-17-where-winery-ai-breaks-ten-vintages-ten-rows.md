---
layout: post
lang: de
title: "Wo KI im Weingut an Grenzen stößt: Zehn Jahrgänge sind zehn Zeilen"
image: /assets/og/where-winery-ai-breaks-ten-vintages-ten-rows.png
description: "Teil 6 von The Cellar Ledger. Eine Brauerei braut Hunderte Sude im Jahr. Ein Weingut bekommt einen Jahrgang. Warum Modelle, die Jahrgangsergebnisse vorhersagen, überanpassen, wo die Daten im Weingut tatsächlich reichhaltig sind und was Zeitreihen-Foundation-Models, synthetische Daten und LLMs gegen ein Problem mit wenigen Daten ausrichten können und was nicht."
date: 2026-07-17 09:00:00 -0700
updated: 2026-07-17
permalink: /de/2026/where-winery-ai-breaks-ten-vintages-ten-rows/
tags: [winemaking, cellar-ledger, machine-learning, generative-ai, data-strategy]
faq:
  - q: "Warum ist maschinelles Lernen im Weingut schwieriger als in der Brauerei?"
    a: "Weil die Lerneinheit oft der Jahrgang ist, und ein Weingut bekommt einen pro Jahr. Zehn Jahre Historie ergeben zehn Zeilen je Parzelle für Fragen wie Lesetermin, Ertrag oder Qualitätsbewertung, während eine Brauerei mit Hunderten Suden im Jahr Tausende hat. Modelle, die auf zehn Zeilen trainiert werden, lernen die Vergangenheit meist auswendig, statt aus ihr zu lernen."
  - q: "Können synthetische Daten oder ein Foundation Model einen kleinen Datensatz im Weingut retten?"
    a: "Allein nicht. Synthetische Daten, die aus den eigenen zehn Jahrgängen erzeugt werden, enthalten keine Information, die diese zehn Jahrgänge nicht schon hatten. Zeitreihen-Foundation-Models können eine brauchbare Zero-Shot-Prognose für eine Kurve liefern, etwa für eine Gärung, wissen aber nichts über den eigenen Weinberg. Beide sind in einem soliden Design nützlich, und keines von beiden erzeugt die fehlende Historie."
  - q: "Wo funktioniert KI im Weingut wirklich?"
    a: "Dort, wo die Daten innerhalb einer einzigen Saison reichhaltig sind: Gärkurven aus jedem Tank, Sensordaten aus dem Keller, Beerenproben während der Reife und Freitext wie Verkostungsnotizen und Kellerprotokolle. Modelle, die die Dynamik einer Gärung lernen, oder ein LLM, das die Protokolle liest, haben Hunderte oder Tausende Beispiele pro Jahr zur Verfügung."
---

**Kurze Antwort: Die meiste KI, die Weingütern angeboten wird, versucht ein Jahrgangsergebnis vorherzusagen, etwa Lesetermin, Ertrag oder eine Qualitätsbewertung, und ein Weingut bekommt einen Jahrgang pro Jahr. Zehn Jahre Historie sind zehn Zeilen je Parzelle. Modelle, die darauf trainiert werden, lernen vor allem auswendig, und das Klima, aus dem diese zehn Jahre stammen, verändert sich bereits. Innerhalb einer Saison sind die Daten dagegen reichhaltig: die Gärkurve jedes Tanks, jeder Sensor, jede Beerenprobe und jede Kellernotiz. Dort sollte man die KI bauen, über Parzellen hinweg bündeln, wo man über Jahre hinweg vorhersagen muss, und sehr skeptisch sein bei allem, was behauptet, ein Foundation Model, synthetische Daten oder ein LLM habe aus zehn Zeilen tausend gemacht.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Drei horizontale Balken vergleichen zehn Jahre an Trainingsbeispielen. Eine Brauerei mit 300 Suden im Jahr hat 3.000 Sud-Zeilen. Ein Weingut mit 120 Gärungen im Jahr hat 1.200 Gärkurven. Dasselbe Weingut hat 10 Jahrgangszeilen je Parzelle für Fragen wie Lesetermin oder Ertrag. Der Balken mit 10 Zeilen ist winzig und pink hervorgehoben.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">ZEHN JAHRE HISTORIE, GEZÄHLT IN TRAININGSBEISPIELEN (ILLUSTRATIV)</text>
<g font-family="sans-serif">
<text x="40" y="80" font-size="12" font-weight="700" fill="#06483f">Brauerei-Sude</text>
<text x="40" y="97" font-size="10.5" fill="#4a6b64">300 pro Jahr</text>
<rect x="260" y="66" width="600" height="34" rx="6" fill="#06483f"/>
<text x="872" y="89" font-size="13" font-weight="700" fill="#06483f">3.000</text>
<text x="40" y="150" font-size="12" font-weight="700" fill="#06483f">Gärungen im Weingut</text>
<text x="40" y="167" font-size="10.5" fill="#4a6b64">120 Tanks pro Jahr, in der Saison</text>
<rect x="260" y="136" width="240" height="34" rx="6" fill="#4db6a2"/>
<text x="512" y="159" font-size="13" font-weight="700" fill="#06483f">1.200</text>
<text x="40" y="220" font-size="12" font-weight="700" fill="#06483f">Jahrgänge im Weingut</text>
<text x="40" y="237" font-size="10.5" fill="#4a6b64">je Parzelle, Lesetermin oder Ertrag</text>
<rect x="260" y="206" width="4" height="34" rx="1" fill="#ff4081"/>
<text x="276" y="229" font-size="13" font-weight="700" fill="#ff4081">10</text>
<rect x="40" y="266" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="291" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">DIE KI DORT BAUEN, WO DIE ZEILEN SIND &#183; EHRLICH SEIN, WO SIE FEHLEN</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Dasselbe Weingut, dieselben zehn Jahre. Innerhalb einer Saison sind die Daten reichhaltig, über die Saisons hinweg dünn.</figcaption>
</figure>

Ein Anbieter zeigt einem Weingut ein Modell, das für jede Parzelle den optimalen Lesetermin vorhersagt. Die Demo sieht gut aus. Das Genauigkeitsdiagramm sieht noch besser aus. Dann fragt jemand, mit wie vielen Jahrgängen es trainiert wurde, und die Antwort lautet: elf.

Elf Lesen sind elf Zeilen je Parzelle. Eine Brauerei mit 300 Suden im Jahr sammelt in zwei Wochen mehr Beispiele für eine Gärung, als dieses Weingut in einem Jahrzehnt an Leseterminen sammelt. Das ist keine Kritik am Anbieter oder am Weingut. Es ist die Form des Geschäfts, und es ist der Grund, warum so viel KI im Weingut in der Demo glänzend aussieht und in der zweiten Saison gewöhnlich.

Dies ist der letzte Beitrag von **The Cellar Ledger**. Die ersten fünf handelten vom Aufbau des Datenfundaments. Dieser handelt davon, was man ehrlich darauf bauen kann.

## Warum zehn Zeilen täuschen

Mit zehn Zeilen und einer Handvoll Merkmale (Wachstumsgradtage, Niederschlag, ein paar Beerenmessungen) kann fast jedes Modell die Vergangenheit eng nachbilden. Genau das ist das Problem. Eine enge Anpassung an zehn Punkte ist vor allem Gedächtnis. Das Modell hat gelernt, welches Jahr welches war, nicht wie der Weinberg funktioniert.

Drei Dinge machen es beim Wein schlimmer:

- **Das Klima bewegt sich.** Die zehn Jahre im Trainingssatz sind keine faire Stichprobe der nächsten zehn. Ein Erwärmungstrend bedeutet, dass der nächste Jahrgang per Definition außerhalb des Bereichs liegt, den das Modell gesehen hat.
- **Der Weinberg verändert sich.** Reben altern, Parzellen werden neu bepflanzt, Bewässerung und Laubwandpraxis ändern sich. Der zehnte Jahrgang einer Parzelle ist nicht dieselbe Parzelle wie ihr erster.
- **Das Ziel ist weich.** Der Lesetermin ist zum Teil eine Entscheidung, geprägt von der Wettervorhersage, den Lesemannschaften und dem Tankplatz. Qualitätsbewertungen sind das Urteil eines Panels. Trainiert man ein Modell darauf, eine Entscheidung vorherzusagen, reproduziert es die alten Entscheidungen, samt aller Gewohnheiten.

Der ehrliche Weg, ein solches Modell zu testen, ist Leave-one-vintage-out: auf neun Jahren trainieren, das zehnte vorhersagen, für jedes Jahr wiederholen. Selbst das hat einen Haken. Zehn Folds liefern eine verrauschte Schätzung des Fehlers selbst, also ist ein Modell, das etwas besser aussieht als die Faustregel des Kellermeisters, womöglich gar nicht besser.

## Wo die Zeilen tatsächlich sind

Die gute Nachricht: Einem Weingut fehlen keine Daten. Es fehlen Jahrgänge. Innerhalb jeder Saison gibt es reichlich:

- **Gärkurven.** Jeder Tank ist eine eigene Gärung, mit Dichte und Temperatur mehrmals täglich protokolliert. Ein Weingut mit 120 Gärungen im Jahr hat nach zehn Jahren 1.200 Kurven, jede mit Hunderten Punkten. Das reicht, um zu lernen, wie eine gesunde Gärung aussieht, und eine schleppende früh zu erkennen, worum es im [Beitrag zur Gärsteuerung]({{ '/de/2024/ai-wine-fermentation-control/' | relative_url }}) geht.
- **Sensordaten.** Tanktemperaturen, Kellerfeuchte, Bedingungen im Fasslager. Kontinuierliche Daten, gut für Anomalieerkennung und Soft Sensors.
- **Beerenproben während der Reife.** Wöchentlich Brix, Säure und pH je Parzelle über die Saison. Nicht genug, um das Ergebnis eines Jahrgangs von Grund auf vorherzusagen, aber genug, um die Reifekurve dieser Saison mit den letzten paar zu vergleichen.
- **Text.** Verkostungsnotizen, Kellerprotokolle, Arbeitsaufträge, Korrekturgründe. Jahre davon, meist ungelesen. Hier glänzen große Sprachmodelle wirklich.

Das Muster: Modelle, die die **Dynamik innerhalb einer Saison** lernen, haben echte Daten. Modelle, die das **Ergebnis über Saisons hinweg** lernen, meist nicht.

## Das Beste aus dünnen Daten machen

Wenn man tatsächlich über Jahrgänge hinweg vorhersagen muss, helfen ein paar Techniken mehr als ein größeres Modell.

**Über Parzellen bündeln.** Ein hierarchisches Modell (Mixed Effects) teilt Information zwischen Parzellen und lässt trotzdem jede Parzelle abweichen. Vierzig Parzellen mal zehn Jahrgänge sind nicht vierhundert unabhängige Zeilen, aber viel besser als zehn.

**Bei der Wissenschaft anfangen.** Phänologiemodelle auf Basis der Wärmesumme, dieselbe Logik der Wachstumsgradtage wie bei der [Reifevorhersage]({{ '/de/2024/predicting-grape-ripeness-harvest-date/' | relative_url }}), bringen Jahrzehnte weinbaulicher Forschung mit. Die Daten sollen ein solides Modell justieren, statt aus zehn Punkten die Botanik entdecken zu müssen.

**Die Saison vorhersagen, nicht den Jahrgang.** Statt im April den Lesetermin vorherzusagen, jede Woche eine Reifeprognose aktualisieren, sobald Beerenproben eintreffen. Jede Wochenprobe ist eine neue Zeile, und die Prognose muss nur wenige Wochen vorausreichen.

**Regionale und öffentliche Daten nutzen.** Aufzeichnungen von Wetterstationen, regionale Ernteberichte und Vegetationsindizes aus Satellitendaten decken mehr Jahre und mehr Weinberge ab als die Aufzeichnungen eines einzelnen Weinguts.

## Was die neuen Werkzeuge können und was nicht

Die naheliegende Frage 2026 ist, ob die neueste KI-Generation daran etwas ändert. Teilweise.

**Zeitreihen-Foundation-Models** (Modelle wie Chronos oder TimesFM, vortrainiert auf riesigen Mengen fremder Zeitreihen) können eine Kurve, die sie nie gesehen haben, zero-shot prognostizieren. Für eine Gärkurve ist das nützlich: eine brauchbare Prognose der nächsten zwei Tage aus den ersten drei, ohne Training auf den eigenen Daten. Für ein Jahrgangsergebnis haben sie nichts, womit sie arbeiten könnten. Sie wissen, wie Kurven im Allgemeinen aussehen. Den eigenen Weinberg kennen sie nicht.

**Synthetische Daten** werden oft als Lösung für kleine Datenmengen angeboten. Das können sie nicht sein. Synthetische Jahrgänge, die aus den zehn echten Jahrgängen erzeugt werden, enthalten keine Information, die diese zehn nicht schon hatten. Sie können helfen, eine Pipeline zu testen oder ein Modell gegen extreme Szenarien zu prüfen, aber sie bringen dem Modell nichts Neues über Trauben bei.

**LLMs** sind brillant mit Text: zehn Jahre Kellerprotokolle zusammenfassen, die Sprache von Verkostungsnotizen clustern, Fragen zu den eigenen SOPs beantworten, Berichte entwerfen, alles weiter oben in dieser Serie behandelt. Bittet man ein LLM, einen Lesetermin vorherzusagen, liefert es einen, in einem selbstsicheren Satz. Aus den eigenen Daten wird es dafür nichts gelernt haben. Genau darauf sollte man in einer Demo achten.

## Wo das an Grenzen stößt

**Große Erzeuger sind anders.** Eine Gruppe mit Dutzenden Weingütern und Hunderten Parzellen hat weit mehr Zeilen, und jahrgangsübergreifende Modelle werden vernünftiger. Das Zehn-Zeilen-Problem trifft ein einzelnes Weingut am härtesten.

**Modelle innerhalb der Saison können bei neuen Bedingungen trotzdem versagen.** Ein Gärmodell, das auf zehn normalen Jahrgängen trainiert wurde, erkennt die Stressmuster einer Hitzewellen-Lese, die es nie gesehen hat, womöglich nicht. Reichhaltige Daten innerhalb der Saisons ersparen nicht den Blick auf ungewöhnliche Jahre.

**Bündeln setzt voraus, dass die Parzellen ähnlich genug sind.** Teilt man Information zwischen einer kühlen Hangparzelle und einer heißen Talsohle, zieht das Modell womöglich beide zu einem Mittelwert, der keiner passt. Die Struktur der Bündelung ist ebenso eine weinbauliche wie eine statistische Entscheidung.

**Auch das Urteil des Kellermeisters ist auf wenigen Jahrgängen trainiert.** Ein Kellermeister mit zwanzig Lesen hat ebenfalls zwanzig Zeilen, wenn auch mit sehr viel Kontext, den ein Modell nicht hat. Ziel ist, diesem Urteil bessere Belege zu liefern, nicht so zu tun, als hätte eine der beiden Seiten Big Data.

## Das Fazit

KI im Weingut scheitert, wenn sie einen Jahrgang wie einen Sud behandelt. Zehn Jahre sind zehn Zeilen, das Klima bewegt sich, und eine enge Anpassung an die Vergangenheit ist vor allem Gedächtnis. Modelle dort bauen, wo die Daten reichhaltig sind, innerhalb der Saison: Gärkurven, Sensoren, Beerenproben und Jahre ungelesenen Texts. Wo man über Jahrgänge hinweg vorhersagen muss, über Parzellen bündeln, bei der Wissenschaft anfangen und wöchentlich aktualisieren. Neue Werkzeuge helfen bei Kurven und bei Text. Keines davon macht aus zehn Zeilen tausend, und wer das Gegenteil behauptet, sollte gefragt werden, mit wie vielen Jahrgängen er trainiert hat.

Damit schließt **The Cellar Ledger**. Es begann mit [einem Chatbot, der drei Antworten gab]({{ '/de/2026/genai-winery-semantic-layer-potential-alcohol/' | relative_url }}), und endet hier, und der rote Faden durch alle sechs Beiträge ist derselbe: GenAI ist nur so vertrauenswürdig wie das Datenmodell darunter. Die vollständige Serie steht auf der [Seite zur Serie Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}), der breitere Weinkatalog im [Track Weinbereitung &amp; KI]({{ '/de/tracks/winemaking-ai/' | relative_url }}).

## Häufig gestellte Fragen

**Warum ist maschinelles Lernen im Weingut schwieriger als in der Brauerei?**
Weil die Lerneinheit oft der Jahrgang ist, und ein Weingut bekommt einen pro Jahr. Zehn Jahre Historie ergeben zehn Zeilen je Parzelle für Fragen wie Lesetermin, Ertrag oder Qualitätsbewertung, während eine Brauerei mit Hunderten Suden im Jahr Tausende hat. Modelle, die auf zehn Zeilen trainiert werden, lernen die Vergangenheit meist auswendig, statt aus ihr zu lernen.

**Können synthetische Daten oder ein Foundation Model einen kleinen Datensatz im Weingut retten?**
Allein nicht. Synthetische Daten, die aus den eigenen zehn Jahrgängen erzeugt werden, enthalten keine Information, die diese zehn Jahrgänge nicht schon hatten. Zeitreihen-Foundation-Models können eine brauchbare Zero-Shot-Prognose für eine Kurve liefern, etwa für eine Gärung, wissen aber nichts über den eigenen Weinberg. Beide sind in einem soliden Design nützlich, und keines von beiden erzeugt die fehlende Historie.

**Wo funktioniert KI im Weingut wirklich?**
Dort, wo die Daten innerhalb einer einzigen Saison reichhaltig sind: Gärkurven aus jedem Tank, Sensordaten aus dem Keller, Beerenproben während der Reife und Freitext wie Verkostungsnotizen und Kellerprotokolle. Modelle, die die Dynamik einer Gärung lernen, oder ein LLM, das die Protokolle liest, haben Hunderte oder Tausende Beispiele pro Jahr zur Verfügung.
