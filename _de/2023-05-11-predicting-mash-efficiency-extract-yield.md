---
layout: post
lang: de
title: "Kann KI Sudhausausbeute und Extraktausbeute vorhersagen?"
image: /assets/og/predicting-mash-efficiency-extract-yield.png
description: "Ein Modell kann Maischeeffizienz und Pfannenextrakt aus Schrot, Maischedicke, Temperaturprofil, Läutern und Malzanalyse vorhersagen — und ertragsschwache Sude früh erkennen."
date: 2023-05-11
updated: 2023-05-11
permalink: /de/2023/predicting-mash-efficiency-extract-yield/
tags: [brewing-science, brewhouse, machine-learning]
faq:
  - q: "Was sagt ein Modell zur Maischeeffizienz vorher?"
    a: "Es sagt voraus, wie viel des Extraktpotenzials der Schüttung du tatsächlich in die Pfanne zurückgewinnst — aus Eingaben wie Schrot, Maischedicke, Temperatur- und Zeitprofil, Läutern und der Malzanalyse."
  - q: "Kann KI mir sagen, dass ein Sud den Ertrag verfehlt, bevor es passiert?"
    a: "Sie kann einen Sud aus Rezept- und Prozesseinstellungen als wahrscheinlich ertragsschwach markieren und dir die Chance geben, das Läutern anzupassen oder die Maische zu verlängern. Sie kann ein bereits steckengebliebenes Läutern nicht beheben."
  - q: "Was hindert ein Ertragsmodell am Funktionieren?"
    a: "Inkonsistenter Prozess und schlechte Protokollierung. Wenn dein Mühlenspalt und dein Läuterverhalten von Charge zu Charge driften und du Einstellungen nicht aufzeichnest, hat das Modell nichts Stabiles, woraus es lernen kann."
---

**Kurze Antwort: Ja, in vernünftigem Rahmen — ein Modell kann Maischeeffizienz und Pfannenextrakt aus deinem Schrot, Maischeprofil, Läutern und der Malzanalyse vorhersagen und einen ertragsschwachen Sud früh erkennen, aber nur, wenn dein Prozess konsistent und gut protokolliert ist.** Es ist ein nützliches Frühwarnsystem, kein Ersatz für solide Sudhauspraxis.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsablauf sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Kann KI Sudhausausbeute und Extraktausbeute vorhersagen?</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gären</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllen</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Bierproduktionsablauf sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Was „Effizienz" wirklich misst
Maischeeffizienz, oder Extraktausbeute, ist schlicht, wie viel des Extraktpotenzials des Getreides du tatsächlich in die Pfanne zurückgewinnst. Die Obergrenze wird durch den Heißwasserextrakt des Malzes gesetzt; die Lücke zwischen dieser Obergrenze und dem, was du sammelst, ist der Punkt, an dem das Sudhaus entweder Geld verdient oder verliert. Diese Lücken kommen aus bekannten Quellen: dem Schrot deiner Mühle, der Maischedicke, der Maischedauer und -temperatur, der Läutertechnik und Läuterretention sowie Trub-, Totraum- und Transferverlusten auf dem Weg zur Pfanne.

Weil jeder dieser Treiber messbar ist, ist die Vorhersage des Ergebnisses ein handhabbares Problem. Gib einem Modell die Schroteinstellung, die Schüttung, die Maischedicke, das Temperatur-Zeit-Profil, das Läutervolumen und die Läutertemperatur sowie die Malzanalyse, und es kann den Extrakt abschätzen, den du sammeln wirst. Der Wert liegt im Timing: Eine Vorhersage, die beim Ansetzen des Suds oder mitten in der Maische getroffen wird, lässt Raum zum Reagieren — die Rast verlängern, das Läutern anpassen —, bevor die Stammwürze in die Pfanne festgelegt ist.

## Datenqualität entscheidet über alles
Dieses Modell steht und fällt mit der Protokollierungsdisziplin, weshalb die datenwissenschaftliche Grundlagenarbeit wichtiger ist als die Algorithmuswahl. Die Merkmale sind operativ: Mühlenspalt, Maischedicke-Verhältnis, Rasttemperaturen und -dauern, Läuterwasservolumen und -temperatur (unter etwa 78 °C gehalten, um das Auswaschen von Tanninen zu vermeiden) und die Malzwerte. Das Label ist der Extrakt, den du tatsächlich in die Pfanne erreicht hast.

„Erst messen" ist hier kein Slogan, sondern die ganze Arbeit. Wenn du deine Mühleneinstellung, deine Maischetemperaturen und deine Läutervolumina nicht konsistent aufzeichnest, lernt das Modell aus Rauschen. Sudhäuser, die diese bereits in einem Chargenprotokoll erfassen, sind fast am Ziel; jene, die das nicht tun, sollten die Protokollierung beheben, bevor sie die Modellierung anrühren. Ein auf sauberen, konsistenten Chargendaten trainiertes Modell erkennt die Muster — diese Schüttung bei dieser Dicke mit jenem Läutern läuft tendenziell einen Punkt zu niedrig —, die über eine Handvoll Sude hinweg unsichtbar sind.

## Wo es scheitert
Die ehrliche Grenze ist, dass physische Drift dominiert. Eine Mühle, die aus dem Spalt wandert, oder ein Läuterbett, das sich verdichtet und Kanäle bildet, wird deine reale Effizienz stärker schwanken lassen als jede Feinheit, die das Modell erfasst — und das Modell kann ein mechanisches Problem nicht sehen, für das es keinen Sensor hat. Wenn dein Prozess wirklich von Charge zu Charge inkonsistent ist, werden die Vorhersagen breit sein, und du wirst ihnen zu Recht aufhören zu vertrauen.

Es ist außerdem ein korrelatives Modell, keine Physiksimulation. Es lernt, was auf deiner Anlage üblicherweise passiert, sodass eine neuartige Schüttung, ein neuer Malzlieferant oder ein unbekanntes Maischeschema außerhalb seiner Erfahrung liegt und die Vorhersage wackeliger wird. Und wie jedes Ertragsmodell sagt es eine zentrale Erwartung voraus; ein einmaliges steckengebliebenes Abläutern wird es trotzdem überraschen. Kombiniere es mit der umfassenderen Sicht der [Sudhaus-Ertragsverlust-Analytik]({{ '/de/2023/brewhouse-yield-loss-analytics/' | relative_url }}), um Rezepteffekte von Anlagendrift zu trennen.

## Einen schwachen Sud in Klartext diagnostizieren
Der generative KI-Aspekt ist ein großes Sprachmodell, das das Chargenprotokoll eines ineffizienten Suds liest und es erklärt. Statt dem Brauer eine Zahl in die Hand zu geben, erzählt es die wahrscheinliche Ursache: „Dieser Sud kam 4 % unter dem Zielextrakt herein. Die Mühleneinstellung war unverändert, aber das Abläutern war 25 Minuten langsamer als dein Durchschnitt und das Läutervolumen 8 % zu niedrig — die wahrscheinlichsten Ursachen sind ein langsames oder teilweises Abläutern und Unterläuterung." Es verwandelt das Protokoll in eine Diagnose, auf die der Brauer reagieren kann, und es kann die Abweichungsnotiz für das Chargenprotokoll automatisch entwerfen.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Was das Maischen antreibt und was es nachgelagert verändert."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WAS ES ANTREIBT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Kann KI Sudhausausbeute und Extraktausbeute vorhersagen?</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Maischen</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Qualität</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Kosten / Risiko</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Was das Maischen antreibt und was es nachgelagert verändert.</figcaption>
</figure>

## Das Fazit
Ein Maischeeffizienz-Modell ist ein lohnendes Frühwarnwerkzeug, wenn dein Prozess stabil und deine Protokollierung ehrlich ist. Es markiert Sude, die auf einen Ertragsausfall zusteuern, rechtzeitig zum Reagieren und hilft, jene zu diagnostizieren, die ihn trotzdem verfehlen. Aber es kann eine driftende Mühle oder ein steckengebliebenes Läutern nicht überlisten — behebe zuerst Prozess und Protokollierung, dann lass das Modell schärfen, was bereits unter Kontrolle ist.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [Malzextrakt und diastatische Kraft vorhersagen]({{ '/de/2023/predicting-malt-extract-diastatic-power/' | relative_url }}).

## Häufig gestellte Fragen

**Was sagt ein Modell zur Maischeeffizienz vorher?**
Es sagt voraus, wie viel des Extraktpotenzials der Schüttung du tatsächlich in die Pfanne zurückgewinnst — aus Eingaben wie Schrot, Maischedicke, Temperatur- und Zeitprofil, Läutern und der Malzanalyse.

**Kann KI mir sagen, dass ein Sud den Ertrag verfehlt, bevor es passiert?**
Sie kann einen Sud aus Rezept- und Prozesseinstellungen als wahrscheinlich ertragsschwach markieren und dir die Chance geben, das Läutern anzupassen oder die Maische zu verlängern. Sie kann ein bereits steckengebliebenes Läutern nicht beheben.

**Was hindert ein Ertragsmodell am Funktionieren?**
Inkonsistenter Prozess und schlechte Protokollierung. Wenn dein Mühlenspalt und dein Läuterverhalten von Charge zu Charge driften und du Einstellungen nicht aufzeichnest, hat das Modell nichts Stabiles, woraus es lernen kann.
