---
layout: post
lang: de
title: "Ein Live-Dashboard zur Gärungsüberwachung in Tableau"
image: /assets/og/tableau-fermentation-monitoring-dashboard.png
description: "Baue ein Live-Dashboard zur Gärungsüberwachung in Tableau mit Stammwürze-, Temperatur- und CO2-Kurven pro Tank, Zielbändern und einer TabPy-ML-Prognose."
date: 2023-02-04
updated: 2023-02-04
permalink: /de/2023/tableau-fermentation-monitoring-dashboard/
tags: [brewing-science, tableau, fermentation]
faq:
  - q: "Kann Tableau Gärungsdaten in Echtzeit anzeigen?"
    a: "Nicht wirklich in Echtzeit. Tableau aktualisiert eine Live-Verbindung oder einen .hyper-Extrakt nach einem Zeitplan, sodass das Dashboard nahezu live ist — Minuten hinterher, nicht Sekunden. Für die meisten Gärungen ist eine Aktualisierung alle paar Minuten mehr als ausreichend."
  - q: "Wie zeige ich, ob eine Gärung im Plan liegt?"
    a: "Trage die Live-Kurven von Stammwürze und Temperatur gegen ein Zielband auf, das aus Referenzlinien oder einer schattierten Fläche aus vergangenen guten Chargen desselben Rezepts gebildet wird. Wenn die Kurve das Band verlässt, braucht der Tank Aufmerksamkeit."
  - q: "Ist die eingebaute Prognose von Tableau gut genug, um eine Gärung vorherzusagen?"
    a: "Für eine grobe Projektion einer glatten Kurve ja; sie nutzt exponentielle Glättung. Für eine echte Vorhersage von Vergärung oder steckengebliebener Gärung schiebe die Daten über TabPy an ein externes Modell und visualisiere dessen Ausgabe — die native Prognose von Tableau ist kein Prozessmodell."
---

**Kurze Antwort: Tableau gibt dir ein nahezu echtzeitfähiges Gärungs-Cockpit, kein Echtzeit-Steuerungssystem.** Es ist hervorragend darin, jeden Tank gegen sein Zielband anzuzeigen, damit ein Brauer eine driftende Gärung früh erkennt — vorausgesetzt, du bist ehrlich über die Aktualisierungsfrequenz und darüber, was die Prognose tatsächlich ist.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für ein Live-Dashboard zur Gärungsüberwachung in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Ein Live-Dashboard zur Gärungsüberwachung in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Schlüsselkennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerteilen.</figcaption>
</figure>

## Design für „verhält sich dieser Tank?"
Ein Gärungs-Dashboard beantwortet eine Frage pro Tank: Folgt diese Gärung dem erwarteten Pfad oder weicht sie davon ab? Alles im Design sollte dieser Frage dienen.

Beginne wie immer mit dem Datenmodell. Eine Zeile pro Messung: Tank, Charge, Rezept, Zeitstempel, Stammwürze, Temperatur und CO2 oder Druck, falls du es protokollierst. Der „erst messen"-Ertrag ist ein Zielband — leite für jedes Rezept aus einer Reihe historisch guter Chargen einen erwarteten Korridor von Stammwürze-über-Zeit und Temperatur-über-Zeit ab. Dieses Band ist deine Referenz; die Live-Kurve ist der Test.

Verbinde Tableau mit deinen Gärungsdaten entweder als Live-Verbindung oder, häufiger, als geplante `.hyper`-Extraktaktualisierung. So oder so ist das Dashboard nahezu live und hinkt der Realität um Minuten hinterher — was in Ordnung ist, denn eine gesunde Gärung bewegt sich über Stunden und Tage, nicht über Sekunden.

## Die Ansicht pro Tank aufbauen
Lege Small-Multiple-Liniendiagramme an, eines pro aktivem Tank, jedes mit der Live-Stammwürzekurve über das Zielband des Rezepts gelegt als schattiertes **Referenzband**. Die Temperatur auf einer Sekundärachse mit Doppelachse, und du siehst die klassische Beziehung: Die Temperatur steigt, die Stammwürze fällt, dann setzen sich beide. Ein berechnetes Feld markiert, wenn der aktuelle Punkt außerhalb des Bandes liegt, und löst einen Farbwechsel und einen einfachen „Achtung"-Indikator aus, damit ein Brauer, der zwanzig Tanks überblickt, den einen in Schwierigkeiten erkennt.

Filteraktionen lassen dich einen Tank anklicken und in seine vollständige Historie eintauchen — Gärungsstart, gelöster Sauerstoff beim Anstellen, Hefegeneration. Parameter lassen dich das Zielband zwischen Rezepten oder Stärken umschalten.

Für die Vorhersage gehst du hier über die eingebauten Funktionen von Tableau hinaus. Übergib die jüngste Kurve über **TabPy** an ein Modell — einen Python-Dienst, den Tableau aufrufen kann — und gib eine projizierte Endstammwürze oder eine Wahrscheinlichkeit für eine steckengebliebene Gärung zurück, dann trage diese Projektion als gestrichelte Verlängerung der Live-Kurve auf. Eine generative KI-Schicht kann dann aus diesen Projektionen die morgendliche „zu beobachtende Tanks"-Notiz entwerfen, die ein Brauer überprüft. Das ist eine echte Prognose, anders als die native Linie der exponentiellen Glättung, die zum Abschätzen eines Trends taugt, aber nichts über Hefe weiß.

Die tiefere Modellierungsfrage — was es tatsächlich braucht, um eine Gärung vorherzusagen — ist ihr eigenes Thema; siehe [Kann KI die Biergärung vorhersagen?]({{ '/de/2026/can-ai-predict-beer-fermentation/' | relative_url }}).

## Wo es scheitert
Die ehrliche Grenze ist das Wort „live". Tableau ist keine SCADA- oder Prozesssteuerungsplattform; es visualisiert Daten, die etwas anderes erfasst und abgelegt hat, nach einem Aktualisierungszeitplan. Verdrahte keine sicherheitskritischen Alarme mit einem Tableau-Extrakt — nutze es für Überwachung und Entscheidungsunterstützung, nicht zum Auslösen eines Ventils.

Die zweite Grenze ist die Prognose. Die eingebaute Prognose extrapoliert eine glatte Kurve und sieht überzeugend aus, aber sie kann einen Stillstand nicht antizipieren, denn sie hat kein Konzept von Vergärungsgrenzen oder Hefegesundheit. Selbst ein gutes TabPy-Modell ist nur so ehrlich wie seine Trainingsdaten; ein Rezept, das es nie gesehen hat, wird geraten, nicht gewusst. Und kein Modell — generativ oder anderweitig — ersetzt eine Spindelmessung oder eine schnelle Verkostung, wenn etwas falsch aussieht.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein geschlossener Regelkreis: messen, berechnen, betätigen — und das Ergebnis zurückführen."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">REGELKREIS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Ein Live-Dashboard zur Gärungsüberwachung in Tableau</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Regler</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Aktor</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Prozess</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">Rückkopplung</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein geschlossener Regelkreis: messen, berechnen, betätigen — und das Ergebnis zurückführen.</figcaption>
</figure>

## Das Fazit
Ein Tableau-Gärungs-Dashboard verwandelt eine Wand aus Tankmesswerten in eine auf einen Blick erfassbare Ansicht: jede Gärung gegen ihr erwartetes Band, mit hervorgehobenen Ausreißern. Behandle es als nahezu echtzeitfähige Überwachung, stütze dich für echte Vorhersage über TabPy auf ein externes Modell und halte den Brauer — nicht das Dashboard — bei den Entscheidungen, auf die es ankommt, in der Schleife.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [Kann KI die Biergärung vorhersagen?]({{ '/de/2026/can-ai-predict-beer-fermentation/' | relative_url }}).

## Häufig gestellte Fragen

**Kann Tableau Gärungsdaten in Echtzeit anzeigen?**
Nicht wirklich in Echtzeit. Tableau aktualisiert eine Live-Verbindung oder einen .hyper-Extrakt nach einem Zeitplan, sodass das Dashboard nahezu live ist — Minuten hinterher, nicht Sekunden. Für die meisten Gärungen ist eine Aktualisierung alle paar Minuten mehr als ausreichend.

**Wie zeige ich, ob eine Gärung im Plan liegt?**
Trage die Live-Kurven von Stammwürze und Temperatur gegen ein Zielband auf, das aus Referenzlinien oder einer schattierten Fläche aus vergangenen guten Chargen desselben Rezepts gebildet wird. Wenn die Kurve das Band verlässt, braucht der Tank Aufmerksamkeit.

**Ist die eingebaute Prognose von Tableau gut genug, um eine Gärung vorherzusagen?**
Für eine grobe Projektion einer glatten Kurve ja; sie nutzt exponentielle Glättung. Für eine echte Vorhersage von Vergärung oder steckengebliebener Gärung schiebe die Daten über TabPy an ein externes Modell und visualisiere dessen Ausgabe — die native Prognose von Tableau ist kein Prozessmodell.
