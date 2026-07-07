---
layout: post
lang: de
title: "Mykotoxin- und Gushing-Risiko in der Mälzerei prognostizieren"
image: /assets/og/forecasting-mycotoxin-gushing-risk-malting.png
description: "Mit Fusarium befallene Gerste bringt DON-Mykotoxin und Gushing-Risiko. Wie maschinelles Lernen eingehende Partien aus Erntewetter und Korndaten bewertet — und warum eine Lebensmittelsicherheits-Entscheidung einen Menschen im Kreislauf hält."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
permalink: /de/2026/forecasting-mycotoxin-gushing-risk-malting/
tags: [brewing-science, malting, food-safety, machine-learning]
faq:
  - q: "Was ist Gushing bei Bier?"
    a: "Gushing ist das spontane Überschäumen von Bier in dem Moment, in dem eine Verpackung geöffnet wird, ohne offensichtliches Schütteln oder Fehler. Primäres Gushing wird durch Hydrophobin-Proteine aus Fusarium-Schimmel auf der Gerste angetrieben, die winzige Kohlendioxidbläschen stabilisieren; es geht auf eine Feldinfektion zurück, nicht auf die Brauerei."
  - q: "Was ist DON und warum ist es beim Mälzen wichtig?"
    a: "DON (Deoxynivalenol) ist ein Mykotoxin, das von Fusarium-Pilzen auf Getreide produziert wird. Es ist eine Lebensmittelsicherheits-Gefahr mit regulatorischen Grenzwerten, es überlebt das Mälzen und Brauen weitgehend, und dieselbe Feldinfektion, die DON erhöht, erhöht oft auch das Gushing-Risiko — daher wird es beim Gersteneingang geprüft."
  - q: "Kann KI das Mykotoxin- oder Gushing-Risiko vorhersagen?"
    a: "Sie kann das Risiko einordnen. Ein Modell, das Erntewetter während der Blüte, Region, Sortenanfälligkeit und Korninspektions- oder Nahinfrarotdaten nutzt, markiert Hochrisiko-Partien zum Testen oder Ablehnen. Es ist ein Triage-Werkzeug, kein Ersatz für den DON-Assay, denn die Kontamination ist fleckig und die Kosten eines Fehlers sind hoch."
---

**Kurze Antwort: Man kann das *Risiko* prognostizieren, nicht das *Ergebnis*. Eine Fusarium-Infektion auf dem Feld produziert sowohl DON-Mykotoxin als auch die Hydrophobine, die Bier zum Gushing bringen, daher kann ein Modell, das mit Erntewetter, Region, Sortenanfälligkeit und Korninspektionsdaten gefüttert wird, eingehende Gerstenpartien von niedrigem bis hohem Risiko einordnen und sie zum Testen, Separieren oder Ablehnen leiten. Diese Triage ist wirklich nützlich — sie konzentriert teure Assays dorthin, wo sie zählen. Aber die Kontamination ist fleckig und die Kosten einer übersehenen Partie sind ein Lebensmittelsicherheits-Rückruf, also screent das Modell; das Labor und ein Mensch entscheiden.**

DON und Gushing sind die zwei Mälzerei-Probleme, die beginnen, bevor die Gerste überhaupt eintrifft: Beide werden Monate früher in einem warmen, feuchten Blütenfenster gesät. Beim Eingang ist der Schaden angerichtet und ungleichmäßig über die Partie verteilt, was sie zugleich zu einem Prognoseproblem und einem Beprobungs-Albtraum macht.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 250" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Eingehende Gerstenpartien, von einem Risikomodell bewertet und zu annehmen, separieren und testen oder ablehnen geleitet">
<rect x="0" y="0" width="760" height="250" fill="#ffffff"/>
<text x="380" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#06483f">Eingangs-Triage — bewerten, dann leiten</text>
<rect x="40" y="95" width="150" height="60" rx="6" fill="#f0f6f5" stroke="#4a6b64"/>
<text x="115" y="120" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">eingehende Partie</text>
<text x="115" y="138" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#4a6b64">Wetter · Sorte · NIR</text>
<rect x="270" y="95" width="150" height="60" rx="6" fill="#00695c"/>
<text x="345" y="122" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#ffffff">Risikowert</text>
<text x="345" y="140" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#ffffff">niedrig · mittel · hoch</text>
<line x1="190" y1="125" x2="262" y2="125" stroke="#4a6b64" stroke-width="2"/>
<polygon points="270,125 260,120 260,130" fill="#4a6b64"/>
<g>
<rect x="500" y="50" width="220" height="40" rx="6" fill="#2e9e7c" fill-opacity="0.15" stroke="#2e9e7c"/>
<text x="610" y="75" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">annehmen</text>
<rect x="500" y="105" width="220" height="40" rx="6" fill="#00695c" fill-opacity="0.15" stroke="#00695c"/>
<text x="610" y="130" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">separieren &amp; DON assayieren</text>
<rect x="500" y="160" width="220" height="40" rx="6" fill="#06483f" fill-opacity="0.15" stroke="#06483f"/>
<text x="610" y="185" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#06483f">ablehnen / umleiten</text>
</g>
<line x1="420" y1="120" x2="500" y2="72" stroke="#4a6b64" stroke-width="1.5"/>
<line x1="420" y1="125" x2="500" y2="125" stroke="#4a6b64" stroke-width="1.5"/>
<line x1="420" y1="130" x2="500" y2="178" stroke="#4a6b64" stroke-width="1.5"/>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Das Modell besteht oder verwirft keine Partie; es sortiert Partien, damit der Labor-Assay und die menschliche Entscheidung dort landen, wo das Risiko am höchsten ist.</figcaption>
</figure>

## Woher Gushing und DON kommen

Beide gehen auf die *Fusarium*-Ährenfäule zurück, eine Pilzinfektion der Getreideähre, die durch warmes, feuchtes Wetter während der Blüte begünstigt wird. Der Pilz produziert **Deoxynivalenol (DON)**, ein Mykotoxin, das eine regulierte Lebensmittelsicherheits-Gefahr ist und das Mälzen und Brauen weitgehend bis ins fertige Bier überlebt. Dieselbe Infektion lagert **Hydrophobine** ab — kleine grenzflächenaktive Proteine, die sich an Kohlendioxidbläschen heften und sie stabilisieren, sodass das Bier ausbricht, wenn die Verpackung geöffnet wird (primäres Gushing). Entscheidend: Das ist ein *Feld*-Problem, kein Brauerei-Problem: Bis die Gerste die Mälzerei erreicht, managst du geerbtes Risiko und entscheidest, welchen Partien du traust.

## Ein Risikowert beim Eingang

Das Modell ist eine klassische Risiko-Ranking-Aufgabe. Merkmale, die wirklich Signal tragen: Wetter während des Blütenfensters der Ernte (Niederschlag, Luftfeuchtigkeit, Temperatur), Anbauregion und Feldhistorie, Sortenanfälligkeit sowie Korninspektions- oder Nahinfrarot (NIR)-Werte beim Eingang, die auf Pilzschäden hindeuten. Trainiere auf vergangenen Partien, beschriftet mit ihrem gemessenen DON und etwaigen Gushing-Vorfällen, und das Modell gibt einen Risikograd je Lieferung aus. Du handelst dann auf den Grad hin: nimm die Niedrigrisiko-Partien an, separiere und assayiere die mittleren, leite die Hochrisiko-Partien zu einer Nicht-Lebensmittelnutzung oder zurück zum Lieferanten. Der Punkt ist nicht, den DON-Test zu überspringen — sondern ihn zu zielen.

## Die Daten und eine generative Berichtsschicht

Das steht und fällt mit Datendisziplin: jede Lieferung an ihren agronomischen Ursprung, ihren NIR-Scan und letztlich ihr Labor-DON-Ergebnis zu binden, damit das Modell weiterlernt. Eine generative KI-Schicht erledigt dann die unglamouröse, aber reale Arbeit der Lebensmittelsicherheits-Dokumentation — den HACCP-Vermerk für eine separierte Partie entwerfen, „Warum wurde Partie 88 markiert?" gegen Wetter und Region für das Lieferantengespräch zusammenfassen und einem Qualitätsmanager erlauben, das Eingangsrisiko der Saison in einfacher Sprache abzufragen. Sie ergänzt die bestehende [Lebensmittelsicherheits-Rückverfolgbarkeit vom Korn ins Glas]({{ '/de/2025/food-safety-traceability-grain-to-glass/' | relative_url }}), statt den Assay oder den Auditor zu ersetzen.

## Wo ein Fehler teuer ist

Das ist der Beitrag, in dem „wo es bricht" am meisten zählt, denn der Fehlermodus ist ein Sicherheitsversagen. **Kontamination ist heterogen** — DON konzentriert sich in Nestern, sodass eine Partie eine Probe bestehen und dennoch einen Hotspot tragen kann, und ein auf Partiendurchschnitts-Labels trainiertes Modell kann nicht auflösen, was die Beprobung selbst übersehen hat. **Gushing ist multifaktoriell**: Hydrophobine sind die primäre Hauptursache, aber Karbonisierung, Metallionen, Calciumoxalat und Verpackung tragen alle bei, sodass ein sauberer Gersten-Risikowert keine ruhige Verpackung garantiert. Und die Asymmetrie ist brutal — ein falsch-negatives Ergebnis, das eine Hoch-DON-Partie durchlässt, ist weit kostspieliger als ein falsch-positives, das einen Assay verschwendet, also muss das Modell so eingestellt werden, dass es zu viel überweist, und ein Mensch muss die Freigabeentscheidung verantworten. Behandle den Wert als Grund zu testen, nie als Grund, es nicht zu tun.

## Das Fazit

KI verdient ihren Platz in der Mälzerei als Triage-Werkzeug für geerbtes Risiko: Sie ordnet eingehende Gerste nach DON- und Gushing-Potenzial ein und richtet dein Testen dorthin, wo es zählt. Sie gibt keine Partie frei — heterogene Kontamination und multifaktorielles Gushing machen das zur Aufgabe des Labors und des Qualitätsmanagers. Halte den Assay im Kreislauf, gewichte das Modell zur Vorsicht, und lass es deine Beprobung klüger machen, nicht deine Sicherheit dünner.

## Häufig gestellte Fragen

**Was ist Gushing bei Bier?**
Gushing ist das spontane Überschäumen von Bier in dem Moment, in dem eine Verpackung geöffnet wird, ohne offensichtliches Schütteln oder Fehler. Primäres Gushing wird durch Hydrophobin-Proteine aus Fusarium-Schimmel auf der Gerste angetrieben, die winzige Kohlendioxidbläschen stabilisieren; es geht auf eine Feldinfektion zurück, nicht auf die Brauerei.

**Was ist DON und warum ist es beim Mälzen wichtig?**
DON (Deoxynivalenol) ist ein Mykotoxin, das von Fusarium-Pilzen auf Getreide produziert wird. Es ist eine Lebensmittelsicherheits-Gefahr mit regulatorischen Grenzwerten, es überlebt das Mälzen und Brauen weitgehend, und dieselbe Feldinfektion, die DON erhöht, erhöht oft auch das Gushing-Risiko — daher wird es beim Gersteneingang geprüft.

**Kann KI das Mykotoxin- oder Gushing-Risiko vorhersagen?**
Sie kann das Risiko einordnen. Ein Modell, das Erntewetter während der Blüte, Region, Sortenanfälligkeit und Korninspektions- oder Nahinfrarotdaten nutzt, markiert Hochrisiko-Partien zum Testen oder Ablehnen. Es ist ein Triage-Werkzeug, kein Ersatz für den DON-Assay, denn die Kontamination ist fleckig und die Kosten eines Fehlers sind hoch.

*Teil des [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }})-Tracks.*
