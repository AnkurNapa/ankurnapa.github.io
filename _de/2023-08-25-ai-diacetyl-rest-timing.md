---
layout: post
lang: de
title: "KI nutzen, um die Diacetylrast zu timen"
image: /assets/og/ai-diacetyl-rest-timing.png
description: "Vorhersagen, wann die Diacetylrast zu beginnen und zu beenden ist, um VDKs unter 0,10 mg/L zu drücken, ohne Tankzeit zu verschwenden — anhand von Stammwürze, Temperatur und Hefezustand."
date: 2023-08-25
updated: 2023-08-25
permalink: /de/2023/ai-diacetyl-rest-timing/
tags: [brewing-science, fermentation, flavor]
faq:
  - q: "Was ist eine Diacetylrast?"
    a: "Es ist das Anheben der Gärtemperatur, meist etwa nach zwei Dritteln, um die Wiederaufnahme und Reduktion von Diacetyl und anderen VDKs durch die Hefe zu geschmacklosen Verbindungen zu beschleunigen, bevor du kühlst und abfüllst."
  - q: "Welchen Diacetyl-Wert sollte ich anstreben?"
    a: "Unter der Geschmacksschwelle von rund 0,10 mg/L für Diacetyl (Butterscotch). Die verwandte Verbindung 2,3-Pentandion hat eine höhere Schwelle nahe 1 mg/L."
  - q: "Warum kommt Diacetyl zurück oder bleibt hoch?"
    a: "Vorzeitige Flockung lässt die Hefe ausfallen, bevor sie die Wiederaufnahme abschließt, sodass Rest-VDK zurückbleibt. Auch eine Pediococcus-Kontamination produziert Diacetyl, was eine Rast nicht beheben wird."
---

**Kurze Antwort: Ein Modell kann den Beginn und das Ende der Diacetylrast aus Stammwürze, Temperatur, VDK-Messungen und Hefezustand bestimmen, sodass du Butterscotch beseitigst, ohne den Tank tagelang "zur Sicherheit" zu parken.** Tankzeit ist Geld, und die meisten Rasten werden aus Gewohnheit getimt.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsfluss sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSFLUSS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">KI nutzen, um die Diacetylrast zu timen</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllen</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Bierproduktionsfluss sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Die Chemie, die du timst
Diacetyl (2,3-Butandion) ist der klassische Butterscotch-Fehlgeschmack mit einer Schwelle um 0,10 mg/L. Der Weg ist wichtig, weil er bestimmt, was du kontrollieren kannst. Während des Wachstums scheidet die Hefe Alpha-Acetolactat aus. Außerhalb der Zelle durchläuft diese Verbindung eine spontane oxidative Decarboxylierung zu Diacetyl. Dieser Schritt ist nicht-enzymatisch und geschwindigkeitsbestimmend, weshalb Diacetyl *nachdem* die Hefe ihre Hauptarbeit erledigt hat erscheinen kann. Die Hefe nimmt das Diacetyl dann wieder auf und reduziert es zu Acetoin und weiter zum geschmacklosen 2,3-Butandiol.

Die Diacetylrast nutzt den letzten Schritt aus: Hebe die Temperatur etwa nach zwei Dritteln der Gärung an, und die Hefe beseitigt VDKs schneller. Time sie falsch, und du kühlst entweder zu früh und schließt Alpha-Acetolactat ein, das sich später in der Abfüllung umwandelt, oder du hältst unnötig warm und verlierst Durchsatz.

## Was das Modell beobachtet
Das ist ein Erst-messen-Problem. Die nützlichen Signale sind:

- **Stammwürzeverlauf** und seine Steigung, um den Zweidrittel-Punkt in Echtzeit zu lokalisieren statt per Rezeptschätzung.
- **Temperaturverlauf** des tatsächlichen Tanks.
- **VDK-Messungen**, idealerweise ein Gesamt-VDK-Assay, das sowohl freies Diacetyl als auch den noch auf die Umwandlung wartenden Alpha-Acetolactat-Vorläufer erfasst.
- **Hefezustand**: Anstellrate, Generation und Flockungsverhalten.

Ein auf vergangenen Gärungen trainiertes Modell sagt voraus, wann Alpha-Acetolactat seinen Höhepunkt erreicht hat, wann die Rast zu beginnen ist und wann das Rest-VDK unter 0,10 mg/L fällt. Die Ausgabe sind zwei Zeitstempel und ein Konfidenzband, keine feste Rezeptregel. Für Brauer, die das ALDC-Enzym (etwa Maturex) verwenden, das Alpha-Acetolactat direkt zu Acetoin umwandelt und Diacetyl gänzlich umgeht, verschiebt sich die Rolle des Modells dahin, zu bestätigen, dass die Umgehung funktioniert hat, statt eine lange Rast zu timen.

## Wo es bricht
Die ehrliche Grenze sind Daten. Ohne periodische VDK-Messung schließt das Modell auf genau das eine, was den Endpunkt tatsächlich definiert, und ein Gesamt-VDK-Assay (erzwungen oder erhitzt) ist das, was eingeschlossenen Vorläufer offenbart. Auch zwei Störfaktoren beißen. Vorzeitige Flockung lässt die Hefe ausfallen, bevor die Wiederaufnahme abgeschlossen ist, sodass dieselbe Stammwürzekurve hohes Rest-VDK ergibt; das Modell braucht die Flockung als Merkmal, sonst ruft es die Rast zu früh aus. Und eine Pediococcus-Kontamination produziert Diacetyl unabhängig vom normalen Stoffwechsel, sodass eine Rast es nicht beheben kann. Bleiben die Messwerte trotz eines sauberen Profils hoch, ist die Antwort eine mikrobiologische Prüfung, nicht mehr Warmzeit.

Eine praktische Ergänzung ist ein Assistent, der die Entscheidung trifft und sie dokumentiert. Er liest die Live-Stammwürze, -Temperatur und das letzte VDK-Ergebnis, empfiehlt, die Rast zu beginnen oder zu beenden, und entwirft die Tankaktionsnotiz mit den Zahlen und der Begründung. Das hält die Entscheidung über Schichten hinweg konsistent und hinterlässt eine Aufzeichnung darüber, warum jede Rast so getimt wurde, wie sie getimt wurde.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Was die Gärung antreibt und was sie nachgelagert verändert."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WAS SIE ANTREIBT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">KI nutzen, um die Diacetylrast zu timen</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Gärung</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Qualität</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Kosten / Risiko</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Was die Gärung antreibt und was sie nachgelagert verändert.</figcaption>
</figure>

## Das Fazit
Die Diacetylrast ist ein Timing-Problem mit klarer chemischer Grundlage, und Timing-Probleme sind dort, wo Modelle ihren Wert beweisen. Speise Stammwürze, Temperatur, VDK-Messungen und Hefezustand ein, achte auf Flockung und Kontamination, und du kannst unter 0,10 mg/L treffen, ohne Tage an Kapazität zu verbrennen. Miss VDK, nimm es nicht an.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [Ester- und Höhere-Alkohole-Bildung prognostizieren]({{ '/de/2023/forecasting-ester-higher-alcohol-formation/' | relative_url }})

## Häufig gestellte Fragen

**Was ist eine Diacetylrast?**
Es ist das Anheben der Gärtemperatur, meist etwa nach zwei Dritteln, um die Wiederaufnahme und Reduktion von Diacetyl und anderen VDKs durch die Hefe zu geschmacklosen Verbindungen zu beschleunigen, bevor du kühlst und abfüllst.

**Welchen Diacetyl-Wert sollte ich anstreben?**
Unter der Geschmacksschwelle von rund 0,10 mg/L für Diacetyl (Butterscotch). Die verwandte Verbindung 2,3-Pentandion hat eine höhere Schwelle nahe 1 mg/L.

**Warum kommt Diacetyl zurück oder bleibt hoch?**
Vorzeitige Flockung lässt die Hefe ausfallen, bevor sie die Wiederaufnahme abschließt, sodass Rest-VDK zurückbleibt. Auch eine Pediococcus-Kontamination produziert Diacetyl, was eine Rast nicht beheben wird.
