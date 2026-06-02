---
layout: post
lang: de
title: "Promotion-Uplift: Echte Nachfrage vom Rabatt-Rauschen trennen"
image: /assets/og/promotional-lift-forecasting.png
description: "Wie man den Promotion-Uplift beim Bier misst und prognostiziert — die Basisnachfrage von rabattgetriebenen Volumenspitzen trennen und die Vorkaufsfalle vermeiden."
date: 2025-07-14
updated: 2025-07-14
permalink: /de/2025/promotional-lift-forecasting/
tags: [forecasting, promotional-lift-forecasting]
faq:
  - q: "Was ist Promotion-Uplift in der Nachfrageprognose?"
    a: "Promotion-Uplift ist das während einer Aktion verkaufte Zusatzvolumen über dem, was zum regulären Preis und unter regulären Bedingungen verkauft worden wäre — der Basisnachfrage. Ihn zu isolieren ist wesentlich, weil Aktionen Volumenspitzen erzeugen, die, wenn man sie für echtes Nachfragewachstum hält, nach dem Ende der Aktion Überproduktion und Bestandsprobleme verursachen."
  - q: "Wie überschätzen Brauereien typischerweise den Wert einer Aktion?"
    a: "Der häufigste Fehler ist, die Aktionsperiode mit der Vorperiode zu vergleichen, ohne Vorkäufe und Nachaktions-Einbrüche zu berücksichtigen. Verbraucher und Händler bevorraten sich während eines Deals und ziehen Volumen vor; die Wochen unmittelbar nach einer Aktion zeigen oft unterdurchschnittliche Verkäufe. Nur den Uplift zu betrachten, ohne den Einbruch zu verrechnen, überschätzt die netto erzeugte Nachfrage erheblich."
  - q: "Wirken Aktionen bei alkoholfreiem Bier anders?"
    a: "Die Evidenz ist richtungsmäßig gemischt. Alkoholfreies Bier zieht tendenziell probierorientierte Käufer an, die beim ersten Kauf preissensibler sein könnten, was nahelegt, dass Aktionen echte Neukundengewinnung statt bloßer Vorkäufe antreiben können. Die Kategorie reift jedoch noch, und die Daten für selbstsichere Verallgemeinerungen sind bei den meisten Marken begrenzt."
---

**Kurze Antwort:** Aktionsbedingte Volumenspitzen sind real, werden aber routinemäßig fehlinterpretiert. Die Disziplin der Promotion-Uplift-Prognose trennt echte Nachfrageschaffung von Timing-Effekten, Vorkäufen und Kannibalisierung benachbarter SKUs. Ohne diese Trennung wird der Aktions-ROI systematisch überschätzt, und auf Aktionsvolumen aufgebaute Lieferpläne erzeugen in den folgenden Wochen kostspieligen Überbestand.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Die Betriebsschleife, die dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DIE BETRIEBSSCHLEIFE</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Promotion-Uplift: Echte Nachfrage vom Rabatt-Rauschen trennen</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">die Werkstatt verändern</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Die Betriebsschleife, die dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Warum Aktionen naive Prognosen brechen

Eine Aktion erzeugt in den Liefer- und Abverkaufsdaten ein Muster, das oberflächlich wie Nachfragewachstum aussieht. Die verkauften Einheiten schießen während der beworbenen Woche oder Wochen in die Höhe, fallen dann zurück — manchmal unter die Basislinie vor der Aktion, während Händler und Verbraucher die während des Deals angesammelten Bestände abbauen.

Ein naives Prognosemodell, das auf diesem Rohsignal trainiert wird, lernt die falsche Lektion: Es erwartet eine dauerhafte Nachfragesteigerung, die nicht existiert. Das Ergebnis sind Überproduktionszusagen, erhöhter Fertigwarenbestand und Abschreibungen.

Die Lösung besteht nicht darin, Aktionen zu ignorieren — sie besteht darin, sie explizit als eigenständige Nachfragekomponente zu modellieren, statt sie in den Basistrend aufzunehmen.

---

## Das Drei-Komponenten-Rahmenwerk

Ein robustes Promotion-Uplift-Modell zerlegt das gesamte verkaufte Volumen in drei Komponenten:

**1. Basisnachfrage.** Das Volumen, das zum vollen Preis ohne jegliche Aktionsaktivität verkauft worden wäre. Das ist die Zahl, die echte Verbraucherpräferenz widerspiegelt und die richtige Eingabe für Kapazitätsplanung, Rohstoffbeschaffung und langfristige Finanzprognosen ist.

**2. Inkrementeller Uplift.** Das Volumen, das durch die Aktion wirklich hinzugefügt wird — entweder dadurch, dass Verbraucher die Kategorie häufiger kaufen (Kategorieerweiterung) oder von einem Wettbewerber wechseln (Trade-up). Das ist der Wert, den Händler und Marke zu schaffen versuchen.

**3. Timing-Transfer.** Volumen, das aus benachbarten Perioden verschoben wird — Vorkäufe von Händlern, die Displays füllen, Verbraucher, die sich bevorraten, oder Vorratshaltung. Dieses Volumen wird in der Nachaktionsperiode negativ sein. Es erzeugt keine Nettonachfrage.

Die praktische Herausforderung ist, dass diese drei Komponenten nicht direkt beobachtbar sind; sie müssen geschätzt werden. Regressionsbasierte Modelle, die für Aktionsmarkierungen, Preisindizes und Händlerbestandsschätzungen kontrollieren, können das Signal mit angemessener Genauigkeit für gut etablierte SKUs mit langen Historien zerlegen.

---

## Den Nachaktions-Einbruch messen

Die am wenigsten überwachte Kennzahl in der Aktionsanalytik ist das Nachaktions-Tal. Eine glaubwürdige Uplift-Analyse zeigt immer die Zwei- bis Vier-Wochen-Periode nach einer großen Aktion neben der Aktionsperiode selbst.

Das Verhältnis von Einbruch zu Uplift zeigt an, wie viel des Aktionsvolumens aus der Zukunft geliehen wurde versus wirklich inkrementell war. Eine Aktion, die in Woche eins einen Volumenanstieg von 25 % erzeugt, aber in den Wochen zwei und drei einen Einbruch von 15 %, hat viel weniger Nettowert geliefert, als es auf den ersten Blick scheint.

Für die Lieferplanung bedeutet das, dass Produktionspläne nicht symmetrisch auf Aktionen reagieren sollten. Auf die beworbene Spitze hin zu produzieren und dann nach der Aktion aggressiv zu kürzen, ist typischerweise der richtige Ansatz — aber nur, wenn das Planungssystem genaue Aktionskalender im Voraus erhält, statt nach den Liefer­spitzen im Nachhinein zu reagieren.

---

## Kannibalisierung innerhalb des Portfolios

Aktionen bei einer SKU können die Verkäufe benachbarter SKUs im selben Portfolio unterdrücken. Ein hoher Rabatt auf ein Flaggschiff-Lager kann die Verkäufe einer Premium-Craft-Variante derselben Marke verlangsamen. Für eine Brauerei, die sowohl konventionelle als auch alkoholfreie SKUs verwaltet, ist diese portfoliointerne Kannibalisierung besonders wichtig zu messen.

Siehe [Kannibalisierung: Frisst alkoholfreies Bier die Verkäufe deines Lagers?]({{ '/de/2025/cannibalization-na-beer-lager/' | relative_url }}) für ein Rahmenwerk, das speziell auf die Dynamik alkoholfrei-versus-konventionell zugeschnitten ist.

Das Prinzip gilt gleichermaßen für den Aktionskontext: Wenn eine Aktion auf das konventionelle Lager das Kategorie-Probieren beschleunigt, das später in einen Kauf von alkoholfreiem Bier umschlägt, ist das ein positiver Überlaufeffekt. Wenn sie einen Kauf von alkoholfreiem Bier nur um einige Wochen verzögert, ist es ein Timing-Transfer. Die beiden zu unterscheiden erfordert entweder Paneldaten oder eine sorgfältig gestaltete Test-und-Kontroll-Marktstruktur.

---

## Vorausschauend prognostizieren: Den Aktionskalender ins Modell einbauen

Eine Promotion-Uplift-Prognose ist nur dann nützlich, wenn der vorausschauende Aktionsplan als Eingabe verfügbar ist. Das klingt offensichtlich und wird routinemäßig verletzt. Aktionen werden häufig von Vertriebsteams in Zeitrahmen verhandelt und bestätigt, die nicht mit den Vorlaufzeiten der Lieferplanung übereinstimmen.

Die organisatorische Lösung ist ein gesperrter Aktionskalender — idealerweise vier bis acht Wochen im Voraus eingefroren — der direkt in das Nachfragemodell einfließt. Jede nach dem Sperrdatum bestätigte Aktion sollte eine ausdrückliche Diskussion zwischen Vertrieb und Lieferung darüber auslösen, ob Volumenzusagen innerhalb der verfügbaren Kapazität und des Bestands angepasst werden können.

Für einen breiteren Blick darauf, wie die Aktionsmodellierung in die treiberbasierte Prognosestufe passt, siehe [Das Reifegradmodell für die Getränke-Nachfrageprognose]({{ '/de/2025/demand-forecasting-maturity-model/' | relative_url }}).

---

## Der ehrliche Vorbehalt

Promotion-Uplift-Modelle benötigen genügend Aktionsereignisse im historischen Datensatz, um Uplift-Koeffizienten zuverlässig zu schätzen. Für SKUs, die selten beworben werden, oder für SKUs alkoholfreien Biers mit begrenzter Historie wird das Modell weite Unsicherheitsintervalle um jede Uplift-Schätzung haben. In solchen Fällen kann eine einfachere Faustregel (z. B. X % Uplift basierend auf Kategorie-Analogien annehmen) ehrlicher sein als ein angepasstes Modell, das präzise erscheint, aber aus dünnen Daten extrapoliert.

*Teil des Tracks Sales Forecasting — [alle durchsehen]({{ '/de/tags/' | relative_url }}#forecasting).*

---

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">BEITRAG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Promotion-Uplift: Echte Nachfrage vom Rabatt-Rauschen trennen</text><text x="60" y="109" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal A</text><rect x="180" y="90" width="300" height="26" rx="4" fill="#b45309"/><text x="60" y="153" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal B</text><rect x="180" y="134" width="230" height="26" rx="4" fill="#b45309"/><text x="60" y="197" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal C</text><rect x="180" y="178" width="150" height="26" rx="4" fill="#b45309"/><text x="60" y="241" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal D</text><rect x="180" y="222" width="90" height="26" rx="4" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist Promotion-Uplift in der Nachfrageprognose?**  
Promotion-Uplift ist das während einer Aktion verkaufte Zusatzvolumen über dem, was zum regulären Preis und unter regulären Bedingungen verkauft worden wäre — der Basisnachfrage. Ihn zu isolieren ist wesentlich, weil Aktionen Volumenspitzen erzeugen, die, wenn man sie für echtes Nachfragewachstum hält, nach dem Ende der Aktion Überproduktion und Bestandsprobleme verursachen.

**Wie überschätzen Brauereien typischerweise den Wert einer Aktion?**  
Der häufigste Fehler ist, die Aktionsperiode mit der Vorperiode zu vergleichen, ohne Vorkäufe und Nachaktions-Einbrüche zu berücksichtigen. Verbraucher und Händler bevorraten sich während eines Deals und ziehen Volumen vor; die Wochen unmittelbar nach einer Aktion zeigen oft unterdurchschnittliche Verkäufe. Nur den Uplift zu betrachten, ohne den Einbruch zu verrechnen, überschätzt die netto erzeugte Nachfrage erheblich.

**Wirken Aktionen bei alkoholfreiem Bier anders?**  
Die Evidenz ist richtungsmäßig gemischt. Alkoholfreies Bier zieht tendenziell probierorientierte Käufer an, die beim ersten Kauf preissensibler sein könnten, was nahelegt, dass Aktionen echte Neukundengewinnung statt bloßer Vorkäufe antreiben können. Die Kategorie reift jedoch noch, und die Daten für selbstsichere Verallgemeinerungen sind bei den meisten Marken begrenzt.
