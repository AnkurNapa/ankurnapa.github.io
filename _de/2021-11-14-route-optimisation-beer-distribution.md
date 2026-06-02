---
layout: post
lang: de
title: "Routenoptimierung für den Bierabsatz"
image: /assets/og/route-optimisation-beer-distribution.png
description: "Wie Tourenplanungs-Optimierung Kilometer, Kosten und Emissionen bei Bierauslieferungen unter Zeitfenstern und Kapazität senkt — und wo das Chaos der Realität ihre Grenzen setzt."
date: 2021-11-14
updated: 2021-11-14
permalink: /de/2021/route-optimisation-beer-distribution/
tags: [commercial-planning, logistics, process-optimization]
faq:
  - q: "Was ist Routenoptimierung für den Bierabsatz?"
    a: "Es ist das Lösen des Tourenplanungsproblems: Es wird entschieden, welcher Lieferwagen welche Bars und Händler in welcher Reihenfolge anfährt, unter Berücksichtigung von Zeitfenstern, Fahrzeugkapazität und Lieferrestriktionen. Ziel sind weniger Kilometer, niedrigere Kosten und geringere Emissionen."
  - q: "Können Routen neu optimiert werden, wenn sich Bestellungen ändern?"
    a: "Ja. Wenn eine neue Bestellung eingeht oder eine storniert wird, kann der Optimierer den Plan neu berechnen, anstatt die Disposition zu zwingen, ihn von Hand zu flicken. Diese Reaktionsfähigkeit macht einen großen Teil des Nutzens aus."
  - q: "Warum kann ein Optimierer Disponenten und Fahrer nicht ersetzen?"
    a: "Weil das Modell nicht alles sieht — den Live-Verkehr, eine umständliche Zufahrt, eine Lieferung, die ein Lokal vor dem Service erreichen muss. Das Wissen von Fahrern und Disponenten bewältigt das Chaos, das den Daten entgeht."
---

**Kurze Antwort: Routenoptimierung löst das Tourenplanungsproblem für Bierauslieferungen — weniger Kilometer, niedrigere Kosten und geringere Emissionen unter realen Restriktionen.** Sie ist einer der am besten quantifizierbaren Analytics-Erfolge im Vertrieb, sofern man die Grenzen der Karte respektiert.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebszyklus, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DER BETRIEBSZYKLUS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Routenoptimierung für den Bierabsatz</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">die Praxis verändern</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Der Betriebszyklus, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Das Tourenplanungsproblem, in Bier-Begriffen
Bier zu vertreiben ist ein klassisches Tourenplanungsproblem im Brauerei-Gewand. Man hat eine Flotte von Lieferwagen und eine Liste von Anfahrtspunkten — Bars, Restaurants, Getränkemärkte und Händler —, jeder mit eigenen Anforderungen. Manche Lokale nehmen Lieferungen nur innerhalb eines Zeitfensters an. Jedes Fahrzeug hat eine begrenzte Kapazität in Fässern und Kisten. Manche Anfahrtspunkte haben Zufahrts- oder Reihenfolgerestriktionen. Die Aufgabe besteht darin, Anfahrtspunkte den Fahrzeugen zuzuweisen und so zu sortieren, dass Gesamtstrecke und -zeit minimiert werden.

Löst man das gut, sind die Einsparungen direkt: weniger gefahrene Kilometer bedeuten niedrigere Kraftstoffkosten, geringere Emissionen und mehr abgeschlossene Anfahrtspunkte pro Schicht. Anders als bei unschärferer Analytik kommt diese hier mit einer sauberen Zielfunktion, was den Business Case leicht messbar und vertretbar macht.

## Erst messen, dann optimieren
Die Disziplin ist hier dieselbe wie bei jedem Analytics-Projekt: messen, bevor man optimiert. Erfassen Sie Ihre aktuellen Routen, Kilometer, Kosten pro Anfahrtspunkt und die Einhaltung der Zeitfenster über einen repräsentativen Zeitraum. Diese Ausgangsbasis ist es, die beweist, dass der Optimierer sein Geld wert war — und sie deckt oft die einfachen Gewinne auf, bevor irgendein Algorithmus läuft, etwa Lokale, die über die Routen hinweg schlecht gebündelt sind.

Der eigentliche Vorteil ist die Reaktionsfähigkeit. Statische Wochenrouten veralten in dem Moment, in dem sich eine Bestellung ändert. Ein moderner Optimierer optimiert neu, wenn Bestellungen hinzugefügt, storniert oder in der Menge geändert werden, sodass der Plan die heutige Realität widerspiegelt statt die vom letzten Montag. In dieser dynamischen Neuplanung steckt ein großer Teil der Einsparung, denn die Nachfrage in der Gastronomie ist selten ordentlich.

Fasslogistik und Auslieferungsrouten verstärken sich ebenfalls gegenseitig: Eine Route kann Fass-Abholungen ebenso wie -Anlieferungen einplanen, sodass Leergut schneller zurückkommt. Wenn Sie Ihre Flotte verfolgen, siehe [KI für Fassflotten-Tracking und -Optimierung]({{ '/de/2021/ai-keg-fleet-tracking/' | relative_url }}) für die Asset-Seite derselben Medaille.

## Eine generative KI-Schicht für die Disposition
Optimierer sind notorisch undurchsichtig — sie liefern einen Plan ohne Erklärung zurück, und Disponenten misstrauen dem, was sie nicht hinterfragen können. Ein generativer KI-Assistent schließt diese Lücke. Wenn sich die Route ändert, kann er in einfacher Sprache erklären, warum: „Dieses Lokal wurde nach vorne verlegt, um sein Mittagsfenster einzuhalten, also wanderten die beiden nahen Anfahrtspunkte zum Nachmittags-Wagen."

Diese Erläuterung bewirkt zweierlei. Sie baut Vertrauen auf, sodass die Disposition dem Plan folgt, statt ihn aus dem Bauch heraus zu übersteuern. Und sie beschleunigt das menschliche Eingreifen, wenn es wirklich nötig ist, weil der Disponent den Kompromiss versteht, den er bricht. Der Assistent erklärt die Entscheidung; er trifft sie nicht.

## Wo es bricht
Die ehrliche Grenze ist, dass die Karte nicht das Gelände ist. Ein Optimierer arbeitet mit den Restriktionen, die man ihm gibt, und die reale Welt liefert solche, die man nicht vorgesehen hat: eine Autobahnsperrung, eine blockierte Laderampe, ein Wirt, der nie vor elf da ist, eine Einbahnstraßenregelung, die die Daten nicht kennen. Live-Verkehr hilft, erfasst das Chaos aber nie vollständig.

Deshalb bleibt das Wissen von Fahrern und Disponenten unverzichtbar. Fahrer wissen, welchen Hintereingang man nutzen muss und welcher Wirt an der Theke unterschreibt. Der Optimierer erstellt einen ausgezeichneten Ausgangsplan; Menschen passen ihn an den Tag an. Behandeln Sie ihn als Entscheidungsunterstützung — eine starke Standardlösung, die Menschen für die Ausnahmen freispielt — statt als Autopiloten, dann liefert er.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 320" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Wo es in der Praxis passiert — Standorte, Routen und Gebiet."><rect x="0" y="0" width="720" height="320" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">IN DER PRAXIS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Routenoptimierung für den Bierabsatz</text><rect x="120" y="80" width="480" height="200" rx="10" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><line x1="180" y1="80" x2="180" y2="280" stroke="#e0d8cc"/><line x1="260" y1="80" x2="260" y2="280" stroke="#e0d8cc"/><line x1="340" y1="80" x2="340" y2="280" stroke="#e0d8cc"/><line x1="420" y1="80" x2="420" y2="280" stroke="#e0d8cc"/><line x1="500" y1="80" x2="500" y2="280" stroke="#e0d8cc"/><line x1="580" y1="80" x2="580" y2="280" stroke="#e0d8cc"/><line x1="120" y1="120" x2="600" y2="120" stroke="#e0d8cc"/><line x1="120" y1="180" x2="600" y2="180" stroke="#e0d8cc"/><line x1="120" y1="240" x2="600" y2="240" stroke="#e0d8cc"/><polyline points="220,150 360,200 470,130 540,240" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="5 4"/><circle cx="220" cy="144" r="9" fill="#7a1f3d"/><polygon points="214,148 226,148 220,158" fill="#7a1f3d"/><circle cx="360" cy="194" r="9" fill="#7a1f3d"/><polygon points="354,198 366,198 360,208" fill="#7a1f3d"/><circle cx="470" cy="124" r="9" fill="#7a1f3d"/><polygon points="464,128 476,128 470,138" fill="#7a1f3d"/><circle cx="540" cy="234" r="9" fill="#7a1f3d"/><polygon points="534,238 546,238 540,248" fill="#7a1f3d"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo es in der Praxis passiert — Standorte, Routen und Gebiet.</figcaption>
</figure>

## Das Fazit
Routenoptimierung gehört zu den klarsten Analytics-Erfolgen im Bierabsatz: ein gut definiertes Problem mit messbaren Einsparungen bei Kilometern, Kosten und Emissionen, dazu die Agilität, neu zu planen, wenn sich Bestellungen verschieben. Erst die Ausgangsbasis erfassen, dann eine generative KI-Schicht ergänzen, damit die Disposition dem Ergebnis vertraut, und das menschliche Urteil im Spiel halten für das Chaos, das kein Modell sehen kann.

*Teil des Tracks [Analytik für die kaufmännische Planung]({{ '/de/tracks/commercial-planning/' | relative_url }}).*

## Häufig gestellte Fragen

**Was ist Routenoptimierung für den Bierabsatz?**
Es ist das Lösen des Tourenplanungsproblems: Es wird entschieden, welcher Lieferwagen welche Bars und Händler in welcher Reihenfolge anfährt, unter Berücksichtigung von Zeitfenstern, Fahrzeugkapazität und Lieferrestriktionen. Ziel sind weniger Kilometer, niedrigere Kosten und geringere Emissionen.

**Können Routen neu optimiert werden, wenn sich Bestellungen ändern?**
Ja. Wenn eine neue Bestellung eingeht oder eine storniert wird, kann der Optimierer den Plan neu berechnen, anstatt die Disposition zu zwingen, ihn von Hand zu flicken. Diese Reaktionsfähigkeit macht einen großen Teil des Nutzens aus.

**Warum kann ein Optimierer Disponenten und Fahrer nicht ersetzen?**
Weil das Modell nicht alles sieht — den Live-Verkehr, eine umständliche Zufahrt, eine Lieferung, die ein Lokal vor dem Service erreichen muss. Das Wissen von Fahrern und Disponenten bewältigt das Chaos, das den Daten entgeht.
