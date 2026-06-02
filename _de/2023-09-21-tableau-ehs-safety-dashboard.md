---
layout: post
lang: de
title: "Ein EHS-Sicherheitsvorfall-Dashboard in Tableau"
image: /assets/og/tableau-ehs-safety-dashboard.png
description: "Baue ein EHS-Sicherheits-Dashboard in Tableau mit TRIR-artigen Raten, Früh- gegen Spätindikatoren, einer Hotspot-Heatmap und Pulse-Benachrichtigungen — plus den Vorbehalt zur Untererfassung."
date: 2023-09-21
updated: 2023-09-21
permalink: /de/2023/tableau-ehs-safety-dashboard/
tags: [ehs, tableau, safety]
faq:
  - q: "Was ist der Unterschied zwischen Früh- und Spätindikatoren für Sicherheit?"
    a: "Spätindikatoren zählen, was bereits schiefgelaufen ist, etwa erfasspflichtige Verletzungen oder Vorfälle mit Ausfallzeit. Frühindikatoren messen präventive Aktivität, wie Beinahe-Unfall-Meldungen, abgeschlossene Audits und geschlossene Korrekturmaßnahmen, die künftiges Risiko vorhersagen."
  - q: "Wie berechne ich eine TRIR-artige Rate in Tableau?"
    a: "Nutze ein berechnetes Feld: erfasspflichtige Vorfälle multipliziert mit 200.000, geteilt durch die gesamten geleisteten Arbeitsstunden. Die 200.000 normalisieren auf 100 Vollzeitbeschäftigte pro Jahr und machen Standorte und Zeiträume vergleichbar."
  - q: "Warum könnte eine fallende Vorfallzahl ein schlechtes Zeichen sein?"
    a: "Weil sie Untererfassung statt verbesserter Sicherheit widerspiegeln kann. Wenn gleichzeitig die Beinahe-Unfall-Meldungen fallen, ist das ein Warnsignal: Möglicherweise haben die Leute aufgehört zu melden, nicht aufgehört, sich zu verletzen."
---

**Kurze Antwort: Ein Sicherheits-Dashboard muss Frühindikatoren genauso aufmerksam beobachten wie Spätindikatoren, denn fallende Vorfallzahlen können weniger Meldungen bedeuten, nicht weniger Gefahren.** Das Dashboard unterstützt eine Sicherheitskultur; es erzeugt keine.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für ein EHS-Sicherheitsvorfall-Dashboard in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Ein EHS-Sicherheitsvorfall-Dashboard in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Kennzahlen-Schlagzeilen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerlegen.</figcaption>
</figure>

## Früh- und Spätindikatoren gemeinsam messen
Die prägende Disziplin der EHS-Analytik ist, das bereits Geschehene mit dem zu paaren, was das Kommende vorhersagt. Spätindikatoren — erfasspflichtige Verletzungen, Fälle mit Ausfallzeit, eine TRIR-artige Rate — sind die gesetzlich vorgeschriebene Bewertungstafel, aber sie sind Rückspiegel. Frühindikatoren — eingereichte Beinahe-Unfall-Meldungen, protokollierte Sicherheitsbeobachtungen, abgeschlossene Audits, fristgerecht geschlossene Korrekturmaßnahmen — sind das Frühwarnsystem. Ein Dashboard, das nur Spätkennzahlen zeigt, bringt einer Organisation bei, ein ruhiges Quartal zu feiern, ohne zu fragen, ob die Ruhe echt ist. Setze beide auf die Leinwand, nebeneinander, von der ersten Skizze an.

## Bauen: Raten, eine Hotspot-Heatmap und Benachrichtigungen
TRIR-artige Normalisierung ist ein berechnetes Feld: erfasspflichtige Vorfälle mal 200.000, geteilt durch geleistete Arbeitsstunden. Die Konstante normalisiert auf grob 100 Vollzeitkräfte über ein Jahr, sodass eine kleine Abfülllinie und ein großes Sudhaus vergleichbar werden. Hülle es in ein LOD, wenn du die Rate auf Standortgranularität berechnen musst, während du eine Unternehmensaufrollung anzeigst.

Die Hotspot-Heatmap ist die Grafik, die dem Dashboard seinen Wert verdient. Kreuztabelliere Vorfallzahlen (oder Raten) nach Bereich gegen Vorfalltyp oder Schicht, und nutze eine sequenzielle Farbskala, sodass die Zelle „Lagerhaus-Verladerampe-in-Nachtschicht" ins Auge springt. Hier verstecken sich Muster, die eine Trendlinie übersieht. Füge einen Parameter hinzu, um Standort und Zeitraum zu wechseln, verdrahtet über Parameteraktionen, sodass das Auswählen eines Standorts die Heatmap, die Raten-BANs und das Frühindikator-Panel in einem Klick aktualisiert.

Schichte Frühindikatoren als kleines Panel: Trend des Beinahe-Unfall-Aufkommens, Anteil der innerhalb des Ziels geschlossenen Korrekturmaßnahmen, Audit-Abschlussrate. Konfiguriere dann Tableau Pulse, um die erfasspflichtige Rate und den Rückstand an Korrekturmaßnahmen zu überwachen, und sende Benachrichtigungen sowie eine Klartext-Zusammenfassung an den EHS-Verantwortlichen — „offene Korrekturmaßnahmen an Standort B um 30 % gestiegen" —, sodass Risiko vor dem nächsten Vorfall an die Oberfläche kommt statt danach. „Explain Data" kann vorschlagen, was sich an einem Bereich mit hohen Vorfallzahlen unterscheidet — ein nützlicher Anstoß für den Sicherheitsrundgang, keine Schlussfolgerung.

## Wo es scheitert: Untererfassung und die Kulturlücke
Die mit Abstand größte Gefahr ist die Untererfassungs-Verzerrung, und kein Diagramm kann sie aus dem Inneren der Daten heraus erkennen. Wenn Frontline-Teams das Gefühl haben, dass das Melden eines Beinahe-Unfalls Schuldzuweisungen auslöst, versiegen die Meldungen, die Spätzahlen verbessern sich, und das Dashboard zeigt fröhlich Grün, während das tatsächliche Risiko klettert. Deshalb sollte ein plötzlicher Rückgang der Beinahe-Unfall-Meldungen als Warnung gelesen werden, nicht als Erfolg. Baue diese Interpretation in die Art ein, wie das Dashboard präsentiert wird, sonst wird es falsch gelesen.

Die tiefere Grenze ist, dass Sicherheit eine Kultur ist, kein Diagramm. Eine schöne Tableau-Arbeitsmappe schließt keine Schutzvorrichtung, ändert kein Verhalten und bringt keinen müden Arbeiter dazu, sich zu Wort zu melden. Generative-KI-Zusammenfassungen können sogar die Wachsamkeit untergraben: Eine selbstbewusste Pulse-Zusammenfassung, die sagt „Vorfallrate auf Rekordtief", lädt genau dann zur Selbstzufriedenheit ein, wenn Frühindikatoren Gelb blinken könnten. Lass Menschen — das EHS-Team und die Frontline-Vorgesetzten — die Interpretation tragen, und nutze das Dashboard, um Gespräche zu beginnen statt sie zu beenden.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Die Sicherheitspyramide: viele Beinahe-Unfälle liegen jedem schweren Ereignis zugrunde — handle an der Basis."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">SICHERHEITSPYRAMIDE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Ein EHS-Sicherheitsvorfall-Dashboard in Tableau</text><polygon points="335.0,80 385.0,80 415.0,138 305.0,138" fill="#7a1f3d"/><text x="360" y="118" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">Schwer · 1</text><polygon points="305.0,144 415.0,144 460.0,202 260.0,202" fill="#b45309"/><text x="360" y="182" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">Leichte Verletzungen · ~30</text><polygon points="260.0,208 460.0,208 520.0,266 200.0,266" fill="#5b7a1f"/><text x="360" y="246" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">Beinahe-Unfälle · ~300</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Die Sicherheitspyramide: viele Beinahe-Unfälle liegen jedem schweren Ereignis zugrunde — handle an der Basis.</figcaption>
</figure>

## Das Fazit
Baue das EHS-Dashboard um gepaarte Früh- und Spätindikatoren, normalisiere mit einer TRIR-artigen Rate, und lass eine Hotspot-Heatmap zutage bringen, wo sich Risiko konzentriert. Nutze Pulse für Benachrichtigungen, aber behandle fallende Zahlen skeptisch und beobachte die Beinahe-Unfall-Meldungen als Stellvertreter für Vertrauen. Die eigentliche Aufgabe des Dashboards ist, das Sicherheitsgespräch ehrlich und fortlaufend zu halten.

*Teil des Tracks [EHS]({{ '/de/tracks/ehs/' | relative_url }}).* Verwandt: [EHS-Berichtsautomatisierung]({{ '/de/2026/ehs-reporting-automation/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist der Unterschied zwischen Früh- und Spätindikatoren für Sicherheit?**
Spätindikatoren zählen, was bereits schiefgelaufen ist, etwa erfasspflichtige Verletzungen oder Vorfälle mit Ausfallzeit. Frühindikatoren messen präventive Aktivität, wie Beinahe-Unfall-Meldungen, abgeschlossene Audits und geschlossene Korrekturmaßnahmen, die künftiges Risiko vorhersagen.

**Wie berechne ich eine TRIR-artige Rate in Tableau?**
Nutze ein berechnetes Feld: erfasspflichtige Vorfälle multipliziert mit 200.000, geteilt durch die gesamten geleisteten Arbeitsstunden. Die 200.000 normalisieren auf 100 Vollzeitbeschäftigte pro Jahr und machen Standorte und Zeiträume vergleichbar.

**Warum könnte eine fallende Vorfallzahl ein schlechtes Zeichen sein?**
Weil sie Untererfassung statt verbesserter Sicherheit widerspiegeln kann. Wenn gleichzeitig die Beinahe-Unfall-Meldungen fallen, ist das ein Warnsignal: Möglicherweise haben die Leute aufgehört zu melden, nicht aufgehört, sich zu verletzen.
