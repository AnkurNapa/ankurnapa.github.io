---
layout: post
lang: de
title: "Promotion-Lift-Analyse in Tableau"
image: /assets/og/tableau-promotion-lift-analysis.png
description: "Baue eine Promotion-Lift-Analyse in Tableau mit Tabellenberechnungen, um Baseline gegen Ist-Volumen zu vergleichen, inkrementelle Marge zu messen und Promo-Zeiträume zu testen."
date: 2023-07-04
updated: 2023-07-04
permalink: /de/2023/tableau-promotion-lift-analysis/
tags: [commercial-planning, tableau, analytics]
faq:
  - q: "Wie misst man den Promotion-Lift in Tableau?"
    a: "Schätze eine Baseline der erwarteten Verkäufe ohne die Promotion und ziehe sie dann von den tatsächlichen Verkäufen während des Promo-Fensters ab, um das inkrementelle Volumen zu erhalten. Tabellenberechnungen erledigen den Periodenvergleich; die Baseline selbst ist der Teil, der Urteilsvermögen erfordert."
  - q: "Warum ist die Verkaufs-Baseline der schwierige Teil?"
    a: "Der Lift ist nur so gut wie das Gegenfaktum, gegen das du vergleichst. Eine Baseline aus einem gleitenden Durchschnitt, dem Vorjahr oder einer nicht beworbenen Kontrollgruppe ergibt jeweils einen anderen Lift, und keine ist nachweislich korrekt, also wählst und dokumentierst du die Methode."
  - q: "Kann Tableau beweisen, dass eine Promotion den Uplift verursacht hat?"
    a: "Nein. Es zeigt eine Korrelation zwischen dem Promo-Zeitraum und höheren Verkäufen, aber andere Faktoren — Wetter, ein Lieferengpass eines Wettbewerbers, Saisonalität — können dieselben Zahlen bewegen. Tableau quantifiziert den Zusammenhang; Kausalität braucht ein kontrolliertes Design."
---

**Kurze Antwort: Die Promotion-Lift-Analyse in Tableau ist nur so ehrlich wie die Baseline, gegen die du vergleichst, also bau die Baseline bewusst auf, miss inkrementelles Volumen und inkrementelle Marge mit Tabellenberechnungen und widerstehe der Versuchung, Korrelation eine Ursache zu nennen.** Das Diagramm ist leicht; das Gegenfaktum ist die Arbeit.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für die Promotion-Lift-Analyse in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Promotion-Lift-Analyse in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Kennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerlegen.</figcaption>
</figure>

## Zuerst messen: die Baseline definieren
Der Lift sind die tatsächlichen Verkäufe minus dem, was ohnehin passiert wäre. Alles hängt an diesem zweiten Term, der Baseline, und es gibt keinen einzigen richtigen Weg, sie aufzubauen. Ein gleitender Durchschnitt der Vor-Promo-Wochen ist einfach, ignoriert aber den Trend. Vorjahr-gleicher-Zeitraum respektiert die Saisonalität, setzt aber voraus, dass die Jahre vergleichbar sind. Ein abgestimmtes, nicht beworbenes Kontrollprodukt ist das sauberste Gegenfaktum, ist aber selten verfügbar. Wähle mit dem Vertriebsteam eine Methode, codiere sie als berechnetes Feld und kennzeichne sie im Dashboard, damit niemand eine Baseline aus gleitendem Durchschnitt mit der Grundwahrheit verwechselt.

Das ist das Messen-zuerst-Prinzip in seiner reinsten Form: Entscheide, wogegen du misst, bevor du die Balken zeichnest. Sobald das Baseline-Feld existiert, ist das inkrementelle Volumen einfach Ist minus Baseline innerhalb des Promo-Fensters, und die inkrementelle Marge wendet die Stückmarge auf dieses Inkrement an. Beide sind sauber, sobald die Baseline feststeht — und bedeutungslos davor.

## Die Lift-Ansicht bauen
Mit Baseline- und Inkrement-Feldern an Ort und Stelle tragen Tabellenberechnungen die Analyse. Nutze eine laufende Summe, um das kumulierte inkrementelle Volumen über den Promo-Zeitraum zu zeigen, und eine Prozentdifferenz-Tabellenberechnung, um den Lift als sauberen Prozentsatz gegenüber der Baseline auszudrücken. Ein Diagramm mit doppelter Achse, mit der Baseline als Referenzband und dem Ist als Balken, lässt die Lücke — den Lift — sofort ablesen.

Lege den Promotionszeitraum als Parameter offen, damit ein Analyst das Fenster verschieben und die Sensitivität testen kann: Hält der Lift, wenn du die erste Soft-Launch-Woche herausnimmst, oder verdampft er? Parameter verwandeln hier eine statische Nachbetrachtung in ein Werkzeug, um die Behauptung unter Druck zu setzen. Die inkrementelle-Marge-Ansicht zählt für Vertriebsführungskräfte am meisten, denn ein tiefer Rabatt kann zugleich riesiges Volumen und einen negativen Margen-Lift erzeugen.

Nutze dann Erläutern von Daten bei einer Promotion, die floppte. Wähle die enttäuschende Markierung, und Tableau schlägt vor, welche Dimensionen statistisch ungewöhnlich aussehen — vielleicht war der Lift in einer Region konzentriert, oder ein großes Kundenkonto trieb die ganze Zahl. Es ist ein schneller Weg, Hypothesen darüber zu erzeugen, warum eine Promo unterdurchschnittlich lief, die du dann prüfst. Derselbe diagnostische Instinkt trägt sich ins [Account-Churn-Dashboard]({{ '/de/2023/tableau-account-churn-dashboard/' | relative_url }}), wo ungewöhnliches Kontoverhalten das Signal ist, das du jagst.

## Wo es bricht
Drei ehrliche Grenzen. Erstens ist die Baseline eine Schätzung, keine Tatsache, sodass jede Lift-Zahl ihre Unsicherheit erbt — präsentiere eine Spanne oder die Methode, niemals eine falsch präzise Einzelzahl. Zweitens ist Korrelation keine Ursache. Eine Promotion, die sich mit einer Hitzewelle, dem Lieferengpass eines Wettbewerbers oder einem Saisonhoch überschneidet, zeigt einen aufgeblähten Lift, den die Promo nicht verdient hat. Tableau quantifiziert den Zusammenhang; nur ein kontrolliertes Design mit ordentlichen Holdout-Gruppen bringt dich nahe an Kausalität, und das lebt außerhalb des Dashboards.

Drittens ist da die Kannibalisierung. Eine Promotion auf einer SKU stiehlt oft Volumen von einem Schwesterprodukt oder zieht Verkäufe vor, die nächsten Monat passiert wären. Eine naive Lift-Ansicht zählt dieses gestohlene und geliehene Volumen als Gewinn. Bau eine Portfolioansicht, die beworbene Zugewinne gegen verwandte Rückgänge aufrechnet, und behandle den Einzel-SKU-Lift als optimistische Obergrenze, nicht als Wahrheit.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">BEITRAG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Promotion-Lift-Analyse in Tableau</text><text x="60" y="109" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal A</text><rect x="180" y="90" width="300" height="26" rx="4" fill="#b45309"/><text x="60" y="153" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal B</text><rect x="180" y="134" width="230" height="26" rx="4" fill="#b45309"/><text x="60" y="197" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal C</text><rect x="180" y="178" width="150" height="26" rx="4" fill="#b45309"/><text x="60" y="241" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal D</text><rect x="180" y="222" width="90" height="26" rx="4" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt.</figcaption>
</figure>

## Das Fazit
Entscheide und dokumentiere die Baseline vor allem anderen, miss inkrementelles Volumen und inkrementelle Marge mit Tabellenberechnungen und nutze einen Zeitraumparameter, um das Ergebnis unter Druck zu setzen. Lass „Erläutern von Daten" dir zeigen, wo du hinschauen sollst. Aber halte die Linie bei den Grenzen: Die Baseline ist eine Schätzung, die Beziehung ist Korrelation, kein Beweis, und Kannibalisierung kann einen Schlagzeilen-Gewinn leise in einen Portfolioverlust verwandeln.

*Teil des Tracks [Commercial-Planning-Analytics]({{ '/de/tracks/commercial-planning/' | relative_url }}).* Verwandt: [das Account-Churn-Dashboard]({{ '/de/2023/tableau-account-churn-dashboard/' | relative_url }}).

## Häufig gestellte Fragen

**Wie misst man den Promotion-Lift in Tableau?**
Schätze eine Baseline der erwarteten Verkäufe ohne die Promotion und ziehe sie dann von den tatsächlichen Verkäufen während des Promo-Fensters ab, um das inkrementelle Volumen zu erhalten. Tabellenberechnungen erledigen den Periodenvergleich; die Baseline selbst ist der Teil, der Urteilsvermögen erfordert.

**Warum ist die Verkaufs-Baseline der schwierige Teil?**
Der Lift ist nur so gut wie das Gegenfaktum, gegen das du vergleichst. Eine Baseline aus einem gleitenden Durchschnitt, dem Vorjahr oder einer nicht beworbenen Kontrollgruppe ergibt jeweils einen anderen Lift, und keine ist nachweislich korrekt, also wählst und dokumentierst du die Methode.

**Kann Tableau beweisen, dass eine Promotion den Uplift verursacht hat?**
Nein. Es zeigt eine Korrelation zwischen dem Promo-Zeitraum und höheren Verkäufen, aber andere Faktoren — Wetter, ein Lieferengpass eines Wettbewerbers, Saisonalität — können dieselben Zahlen bewegen. Tableau quantifiziert den Zusammenhang; Kausalität braucht ein kontrolliertes Design.
