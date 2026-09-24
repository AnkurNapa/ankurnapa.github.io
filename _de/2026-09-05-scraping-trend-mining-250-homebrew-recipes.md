---
layout: post
lang: de
title: "250 öffentliche Hobbybrau-Rezepte scrapen und nach Trends durchsuchen: Regex, wo es geht, LLM, wo es sein muss"
image: /assets/og/scraping-trend-mining-250-homebrew-recipes.png
description: "Teil 4 von The Brewer's Agent. Ein kleines Data-Engineering-Projekt mit 250 kürzlich geteilten Hobbybrau-Rezepten: höfliches Scraping, die Fallen beim Parsen, Normalisierung auf Basiseinheiten, wann Regex ein LLM schlägt und wann nicht, eine Konsistenzprüfung, an der die Daten 12 Mal scheiterten, und was die Rezepte tatsächlich über das Brauen in 2025 und 2026 sagen."
date: 2026-09-05 09:00:00 -0700
updated: 2026-09-05
permalink: /de/2026/scraping-trend-mining-250-homebrew-recipes/
tags: [brewing-science, brewers-agent, data-engineering, generative-ai, recipe-design]
faq:
  - q: "Ist es in Ordnung, öffentliche Hobbybrau-Rezeptseiten zu scrapen?"
    a: "Nur im Rahmen der Nutzungsbedingungen und der robots.txt der Seite, mit einer zurückhaltenden Anfragerate und zur Analyse statt zur Wiederveröffentlichung. Scrape Seiten, die ohne Anmeldung öffentlich sind, gib dich zu erkennen, cache alles Abgerufene, damit du keine Seite zweimal aufrufst, und veröffentliche aggregierte Ergebnisse statt die Rezepte anderer zu kopieren."
  - q: "Sollte ich ein LLM oder reguläre Ausdrücke zum Parsen von Rezeptdaten verwenden?"
    a: "Verwende reguläre Ausdrücke und einfaches Parsen für strukturierte Felder wie Stammwürze, Bittere und Mengen, weil sie schnell, kostenlos und exakt sind. Verwende ein LLM für die unordentlichen Teile, etwa um Hopfen- und Hefenamen aufzulösen, die auf mehrere Arten geschrieben werden, und prüfe seine Ausgabe gegen eine Liste bekannter Sorten."
  - q: "Was zeigten 250 aktuelle Hobbybrau-Rezepte über Trends?"
    a: "American IPA war mit 26 Rezepten der am häufigsten geteilte Stil, Citra und Cascade lagen als meistgenutzte Hopfen mit 84 und 83 Verwendungen fast gleichauf, und zwei saubere amerikanische Ale-Hefen trugen fast ein Viertel aller Rezepte. Hazy und New England IPA war mit 13 Rezepten der deutlichste moderne Trend. Es ist der aktuelle Feed einer einzigen Seite, also behandle es als Signal, nicht als Vollerhebung."
---

**Kurze Antwort: 250 kürzlich geteilte Hobbybrau-Rezepte sind ein gutes kleines Data-Engineering-Projekt, und der größte Teil der Arbeit ist nicht das Scraping. Es ist das Parsen: Kennzahlen, die zu zweit in einer Zeile stehen, Mengen wie "7 lbs 14.00 oz", eigene Zutaten mit einem Sternchen markiert, und ein Hopfen in drei Schreibweisen. Parse die strukturierten Felder mit einfachem Code, normalisiere alles auf Basiseinheiten, nutze ein LLM nur zum Auflösen unordentlicher Namen, und prüfe die Daten gegen sich selbst (bei 12 Rezepten passte der ABV nicht zu den eigenen Dichtewerten). Das Ergebnis: American IPA führt, Citra und Cascade liegen Kopf an Kopf, und Hazy IPA ist der Trend, der sich tatsächlich bewegt.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Eine Pipeline für 250 Hobbybrau-Rezepte. Höfliches Scraping öffentlicher Seiten in einen Roh-Cache, dann strukturierte Felder mit Regex parsen, dann auf Basiseinheiten wie Kilogramm, Liter und Gramm pro Liter normalisieren, dann unordentliche Hopfen- und Hefenamen mit einem LLM auflösen, geprüft gegen eine bekannte Liste, dann Konsistenzprüfungen, bei denen 12 Rezepte einen ABV hatten, der um mehr als 0,3 Punkte von ihren eigenen Dichtewerten abwich, dann Trends aggregieren. Wichtigste Ergebnisse: American IPA 26 Rezepte, Citra 84 Verwendungen, Cascade 83 Verwendungen, Hazy IPA 13 Rezepte.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">250 REZEPTE, SECHS SCHRITTE, EIN TEIL, DER EIN LLM BRAUCHT</text>
<g font-family="sans-serif">
<rect x="20" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="94" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">höflich scrapen</text>
<text x="94" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">öffentliche Seiten, gecacht</text>
<rect x="183" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="257" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">parsen</text>
<text x="257" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">Regex auf Labels</text>
<rect x="346" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="420" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">normalisieren</text>
<text x="420" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">kg, L, g/L, &#176;P</text>
<rect x="509" y="60" width="148" height="80" rx="9" fill="#06483f"/>
<text x="583" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">Namen auflösen</text>
<text x="583" y="112" text-anchor="middle" font-size="10" fill="#cfe6df">LLM + bekannte Liste</text>
<rect x="672" y="60" width="148" height="80" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="746" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">prüfen</text>
<text x="746" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">12 ABV-Abweichungen</text>
<rect x="835" y="60" width="148" height="80" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="909" y="92" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">aggregieren</text>
<text x="909" y="112" text-anchor="middle" font-size="10" fill="#4a6b64">Trends, keine Kopien</text>
<g font-size="11" fill="#06483f">
<rect x="20" y="170" width="230" height="70" rx="9" fill="#f0f6f5"/>
<text x="135" y="198" text-anchor="middle" font-weight="700">American IPA</text><text x="135" y="220" text-anchor="middle">26 Rezepte, Spitzenstil</text>
<rect x="266" y="170" width="230" height="70" rx="9" fill="#f0f6f5"/>
<text x="381" y="198" text-anchor="middle" font-weight="700">Citra 84 &#183; Cascade 83</text><text x="381" y="220" text-anchor="middle">Hopfenverwendungen, Kopf an Kopf</text>
<rect x="512" y="170" width="230" height="70" rx="9" fill="#f0f6f5"/>
<text x="627" y="198" text-anchor="middle" font-weight="700">2 Ale-Hefen</text><text x="627" y="220" text-anchor="middle">58 von 250 Rezepten</text>
<rect x="758" y="170" width="225" height="70" rx="9" fill="#f0f6f5"/>
<text x="870" y="198" text-anchor="middle" font-weight="700">Hazy / NEIPA</text><text x="870" y="220" text-anchor="middle">13 Rezepte, der Aufsteiger</text>
</g>
<rect x="20" y="268" width="963" height="46" rx="10" fill="#06483f"/>
<text x="500" y="296" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">DAS SCRAPING DAUERT EINE STUNDE &#183; DAS PARSEN DAS GANZE WOCHENENDE</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Zahlen aus den 250 zuletzt geteilten Rezepten einer öffentlichen Seite, abgerufen Mitte 2026. Ein Signal aus einer Community, keine Vollerhebung des Brauens.</figcaption>
</figure>

Jeder Brauer, der programmiert, will irgendwann wissen, was alle anderen brauen. Rezeptportale veröffentlichen Tausende Rezepte offen, und es ist verlockend, alles abzuziehen und ein Sprachmodell nach den Trends zu fragen. Ich habe eine kleinere, sorgfältigere Version gemacht: die 250 zuletzt geteilten Rezepte auf einer öffentlichen Seite. Daraus wurde eine saubere, vollständige Data-Engineering-Übung, mit einer Stelle, an der ein LLM wirklich hilft, und mehreren, an denen es die Sache verschlechtert hätte.

## Höflich scrapen oder gar nicht

Vor jedem Code drei Prüfungen:

1. **Lies robots.txt und die Nutzungsbedingungen.** Sagt die Seite nein, endet das Projekt dort.
2. **Nur öffentliche Seiten.** Keine Anmeldung, um Inhalte anderer abzugreifen, kein Umgehen von Bezahlschranken.
3. **Analyse, keine Wiederveröffentlichung.** Die Leute haben diese Rezepte mit ihrer Community geteilt. Aggregierte Zahlen zu veröffentlichen ist fair. Ihre Rezepte vollständig neu zu posten ist es nicht.

Dann halte den Fußabdruck klein: ein echter User-Agent mit Kontaktadresse, eine Anfrage alle paar Sekunden und ein lokaler Cache, damit jede Seite genau einmal abgerufen wird. Die nach Aktualität sortierten Listenseiten enthielten jeweils etwa 20 Rezepte, also waren 250 Rezepte ein Dutzend Listenseiten und 250 Detailseiten. Das ist eine Stunde in gemächlichem Tempo. Kein Server sollte dich bemerken.

## Die Fallen beim Parsen

Hier ging die Zeit hin. Rezeptseiten sind für Menschen geschrieben, und Menschen brauchen keine konsistente Formatierung.

**Kennzahlen zu zweit in einer Zeile.** Die Seite druckte "Batch Size: 5.00 gal" und "Style: American IPA" ohne Trennzeichen in dieselbe Zeile. Nach Zeilen zu trennen ergibt Unsinn. Die Lösung ist, sich an den Labels selbst zu verankern und bis zum nächsten bekannten Label zu lesen.

**Mengen mit gemischten Einheiten.** Malzmengen kamen als "7 lbs 14.00 oz", "12.00 oz" oder "3 lbs". In den 250 Rezepten nutzten 529 Malzzeilen Pfund und Unzen zusammen, 276 nur Unzen und 189 nur Pfund. Ein Parser, der die erste Zahl und die erste Einheit liest, bekommt 7 Pfund und verliert still 14 Unzen.

**Eigene Zutaten.** Brauer, die eine eigene Zutat anlegen, bekommen sie mit einem Sternchen davor. Lässt du das Sternchen stehen, zählen "*Safale US-05" und "Safale US-05" als zwei Hefen.

**Verirrte Leerzeichen.** Doppelte Leerzeichen in Namen teilen einen Hopfen in jeder Zählung in zwei. Fasse Leerraum zusammen, bevor du irgendetwas aggregierst.

**Der Typ steht im Titel.** Ob ein Rezept All-Grain oder Extrakt ist, war das letzte Wort der Titelzeile, kein eigenes Feld. Fürs Protokoll: 243 der 250 waren All-Grain.

## Einmal auf Basiseinheiten normalisieren

Jede Menge wurde beim Einlesen umgerechnet: Malz in Kilogramm, Hopfen in Gramm, Volumen in Liter und Hopfengaben in Gramm pro Liter, damit sich ein 5-Gallonen-Sud und ein 20-Liter-Sud vergleichen lassen. Die Dichtewerte blieben so, wie die Seite sie angab (spezifisches Gewicht), mit einer Plato-Spalte, abgeleitet über eine getestete Umrechnung.

Das ist dieselbe Regel wie bei [den Rechenwerkzeugen in Teil 2]({{ '/de/2026/brewing-agent-calculation-tools-not-sums/' | relative_url }}): Basiseinheiten innen, Anzeigeeinheiten am Rand. An einer Stelle umzurechnen, in Code mit Tests, heißt, dass ein Trenddiagramm nie still Unzen und Gramm vermischt.

## Regex, wo es geht, LLM, wo es sein muss

Heute ist es leicht, jede Seite einem Sprachmodell hinzuwerfen und JSON zu verlangen. Für diese Aufgabe wäre das bei den meisten Feldern langsamer, teurer und ungenauer gewesen.

**Strukturierte Felder: einfacher Code.** Stammwürze, Restextrakt, ABV, IBU, Farbe, Mengen und Kochzeiten stehen neben festen Labels. Reguläre Ausdrücke ziehen sie exakt heraus, kostenlos, in Millisekunden. Ein LLM würde gelegentlich eine Zahl runden, eine Nachkommastelle verlieren oder "hilfreich" eine Einheit umrechnen.

**Namen: Hier verdient sich das LLM seinen Platz.** Hopfen- und Hefenamen sind ein Durcheinander. In dieser Stichprobe sind "Amarillo Gold" (49 Verwendungen) und "Amarillo" (27) derselbe Hopfen unter zwei Namen, und "Fuggle" und "Fuggles" teilen sich 16 und 16. Hefen erscheinen unter einem Laborcode, einem Markennamen oder einem Spitznamen. Das aufzulösen ist unscharfes Matching mit Fachwissen, und das können Sprachmodelle gut.

Der sichere Weg: Gib dem Modell den Rohnamen und eine Liste bekannter Sorten, lass es eine auswählen oder "unbekannt" sagen, und akzeptiere nie einen Namen, der nicht auf der Liste steht. Das Modell ordnet zu. Die Liste entscheidet.

Für die veröffentlichten Zahlen habe ich Amarillo und Amarillo Gold tatsächlich getrennt gelassen und das auch gesagt, denn sie zusammenzuführen ist eine Ermessensfrage, und der Leser sollte sie sehen. Eine solche Entscheidung macht man besser sichtbar, statt sie in einer Pipeline zu vergraben.

## Die Daten gegen sich selbst prüfen

Gescrapte Daten bringen ihre eigenen Fehler mit, und Braudaten haben eine eingebaute Prüfung: Der ABV sollte sich aus Stammwürze und Restextrakt ergeben. Mit der gängigen Näherung aus dem Hobbybrauen (Dichteabfall mal 131.25) lieferten 12 der 250 Rezepte einen ABV, der um mehr als 0,3 Punkte von dem abwich, was ihre eigenen Dichtewerte ergeben.

Das heißt nicht, dass 12 Brauer Fehler gemacht haben. Rezeptsoftware bietet mehr als eine ABV-Formel an, manche Brauer ändern die Zahl von Hand, und manche Rezepte sind Vorlagen mit veralteten Zahlen. Es heißt, dass du der ABV-Spalte nicht blind trauen solltest, und dass ein Trenddiagramm zum ABV aus den Dichtewerten mit einer angegebenen Formel gebaut werden sollte.

## Was die 250 Rezepte sagten

Mit dem Vorbehalt, dass dies der aktuelle Feed einer einzigen Seite ist:

- **Stile:** American IPA führte mit 26 Rezepten, dann American Pale Ale mit 18. Saison, Blonde Ale, Witbier und Session IPA lagen mit je 10 gleichauf. Die Community ist IPA-geprägt, aber weit davon entfernt, nur IPA zu brauen.
- **Hopfen:** Citra (84 Verwendungen) und Cascade (83) liegen fast gleichauf. Centennial, Amarillo, Magnum, Saaz und Simcoe folgen. Die klassischen amerikanischen C-Hopfen dominieren weiterhin gegenüber neueren Sorten.
- **Hefe:** Zwei saubere amerikanische Ale-Stämme trugen zusammen 58 Rezepte, fast ein Viertel der Stichprobe.
- **Was sich bewegt:** Hazy und New England IPA, 13 Rezepte nach Name oder Stil, deutlich vor jedem anderen neueren Stil. Neuere Hazy-Stämme tauchen auf, sind aber noch selten.
- **Typisches Bier:** Median der Stammwürze 1.055, Median des ABV 5,6%, Median der Bittere etwa 33 IBU.

Nichts davon wird jemanden überraschen, der bei Hobbybrau-Wettbewerben richtet. Das ist in Ordnung. Der Wert liegt darin, es als Daten zu haben, die du nächstes Quartal erneut laufen lassen und vergleichen kannst, nicht in einer Offenbarung.

## Wo das an Grenzen stößt

**Eine Seite ist eine Community.** Leute, die Rezepte öffentlich teilen, sind nicht alle Brauer. Kommerzielle Brauereien fehlen, und manche Stile sind überrepräsentiert, weil ihre Brauer gern teilen.

**Aktuell ist nicht repräsentativ.** Ein nach Aktualität sortierter Feed über ein paar Monate erfasst saisonales Brauen. Lass es im Winter laufen, und die Stouts steigen.

**Namen bleiben Ermessensfragen.** Schreibweisen zusammenführen, Hazy und NEIPA gruppieren, entscheiden, ob "Session IPA" ein eigener Stil ist: Jede dieser Entscheidungen verändert eine Zählung. Veröffentliche die Regeln mit den Ergebnissen.

**Bedingungen ändern sich.** Eine Seite, die heute höfliches Crawlen erlaubt, tut das morgen vielleicht nicht mehr. Prüfe vor jedem neuen Lauf erneut.

## Das Fazit

Das Scraping war die leichte Stunde. Das Wochenende ging für Kennzahlen zu zweit in einer Zeile drauf, für Mengen in Pfund und Unzen, für Sternchen und für einen Hopfen mit drei Namen, und das ist normal für jede echte Data-Engineering-Aufgabe. Parse strukturierte Felder mit einfachem Code, normalisiere einmal in getesteten Funktionen, nutze ein LLM für die unscharfen Namen mit einer Liste, aus der es wählen muss, und prüfe die Daten gegen ihre eigene Physik. Dann lohnt sich auch der Blick aufs Trenddiagramm.

Früher auf diesem Blog: [Kann KI ein Bierrezept entwerfen?]({{ '/de/2026/can-ai-design-a-beer-recipe/' | relative_url }}) hat sich die Generierung angesehen. In diesem Beitrag ging es um die Daten, die ein Generator bräuchte. Als Nächstes in der Serie: [Evals für einen Brau-Assistenten]({{ '/de/2026/evals-for-a-brewing-assistant/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite von The Brewer's Agent]({{ '/series/brewers-agent/' | relative_url }}).

## Häufig gestellte Fragen

**Ist es in Ordnung, öffentliche Hobbybrau-Rezeptseiten zu scrapen?**
Nur im Rahmen der Nutzungsbedingungen und der robots.txt der Seite, mit einer zurückhaltenden Anfragerate und zur Analyse statt zur Wiederveröffentlichung. Scrape Seiten, die ohne Anmeldung öffentlich sind, gib dich zu erkennen, cache alles Abgerufene, damit du keine Seite zweimal aufrufst, und veröffentliche aggregierte Ergebnisse statt die Rezepte anderer zu kopieren.

**Sollte ich ein LLM oder reguläre Ausdrücke zum Parsen von Rezeptdaten verwenden?**
Verwende reguläre Ausdrücke und einfaches Parsen für strukturierte Felder wie Stammwürze, Bittere und Mengen, weil sie schnell, kostenlos und exakt sind. Verwende ein LLM für die unordentlichen Teile, etwa um Hopfen- und Hefenamen aufzulösen, die auf mehrere Arten geschrieben werden, und prüfe seine Ausgabe gegen eine Liste bekannter Sorten.

**Was zeigten 250 aktuelle Hobbybrau-Rezepte über Trends?**
American IPA war mit 26 Rezepten der am häufigsten geteilte Stil, Citra und Cascade lagen als meistgenutzte Hopfen mit 84 und 83 Verwendungen fast gleichauf, und zwei saubere amerikanische Ale-Hefen trugen fast ein Viertel aller Rezepte. Hazy und New England IPA war mit 13 Rezepten der deutlichste moderne Trend. Es ist der aktuelle Feed einer einzigen Seite, also behandle es als Signal, nicht als Vollerhebung.
