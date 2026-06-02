---
layout: post
lang: de
title: "Mein erstes echtes KI-Projekt: Bierbedarf prognostizieren — was funktionierte, was floppte"
image: /assets/og/my-first-ai-project-beer-demand-forecasting.png
description: "Eine ehrliche Nachbetrachtung des Aufbaus der Bierbedarfsprognose bei iWort — wo Machine Learning die Tabellenkalkulation schlug, wo nicht, und die Datenlektionen, die mich am meisten kosteten."
date: 2026-05-25 16:00:00 -0700
updated: 2026-05-25
permalink: /de/2026/my-first-ai-project-beer-demand-forecasting/
tags: [brewer-to-ai, demand-forecasting, machine-learning, iwort]
faq:
  - q: "Kann KI den Bierbedarf prognostizieren?"
    a: "Ja, für etablierte Biere mit stabiler, saisonaler Nachfrage und genug sauberer Verkaufshistorie. Sie tut sich schwer mit Neuerscheinungen und einmaligen Ereignissen, wo sie oft nicht besser ist als eine sorgfältige menschliche Schätzung."
  - q: "War Machine Learning besser als eine Tabellenkalkulation für die Bedarfsprognose?"
    a: "Nur manchmal. Für Fälle mit hohem Volumen, vielen SKUs und Saisonalität brachte ML echten Mehrwert. Für kleine Sortimente und neue Produkte lag eine einfache saisonale Tabellenkalkulation auf wenige Prozent genau dran — zu null Kosten und voller Transparenz."
  - q: "Was ist der schwierigste Teil eines Prognoseprojekts in einer Brauerei?"
    a: "Die Daten, nicht das Modell. Inkonsistente Verkaufsaufzeichnungen, Produkte, die es letztes Jahr nicht gab, und eine von Ereignissen getriebene Nachfrage, die das Modell nie gesehen hat, sind das, was Prognosen in der Praxis sprengt."
---

**Kurze Antwort: Mein erstes ernsthaftes KI-Projekt war die Bierbedarfsprognose — vorherzusagen, welche Biere herzustellen sind und wie viel, damit Brauereien zur richtigen Zeit am richtigen Ort verkaufen. Es funktionierte wirklich gut für etablierte, saisonale Produkte mit sauberer Historie. Es floppte bei Neuerscheinungen und einmaligen Ereignissen, wo eine einfache Tabellenkalkulation mithielt. Der schwierige Teil war nie das Modell; es waren die Daten.** Hier ist die ehrliche Nachbetrachtung.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Von Rohdaten zu einer Entscheidung, auf die das Team reagieren kann — die Pipeline hinter diesem Beitrag."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DATEN → ENTSCHEIDUNG</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Mein erstes echtes KI-Projekt: Bierbedarf prognostizieren — was funktionierte, was floppte</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Daten</text><text x="90.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Sensoren, Protokolle</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Merkmale</text><text x="289.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">bereinigen &amp; formen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Modell</text><text x="488.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">trainieren / bewerten</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Vorhersage</text><text x="687.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">was als Nächstes passiert</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Aktion</text><text x="886.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Team handelt</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Von Rohdaten zu einer Entscheidung, auf die das Team reagieren kann — die Pipeline hinter diesem Beitrag.</figcaption>
</figure>

## Das Problem, das es wert ist, gelöst zu werden

Die Bedarfsprognose ist eines der wertvollsten Dinge, die eine Brauerei richtig hinbekommen kann: Überproduziere, und du schüttest Geld in den Abfluss; unterproduziere, und du verpasst Verkäufe. Es ist das Problem, um das herum ich bei **iWort** gebaut habe — KI-/Datenprognosen für Craft- und kommerzielle Brauereien erschwinglich zu machen, damit sie Angebot und reale Nachfrage in Einklang bringen können.

Es ist auch ein Problem, für das du Daten hast, die du ohnehin schon sammelst: die Verkaufshistorie. Das machte es zum richtigen ersten Projekt.

## Was funktionierte

Für Biere mit einer Vorgeschichte — ganzjährige Produkte, klare Saisonalität, genug saubere Verkaufshistorie — verdiente sich Machine Learning seinen Platz. Es griff Muster über Wetter, Wochentag, Feiertage und Aktionen hinweg auf, die ein Mensch, der mit Tabellenkalkulationen jongliert, schlicht nicht im Kopf behalten kann. Für Betriebe mit vielen SKUs und höherem Volumen ist das echtes gespartes Geld.

## Was floppte

Der ehrliche Teil. Das Modell war genau dort am schwächsten, wo ich am meisten Hilfe wollte:

- **Neuerscheinungen** hatten keine Historie, also fiel das Modell auf generische Schätzungen zurück — manchmal schlechter als das Bauchgefühl eines Brauers.
- **Einmalige Ereignisse** — ein Festival, ein viraler Moment, eine Hitzewelle — waren für es unsichtbar. Es kann nur aus dem lernen, was es gesehen hat.
- **Dünne Daten führten zu Overfitting.** Gib einem flexiblen Modell zu wenig Historie, und es „lernt“ Rauschen und prognostiziert es dir dann mit voller Überzeugung zurück.

Ich gehe in [KI-Nachfrageprognose für Brauereien]({{ '/de/2026/ai-demand-forecasting-for-breweries/' | relative_url }}) darauf ein, wann sich Prognosen lohnen und wann nicht. Die Kurzfassung: Manchmal lag eine saisonale Tabellenkalkulation auf wenige Prozent am Modell dran — kostenlos, transparent und gut genug.

## Die Lektion, die hängen blieb

Das Modell war vielleicht 20 % der Arbeit. Die anderen 80 % waren das Bändigen unordentlicher Verkaufsdaten und das ehrliche Eingeständnis, was die Prognose sehen konnte und was nicht. Mein größter früher Fehler war, einer selbstbewussten Zahl aus dünnen Daten zu vertrauen. Dieser Fehler — und ein paar schlimmere — ist das Thema des nächsten Beitrags.

*From Brewer to AI — Teil 5 von 8. [Vollständige Serie]({{ '/de/series/brewer-to-ai/' | relative_url }}) · [Weiter: Wo KI mir auf die Füße fiel →]({{ '/de/2026/where-ai-burned-me/' | relative_url }})*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Historie (durchgezogen) und die vorausschauende Prognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">PROGNOSE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Mein erstes echtes KI-Projekt: Bierbedarf prognostizieren — was funktionierte, was floppte</text><g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#b45309" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#b45309" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#7a1f3d" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">heute</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Historie</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">Prognose</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Historie (durchgezogen) und die vorausschauende Prognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit.</figcaption>
</figure>

## Häufig gestellte Fragen

**Kann KI den Bierbedarf prognostizieren?**
Ja, für etablierte Biere mit stabiler, saisonaler Nachfrage und genug sauberer Verkaufshistorie. Sie tut sich schwer mit Neuerscheinungen und einmaligen Ereignissen, wo sie oft nicht besser ist als eine sorgfältige menschliche Schätzung.

**War Machine Learning besser als eine Tabellenkalkulation für die Bedarfsprognose?**
Nur manchmal. Für Fälle mit hohem Volumen, vielen SKUs und Saisonalität brachte ML echten Mehrwert. Für kleine Sortimente und neue Produkte lag eine einfache saisonale Tabellenkalkulation auf wenige Prozent genau dran — zu null Kosten und voller Transparenz.

**Was ist der schwierigste Teil eines Prognoseprojekts in einer Brauerei?**
Die Daten, nicht das Modell. Inkonsistente Verkaufsaufzeichnungen, Produkte, die es letztes Jahr nicht gab, und eine von Ereignissen getriebene Nachfrage, die das Modell nie gesehen hat, sind das, was Prognosen in der Praxis sprengt.
