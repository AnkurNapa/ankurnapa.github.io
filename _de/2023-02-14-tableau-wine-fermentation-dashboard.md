---
layout: post
lang: de
title: "Ein Dashboard zur Überwachung der Weingärung in Tableau"
image: /assets/og/tableau-wine-fermentation-dashboard.png
description: "Baue ein Tableau-Gärungs-Dashboard, das pro Tank Brix- und Temperaturkurven, Flags für stockende Gärungen und YAN verfolgt — mit Explain-Data-Diagnostik."
date: 2023-02-14
updated: 2023-02-14
permalink: /de/2023/tableau-wine-fermentation-dashboard/
tags: [winemaking, tableau, fermentation]
faq:
  - q: "Was sollte ein Gärungs-Dashboard in Tableau tatsächlich zeigen?"
    a: "Den Brix-Abfall und die Temperatur je Tank gegen ein Zielband, dazu ein Flag für stockende Gärung und den Anfangs-YAN-Wert. Diese vier zusammen sagen dir, ob jeder Tank auf Kurs ist oder einen Eingriff braucht."
  - q: "Kann Tableau eine stockende Gärung erkennen?"
    a: "Es kann das Symptom markieren — eine Brix-Kurve, die oberhalb der Trockenheit abgeflacht ist — mithilfe eines berechneten Feldes, das den jüngsten Messwert mit den Vortagen vergleicht. Die Ursache kann es nicht diagnostizieren; das braucht weiterhin eine Kellerkraft und ein Labor."
  - q: "Funktioniert Explain Data bei Gärtanks?"
    a: "Explain Data kann aufzeigen, welche Felder in deinen Daten mit einem langsamen Tank korrelieren, etwa niedriges YAN oder ein Temperaturabfall. Behandle seine Ausgabe als Anstoß zur Untersuchung, nicht als Urteil."
---

**Kurze Antwort: Ein Gärungs-Dashboard verdient seinen Platz, wenn es den Brix-Abfall jedes Tanks gegen ein Temperaturband auf einem Bildschirm zeigt, sodass eine träge Gärung offensichtlich wird, bevor sie stockt.** Lege zuerst die Zielbänder fest; die Diagramme folgen.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für Ein Dashboard zur Überwachung der Weingärung in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Ein Dashboard zur Überwachung der Weingärung in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#ffffff" stroke="#00695c"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#4a6b64">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#00695c"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Trend</text><rect x="120" y="268" width="46" height="70" fill="#00695c"/><rect x="200" y="243" width="46" height="95" fill="#00695c"/><rect x="280" y="278" width="46" height="60" fill="#00695c"/><rect x="360" y="228" width="46" height="110" fill="#00695c"/><rect x="440" y="253" width="46" height="85" fill="#00695c"/><rect x="520" y="218" width="46" height="120" fill="#00695c"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#d8e6e1" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#4a6b64">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#00695c"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#00695c"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#00695c"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f0f6f5"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Kennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerschneiden.</figcaption>
</figure>

## Definiere die Bänder, bevor du baust
Die Data-Science-Gewohnheit — erst messen — zählt im Keller mehr als im Weinberg, denn Gärung bewegt sich in Stunden. Lege deine Zielfenster vorab fest: Weißweine, die kühl vergären, bei etwa 12 bis 18 °C, Rotweine warm bei 25 bis 30 °C, das Anfangs-YAN idealerweise irgendwo um 150 bis 250 mg/L. Diese Zahlen werden zu Parametern und Referenzbändern, nicht zu fest codierten Markierungen, sodass ein Winzer die Obergrenze der Weißweingärung verschieben kann, ohne die Arbeitsmappe zu bearbeiten.

Deine Quelle ist meist ein Tank-Protokollsystem oder ein in eine Tabelle exportiertes manuelles Protokoll. Eine Live-Verbindung ist während der Hauptgärung ideal; andernfalls genügt ein häufig aktualisierter .hyper-Extrakt. Tableau Prep bereinigt das unvermeidliche Durcheinander von Tank-Umbenennungen mitten im Jahrgang und verschmilzt die YAN-Ergebnisse des Labors mit den Temperaturprotokollen des Kellers.

## Das Small Multiple je Tank
Die Arbeitspferd-Ansicht ist ein Small-Multiple-Raster: ein Mini-Diagramm pro Tank, Zeit auf der Achse, Brix als absteigende Linie, mit dem Ziel-Temperaturband als schattierte Referenz gezeichnet. Färbe die Brix-Linie danach, ob die jüngste Temperatur innerhalb oder außerhalb des Bandes liegt, und der Keller liest es in Sekunden.

Eine FIXED-Level-of-Detail-Berechnung fixiert den Anfangs-Brix jedes Tanks — `{FIXED [Tank] : MIN([Brix])}` — sodass du den Prozentsatz des verbrauchten Zuckers berechnen kannst, unabhängig davon, wie viele Messwerte ein Tank hat. Ein Flag für stockende Gärung ist eine Tabellenberechnung, die den jüngsten Brix mit dem Messwert zwei oder drei Tage zuvor vergleicht: Wenn er sich kaum bewegt hat und oberhalb der Trockenheit liegt, wird der Tank rot. Füge eine Parameteraktion hinzu, sodass ein Klick auf einen Tank seine vollständige Detailansicht mit YAN- und biologischem Säureabbau-Status lädt.

## Lass Explain Data den langsamen Tank befragen
Wenn ein Tank nachhinkt, mache einen Rechtsklick auf die Markierung und führe Explain Data aus. Einsteins Explain Data durchsucht die anderen Felder und meldet, was diesen Tank statistisch unterscheidet — vielleicht startete er mit niedrigem YAN, oder seine Temperatur fiel über Nacht ab. Das ist ein schneller, nützlicher Anstoß. Tableau Pulse, auf die kellerweite Kennzahl „Tanks außerhalb des Ziels" gesetzt, sendet einen morgendlichen Überblick, sodass das Team weiß, wohin es zuerst gehen soll.

## Wo es scheitert
Die ehrlichen Grenzen betreffen Taktung und Biologie. Wenn deine Sensoren alle sechs Stunden protokollieren, kann das Dashboard keine Temperaturspitze erfassen, die dazwischen ihren Höhepunkt erreicht und vorbeizieht. Spontan- und Wildgärungen sind von Natur aus unberechenbar — eine flache Brix-Kurve könnte eine gesunde Anlaufphase sein, kein Stocken — sodass ein naives Stockungs-Flag bei einem langsamen-aber-gesunden Tank falschen Alarm schlägt. Explain Data kennt nur die Spalten, die du ihm gegeben hast; es wird nie vorschlagen, dass der wahre Übeltäter eine Nährstoffgabe war, die niemand protokolliert hat. Und kein Dashboard steuert SO2 oder riecht die schleichend steigende flüchtige Säure; das bleibt eine menschliche Aufgabe.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein geschlossener Regelkreis: messen, rechnen, stellen — dann das Ergebnis zurückspeisen."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">REGELKREIS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Ein Dashboard zur Überwachung der Weingärung in Tableau</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Regler</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Aktor</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Prozess</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">Rückkopplung</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein geschlossener Regelkreis: messen, rechnen, stellen — dann das Ergebnis zurückspeisen.</figcaption>
</figure>

## Das Fazit
Ein Tableau-Gärungs-Dashboard ist ein Frühwarnraster: Brix je Tank gegen ein Temperaturband, ein Stockungs-Flag und YAN-Kontext, wobei Explain Data und Pulse dich auf den Tank zeigen, der Aufmerksamkeit braucht. Setze die Zielbänder als Parameter, respektiere die Taktung deiner Sensoren, und denk daran, dass das Dashboard Symptome markiert, während der Keller Ursachen diagnostiziert.

*Teil des Tracks [Weinbereitung & KI]({{ '/de/tracks/winemaking-ai/' | relative_url }}).* Verwandt: [KI-Steuerung der Weingärung]({{ '/de/2024/ai-wine-fermentation-control/' | relative_url }}).

## Häufig gestellte Fragen

**Was sollte ein Gärungs-Dashboard in Tableau tatsächlich zeigen?**
Den Brix-Abfall und die Temperatur je Tank gegen ein Zielband, dazu ein Flag für stockende Gärung und den Anfangs-YAN-Wert. Diese vier zusammen sagen dir, ob jeder Tank auf Kurs ist oder einen Eingriff braucht.

**Kann Tableau eine stockende Gärung erkennen?**
Es kann das Symptom markieren — eine Brix-Kurve, die oberhalb der Trockenheit abgeflacht ist — mithilfe eines berechneten Feldes, das den jüngsten Messwert mit den Vortagen vergleicht. Die Ursache kann es nicht diagnostizieren; das braucht weiterhin eine Kellerkraft und ein Labor.

**Funktioniert Explain Data bei Gärtanks?**
Explain Data kann aufzeigen, welche Felder in deinen Daten mit einem langsamen Tank korrelieren, etwa niedriges YAN oder ein Temperaturabfall. Behandle seine Ausgabe als Anstoß zur Untersuchung, nicht als Urteil.
