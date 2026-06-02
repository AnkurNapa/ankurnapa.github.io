---
layout: post
lang: de
title: "Vorausschauende Wartung als Sicherheitsstrategie"
image: /assets/og/predictive-maintenance-safety-strategy.png
description: "Wie Programme zur vorausschauenden Wartung in Brauereien anlagenbezogene Vorfälle reduzieren, indem sie das Ausfallrisiko sichtbar machen, bevor ein Defekt oder eine Verletzung eintritt."
date: 2025-12-24
updated: 2025-12-24
permalink: /de/2025/predictive-maintenance-safety-strategy/
tags: [ehs, predictive-maintenance, equipment-safety]
faq:
  - q: "Wie unterscheidet sich vorausschauende Wartung von vorbeugender Wartung?"
    a: "Vorbeugende Wartung ersetzt oder wartet Komponenten nach einem festen Zeitplan, unabhängig vom tatsächlichen Zustand. Vorausschauende Wartung nutzt Zustandsüberwachungsdaten — Vibrations-, Temperatur-, Drucktrends —, um Komponenten zu warten, wenn ihr tatsächlicher Zustand einen bevorstehenden Ausfall anzeigt, und reduziert sowohl ungeplante Stillstände als auch unnötige Eingriffe."
  - q: "Welche Brauereianlagen profitieren am meisten von einem vorausschauenden Wartungsansatz?"
    a: "Kältekompressoren, CO2-Rückgewinnungs- und Speichersysteme, Druckbehälter und ihre Sicherheitsventile, Zentrifugen sowie Antriebe von Hochgeschwindigkeits-Abfülllinien sind typischerweise die wertvollsten Ziele — sie verbinden hohe Ausfallfolgen, messbare Zustandssignale und teure ungeplante Stillstände."
  - q: "Ist vorausschauende Wartung für eine kleine Craft-Brauerei realistisch?"
    a: "Vollständige IoT-getriebene vorausschauende Wartung erfordert Investitionen, die für einen kleinen Betrieb schwer zu rechtfertigen sind. Die zugrunde liegende Disziplin — Anlagenzustandsdaten im Trend verfolgen, Frühindikatoren für Ausfälle nachhalten und Anomalien eskalieren — ist jedoch skalierbar. Mit manueller Zustandsüberwachung an zwei oder drei kritischen Anlagen zu beginnen, ist ein praktischer Einstieg."
---

**Kurze Antwort:** Vorausschauende Wartung ist nicht nur eine Verfügbarkeitsstrategie — sie ist eine Sicherheitsstrategie. Anlagen, die in einer Brauerei unerwartet ausfallen, sind Anlagen, die Arbeiter verletzen, CO2 freisetzen, Druckleitungen aufreißen oder die Systeme (Kühlung, Lüftung) lahmlegen können, die die Anlage sicher halten. Zustandsbasierte Wartung reduziert dieses Risiko, indem Anlagen vor dem Ausfall gewartet werden, nicht danach.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Vorausschauende Wartung als Sicherheitsstrategie</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">den Betrieb ändern</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Das Sicherheitsargument für zustandsbasierte Wartung

Das Standardargument für vorausschauende Wartung ist wirtschaftlich: weniger ungeplante Abschaltungen, geringerer Ersatzteilverbrauch, längere Anlagenlebensdauer. Das Sicherheitsargument wird seltener vorgebracht, ist aber ebenso wichtig.

In einer Brauerei ist unerwarteter Anlagenausfall selten nur eine betriebliche Unannehmlichkeit. Ein Ausfall eines Kältekompressors in einem CO2-Rückgewinnungssystem kann eine gleichzeitige atmosphärische Gefahr schaffen. Ein defektes Sicherheitsventil an einem Gärtank ist ein eingegrenztes Problem, bis der Tank überdrückt wird, und dann nicht mehr. Eine Zentrifuge mit unentdecktem Lagerverschleiß kann bei Drehzahl katastrophal versagen. Die Sicherheits- und Betriebsfolgen dieser Ausfälle sind untrennbar.

Programme zur vorausschauenden Wartung gehen das an, indem sie den Anlagenzustand als Frühindikator für Sicherheit behandeln — ein Signal für sich entwickelndes Risiko, auf das reagiert werden kann, bevor der Ausfall, der Stillstand und die mögliche Verletzung eintreten.

## Das Werkzeugkasten der Zustandsüberwachung

Vorausschauende Wartung stützt sich auf Datenströme, die den Anlagenzustand über die Zeit widerspiegeln. Die relevanten Signale für Brauereianlagen umfassen:

**Vibrationsanalyse**: Die ausgereifteste PdM-Technologie. Auf rotierenden Anlagen (Kompressoren, Pumpen, Zentrifugen, Abfülllinienantriebe) montierte Beschleunigungssensoren erkennen Änderungen der Vibrationssignatur, die mit Lagerverschleiß, Unwucht oder Fehlausrichtung korrelieren. Das Muster ändert sich weit, bevor hörbare Symptome entstehen.

**Thermografie**: Periodische Infrarotscans von Schaltschränken, Motorgehäusen und Rohrverbindungen bringen Hotspots ans Licht, die Widerstandsfehler, Isolationsversagen oder Durchflussbeschränkungen anzeigen. Das ist eine Prüfung mit niedrigerer Frequenz (vierteljährlich oder halbjährlich) statt kontinuierlicher Überwachung.

**Druck- und Temperaturtrends**: Für Druckbehälter, CO2-Speichertanks und Kältekreise schafft kontinuierliche Druck- und Temperaturaufzeichnung eine Basislinie, von der aus Anomalien erkannt werden können. Ein allmählicher Druckabfall in einem CO2-Speichertank über 30 Tage ist ein anderes Signal als ein plötzlicher Abfall — beide zählen, erfordern aber unterschiedliche Reaktionen.

**Ölanalyse**: Für Kompressoren und Getriebe erkennt periodische Schmierstoffanalyse (Partikelzahl, Viskosität, Säuregehalt) inneren Verschleiß, bevor er bis zum Ausfall fortschreitet.

## PdM mit EHS integrieren

Der praktische Integrationspunkt zwischen vorausschauender Wartung und der EHS-Funktion ist der Workflow für Korrekturmaßnahmen. Wenn eine Zustandsüberwachungsanomalie erkannt wird — eine steigende Vibrationssignatur an einer Gärtankpumpe, ein Hotspot an einem CO2-Kompressormotor —, sollte sie eine Korrekturmaßnahme im CMMS erzeugen, die sowohl für die Wartung als auch für den EHS-Manager sichtbar ist. Das schafft eine gemeinsame Aufzeichnung und stellt sicher, dass Sicherheitsimplikationen (z. B. "diese Pumpe sitzt am CO2-Spülkreis des Drucktanks") bei der Priorisierung der Reparatur berücksichtigt werden.

Druckbehälterinspektionen, Sicherheitsventilprüfungen und Sicherheitschecks von Kältesystemen sollten als hochprioritäre PdM-Aufgaben behandelt werden, unabhängig davon, ob die Anlage Zustandsanomalien zeigt, weil ihre Ausfallfolgen schwerwiegend sind und weil regulatorische Anforderungen Mindestinspektionsfrequenzen festlegen. Siehe [Compliance-Analytik: Nie eine Inspektion oder Genehmigung verpassen]({{ '/de/2025/ehs-compliance-analytics/' | relative_url }}) dafür, wie diese Inspektionspflichten in den Compliance-Tracking-Rahmen passen.

## Wo KI und Machine Learning Wert hinzufügen

Machine Learning wird zunehmend auf Vibrations- und Prozessdaten angewandt, um multivariable Anomalien zu erkennen, die regelbasierte Schwellenüberwachung verpasst. Ein auf historische Ausfallereignisse trainiertes ML-Modell kann eine Kombination aus Temperatur-, Vibrations- und Laufzeitmustern identifizieren, die einem bestimmten Ausfallmodus vorangeht, selbst wenn kein einzelner Parameter seinen individuellen Schwellenwert überschreitet.

Voraussetzung ist ausreichend historische Daten — typischerweise mindestens 12–18 Monate an Zustandsüberwachungsaufzeichnungen mit gekennzeichneten bekannten Ausfallereignissen. Für die meisten kleinen und mittelgroßen Brauereien existiert diese Datenhistorie noch nicht, was den Ausgangspunkt zu einem manuellen oder regelbasierten System macht, das den Datensatz aufbaut, statt zu einem ausgefeilten ML-Einsatz.

Die ehrliche Einschränkung: Modelle zur vorausschauenden Wartung sagen dir, wann sich der Zustand einer Anlage in Richtung einer historischen Ausfallsignatur entwickelt. Sie können neuartige Ausfallmodi nicht vorhersagen, Sensordrift ohne Kalibrierungsprogramm nicht korrekt interpretieren oder Anlagen nicht kompensieren, die bereits vor Beginn der Überwachung degradiert waren.

## Loslegen ohne ein vollständiges IoT-Programm

Für Brauereien, die noch nicht bereit sind, in anlagenweite Sensorinfrastruktur zu investieren, ist ein praktischer Ausgangspunkt, zwei oder drei kritische Anlagen auszuwählen — diejenigen, deren Ausfall eine Sicherheitsgefahr schaffen oder die Produktion stoppen würde — und manuelle Zustandsüberwachung umzusetzen: monatliche Vibrationsmessungen mit einem Handmessgerät, vierteljährliche Ölprobenahme und ein Temperaturprotokoll aus dem Kompressorschaltschrank. Die Daten gehen in eine einfache Tabelle mit einem rollierenden Trenddiagramm. Wenn sich der Trend ändert, löst er eine Untersuchung aus. Das ist nicht ausgefeilt, aber es ist eine bedeutende Verbesserung gegenüber dem Warten, bis die Anlage ausfällt.

*Teil des EHS-Tracks — [alle durchsuchen]({{ '/de/tags/' | relative_url }}#ehs).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Die Sicherheitspyramide: viele Beinahe-Unfälle liegen jedem schweren Ereignis zugrunde — handle an der Basis."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">SICHERHEITSPYRAMIDE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Vorausschauende Wartung als Sicherheitsstrategie</text><polygon points="335.0,80 385.0,80 415.0,138 305.0,138" fill="#7a1f3d"/><text x="360" y="118" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">Schwer · 1</text><polygon points="305.0,144 415.0,144 460.0,202 260.0,202" fill="#b45309"/><text x="360" y="182" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">Leichte Verletzungen · ~30</text><polygon points="260.0,208 460.0,208 520.0,266 200.0,266" fill="#5b7a1f"/><text x="360" y="246" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">Beinahe-Unfälle · ~300</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Die Sicherheitspyramide: viele Beinahe-Unfälle liegen jedem schweren Ereignis zugrunde — handle an der Basis.</figcaption>
</figure>

## Häufig gestellte Fragen

**Wie unterscheidet sich vorausschauende Wartung von vorbeugender Wartung?**
Vorbeugende Wartung ersetzt oder wartet Komponenten nach einem festen Zeitplan, unabhängig vom tatsächlichen Zustand. Vorausschauende Wartung nutzt Zustandsüberwachungsdaten — Vibrations-, Temperatur-, Drucktrends —, um Komponenten zu warten, wenn ihr tatsächlicher Zustand einen bevorstehenden Ausfall anzeigt, und reduziert sowohl ungeplante Stillstände als auch unnötige Eingriffe.

**Welche Brauereianlagen profitieren am meisten von einem vorausschauenden Wartungsansatz?**
Kältekompressoren, CO2-Rückgewinnungs- und Speichersysteme, Druckbehälter und ihre Sicherheitsventile, Zentrifugen sowie Antriebe von Hochgeschwindigkeits-Abfülllinien sind typischerweise die wertvollsten Ziele — sie verbinden hohe Ausfallfolgen, messbare Zustandssignale und teure ungeplante Stillstände.

**Ist vorausschauende Wartung für eine kleine Craft-Brauerei realistisch?**
Vollständige IoT-getriebene vorausschauende Wartung erfordert Investitionen, die für einen kleinen Betrieb schwer zu rechtfertigen sind. Die zugrunde liegende Disziplin — Anlagenzustandsdaten im Trend verfolgen, Frühindikatoren für Ausfälle nachhalten und Anomalien eskalieren — ist jedoch skalierbar. Mit manueller Zustandsüberwachung an zwei oder drei kritischen Anlagen zu beginnen, ist ein praktischer Einstieg.
