---
layout: post
lang: de
title: "KI für Personal- und Schichtplanung in der Brauerei"
image: /assets/og/ai-brewery-workforce-shift-scheduling.png
description: "Wie Optimierung Brauerei-Personal an den Produktionsplan anpasst — unter Berücksichtigung von Qualifikationen, Verfügbarkeit und Arbeitsrecht — und warum Menschen keine Bauteile sind."
date: 2022-08-14
updated: 2022-08-14
permalink: /de/2022/ai-brewery-workforce-shift-scheduling/
tags: [brewing-science, planning, process-optimization]
faq:
  - q: "Wie unterscheidet sich die Personalplanung von der Produktionsplanung?"
    a: "Die Produktionsplanung entscheidet, was wann gebraut wird; die Personalplanung entscheidet, wer wann arbeitet, um diesen Plan umzusetzen. Sie nimmt den Produktions- und Abfüllplan als Eingabe und ordnet ihm Personal zu — unter Berücksichtigung von Qualifikationen, Verfügbarkeit und Arbeitsrecht. Beide sind verknüpft — der Dienstplan ist nur so gut wie der Produktionsplan, dem er dient."
  - q: "Welche Nebenbedingungen bewältigt ein Dienstplan-Optimierer?"
    a: "Qualifikationsabgleich, damit die richtigen befähigten Leute jede Aufgabe abdecken; Verfügbarkeit, einschließlich Urlaub und Teilzeitmuster; und Arbeitsregeln wie Höchstarbeitszeiten, Mindestruhezeiten und Pausenansprüche. Über diese harten Regeln hinaus kann er weichere Ziele wie Fairness und Präferenz abwägen — und genau darin liegt die eigentliche Schwierigkeit."
  - q: "Kann er prognostizieren, wie viele Leute ich brauchen werde?"
    a: "Ja. Weil der Produktionsplan eine Arbeitslast vorgibt — Sude, Abfüllläufe, CIP-Zyklen — kannst du daraus den Personalbedarf prognostizieren und gegen die erwartete Last planen statt gegen eine pauschale Kopfzahl. Allerdings übernimmt die Prognose jede Unsicherheit aus dem Produktionsplan, auf dem sie aufbaut."
---

**Kurze Antwort: Optimierung kann Personal an deinen Sud- und Abfüllplan anpassen — unter Berücksichtigung von Qualifikationen, Verfügbarkeit und Arbeitsrecht — und prognostizieren, wie viele Leute jede Schicht braucht. Aber Menschen sind keine Bauteile, und bei den weichen Nebenbedingungen wird es schwierig.** Die Dienstplanung ist eine der zeitaufwendigsten Aufgaben eines Brauereileiters. Sie ist zugleich ein gut geformtes Optimierungsproblem.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">KI für Personal- und Schichtplanung in der Brauerei</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Gärung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Abfüllung</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende.</figcaption>
</figure>

## Vom Produktionsplan zum Personalplan
Die Personalplanung beginnt nicht bei null; sie beginnt beim Produktionsplan. Sobald du weißt, was in den kommenden Wochen gebraut, abgefüllt und gereinigt wird, kennst du die Arbeitslast, die das mit sich bringt. Von dort verwandelt die Prognose den Plan in einen Personalbedarf — wie viele Leute, mit welchen Qualifikationen, zu welchen Zeiten — und ein Optimierer weist Mitarbeitende den Schichten zu, um ihn zu erfüllen.

Die harten Nebenbedingungen sind jedem Leiter vertraut, der einen Dienstplan von Hand füllt: Nur qualifiziertes Personal darf bestimmte Anlagen bedienen, Leute haben Verfügbarkeiten und Urlaub, und Arbeitsregeln begrenzen die Stunden, schreiben Ruhezeiten vor und schützen Pausen. Das manuell für einen ausgelasteten Standort zu erledigen, ist langsam und fehleranfällig. Ein Optimierer kann all diese Regeln gleichzeitig erfüllen und in Sekunden einen machbaren Dienstplan erstellen — was wirklich nützlich ist, denn die manuelle Variante frisst Stunden und patzt trotzdem.

Weil der Dienstplan vollständig vom Produktionsplan abhängt, lohnt es sich, diesen zuerst richtig zu machen; [KI für die Produktionsplanung in der Brauerei]({{ '/de/2021/ai-brewery-production-scheduling/' | relative_url }}) behandelt die vorgelagerte Entscheidung, die die hiesige Arbeitslast steuert.

## Zuerst messen: die echte Arbeitslast modellieren
Der Optimierer ist nur so gut wie sein Bild von der Arbeit. Das bedeutet, zu messen, wie lange Aufgaben tatsächlich dauern, welche Qualifikationen jede Rolle wirklich erfordert und wie die Arbeitslast über die Woche schwankt — statt eine flache, ordentliche Nachfrage anzunehmen. Die Disziplin ist dieselbe wie überall in diesem Track: Miss den Prozess, bevor du ihn modellierst.

Wenn deine Personalbedarfsprognose annimmt, dass jeder Brautag gleich aussieht, wird der Dienstplan an den Tagen falsch sein, die zählen — der schwere Abfülllauf, die doppelte CIP, der heikle Sortenwechsel. Erfasse die echte Schwankung der Arbeitslast, und der Optimierer kann danach besetzen. Überspringe diesen Schritt, und du planst nach dem Durchschnitt und bist genau dann unterbesetzt, wenn es darauf ankommt.

## Wo es versagt
Dies ist die Anwendung, bei der die ehrlichen Grenzen am meisten zählen, denn die „Ressourcen", die geplant werden, sind Menschen. Arbeitsregeln sind wirklich komplex und variieren je nach Vertrag und Rechtsraum; sie korrekt abzubilden ist echte Arbeit, und ein Optimierer, der sie falsch anwendet, schafft Compliance-Risiko, nicht Effizienz.

Noch schwieriger ist Fairness. Ein Dienstplan, der mathematisch optimal für Kosten oder Abdeckung ist, kann zutiefst unbeliebt sein, wenn er jede unangenehme Schicht denselben Leuten aufbürdet. Fairness, Präferenz und Moral sind weiche Nebenbedingungen, die sich einer sauberen Formulierung widersetzen, und auf die harten Zahlen zu überoptimieren, während man sie ignoriert, ist ein schneller Weg zu Groll und Fluktuation. Menschen sind keine Bauteile; ein Dienstplan, der sie als austauschbare Einheiten behandelt, wird technisch funktionieren und still scheitern. Der Optimierer sollte vorschlagen, und ein Leiter, der das Team kennt, sollte entscheiden.

## Ein praktischer generativer-KI-Blickwinkel
Generative KI passt als Erklärer und Entwerfer obendrauf auf den Optimierer. Sie kann einen regelkonformen Dienstplan-Entwurf erstellen und — entscheidend — die Kompromisse in einfacher Sprache erklären: „Dieser Dienstplan hält alle innerhalb der Stunden, gibt Sam aber drei Spätschichten; ein Tausch mit Priya gleicht das aus, braucht aber den Staplerschein, den sie hat und Sam nicht." Das erleichtert das weiche, menschliche Urteilen, weil der Leiter sehen kann, *warum* der Optimierer das gewählt hat, was er gewählt hat, und mit vollem Blick auf die Folgen anpassen kann. Wie immer muss er über die echte Verfügbarkeit und die echten Regeln schließen, und die letzte Entscheidung bleibt bei einem Menschen.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">REGELKREIS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">KI für Personal- und Schichtplanung in der Brauerei</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Regler</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Stellglied</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Prozess</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">Rückkopplung</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen.</figcaption>
</figure>

## Das Fazit
Die Personalplanung passt stark zur Optimierung: Sie nimmt deinen Produktionsplan, prognostiziert den daraus folgenden Personalbedarf und erstellt einen regelkonformen Dienstplan weit schneller als von Hand. Aber Arbeitsregeln sind verwickelt und Fairness widersetzt sich Formeln, daher ist dies die Anwendung, bei der du am meisten einen Menschen im Regelkreis brauchst. Miss die echte Arbeitslast, bilde die Regeln sorgfältig ab, lass den Optimierer vorschlagen und einen generativen-KI-Assistenten erklären — und lass einen Leiter, der das Team kennt, die letzte Entscheidung treffen.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).*

## Häufig gestellte Fragen

**Wie unterscheidet sich die Personalplanung von der Produktionsplanung?**
Die Produktionsplanung entscheidet, was wann gebraut wird; die Personalplanung entscheidet, wer wann arbeitet, um diesen Plan umzusetzen. Sie nimmt den Produktions- und Abfüllplan als Eingabe und ordnet ihm Personal zu — unter Berücksichtigung von Qualifikationen, Verfügbarkeit und Arbeitsrecht. Beide sind verknüpft — der Dienstplan ist nur so gut wie der Produktionsplan, dem er dient.

**Welche Nebenbedingungen bewältigt ein Dienstplan-Optimierer?**
Qualifikationsabgleich, damit die richtigen befähigten Leute jede Aufgabe abdecken; Verfügbarkeit, einschließlich Urlaub und Teilzeitmuster; und Arbeitsregeln wie Höchstarbeitszeiten, Mindestruhezeiten und Pausenansprüche. Über diese harten Regeln hinaus kann er weichere Ziele wie Fairness und Präferenz abwägen — und genau darin liegt die eigentliche Schwierigkeit.

**Kann er prognostizieren, wie viele Leute ich brauchen werde?**
Ja. Weil der Produktionsplan eine Arbeitslast vorgibt — Sude, Abfüllläufe, CIP-Zyklen — kannst du daraus den Personalbedarf prognostizieren und gegen die erwartete Last planen statt gegen eine pauschale Kopfzahl. Allerdings übernimmt die Prognose jede Unsicherheit aus dem Produktionsplan, auf dem sie aufbaut.
