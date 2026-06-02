---
layout: post
lang: de
title: "Stillstandszeiten der Abfülllinie vorhersagen und die OEE heben"
image: /assets/og/packaging-line-oee-downtime-prediction.png
description: "Wie maschinelles Lernen Mikrostopps am Füller- und Verschließer-Engpass vorhersagt, um die Stillstandszeiten zu verhindern, die die OEE-Verluste der Abfülllinie dominieren."
date: 2024-02-25
updated: 2024-02-25
permalink: /de/2024/packaging-line-oee-downtime-prediction/
tags: [brewing-science, packaging, predictive-maintenance]
faq:
  - q: "Was ist OEE und wie wird sie berechnet?"
    a: "Overall Equipment Effectiveness ist Verfügbarkeit mal Leistung mal Qualität. Sie erfasst Stopps, Geschwindigkeitsverluste und Ausschussraten in einer Zahl und zeigt so die wahre Output-Lücke, nicht nur die Laufzeit."
  - q: "Warum sich auf Füller und Verschließer konzentrieren?"
    a: "Der Füller und der Verschließer, und manchmal der Etikettierer, sind meist der Linienengpass. Verluste dort begrenzen die ganze Linie, also ist eine am Engpass gesparte Minute eine Minute echten zusätzlichen Outputs."
  - q: "Was dominiert die Verluste der Abfülllinie?"
    a: "Mikrostopps und Umrüstungen, nicht große Ausfälle. Dutzende kurzer Stillstände pro Schicht erodieren Leistung und Verfügbarkeit leise stärker als der gelegentliche große Ausfall."
---

**Kurze Antwort: Die Verluste, die die Abfüll-OEE ruinieren, sind Mikrostopps und Umrüstungen am Füller und Verschließer, und maschinelles Lernen kann sie früh genug vorhersagen, um ihnen zuvorzukommen.** Behebe den Engpass, und du hebst die ganze Linie.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Whiskey-Produktionsablauf sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Stillstandszeiten der Abfülllinie vorhersagen und die OEE heben</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maischen</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gären</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Destillieren</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Reifen</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllen</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Whiskey-Produktionsablauf sitzt, von Anfang bis Ende.</figcaption>
</figure>

## OEE und wo sie leckt
Overall Equipment Effectiveness multipliziert drei Dinge: Verfügbarkeit (läuft die Linie, wenn sie soll), Leistung (läuft sie mit Nenngeschwindigkeit) und Qualität (ist der Output beim ersten Mal gut). Eine Zahl, drei Wege zu verlieren. Der Fehler ist, allein die Verfügbarkeit zu jagen — große Ausfälle zu jagen —, wenn der eigentliche Abfluss meist die Leistung ist, ausgeblutet durch Mikrostopps: die Fünf-Sekunden-Stillstände, die dutzende Male pro Schicht passieren und einzeln kaum auffallen.

Und nicht jede Maschine zählt gleich viel. Der Füller und der Verschließer, oft mit dem Etikettierer, sind der Engpass; was immer sie verlieren, verliert die Linie. Ein Stau weiter oben, den der Puffer absorbiert, kostet nichts. Derselbe Stau am Füller kostet direkt Output. Das Ziel ist also klar, bevor irgendein Modell gebaut wird: Mikrostopps und Umrüstverluste am Engpass.

## Erst messen: das Linienleitsystem auswerten
Die Daten existieren bereits. Das Linienleitsystem protokolliert Stopps, Dauern, Fehlercodes, Geschwindigkeiten und Ausschusszahlen. Die Data-Science-Aufgabe ist, sie zu ehrlichen Merkmalen zu bereinigen — Stoppfrequenz je Station, Mikrostopp-Clustering, Geschwindigkeit gegen Nenngeschwindigkeit, Zeit-seit-Umrüstung, jüngste Fehlermuster — denn Rohprotokolle sind verrauscht, mit falsch beschrifteten und uncodierten Stopps, die das Bild schönen oder verzerren.

Mit sauberer Historie lernt ein Modell die Signaturen, die einem Stillstand vorausgehen: ein schleichender Anstieg kurzer Stopps am Verschließer, eine Vibrations- oder Drehmomentdrift, die Bedingungen, unter denen eine bestimmte Umrüstung lange dauert. Es sagt den nächsten wahrscheinlichen Verlust mit genug Vorlaufzeit zum Eingreifen voraus — die Linie leicht drosseln, ein verschlissenes Teil bei der nächsten Pause tauschen, einen Zulauf justieren — statt nach dem Stillstand zu reagieren. Du kommst Leistungsverlusten zuvor, dort verstecken sich die OEE-Punkte.

## Ein Copilot für den Schichtbericht
Der Generative-KI-Aspekt ist die Schichtende-Zusammenfassung, die niemand gern schreibt. Ein Copilot liest die Stillstandsprotokolle der Schicht und die Vorhersagen des Modells und erstellt die OEE-Zusammenfassung automatisch: die Zahl, ihre Aufschlüsselung in Verfügbarkeit, Leistung und Qualität, die Hauptursachen verlorener Zeit und eine geordnete Top-drei der Behebungen für die nächste Schicht. „Verschließer-Mikrostopps kosteten 22 Minuten, konzentriert nach der Umrüstung um 11:00; empfohlen, die Zulauf-Taktung zu prüfen und den verdächtigen Heber zu ersetzen." Die Übergabe hängt nicht mehr davon ab, wer gerade aufgepasst hat.

## Wo es scheitert
Die harte Grenze ist die Datenqualität. Wenn Bediener Stopps uncodiert lassen oder das Leitsystem Fehler falsch beschriftet, lernt das Modell Fiktion, und der Schichtbericht erbt sie still. Schlimmer noch: Vorhersage ist nicht Ursache — das Modell markiert steigende Verschließer-Stopps, aber die Grundursache ist mechanisch, und ein Instandhalter muss das verschlissene Teil immer noch finden und beheben. Es gibt hier keine autonome Reparatur. Behandle Vorhersagen als Frühwarnung, die Zeit kauft, nicht als Diagnose, und investiere in disziplinierte Stillstandscodierung, bevor du irgendetwas davon vertraust.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">REGELKREIS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Stillstandszeiten der Abfülllinie vorhersagen und die OEE heben</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Regler</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Stellglied</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Prozess</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">Rückführung</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen.</figcaption>
</figure>

## Das Fazit
Ziele auf Mikrostopps und Umrüstungen am Füller und Verschließer, nutze die eigenen Protokolle des Leitsystems, um Verluste vorherzusagen, bevor sie eintreten, und lass einen Copilot die OEE-Zusammenfassung und die wichtigsten Behebungen schreiben. Die Mathematik ist einfach — Verfügbarkeit mal Leistung mal Qualität — aber die Gewinne liegen in sauberen Daten und im Handeln am Engpass.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [vorausschauende Instandhaltung für Füller und Verschließer]({{ '/de/2024/predictive-maintenance-filler-seamer/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist OEE und wie wird sie berechnet?**
Overall Equipment Effectiveness ist Verfügbarkeit mal Leistung mal Qualität. Sie erfasst Stopps, Geschwindigkeitsverluste und Ausschussraten in einer Zahl und zeigt so die wahre Output-Lücke, nicht nur die Laufzeit.

**Warum sich auf Füller und Verschließer konzentrieren?**
Der Füller und der Verschließer, und manchmal der Etikettierer, sind meist der Linienengpass. Verluste dort begrenzen die ganze Linie, also ist eine am Engpass gesparte Minute eine Minute echten zusätzlichen Outputs.

**Was dominiert die Verluste der Abfülllinie?**
Mikrostopps und Umrüstungen, nicht große Ausfälle. Dutzende kurzer Stillstände pro Schicht erodieren Leistung und Verfügbarkeit leise stärker als der gelegentliche große Ausfall.
