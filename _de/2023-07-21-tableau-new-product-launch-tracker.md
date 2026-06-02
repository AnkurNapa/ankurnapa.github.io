---
layout: post
lang: de
title: "Ein Tracker für Produktneueinführungen in Tableau"
image: /assets/og/tableau-new-product-launch-tracker.png
description: "Bauen Sie einen Tracker für Produktneueinführungen in Tableau mit LOD-Berechnungen, Tabellenberechnungen und Pulse, um Probierkauf, Wiederkauf und Abverkaufsrate je Verkaufsstelle zu verfolgen."
date: 2023-07-21
updated: 2023-07-21
permalink: /de/2023/tableau-new-product-launch-tracker/
tags: [marketing, tableau, analytics]
faq:
  - q: "Welche Kennzahlen sind beim Verfolgen einer Produktneueinführung am wichtigsten?"
    a: "Distributionsaufbau (Verkaufsstellen, die führen), Abverkaufsrate je Verkaufsstelle und das Verhältnis von Probier- zu Wiederkauf. Volumen allein schmeichelt einer Einführung; die Wiederkaufrate sagt Ihnen, ob sie Bestand haben wird."
  - q: "Kann Tableau prognostizieren, wie eine Einführung ankommt?"
    a: "Tableaus eingebaute Prognose nutzt exponentielle Glättung, was für eine grobe Trendlinie in Ordnung ist, aber schwach bei einer Einführung mit nur wenigen Wochen verrauschter Daten. Behandeln Sie sie als richtungsweisend, nicht als Evangelium."
  - q: "Wie vergleiche ich verschiedene Einführungs-Kohorten in einer Ansicht?"
    a: "Verwenden Sie einen Parameter zur Auswahl der Einführungs-Kohorte oder des Wochen-seit-Einführung-Index, und steuern Sie dann eine Tabellenberechnung darüber, sodass jedes Produkt an seinem eigenen Einführungsdatum statt am Kalender ausgerichtet ist."
---

**Kurze Antwort: Ein guter Einführungs-Tracker misst Wiederkauf und Abverkaufsrate je Verkaufsstelle, nicht nur die insgesamt ausgelieferten Kisten.** Auslieferungen sagen Ihnen, was Sie in den Handel gedrückt haben; der Tracker muss Ihnen sagen, was tatsächlich durchverkauft wurde und für mehr zurückkam.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für Ein Tracker für Produktneueinführungen in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Ein Tracker für Produktneueinführungen in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Kennzahlen-Überschriften oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Zerlegen.</figcaption>
</figure>

## Entscheiden Sie die Messgröße, bevor Sie ein Diagramm anfassen
Die Disziplin eines Einführungs-Trackers besteht darin, zu entscheiden, was „funktioniert" bedeutet, bevor die Daten Sie verführen. Für ein neues Bier oder RTD tragen drei Messgrößen das Urteil: Distributionsaufbau (wie viele Verkaufsstellen es führen), Abverkaufsrate je Verkaufsstelle (Geschwindigkeit, nicht nur Präsenz) und das Verhältnis von Probier- zu Wiederkauf (kamen die Trinker zurück). Skizzieren Sie diese zuerst auf Papier. Ein Dashboard, das mit einer eitlen Kistenvolumen-Zahl öffnet, trainiert alle darauf, den Verkauf in den Handel zu feiern und den Durchverkauf zu ignorieren — und genau so stirbt eine Einführung leise im Regal.

In datenwissenschaftlichen Begriffen trennen Sie eine Bestandskennzahl (kumulierte Distribution) von einer Flusskennzahl (wöchentliche Abverkaufsrate). Sie auf einer Achse zu mischen ist der häufigste Fehler beim Einführungs-Tracking, den ich sehe.

## Bauen Sie es: LOD, Tabellenberechnungen und ein Kohorten-Parameter
Das Handwerk beginnt mit der Ausrichtung. Kalenderwochen sind nutzlos, wenn Produkte an verschiedenen Daten eingeführt werden, also bauen Sie einen „Wochen seit Einführung"-Index und lassen Sie jedes Produkt bei Woche null starten. Ein FIXED-LOD-Ausdruck fixiert das Einführungsdatum jedes Produkts unabhängig von den Filtern der Ansicht:

`{ FIXED [Product] : MIN([First Sale Date]) }`

Ziehen Sie das vom Verkaufsdatum ab, und Sie haben Ihre einführungsrelative Achse. Die Abverkaufsrate ist dann eine Tabellenberechnung: verkaufte Einheiten geteilt durch aktive Verkaufsstellen, berechnet entlang des Einführungswochen-Index. Der Distributionsaufbau ist eine laufende Zählung eindeutiger Verkaufsstellen, wieder eine nach Produkt partitionierte Tabellenberechnung.

Fügen Sie einen Parameter hinzu, um die Analyse-Kohorte zu wechseln — Sommereinführungen gegen Herbst, Premium gegen Kern — und verdrahten Sie ihn mit einer Parameteraktion, sodass ein Klick auf ein Produkt die ganze Ansicht neu rahmt. Probier-gegen-Wiederkauf braucht ein berechnetes Feld, das den Erstkauf eines Kunden gegen Folgekäufe markiert; ein INCLUDE-LOD lässt Sie Wiederkäufer auf Kundengranularität zählen und dennoch auf Produktgranularität anzeigen.

Für die Führungsebene richten Sie Tableau Pulse auf Abverkaufsrate und Wiederkaufrate. Pulse überwacht diese Kennzahlen und sendet eine Zusammenfassung in natürlicher Sprache, „Abverkaufsrate Woche über Woche um 12 % gestiegen, getrieben von der Region Süd", sodass die Führung die Einführung liest, ohne die Arbeitsmappe zu öffnen. „Explain Data" von Einstein Copilot kann sich an einem Versuch wagen, warum eine Region hochsprang, aber Sie sollten seine Begründung überprüfen, bevor Sie sie wiederholen.

## Wo es bricht
Frühe Einführungsdaten sind wirklich verrauscht. Zwei Wochen Durchverkauf über eine Handvoll Verkaufsstellen sind kein Trend, und ein Tracker, der täglich aktualisiert, lädt dazu ein, auf Stichprobenrauschen überzureagieren. Die Wiederkaufrate ist der schlimmste Übeltäter: Sie kann sich physisch nicht stabilisieren, bevor genug Trinker Zeit hatten zurückzukommen, oft sechs bis acht Wochen bei einer regelmäßig gekauften Kategorie. Wenn Ihr Dashboard in Woche zwei eine selbstbewusste Wiederkaufzahl blinken lässt, lügt es mit ernster Miene.

Es gibt auch die Attributionsfalle. Eine Spitze könnte eine Aktionsplatzierung, ein Lieferengpass eines Wettbewerbers oder eine Hitzewelle sein — von all dem weiß Tableau nichts. Das Diagramm zeigt das Was; das Warum braucht noch einen Menschen, der den Handel abgegangen ist. Generative KI-Zusammenfassungen verstärken dieses Risiko: Eine flüssige Pulse-Zusammenfassung liest sich maßgeblich, selbst wenn die zugrunde liegende Stichprobe dünn ist, also setzen Sie Konfidenz-Vorbehalte ins Dashboard selbst.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">BEITRAG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Ein Tracker für Produktneueinführungen in Tableau</text><text x="60" y="109" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal A</text><rect x="180" y="90" width="300" height="26" rx="4" fill="#b45309"/><text x="60" y="153" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal B</text><rect x="180" y="134" width="230" height="26" rx="4" fill="#b45309"/><text x="60" y="197" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal C</text><rect x="180" y="178" width="150" height="26" rx="4" fill="#b45309"/><text x="60" y="241" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Kanal D</text><rect x="180" y="222" width="90" height="26" rx="4" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt.</figcaption>
</figure>

## Das Fazit
Ein Einführungs-Tracker verdient seinen Platz, wenn er das Gespräch von „wie viele haben wir ausgeliefert" zu „kommt es zurück" verschiebt. Bauen Sie die Kohorten-Ausrichtung mit LOD und Tabellenberechnungen, führen Sie mit Abverkaufsrate und Wiederkauf, und lassen Sie Pulse den wöchentlichen Stand zu den Führungskräften tragen. Dann behalten Sie die Nerven bei frühen Daten und lassen die Wiederkaufrate reifen, bevor Sie die Einführung bewerten.

*Teil des Tracks [Marketing]({{ '/de/tracks/marketing/' | relative_url }}).* Verwandt: das breitere [Dashboard für Marken- und Marketingleistung]({{ '/de/2023/tableau-brand-marketing-dashboard/' | relative_url }}).

## Häufig gestellte Fragen

**Welche Kennzahlen sind beim Verfolgen einer Produktneueinführung am wichtigsten?**
Distributionsaufbau (Verkaufsstellen, die führen), Abverkaufsrate je Verkaufsstelle und das Verhältnis von Probier- zu Wiederkauf. Volumen allein schmeichelt einer Einführung; die Wiederkaufrate sagt Ihnen, ob sie Bestand haben wird.

**Kann Tableau prognostizieren, wie eine Einführung ankommt?**
Tableaus eingebaute Prognose nutzt exponentielle Glättung, was für eine grobe Trendlinie in Ordnung ist, aber schwach bei einer Einführung mit nur wenigen Wochen verrauschter Daten. Behandeln Sie sie als richtungsweisend, nicht als Evangelium.

**Wie vergleiche ich verschiedene Einführungs-Kohorten in einer Ansicht?**
Verwenden Sie einen Parameter zur Auswahl der Einführungs-Kohorte oder des Wochen-seit-Einführung-Index, und steuern Sie dann eine Tabellenberechnung darüber, sodass jedes Produkt an seinem eigenen Einführungsdatum statt am Kalender ausgerichtet ist.
