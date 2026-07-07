---
layout: post
lang: de
title: "CO2-Bilanzierung: Scope 1, 2 und 3 für Brauereien"
image: /assets/og/carbon-accounting-breweries-scope.png
description: "Ein praktischer Rahmen für die CO2-Bilanzierung des Brauereibetriebs über Scope-1-, 2- und 3-Emissionen — für Nachhaltigkeitsverantwortliche und CFOs."
date: 2025-03-28
updated: 2025-03-28
permalink: /de/2025/carbon-accounting-breweries-scope/
tags: [esg, carbon-accounting, scope-3]
faq:
  - q: "Was sind Scope-1-, 2- und 3-Emissionen im Kontext einer Brauerei?"
    a: "Scope 1 umfasst direkte Emissionen aus brauereieigener Verbrennung — Kessel, Fuhrpark, Kältemittel. Scope 2 umfasst zugekauften Strom und Wärme. Scope 3 erfasst alles vor- und nachgelagert: landwirtschaftliche Inputs (Gerste, Hopfen, Wasser), Verpackungsmaterialien, Logistik und Verbrauchernutzung. Für die meisten Brauereien ist Scope 3 mit Abstand die größte Kategorie."
  - q: "Ist die Berichterstattung über Scope 3 für Brauereien verpflichtend?"
    a: "Der Pflichtstatus hängt von Rechtsraum und Rahmenwerk ab. Unter der EU-CSRD (für betroffene Unternehmen) müssen wesentliche Scope-3-Kategorien berichtet werden. GRI und CDP fragen Scope 3 freiwillig ab, aber mit wachsendem Investorendruck. Selbst wo rechtlich nicht erforderlich, wird das Weglassen von Scope 3 in Lieferanten- und Investorengesprächen zunehmend zum Glaubwürdigkeitsrisiko."
  - q: "Wie genau kann die Scope-3-Schätzung einer Brauerei realistisch sein?"
    a: "Die Genauigkeit hängt von der Datenqualität auf jeder Stufe der Lieferkette ab. Ausgabenbasierte Emissionsfaktoren (mit finanziellen Stellvertretern) sind schnell, aber ungenau — Fehler von 30–50 % gegenüber prozessbasierten Daten sind in Lebensmittel- und Getränkelieferketten üblich. Primärdaten von Lieferanten liefern bessere Zahlen, erfordern aber erhebliches Engagement des Beschaffungsteams. Die meisten Brauereien nutzen einen Hybridansatz und legen die Methodik neben der Zahl offen."
---

**Kurze Antwort:** Die Herausforderung der CO2-Bilanzierung für eine Brauerei ist nicht Scope 1 oder 2 — die sind mit vorhandenen Zählern und Versorgungsrechnungen messbar. Das harte, wesentliche Problem ist Scope 3, wo der Großteil des tatsächlichen Klimaeinflusses einer Brauerei liegt und wo die Datenqualität umso stärker sinkt, je weiter vorgelagert man geht.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Die Betriebsschleife, die dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DIE BETRIEBSSCHLEIFE</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">CO2-Bilanzierung: Scope 1, 2 und 3 für Brauereien</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">den Betrieb ändern</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die Betriebsschleife, die dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Das Drei-Scope-Modell, angewandt aufs Brauen

Die Drei-Scope-Taxonomie des GHG Protocol ist heute das Standardvokabular für die Klima-Berichterstattung von Unternehmen, und sie bildet sich auf den Brauereibetrieb auf eine spezifische und lehrreiche Weise ab.

**Scope 1** (direkt): Verbrennung in Kesseln, direktbefeuerten Sudpfannensystemen, Kältemittelleckagen vor Ort, eigene Lieferfahrzeuge. Handhabbar und messbar; der Weg zur Reduktion führt über Brennstoffwechsel und Anlagenmodernisierung.

**Scope 2** (indirekte Energie): zugekaufter Strom und Dampf. Die CO2-Intensität des Netzes einer Brauerei bestimmt den Großteil dieser Zahl. Stromabnahmeverträge (PPAs) und Vor-Ort-Erneuerbare sind die wichtigsten Minderungshebel.

**Scope 3** (Wertschöpfungskette): Hier liegt die eigentliche Arbeit — und das eigentliche Risiko. Kategorie 1 (zugekaufte Waren und Dienstleistungen) umfasst Gerste, Hopfen, Zusatzstoffe, Verpackung und Verarbeitungshilfsstoffe. Kategorie 4 (vorgelagerte Logistik) umfasst eingehende Fracht. Kategorie 11 (Nutzung verkaufter Produkte) ist für Bier in der Regel unwesentlich. Die Kategorien 12 und 13 (End-of-Life und nachgelagerter Transport) sind für Verpackungsentscheidungen relevant. Für die meisten mittleren bis großen Brauereien stellt Scope 3 die deutliche Mehrheit der Gesamtemissionen dar — überwältigend getrieben von Rohstoffen und Verpackung.

## Warum Verpackung ein Scope-3-Brennpunkt ist

Glas, Aluminium und Wellpappe tragen jeweils wesentlich unterschiedlichen eingebetteten Kohlenstoff pro Einheit. Aluminiumdosen haben hohe Produktionsenergie, aber hohes Recyclinganteilspotenzial und geringeres Transportgewicht. Glas ist schwerer und energieintensiv in der Herstellung, wobei Mehrwegflaschensysteme die Lebenszyklusrechnung ändern können. Fässer zeigen bei mehrfacher Wiederverwendung über viele Zyklen oft günstige Pro-Ausschank-CO2-Profile. Keiner dieser Vergleiche ist einfach, weil sie von Recyclingquoten, Logistikdistanzen und Verbraucherverhalten abhängen — die alle je nach Markt variieren. Die Verpackungs-CO2-Frage wird ausführlich behandelt unter [{{ '/de/2025/packaging-footprint-glass-can-keg/' | relative_url }}]({{ '/de/2025/packaging-footprint-glass-can-keg/' | relative_url }}).

## Einen glaubwürdigen Mess-Stack aufbauen

Eine Brauerei, die von ambitionierten Zusagen zu prüfbaren CO2-Bilanzen übergeht, braucht vier Komponenten:

1. **Erhebung von Aktivitätsdaten**: Produktionsmengen, Energierechnungen, Logistikaufzeichnungen, Beschaffungsausgaben nach Warenkategorie.
2. **Emissionsfaktoren**: idealerweise Primärdaten von Lieferanten; realistisch ein Mix aus sektorüblichen Faktoren (z. B. aus Ecoinvent-, DEFRA- oder EPA-Datenbanken), gewichtet auf Kategorien mit der höchsten Materialintensität.
3. **Konsolidierungssoftware**: manuelle Tabellen werden jenseits einer bescheidenen Anzahl von Standorten und SKUs unhaltbar. Plattformen wie Persefoni, Watershed oder branchenspezifische Werkzeuge integrieren sich mit ERP-Daten und wenden Faktorbibliotheken konsistent an.
4. **Prüfsicherheit**: Eine eingeschränkte oder hinreichende Prüfsicherheit durch Dritte wird zunehmend von großen Einzelhandelskunden und institutionellen Investoren erwartet und ist unter der CSRD für betroffene Einheiten erforderlich.

## Alkoholfreies Bier und die CO2-Linse

Alkoholfreies Bier bringt durch die Entalkoholisierungsenergie Scope-1-Komplexität, aber sein Scope-3-Profil aus Rohstoffen ist bei gleichem Chargenvolumen weitgehend ähnlich zu den vollwertigen Äquivalenten. Der interessantere Blickwinkel ist die Portfolioebene: Eine Brauerei, die Volumen von vollwertig zu alkoholfrei verschiebt, sieht in der Regel keine automatische Scope-3-Reduktion, kann aber einen bedeutsamen ESG-Gewinn in der sozialen Säule sehen — was für Rahmenwerke zählt, die über alle drei Dimensionen bewerten. Siehe den eigenen ESG-Fall für alkoholfreies Bier unter [{{ '/de/2025/non-alcoholic-beer-esg-story/' | relative_url }}]({{ '/de/2025/non-alcoholic-beer-esg-story/' | relative_url }}).

## Aus Zahlen Zusagen machen

Die Freigabe durch die Science-Based Targets initiative (SBTi) erfordert modellierte Scope-1+2+3-Pfade, ausgerichtet an 1,5-°C-Trajektorien. Die Brauereibranche hat mehrere Unternehmen in verschiedenen Stadien der SBTi-Validierung. Die durch die SBTi-Methodik auferlegte Disziplin — ein Basisjahr definieren, Abdeckungsgrenzen dokumentieren, Neuberechnungsrichtlinien erklären — ist unabhängig vom externen Siegel wertvoll, weil sie eine interne Abstimmung darüber erzwingt, was die Zahlen bedeuten und wer sie verantwortet.

> **Ehrlicher Vorbehalt:** Emissionsfaktoren für landwirtschaftliche Rohstoffe wie Gerste und Hopfen tragen erhebliche Unsicherheit aufgrund regionaler Unterschiede in landwirtschaftlicher Praxis, Düngemitteleinsatz und Bilanzierung von Landnutzungsänderungen. Jede Scope-3-Zahl ist eine Schätzung; die Methodik-Fußnote ist so wichtig wie die Schlagzeilenzahl.

*Teil des ESG-Tracks — [alle durchsuchen]({{ '/de/tags/' | relative_url }}#esg).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Emissionen nach Scope aufgeteilt — der Großteil des Fußabdrucks versteckt sich meist in Scope 3."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">FUSSABDRUCK NACH SCOPE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">CO2-Bilanzierung: Scope 1, 2 und 3 für Brauereien</text><rect x="300" y="80" width="120" height="40" fill="#2e9e7c"/><rect x="300" y="120" width="120" height="40" fill="#00695c"/><rect x="300" y="160" width="120" height="90" fill="#06483f"/><rect x="460" y="84" width="14" height="14" fill="#2e9e7c"/><text x="482" y="96" font-family="sans-serif" font-size="12.5" fill="#06483f">Scope 1 — direkt</text><rect x="460" y="124" width="14" height="14" fill="#00695c"/><text x="482" y="136" font-family="sans-serif" font-size="12.5" fill="#06483f">Scope 2 — Energie</text><rect x="460" y="184" width="14" height="14" fill="#06483f"/><text x="482" y="196" font-family="sans-serif" font-size="12.5" fill="#06483f">Scope 3 — Wertschöpfungskette (größte)</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Emissionen nach Scope aufgeteilt — der Großteil des Fußabdrucks versteckt sich meist in Scope 3.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was sind Scope-1-, 2- und 3-Emissionen im Kontext einer Brauerei?**
Scope 1 umfasst direkte Emissionen aus brauereieigener Verbrennung — Kessel, Fuhrpark, Kältemittel. Scope 2 umfasst zugekauften Strom und Wärme. Scope 3 erfasst alles vor- und nachgelagert: landwirtschaftliche Inputs (Gerste, Hopfen, Wasser), Verpackungsmaterialien, Logistik und Verbrauchernutzung. Für die meisten Brauereien ist Scope 3 mit Abstand die größte Kategorie.

**Ist die Berichterstattung über Scope 3 für Brauereien verpflichtend?**
Der Pflichtstatus hängt von Rechtsraum und Rahmenwerk ab. Unter der EU-CSRD (für betroffene Unternehmen) müssen wesentliche Scope-3-Kategorien berichtet werden. GRI und CDP fragen Scope 3 freiwillig ab, aber mit wachsendem Investorendruck. Selbst wo rechtlich nicht erforderlich, wird das Weglassen von Scope 3 in Lieferanten- und Investorengesprächen zunehmend zum Glaubwürdigkeitsrisiko.

**Wie genau kann die Scope-3-Schätzung einer Brauerei realistisch sein?**
Die Genauigkeit hängt von der Datenqualität auf jeder Stufe der Lieferkette ab. Ausgabenbasierte Emissionsfaktoren (mit finanziellen Stellvertretern) sind schnell, aber ungenau — Fehler von 30–50 % gegenüber prozessbasierten Daten sind in Lebensmittel- und Getränkelieferketten üblich. Primärdaten von Lieferanten liefern bessere Zahlen, erfordern aber erhebliches Engagement des Beschaffungsteams. Die meisten Brauereien nutzen einen Hybridansatz und legen die Methodik neben der Zahl offen.
