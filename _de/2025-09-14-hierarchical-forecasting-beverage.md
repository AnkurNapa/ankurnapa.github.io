---
layout: post
lang: de
title: "Hierarchische Prognose: SKU-, Marken- und Gesamtvolumen abstimmen"
image: /assets/og/hierarchical-forecasting-beverage.png
description: "Wie hierarchische Prognose Nachfragesignale über SKU-, Marken- und Portfolioebenen hinweg abstimmt — und warum Fehlausrichtung zwischen Ebenen die Planungsglaubwürdigkeit zerstört."
date: 2025-09-14
updated: 2025-09-14
permalink: /de/2025/hierarchical-forecasting-beverage/
tags: [forecasting, hierarchical-forecasting]
faq:
  - q: "Was ist hierarchische Prognose?"
    a: "Hierarchische Prognose ist eine Methode zur Erstellung von Prognosen auf mehreren Aggregationsebenen — SKU, Marke, Kategorie, Gesamtportfolio — bei gleichzeitiger Sicherstellung, dass sie mathematisch konsistent sind. Eine Bottom-up-SKU-Prognose, die sich auf mehr summiert als das Top-down-Portfolioziel, ist ein häufiger und kostspieliger Fehlermodus, den diese Methode verhindern soll."
  - q: "Was ist der Unterschied zwischen Bottom-up- und Top-down-Prognose bei Getränken?"
    a: "Bottom-up-Prognose beginnt auf der SKU-Ebene und summiert nach oben. Top-down beginnt auf der Ebene des Gesamtportfolios oder Marktanteils und teilt nach unten zu. Jede hat blinde Flecken: Bottom-up kann Makrobeschränkungen verfehlen; Top-down kann SKU-Genauigkeit verlieren. Hierarchische Methoden kombinieren beides mithilfe von Abstimmungsalgorithmen."
  - q: "Wie verändert die Einführung eines alkoholfreien Biers die Hierarchie?"
    a: "Eine neue alkoholfreie SKU führt einen Zweig in die Hierarchie ein, der womöglich mehr Top-down-Marktkontext (Kategoriewachstumsraten) als Bottom-up-Daten hat (sie hat keine Historie). Hierarchische Modelle handhaben das elegant, indem sie das Top-down-Signal den alkoholfreien Knoten dominieren lassen, während das Bottom-up-Signal reife SKUs in derselben Markenfamilie verankert."
---

**Kurze Antwort:** Eine Prognose, die auf SKU-Ebene genau, aber mit dem Ziel auf Markenebene inkonsistent ist — oder ein Markenplan, der sich nicht zum Portfoliogesamt summiert — ist nicht nur ein mathematisches Ärgernis. Sie zerstört die Planungsglaubwürdigkeit, schafft kontroverse S&OP-Prozesse und führt zu widersprüchlichen Produktions- und Vertriebszusagen. Hierarchische Prognose löst dies strukturell, nicht durch Verhandlung.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Hierarchische Prognose: SKU-, Marken- und Gesamtvolumen abstimmen</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Daten hinein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">den Betrieb ändern</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Das Abstimmungsproblem, das S&OP sprengt

Die meisten Getränkeunternehmen führen mindestens zwei Prognoseprozesse parallel: eine kommerzielle oder Top-Line-Prognose, gebaut aus Marktanteils- und Kategoriewachstumsannahmen, und eine operative oder Liefer-Prognose, gebaut aus SKU-Historie. Diese beiden Prognosen stimmen standardmäßig fast nie überein.

Die resultierende „Lücke" wird zum Fokus der monatlichen Sales-&-Operations-Planning-(S&OP)-Meetings — nicht weil das zugrunde liegende Nachfragesignal wirklich unsicher ist, sondern weil niemand eine konsistente Methode zur Abstimmung der beiden Ebenen festgelegt hat. Manager verbringen Stunden damit, zu debattieren, welche Zahl „richtig" ist, statt Entscheidungen zu treffen.

Hierarchische Prognose eliminiert diese strukturelle Inkonsistenz von Grund auf.

---

## Die Hierarchie: Ebenen und ihr Zweck

Eine typische Getränke-Nachfragehierarchie hat drei bis fünf Ebenen:

- **Gesamtportfolio** — die Zahl, die in die Finanzplanung und Unternehmenszusagen einfließt
- **Markenfamilie** — die Zahl, die Markeninvestitionsentscheidungen und kommerzielle Ziele antreibt
- **SKU × Kanal** — die Zahl, die die Produktionsplanung und Bestandspositionierung antreibt
- **SKU × Kanal × Region** — die Zahl, die Distributions- und Außendienstziele antreibt (relevant für größere Brauereien mit landesweiter Präsenz)

Jede Ebene dient einem anderen Entscheider mit anderen Planungshorizonten. Gesamtportfolio-Prognosen werden jährlich fixiert, mit vierteljährlichen Aktualisierungen. SKU-Prognosen aktualisieren sich in den meisten modernen Lieferketten wöchentlich.

Die Hierarchie muss explizit definiert werden, bevor irgendeine Abstimmungsmethode angewendet wird. Mehrdeutigkeit darüber, wo alkoholfreies Bier in der Hierarchie sitzt — ist es eine Markenfamilie, eine Submarke eines bestehenden Lagers oder ein eigener Kategorieknoten? — verursacht hartnäckige Abstimmungsfehler.

---

## Abstimmungsmethoden: Bottom-up, Top-down und optimal

**Bottom-up (BU):** Erzeuge SKU-Prognosen unabhängig, dann summiere zu Marke und Portfolio. Vorteil: erfasst SKU-Signale gut. Risiko: Die Portfoliosumme kann makroökonomischen oder Marktanteilserwartungen widersprechen.

**Top-down (TD):** Erzeuge eine Portfolioprognose, dann disaggregiere mithilfe historischer Anteilsproportionen. Vorteil: respektiert Makrobeschränkungen. Risiko: verliert SKU-Genauigkeit, besonders für schnell wachsende oder schnell schrumpfende einzelne SKUs.

**Optimale Abstimmung (MinT / ERM):** Eine Familie von Methoden, die Prognosen auf allen Ebenen unabhängig erzeugt und dann einen Satz abgestimmter Prognosen findet, der den gesamten Prognosefehler über die Hierarchie hinweg minimiert, während die Summierungsbedingungen durchgesetzt werden. Die akademische Forschung des letzten Jahrzehnts hat festgestellt, dass optimale Abstimmung sowohl reine BU- als auch reine TD-Ansätze auf echten kommerziellen Datensätzen konsistent übertrifft.

Für die meisten Getränkeplanungsteams ist der praktische Ausgangspunkt eine gut implementierte BU-Prognose mit einer manuellen Top-down-Beschränkung auf Portfolioebene — ein „beschränktes BU". Vollständige optimale Abstimmung erfordert statistisches Werkzeug und saubere Daten über alle Ebenen gleichzeitig, ist aber mit modernen Prognoseplattformen erreichbar.

---

## Alkoholfreies Bier in der Hierarchie

Alkoholfreies Bier schafft eine spezifische hierarchische Herausforderung: Es hat starke Top-down-Signale (die alkoholfreie Kategorie wächst, und Kategoriewachstumsraten sind beobachtbar), aber schwache Bottom-up-Signale (einzelne SKUs haben begrenzte Historie). Das ist die Umkehrung einer reifen Lager-SKU, die zuverlässige Bottom-up-Historie, aber begrenztes differenziertes Top-down-Signal hat.

Die natürliche Lösung ist es, das Informationsgewicht je Knoten in der Hierarchie variieren zu lassen. Für alkoholfreie SKUs sollte die Top-down-Kategoriewachstumsrate in der abgestimmten Prognose mehr Gewicht erhalten. Für reife Lager-SKUs sollte die Bottom-up-Zeitreihenschätzung dominieren. Hierarchische Rahmen, die mit expliziter Gewichtung nach Ebenenreife entworfen sind, handhaben dies sauber.

Das verbindet sich auch mit dem Analogie-Prognoseansatz für Neuprodukteinführungen, der in [Prognose ohne Historie: Das Problem des alkoholfreien Biers]({{ '/de/2025/forecasting-new-products-na-beer/' | relative_url }}) besprochen wird — die analogiebasierte alkoholfreie Prognose kann als Knoten mit expliziter hoher Unsicherheit in die Hierarchie eingefügt werden, sodass die Abstimmung sie entsprechend behandeln kann.

---

## Genauigkeitsberichterstattung über die Hierarchie hinweg

Ein häufiger Fehler ist, die Prognosegenauigkeit nur auf der Ebene zu messen, auf der die Prognose am leichtesten zu erstellen ist — typischerweise der Marken- oder Gesamtportfolioebene — während die SKU-Prognose, die die tatsächlichen Lieferentscheidungen antreibt, ungemessen bleibt.

Genauigkeitsmetriken sollten auf jeder Ebene der Hierarchie berichtet werden, und die Metriken sollten für den Entscheidungseinsatz jeder Ebene angemessen sein. Mehr dazu, welche Genauigkeitsmetriken man verwenden und welche man verwerfen sollte, siehe [Prognosegenauigkeitsmetriken, die zählen]({{ '/de/2026/forecast-accuracy-metrics/' | relative_url }}).

---

## Der ehrliche Vorbehalt

Hierarchische Prognose ist technisch überzeugend, aber organisatorisch anspruchsvoll. Die Methode verlangt, dass sich alle Beteiligten auf die Hierarchiedefinition einigen, dass Daten auf jeder Ebene konsistent gekennzeichnet sind und dass die abgestimmte Prognose — statt der bevorzugten Zahl irgendeiner einzelnen Ebene — diejenige ist, die tatsächlich Entscheidungen antreibt. In Organisationen, in denen Vertriebs- und Lieferteams historisch ihre eigenen Prognosen verteidigt haben, erfordert dies ebenso Change Management wie statistische Methodik.

*Teil des Tracks Absatzprognose — [alle durchsehen]({{ '/de/tags/' | relative_url }}#forecasting).*

---

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">PROGNOSE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Hierarchische Prognose: SKU-, Marken- und Gesamtvolumen abstimmen</text><g stroke="#06483f" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#00695c" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#00695c" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#06483f" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">heute</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">Historie</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">Prognose</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist hierarchische Prognose?**  
Hierarchische Prognose ist eine Methode zur Erstellung von Prognosen auf mehreren Aggregationsebenen — SKU, Marke, Kategorie, Gesamtportfolio — bei gleichzeitiger Sicherstellung, dass sie mathematisch konsistent sind. Eine Bottom-up-SKU-Prognose, die sich auf mehr summiert als das Top-down-Portfolioziel, ist ein häufiger und kostspieliger Fehlermodus, den diese Methode verhindern soll.

**Was ist der Unterschied zwischen Bottom-up- und Top-down-Prognose bei Getränken?**  
Bottom-up-Prognose beginnt auf der SKU-Ebene und summiert nach oben. Top-down beginnt auf der Ebene des Gesamtportfolios oder Marktanteils und teilt nach unten zu. Jede hat blinde Flecken: Bottom-up kann Makrobeschränkungen verfehlen; Top-down kann SKU-Genauigkeit verlieren. Hierarchische Methoden kombinieren beides mithilfe von Abstimmungsalgorithmen.

**Wie verändert die Einführung eines alkoholfreien Biers die Hierarchie?**  
Eine neue alkoholfreie SKU führt einen Zweig in die Hierarchie ein, der womöglich mehr Top-down-Marktkontext (Kategoriewachstumsraten) als Bottom-up-Daten hat (sie hat keine Historie). Hierarchische Modelle handhaben das elegant, indem sie das Top-down-Signal den alkoholfreien Knoten dominieren lassen, während das Bottom-up-Signal reife SKUs in derselben Markenfamilie verankert.
