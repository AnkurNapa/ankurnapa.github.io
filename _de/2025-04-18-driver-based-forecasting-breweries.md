---
layout: post
lang: de
title: "Treiberbasierte Prognose: Jenseits des Jahresbudgets"
image: /assets/og/driver-based-forecasting-breweries.png
description: "Treiberbasierte Prognose ersetzt statische Brauereibudgets durch dynamische Modelle, gebunden an reale Volumen-, Mix- und Kostentreiber — auch für alkoholfreies Bier."
date: 2025-04-18
updated: 2025-04-18
permalink: /de/2025/driver-based-forecasting-breweries/
tags: [fpna, forecasting, budgeting]
faq:
  - q: "Was ist treiberbasierte Prognose für eine Brauerei?"
    a: "Die treiberbasierte Prognose baut die Finanzprognose aus operativen Eingaben auf — geplante Sude, hL pro SKU, Personal pro Schicht, Rohstoff-Vertragspreise — statt aus den Zahlen des Vorjahres mit einer prozentualen Anpassung. Die GuV wird zu einem nachgelagerten Output des Betriebsmodells, nicht zu einem Ausgangspunkt."
  - q: "Wie behandelt die treiberbasierte Prognose das Volumen alkoholfreien Biers anders?"
    a: "Alkoholfreies Bier hat oft eine andere Nachfrage-Saisonalität als reguläres Bier — die Spitzenmonate können sich in Richtung Januar und sommerliche Trockenperioden verschieben statt traditioneller On-Premise-Saisons. Ein treiberbasiertes Modell erfasst das, indem es NA-spezifische Volumentreiber nutzt, statt eine pauschale Wachstumsrate auf das Gesamtportfolio anzuwenden."
  - q: "Was ist das größte Hindernis für die treiberbasierte Prognose in kleinen und mittelgroßen Brauereien?"
    a: "Datenfragmentierung. Volumendaten leben im Brausystem, Preisdaten in Distributorenportalen und Kostendaten im ERP. Bis diese drei Quellen ein einziges Modell speisen, ist jede Prognoseaktualisierung eine manuelle Abstimmungsübung, die die Zeit verschlingt, die sie eigentlich sparen sollte."
---

**Kurze Antwort:** Das Jahresbudget ist das falsche Werkzeug für ein Geschäft, in dem Gerstenpreise sich in einem Quartal um 20 % bewegen können, die Nachfrage nach alkoholfreiem Bier die Sommerverkaufskurve umformt und ein einziger großer Großhandelskunde deinen Kanal-Mix über Nacht verschieben kann. Die treiberbasierte Prognose ersetzt das kalendergetriebene Ritual durch ein lebendiges Modell, das sich aktualisiert, wann immer sich die Eingaben ändern, die deine Ökonomie tatsächlich treiben.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Treiberbasierte Prognose: Jenseits des Jahresbudgets</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">den Betrieb ändern</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Was „treiberbasiert" tatsächlich bedeutet

Die meisten Brauereibudgets werden gebaut, indem man mit der Umsatzzeile des Vorjahres beginnt, eine Wachstumsannahme anwendet und dann prüft, ob die Kostenstruktur bei diesem Umsatzniveau tragbar ist. Das Ergebnis ist ein Dokument, das am Tag der Unterschrift genau ist und für die folgenden elf Monate zunehmend fiktiv wird.

Die treiberbasierte Prognose kehrt die Logik um. Das Modell beginnt mit den operativen Treibern — geplanter Sudplan, SKU-Mix, Preis pro hL je Kanal und Rohstoff-Vertragspreise — und leitet die Finanzkennzahlen aus diesen Eingaben ab. Wenn sich ein Treiber ändert, aktualisieren sich GuV und Cashflow automatisch.

Die Unterscheidung ist wichtig, weil sie ändert, wem die Prognose gehört. In einem treiberbasierten Modell hat die Entscheidung des Braumeisters, zwei Sude von einem hochgrädigen Saisonbier auf ein Standard-Lager zu verschieben, eine sofortige, sichtbare finanzielle Konsequenz. Diese Transparenz schafft eine Verantwortlichkeit, die ein Tabellenbudget nicht kann.

## Den Treiberbaum aufbauen

Ein Brauerei-Treiberbaum hat typischerweise drei Ebenen:

**Volumentreiber** — geplante Sude, erwarteter Ausbeuteverlust, hL nach SKU, prognostizierter Abverkauf nach Kanal (On-Premise, Off-Premise, DTC, Export). Volumen ist der Haupthebel; alles andere skaliert daraus.

**Preis- und Mix-Treiber** — durchschnittlicher Nettoumsatz pro hL je Kanal, Trade-Spend-Rate und SKU-Mix. Eine Verschiebung hin zu alkoholfreiem Bier — das oft einen höheren Bruttopreis, aber auch höhere Produktionskosten trägt — ändert die mixbereinigte Marge, selbst wenn das Gesamtvolumen flach ist. Hier gehen viele Brauereiprognosen schief: Sie modellieren das Gesamt-hL, aber nicht den Mix.

**Kostentreiber** — Standard-COGS pro hL (siehe den [Beitrag zu Herstellkosten pro Hektoliter]({{ '/de/2025/cost-of-goods-per-hectoliter/' | relative_url }})), Rohstoffpreis-Annahmen, Personal pro Schicht und Versorgungstarife. Jeder davon sollte einen benannten Annahmen-Eigentümer haben, der für die Aktualisierung verantwortlich ist, wenn sich die Marktbedingungen ändern.

## Die Reforecast-Kadenz

Ein Jahresbudget mit einem Halbjahres-Reforecast ist keine Prognose — es sind zwei Budgets. Ein treiberbasiertes Modell ermöglicht eine rollierende Prognose in monatlicher oder quartalsweiser Kadenz ohne das politische Gewicht einer „Budgetrevision".

Die praktische Kadenz für die meisten Brauereien: ein monatlicher Flash, fokussiert auf die drei wichtigsten Volumen- und Kostentreiber, ein quartalsweiser rollierender 12-Monats-Reforecast, der alle Annahmen aktualisiert, und eine Szenarioaktualisierung, wann immer eine Makro-Eingabe — Getreide, Energie, Aluminium — außerhalb des im Modell definierten Toleranzbereichs liegt.

## Alkoholfreies Bier als Prognose-Herausforderung

Alkoholfreies Bier verkompliziert die Prognose auf zwei Arten, die eine explizite Behandlung verdienen.

Erstens unterscheidet sich die Nachfrage-Saisonalität. Standardbier erreicht seinen Höhepunkt im Sommer im On-Premise. Alkoholfreies Bier erlebt Nachfragespitzen, die an Trockenmonat-Kampagnen und Wellness-Trends gebunden sind, die nicht derselben Kurve folgen. Einen Standard-Saisonindex auf das NA-Volumen anzuwenden, wird systematisch den Januar unterprognostizieren und den Mai überprognostizieren.

Zweitens ist die Kostenstruktur unterschiedlich genug, dass NA-hL eine eigene Treiberzeile im Modell haben sollte, nicht in einen gemischten Durchschnitt eingefaltet werden. Die Entalkoholisierungskosten, die oft kleineren Chargengrößen und der Verpackungsmix (Dosen gegen Fässer) können die Stückökonomie von NA sehr anders aussehen lassen als beim Flaggschiff-Lager — besser in einigen Kanälen, schlechter in anderen.

## Wo treiberbasierte Modelle zusammenbrechen

Der ehrliche Vorbehalt: Ein treiberbasiertes Modell ist nur so gut wie die Disziplin hinter seinen Eingaben. Wenn das Vertriebsteam die Volumenannahmen nicht monatlich aktualisiert, wenn das Einkaufsteam Änderungen an Rohstoffverträgen nicht markiert und wenn das Betriebsteam die tatsächlichen Chargenausbeuten nicht erfasst, driftet das Modell wieder zu einer ausgefeilt aussehenden Tabelle, der niemand traut.

Die Lösung ist Governance, nicht mehr Technologie. Weise jedem Treiber einen benannten Eigentümer zu, definiere einen Aktualisierungsplan und baue einen einfachen Abweichungsbericht, der zeigt, wann eine Annahme um mehr als eine definierte Schwelle von den Ist-Werten abgewichen ist. Die KI-gestützten Prognosewerkzeuge, die in [KI-Nachfrageprognose für Brauereien]({{ '/de/2026/ai-demand-forecasting-for-breweries/' | relative_url }}) besprochen werden, können bei der Volumenebene helfen, aber die Kosten- und Preistreiber erfordern nach wie vor menschliches Urteil.

*Teil des Tracks Financial Planning & Analytics — [alle durchsuchen]({{ '/de/tags/' | relative_url }}#fpna).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">PROGNOSE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Treiberbasierte Prognose: Jenseits des Jahresbudgets</text><g stroke="#06483f" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#00695c" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#00695c" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#06483f" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">heute</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">Historie</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">Prognose</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist treiberbasierte Prognose für eine Brauerei?**
Die treiberbasierte Prognose baut die Finanzprognose aus operativen Eingaben auf — geplante Sude, hL pro SKU, Personal pro Schicht, Rohstoff-Vertragspreise — statt aus den Zahlen des Vorjahres mit einer prozentualen Anpassung. Die GuV wird zu einem nachgelagerten Output des Betriebsmodells, nicht zu einem Ausgangspunkt.

**Wie behandelt die treiberbasierte Prognose das Volumen alkoholfreien Biers anders?**
Alkoholfreies Bier hat oft eine andere Nachfrage-Saisonalität als reguläres Bier — die Spitzenmonate können sich in Richtung Januar und sommerliche Trockenperioden verschieben statt traditioneller On-Premise-Saisons. Ein treiberbasiertes Modell erfasst das, indem es NA-spezifische Volumentreiber nutzt, statt eine pauschale Wachstumsrate auf das Gesamtportfolio anzuwenden.

**Was ist das größte Hindernis für die treiberbasierte Prognose in kleinen und mittelgroßen Brauereien?**
Datenfragmentierung. Volumendaten leben im Brausystem, Preisdaten in Distributorenportalen und Kostendaten im ERP. Bis diese drei Quellen ein einziges Modell speisen, ist jede Prognoseaktualisierung eine manuelle Abstimmungsübung, die die Zeit verschlingt, die sie eigentlich sparen sollte.
