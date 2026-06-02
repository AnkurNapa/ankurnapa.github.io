---
layout: post
lang: de
title: "Ein Abverkaufs- und Sell-Through-Dashboard in Tableau"
image: /assets/og/tableau-depletions-sell-through-dashboard.png
description: "Baue ein Abverkaufs- und Sell-Through-Dashboard in Tableau mit LOD-Ausdrücken, YoY-Tabellenberechnungen und Pulse, um Accounts zu erkennen, die langsamer werden."
date: 2023-03-04
updated: 2023-03-04
permalink: /de/2023/tableau-depletions-sell-through-dashboard/
tags: [sales-intelligence, tableau, analytics]
faq:
  - q: "Was ist der Unterschied zwischen Depletions und Lieferungen?"
    a: "Lieferungen sind Kartons, die du an einen Distributor verkaufst; Depletions sind Kartons, die der Distributor an Einzelhandels-Accounts weiterverkauft. Depletions sind das wahrere Nachfragesignal, aber sie kommen später und hängen vom Reporting des Distributors ab."
  - q: "Wie berechne ich die Sell-Through-Rate in Tableau?"
    a: "Nutze einen FIXED-LOD-Ausdruck, um Depletions und Bestand auf der Account-SKU-Granularität zu fixieren, und teile dann Depletions durch die Summe aus Anfangsbestand plus Lieferungen. So bleibt die Rate unabhängig von Dashboard-Filtern stabil."
  - q: "Kann Tableau mich warnen, wenn ein Account langsamer wird?"
    a: "Ja. Tableau Pulse kann die Depletion-Geschwindigkeit je Account überwachen und einen Digest in natürlicher Sprache senden, wenn eine Kennzahl außerhalb ihres erwarteten Bereichs fällt, aber es markiert die Veränderung, statt die Ursache zu diagnostizieren."
---

**Kurze Antwort: Depletions, nicht Lieferungen, sind das Nachfragesignal, das es wert ist, beobachtet zu werden — und eine gut gebaute Tableau-Ansicht macht Sell-Through pro Account und SKU lesbar.** Lieferungen sagen dir, was dein Lager verlassen hat; Depletions sagen dir, was der Markt tatsächlich gezogen hat. Die Lücke dazwischen liegt im Keller eines Distributors, und genau dort gerät der Umsatz still ins Stocken.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für ein Abverkaufs- und Sell-Through-Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Ein Abverkaufs- und Sell-Through-Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Schlagzeilen-Kennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Aufgliedern.</figcaption>
</figure>

## Erst messen, dann visualisieren

Bevor du Tableau öffnest, definiere die Kennzahlen. Die Versuchung ist, ein Diagramm zu bauen und die Kennzahl rückwärts zu erschließen, und genau so streiten Teams im Meeting über Zahlen, statt danach zu handeln. Lege drei Dinge im Voraus fest: die Granularität (Account nach SKU nach Monat), die Nachfragekennzahl (Depletions in Kartons oder Neun-Liter-Äquivalenten) und die Effizienzkennzahl (Sell-Through-Rate).

Die Sell-Through-Rate ist Depletions geteilt durch verfügbaren Bestand — Anfangsbestand plus Lieferungen in der Periode. Fixiere in Tableau beide Seiten mit einem FIXED Level-of-Detail-Ausdruck, damit das Verhältnis korrekt bleibt, wenn ein Nutzer auf eine Marke oder eine Kette filtert:

`{ FIXED [Account], [SKU] : SUM([Depletion Cases]) } / { FIXED [Account], [SKU] : SUM([Opening Inv]) + SUM([Shipment Cases]) }`

FIXED ignoriert den Filterkontext des Dashboards, sodass der Nenner nicht schrumpft, wenn jemand hineindrillt. Diese eine Disziplin verhindert die meisten „Warum ändert sich der Prozentsatz, wenn ich klicke"-Beschwerden.

## Das Dashboard-Layout

Beginne mit der Divergenz zwischen Lieferungen und Depletions, denn das ist die zentrale Erkenntnis. Eine Linie mit zwei Achsen — Lieferungen als blasses Band, Depletions als kräftige Linie — zeigt sofort, wann du schneller einlieferst, als der Markt herauszieht. Füge eine YoY-Wachstumsspalte mit einer Tabellenberechnung hinzu (`(ZN(SUM([Depletions])) - LOOKUP(ZN(SUM([Depletions])), -12)) / ABS(LOOKUP(...))`), berechnet entlang der Monatsachse, damit ein nationaler Manager den Schwung sieht, nicht nur das absolute Volumen.

Die Arbeitsansicht ist eine Highlight-Tabelle mit Accounts in den Zeilen und den letzten Monaten über die Spalten, eingefärbt nach Sell-Through-Rate. Heiße Zellen sind gesund; kühle Zellen sind Bestand, der sich nicht bewegt. Füge einen Parameter hinzu, der die geografische Dimension tauscht — Gebiet, Bundesland, Distributor — sodass ein Dashboard dem Außendienstmitarbeiter und dem VP dient, ohne Arbeitsblätter zu duplizieren. Parameteraktionen ermöglichen es, dass ein Klick auf eine Region das Detailpanel darunter filtert, sodass die Navigation innerhalb der Leinwand bleibt, statt über Registerkarten verstreut zu sein.

Lege die KI obendrauf, nicht darunter. Tableau Pulse kann die Depletion-Geschwindigkeit je Schlüsselaccount beobachten und einen Digest in einfacher Sprache ausgeben — „Depletions für Account 4471 sind um 18 % gegenüber dem nachlaufenden Trend gesunken" — in den Posteingang des Außendienstmitarbeiters. Das ist echter Mehrwert: Es lenkt das menschliche Auge auf die richtige Zeile. Es ist jedoch Überwachung, keine Diagnose. Pulse sagt dir, dass der Account langsamer wurde; es kann dir nicht sagen, dass die Kette ihr Planogramm zurückgesetzt oder ein Wettbewerber das Endregal gekauft hat.

## Wo es scheitert

Die ehrliche Einschränkung liegt vorgelagert. Depletion-Daten sind nur so aktuell und sauber wie deine Distributor-Feeds, und die verzögern sich oft um zwei bis sechs Wochen, kommen in inkonsistenten Formaten an oder verrechnen Retouren still. Eine schöne Sell-Through-Heatmap, gebaut auf einem zwei Wochen alten, halb zugeordneten Feed, wird mit großer Überzeugung in die Irre führen. Tableau Prep kann die eingehenden Dateien standardisieren und entdoppeln, aber es kann keine Daten erfinden, die ein Distributor nie gesendet hat. Ordne deine SKUs und Accounts einer Master-Liste zu, bevor du einem einzigen Prozentsatz vertraust — nicht zugeordnete Zeilen verschwinden still aus den FIXED-Summen und verzerren die Rate.

Ebenso ist Sell-Through ein Verhältnis, und Verhältnisse verbergen Volumen. Ein Sell-Through von 95 % auf vier Kartons ist Rauschen; behandle winzige Nenner mit Misstrauen und erwäge, Accounts unter einer Mindestbestandsschwelle zu unterdrücken.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall ist."><rect x="0" y="0" width="720" height="310" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Ein Abverkaufs- und Sell-Through-Dashboard in Tableau</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#b45309" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reichweite · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#b45309" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interesse · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#b45309" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Test · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#b45309" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Gewinn · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall ist.</figcaption>
</figure>

## Das Fazit

Ein Depletions-Dashboard verdient sich seinen Platz, indem es die Lücke zwischen Lieferung und Markt unübersehbar macht, mit LOD-gestütztem Sell-Through, das das Filtern übersteht, und YoY-Tabellenberechnungen, die den Schwung zeigen. Lass Pulse die Verlangsamungen markieren und lass einen Menschen herausfinden, warum. Das Dashboard ist nur so ehrlich wie der Distributor-Feed darunter, also investiere in die Datenleitungen, bevor du an die Visualisierungen gehst.

*Teil des Tracks [Sales Intelligence]({{ '/de/tracks/sales-intelligence/' | relative_url }}).* Verwandt: [Eine Distributor-Scorecard in Tableau bauen]({{ '/de/2023/tableau-distributor-scorecard/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist der Unterschied zwischen Depletions und Lieferungen?**
Lieferungen sind Kartons, die du an einen Distributor verkaufst; Depletions sind Kartons, die der Distributor an Einzelhandels-Accounts weiterverkauft. Depletions sind das wahrere Nachfragesignal, aber sie kommen später und hängen vom Reporting des Distributors ab.

**Wie berechne ich die Sell-Through-Rate in Tableau?**
Nutze einen FIXED-LOD-Ausdruck, um Depletions und Bestand auf der Account-SKU-Granularität zu fixieren, und teile dann Depletions durch die Summe aus Anfangsbestand plus Lieferungen. So bleibt die Rate unabhängig von Dashboard-Filtern stabil.

**Kann Tableau mich warnen, wenn ein Account langsamer wird?**
Ja. Tableau Pulse kann die Depletion-Geschwindigkeit je Account überwachen und einen Digest in natürlicher Sprache senden, wenn eine Kennzahl außerhalb ihres erwarteten Bereichs fällt, aber es markiert die Veränderung, statt die Ursache zu diagnostizieren.
