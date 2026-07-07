---
layout: post
lang: de
title: "Weinfehler früh erkennen: Brett, flüchtige Säure, TCA"
image: /assets/og/detecting-wine-faults-brett-va-tca.png
description: "Wie KI Weinfehler früh markiert — Brettanomyces, flüchtige Säure und TCA-Korkton — aus Kellerbedingungen und Schnellanalyse, da sich die meisten Fehler leichter verhindern als rückgängig machen lassen."
date: 2024-08-05
updated: 2024-08-05
permalink: /de/2024/detecting-wine-faults-brett-va-tca/
tags: [winemaking, quality-control, microbiology]
faq:
  - q: "Kann KI Korkton (TCA) erkennen?"
    a: "Nur indirekt. TCA ist bei einstelligen Nanogramm pro Liter nachweisbar, weit unter dem, was Kellersensoren sehen, daher hilft KI vor allem, indem sie das Kontaminationsrisiko markiert und gezielte GC-MS-Tests auslöst, statt TCA selbst zu messen."
  - q: "Welche Weinfehler kann KI früh vorhersagen?"
    a: "Mikrobielle und chemische Fehler mit messbaren Vorläufern — Brettanomyces, flüchtige Säure, Reduktion und Oxidation — durch Beobachtung von pH-Wert, freier und molekularer SO2, Temperatur und Sauerstoffexposition gegen schnelle Mikro- und Chemieergebnisse."
  - q: "Bedeutet Früherkennung, dass ich den Fehler beheben kann?"
    a: "Manchmal, aber der eigentliche Gewinn ist Prävention. Die meisten Fehler sind weit leichter zu verhindern als rückgängig zu machen, daher liegt der Wert des Modells darin, die Bedingungen abzufangen, bevor sich der Fehler einstellt."
---

**Kurze Antwort: KI ist bei Weinfehlern am wertvollsten als Frühwarnsystem für die Bedingungen, die sie verursachen — denn Brett, flüchtige Säure und TCA lassen sich weit leichter verhindern als rückgängig machen.** Eine einzige verdorbene Partie kann die Marge eines Jahrgangs auslöschen, weshalb es sich auszahlt, die Drift früh abzufangen.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Weinproduktionsablauf steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Weinfehler früh erkennen: Brett, flüchtige Säure, TCA</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ernte</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mahlen / Pressen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Gärung</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Reifung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Abfüllung</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Wo dies im Weinproduktionsablauf steht, von Anfang bis Ende.</figcaption>
</figure>

## Die Fehler, die es sich lohnt, früh abzufangen
Eine Handvoll Fehler richtet den größten Schaden an. *Brettanomyces*-Hefe produziert 4-Ethylphenol und 4-Ethylguaiacol — die „Pferdestall"- und „medizinischen" Noten — und gedeiht bei warmen, SO2-armen, höheren pH-Bedingungen. Flüchtige Säure ist Essigsäure, produziert von *Acetobacter*, mit einer sensorischen Schwelle um 0,7–1,2 g/L. Korkton ist 2,4,6-Trichloranisol (TCA), nachweisbar bei nur wenigen Nanogramm pro Liter — einstellige ng/L. Reduktion wirft Schwefelwasserstoff und Mercaptane aus („faules Ei"); Oxidation zeigt sich als Acetaldehyd. Die meisten davon werden durch GC-MS und geschulte Sensorikpanels bestätigt, aber bis ein Panel sie riecht, kann die Partie bereits kompromittiert sein.

Der strategische Punkt ist die Asymmetrie: Prävention ist günstig und Umkehr ist teuer oder unmöglich. Genau das ist die Art von Problem, bei der sich ein prädiktives Modell seinen Platz verdient.

## Zuerst messen: Bedingungen plus Schnellanalyse
Das Modell beobachtet die Kellerbedingungen, die mikrobielle und chemische Fehler antreiben, und gleicht dann Schnelltests ab. Die Kerndaten: pH-Wert, freie und molekulare SO2, Temperatur und Sauerstoffexposition über jede Partie, im Zeitverlauf protokolliert. SO2 verdient besondere Aufmerksamkeit, denn die aktive, schützende Fraktion ist die molekulare SO2, die sowohl von der freien SO2 als auch vom pH-Wert abhängt — daher bewirkt dieselbe Zugabe bei niedrigem pH-Wert weit mehr als bei hohem. Ein Modell, das die molekulare SO2 verfolgt statt nur die freie SO2, versteht das echte Verderbnisrisiko viel besser.

Lege schnelle Mikrobiologie (Brett-Zellzahlen) und gezielte Chemie obendrauf, und das Modell lernt, welche Kombinationen von Bedingungen welchen Fehlern vorausgehen. Das Ziel ist nicht, GC-MS oder das Sensorikpanel zu ersetzen — es ist, dir zu sagen, welche Partien zuerst deren Aufmerksamkeit verdienen. Auch die Panel-Kalibrierung zählt hier; siehe [KI für Sensorikpanel- und Verkoster-Kalibrierung]({{ '/de/2024/ai-sensory-panel-taster-calibration/' | relative_url }}).

## Wo es versagt
TCA ist die ehrliche Grenze. Bei einstelligen Nanogramm pro Liter liegt es weit unter allem, was ein Kellersensor ablesen kann, und seine Quelle ist sporadisch — ein kontaminierter Korken, ein verdorbenes Fass, ein behandeltes Stück Kellerholz. KI kann TCA nicht aus den Bedingungen messen; bestenfalls markiert sie das Kontaminationsrisiko und leitet verdächtige Partien zur GC-MS. Die zweite Grenze sind Daten zu seltenen Ereignissen: schwere Brett-Ausbrüche und Partien mit hoher flüchtiger Säure sind in einem gut geführten Keller selten, daher hat ein Modell wenige Beispiele, aus denen es lernen kann, und kann den ungewöhnlichen Fall übersehen. Und die Laborbestätigung ist nie optional — das „erhöhte Brett-Risiko" eines Modells ist ein Anstoß, zu testen und bei SO2 und Temperatur zu handeln, keine Diagnose. Behandle die Ausgabe als Triage-Signal, nicht als Urteil.

## Wie generative KI hineinpasst
Der praktische generative Blickwinkel ist ein Copilot, der Mikrobiologie und Chemie zu einer Frühwarnmeldung mit Präventions-Checkliste verschmilzt. Statt drei getrennter Berichte bekommt der Winzer: „Fasskeller Partie 4 — der pH-Wert ist auf 3,78 gekrochen, die molekulare SO2 ist bei diesem pH-Wert unter das schützende Niveau gefallen, die Temperatur läuft warm, und die letzte Brett-Zahl ist gestiegen. Erhöhtes Brett-Risiko. Empfehle eine SO2-Zugabe zur Wiederherstellung der molekularen SO2, die Raumtemperatur zu senken und in einer Woche erneut zu testen." Es erklärt die Argumentationskette und übergibt Maßnahmen, nicht nur ein rotes Licht. Auch synthetische Daten helfen: Weil schwere Fehler selten sind, können simulierte Fehlerszenarien das Modell darauf trainieren, Warnmuster zu erkennen, die es sonst fast nie sehen würde — immer validiert gegen echte Laborergebnisse.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Die meisten Messwerte liegen innerhalb des normalen Bands; das Modell markiert den, der das nicht tut."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">ANOMALIEERKENNUNG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Weinfehler früh erkennen: Brett, flüchtige Säure, TCA</text><rect x="60" y="120" width="620" height="70" fill="#2e9e7c" opacity="0.12"/><line x1="60" y1="120" x2="680" y2="120" stroke="#2e9e7c" stroke-width="1" stroke-dasharray="4 3"/><line x1="60" y1="190" x2="680" y2="190" stroke="#2e9e7c" stroke-width="1" stroke-dasharray="4 3"/><circle cx="110" cy="150" r="5" fill="#4a6b64"/><circle cx="160" cy="140" r="5" fill="#4a6b64"/><circle cx="210" cy="165" r="5" fill="#4a6b64"/><circle cx="265" cy="148" r="5" fill="#4a6b64"/><circle cx="320" cy="158" r="5" fill="#4a6b64"/><circle cx="380" cy="143" r="5" fill="#4a6b64"/><circle cx="440" cy="168" r="5" fill="#4a6b64"/><circle cx="500" cy="150" r="5" fill="#4a6b64"/><circle cx="560" cy="160" r="5" fill="#4a6b64"/><circle cx="620" cy="146" r="5" fill="#4a6b64"/><circle cx="345" cy="92" r="7" fill="#06483f"/><text x="345" y="80" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">Anomalie</text><text x="668" y="138" text-anchor="end" font-family="sans-serif" font-size="11" fill="#2e9e7c">normales Band</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die meisten Messwerte liegen innerhalb des normalen Bands; das Modell markiert den, der das nicht tut.</figcaption>
</figure>

## Das Fazit
KI misst keinen Korkton, und sie wird dich nicht vor einem Fehler retten, den du erst bei der Abfüllung riechst. Ihr eigentlicher Wert ist das Lenken der Aufmerksamkeit: Beobachte molekulare SO2, pH-Wert, Temperatur und Sauerstoff über deine Partien, lass das Modell triagieren, welche das Labor und das Panel brauchen, und handle früh an den Bedingungen. Im Fehlermanagement ist Prävention das ganze Spiel — und genau das hilft dir ein gutes Modell zu spielen.

*Teil des Tracks [Winemaking & AI]({{ '/de/tracks/winemaking-ai/' | relative_url }}).* Verwandt: [KI für Sensorikpanel- und Verkoster-Kalibrierung]({{ '/de/2024/ai-sensory-panel-taster-calibration/' | relative_url }}).

## Häufig gestellte Fragen

**Kann KI Korkton (TCA) erkennen?**
Nur indirekt. TCA ist bei einstelligen Nanogramm pro Liter nachweisbar, weit unter dem, was Kellersensoren sehen, daher hilft KI vor allem, indem sie das Kontaminationsrisiko markiert und gezielte GC-MS-Tests auslöst, statt TCA selbst zu messen.

**Welche Weinfehler kann KI früh vorhersagen?**
Mikrobielle und chemische Fehler mit messbaren Vorläufern — Brettanomyces, flüchtige Säure, Reduktion und Oxidation — durch Beobachtung von pH-Wert, freier und molekularer SO2, Temperatur und Sauerstoffexposition gegen schnelle Mikro- und Chemieergebnisse.

**Bedeutet Früherkennung, dass ich den Fehler beheben kann?**
Manchmal, aber der eigentliche Gewinn ist Prävention. Die meisten Fehler sind weit leichter zu verhindern als rückgängig zu machen, daher liegt der Wert des Modells darin, die Bedingungen abzufangen, bevor sich der Fehler einstellt.
