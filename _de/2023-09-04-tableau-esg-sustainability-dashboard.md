---
layout: post
lang: de
title: "Ein ESG-Nachhaltigkeits-Dashboard in Tableau (Wasser, Energie, CO₂ pro hl)"
image: /assets/og/tableau-esg-sustainability-dashboard.png
description: "Baue ein ESG-Dashboard in Tableau, das Wasser-zu-Bier-Verhältnis, Energie pro hl und CO₂ nach Scope gegen Ziele verfolgt, mit Pulse-Überblicken und ehrlichen Datenvorbehalten."
date: 2023-09-04
updated: 2023-09-04
permalink: /de/2023/tableau-esg-sustainability-dashboard/
tags: [esg, tableau, sustainability]
faq:
  - q: "Was sind die zentralen ESG-Kennzahlen für ein Brauerei-Dashboard?"
    a: "Wasser-zu-Bier-Verhältnis (hl Wasser pro hl Bier), Energieintensität (kWh oder MJ pro hl) und CO₂-Emissionen nach Scope (1, 2 und idealerweise 3) pro hl. Die Normalisierung pro hl macht Standorte unterschiedlicher Größe vergleichbar."
  - q: "Wie berechne ich CO₂-Emissionen in Tableau?"
    a: "Multipliziere Aktivitätsdaten, etwa Gas- oder Stromverbrauch, mit einem Emissionsfaktor in einem berechneten Feld. Die Zahl ist nur so gut wie der Faktor, speichere Faktoren daher als gepflegte Referenztabelle, nicht als fest codierte Konstanten."
  - q: "Kann ein Dashboard Greenwashing verhindern?"
    a: "Es kann helfen, indem es Bilanzgrenzen, Faktoren und Annahmen explizit macht, aber es kann selektive Berichterstattung nicht verhindern. Greenwashing ist ein Governance-Problem; die Rolle des Dashboards ist es, das Gesamtbild ehrlich zu zeigen, einschließlich der schlechten Trends."
---

**Kurze Antwort: Ein ESG-Dashboard steht und fällt mit Datenqualität und klar benannten Bilanzgrenzen, nicht mit der Cleverness des Diagramms.** Das Schwierige ist nicht, Wasser, Energie und CO₂ zu visualisieren; es ist, den Zahlen zu vertrauen, die du einspeist.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für Ein ESG-Nachhaltigkeits-Dashboard in Tableau (Wasser, Energie, CO₂ pro hl)"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Ein ESG-Nachhaltigkeits-Dashboard in Tableau (Wasser, Energie, CO₂ pro hl)</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Kennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerschneiden.</figcaption>
</figure>

## Wähle zuerst die Intensitätskennzahlen
Nachhaltigkeitsdaten lassen sich leicht durch den Wechsel zwischen absoluten und Intensitätsansichten manipulieren, also entscheide vorab. Für eine Brauerei erledigen drei normalisierte Kennzahlen den Großteil der Arbeit: Wasser-zu-Bier-Verhältnis (hl Wasser pro hl Bier), Energieintensität (kWh oder MJ pro hl) und CO₂ pro hl aufgeteilt nach Scope. Die Normalisierung pro hl ist die Data-Science-Disziplin, die einen kleinen Craft-Standort und ein großes regionales Werk fair auf dasselbe Diagramm bringt. Zeige auch absolute Summen, denn eine fallende Intensität bei steigendem Volumen kann dennoch steigende Gesamtemissionen bedeuten, aber führe mit der Intensität für operative Rechenschaft.

## Bau es: berechnete Felder, Ziele und Standortvergleich
Jede Kennzahl ist ein berechnetes Feld. Das Wasserverhältnis ist das gesamte Wasservolumen geteilt durch das gesamte Produktionsvolumen. CO₂ ist das interessante: Aktivitätsdaten mal einem Emissionsfaktor. Widersteh dem fest codierten Eintragen von Faktoren in die Berechnung, sie ändern sich jährlich und variieren regional, verknüpfe daher eine gepflegte Emissionsfaktor-Referenztabelle und berechne:

`SUM([Gas kWh]) * [Gas Emission Factor] + SUM([Electricity kWh]) * [Grid Factor]`

Halte die Scopes getrennt. Scope 1 (direkte Verbrennung), Scope 2 (zugekaufter Strom) und Scope 3 (alles vor- und nachgelagert, Verpackung, Distribution, Landwirtschaft) verhalten sich unterschiedlich und haben sehr unterschiedliche Datensicherheit. Zeige sie als gestapelte Ansichten oder Small Multiples, damit niemand einen ordentlichen Scope-1-Trend als die gesamte CO₂-Geschichte liest.

Trage jede Kennzahl gegen das Ziel auf. Eine Bezugslinie für das Jahresziel plus eine farbcodierte Abweichung verwandelt das Dashboard in ein Führungswerkzeug statt eine Aufzeichnung. Für den Standortvergleich lässt ein Small-Multiples-Layout oder ein gerankter Balken den Betriebsleiter sehen, welches Werk den Durchschnitt nach unten zieht. Tableau Prep bewältigt die unordentliche Realität monatlicher Zählerstände, die in unterschiedlichen Einheiten und Zeitstempeln ankommen. Richte schließlich Tableau Pulse auf die wichtigsten Intensitätskennzahlen, sodass das Nachhaltigkeitsteam einen monatlichen natürlichsprachlichen Überblick erhält, nützlich beim Befüllen von Vorstands- und regulatorischen Berichtszyklen.

## Wo es bricht: Bilanzgrenzen, Faktoren und Greenwashing
Hier täuschen ESG-Dashboards leise. Drei Fehlerarten kehren wieder. Erstens Bilanzgrenzen: Wenn Standort A das eingehende Wasser am Hausanschluss misst und Standort B es nach der Aufbereitung misst, ist dein Vergleich Unsinn, und das Diagramm warnt dich nicht. Zweitens Emissionsfaktoren: Besonders Scope 3 stützt sich auf Schätzungen und Branchendurchschnitte, sodass eine selbstsichere CO₂-pro-hl-Zahl einen weiten, unsichtbaren Fehlerbalken tragen kann. Drittens das Greenwashing-Risiko: Ein Dashboard macht es trivial einfach, die schmeichelhafte Kennzahl hervorzuheben und die steigende zu verstecken. Die Gegenmaßnahme ist Transparenz auf der Leinwand selbst, ergänze die Bilanzgrenze in einer Fußnote, nenne die Faktorquelle und verstecke nie einen sich verschlechternden Trend hinter einem Tab, den niemand öffnet.

Generative KI fügt eine subtilere Gefahr hinzu. Ein Pulse-Überblick, der „CO₂-Intensität um 8 % verbessert" erzählt, liest sich als saubere Tatsache, aber er kann nicht sehen, dass die Hälfte der Verbesserung von einer Methodenänderung bei deinen Emissionsfaktoren kam. Halte einen Menschen, idealerweise mit Hintergrund in Nachhaltigkeitsberichterstattung, zwischen die KI-Erzählung und jede externe Offenlegung.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Emissionen aufgeteilt nach Scope — der größte Teil des Fußabdrucks verbirgt sich meist in Scope 3."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">FUSSABDRUCK NACH SCOPE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Ein ESG-Nachhaltigkeits-Dashboard in Tableau (Wasser, Energie, CO₂ pro hl)</text><rect x="300" y="80" width="120" height="40" fill="#5b7a1f"/><rect x="300" y="120" width="120" height="40" fill="#b45309"/><rect x="300" y="160" width="120" height="90" fill="#7a1f3d"/><rect x="460" y="84" width="14" height="14" fill="#5b7a1f"/><text x="482" y="96" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Scope 1 — direkt</text><rect x="460" y="124" width="14" height="14" fill="#b45309"/><text x="482" y="136" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Scope 2 — Energie</text><rect x="460" y="184" width="14" height="14" fill="#7a1f3d"/><text x="482" y="196" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Scope 3 — Wertschöpfungskette (größter)</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Emissionen aufgeteilt nach Scope — der größte Teil des Fußabdrucks verbirgt sich meist in Scope 3.</figcaption>
</figure>

## Das Fazit
Bau das ESG-Dashboard auf normalisierten Intensitätskennzahlen, trenne die CO₂-Scopes und behandle Emissionsfaktoren als gepflegte Referenzdaten statt als Konstanten. Nutze Pulse, um die Routineberichterstattung zu verschlanken, aber stell Bilanzgrenzen und Annahmen auf das Dashboard, damit die Zahlen verteidigt werden können. Das Diagramm sind die einfachen 20 %; die vertrauenswürdige Datengrundlage sind die 80 %, auf die es tatsächlich ankommt.

*Teil des Tracks [ESG]({{ '/de/tracks/esg/' | relative_url }}).* Verwandt: [Aufbau einer Brauerei-Datengrundlage für KI]({{ '/de/2024/building-brewery-data-foundation-ai/' | relative_url }}).

## Häufig gestellte Fragen

**Was sind die zentralen ESG-Kennzahlen für ein Brauerei-Dashboard?**
Wasser-zu-Bier-Verhältnis (hl Wasser pro hl Bier), Energieintensität (kWh oder MJ pro hl) und CO₂-Emissionen nach Scope (1, 2 und idealerweise 3) pro hl. Die Normalisierung pro hl macht Standorte unterschiedlicher Größe vergleichbar.

**Wie berechne ich CO₂-Emissionen in Tableau?**
Multipliziere Aktivitätsdaten, etwa Gas- oder Stromverbrauch, mit einem Emissionsfaktor in einem berechneten Feld. Die Zahl ist nur so gut wie der Faktor, speichere Faktoren daher als gepflegte Referenztabelle, nicht als fest codierte Konstanten.

**Kann ein Dashboard Greenwashing verhindern?**
Es kann helfen, indem es Bilanzgrenzen, Faktoren und Annahmen explizit macht, aber es kann selektive Berichterstattung nicht verhindern. Greenwashing ist ein Governance-Problem; die Rolle des Dashboards ist es, das Gesamtbild ehrlich zu zeigen, einschließlich der schlechten Trends.
