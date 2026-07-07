---
layout: post
lang: de
title: "Der ESG-Reporting-Stack: CSRD- und GRI-Offenlegung automatisieren"
image: /assets/og/esg-reporting-automation-csrd.png
description: "Wie ESG-Reporting-Automatisierung Brauereien hilft, CSRD- und GRI-Anforderungen zu erfüllen, ohne in manueller Datenerfassung zu ertrinken."
date: 2025-05-28
updated: 2025-05-28
permalink: /de/2025/esg-reporting-automation-csrd/
tags: [esg, csrd, reporting-automation]
faq:
  - q: "Was ist CSRD und gilt sie für Brauereien?"
    a: "Die Corporate Sustainability Reporting Directive ist eine EU-Verordnung, die große und börsennotierte Unternehmen verpflichtet, detaillierte Nachhaltigkeitsinformationen anhand der European Sustainability Reporting Standards (ESRS) offenzulegen. Sie gilt für in der EU ansässige Brauereien, die Größenschwellen erreichen (grob: 250+ Mitarbeitende oder 40 Mio. € + Umsatz), und wird schrittweise kleinere Unternehmen und Nicht-EU-Firmen mit erheblicher EU-Tätigkeit erfassen. Die Fristen sind nach Unternehmensgröße gestaffelt."
  - q: "Kann ESG-Reporting-Software von der Stange einen Nachhaltigkeitsberater ersetzen?"
    a: "Nein — und Anbieter, die etwas anderes nahelegen, übertreiben. Software automatisiert die Datenaggregation, wendet Emissionsfaktoren an und formatiert die Ausgabe für Framework-Vorlagen. Sie kann die Wesentlichkeitsanalyse, die Stakeholder-Einbindung und die Ermessensentscheidungen nicht ersetzen, die definieren, was ein Unternehmen berichten sollte. Berater und internes Fachwissen bleiben unerlässlich, besonders für die unter CSRD geforderten doppelten Wesentlichkeitsanalysen."
  - q: "Wie verbindet eine Brauerei ihre ERP-Daten mit ESG-Reporting-Tools?"
    a: "Die meisten ESG-Plattformen akzeptieren Daten über Flat-File-Import (CSV/Excel), API-Integration oder vorgefertigte Konnektoren zu gängigen ERPs. Die entscheidende Voraussetzung ist, dass die ERP-Quelldaten sauber und korrekt getaggt sind — Energieverbrauch je Standort, Produktionsvolumen je Produktlinie, Beschaffungsausgaben je Rohstoff. Ohne strukturierte Quelldaten verstärkt Automatisierung Inkonsistenz, statt manuellen Aufwand zu beseitigen."
---

**Kurze Antwort:** ESG-Reporting-Automatisierung kann den manuellen Aufwand der Offenlegung drastisch reduzieren — aber sie kann das schwierigere vorgelagerte Problem inkonsistenter, unstrukturierter Quelldaten nicht lösen. Die Technologie ist der einfache Teil; die Daten-Governance ist es nicht.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Der ESG-Reporting-Stack: CSRD- und GRI-Offenlegung automatisieren</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Daten herein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">die Halle verändern</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Warum Reporting zu einer großen operativen Last geworden ist

Eine Brauerei, die gleichzeitig gegenüber den GRI-Standards, CDP Climate und der EU-CSRD offenlegt, steht vor Hunderten verschiedener Datenpunkte: Energie nach Quelle, Wasser nach Entnahmekategorie, Abfall nach Entsorgungsweg, THG-Emissionen nach Scope und Kategorie, Lieferantenbewertungen, Arbeitskennzahlen und Governance-Indikatoren. Wenn diese Zahlen in getrennten Systemen leben — Energiemanagement-Plattformen, ERP, HR-Software, Logistikportale — wird das Zusammenstellen eines kohärenten Jahresberichts zu einer monatelangen manuellen Übung mit hohem Fehlerrisiko.

Die Kosten sind nicht nur Arbeit. Fehler in offengelegten Daten oder nach der Veröffentlichung entdeckte wesentliche Auslassungen tragen regulatorische und reputationsbezogene Folgen, die mit strenger werdenden Reporting-Standards eskalieren. CSRD führt zunächst Anforderungen an eine begrenzte Prüfsicherheit ein und bewegt sich auf eine hinreichende Prüfsicherheit zu — das heißt, offengelegte Zahlen müssen externer Prüfung standhalten.

## Die Schichten eines modernen ESG-Reporting-Stacks

Ein gut architekturierter Automatisierungs-Stack lässt sich am besten in vier Schichten verstehen:

**1. Datenerfassung**: Sensoren, Zähler und operative Systeme erzeugen die Rohsignale. Eine Submetering-Infrastruktur (besprochen im [Beitrag zur Wasser-Bewirtschaftung]({{ '/de/2025/water-stewardship-analytics-brewing/' | relative_url }})) ist das ökologische Fundament. HR- und Beschaffungssysteme speisen die Sozial- und Lieferkettenschichten.

**2. Datenintegration und -normalisierung**: ETL-Prozesse (Extrahieren-Transformieren-Laden) ziehen Daten aus Quellsystemen, wenden Einheitenumrechnungen an und richten Berichtsperioden aus. In dieser Schicht wird der meiste Umsetzungsaufwand verbraucht und treten die meisten Projektfehlschläge auf.

**3. Berechnung und Faktoranwendung**: Emissionsfaktoren, Intensitätsverhältnisse und Logik zur Zielverfolgung werden angewendet. Führende Plattformen pflegen Faktorbibliotheken, die an DEFRA-, EPA- und GHG-Protocol-Standards gebunden sind, und aktualisieren sie, wenn Faktoren überarbeitet werden.

**4. Offenlegungsformatierung**: Frameworks unterscheiden sich in der Struktur. GRI nutzt eine themenweise Erzählung plus quantitative Tabellen. ESRS (unter CSRD) erfordert Informationen auf Unternehmensebene, Offenlegungsanforderungen und Datenpunkte, die auf die Ergebnisse der doppelten Wesentlichkeit abgebildet werden. CDP nutzt bewertete Fragebögen. Gute Plattformen erzeugen Framework-zugeordnete Ausgaben, statt für jedes eine manuelle Neuformatierung zu erfordern.

## Doppelte Wesentlichkeit: Die analytische Herausforderung, die Automatisierung nicht lösen kann

Die methodisch prägende Anforderung der CSRD ist die *doppelte Wesentlichkeitsanalyse* — die Bewertung sowohl, wie Nachhaltigkeitsthemen das Unternehmen beeinflussen (finanzielle Wesentlichkeit), als auch, wie das Unternehmen Umwelt und Gesellschaft beeinflusst (Wirkungswesentlichkeit). Dies erfordert strukturierte Stakeholder-Einbindung, interne Beratung und dokumentierte Belegketten. Keine Software automatisiert das. Was Software tun kann, ist die Ausgabe organisieren — identifizierte wesentliche Themen bestimmten ESRS-Offenlegungsanforderungen zuordnen und Datenlücken markieren.

Brauereien, die doppelte Wesentlichkeitsanalysen durchgeführt haben, identifizieren durchweg Wasserverbrauch, Emissionen der landwirtschaftlichen Lieferkette, das Lebensende von Verpackungen und verantwortungsvollen Konsum (die AF-Bier-Chance) als hochpriorisierte Themen. Der Analyseprozess dient damit zugleich als strategische Priorisierungsübung.

## Worauf bei einer ESG-Plattform zu achten ist

Angesichts der Vielzahl von Anbietern in diesem Bereich sollte eine praktische Bewertung Folgendes gewichten:

- **Framework-Abdeckung**: Unterstützt sie ESRS, GRI, CDP und idealerweise TCFD nativ in einer einzigen Umgebung?
- **Prüfpfad**: Lässt sich jeder offengelegte Datenpunkt auf einen Quelldatensatz zurückverfolgen, mit dokumentierter Berechnungsmethodik?
- **Tiefe der ERP-Integration**: vorgefertigte Konnektoren vs. generische API vs. manueller Import — der Unterschied zählt enorm für die laufenden Wartungskosten.
- **Prüfbereitschaft**: Kann die Plattform die strukturierten Belegpakete erzeugen, die externe Prüfungsanbieter benötigen?

> **Ehrlicher Vorbehalt:** Die Marktversprechen von ESG-Software sind häufig der gelieferten Funktionalität voraus. Referenzprüfungen mit Unternehmen ähnlicher Größe und Komplexität im Lebensmittel- und Getränkesektor sind aufschlussreicher als Analysten-Rankings oder vom Anbieter gelieferte Fallstudien.

*Teil des ESG-Tracks — [alle durchsuchen]({{ '/de/tags/' | relative_url }}#esg).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Emissionen aufgeteilt nach Scope — der größte Teil des Fußabdrucks verbirgt sich meist in Scope 3."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FUSSABDRUCK NACH SCOPE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Der ESG-Reporting-Stack: CSRD- und GRI-Offenlegung automatisieren</text><rect x="300" y="80" width="120" height="40" fill="#2e9e7c"/><rect x="300" y="120" width="120" height="40" fill="#00695c"/><rect x="300" y="160" width="120" height="90" fill="#06483f"/><rect x="460" y="84" width="14" height="14" fill="#2e9e7c"/><text x="482" y="96" font-family="sans-serif" font-size="12.5" fill="#06483f">Scope 1 — direkt</text><rect x="460" y="124" width="14" height="14" fill="#00695c"/><text x="482" y="136" font-family="sans-serif" font-size="12.5" fill="#06483f">Scope 2 — Energie</text><rect x="460" y="184" width="14" height="14" fill="#06483f"/><text x="482" y="196" font-family="sans-serif" font-size="12.5" fill="#06483f">Scope 3 — Wertschöpfungskette (größter)</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Emissionen aufgeteilt nach Scope — der größte Teil des Fußabdrucks verbirgt sich meist in Scope 3.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist CSRD und gilt sie für Brauereien?**
Die Corporate Sustainability Reporting Directive ist eine EU-Verordnung, die große und börsennotierte Unternehmen verpflichtet, detaillierte Nachhaltigkeitsinformationen anhand der European Sustainability Reporting Standards (ESRS) offenzulegen. Sie gilt für in der EU ansässige Brauereien, die Größenschwellen erreichen (grob: 250+ Mitarbeitende oder 40 Mio. € + Umsatz), und wird schrittweise kleinere Unternehmen und Nicht-EU-Firmen mit erheblicher EU-Tätigkeit erfassen. Die Fristen sind nach Unternehmensgröße gestaffelt.

**Kann ESG-Reporting-Software von der Stange einen Nachhaltigkeitsberater ersetzen?**
Nein — und Anbieter, die etwas anderes nahelegen, übertreiben. Software automatisiert die Datenaggregation, wendet Emissionsfaktoren an und formatiert die Ausgabe für Framework-Vorlagen. Sie kann die Wesentlichkeitsanalyse, die Stakeholder-Einbindung und die Ermessensentscheidungen nicht ersetzen, die definieren, was ein Unternehmen berichten sollte. Berater und internes Fachwissen bleiben unerlässlich, besonders für die unter CSRD geforderten doppelten Wesentlichkeitsanalysen.

**Wie verbindet eine Brauerei ihre ERP-Daten mit ESG-Reporting-Tools?**
Die meisten ESG-Plattformen akzeptieren Daten über Flat-File-Import (CSV/Excel), API-Integration oder vorgefertigte Konnektoren zu gängigen ERPs. Die entscheidende Voraussetzung ist, dass die ERP-Quelldaten sauber und korrekt getaggt sind — Energieverbrauch je Standort, Produktionsvolumen je Produktlinie, Beschaffungsausgaben je Rohstoff. Ohne strukturierte Quelldaten verstärkt Automatisierung Inkonsistenz, statt manuellen Aufwand zu beseitigen.
