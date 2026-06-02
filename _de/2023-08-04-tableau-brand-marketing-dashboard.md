---
layout: post
lang: de
title: "Ein Marken- und Marketing-Performance-Dashboard in Tableau"
image: /assets/og/tableau-brand-marketing-dashboard.png
description: "Mische Werbeausgaben, Verkäufe und Social in Tableau, um ein Marken- und Marketing-Dashboard mit Kanal-ROI, Funnel-Ansichten und einer ehrlichen Sicht auf Attribution zu bauen."
date: 2023-08-04
updated: 2023-08-04
permalink: /de/2023/tableau-brand-marketing-dashboard/
tags: [marketing, tableau, analytics]
faq:
  - q: "Wie kombiniere ich Werbeausgaben- und Verkaufsdaten in Tableau?"
    a: "Nutze eine Datenmischung oder einen Join über eine gemeinsame Dimension wie Datum und Kanal. Eine Mischung hält die Quellen getrennt und ist sicherer, wenn die Granularitäten abweichen; ein Join ist sauberer, wenn beide auf derselben Granularität liegen."
  - q: "Kann Tableau beweisen, welcher Kanal einen Verkauf ausgelöst hat?"
    a: "Kein Werkzeug kann aus rein beobachtenden Daten eine Single-Touch-Kausalität beweisen. Tableau zeigt Korrelation über ein Attributionsfenster; echte Kausalität braucht Experimente wie Geo-Holdouts oder Media-Mix-Modellierung."
  - q: "Wofür ist der Attributionsfenster-Parameter?"
    a: "Er erlaubt dir, einen Verkauf der Marketingaktivität innerhalb eines gewählten Rückblickzeitraums zuzuschreiben, etwa 7, 14 oder 30 Tage, damit du testen kannst, wie empfindlich deine ROI-Zahlen auf diese Annahme reagieren."
---

**Kurze Antwort: Ein Marken-Dashboard ist nur so ehrlich wie seine Attributionsannahmen, also mache diese Annahmen zu einem sichtbaren, anpassbaren Parameter.** Die Aufgabe des Dashboards ist es, Ausgaben mit Ergebnissen zu verbinden, ohne vorzutäuschen, die Verbindung sei sauberer, als sie ist.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für Ein Marken- und Marketing-Performance-Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Ein Marken- und Marketing-Performance-Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Kennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerschneiden.</figcaption>
</figure>

## Beginne bei der Entscheidung, nicht beim Datenfeed
Marketing-Dashboards verrotten, wenn sie zu einer Wand aus jeder Kennzahl werden, die jede Plattform bietet. Beginne mit der Entscheidung, die das Dashboard stützt: wohin das nächste Pfund Budget verschoben werden soll. Das erzwingt eine Kennzahlenhierarchie, Umsatz und Deckungsbeitrag ganz oben, Kanal-ROI in der Mitte und Engagement-Kennzahlen (Reichweite, Klicks, Social Sentiment) als unterstützender Kontext, nicht als Schlagzeilen-KPIs. Impressions sind ein Input; verkaufte Kisten sind das Ergebnis. Lässt du eine Eitelkeitskennzahl wie Gesamt-Impressions oben links sitzen, optimierst du auf sie.

## Bau es: Mischungen, ein Funnel und eine Kanal-ROI-Ansicht
Der technische Kern ist multi-source. Werbeausgaben liegen in einem Extrakt, der Abverkauf in einem anderen, Social in einem dritten. Mische sie über gemeinsame Dimensionen, meist Datum und Kanal, wenn die Granularitäten abweichen, und reserviere Joins für Quellen, die bereits auf einer gemeinsamen Granularität liegen. Tableau Prep ist hier die Mühe wert, um Kanalbenennungen zu bereinigen, bevor sie die Arbeitsmappe erreichen; inkonsistente „FB"- gegen „Facebook"-Bezeichnungen brechen leise jede nachgelagerte Mischung.

Modelliere den Funnel als eine Reihe berechneter Felder, Awareness zu Consideration zu Trial zu Repeat, und zeige Konversionsraten zwischen den Stufen statt Rohzählungen, damit Stufen sehr unterschiedlicher Größe vergleichbar bleiben. Kanal-ROI ist ein berechnetes Feld, zugeordneter Umsatz geteilt durch Ausgaben, und hier verdient sich der Attributionsfenster-Parameter seinen Wert. Verdrahte einen Parameter (7 / 14 / 30 Tage) in die Berechnung, die einem Verkauf vorausgegangene Aktivität zuschreibt, und lass Nutzer dann zusehen, wie sich die ROI-Rangfolgen umsortieren, sobald sich das Fenster ändert. Diese eine Interaktion lehrt mehr Demut gegenüber Attribution als jede Fußnote.

Wenn ein Kanal ausschlägt, führe Explain Data auf der Markierung aus. Einstein Copilot bringt Treiberkandidaten zum Vorschein, eine live gegangene Kampagne, eine überperformende Region, was eine nützliche Ausgangshypothese ist. Tableau Pulse kann dann den Kanal-ROI überwachen und dem CMO eine klarsprachliche Zusammenfassung senden, die bedeutsame Bewegungen markiert, ohne dass jemand die Arbeitsmappe öffnet.

## Wo es bricht: Attribution und die Kausalitätsfalle
Das ist das Dashboard, das am ehesten in die Irre führt, also benenne die Grenzen klar. Last-Touch- und fensterbasierte Attribution sind Konventionen, keine Wahrheit; sie überkreditieren, was am nächsten zum Kauf zündet (oft Marken-Suche) und unterkreditieren den oberen Funnel-Markenaufbau, der sich Wochen früher auszahlte. Korrelation ist nicht Ursache: Ein Kanal kann effizient aussehen, einfach weil er Menschen anspricht, die ohnehin gekauft hätten. Die ehrliche Antwort auf „was funktioniert" kommt aus Experimenten, Geo-Holdouts, Inkrementalitätstests, Media-Mix-Modellierung über TabPy, nicht aus einem Dashboard allein.

Generative KI verschärft sowohl den Vorteil als auch die Gefahr. Eine Pulse-Zusammenfassung, die sagt „Social trieb den Anstieg", ist flüssig und selbstsicher, und eine vielbeschäftigte Führungskraft nimmt sie für bare Münze. Aber das Modell fasst Korrelationen innerhalb deines gewählten Fensters zusammen; es kennt deine Holdout-Ergebnisse nicht. Halte den Menschen in der Schleife und kennzeichne die Attributionsannahme auf dem Dashboard selbst, damit die Lesart „ROI bei einem 14-Tage-Fenster" ist, niemals nur „ROI".

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">BEITRAG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Ein Marken- und Marketing-Performance-Dashboard in Tableau</text><text x="60" y="109" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal A</text><rect x="180" y="90" width="300" height="26" rx="4" fill="#b45309"/><text x="60" y="153" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal B</text><rect x="180" y="134" width="230" height="26" rx="4" fill="#b45309"/><text x="60" y="197" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal C</text><rect x="180" y="178" width="150" height="26" rx="4" fill="#b45309"/><text x="60" y="241" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal D</text><rect x="180" y="222" width="90" height="26" rx="4" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt.</figcaption>
</figure>

## Das Fazit
Baue das Marken-Dashboard um die Budgetentscheidung herum, mische die Quellen sauber und mache Attribution zu einer anpassbaren, sichtbaren Annahme statt einer versteckten. Nutze Explain Data und Pulse, um die Lesart zu beschleunigen, und behandle ihre Narrative dann als zu prüfende Hypothesen, nicht als Urteile. Das Dashboard gewinnt, wenn es alle ein wenig skeptischer gegenüber einfachen Attributionsbehauptungen macht.

*Teil des Tracks [Marketing]({{ '/de/tracks/marketing/' | relative_url }}).* Verwandt: die [Risiken KI-generierter Markeninhalte]({{ '/de/2026/ai-generated-brand-content-risks/' | relative_url }}).

## Häufig gestellte Fragen

**Wie kombiniere ich Werbeausgaben- und Verkaufsdaten in Tableau?**
Nutze eine Datenmischung oder einen Join über eine gemeinsame Dimension wie Datum und Kanal. Eine Mischung hält die Quellen getrennt und ist sicherer, wenn die Granularitäten abweichen; ein Join ist sauberer, wenn beide auf derselben Granularität liegen.

**Kann Tableau beweisen, welcher Kanal einen Verkauf ausgelöst hat?**
Kein Werkzeug kann aus rein beobachtenden Daten eine Single-Touch-Kausalität beweisen. Tableau zeigt Korrelation über ein Attributionsfenster; echte Kausalität braucht Experimente wie Geo-Holdouts oder Media-Mix-Modellierung.

**Wofür ist der Attributionsfenster-Parameter?**
Er erlaubt dir, einen Verkauf der Marketingaktivität innerhalb eines gewählten Rückblickzeitraums zuzuschreiben, etwa 7, 14 oder 30 Tage, damit du testen kannst, wie empfindlich deine ROI-Zahlen auf diese Annahme reagieren.
