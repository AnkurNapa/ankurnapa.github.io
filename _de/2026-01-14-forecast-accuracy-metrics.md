---
layout: post
lang: de
title: "Prognosegenauigkeits-Kennzahlen, die zählen (und die Vanity-Kennzahlen, die wegmüssen)"
image: /assets/og/forecast-accuracy-metrics.png
description: "Welche Prognosegenauigkeits-Kennzahlen tatsächlich bessere Getränkeplanungsentscheidungen antreiben — MAPE, WMAPE, Bias, CFE — und welche schmeicheln, aber in die Irre führen."
date: 2026-01-14
updated: 2026-01-14
permalink: /de/2026/forecast-accuracy-metrics/
tags: [forecasting, forecast-accuracy-metrics]
faq:
  - q: "Was ist die beste Prognosegenauigkeits-Kennzahl für die Bedarfsplanung beim Bier?"
    a: "Es gibt keine einzelne beste Kennzahl — die richtige Wahl hängt von der unterstützten Entscheidung ab. WMAPE (gewichteter mittlerer absoluter prozentualer Fehler) ist die am weitesten verbreitete operative Kennzahl für die Versorgungsplanung auf SKU-Ebene, weil sie hochvolumige SKUs naturgemäß stärker gewichtet. Bias (oder CFE, kumulativer Prognosefehler) ist ebenso wichtig, weil ein Modell mit geringem Fehler, das durchgängig in eine Richtung falsch liegt, systematische Bestandsungleichgewichte erzeugt."
  - q: "Warum ist MAPE eine problematische Prognosegenauigkeits-Kennzahl?"
    a: "MAPE (mittlerer absoluter prozentualer Fehler) ist in Prozenten symmetrisch, aber in der Geschäftswirkung asymmetrisch, wenn er auf niedrigvolumige SKUs angewandt wird. Eine SKU, die 10 Kisten pro Woche verkauft und für die du 5 prognostizierst, erzeugt einen 50%-Fehler; 15 zu prognostizieren erzeugt ebenfalls einen 50%-Fehler — aber die Lieferkettenfolgen sind sehr verschieden. MAPE bricht auch zusammen, wenn die Istwerte nahe null liegen, was bei neuen oder saisonalen SKUs häufig ist."
  - q: "Wie sollte die Prognosegenauigkeit für ein Portfolio alkoholfreien Biers mit neuen SKUs berichtet werden?"
    a: "Neue NA-SKUs sollten getrennt von reifen SKUs berichtet werden, mit absolutem Fehler (Kisten oder Einheiten) statt prozentualem Fehler, angesichts der geringen Mengen in frühen Perioden. Die Genauigkeit neuer Produkte in eine MAPE-Berechnung zu mischen, die hochvolumige reife SKUs enthält, verschleiert die Leistung in beide Richtungen."
---

**Kurze Antwort:** Die meisten Getränkeunternehmen messen die Prognosegenauigkeit mit MAPE, berichten die Zahl im S&OP und treffen damit keine Entscheidungen. Die Kennzahlen, die tatsächlich bessere Planung antreiben — Bias-Erkennung, volumengewichteter Fehler und Verknüpfung mit dem Servicegrad — werden seltener genutzt, sind aber weit handlungsfähiger. Ein kurzer, bewusster Genauigkeitsrahmen schlägt ein langes Dashboard aus Vanity-Statistiken.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Die Betriebsschleife, die dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DIE BETRIEBSSCHLEIFE</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Prognosegenauigkeits-Kennzahlen, die zählen (und die Vanity-Kennzahlen, die wegmüssen)</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">den Ausschank verändern</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Die Betriebsschleife, die dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Das Problem mit MAPE als Standard

MAPE (mittlerer absoluter prozentualer Fehler) wurde weitgehend deshalb zur Standardkennzahl für Prognosegenauigkeit, weil er intuitiv ist: "wir lagen im Schnitt 12 % daneben" ist leicht zu kommunizieren. Aber MAPE hat gut dokumentierte strukturelle Schwächen, die ihn zu einer schlechten primären Kennzahl für die Getränkeversorgungsplanung machen:

- **Unendliche oder instabile Werte nahe null.** Saisonale oder neu eingeführte SKUs mit nahezu null Volumen in bestimmten Perioden erzeugen extreme MAPE-Werte, die portfolioweite Mittelwerte verzerren.
- **Asymmetrische Geschäftsfolgen.** Eine 20%-Überprognose und eine 20%-Unterprognose haben identische MAPE-Wirkung, aber gegenteilige Lieferketteneffekte — eine erzeugt Überbestand, die andere erzeugt Fehlbestände. MAPE ist blind für die Richtung.
- **Aufblähung durch niedrigvolumige SKUs.** Ungewichteter MAPE gibt einer SKU mit 10 Kisten pro Woche denselben Beitrag zum Mittelwert wie einer SKU mit 10.000 Kisten pro Woche. Das Ergebnis ist eine Schlagzeilen-Genauigkeitszahl, die die Leistung bei den am wenigsten kommerziell wichtigen Artikeln widerspiegelt.

Keiner dieser Mängel bedeutet, dass MAPE nutzlos ist. Für eine einzelne SKU mit stabilem, mittlerem Volumen ist er ein vernünftiges Fehlermaß. Das Problem ist, ihn als primäre portfolioweite Kennzahl im S&OP-Reporting zu verwenden.

---

## Die Kennzahlen, die Entscheidungen antreiben

**WMAPE (gewichteter mittlerer absoluter prozentualer Fehler).** Gewichtet absolute Fehler nach dem Istvolumen und stellt sicher, dass hochvolumige SKUs die Portfolio-Kennzahl dominieren. Das richtet das Genauigkeitsmaß an der kommerziellen und versorgungsbezogenen Bedeutung aus. Die meisten Planungsteams, die von MAPE auf WMAPE umsteigen, stellen fest, dass sich ihre Schlagzeilen-Genauigkeitszahlen erheblich ändern — meist verschlechtern sie sich, weil es schwerer wird, schlechte Leistung bei wichtigen SKUs hinter guter Leistung bei kleinen zu verstecken.

**Bias / CFE (kumulativer Prognosefehler).** Verfolgt, ob die Prognose über die Zeit durchgängig zu hoch oder durchgängig zu niedrig liegt. Ein Modell mit null Durchschnittsfehler, aber durchgängiger Überprognose im Sommer und Unterprognose im Winter hat ein Bias-Problem, das MAPE nicht aufdecken wird. CFE = Summe von (Prognose minus Ist) über einen rollierenden Zeitraum. Ein anhaltend positiver CFE signalisiert systematische Überprognose; negativer CFE signalisiert Unterprognose. Beide erzeugen strukturelle Bestandsprobleme.

**Tracking Signal.** Eine normalisierte Version des CFE, die markiert, wenn der kumulative Fehler eine Schwelle überschreitet — typischerweise ±4 bis ±6 — und eine Überprüfung des zugrunde liegenden Prognosemodells auslöst. Das ist der operative Mechanismus, der die Bias-Erkennung in eine Modellintervention umwandelt.

**Verknüpfung mit dem Servicegrad.** Letztlich besteht der Zweck einer genauen Bedarfsprognose darin, einen Servicegrad zu unterstützen — Lieferbereitschaftsgrad, Regalverfügbarkeit oder Kistenlieferquote an Einzelhändler. Die Prognosegenauigkeit losgelöst von tatsächlichen Service-Ergebnissen zu berichten misst eine Eingabe statt das Resultat. Eine Brauerei, die bei einem WMAPE von 15 % eine Kistenlieferquote von 95 % erreicht, hat ein anderes Problem als eine, die bei einem WMAPE von 15 % eine Quote von 80 % erreicht: Das Verhältnis zwischen Prognosefehler und Servicegrad sagt dir, ob der Versorgungspuffer korrekt dimensioniert ist.

---

## Berichten über die Portfolio-Hierarchie hinweg

Genauigkeitskennzahlen sollten die Prognosehierarchie spiegeln. Wie in [Hierarchische Prognose: SKU-, Marken- und Gesamtvolumen abstimmen]({{ '/de/2025/hierarchical-forecasting-beverage/' | relative_url }}) behandelt, werden Entscheidungen auf mehreren Aggregationsebenen getroffen — und die Genauigkeit sollte auf jeder gemessen und berichtet werden.

Ein häufiger Fehlermodus ist, die Genauigkeit nur auf Marken- oder Gesamtportfolioebene zu messen, wo Aggregation Fehler naturgemäß glättet. Die Genauigkeit auf SKU-Ebene sollte getrennt berichtet werden und ist typischerweise 30–50 % schlechter als die Genauigkeit auf Markenebene — eine Lücke, die den echten Informationsgehalt auf jeder Ebene widerspiegelt und die die Sicherheitsbestandspolitik und die Anforderungen an die Produktionsflexibilität informieren sollte.

---

## NA-Bier und die Genauigkeit neuer Produkte

Für alkoholfreies Bier und andere neu eingeführte SKUs sind prozentbasierte Kennzahlen in den ersten 12 Monaten oft ungeeignet. Der absolute Fehler (Kisten oder äquivalente Einheiten) ist nützlicher:

- Er ist stabil, selbst wenn die tatsächlichen Verkaufsmengen klein sind.
- Er verbindet sich direkt mit der Bestandswirkung.
- Er erzwingt ein sinnvolles Gespräch darüber, ob ein 200-Kisten-Fehler bei einer 1.000-Kisten-Prognose akzeptabel ist, statt sich hinter "20 % MAPE" zu verstecken, das unabhängig vom Maßstab gleichwertig klingt.

Die Genauigkeit neuer SKUs sollte auf einem separaten Dashboard verfolgt werden, mit ausdrücklichem Eingeständnis, dass die analogiebasierten oder bayesschen Methoden, die für die Prognose neuer Produkte verwendet werden (siehe [Prognose ohne Historie: Das Problem des alkoholfreien Biers]({{ '/de/2025/forecasting-new-products-na-beer/' | relative_url }})), höhere Fehler produzieren als reife SKU-Modelle — und dass dies erwartet wird, kein Versagen.

---

## Die Falle des Genauigkeits-Reportings

Es gibt eine subtile, aber wichtige Unterscheidung zwischen dem Messen der Genauigkeit, um die Prognose zu verbessern, und dem Messen der Genauigkeit, um eine Zahl zu berichten. Letzteres ist überraschend häufig: Genauigkeitskennzahlen werden zu KPIs, die für die Optik statt für die Erkenntnis verwaltet werden.

Anzeichen der Reporting-Falle: Die Genauigkeit wird nur für die Perioden nach dem letzten großen Fehler berechnet; niedrigvolumige SKUs werden ohne dokumentierte Begründung aus der Berechnung ausgeschlossen; die Genauigkeitskennzahl bewegt sich im Gleichschritt mit dem Volumenwachstum (weil hochvolumige SKUs leichter zu prognostizieren sind), wird aber als methodische Verbesserung interpretiert.

Das Gegenmittel ist, die Methodik der Genauigkeitsmessung einmal zu definieren, sie zu dokumentieren und sie konsistent über Perioden, SKUs und Planungszyklen hinweg anzuwenden — einschließlich derer, in denen die Leistung schlecht war.

---

## Der ehrliche Vorbehalt

Keine Genauigkeitskennzahl, so gut sie auch entworfen ist, sagt dir, ob die Prognose für die Entscheidung, die sie unterstützt, gut genug ist. Ein WMAPE von 25 % mag für eine margenschwache saisonale SKU mit hoher Versorgungsflexibilität völlig akzeptabel sein; er mag für ein margenstarkes Produkt mit langer Vorlaufzeit disqualifizierend sein. Genauigkeitsziele nach SKU-Klasse, Vorlaufzeit und Margenprofil zu kontextualisieren ist die Arbeit, die ein Kennzahl-Dashboard in ein Planungswerkzeug verwandelt.

*Teil des Tracks Sales Forecasting — [alle durchsehen]({{ '/de/tags/' | relative_url }}#forecasting).*

---

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">PROGNOSE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Prognosegenauigkeits-Kennzahlen, die zählen (und die Vanity-Kennzahlen, die wegmüssen)</text><g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#b45309" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#b45309" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#7a1f3d" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">heute</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Historie</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">Prognose</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist die beste Prognosegenauigkeits-Kennzahl für die Bedarfsplanung beim Bier?**  
Es gibt keine einzelne beste Kennzahl — die richtige Wahl hängt von der unterstützten Entscheidung ab. WMAPE (gewichteter mittlerer absoluter prozentualer Fehler) ist die am weitesten verbreitete operative Kennzahl für die Versorgungsplanung auf SKU-Ebene, weil sie hochvolumige SKUs naturgemäß stärker gewichtet. Bias (oder CFE, kumulativer Prognosefehler) ist ebenso wichtig, weil ein Modell mit geringem Fehler, das durchgängig in eine Richtung falsch liegt, systematische Bestandsungleichgewichte erzeugt.

**Warum ist MAPE eine problematische Prognosegenauigkeits-Kennzahl?**  
MAPE (mittlerer absoluter prozentualer Fehler) ist in Prozenten symmetrisch, aber in der Geschäftswirkung asymmetrisch, wenn er auf niedrigvolumige SKUs angewandt wird. Eine SKU, die 10 Kisten pro Woche verkauft und für die du 5 prognostizierst, erzeugt einen 50%-Fehler; 15 zu prognostizieren erzeugt ebenfalls einen 50%-Fehler — aber die Lieferkettenfolgen sind sehr verschieden. MAPE bricht auch zusammen, wenn die Istwerte nahe null liegen, was bei neuen oder saisonalen SKUs häufig ist.

**Wie sollte die Prognosegenauigkeit für ein Portfolio alkoholfreien Biers mit neuen SKUs berichtet werden?**  
Neue NA-SKUs sollten getrennt von reifen SKUs berichtet werden, mit absolutem Fehler (Kisten oder Einheiten) statt prozentualem Fehler, angesichts der geringen Mengen in frühen Perioden. Die Genauigkeit neuer Produkte in eine MAPE-Berechnung zu mischen, die hochvolumige reife SKUs enthält, verschleiert die Leistung in beide Richtungen.
