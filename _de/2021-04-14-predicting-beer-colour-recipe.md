---
layout: post
lang: de
title: "Bierfarbe (EBC/SRM) aus einem Rezept vorhersagen"
image: /assets/og/predicting-beer-colour-recipe.png
description: "Wie KI die fertige Bierfarbe in EBC/SRM aus Malzfarben und Schüttungsanteilen vorhersagt, wo sie Moreys Gleichung schlägt und wo sie scheitert."
date: 2021-04-14
updated: 2021-04-14
permalink: /de/2021/predicting-beer-colour-recipe/
tags: [brewing-science, recipe, machine-learning]
faq:
  - q: "Kann man die Bierfarbe vorhersagen, bevor man braut?"
    a: "Ja, ziemlich gut. Ein Rezept liefert die Farbe und den Anteil jedes Malzes, und Modelle von Moreys Gleichung bis hin zu brauereispezifischem ML können das fertige EBC/SRM auf wenige Einheiten genau schätzen, noch bevor die Pfanne überhaupt angeheizt ist."
  - q: "Warum ist meine gemessene Farbe dunkler, als der Rechner vorhersagt?"
    a: "Karamellisierung in der Pfanne und Maillard-Reaktionen während eines langen, kräftigen Kochens fügen Farbe hinzu, die einfache lineare Formeln ignorieren. Kochintensität, Stammwürze und pH-Wert schieben den gemessenen Wert allesamt über die Rezeptschätzung hinaus."
  - q: "Bedeutet dunkleres Bier mehr Geschmack?"
    a: "Nein. Farbe und Geschmack korrelieren über die Malzwahl, sind aber nicht identisch. Ein Modell, das das EBC genau trifft, sagt nichts über Bittere, Körper oder Fehlaromen aus, daher ist Farbe ein Ausgangspunkt, kein Urteil."
---

**Kurze Antwort: Ja, man kann die fertige Bierfarbe aus einem Rezept erstaunlich gut vorhersagen, und brauereispezifisches Machine Learning schlägt die Lehrbuchgleichungen.** Farbe ist eines der am besten messbaren Dinge beim Brauen, was sie zu einem idealen ersten Ziel für einen datengetriebenen Ansatz macht.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Bierfarbe (EBC/SRM) aus einem Rezept vorhersagen</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Maischen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Gären</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Abfüllen</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende.</figcaption>
</figure>

## Was die Farbe im Glas tatsächlich bestimmt
Bierfarbe wird in EBC (Europa) oder SRM (USA) gemessen und wird hauptsächlich vom Malz bestimmt: dem Lovibond- oder EBC-Wert jedes Getreides, dem Anteil jedes einzelnen in der Schüttung und der Farbe, die sich durch Maillard- und Karamellisierungsreaktionen während des Kochens entwickelt. Ein helles Pilsner Malz in hohem Anteil hält das Ganze strohfarben; wenige Prozent Röst- oder Karamellmalz verändern das Ergebnis dramatisch, weil dunkle Malze nichtlineare Beiträge liefern.

Der klassische Ausgangspunkt ist Moreys Gleichung, die das SRM aus den Malzfarbeinheiten je Volumeneinheit über eine Potenzgesetz-Anpassung schätzt. Sie ist schnell, transparent und für die Hobbybrau-Planung gut genug. Aber sie wurde an einen generischen Datensatz angepasst, nicht an deine Pfanne, dein Wasser oder dein Kochregime, daher liegt sie für jede konkrete Brauerei systematisch daneben.

## Erst messen, dann das Modell deine Pfanne lernen lassen
Der ehrliche Weg, Morey zu verbessern, besteht darin, zuerst zu messen. Protokolliere die Rezepteingaben (Farbe und Gewicht jedes Malzes, Maisch- und Kochparameter) gegen das gemessene EBC/SRM des fertigen Biers für jeden Sud, den du kannst. Sobald du ein paar Dutzend gepaarte Beobachtungen hast, lernt selbst ein bescheidenes Regressionsmodell den systematischen Versatz, den dein Prozess einführt.

Hier verdient sich Machine Learning seinen Platz. Ein Gradient-Boosting-Modell oder ein kleines neuronales Netz kann den nichtlinearen Beitrag dunkler Malze und das Zusammenspiel zwischen Kochdauer und Stammwürze weit besser erfassen als ein einzelnes Potenzgesetz. Das Modell ist keine Zauberei; es ist schlicht an *deine* Daten angepasst statt an einen generischen Durchschnitt, daher korrigiert es die konsistente Verzerrung, die deine Ausrüstung einführt. In der Praxis halbiert ein brauereispezifisches Modell oft den Vorhersagefehler einer generischen Formel und macht aus einer „grob richtigen" Schätzung etwas, um das herum man eine Schüttung planen kann.

Die datenwissenschaftliche Disziplin zählt mehr als der Algorithmus. Saubere Farbmessungen aus einem kalibrierten Spektralfotometer, konsistente Probenahme und ehrliche Protokollierung von Prozessabweichungen schlagen jedes raffinierte Modell, das auf schlampigen Daten trainiert wurde.

## Ein Generative-KI-Copilot, um eine Zielfarbe zu treffen
Die interessante kurzfristige Anwendung ist generativ, nicht nur prädiktiv. Statt zu fragen „welche Farbe ergibt diese Schüttung?", stellst du die Umkehrfrage: „Ich möchte 25 EBC für ein Wiener Lager, schlag mir Schüttungsanpassungen vor." Ein Copilot, der auf deinem angepassten Farbmodell aufbaut, kann den Rezeptraum durchsuchen, zwei oder drei Schüttungsanpassungen vorschlagen, die das Ziel treffen, und die Zielkonflikte erklären (mehr Karamellmalz für die Farbe gegenüber der Süße, die es hinzufügt). Es verwandelt das Modell in einen Design-Assistenten, mit dem ein Brauer tatsächlich ins Gespräch kommen kann, während der Brauer das letzte Urteil behält.

## Wo es scheitert
Farbvorhersage ist eines der freundlicheren Probleme beim Brauen, hat aber harte Grenzen. Karamellisierung in der Pfanne hängt von Kochintensität, Oberfläche und Stammwürze auf eine Weise ab, die von Sud zu Sud variiert, daher setzt Prozessvariation der Genauigkeit eine Untergrenze. Wasserchemie und Maische-pH verschieben die Extraktion und den endgültigen Farbton. Das Malz selbst variiert je Ernte und Mälzerei-Charge, daher ist der Farbwert auf dem Sack eine Nominalangabe, keine Garantie.

Am wichtigsten: Farbe ist nicht Geschmack. Ein Modell kann dein Ziel-EBC perfekt treffen und dir nichts darüber sagen, ob das Bier so schmeckt, wie du es beabsichtigt hast. Behandle Farbvorhersage als Planungswerkzeug, das Probesude spart, nicht als Qualitätsurteil. Die Referenz für „schmeckt es richtig" bleibt ein kalibriertes Sensorikpanel, keine Zahl.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">REGELKREIS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Bierfarbe (EBC/SRM) aus einem Rezept vorhersagen</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Regler</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Aktor</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Prozess</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">Rückführung</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen.</figcaption>
</figure>

## Das Fazit
Bierfarbe ist vorhersagbar, und ein brauereispezifisches Modell, das auf deinen eigenen gemessenen Suden trainiert ist, schlägt generische Gleichungen wie die von Morey, indem es die systematische Verzerrung deiner Pfanne korrigiert. Erst messen, die Daten sauber halten und einen generativen Copilot nutzen, um Schüttungsanpassungen in Richtung eines Ziels vorzuschlagen. Denk nur daran: Das Modell sagt eine Farbe voraus, kein Bier.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [Kann KI ein Bierrezept entwerfen?]({{ '/de/2026/can-ai-design-a-beer-recipe/' | relative_url }})

## Häufig gestellte Fragen

**Kann man die Bierfarbe vorhersagen, bevor man braut?**
Ja, ziemlich gut. Ein Rezept liefert die Farbe und den Anteil jedes Malzes, und Modelle von Moreys Gleichung bis hin zu brauereispezifischem ML können das fertige EBC/SRM auf wenige Einheiten genau schätzen, noch bevor die Pfanne überhaupt angeheizt ist.

**Warum ist meine gemessene Farbe dunkler, als der Rechner vorhersagt?**
Karamellisierung in der Pfanne und Maillard-Reaktionen während eines langen, kräftigen Kochens fügen Farbe hinzu, die einfache lineare Formeln ignorieren. Kochintensität, Stammwürze und pH-Wert schieben den gemessenen Wert allesamt über die Rezeptschätzung hinaus.

**Bedeutet dunkleres Bier mehr Geschmack?**
Nein. Farbe und Geschmack korrelieren über die Malzwahl, sind aber nicht identisch. Ein Modell, das das EBC genau trifft, sagt nichts über Bittere, Körper oder Fehlaromen aus, daher ist Farbe ein Ausgangspunkt, kein Urteil.
