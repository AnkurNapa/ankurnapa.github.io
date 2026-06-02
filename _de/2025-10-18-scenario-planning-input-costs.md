---
layout: post
lang: de
title: "Szenarioplanung für Gersten-, Energie- und Aluminiumkosten"
image: /assets/og/scenario-planning-input-costs.png
description: "Szenarioplanung für Brauerei-Inputkosten — Gerste, Energie, Aluminium — verwandelt Rohstoffrisiko in strukturierte Entscheidungen statt reaktiver Überraschungen."
date: 2025-10-18
updated: 2025-10-18
permalink: /de/2025/scenario-planning-input-costs/
tags: [fpna, scenario-planning, commodity-risk]
faq:
  - q: "Was sind die drei größten Rohstoffkostenrisiken für eine Brauerei?"
    a: "Malz (aus Gerste gewonnen), Energie (Erdgas und Strom für Brauen und Kühlung) und Aluminium (für Dosen) sind für die meisten Brauereien durchweg die größten variablen Inputkostenrisiken. Jedes hat einen anderen Preistreiber — landwirtschaftliches Angebot bei Gerste, Energiemärkte bei Versorgern und globale Industrienachfrage bei Aluminium —, was bedeutet, dass sie sich nicht immer gemeinsam bewegen, weshalb diversifiziertes Hedging und Szenarioplanung wichtig sind."
  - q: "Wie sollte eine Brauerei Inputkosten-Szenarien strukturieren?"
    a: "Eine praktische Drei-Szenarien-Struktur nutzt einen Basisfall (aktuelle kontrahierte oder Spot-Preise konstant gehalten), einen Stressfall (eine definierte ungünstige Bewegung bei jedem Schlüsselinput, z. B. Malz +20 %, Energie +30 %, Aluminium +15 %) und einen Chancenfall (günstige Bewegungen, die die Marge ausweiten könnten). Jedes Szenario sollte sich direkt in eine Auswirkung auf die COGS pro hL und die Bruttomarge übersetzen, um die Einsätze konkret zu machen."
  - q: "Gilt die Szenarioplanung für Inputkosten bei alkoholfreiem Bier anders?"
    a: "Ja. Die Kostenstruktur von AF-Bier ist aufgrund des Entalkoholisierungsprozesses energieintensiver, was die Energiekosten-Szenariolinie empfindlicher macht als bei Standardbier. Wenn die AF-Linie zudem mit geringerem Durchsatz als die Hauptbrauerei läuft, verteilen sich fixe Energiekosten auf weniger hL, was die Auswirkung eines Energiepreissprungs pro Einheit verstärkt."
---

**Kurze Antwort:** Gerste, Energie und Aluminium machen zusammen einen wesentlichen Anteil der COGS einer Brauerei aus — und alle drei werden von Kräften außerhalb der Kontrolle der Brauerei getrieben. Szenarioplanung beseitigt dieses Risiko nicht, aber sie ersetzt reaktives Gewusel durch vorab festgelegte Entscheidungsregeln, was eine bessere Nutzung der Managementaufmerksamkeit und eine besser verteidigbare Position gegenüber Investoren und Kreditgebern ist.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Szenarioplanung für Gersten-, Energie- und Aluminiumkosten</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Daten herein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">die Halle verändern</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Warum Inputkosten-Überraschungen sich schlimmer anfühlen, als sie sind

Wenn die Malzpreise hochschnellen oder die Energierechnung im Quartalsvergleich um 30 % springt, ist der Instinkt, es als Notfall zu behandeln. In den meisten Fällen ist es kein Notfall — es ist ein vorhersehbares Bereichsergebnis, das schlicht nie explizit eingeplant wurde. Die Kosten der Überraschung sind nicht nur finanziell; es ist die Managementzeit, die von einer reaktiven Reaktion verschlungen wird, die Monate früher hätte skriptiert werden können.

Szenarioplanung wandelt diese reaktiven Kosten in eine proaktive Investition um. Indem das Finanzteam explizite Modelle dessen baut, was unter ungünstigen, Basis- und günstigen Inputkostenannahmen mit der Brauereiökonomie passiert, kann es Entscheidungsauslöser im Voraus vorbereiten: Bei welchem Malzpreis muss die Preisstrategie überdacht werden? Bei welchen Energiekosten ändert sich der Investitionsfall für ein Wärmerückgewinnungssystem? Diese Antworten lassen sich viel leichter ruhig vor dem Ereignis entwickeln als unter Druck.

## Die drei Inputkostentreiber und ihre Mechanik

**Malz und Gerste** — die größte Rohstoffposition für die meisten Brauereien. Gerste ist ein landwirtschaftlicher Rohstoff, der Ernteschwankungen, regionalen Anbaubedingungen und Währungseffekten bei importierten Malzsorten unterliegt. Brauereien, die ihre Malzverträge nicht bis zum Spätsommer fixiert haben, kaufen typischerweise in einen Markt hinein, in dem die Preissicht für das Folgejahr begrenzt ist. Die Szenarioplanung sollte mindestens einen Basis- und einen 20–25-%-Ungünstigfall bei den Malzkosten modellieren, übersetzt in die Auswirkung auf COGS/hL.

**Energie** — Erdgas für Brauen und Dampferzeugung, Strom für Kühlung und Druckluft. Energie ist oft die zweitgrößte Inputkostenposition für Brauereien mit Gärung und Kühllagerung vor Ort. Die Kosten sind teils durch Effizienzinvestitionen steuerbar (Wärmerückgewinnung, LED-Beleuchtung, drehzahlgeregelte Antriebe), aber die Rohstoffpreiskomponente ist es nicht. AF-Bier-Betriebe sind besonders exponiert, weil die Entalkoholisierung energieintensiv ist — eine 30-prozentige Energiepreiserhöhung trifft die AF-COGS/hL anteilig härter als die COGS/hL von Standardbier.

**Aluminium** — relevant für jede Brauerei mit erheblichem Dosenvolumen, was inzwischen die meisten Craft-Betriebe beschreibt. Aluminiumpreise sind an die globale Industrienachfrage, die Energiekosten (Aluminiumverhüttung ist energieintensiv) und die Handelspolitik gekoppelt. Dosenpreise hinken dem Aluminium-Spot um die Länge der Lieferverträge hinterher, sodass ein Aluminium-Sprung die Gewinn-und-Verlust-Rechnung der Brauerei vielleicht erst in sechs bis zwölf Monaten trifft — aber er wird es irgendwann, und die Verzögerungsperiode ist die Zeit, in der die Szenarioplanung Preis- und Hedging-Entscheidungen formen sollte.

## Das Szenariomodell bauen

Ein praktisches Inputkosten-Szenariomodell hat drei Komponenten:

**Sensitivitätstabelle** — was ist für jeden Hauptinput die Auswirkung auf COGS/hL bei einer Preiserhöhung von 10 %, 20 % und 30 %? Das ist eine einfache Berechnung, sobald der Kostentreiberbaum aus [Herstellkosten pro Hektoliter]({{ '/de/2025/cost-of-goods-per-hectoliter/' | relative_url }}) vorhanden ist. Eine Sensitivitätstabelle gibt dem Finanzteam und dem Führungsteam einen gemeinsamen Bezugspunkt.

**Szenariodefinitionen** — drei benannte Szenarien mit spezifischen Annahmen für jeden Input. Basis, Stress und Chance. Der Stressfall sollte unangenehm, aber plausibel sein — kein katastrophales Tail-Ereignis —, weil das Ziel ist, eine Reaktion zu entwerfen, nicht Alarm zu erzeugen. Zum Beispiel: Malz +20 % (eine bedeutende, aber historisch beobachtete Dürreauswirkung), Energie +30 % (im Einklang mit jüngster Marktvolatilität), Aluminium +15 % (innerhalb jüngster Jahresbereiche).

**Entscheidungsauslöser-Karte** — was sind für jedes Szenario die vorab festgelegten Reaktionen? Schwellen für Preiserhöhungen, Hedging-Maßnahmen (wenn die Brauerei das Volumen hat, um Zugang zu Futures oder Swaps zu erhalten), Entscheidungen zur SKU-Rationalisierung und Capex-Verschiebungen. Die Auslöser sollten spezifisch genug sein, um ohne ein weiteres Entscheidungsmeeting zu handeln.

## Szenarien mit der rollierenden Prognose verbinden

Szenarioplanung ist am wertvollsten, wenn sie in die treiberbasierte Prognosekadenz integriert ist, die in [treiberbasierte Prognose für Brauereien]({{ '/de/2025/driver-based-forecasting-breweries/' | relative_url }}) beschrieben wird. Das Basisszenario sollte der zentrale Fall in der rollierenden Prognose sein; das Stressszenario sollte der dem Vorstand präsentierte Abwärtsfall sein. Wenn die tatsächlichen Inputpreise beginnen, in Richtung des Stressszenarios zu laufen, liefert die Entscheidungsauslöser-Karte ein vorab genehmigtes Playbook.

## Die ehrliche Grenze

Szenarioplanung prognostiziert nicht, welches Szenario eintreten wird. Sie strukturiert die Reaktion auf eine Bandbreite von Ergebnissen. Brauereien, die den Basisfall als die Prognose und den Stressfall als die Feuerübung behandeln, ziehen tendenziell den meisten Wert aus der Übung. Brauereien, die den Stressfall als das Budget behandeln, neigen dazu, in Wachstumschancen unterzuinvestieren. Die Disziplin liegt darin, beide Fälle gleichzeitig zu halten und zu wissen, welche Reihe von Entscheidungen jeder einzelne erfordert.

*Teil des Tracks Financial Planning & Analytics — [alle durchsuchen]({{ '/de/tags/' | relative_url }}#fpna).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Von Anfang bis Ende, aufgeschlüsselt in die Teile, die die Zahl bewegen."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">BRÜCKE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Szenarioplanung für Gersten-, Energie- und Aluminiumkosten</text><line x1="60" y1="250" x2="680" y2="250" stroke="#1c1a17" stroke-width="1.5"/><rect x="90" y="100" width="80" height="150" fill="#b45309"/><text x="130" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Start</text><rect x="230" y="140" width="80" height="40" fill="#7a1f3d"/><text x="270" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">−40</text><rect x="350" y="170" width="80" height="30" fill="#7a1f3d"/><text x="390" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">−30</text><rect x="470" y="130" width="80" height="40" fill="#5b7a1f"/><text x="510" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">+40</text><rect x="590" y="130" width="80" height="120" fill="#b45309"/><text x="630" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Ende</text><line x1="170" y1="100" x2="230" y2="100" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><line x1="310" y1="140" x2="350" y2="140" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><line x1="430" y1="170" x2="470" y2="170" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><line x1="550" y1="130" x2="590" y2="130" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Von Anfang bis Ende, aufgeschlüsselt in die Teile, die die Zahl bewegen.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was sind die drei größten Rohstoffkostenrisiken für eine Brauerei?**
Malz (aus Gerste gewonnen), Energie (Erdgas und Strom für Brauen und Kühlung) und Aluminium (für Dosen) sind für die meisten Brauereien durchweg die größten variablen Inputkostenrisiken. Jedes hat einen anderen Preistreiber — landwirtschaftliches Angebot bei Gerste, Energiemärkte bei Versorgern und globale Industrienachfrage bei Aluminium —, was bedeutet, dass sie sich nicht immer gemeinsam bewegen, weshalb diversifiziertes Hedging und Szenarioplanung wichtig sind.

**Wie sollte eine Brauerei Inputkosten-Szenarien strukturieren?**
Eine praktische Drei-Szenarien-Struktur nutzt einen Basisfall (aktuelle kontrahierte oder Spot-Preise konstant gehalten), einen Stressfall (eine definierte ungünstige Bewegung bei jedem Schlüsselinput, z. B. Malz +20 %, Energie +30 %, Aluminium +15 %) und einen Chancenfall (günstige Bewegungen, die die Marge ausweiten könnten). Jedes Szenario sollte sich direkt in eine Auswirkung auf die COGS pro hL und die Bruttomarge übersetzen, um die Einsätze konkret zu machen.

**Gilt die Szenarioplanung für Inputkosten bei alkoholfreiem Bier anders?**
Ja. Die Kostenstruktur von AF-Bier ist aufgrund des Entalkoholisierungsprozesses energieintensiver, was die Energiekosten-Szenariolinie empfindlicher macht als bei Standardbier. Wenn die AF-Linie zudem mit geringerem Durchsatz als die Hauptbrauerei läuft, verteilen sich fixe Energiekosten auf weniger hL, was die Auswirkung eines Energiepreissprungs pro Einheit verstärkt.
