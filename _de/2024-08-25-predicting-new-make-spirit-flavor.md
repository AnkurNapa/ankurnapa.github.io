---
layout: post
lang: de
title: "Das Aroma von New-Make-Spirit vorhersagen"
image: /assets/og/predicting-new-make-spirit-flavor.png
description: "Wie KI und Data Science die Kongenere von New-Make-Spirit aus Gärung, Brennblasenform und Schnitt modellieren, damit Brenner das Aroma vor dem Fass steuern."
date: 2024-08-25
updated: 2024-08-25
permalink: /de/2024/predicting-new-make-spirit-flavor/
tags: [distilling-maturation, whiskey, flavor]
faq:
  - q: "Was treibt das Aroma von New-Make-Spirit an?"
    a: "Kongenere tun es: Ester geben Fruchtigkeit, höhere Alkohole geben Körper, und Aldehyde und Schwefelverbindungen geben grüne oder herzhafte Noten. Diese werden von der Gärdauer, der Brennblasenform und dem Rücklauf, dem Kupferkontakt und davon geprägt, wo du den Brennlauf schneidest."
  - q: "Kann ein Modell wirklich das Aroma vor der Destillation vorhersagen?"
    a: "Es kann das chemische Kongenerprofil recht gut aus den Prozesseingaben vorhersagen, und dieses Profil korreliert mit dem Aroma. Aber die sensorische Verkostung bleibt der letzte Richter, denn Wahrnehmung ist keine einfache Summe von Verbindungen."
  - q: "Wie viele historische Daten brauche ich für den Start?"
    a: "Genug beschriftete Chargen, um deine normale Bandbreite an Gärdauern, Brennblaseneinstellungen und Schnitten abzudecken, idealerweise mit sowohl GC-Analyse als auch Verkostungsbewertungen. Ein paar Dutzend gut dokumentierte Chargen schlagen Hunderte schlecht protokollierte."
---

**Kurze Antwort: Ein Modell kann das Kongenerprofil deines New-Make aus den Prozesseingaben vorhersagen, sodass du den Charakter steuern kannst, bevor der Spirit je ein Fass sieht.** Die sensorische Verkostung bestätigt das Ergebnis weiterhin, aber du fliegst nicht mehr blind.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Whiskey-Produktionsfluss steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSFLUSS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Das Aroma von New-Make-Spirit vorhersagen</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Brennen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Reifung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllen</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Whiskey-Produktionsfluss steht, von Anfang bis Ende.</figcaption>
</figure>

## Das Aroma wird vor dem Fass festgelegt
Es ist verlockend, die Reifung als den Ort zu behandeln, an dem das Aroma entsteht, aber der New-Make-Spirit kommt bereits mit seiner DNA am Fass an. Diese DNA sind Kongenere: Ester für fruchtige Noten, höhere oder Fusel-Alkohole für Körper und Gewicht, Aldehyde für grünen und grasigen Charakter und Schwefelverbindungen für herzhafte oder fleischige Noten, die der Kupferkontakt später herausnimmt. Mach den New-Make falsch, und kein Fass wird ihn vollständig retten.

Diese Kongenere sind nicht zufällig. Sie reagieren auf Hebel, die du bereits ziehst. Lange Gärungen treiben mehr Ester und einen fruchtigeren Spirit. Die Brennblasenform und der Grad des Rücklaufs entscheiden, wie viel schweres Material übergeht: hohe Hälse und hoher Rücklauf machen einen leichteren, saubereren Spirit. Kupferkontakt entfernt Schwefel. Und der Schnitt, wo du das Herz des Laufs ziehst, legt das Gleichgewicht von leichten und schweren Kongeneren im fertigen Spirit fest.

## Die Hebel modellieren
Der Data-Science-Schritt besteht darin, diese Hebel zu expliziten Merkmalen und das Kongenerprofil zum Ziel zu machen. Erst messen: Protokolliere Gärdauer und -temperatur, Brennblasengeometrie und Rücklaufbedingungen, Kupferexposition und Schnittpunkte für jede Charge. Koppele jede Charge mit einer GC-Analyse ihrer Kongenere und, entscheidend, einer sensorischen Bewertung.

Ein Regressions- oder Gradient-Boosting-Modell lernt dann, wie Eingaben auf Ausgaben abgebildet werden. Frage es, was passiert, wenn du die Gärung um zwölf Stunden verlängerst oder einen Tick früher schneidest, und es schätzt die Verschiebung der Ester- und Fuselwerte. Das verwandelt Aroma von etwas, das man im Nachhinein entdeckt, in etwas, das man gezielt anvisiert. Für eine Brennerei, die einen Hausstil über Jahreszeiten und Rohstoffschwankungen halten will, ist diese Vorhersagbarkeit mehr wert als jedes einzelne clevere Rezept.

Das liegt direkt stromabwärts davon, wie du den Schnitt setzt. Dieselbe Mittellauf-Entscheidung, die Konsistenz antreibt, bewegt auch das Kongenergleichgewicht, weshalb es sich lohnt, die beiden gemeinsam zu modellieren; siehe [Destillations-Schnittpunkte wählen]({{ '/de/2024/predicting-distillation-cut-points-ai/' | relative_url }}).

## Wo das Modell danebenliegt
Die ehrliche Grenze ist Wechselwirkung. Die Kongenerbildung ist ein Netz aus gekoppelter Chemie und Biologie, kein Satz unabhängiger Regler. Eine Änderung der Gärdauer wirkt mit der Hefegesundheit zusammen, die mit der Brennblasenbeladung zusammenwirkt, die mit dem Schnitt zusammenwirkt. Modelle erfassen die starken, wiederholten Muster; sie kämpfen mit den seltenen Kombinationen, die sie nie gesehen haben, und sie werden bereitwillig mit falschem Selbstvertrauen über deinen tatsächlichen Betriebsbereich hinaus extrapolieren.

Dann gibt es die Wahrnehmung. Aroma ist nicht die arithmetische Summe der Verbindungen. Zwei Spirituosen mit nahezu identischen GC-Profilen können unterschiedlich schmecken, und ein Modell, das Chemie vorhersagt, sagt nicht das Urteil des Panels vorher. Behandle das vorhergesagte Profil als starke Hypothese und lass die Verkostung es bestätigen. Wo das Modell klaren Wert hinzufügt, ist das Eingrenzen der Suche und das frühe Markieren von Chargen, die vom Stil abdriften, nicht das Erklären eines Spirits für gut.

## Das Modell in einfachem Deutsch fragen
Der generative Blickwinkel dreht die übliche Richtung um. Statt Einstellungen einzuspeisen und ein Profil herauszulesen, lässt dich ein generativer Assistent das Ziel angeben: „Welche Wash- und Brennblaseneinstellungen geben mir einen esterbetonten, leicht schwefligen New-Make bei diesem ABV?" Das Modell schlägt dann Kandidaten für Gärdauern, Rücklaufbedingungen und Schnittpunkte vor, die nahe am Ziel landen, mit vermerkten Kompromissen. Es ist ein Designwerkzeug, das den Rezeptraum weit schneller erkundet als Versuchschargen, während du das letzte Wort behältst, welcher Kandidat es wert ist, tatsächlich destilliert zu werden.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Was die Reifung antreibt und was sie stromabwärts verändert."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WAS SIE ANTREIBT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Das Aroma von New-Make-Spirit vorhersagen</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Reifung</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Qualität</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Kosten / Risiko</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Was die Reifung antreibt und was sie stromabwärts verändert.</figcaption>
</figure>

## Das Fazit
Du kannst das New-Make-Aroma aus den Eingaben vorhersagen und steuern, die du bereits kontrollierst, vorausgesetzt, du misst Kongenere und verkostest konsistent. Das Modell grenzt die Optionen ein und fängt Drift ab; das Panel beurteilt den Spirit weiterhin. Baue zuerst die Datengewohnheit auf, denn die Vorhersage ist nur so gut wie die Chargen, die du protokolliert hast.

*Teil des Tracks [Destillation & Reifung]({{ '/de/tracks/distilling-maturation/' | relative_url }}).*

## Häufig gestellte Fragen

**Was treibt das Aroma von New-Make-Spirit an?**
Kongenere tun es: Ester geben Fruchtigkeit, höhere Alkohole geben Körper, und Aldehyde und Schwefelverbindungen geben grüne oder herzhafte Noten. Diese werden von der Gärdauer, der Brennblasenform und dem Rücklauf, dem Kupferkontakt und davon geprägt, wo du den Brennlauf schneidest.

**Kann ein Modell wirklich das Aroma vor der Destillation vorhersagen?**
Es kann das chemische Kongenerprofil recht gut aus den Prozesseingaben vorhersagen, und dieses Profil korreliert mit dem Aroma. Aber die sensorische Verkostung bleibt der letzte Richter, denn Wahrnehmung ist keine einfache Summe von Verbindungen.

**Wie viele historische Daten brauche ich für den Start?**
Genug beschriftete Chargen, um deine normale Bandbreite an Gärdauern, Brennblaseneinstellungen und Schnitten abzudecken, idealerweise mit sowohl GC-Analyse als auch Verkostungsbewertungen. Ein paar Dutzend gut dokumentierte Chargen schlagen Hunderte schlecht protokollierte.
