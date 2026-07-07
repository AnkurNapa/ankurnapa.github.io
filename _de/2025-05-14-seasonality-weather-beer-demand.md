---
layout: post
lang: de
title: "Saisonalität und Wetter: Biers vorhersagbarste Schwankungen"
image: /assets/og/seasonality-weather-beer-demand.png
description: "Wie Wetter und Saisonalität die Bedarfsprognose für Bier treiben — Zerlegungsmethoden, Temperaturindizes und was sich bei alkoholfreiem Bier ändert."
date: 2025-05-14
updated: 2025-05-14
permalink: /de/2025/seasonality-weather-beer-demand/
tags: [forecasting, weather-demand-forecasting]
faq:
  - q: "Wie stark beeinflusst das Wetter den Bierabsatz tatsächlich?"
    a: "Temperatur und Sonnenschein gehören zu den stärksten kurzfristigen Treibern des Biervolumens — besonders bei Anlässen im Off-Premise und im Außenbereich des On-Premise. Der Effekt ist über Märkte hinweg richtungsmäßig gut dokumentiert, auch wenn die genaue Größenordnung je nach Marke, Kanal und Region variiert."
  - q: "Wie trennt man Saisonalität von einem zugrunde liegenden Trend in einer Bierprognose?"
    a: "Die Zeitreihenzerlegung (z. B. STL oder klassische multiplikative Zerlegung) teilt eine Bedarfsreihe in Trend-, Saison- und Restkomponenten. Die Saisonkomponente erfasst das sich wiederholende Kalendermuster; der Trend erfasst das zugrunde liegende Wachstum oder den Rückgang; im Rest zeigen sich Aktionen, Wetteranomalien und einmalige Ereignisse."
  - q: "Folgt alkoholfreies Bier demselben Saisonmuster wie konventionelles Bier?"
    a: "Teilweise. Alkoholfreies Bier teilt den sommerlichen Aufschwung der Außenanlässe, zeigt aber tendenziell eine zweite Spitze im Januar rund um den Dry January und wellnessmotivierte Abstinenzphasen — ein Muster, das konventionelles Bier nicht aufweist. Planer sollten die Saisonalität von alkoholfreiem Bier separat modellieren, statt anzunehmen, sie spiegele Lager wider."
---

**Kurze Antwort:** Saisonalität ist der am besten modellierbare Treiber im Bierbedarf — sie ist wiederkehrend, quantifizierbar und in jedem ausgereiften Datensatz sichtbar. Das Wetter fügt eine sekundäre Schicht kurzfristiger Variabilität hinzu. Zusammen machen sie einen großen Anteil der vorhersagbaren Varianz im Biervolumen aus, was sie zu den Signalen mit dem höchsten ROI macht, die man in jedes Prognosemodell einbetten kann. Alkoholfreies Bier teilt das Sommermuster, fügt aber eine charakteristische Januar-Spitze hinzu, die konventionellem Bier fehlt.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Die Betriebsschleife, die dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DIE BETRIEBSSCHLEIFE</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Saisonalität und Wetter: Biers vorhersagbarste Schwankungen</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">die Halle verändern</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die Betriebsschleife, die dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Warum Saisonalität das Fundament ist, keine Verfeinerung

Die Bedarfsprognose bei Getränken behandelt Saisonalität oft als Anpassung, die angewandt wird, nachdem die „eigentliche" Prognose erstellt ist. Diese Sichtweise ist verkehrt herum. Für die meisten Bier-SKUs erklärt die Saisonkomponente den Großteil der Volumenschwankung von Woche zu Woche. Ein Modell, das die Saisonalität zuerst herauslöst — und den entsaisonalisierten Trend separat prognostiziert — wird eines, das versucht, das Rohvolumen direkt zu prognostizieren, dramatisch übertreffen.

Die praktische Konsequenz: Jede Brauerei oberhalb der Reifestufe 1 (siehe [Das Reifegradmodell der Getränke-Bedarfsprognose]({{ '/de/2025/demand-forecasting-maturity-model/' | relative_url }})) sollte die saisonale Zerlegung umsetzen, bevor sie irgendeine andere Prognose-Raffinesse hinzufügt.

---

## Das Signal zerlegen: STL und seine Varianten

STL (Seasonal and Trend decomposition using Loess) ist die Arbeitspferd-Methode für die Getränke-Saisonalität. Sie bietet mehrere Vorteile gegenüber der klassischen Zerlegung:

- **Robustheit gegenüber Ausreißern.** Aktionsspitzen, Lieferengpässe und Verzerrungen aus der COVID-Ära werden als Reste behandelt, statt die Saisonschätzung zu verzerren.
- **Flexible Saisonfenster.** Bier kann sowohl ein wöchentliches Muster (Freitag-Samstag-Aufschwung im On-Premise) als auch ein jährliches Muster (Sommerspitze, Q4-Feiertagsanstieg) haben. STL bewältigt mehrere Periodizitäten.
- **Aktualisierbar.** Anders als klassische Methoden, die ein volles Jahr Historie zur Neuschätzung benötigen, können STL-Saisonschätzungen schrittweise aktualisiert werden, wenn neue Daten eintreffen.

Ein praktischer Ausgangspunkt für ein regionales Lager-SKU: Zerlege drei bis fünf Jahre wöchentlicher Abverkaufsdaten, inspiziere die Saisonkomponente visuell und bestätige, dass sie über die Jahre stabil ist, bevor du annimmst, dass sie sich wiederholt. Wenn die Saisonform sich verschiebt — wie es bei Marken mit sich ändernder Distribution oder einer wachsenden On-Trade-Präsenz der Fall sein kann —, ist ein Modell vorzuziehen, das der Saisonkomponente erlaubt, sich von Jahr zu Jahr zu entwickeln.

---

## Wetter als Treiber: nützlich, aber kein Ersatz für den Prozess

Temperatur und Sonnenstunden sind echte Bedarfstreiber für Bier, besonders in den Kanälen Off-Premise und Außenbereich On-Premise. Der Mechanismus ist intuitiv: Warmes Wetter erhöht Häufigkeit und Umfang informeller Konsumanlässe im Freien.

Einen Temperaturindex zu einer regressionsbasierten Prognose hinzuzufügen, kann die kurzfristige Genauigkeit verbessern, besonders in den Übergangssaisons (April–Mai, September–Oktober), wenn Vorjahresvergleiche am verrauschtesten sind. Der praktische Ansatz:

1. Beschaffe historische tägliche Temperaturdaten für die Schlüsselmärkte im Distributionsgebiet.
2. Aggregiere zu wöchentlichen „Kühlgradtagen" oder einem einfachen Temperaturindex über einem Schwellenwert.
3. Nimm den Index als Merkmal in eine treiberbasierte Regression auf, neben Distribution, Aktionskennzeichen und Zeittrend.
4. Verwende beim Erstellen einer Vorausprognose probabilistische Vorhersagen des Wetterdienstes für die nächsten 4–8 Wochen; kehre für längere Horizonte zu Saisonnormen zurück.

**Die Grenzen der Wettermodellierung** verdienen gleiche Aufmerksamkeit. Das Wetter erklärt die Volumenvolatilität innerhalb einer Saison — es erklärt nicht, warum ein Sommer einen anderen um mehr als erwartet übertrifft. Distributionsgewinne, Wettbewerbsdynamik und das makroökonomische Verbrauchervertrauen leisten auf jährlicher Ebene mehr. Das Wetter im Jahresplan überzugewichten, erzeugt ein falsches Gefühl von Präzision.

---

## Alkoholfreies Bier: eine andere Saisonform

Das Saisonprofil von alkoholfreiem Bier weicht in einem wichtigen Punkt von konventionellem Bier ab: der Januar-Spitze. Der Dry January ist in mehreren Schlüsselmärkten zu einem echten Bedarfsereignis geworden, konzentriert auf die ersten drei Wochen des Jahres. Für gut distribuierte alkoholfreie SKUs rivalisiert der Januar inzwischen mit dem Sommer als nachfragestärkste Periode des Kalenderjahres oder übertrifft ihn.

Planer, die einen konventionellen Bier-Saisonindex auf alkoholfreie SKUs anwenden, werden den Januar systematisch unterprognostizieren und den Sommer möglicherweise überprognostizieren. Die Lösung ist unkompliziert, erfordert aber explizite Modellierung: Bau einen separaten Saisonindex für alkoholfreie Linien, statt ihn vom breiteren Portfolio zu erben.

Wettereffekte auf alkoholfreies Bier sind weniger sicher. Der lockere Outdoor-Anlass mit hohem ABV ist für die Motivation des alkoholfreien Käufers weniger zentral. Es ist mehr Forschung nötig, bevor man alkoholfreiem Bier zuversichtlich dieselbe Temperaturempfindlichkeit zuschreibt, die konventionelles Lager aufweist.

---

## Der ehrliche Vorbehalt

Saisonmodelle sind nur so gut wie die Historie, auf der sie aufbauen. Wenn die vergangenen drei Jahre eine Pandemie, eine Distributionsumstrukturierung oder einen großen Wettbewerbseintritt umfassten, wird die vom Modell extrahierte „saisonale" Komponente Artefakte aus diesen Ereignissen enthalten. Die visuelle Inspektion der Zerlegungsergebnisse — nicht nur statistische Anpassungsmaße — ist eine wesentliche Qualitätsprüfung, bevor ein Saisonmodell in die Produktionsplanung gestellt wird.

*Teil des Tracks Sales Forecasting — [alle durchsehen]({{ '/de/tags/' | relative_url }}#forecasting).*

---

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Historie (durchgezogen) und die Vorausprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">PROGNOSE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Saisonalität und Wetter: Biers vorhersagbarste Schwankungen</text><g stroke="#06483f" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#00695c" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#00695c" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#06483f" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">heute</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">Historie</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">Prognose</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Historie (durchgezogen) und die Vorausprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit.</figcaption>
</figure>

## Häufig gestellte Fragen

**Wie stark beeinflusst das Wetter den Bierabsatz tatsächlich?**  
Temperatur und Sonnenschein gehören zu den stärksten kurzfristigen Treibern des Biervolumens — besonders bei Anlässen im Off-Premise und im Außenbereich des On-Premise. Der Effekt ist über Märkte hinweg richtungsmäßig gut dokumentiert, auch wenn die genaue Größenordnung je nach Marke, Kanal und Region variiert.

**Wie trennt man Saisonalität von einem zugrunde liegenden Trend in einer Bierprognose?**  
Die Zeitreihenzerlegung (z. B. STL oder klassische multiplikative Zerlegung) teilt eine Bedarfsreihe in Trend-, Saison- und Restkomponenten. Die Saisonkomponente erfasst das sich wiederholende Kalendermuster; der Trend erfasst das zugrunde liegende Wachstum oder den Rückgang; im Rest zeigen sich Aktionen, Wetteranomalien und einmalige Ereignisse.

**Folgt alkoholfreies Bier demselben Saisonmuster wie konventionelles Bier?**  
Teilweise. Alkoholfreies Bier teilt den sommerlichen Aufschwung der Außenanlässe, zeigt aber tendenziell eine zweite Spitze im Januar rund um den Dry January und wellnessmotivierte Abstinenzphasen — ein Muster, das konventionelles Bier nicht aufweist. Planer sollten die Saisonalität von alkoholfreiem Bier separat modellieren, statt anzunehmen, sie spiegele Lager wider.
