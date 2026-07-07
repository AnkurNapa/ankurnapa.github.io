---
layout: post
lang: de
title: "On-Premise- vs. Off-Premise-Intelligence: Zwei Spiele, ein Portfolio"
image: /assets/og/on-premise-off-premise-intelligence.png
description: "On-Premise- und Off-Premise-Daten erfordern zwei unterschiedliche analytische Rahmen — so bauen Getränkemarken Intelligence für beide Kanäle, ohne ihren Aufwand zu verdoppeln."
date: 2025-10-06
updated: 2025-10-06
permalink: /de/2025/on-premise-off-premise-intelligence/
tags: [sales-intelligence, channel-strategy]
faq:
  - q: "Was ist der zentrale Unterschied zwischen On-Premise- und Off-Premise-Daten?"
    a: "Off-Premise-Daten (Einzelhandel) sind strukturierter und verfügbarer — Scannerdaten, Regalanteilsberichte und Händler-POS sind relativ zugänglich. On-Premise-Daten (Bars, Restaurants) sind fragmentiert und weitgehend selbstgemeldet, was sie schwerer aggregierbar, aber oft wertvoller für markenbildende Signale macht."
  - q: "Welcher Kanal zählt mehr für den Launch eines neuen Biers oder einer NA-Biermarke?"
    a: "On-Premise ist für Neueinführungen im Allgemeinen der stärkere markenbildende Kanal — Accounts bieten Verkostungsgelegenheiten, Personal-Fürsprache und sichtbare Markenpräsenz, die Off-Premise-Probierkäufe antreiben. Off-Premise-Volumen ist jedoch der Ort, an dem Marken den Umsatz halten, sobald der Probierkauf etabliert ist."
  - q: "Wie misst man die On-Premise-Leistung ohne zuverlässige POS-Daten?"
    a: "Stellvertreter-Kennzahlen sind die praktische Alternative: Depletion-Geschwindigkeit auf Account-Ebene (aus Distributordaten), Menüplatzierung (verfolgt über periodische Audits oder Außendienstbesuche) und Anzahl der Zapfhähne bei Fassprodukten. Keine ist perfekt, aber zusammen nähern sie sich dem Leistungssignal an, das POS-Daten direkt liefern würden."
---

**Kurze Antwort:** On-Premise und Off-Premise sind keine Varianten desselben Spiels — sie sind strukturell unterschiedliche Kanäle, die unterschiedliche Daten, unterschiedliche Erfolgskennzahlen und unterschiedliche Investitionslogik erfordern. Marken, die einen einzigen Analytics-Rahmen auf beide anwenden, lesen die Leistung durchweg falsch und allozieren Vertriebsressourcen falsch.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">On-Premise- vs. Off-Premise-Intelligence: Zwei Spiele, ein Portfolio</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">den Betrieb anpassen</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Warum dieselben Kennzahlen nicht für beide Kanäle funktionieren

Off-Premise (Einzelhandel) begünstigt Volumen, Geschwindigkeit und Regalanteil. Die Frage ist, wie schnell sich ein Produkt über eine SKU in einer definierten Menge von Geschäften bewegt. Daten sind relativ verfügbar — Einzelhandels-POS, Scannerdatendienste und Lieferungen auf Geschäftsebene liefern ein einigermaßen klares Bild.

On-Premise (Bars, Restaurants, Veranstaltungsorte) arbeitet auf gänzlich anderer Ökonomie. Das Volumen je Account ist geringer, aber der markenbildende Wert ist höher. Eine Listung im richtigen, gut sichtbaren Restaurant kann den Probierkauf der Verbraucher und in der Folge den Off-Premise-Sog beeinflussen. Die Datenumgebung ist auch strukturell trüber — es gibt keinen konsistenten On-Premise-POS-Aggregator für den Getränkehandel auf der Ebene einer Regionalbrauerei.

Alkoholfreies Bier fügt weitere Komplexität hinzu. NA-Bier ist in seinen frühen Distributionsphasen überproportional auf On-Premise indexiert, weil Restaurants und Bars einen konkreten Bedarf an glaubwürdigen alkoholfreien Optionen auf ihren Karten haben. Die markenbildende Logik der On-Premise-Platzierung ist für NA besonders stark — Verbraucher entdecken NA-Optionen in geselligen Umgebungen, wo sie sie ohne die Verbindlichkeit eines Einzelhandelskaufs probieren können.

## Der Off-Premise-Intelligence-Rahmen

Off-Premise-Analytics für Getränke dreht sich um drei Fragen:

**1. Geschwindigkeit je Distributionspunkt (POD)**: Gesamt-Depletions geteilt durch aktive Einzelhandels-Accounts in der Periode. Das normalisiert das Volumen für die Distributionsbreite — eine Marke in 50 Geschäften, die 200 Kartons verkauft, übertrifft eine in 200 Geschäften, die 300 Kartons verkauft, und die Geschwindigkeit je POD macht das deutlich.

**2. Regalanteil vs. Wettbewerbsset**: Welchen Prozentsatz des linearen Regalplatzes oder der SKU-Frontansichten hält deine Marke relativ zur Kategorie? Im Filialeinzelhandel schaffen Regal-Resets strukturelle Chancen und Risiken, die Geschwindigkeitsdaten allein nicht erfassen.

**3. Aktionshebel und -effizienz**: Wenn Preisaktionen oder Display-Programme laufen, wie viel zusätzliches Volumen erzeugen sie? Marken, die den Aktions-ROI nach Account-Stufe quantifizieren können, gewinnen erheblichen Verhandlungshebel in Planungsgesprächen mit Händlern.

## Der On-Premise-Intelligence-Rahmen

On-Premise-Analytics erfordert andere Stellvertreter, weil direkte POS-Daten selten verfügbar sind:

**1. Menü-Durchdringungsrate**: Welcher Prozentsatz der Ziel-On-Premise-Accounts führt deine Marke auf ihrer Karte oder Zapfliste? Verfolge das über Außendienst-Besuchsprotokolle und periodische Audits. Für NA-Bier verfolge speziell die Platzierung im alkoholfreien Bereich — Präsenz dort signalisiert bewusste Kategorieentwicklung durch den Betreiber.

**2. Zapfhahn-Platzierung und -Verweildauer**: Verfolge bei Fassprodukten die Hahnanzahl (wie viele Accounts einen dedizierten Zapfhahn haben) und die Verweildauer (wie lange jeder Hahn aktiv war). Ein Hahn, der über mehrere Quartale aktiv bleibt, ist ein bedeutsames Signal echten Sogs. Hähne mit kurzer Verweildauer, die schnell wechseln, deuten auf ein Probieren-und-Ablehnen-Muster hin, das es wert ist, untersucht zu werden.

**3. Personal-Fürsprache-Index**: Verfolge in On-Premise-Accounts mit höherer Investition, ob das Servicepersonal das Produkt akkurat beschreiben und empfehlen kann. Das ist eine qualitative Kennzahl, gesammelt durch Außendienstbeobachtung, aber sie ist ein Frühindikator für nachhaltige Geschwindigkeit in erlebnisgetriebenen Lokalen.

## Eine integrierte Sicht bauen

Die Kanäle sind analytisch unterschiedlich, aber kommerziell voneinander abhängig. Ein praktischer Integrationspunkt: Nutze On-Premise-Depletion-Geschwindigkeit und Menü-Durchdringung in gut sichtbaren Accounts als Frühindikator für die Off-Premise-Nachfrage in derselben Geografie. Marken sehen oft einen Anstieg der Off-Premise-Geschwindigkeit in Postleitzahlgebieten, in denen die On-Premise-Präsenz bewusst aufgebaut wurde — und können dieses Signal nutzen, um die Off-Premise-Expansion zu terminieren.

Siehe auch: [Account-Scoring: Deine nächsten 100 Outlets finden]({{ '/de/2025/account-scoring-beverage-sales/' | relative_url }}) dazu, wie der Kanaltyp in die Priorisierung auf Account-Ebene einfließt.

## Wo Channel-Intelligence scheitert

- **On-Premise-Daten sind wirklich schwer richtig zu bekommen**. Distributor-Depletion-Daten auf Account-Ebene sind der beste verfügbare Stellvertreter, aber die Reporting-Qualität der Distributoren für On-Premise-Accounts ist oft weniger zuverlässig als für den Einzelhandel. Behandle On-Premise-Depletion-Daten als richtungsweisend, nicht präzise.
- **Kanal-Attribution ist unsauber**. Zu beweisen, dass On-Premise-Investition den Off-Premise-Hebel angetrieben hat, erfordert kontrollierte Marktanalyse, die die meisten Regionalbrauereien praktisch nicht durchführen können. Behandle die Beziehung als Arbeitshypothese, informiert durch Marktbeobachtung.
- **On-Premise-Benchmarks für NA-Bier werden noch geschrieben**. Wie eine „gute" NA-Bier-Menüplatzierung in Bezug auf Geschwindigkeit, Verweildauer und Personalannahme aussieht, ist eine offene Frage. Dokumentiere deine eigenen Erfahrungen systematisch — deine Daten werden mit zunehmender Reife der Kategorie an Wert gewinnen.

*Teil des Tracks Sales Intelligence — [alle ansehen]({{ '/de/tags/' | relative_url }}#sales-intelligence).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 320" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Zwei Dimensionen, vier Quadranten — wo jedes Element landet, sagt dir, was zu tun ist."><rect x="0" y="0" width="720" height="320" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">2×2-MATRIX</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">On-Premise- vs. Off-Premise-Intelligence: Zwei Spiele, ein Portfolio</text><rect x="180" y="70" width="380" height="210" fill="none" stroke="#d8e6e1" stroke-width="1.5"/><line x1="370.0" y1="70" x2="370.0" y2="280" stroke="#d8e6e1"/><line x1="180" y1="175.0" x2="560" y2="175.0" stroke="#d8e6e1"/><rect x="370.0" y="70" width="190.0" height="105.0" fill="#00695c" opacity="0.12"/><text x="192" y="266" font-family="sans-serif" font-size="12" fill="#4a6b64">niedrig / niedrig</text><text x="382.0" y="94" font-family="sans-serif" font-size="12" fill="#4a6b64">hoher Fokus</text><text x="192" y="94" font-family="sans-serif" font-size="12" fill="#4a6b64">beobachten</text><text x="382.0" y="266" font-family="sans-serif" font-size="12" fill="#4a6b64">halten</text><circle cx="440.0" cy="130" r="6" fill="#00695c"/><circle cx="480.0" cy="160" r="6" fill="#00695c"/><circle cx="420.0" cy="165" r="6" fill="#00695c"/><circle cx="240" cy="225.0" r="6" fill="#00695c"/><circle cx="410.0" cy="235.0" r="6" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Zwei Dimensionen, vier Quadranten — wo jedes Element landet, sagt dir, was zu tun ist.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist der zentrale Unterschied zwischen On-Premise- und Off-Premise-Daten?**
Off-Premise-Daten (Einzelhandel) sind strukturierter und verfügbarer — Scannerdaten, Regalanteilsberichte und Händler-POS sind relativ zugänglich. On-Premise-Daten (Bars, Restaurants) sind fragmentiert und weitgehend selbstgemeldet, was sie schwerer aggregierbar, aber oft wertvoller für markenbildende Signale macht.

**Welcher Kanal zählt mehr für den Launch eines neuen Biers oder einer NA-Biermarke?**
On-Premise ist für Neueinführungen im Allgemeinen der stärkere markenbildende Kanal — Accounts bieten Verkostungsgelegenheiten, Personal-Fürsprache und sichtbare Markenpräsenz, die Off-Premise-Probierkäufe antreiben. Off-Premise-Volumen ist jedoch der Ort, an dem Marken den Umsatz halten, sobald der Probierkauf etabliert ist.

**Wie misst man die On-Premise-Leistung ohne zuverlässige POS-Daten?**
Stellvertreter-Kennzahlen sind die praktische Alternative: Depletion-Geschwindigkeit auf Account-Ebene (aus Distributordaten), Menüplatzierung (verfolgt über periodische Audits oder Außendienstbesuche) und Anzahl der Zapfhähne bei Fassprodukten. Keine ist perfekt, aber zusammen nähern sie sich dem Leistungssignal an, das POS-Daten direkt liefern würden.
