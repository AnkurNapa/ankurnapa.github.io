---
layout: post
lang: de
title: "KI für die Ertragsprognose im Weinberg"
image: /assets/og/ai-vineyard-yield-forecasting.png
description: "Wie KI den Weinbergertrag aus Traubenzählungen, Beerengewicht, NDVI-Fernerkundung und Wetter prognostiziert — um Tanks, Fässer und Verkauf zu planen — und warum das Jahrgangswetter das Modell weiterhin sprengt."
date: 2024-04-05
updated: 2024-04-05
permalink: /de/2024/ai-vineyard-yield-forecasting/
tags: [winemaking, viticulture, forecasting]
faq:
  - q: "Wie genau ist die KI-Ertragsprognose?"
    a: "Gut genug, um Tanks und Verkauf zu planen, nicht gut genug, um den Jahrgang darauf zu verwetten. Die Fehler weiten sich, je weiter du vor der Ernte prognostizierst, und ein Frost oder ein schlechter Fruchtansatz kann jedes Modell überrollen."
  - q: "Welche Eingaben treiben eine Ertragsprognose?"
    a: "Traubenzählungen je Rebstock, Beeren- und Traubengewicht, historische Parzellenerträge, NDVI-Laubwandkarten von Satellit oder Drohne und das Wetter während Blüte und Ansatz."
  - q: "Kann ich den Ertrag ohne Fernerkundung prognostizieren?"
    a: "Ja. Disziplinierte Traubenzählungen, Beerengewichte und ein paar Jahre Parzellenhistorie bringen dich den größten Teil des Weges. NDVI hilft hauptsächlich, klüger zu beproben und die Variabilität innerhalb einer Parzelle zu kartieren."
---

**Kurze Antwort: KI schärft Weinberg-Ertragsprognosen genug, um Tanks, Fässer und Verkauf zu planen — aber das Jahrgangswetter kann die Schätzung weiterhin sprengen, also prognostiziere in Spannen, nicht in Punkten.** Der Ertrag ist die Zahl, an der jede nachgelagerte Entscheidung hängt, und die meisten Keller raten sie immer noch.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Weinproduktionsfluss steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSFLUSS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">KI für die Ertragsprognose im Weinberg</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ernte</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maischen / Pressen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gären</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Reifen</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllen</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Weinproduktionsfluss steht, von Anfang bis Ende.</figcaption>
</figure>

## Warum eine Ertragszahl die ganze Saison treibt
Schätz den Ertrag falsch, und die Kosten häufen sich. Unterschätze ihn, und du kämpfst um Tankplatz oder verkaufst Trauben, die du hättest vinifizieren können; überschätze ihn, und du bindest Fässer, Verpackung und Verkaufsaufträge an Wein, der nie eintrifft. Die Ertragsprognose untermauert die Tank- und Fassplanung, die Lese-Logistik und die Verkaufszusagen, die du Monate vor der Ernte machst. Eine Prognose, die in einer sinnvollen Spanne landet, früh genug zum Handeln, ist echtes Geld wert.

Traditionell ist das Traubenzählungen mal Traubengewicht mal einem Verzögerungsfaktor, angepasst nach Bauchgefühl. KI wirft das nicht über Bord — sie formalisiert es, lernt das historische Verhalten jeder Parzelle und bezieht Signale ein, die ein Klemmbrett nicht kann.

## Zuerst messen: die Eingaben, die zählen
Ein nützliches Modell baut auf ein paar soliden Datenströmen. Traubenzählungen je Rebstock und repräsentative Beeren- und Traubengewichte geben dir die Kernschätzung. Mehrere Saisons mit Erträgen auf Parzellenebene lassen das Modell den typischen Ertrag jeder Parzelle und ihre Empfindlichkeit gegenüber Bedingungen lernen. NDVI von Satellit oder Drohne kartiert die Laubwand-Vigor, sodass du die Variabilität innerhalb einer Parzelle sehen und deine Beprobung dort ansetzen kannst, wo sie zählt, statt jede Reihe abzulaufen. Das Wetter während Blüte und Fruchtansatz — das Fenster, das entscheidet, wie viele Beeren tatsächlich ansetzen — ist oft der einzelne größte Schwankungsfaktor.

Die Disziplin zählt mehr als der Algorithmus. Wenn du diese Gewohnheit nie aufgebaut hast, beginne mit [sammle deine Daten vor der KI]({{ '/de/2026/collect-your-data-before-ai/' | relative_url }}): Ein paar Saisons konsistenter Zählungen und Gewichte schlagen ein ausgeklügeltes Modell, das mit der Beprobung eines Nachmittags gefüttert wird.

## Wo es bricht
Das Jahrgangswetter ist der große Demütiger von Ertragsmodellen. Ein Spätfrost, ein Kälteeinbruch während der Blüte, der den Fruchtansatz ruiniert, oder ein Hitzeereignis im Hochsommer kann den tatsächlichen Ertrag um Dutzende Prozent verändern — und genau das sind die Ereignisse, die Modelle am schlechtesten prognostizieren, weil sie selten und abrupt sind. Ein auf fünf „normalen" Jahrgängen trainiertes Modell hat wenig über den Ausreißer-Jahrgang zu sagen.

Grundwahrheitsdaten sind die andere Schwäche. Traubenzählungen sind arbeitsintensiv, sodass die meisten Keller spärlich beproben, und kleine Stichproben in einer variablen Parzelle erzeugen breite Fehlerbalken. Die Variabilität von Parzelle zu Parzelle und innerhalb einer Parzelle bedeutet, dass ein einzelner Durchschnitt viel verbirgt. Der ehrliche Schritt ist, als Spanne mit angegebener Konfidenz zu prognostizieren, die Spanne früh in der Saison zu weiten und sie zu verengen, wenn die Ernte näher rückt und die Früchte am Stock sind, wo du sie tatsächlich zählen kannst.

## Wie generative KI hineinpasst
Zwei Blickwinkel sind hier wirklich nützlich. Erstens die natürliche Sprachabfrage: Statt sich durch Tabellen zu graben, fragt ein Winzer „erwartete Tonnen für Parzelle 7 in diesem Jahrgang, und wie verhält sich das zum Vorjahr?", und eine generative Schicht über den Weinbergdaten antwortet in einfachem Deutsch mit den dargestellten Annahmen. Zweitens das automatisch entworfene Reporting: Am Ende jeder Beprobungsrunde schreibt das System einen Ertragsbericht — Parzelle für Parzelle, mit der Schätzung, der Spanne, den Hauptrisiken (Ansatz, Frostexposition, Krankheitsdruck) und was sich seit der letzten Runde geändert hat. Das spart dem Weinbergtechniker einen Nachmittag und gibt den Vertriebs- und Betriebsteams ein Dokument, gegen das sie tatsächlich planen können. Die generative Schicht verbessert die Prognose nicht; sie macht die Prognose für jeden nutzbar, der sie braucht.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">PROGNOSE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">KI für die Ertragsprognose im Weinberg</text><g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#b45309" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#b45309" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#7a1f3d" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">heute</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Historie</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">Prognose</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit.</figcaption>
</figure>

## Das Fazit
Die KI-Ertragsprognose verwandelt verstreute Zählungen, Laubwandkarten und Wetter in eine Planungszahl, mit der du eine Saison fahren kannst — vorausgesetzt, du behandelst sie als Spanne und respektierst, was Frost und schlechter Fruchtansatz ihr antun können. Investiere zuerst in disziplinierte Grundwahrheits-Beprobung, prognostiziere in Spannen und lass eine generative Schicht die Zahlen leicht abfragbar und berichtbar machen.

*Teil des Tracks [Weinbereitung & KI]({{ '/de/tracks/winemaking-ai/' | relative_url }}).* Verwandt: [Sammle deine Daten vor der KI]({{ '/de/2026/collect-your-data-before-ai/' | relative_url }}).

## Häufig gestellte Fragen

**Wie genau ist die KI-Ertragsprognose?**
Gut genug, um Tanks und Verkauf zu planen, nicht gut genug, um den Jahrgang darauf zu verwetten. Die Fehler weiten sich, je weiter du vor der Ernte prognostizierst, und ein Frost oder ein schlechter Fruchtansatz kann jedes Modell überrollen.

**Welche Eingaben treiben eine Ertragsprognose?**
Traubenzählungen je Rebstock, Beeren- und Traubengewicht, historische Parzellenerträge, NDVI-Laubwandkarten von Satellit oder Drohne und das Wetter während Blüte und Ansatz.

**Kann ich den Ertrag ohne Fernerkundung prognostizieren?**
Ja. Disziplinierte Traubenzählungen, Beerengewichte und ein paar Jahre Parzellenhistorie bringen dich den größten Teil des Weges. NDVI hilft hauptsächlich, klüger zu beproben und die Variabilität innerhalb einer Parzelle zu kartieren.
