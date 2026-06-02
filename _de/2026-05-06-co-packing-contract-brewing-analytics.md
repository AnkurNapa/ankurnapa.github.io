---
layout: post
lang: de
title: "Analytics für Co-Packing und Lohnbrauen: Kapazität rentabel machen"
image: /assets/og/co-packing-contract-brewing-analytics.png
description: "Lohnbrauen und Co-Packing stehen und fallen mit der Kapazitätsauslastung und den wahren Kosten pro Vertrag. Die Analysen, die entscheiden, ob jede Kundenmarke tatsächlich Geld verdient — und wo KI hilft."
date: 2026-05-06 09:00:00 -0700
updated: 2026-05-06
permalink: /de/2026/co-packing-contract-brewing-analytics/
tags: [brewing-science, contract-brewing, co-packing, capacity-planning, commercial-planning]
faq:
  - q: "Was ist Lohnbrauen und Co-Packing?"
    a: "Lohnbrauen heißt, Bier für die Marke eines anderen Unternehmens herzustellen; Co-Packing (Co-Manufacturing) heißt, es für sie zu verpacken — in Dosen, Flaschen oder Fässer. In beiden Fällen verkauft der Produzent Kapazität und Ausführung statt der eigenen Marke, daher wird das Geschäft auf Tank-Tagen, Linienstunden und Kosten pro Vertrag geführt, nicht auf Abverkäufen."
  - q: "Welche Kennzahlen sind beim Lohnbrauen am wichtigsten?"
    a: "Kapazitätsauslastung (Gärtank-Tage und Abfülllinien-Stunden sind die echten Engpässe), Umrüst- und CIP-Zeit zwischen Marken, Ausbeute und Sudhaus-Effizienz je Rezept, wahre Cost-to-Serve pro Vertrag und Marge je Kunde nach jedem Verlust. Lieferungen sagen wenig; Auslastung und Marge pro Vertrag sagen alles."
  - q: "Wie hilft Analytics einer Lohnbrauerei?"
    a: "Es beantwortet die zwei Fragen, an denen das Geschäft hängt: Ist die Anlage voll, und verdient jeder Vertrag Geld? Scheduling-Analysen maximieren Tank-Tage und minimieren Umrüstungen; Cost-to-Serve- und Ausbeute-Analysen decken unrentable Verträge auf; und die Chargen-Genealogie hält die Marke jedes Kunden über gemeinsam genutzte Linien hinweg rückverfolgbar und spezifikationskonform."
---

**Kurze Antwort: Lohnbrauen und Co-Packing verkaufen Kapazität, keine Marke — daher läuft das gesamte Geschäft auf zwei Zahlen: wie voll die Anlage ist und ob jeder Kundenvertrag nach jedem Verlust tatsächlich Geld verdient. Die Analysen, auf die es ankommt, sind Kapazitätsauslastung (Gärtank-Tage und Linienstunden), Umrüst- und CIP-Zeit, Ausbeute je Rezept sowie wahre Cost-to-Serve und Marge pro Vertrag. KI schärft den Plan und die Kalkulation; sie ändert nichts an den Grundlagen.**

Das Produkt einer Lohnbrauerei ist ihr Sudhaus, ihre Gärtanks und ihre Abfülllinien — verkauft nach Tank-Tag und Linienstunde. Das macht sie zu einem anderen analytischen Tier als eine markenbesitzende Brauerei: Erfolg sind nicht Abverkäufe, sondern eine volle Anlage profitabler Verträge. Dieselbe Brille gilt, egal ob man der Co-Packer *ist* oder einen *nutzt*. Es baut auf [Herstellkosten pro Hektoliter]({{ '/de/2025/cost-of-goods-per-hectoliter/' | relative_url }}) und [Cost-to-Serve-Profitabilität]({{ '/de/2025/cost-to-serve-na-beer-profitability/' | relative_url }}) auf.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Analytics-Fluss beim Lohnbrauen: Kapazität, Plan, Brauen je Marke, Kosten und Ausbeute, Abrechnung und Marge">
<rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/>
<text x="500" y="34" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Die Lohnbrauerei, in Zahlen</text>
<g font-family="sans-serif">
<rect x="20" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><circle cx="106" cy="114" r="15" fill="#b45309"/><text x="106" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">1</text><text x="106" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#1c1a17">Kapazität</text><text x="106" y="193" text-anchor="middle" font-size="11" fill="#6b6258">Tank-Tage, Linienstunden</text>
<rect x="216" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><circle cx="302" cy="114" r="15" fill="#b45309"/><text x="302" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">2</text><text x="302" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#1c1a17">Planen</text><text x="302" y="193" text-anchor="middle" font-size="11" fill="#6b6258">die Marken einpassen</text>
<rect x="412" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><circle cx="498" cy="114" r="15" fill="#b45309"/><text x="498" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">3</text><text x="498" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#1c1a17">Brauen je Marke</text><text x="498" y="193" text-anchor="middle" font-size="11" fill="#6b6258">nach jeder Spezifikation</text>
<rect x="608" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><circle cx="694" cy="114" r="15" fill="#b45309"/><text x="694" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">4</text><text x="694" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#1c1a17">Kosten & Ausbeute</text><text x="694" y="193" text-anchor="middle" font-size="11" fill="#6b6258">pro Vertrag</text>
<rect x="804" y="80" width="172" height="150" rx="8" fill="#b45309"/><circle cx="890" cy="114" r="15" fill="#fff"/><text x="890" y="119" text-anchor="middle" font-size="13.5" font-weight="700" fill="#b45309">5</text><text x="890" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">Abrechnen & Marge</text><text x="890" y="193" text-anchor="middle" font-size="11" fill="#f7ece0">der wahre Gewinn</text>
</g>
<g fill="#b45309" stroke="#b45309" stroke-width="2">
<line x1="192" y1="155" x2="209" y2="155"/><polygon points="209,150 216,155 209,160" stroke="none"/>
<line x1="388" y1="155" x2="405" y2="155"/><polygon points="405,150 412,155 405,160" stroke="none"/>
<line x1="584" y1="155" x2="601" y2="155"/><polygon points="601,150 608,155 601,160" stroke="none"/>
<line x1="780" y1="155" x2="797" y2="155"/><polygon points="797,150 804,155 797,160" stroke="none"/>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Die Wertschöpfungskette einer Lohnbrauerei läuft auf Kapazität und Kosten pro Vertrag — nicht auf eigenen Abverkäufen.</figcaption>
</figure>

## Kapazität ist das Produkt

Der bindende Engpass beim Lohnbrauen ist selten das Sudhaus — es sind Gär- und Reifetank-Tage sowie Abfülllinien-Stunden. Ein Tank, der für ein langsam vergärendes Rezept zwei zusätzliche Tage blockiert ist, ist Kapazität, die man nicht verkaufen kann. Die erste Analytics-Aufgabe ist daher Auslastung: Wie viele der verfügbaren Tank-Tage und Linienstunden werden tatsächlich abgerechnet, und wo gehen sie an Umrüstungen, CIP zwischen Marken und Leerlauf-Lücken verloren. Scheduling-Analysen — die Sequenzierung von Marken zur Minimierung von CIP und die Abstimmung der Gärprofile von Rezepten auf Tankumläufe — schaffen direkt verkaufbare Kapazität, das Thema von [Produktionsplanung]({{ '/de/2021/ai-brewery-production-scheduling/' | relative_url }}).

## Wahre Kosten und Marge pro Vertrag

Ein Vertrag wirkt im Angebot profitabel und verliert in der Realität Geld, wenn die Verluste nicht zugeordnet werden. Echte Cost-to-Serve pro Kunde muss die tatsächliche Sudhaus-Ausbeute und Extraktausnutzung dieser Marke tragen, ihre Gärverluste und Tankzeit, ihre Umrüst- und CIP-Last, die OEE ihrer Abfülllinie und ihren Materialausschuss sowie ihren Anteil an Versorgung und Gemeinkosten. Erst dann wird die Marge pro Vertrag ehrlich — und sie offenbart regelmäßig, dass ein hochvolumiger Kunde, der einen niedrigen Satz zahlt, weniger wert ist als ein kleinerer, einfacherer. Die Zuordnung der Ausbeute je Rezept (Stammwürze, Vergärung und Sudhaus-Effizienz variieren je Marke) ist der unglamouröse Kern der Kalkulation.

## Rückverfolgbarkeit und Spezifikationskontrolle über viele Marken

Die Marken mehrerer Kunden durch gemeinsam genutzte Gefäße und Linien zu fahren, macht Rückverfolgbarkeit und Qualität nicht verhandelbar. Jede Marke ist ein eigenes Rezept und eine eigene Spezifikation, und die IBD-Grundlagen gelten weiterhin: die Ziel-Stammwürze und den Vergärungsgrad des Kunden treffen, seine Farbe und Bittere, seine Spezifikationen für gelösten Sauerstoff und Karbonisierung — auf *seinem* Rezept, nicht einem Hausstandard. Die Chargen-Genealogie (Los zu Tank zu Gebinde zu Palette, je Kunde) schützt vor Verwechslungen, unterstützt die Rückrufe jeder Marke unabhängig und untermauert die Abrechnung. Gemeinsam genutzte Linien machen außerdem die Allergen- und Kreuzkontaminationskontrolle zu einem Analytics-Anliegen erster Ordnung, nicht zu einem Nachgedanken.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 210" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Wohin die Kapazität geht: abgerechnete Produktion, Umrüstung und CIP, Ausbeuteverlust und Leerlauf">
<rect x="0" y="0" width="760" height="210" fill="#fdfbf7"/>
<text x="380" y="30" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Wohin die Kapazität (das Produkt) geht</text>
<rect x="60" y="62" width="396.8" height="44" fill="#b45309"/>
<rect x="456.8" y="62" width="89.6" height="44" fill="#8a5a2b"/>
<rect x="546.4" y="62" width="51.2" height="44" fill="#7a1f3d"/>
<rect x="597.6" y="62" width="102.4" height="44" fill="#6b6258"/>
<text x="258" y="90" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#fdfbf7">Abgerechnete Produktion 62%</text>
<g font-family="sans-serif" font-size="12.5" fill="#1c1a17">
<rect x="60" y="140" width="14" height="14" fill="#b45309"/><text x="80" y="152">Abgerechnete Produktion — 62%</text>
<rect x="300" y="140" width="14" height="14" fill="#8a5a2b"/><text x="320" y="152">Umrüstung & CIP — 14%</text>
<rect x="540" y="140" width="14" height="14" fill="#7a1f3d"/><text x="560" y="152">Ausbeuteverlust — 8%</text>
<rect x="60" y="166" width="14" height="14" fill="#6b6258"/><text x="80" y="178">Leerlauf / unverkauft — 16%</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Nur der abgerechnete Anteil verdient. Umrüstung, CIP, Ausbeuteverlust und Leerlaufzeit sind Kapazität, für die man bezahlt und die man nicht verkauft hat — das Analytics-Ziel.</figcaption>
</figure>

## Wo KI hilft — und wo nicht

Maschinelles Lernen schärft die zwei schweren Probleme: Scheduling (Marken und Tankumläufe sequenzieren, um abgerechnete Tank-Tage zu maximieren und CIP zu minimieren) und Prognose (die Gärzeit und Ausbeute einer Marke vorhersagen, damit der Plan realistisch ist), wobei [Abfülllinien-OEE]({{ '/de/2023/tableau-packaging-line-oee-dashboard/' | relative_url }})-Analysen die Linienseite auspressen. Ein generativer KI-Copilot kann die Margenüberprüfung pro Vertrag und den kundengerichteten Produktionsbericht aus den Daten entwerfen.

Drei ehrliche Grenzen. Erstens: **Müll-Kalkulation rein, Müll-Marge raus** — wenn man Ausbeute, Tankzeit und CIP nicht der richtigen Marke zuordnet, ist die Marge pro Vertrag Fiktion, und KI berechnet die Fiktion nur schneller. Zweitens: **Kapazität ist klumpig und vertraglich** — man kann nicht reibungslos um Mindestabnahme-Verpflichtungen und das feste Launch-Datum eines Kunden herum optimieren, der Plan hat also harte menschliche Beschränkungen. Drittens: **Qualität ist der Vertrag** — der Ruf eines Co-Packers besteht darin, jede Spezifikation jeder Marke jedes Mal zu treffen; kein Auslastungsgewinn ist eine spezifikationswidrige Charge wert, die den Kunden kostet.

## Das Fazit

Lohnbrauen und Co-Packing sind ein Kapazitätsgeschäft in den Kleidern einer Brauerei. Miss die Auslastung in Tank-Tagen und Linienstunden, ordne jeden Verlust der Marke zu, die ihn verursacht hat, und berechne eine ehrliche Marge pro Vertrag — und lass dann Scheduling- und Prognose-Analysen die Anlage voll und die Kalkulation knapp halten. Halte Rückverfolgbarkeit und Spezifikationskontrolle absolut, denn das Produkt, das du tatsächlich verkaufst, ist verlässliche Kapazität.

## Häufig gestellte Fragen

**Was ist Lohnbrauen und Co-Packing?**
Lohnbrauen heißt, Bier für die Marke eines anderen Unternehmens herzustellen; Co-Packing (Co-Manufacturing) heißt, es für sie zu verpacken — in Dosen, Flaschen oder Fässer. In beiden Fällen verkauft der Produzent Kapazität und Ausführung statt der eigenen Marke, daher wird das Geschäft auf Tank-Tagen, Linienstunden und Kosten pro Vertrag geführt, nicht auf Abverkäufen.

**Welche Kennzahlen sind beim Lohnbrauen am wichtigsten?**
Kapazitätsauslastung (Gärtank-Tage und Abfülllinien-Stunden sind die echten Engpässe), Umrüst- und CIP-Zeit zwischen Marken, Ausbeute und Sudhaus-Effizienz je Rezept, wahre Cost-to-Serve pro Vertrag und Marge je Kunde nach jedem Verlust. Lieferungen sagen wenig; Auslastung und Marge pro Vertrag sagen alles.

**Wie hilft Analytics einer Lohnbrauerei?**
Es beantwortet die zwei Fragen, an denen das Geschäft hängt: Ist die Anlage voll, und verdient jeder Vertrag Geld? Scheduling-Analysen maximieren Tank-Tage und minimieren Umrüstungen; Cost-to-Serve- und Ausbeute-Analysen decken unrentable Verträge auf; und die Chargen-Genealogie hält die Marke jedes Kunden über gemeinsam genutzte Linien hinweg rückverfolgbar und spezifikationskonform.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).*
