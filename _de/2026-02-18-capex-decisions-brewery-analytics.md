---
layout: post
lang: de
title: "Capex mit Analytik: Wann man einen Tank oder eine Dosenlinie ergänzt"
image: /assets/og/capex-decisions-brewery-analytics.png
description: "Capex-Entscheidungsanalytik für Brauereien — wie man Kapazitätsauslastung, Margenbeitrag und Amortisationsmodellierung nutzt, um Tank- und Dosenlinien-Investitionen zu terminieren."
date: 2026-02-18
updated: 2026-02-18
permalink: /de/2026/capex-decisions-brewery-analytics/
tags: [fpna, capex, capacity-planning]
faq:
  - q: "Welche Finanzkennzahlen sollten die Entscheidung einer Brauerei treiben, Gärkapazität zu ergänzen?"
    a: "Die primären Kennzahlen sind die Tankauslastungsrate (liegt die Spitzenauslastung konstant über 85 %, fallen wahrscheinlich Engpasskosten an), der inkrementelle Margenbeitrag aus dem eingeschränkten Volumen (welche Bruttomarge durch das Kapazitätslimit verloren geht) und die Amortisationszeit für den neuen Tank bei realistischen Durchsatzannahmen. Ein Tank bei 60 % Auslastung ohne glaubwürdiges Nachfragesignal rechtfertigt das Kapital nicht."
  - q: "Wie sollte eine Brauerei eine Dosenlinien-Investition gegenüber Lohnabfüllung bewerten?"
    a: "Der Vergleich sollte auf Gesamtkostenbasis aufgebaut werden: hauseigene Dosenkosten pro Kiste (amortisiertes Kapital, direkte Arbeit, Verbrauchsmaterial, Wartung) gegenüber Lohnabfüllkosten pro Kiste inklusive Fracht und Vorlaufzeitaufschlag. Die Break-even-Volumenschwelle — das Volumen, ab dem hauseigen günstiger ist — sollte gegen die glaubwürdige 3-Jahres-Nachfrageprognose der Brauerei modelliert werden. Unterhalb dieser Schwelle erhält die Lohnabfüllung Kapital und bewahrt Flexibilität."
  - q: "Ändert eine alkoholfreie Bierlinie das Capex-Bewertungsrahmenwerk?"
    a: "Ja in einer wichtigen Hinsicht: Entalkoholisierungsausrüstung für alkoholfreies Bier (Umkehrosmose oder Vakuumdestillation) ist eine relativ spezialisierte Kapitalinvestition mit einem engeren Satz alternativer Nutzungen, falls die NA-Linie unterdurchschnittlich abschneidet. Das Restwertrisiko ist höher als bei einem Standard-Gärtank, der über das Bierportfolio hinweg umgewidmet werden kann. Der auf NA-spezifisches Capex angewandte Mindestrenditesatz sollte diese reduzierte Optionalität widerspiegeln."
---

**Kurze Antwort:** Der falsche Zeitpunkt, eine Tank- oder Dosenlinien-Investition zu bewerten, ist, wenn das Produktionsteam sagt, dass der Brauerei die Kapazität ausgeht. Zu diesem Zeitpunkt wird die Entscheidung unter operativem Druck statt analytischer Klarheit getroffen. Brauereien, die ein dauerhaftes Capex-Rahmenwerk aufbauen — Auslöserkennzahlen, Amortisationsmodell, Szenariobandbreite — tätigen bessere Investitionen und vermeiden sowohl Unter- als auch Überbau.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Capex mit Analytik: Wann man einen Tank oder eine Dosenlinie ergänzt</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">den Betrieb ändern</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Die zwei Versagensmodi des Brauerei-Capex

Brauerei-Kapitalinvestitionen scheitern auf vorhersehbare Weise an beiden Enden des Spektrums.

**Überinvestition** ist das sichtbarere Versagen: Eine Brauerei kauft zwei Gärtanks auf Basis einer Nachfrageprognose, die nicht eintritt, betreibt die neuen Tanks bei 40 % Auslastung und trägt Abschreibungen, die die Marge jahrelang zusammendrücken. Kreditgeber und Investoren sehen den Vermögenswert in der Bilanz; sie sehen selten die Opportunitätskosten des Betriebskapitals und der Zinsaufwendungen, die er verzehrt hat.

**Unterinvestition** ist weniger sichtbar, aber gleichermaßen kostspielig: Die Brauerei weist Bestellungen ab, liefert gegen Distributorenverpflichtungen zu wenig, verpasst Saisonfenster oder — am teuersten — verliert Distributionsvereinbarungen, weil sie nicht zuverlässig liefern kann. Die verlorene Marge aus nicht gedeckter Nachfrage erscheint selten als Posten irgendwo in den Managementbüchern.

Ein analytikgetriebenes Capex-Rahmenwerk reduziert beide Versagensmodi, indem es den Investitionsauslöser explizit und evidenzbasiert statt reaktiv macht.

## Das Capex-Auslöser-Rahmenwerk

Ein praktisches Auslöser-Rahmenwerk für Produktionskapazitätsinvestitionen hat drei Komponenten:

**Auslastungsschwelle** — definiere eine rollierende Auslastungsrate (für Gärtanks ausgedrückt als belegte Tank-Tage gegenüber verfügbaren Tank-Tagen; für die Dosenlinie als gelaufene Stunden gegenüber verfügbaren Stunden), oberhalb derer ein Kapazitätsengpass bestätigt ist. Eine anhaltende Spitzenauslastungsrate über 80–85 % ist eine gängige Schwelle, aber die richtige Zahl hängt davon ab, wie viel Puffer der Produktionsplan für Reinigung, Wartung und Rezeptwechsel benötigt.

**Verlorene-Marge-Berechnung** — sobald der Engpass bestätigt ist, quantifiziere das Volumen, das die Brauerei gegen bekannte Nachfrage nicht produzieren oder liefern kann. Multipliziere mit dem Deckungsbeitrag pro hL für die eingeschränkte SKU. Das ergibt eine konkrete Zahl: „Wir lassen wegen dieses Engpasses etwa X Dollar Bruttomarge pro Quartal liegen." Diese Zahl ist der ökonomische Fall für die Investition, formuliert in Begriffen, die Vorstand und Kreditgeber bewerten können.

**Amortisationsmodell** — eine realistische Amortisationsberechnung bei drei Volumenszenarien (Basis, konservativ, optimistisch) unter Verwendung der tatsächlichen Kapitalkosten, Installationskosten, inkrementellen Betriebskosten (zusätzliche Arbeit, Versorgung, Wartung) und des inkrementellen Margenbeitrags. Ein Tank, der sich im konservativen Volumenfall in unter drei Jahren amortisiert, ist meist eine unkomplizierte Genehmigung. Ein Tank, der optimistische Volumenannahmen braucht, um eine Fünfjahres-Amortisation zu erreichen, ist eine strategische Wette und sollte als solche präsentiert werden.

## Dosenlinie vs. Lohnabfüllung: Die Make-or-Buy-Entscheidung

Die Entscheidung zwischen der Investition in eine hauseigene Dosenlinie und der weiteren Nutzung der Lohnabfüllung ist eine der häufigsten Capex-Entscheidungen im Craft-Brauwesen und eine der am häufigsten aus Intuition statt aus Analyse getroffenen.

Der Finanzfall sollte auf einem Vergleich der Gesamtkosten pro Kiste aufgebaut werden. Die hauseigenen Dosenkosten umfassen amortisiertes Kapital (Linienkosten geteilt durch Nutzungsdauer, geteilt durch jährliche Dosen), direkte Arbeit, Verbrauchsmaterial (Falzmasse, Tinte, CO2), Wartungsrückstellung und Qualitätskontroll-Overhead. Die Lohnabfüllkosten umfassen den Vertragssatz pro Kiste, ein- und ausgehende Fracht und einen Aufschlag für die Vorlaufzeit — Lohnlinien verlangen oft vier bis acht Wochen Planungshorizont, was Betriebskapitalkosten und Reaktionsfähigkeitskosten hat.

Das Break-even-Volumen ist der Punkt, an dem die hauseigenen Kosten pro Kiste den Lohnkosten pro Kiste entsprechen. Für die meisten Dosenlinien im mittleren Bereich liegt dieser Break-even irgendwo im Bereich mehrerer Hunderttausend Kisten jährlich, wobei die genaue Zahl erheblich mit Liniengeschwindigkeit, Arbeitskosten und Lohnpreisgestaltung im lokalen Markt variiert. Die 3-Jahres-Nachfrageprognose der Brauerei, stresstgetestet gegen das Szenario-Rahmenwerk aus [Szenarioplanung für Inputkosten]({{ '/de/2025/scenario-planning-input-costs/' | relative_url }}), sollte der Input für diese Berechnung sein — nicht die Best-Case-Volumenannahme.

## Der NA-Bier-Capex-Fall

Alkoholfreies Bier führt eine spezifische Capex-Überlegung ein: Entalkoholisierungsausrüstung. Ob die Investition ein Umkehrosmose-Membransystem oder eine Vakuumdestillationseinheit ist, das Kapital ist im Vergleich zu einem Standard-Gärtank oder einer Dosenlinie relativ spezialisiert. Der Restwert, falls die NA-Linie unterdurchschnittlich abschneidet, ist niedriger, und der Markt für gebrauchte Entalkoholisierungsausrüstung ist dünner.

Das spricht nicht gegen die Investition — aber es spricht dafür, einen höheren Mindestrenditesatz anzuwenden und vor der Genehmigung einen konservativeren Amortisationsfall zu verlangen. Auch die Betriebskapitaldynamik von NA — besprochen in [Betriebskapital im Brauwesen]({{ '/de/2025/working-capital-brewing/' | relative_url }}) — sollte in die Gesamtkapitalkostenberechnung einbezogen werden, da NA-Bestand langsamer umschlagen kann als Standardbier-Bestand.

## Die ehrliche Grenze

Capex-Analytik produziert besser informierte Entscheidungen, nicht korrekte. Nachfrageprognosen können falsch sein, Installationskosten können überschritten werden, und Marktbedingungen können sich zwischen Kapitalgenehmigung und voller Produktion ändern. Die Disziplin, das Rahmenwerk aufzubauen, ist wertvoll, selbst wenn die Inputs unsicher sind — sie erzwingt explizites Annehmen und schafft einen Prüfpfad nach der Investition, der künftige Entscheidungen verbessert.

*Teil des Tracks Financial Planning & Analytics — [alle durchsuchen]({{ '/de/tags/' | relative_url }}#fpna).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Von Anfang bis Ende, aufgeteilt in die Teile, die die Zahl bewegen."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">BRIDGE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Capex mit Analytik: Wann man einen Tank oder eine Dosenlinie ergänzt</text><line x1="60" y1="250" x2="680" y2="250" stroke="#1c1a17" stroke-width="1.5"/><rect x="90" y="100" width="80" height="150" fill="#b45309"/><text x="130" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Start</text><rect x="230" y="140" width="80" height="40" fill="#7a1f3d"/><text x="270" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">−40</text><rect x="350" y="170" width="80" height="30" fill="#7a1f3d"/><text x="390" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">−30</text><rect x="470" y="130" width="80" height="40" fill="#5b7a1f"/><text x="510" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">+40</text><rect x="590" y="130" width="80" height="120" fill="#b45309"/><text x="630" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Ende</text><line x1="170" y1="100" x2="230" y2="100" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><line x1="310" y1="140" x2="350" y2="140" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><line x1="430" y1="170" x2="470" y2="170" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><line x1="550" y1="130" x2="590" y2="130" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Von Anfang bis Ende, aufgeteilt in die Teile, die die Zahl bewegen.</figcaption>
</figure>

## Häufig gestellte Fragen

**Welche Finanzkennzahlen sollten die Entscheidung einer Brauerei treiben, Gärkapazität zu ergänzen?**
Die primären Kennzahlen sind die Tankauslastungsrate (liegt die Spitzenauslastung konstant über 85 %, fallen wahrscheinlich Engpasskosten an), der inkrementelle Margenbeitrag aus dem eingeschränkten Volumen (welche Bruttomarge durch das Kapazitätslimit verloren geht) und die Amortisationszeit für den neuen Tank bei realistischen Durchsatzannahmen. Ein Tank bei 60 % Auslastung ohne glaubwürdiges Nachfragesignal rechtfertigt das Kapital nicht.

**Wie sollte eine Brauerei eine Dosenlinien-Investition gegenüber Lohnabfüllung bewerten?**
Der Vergleich sollte auf Gesamtkostenbasis aufgebaut werden: hauseigene Dosenkosten pro Kiste (amortisiertes Kapital, direkte Arbeit, Verbrauchsmaterial, Wartung) gegenüber Lohnabfüllkosten pro Kiste inklusive Fracht und Vorlaufzeitaufschlag. Die Break-even-Volumenschwelle — das Volumen, ab dem hauseigen günstiger ist — sollte gegen die glaubwürdige 3-Jahres-Nachfrageprognose der Brauerei modelliert werden. Unterhalb dieser Schwelle erhält die Lohnabfüllung Kapital und bewahrt Flexibilität.

**Ändert eine alkoholfreie Bierlinie das Capex-Bewertungsrahmenwerk?**
Ja in einer wichtigen Hinsicht: Entalkoholisierungsausrüstung für alkoholfreies Bier (Umkehrosmose oder Vakuumdestillation) ist eine relativ spezialisierte Kapitalinvestition mit einem engeren Satz alternativer Nutzungen, falls die NA-Linie unterdurchschnittlich abschneidet. Das Restwertrisiko ist höher als bei einem Standard-Gärtank, der über das Bierportfolio hinweg umgewidmet werden kann. Der auf NA-spezifisches Capex angewandte Mindestrenditesatz sollte diese reduzierte Optionalität widerspiegeln.
