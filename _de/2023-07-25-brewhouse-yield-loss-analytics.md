---
layout: post
lang: de
title: "Sudhausausbeute: Mit Analytik finden, wo der Extrakt verschwindet"
image: /assets/og/brewhouse-yield-loss-analytics.png
description: "Nutze Massenbilanzrechnung und Analytik, um die Lücke zwischen theoretischem und tatsächlichem Extrakt auf Schroten, Läutern, Trub, Transfer und Verdampfung zuzuordnen."
date: 2023-07-25
updated: 2023-07-25
permalink: /de/2023/brewhouse-yield-loss-analytics/
tags: [brewing-science, brewhouse, analytics]
faq:
  - q: "Ist das ein KI-Projekt oder ein Buchhaltungsprojekt?"
    a: "Zuerst Buchhaltung. Eine Massenbilanz, die den Extraktverlust auf Schroten, Läuterretention, Trub und Totstrecken, Transfer und Verdampfung zuordnet, sagt dir das meiste von dem, was du brauchst. Modellierung und KI kommen, nachdem die Zahlen aufgehen."
  - q: "Was ist üblicherweise der größte Verlust?"
    a: "Das variiert je nach Brauerei, was genau der Sinn des Messens statt Ratens ist. Häufige Übeltäter sind Läuter-Treberretention, Trub- und Totstreckenverluste sowie überdimensionierte Verdampfung — aber du behebst das größte Leck, das du tatsächlich findest, nicht das, das du annimmst."
  - q: "Wie genau müssen meine Daten sein?"
    a: "Genau genug, um die Massenbilanz zu schließen. Wenn theoretisch minus gemessene Verluste nicht mit dem tatsächlichen Extrakt aufgeht, hast du eine Messlücke zu beheben, bevor irgendeine Analytik oder ein Modell vertrauenswürdig ist."
---

**Kurze Antwort: Bevor du irgendetwas modellierst, baue eine Massenbilanz, die die Lücke zwischen theoretischem und tatsächlichem Extrakt auf jeden Verlustpunkt zuordnet — und behebe dann zuerst das größte Leck.** Sudhausausbeute ist ein Buchhaltungsproblem, bevor sie ein KI-Problem ist.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsfluss sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSFLUSS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Sudhausausbeute: Mit Analytik finden, wo der Extrakt verschwindet</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllung</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Bierproduktionsfluss sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Ausbeuteverlust hat benannte Adressen
Die Lücke zwischen dem theoretischen Extrakt und dem, was im Gärtank landet, ist kein Rätsel; sie hat konkrete Adressen. Extrakt entweicht beim Schroten und Quetschen, an der Läuter-Treberretention, in Trub und Totstrecken, während Transfer und Whirlpool sowie durch Verdampfung beim Kochen. Jeder ist ein realer, zuordenbarer Verlust.

Die Massenbilanzrechnung ist die Disziplin, den fehlenden Extrakt diesen Adressen zuzuweisen. Du startest vom theoretischen Extrakt für die Schüttung, ziehst jeden gemessenen Verlust ab und siehst, ob der Rest mit dem tatsächlichen Extrakt im Gärtank übereinstimmt. Wenn es aufgeht, hast du ein wahres Bild davon, wohin deine Ausbeute geht. Wenn nicht, ist die Diskrepanz selbst Information — meist eine Messung, die du nicht vornimmst.

## Buchhaltung vor Modellierung
Das ist der datenwissenschaftliche Punkt, der eine Wiederholung wert ist: zuerst messen, und in diesem Fall *ist* die Messung der Großteil der Arbeit. Eine saubere Massenbilanz beantwortet die Frage oft direkt, ohne ein Modell. Wiege die Schüttung, bemustere Würzedichte und -volumen bei jedem Transfer, quantifiziere Treber-Restfeuchte und zurückgehaltenen Extrakt, miss das Trubvolumen und verfolge die Verdampfung. Lege das gegen den theoretischen Extrakt und die Lecks zeigen sich von selbst.

Erst wenn die Bilanz aufgeht, fügt Analytik Wert hinzu — etwa zu erkennen, dass die Läuterretention mit der Quetschung driftet oder dass die Verdampfung bei langgekochten Rezepten ansteigt. Das ist auch der Grund, warum ein Ausbeuteprogramm davon abhängt, überhaupt die richtigen Daten gesammelt zu haben; unsere Notiz über das [Sammeln deiner Daten vor der KI]({{ '/de/2026/collect-your-data-before-ai/' | relative_url }}) legt das klar dar. Für die Maischeseite derselben Rechnung siehe [Maischeeffizienz und Extraktausbeute vorhersagen]({{ '/de/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}).

## Von einer Bilanz zu einer priorisierten Maßnahmenliste
Der Aspekt der generativen KI ist bescheiden, aber wirklich nützlich. Eine Massenbilanz ist eine Zahlentabelle, auf die die meisten Brauer nicht reagieren werden. Ein LLM kann diese Tabelle lesen und sie in eine priorisierte, klar formulierte Maßnahmenliste verwandeln: "Dein größtes Leck in diesem Quartal ist die Läuter-Treberretention mit 1,9 % des Extrakts — überprüfe zuerst Quetschung und Sparge-Volumen. Die Verdampfung ist mit 1,1 % an zweiter Stelle; Trubverluste sind gering und noch nicht der Verfolgung wert." Es übersetzt Buchhaltung in Prioritäten, mit angehängter Begründung, sodass das Sudhaus das größte Leck behebt statt des sichtbarsten.

## Wo es bricht
Die Grenze ist die Messehrlichkeit. Eine Massenbilanz ist nur so gut wie die Messwerte, die sie speisen, und Brauereien untermessen routinemäßig Trubvolumen, Totstreckenrückhalt und Treberextrakt, weil sie schwer zu beproben sind. Wenn diese Zahlen Schätzungen sind, schließt die Bilanz auf falscher Präzision und die priorisierte Maßnahmenliste weist dich auf das falsche Leck hin. Verdampfungs- und Transferverluste können sich auch ineinander verstecken, wenn deine Volumenmessungen grob sind. Die Lösung ist kein ausgefeilteres Modell — es ist bessere Instrumentierung und konsistente Probenahme, bis die Bilanz wirklich aufgeht. Widerstehe dem Drang, Analytik über Zahlen zu schichten, die nicht stimmen.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Was den Prozess treibt und was es stromabwärts verändert."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WAS ES TREIBT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Sudhausausbeute: Mit Analytik finden, wo der Extrakt verschwindet</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Der Prozess</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Qualität</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Kosten / Risiko</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Was den Prozess treibt und was es stromabwärts verändert.</figcaption>
</figure>

## Das Fazit
Sudhausausbeute gewinnt man mit Arithmetik, nicht mit Algorithmen. Baue eine Massenbilanz, die verlorenen Extrakt dem Schroten, Läutern, Trub, Transfer und der Verdampfung zuordnet; schließe sie mit ehrlicher Messung; lass dann ein generatives Werkzeug die Lecks in eine Maßnahmenliste priorisieren. Behebe das größte, miss neu und wiederhole. Die KI ist hier der Bote — die Buchhaltung leistet die Arbeit.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [Sammeln deiner Daten vor der KI]({{ '/de/2026/collect-your-data-before-ai/' | relative_url }}).

## Häufig gestellte Fragen

**Ist das ein KI-Projekt oder ein Buchhaltungsprojekt?**
Zuerst Buchhaltung. Eine Massenbilanz, die den Extraktverlust auf Schroten, Läuterretention, Trub und Totstrecken, Transfer und Verdampfung zuordnet, sagt dir das meiste von dem, was du brauchst. Modellierung und KI kommen, nachdem die Zahlen aufgehen.

**Was ist üblicherweise der größte Verlust?**
Das variiert je nach Brauerei, was genau der Sinn des Messens statt Ratens ist. Häufige Übeltäter sind Läuter-Treberretention, Trub- und Totstreckenverluste sowie überdimensionierte Verdampfung — aber du behebst das größte Leck, das du tatsächlich findest, nicht das, das du annimmst.

**Wie genau müssen meine Daten sein?**
Genau genug, um die Massenbilanz zu schließen. Wenn theoretisch minus gemessene Verluste nicht mit dem tatsächlichen Extrakt aufgeht, hast du eine Messlücke zu beheben, bevor irgendeine Analytik oder ein Modell vertrauenswürdig ist.
