---
layout: post
lang: de
title: "20 fortgeschrittene Brauberechnungen, die du in Excel machen kannst (Formeln inklusive)"
image: /assets/og/advanced-brewing-calculations-excel.png
description: "Einmaischtemperatur, IBU, ABV, Anstellrate, Karbonisierung, Farbe, Effizienz und mehr — 20 fortgeschrittene Brauberechnungen als einfügefertige Excel-Formeln mit durchgerechneten Beispielen."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
permalink: /de/2026/advanced-brewing-calculations-excel/
tags: [brewing-science, excel, brewing-calculations, recipe-formulation, quality-control]
faq:
  - q: "Kann man ABV in Excel berechnen?"
    a: "Ja. Die Standardformel lautet =(OG-FG)*131.25, wobei OG und FG deine Stammwürze- und Endvergärungsdichte (spezifisches Gewicht) sind. Für stärkere Biere ist eine genauere Variante =(76.08*(OG-FG)/(1.775-OG))*(FG/0.794). Beide funktionieren in jeder Excel-Version ohne Add-ins."
  - q: "Wie lautet die Excel-Formel für die Einmaisch-Wassertemperatur?"
    a: "Einmaischtemperatur Tw = (0.2/R)(T2-T1)+T2, wobei R das Wasser-zu-Schüttung-Verhältnis in Quarts pro Pound ist, T1 die Schüttungstemperatur und T2 deine Zielmaischtemperatur in °F. In Excel: =(0.2/B2)*(B4-B3)+B4 mit R in B2, Schüttungstemperatur in B3 und Ziel in B4. Für metrisch (L/kg, °C) ersetze die 0.2 durch 0.41."
  - q: "Brauche ich spezielle Brausoftware für diese Berechnungen?"
    a: "Nein. Jede Berechnung hier — Dichte, Effizienz, IBU, Farbe, Anstellrate, Karbonisierung, ABV — ist nur Arithmetik, die Brausoftware unter der Haube ausführt. Ein einziges Excel-Blatt mit diesen Formeln bildet das nach, und weil du jede Zelle sehen kannst, verstehst du das Ergebnis und vertraust ihm."
---

**Kurze Antwort: Jede Zahl, die dir eine Brau-App liefert — Einmaischtemperatur, IBU, ABV, Anstellrate, Speisezucker, Farbe, Effizienz — ist schlichte Arithmetik, die du in einem Excel-Blatt ohne Add-ins aufbauen kannst. Unten stehen 20 fortgeschrittene Brauberechnungen als einfügefertige Formeln mit durchgerechneten Beispielen, organisiert über den Brautag hinweg. Richte die Zellen einmal ein, und du hast einen Sudhaus-Rechner, den du vollständig verstehst.**

Brausoftware verbirgt die Mathematik. Das ist in Ordnung, bis du um 6 Uhr morgens ein Rezept anpassen, einen Effizienz-Fehlschlag abgleichen oder einem neuen Brauer einen Karbonisierungs-Sollwert erklären musst. Eine Tabelle, die du selbst gebaut hast, macht all das und zeigt ihren Rechenweg. Wenn du dich noch in die Idee hineinredest, ist [zuerst die Daten zu sammeln]({{ '/de/2026/collect-your-data-before-ai/' | relative_url }}) der richtige Instinkt — diese Formeln verwandeln jene Zahlen in Entscheidungen.

Eine Konvention für den ganzen Artikel: Zellbezüge wie `B2` sind Beispiele — trag deinen Input in jene Zelle ein und füge die Formel daneben ein. Dichten sind spezifisches Gewicht (z. B. 1.050), sofern nicht anders angegeben; „Punkte" meint die letzten drei Ziffern ((SG − 1) × 1000), also 1.050 = 50 Punkte. Schreibweisen sind britisch (colour, litres); imperiale und metrische Hinweise stehen dort, wo sich die Konstante ändert.

<aside style="margin:1.6rem 0;padding:1rem 1.25rem;border:1px solid #00695c;border-left:5px solid #00695c;border-radius:8px;background:#f0f6f5">
<strong style="color:#00695c">📊 Die Serie „Excel für Brauer"</strong>
<p style="margin:.5rem 0 .35rem">Dieser Beitrag ist der Knotenpunkt. Sechs der untenstehenden Berechnungen haben eine vollständige Vertiefung — ein kompletter Blatt-Aufbau, zusätzliche Formeln, durchgerechnete Beispiele und ein Diagramm:</p>
<ul style="margin:0;padding-left:1.2rem;line-height:1.5">
<li><a href="{{ '/de/2026/build-brewing-water-chemistry-calculator-excel/' | relative_url }}">Wasserchemie-Rechner</a> — Salze, Ionen, Restalkalität, Sulfat:Chlorid <em>(Anwendungsfall 9)</em></li>
<li><a href="{{ '/de/2026/mash-water-temperature-calculator-excel/' | relative_url }}">Maischwasser- &amp; Temperaturrechner</a> — Einmaischen, Rasten, Absorption, Läutern <em>(5, 7, 8)</em></li>
<li><a href="{{ '/de/2026/ibu-recipe-builder-excel/' | relative_url }}">IBU-Rezeptbaukasten</a> — Multi-Gaben-Tinseth, BU:GU, Skalierung <em>(10, 11)</em></li>
<li><a href="{{ '/de/2026/yeast-pitching-rates-starters-excel/' | relative_url }}">Hefe-Anstellraten &amp; Starter</a> — Vitalitätsabfall, Starterwachstum <em>(13)</em></li>
<li><a href="{{ '/de/2026/carbonation-calculator-excel/' | relative_url }}">Karbonisierungsrechner</a> — Speisezucker, Keg-PSI, Leitungsbalancierung <em>(17)</em></li>
<li><a href="{{ '/de/2026/brewhouse-efficiency-yield-excel/' | relative_url }}">Sudhaus-Effizienz &amp; Ausbeute-Abgleich</a> — Konversion vs. Läuterverlust <em>(2, 3)</em></li>
</ul>
</aside>

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1046 280" width="100%" style="max-width:1046px;height:auto" role="img" aria-label="Brautag-Prozessfluss, der zeigt, welche der 20 Berechnungen in jeder Phase gelten">
<rect x="0" y="0" width="1046" height="280" fill="#ffffff"/>
<text x="523" y="34" text-anchor="middle" font-family="sans-serif" font-size="18" font-weight="700" fill="#06483f">Der Brautag in Zahlen — wo jede Berechnung landet</text>
<g font-family="sans-serif">
<rect x="4" y="60" width="158" height="190" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="83" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#00695c">REZEPT</text>
<text x="83" y="114" text-anchor="middle" font-size="12.5" fill="#06483f">1 · SG ↔ °Plato</text>
<text x="83" y="138" text-anchor="middle" font-size="12.5" fill="#06483f">2 · OG aus Schüttung</text>
<text x="83" y="162" text-anchor="middle" font-size="12.5" fill="#06483f">3 · Effizienz</text>
<text x="83" y="186" text-anchor="middle" font-size="12.5" fill="#06483f">12 · Farbe SRM</text>
<rect x="180" y="60" width="158" height="190" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="259" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#00695c">MAISCHE</text>
<text x="259" y="114" text-anchor="middle" font-size="12.5" fill="#06483f">5 · Einmaischtemp.</text>
<text x="259" y="138" text-anchor="middle" font-size="12.5" fill="#06483f">6 · Rasten-Infusion</text>
<text x="259" y="162" text-anchor="middle" font-size="12.5" fill="#06483f">7 · Wasser:Schüttung</text>
<text x="259" y="186" text-anchor="middle" font-size="12.5" fill="#06483f">9 · Wassersalze</text>
<rect x="356" y="60" width="158" height="190" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="435" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#00695c">KOCHEN</text>
<text x="435" y="114" text-anchor="middle" font-size="12.5" fill="#06483f">8 · Verdampfung</text>
<text x="435" y="138" text-anchor="middle" font-size="12.5" fill="#06483f">10 · IBU (Tinseth)</text>
<text x="435" y="162" text-anchor="middle" font-size="12.5" fill="#06483f">11 · Hopfen-Ersatz</text>
<rect x="532" y="60" width="158" height="190" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="611" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#00695c">GÄRUNG</text>
<text x="611" y="114" text-anchor="middle" font-size="12.5" fill="#06483f">13 · Anstellrate</text>
<text x="611" y="138" text-anchor="middle" font-size="12.5" fill="#06483f">14 · Vergärungsgrad</text>
<text x="611" y="162" text-anchor="middle" font-size="12.5" fill="#06483f">4 · Temp.-Korrektur</text>
<text x="611" y="186" text-anchor="middle" font-size="12.5" fill="#06483f">15 · Refraktometer</text>
<rect x="708" y="60" width="158" height="190" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="787" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#00695c">ABFÜLLEN</text>
<text x="787" y="114" text-anchor="middle" font-size="12.5" fill="#06483f">16 · ABV</text>
<text x="787" y="138" text-anchor="middle" font-size="12.5" fill="#06483f">17 · Karbonisierung</text>
<text x="787" y="162" text-anchor="middle" font-size="12.5" fill="#06483f">18 · Verschnitt/Verdünnung</text>
<text x="787" y="186" text-anchor="middle" font-size="12.5" fill="#06483f">19 · Kalorien</text>
<rect x="884" y="60" width="158" height="190" rx="8" fill="#f0f6f5" stroke="#06483f" stroke-width="1.5"/>
<text x="963" y="86" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">KOSTEN</text>
<text x="963" y="118" text-anchor="middle" font-size="12.5" fill="#06483f">20 · COGS / hL</text>
<text x="963" y="142" text-anchor="middle" font-size="12.5" fill="#06483f">&amp; Kosten pro Pint</text>
</g>
<g fill="#00695c" stroke="#00695c" stroke-width="2">
<line x1="162" y1="155" x2="174" y2="155"/><polygon points="174,150 181,155 174,160" stroke="none"/>
<line x1="338" y1="155" x2="350" y2="155"/><polygon points="350,150 357,155 350,160" stroke="none"/>
<line x1="514" y1="155" x2="526" y2="155"/><polygon points="526,150 533,155 526,160" stroke="none"/>
<line x1="690" y1="155" x2="702" y2="155"/><polygon points="702,150 709,155 702,160" stroke="none"/>
<line x1="866" y1="155" x2="878" y2="155"/><polygon points="878,150 885,155 878,160" stroke="none"/>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die 20 Berechnungen, zugeordnet zu der Phase, in der du sie nutzt. Die Nummern unten entsprechen dieser Karte.</figcaption>
</figure>

## Rezept und Dichte

**1. Spezifisches Gewicht in °Plato umrechnen.** Brauer und Instrumente sind sich über die Skala uneins; rechne ohne Nachschlagetabelle um.
Formel: °P ≈ 259 − (259 ÷ SG).
Excel (SG in `B2`): `=259-(259/B2)`. Umkehrung (Plato → SG): `=259/(259-B2)`.
Beispiel: SG 1.048 → `=259-(259/1.048)` = **11.9 °P**.

**2. Stammwürze aus der Schüttung vorhersagen.** Kenne deine OG, bevor du braust.
Formel: Punkte = Σ(Gewicht × PPG) × Effizienz ÷ Volumen; OG = 1 + Punkte ÷ 1000. PPG ist points-per-pound-per-gallon (≈ 37 für Pale Malt).
Excel (Gewichte in `B2:B6`, PPGs in `C2:C6`, Effizienz in `F2`, Nachkoch-Gallonen in `G2`): `=1+(SUMPRODUCT(B2:B6,C2:C6)*F2)/(G2*1000)`.
Beispiel: 10 lb Pale Malt (PPG 37) bei 75 % in 5,5 gal → **1.050**.

**3. Sudhaus- und Maische-Effizienz.** Die eine Zahl, die erklärt, warum deine OG danebenlag.
Formel: Effizienz = (gemessene Punkte × Volumen) ÷ maximal mögliche Punkte.
Excel (OG in `B2`, gesammelte Gallonen in `B3`, gesamte mögliche Punkte Σ(lb × PPG) in `B4`): `=((B2-1)*1000*B3)/B4*100`.
Beispiel: OG 1.050, 5,5 gal, 370 mögliche Punkte → **74 %**.

**4. Aräometer-Temperaturkorrektur.** Eine warme Probe liest zu niedrig; korrigiere sie, statt zu raten.
Formel: ein kubisches Polynom in der Probentemperatur relativ zur Kalibriertemperatur des Aräometers (°F).
Excel (gemessene SG `B2`, Probentemp. °F `B3`, Kalibriertemp. °F `B4`): `=B2*((1.00130346-0.000134722124*B3+0.00000204052596*B3^2-0.00000000232820948*B3^3)/(1.00130346-0.000134722124*B4+0.00000204052596*B4^2-0.00000000232820948*B4^3))`.
Beispiel: 1.050 abgelesen bei 100 °F, kalibriert bei 60 °F → **1.056**.

## Maische und Wasser

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 230" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Einmaischwasser-Wärmebilanz: heißes Brauwasser plus kühle Schüttung ergibt Maische auf Zieltemperatur">
<rect x="0" y="0" width="760" height="230" fill="#ffffff"/>
<rect x="20" y="60" width="180" height="110" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="110" y="100" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#06483f">Heißes Brauwasser</text>
<text x="110" y="126" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#00695c">Tw ≈ 164 °F</text>
<text x="110" y="150" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">(worauf du erhitzt)</text>
<text x="230" y="122" text-anchor="middle" font-family="sans-serif" font-size="30" font-weight="700" fill="#4a6b64">+</text>
<rect x="260" y="60" width="180" height="110" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="350" y="100" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#06483f">Schüttung</text>
<text x="350" y="126" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#00695c">T1 = 65 °F</text>
<text x="350" y="150" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">(spezif. Wärme ≈ 0.2)</text>
<g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="450" y1="115" x2="490" y2="115"/><polygon points="490,108 502,115 490,122" stroke="none"/></g>
<rect x="510" y="60" width="220" height="110" rx="8" fill="#00695c"/>
<text x="620" y="100" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Maischbottich</text>
<text x="620" y="126" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#ffffff">T2 = 152 °F Ziel</text>
<text x="620" y="150" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#f0f6f5">(was du willst)</text>
<text x="380" y="205" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#06483f">Tw = (0.2 ÷ R)(T2 − T1) + T2  →  erhitze das Wasser heißer, um die kalte Masse der Schüttung aufzunehmen</text>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Einmaischwasser-Wärmebilanz (Anwendungsfall 5): Das Wasser muss heiß genug laufen, dass die kühle Schüttung die Mischung auf das Ziel herunterzieht.</figcaption>
</figure>

**5. Einmaisch-Wassertemperatur.** Erhitze das Brauwasser heiß genug, dass kalte Schüttung dich aufs Ziel bringt.
Formel: Tw = (0.2 ÷ R)(T2 − T1) + T2 — R = Wasser:Schüttung in qt/lb, T1 = Schüttungstemp., T2 = Zielmaischtemp. (°F).
Excel (R in `B2`, Schüttungstemp. in `B3`, Ziel in `B4`): `=(0.2/B2)*(B4-B3)+B4`.
Beispiel: R = 1,5 qt/lb, Schüttung 65 °F, Ziel 152 °F → **163,6 °F**. Metrisch (L/kg, °C): ersetze `0.2` durch `0.41`.

**6. Stufenmaische-Infusion (Zugabe kochenden Wassers).** Wie viel kochendes Wasser die Maische zur nächsten Rast anhebt.
Formel: Wa = (T2 − T1)(0.2·G + Wm) ÷ (Tw − T2) — G = Schüttung (lb), Wm = bereits in der Maische befindliches Wasser (qt), Tw = 212 °F.
Excel (G `B2`, aktuelle Temp. `B3`, Ziel `B4`, Maischwasser `B5`, Infusionstemp. `B6`): `=(B4-B3)*(0.2*B2+B5)/(B6-B4)`.
Beispiel: 10 lb, 152→168 °F, 15 qt in der Maische, 212 °F Wasser → **6,2 qt**.

**7. Wasser-zu-Schüttung-Verhältnis (Maischdicke).** Dünne Maischen begünstigen die Vergärbarkeit; dicke Maischen schützen Enzyme.
Formel: Verhältnis = Wasser ÷ Schüttung.
Excel (Wasser `B2`, Schüttung `B3`): `=B2/B3`. Umrechnung qt/lb → L/kg mit `=B2/B3*2.086`.
Beispiel: 15 qt ÷ 10 lb = **1,5 qt/lb** (≈ 3,13 L/kg).

**8. Vorderwürze-Volumen und Verdampfung.** Triff dein Nachkoch-Volumen, indem du mit dem richtigen Vorderkoch-Volumen startest.
Formel: Vorderkoch = Ziel-Nachkoch + (Verdampfungsrate × Kochstunden); füge ~4 % für Abkühlschrumpfung hinzu.
Excel (Ziel-Nachkoch-Liter `B2`, Verdampfung L/h `B3`, Stunden `B4`): `=(B2/0.96)+B3*B4`.
Beispiel: 23 L Ziel, 4 L/h, 1 h → **≈ 28 L** Vorderwürze.

**9. Wasserchemie — Restalkalität und Sulfat:Chlorid.** Zwei Zahlen, die den Maische-pH und den Hopfencharakter bestimmen.
Formeln: RA = Alkalität − (Ca ÷ 3.5 + Mg ÷ 7), alle in ppm; SO₄:Cl = Sulfat ÷ Chlorid.
Excel (Alkalität als CaCO₃ `B2`, Ca `B3`, Mg `B4`, Sulfat `B5`, Chlorid `B6`): RA `=B2-(B3/3.5+B4/7)`, Verhältnis `=B5/B6`.
Salzzugaben (pro Gramm pro Gallone): Gips fügt 61,5 ppm Ca + 147,4 ppm SO₄ hinzu; Calciumchlorid fügt 72 ppm Ca + 127,4 ppm Cl hinzu. Neues Niveau: `=base_ppm + grams_per_gal*61.5`.
Beispiel: Alkalität 100, Ca 50, Mg 10 → RA **84 ppm**; SO₄ 150, Cl 50 → **3.0** (hopfenbetont).

## Kochen und Hopfen

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 620 350" width="100%" style="max-width:620px;height:auto" role="img" aria-label="Tinseth-Hopfenausnutzungskurve, die steil ansteigt und dann bei 60 Minuten Kochzeit abflacht">
<rect x="0" y="0" width="620" height="350" fill="#ffffff"/>
<text x="320" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#06483f">Hopfenausnutzung vs. Kochzeit (Tinseth)</text>
<g stroke="#d8e6e1" stroke-width="1">
<line x1="60" y1="40" x2="580" y2="40"/><line x1="60" y1="170" x2="580" y2="170"/>
</g>
<g stroke="#06483f" stroke-width="1.5"><line x1="60" y1="40" x2="60" y2="300"/><line x1="60" y1="300" x2="580" y2="300"/></g>
<polyline points="60,300 117.8,217.3 175.6,161.9 233.3,124.9 291.1,100.1 406.7,72.1 493.3,61.9 580,56.2" fill="none" stroke="#00695c" stroke-width="3"/>
<g font-family="sans-serif" font-size="12" fill="#4a6b64" text-anchor="middle">
<text x="60" y="318">0</text><text x="233" y="318">30</text><text x="406" y="318">60</text><text x="580" y="318">90</text>
<text x="320" y="340">Kochzeit (Minuten)</text>
</g>
<text x="20" y="170" font-family="sans-serif" font-size="12" fill="#4a6b64" text-anchor="middle" transform="rotate(-90 20 170)">Ausnutzung</text>
<line x1="406" y1="72" x2="470" y2="120" stroke="#06483f" stroke-width="1"/>
<text x="475" y="124" font-family="sans-serif" font-size="12" fill="#06483f">die meiste Bittere</text>
<text x="475" y="140" font-family="sans-serif" font-size="12" fill="#06483f">bis ~60 Min. festgelegt</text>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Warum eine 90-Minuten-Gabe nicht viel bitterer ist als eine 60-Minuten-Gabe (Anwendungsfall 10).</figcaption>
</figure>

**10. IBU nach der Tinseth-Methode.** Die branchenübliche Bitterkeitsschätzung, in zwei Zellen.
Formeln: Ausnutzung = (1.65 × 0.000125^(OG−1)) × ((1 − e^(−0.04·t)) ÷ 4.15); IBU = Ausnutzung × (AA% × Gramm × 1000 ÷ Liter).
Excel (AA% `B2`, Gramm `B3`, Kochmin. `B4`, Liter `B5`, OG `B6`): Ausnutzung in `B7` = `=(1.65*0.000125^(B6-1))*((1-EXP(-0.04*B4))/4.15)`; IBU = `=B7*((B2/100)*B3*1000)/B5`.
Beispiel: 28 g bei 6,4 % AA, 60 Min., 23 L, OG 1.050 → **≈ 18 IBU**.

**11. Hopfenersatz nach Alphasäure.** Ausverkauft? Triff die Bittere, nicht das Gewicht.
Formel: neues Gewicht = (Originalgewicht × Original-AA%) ÷ neues AA%.
Excel (Originalgramm `B2`, Original-AA% `B3`, Ersatz-AA% `B4`): `=(B2*B3)/B4`.
Beispiel: Rezept will 28 g bei 6,4 %; du hast Hopfen mit 9,2 % AA → **19,5 g**.

**12. Bierfarbe (SRM und EBC).** Schätze das Glas, bevor du einmaischst.
Formeln: MCU = Σ(Malz °L × Gewicht lb) ÷ Gallonen; SRM = 1.4922 × MCU^0.6859 (Morey); EBC = SRM × 1.97.
Excel (°L `B2:B3`, Gewichte `C2:C3`, Gallonen `D2`): MCU `E2` = `=SUMPRODUCT(B2:B3,C2:C3)/D2`; SRM `F2` = `=1.4922*E2^0.6859`; EBC = `=F2*1.97`.
Beispiel: 9 lb Pale (3 °L) + 1 lb Crystal (60 °L) in 5,5 gal → MCU 15,8 → **≈ 10 SRM / 19 EBC** (Amber).

## Hefe und Gärung

**13. Hefe-Anstellrate.** Unteranstellen ist der häufigste vermeidbare Fehler; bemiss sie.
Formel: Milliarden Zellen = Anstellrate (Mio. Zellen/mL/°P) × Volumen (L) × °Plato. Rate ≈ 0,75 für Ales, 1,5 für Lager.
Excel (Rate `B2`, Liter `B3`, °P `B4`): Zellen `=B2*B3*B4`; Packs zu je 100 Mrd. `=B2*B3*B4/100`.
Beispiel: Ale bei 0,75, 23 L, 12 °P → **207 Milliarden Zellen** ≈ 2 frische Packs oder ein Starter.

**14. Scheinbarer und realer Vergärungsgrad.** Wie weit die Hefe tatsächlich kam.
Formeln: scheinbar = (OG − FG) ÷ (OG − 1) × 100; real ≈ scheinbar × 0.81 (der echte reale Grad nutzt den realen Extrakt aus Plato).
Excel (OG `B2`, FG `B3`): scheinbar `=(B2-B3)/(B2-1)*100`; real `=(B2-B3)/(B2-1)*100*0.81`.
Beispiel: 1.050 → 1.010 → **80 % scheinbar / ≈ 65 % real**.

**15. Refraktometer-Endvergärungs-Korrektur.** Refraktometer lügen, sobald Alkohol vorhanden ist; das behebt es.
Formel: Terrill-Kubik in anfänglichem und finalem Brix (teile zuerst jede Ablesung durch deinen Würze-Korrekturfaktor, ~1,04).
Excel (korrigiertes Anfangs-Brix `B2`, korrigiertes End-Brix `B3`): `=1.0000-0.0044993*B2+0.011774*B3+0.00027581*B2^2-0.0012717*B3^2-0.00000728*B2^3+0.000063293*B3^3`.
Beispiel: 12,5 → 6,0 Brix → FG **≈ 1.011**.

**16. ABV aus der Dichte.** Die Schlagzeilenzahl, auf zwei Wegen.
Formeln: einfach = (OG − FG) × 131.25; genauer (stärkere Biere) = (76.08 × (OG − FG) ÷ (1.775 − OG)) × (FG ÷ 0.794).
Excel (OG `B2`, FG `B3`): einfach `=(B2-B3)*131.25`; genau `=(76.08*(B2-B3)/(1.775-B2))*(B3/0.794)`.
Beispiel: 1.050 → 1.011 → **5,1 % (einfach) / 5,2 % (genau)**.

## Abfüllung und Finish

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 560 300" width="100%" style="max-width:560px;height:auto" role="img" aria-label="Pearson-Quadrat zum Verschneiden zweier Biere auf einen Ziel-ABV">
<rect x="0" y="0" width="560" height="300" fill="#ffffff"/>
<text x="280" y="28" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#06483f">Pearson-Quadrat — auf ein Ziel verschneiden</text>
<rect x="170" y="60" width="220" height="180" fill="none" stroke="#00695c" stroke-width="1.5"/>
<line x1="170" y1="60" x2="390" y2="240" stroke="#d8e6e1" stroke-width="1.5"/>
<line x1="170" y1="240" x2="390" y2="60" stroke="#d8e6e1" stroke-width="1.5"/>
<rect x="232" y="128" width="96" height="44" rx="6" fill="#00695c"/>
<text x="280" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#ffffff">ZIEL</text>
<text x="280" y="164" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">5.0%</text>
<text x="178" y="84" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">A: 6.5%</text>
<text x="178" y="232" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">B: 3.0%</text>
<text x="382" y="84" text-anchor="end" font-family="sans-serif" font-size="13" fill="#06483f">Teile A = 5.0−3.0 = 2.0</text>
<text x="382" y="232" text-anchor="end" font-family="sans-serif" font-size="13" fill="#06483f">Teile B = 6.5−5.0 = 1.5</text>
<text x="280" y="278" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#06483f">Verschneide 2.0 : 1.5 (A : B) → 5.0% ✓</text>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Pearson-Quadrat (Anwendungsfall 18): Jede Ecke subtrahiert diagonal, um das Verschnittverhältnis zu ergeben.</figcaption>
</figure>

**17. Speisezucker für die Flaschenkarbonisierung.** Triff ein CO₂-Ziel ohne Flaschenbomben.
Formeln: Rest-CO₂ (Vol.) = 3.0378 − 0.050062·T + 0.00026555·T² (T = höchste Temperatur, die das Bier sah, °F); Traubenzucker (g) = (Ziel-Vol. − Rest) × Liter × 4.0.
Excel (Max.-Temp. °F `B2`, Ziel-Vol. `B3`, Liter `B4`): Rest `B5` = `=3.0378-0.050062*B2+0.00026555*B2^2`; Zucker = `=(B3-B5)*B4*4.0`.
Beispiel: 68 °F, Ziel 2,4 Vol., 23 L → Rest 0,86 → **≈ 141 g Traubenzucker**. (Haushaltszucker: × 0,91.)

**18. Verschneiden oder Verdünnen auf ein Ziel.** Eine hochgrädige Würze mit Wasser trimmen oder zwei Biere auf eine Zahl vermählen.
Verdünnungsformel: hinzuzufügendes Wasser = Volumen × (aktuelle Punkte − Zielpunkte) ÷ Zielpunkte.
Excel (Volumen `B2`, aktuelle Punkte `B3`, Zielpunkte `B4`): `=B2*(B3-B4)/B4`.
Beispiel: 25 L bei 1.060 (60 Pkt.) herunter auf 1.050 (50 Pkt.) → füge **5 L Wasser** hinzu. Zum Verschneiden zweier fertiger Biere auf einen Ziel-ABV nutze das Pearson-Quadrat oben: Teile = die diagonalen Differenzen.

**19. Kalorien pro Portion.** Eine Etikettzahl, nach der das Marketing immer fragt.
Formeln (pro 12 oz / 355 mL): Alkohol-Kal = 1881.22 × FG × (OG − FG) ÷ (1.775 − OG); Kohlenhydrat-Kal = 3550 × FG × ((0.1808 × OG) + (0.8192 × FG) − 1.0004); Gesamt = Summe.
Excel (OG `B2`, FG `B3`): Alkohol `=1881.22*B3*(B2-B3)/(1.775-B2)`; Kohlenhydrate `=3550*B3*((0.1808*B2)+(0.8192*B3)-1.0004)`; skaliere nach Portionsgröße ab 355 mL.
Beispiel: 1.050 → 1.011 → ≈ 102 (Alkohol) + 64 (Kohlenhydrate) = **≈ 166 Kal** pro 12 oz.

## Kalkulation

**20. Herstellkosten pro Hektoliter und pro Pint.** Wo Rezeptmathematik auf die Gewinn- und Verlustrechnung trifft.
Formeln: COGS/hL = gesamte Chargenkosten ÷ Chargenvolumen (hL); Kosten/Pint = COGS/hL × 0.00568 (ein britisches Pint sind 0,568 L; 1 hL = 100 L).
Excel (gesamte Chargenkosten `B2`, Charge hL `B3`): COGS/hL `B4` = `=B2/B3`; Kosten/Pint = `=B4*0.00568`.
Beispiel: £450 Charge, 10 hL → **£45/hL ≈ £0,26 pro Pint**. Bau es sauber auf mit der Methode in [Herstellkosten pro Hektoliter]({{ '/de/2025/cost-of-goods-per-hectoliter/' | relative_url }}).

## Das Fazit

Diese 20 Formeln decken den Brautag von Anfang bis Ende ab: Rezeptgestaltung, Maische und Wasser, Kochen und Hopfen, Gärung, Abfüllung und Kosten. Keine braucht ein Add-in — füge sie in ein Blatt ein, beschrifte deine Input-Zellen, und du hast einen Sudhaus-Rechner, der seinen Rechenweg zeigt und den du Zeile für Zeile prüfen kannst. Halte die Inputs ehrlich (wiegen, messen, aufzeichnen) und die Mathematik wird jedes Mal stimmen; genau diese Disziplin macht den Sprung [vom Brauer zum Data Scientist]({{ '/de/2026/from-brewer-to-data-scientist/' | relative_url }}) zu einem kurzen, wenn du dafür bereit bist.

## Häufig gestellte Fragen

**Kann man ABV in Excel berechnen?**
Ja. Die Standardformel lautet =(OG-FG)*131.25, wobei OG und FG deine Stammwürze- und Endvergärungsdichte (spezifisches Gewicht) sind. Für stärkere Biere ist eine genauere Variante =(76.08*(OG-FG)/(1.775-OG))*(FG/0.794). Beide funktionieren in jeder Excel-Version ohne Add-ins.

**Wie lautet die Excel-Formel für die Einmaisch-Wassertemperatur?**
Einmaischtemperatur Tw = (0.2/R)(T2-T1)+T2, wobei R das Wasser-zu-Schüttung-Verhältnis in Quarts pro Pound ist, T1 die Schüttungstemperatur und T2 deine Zielmaischtemperatur in °F. In Excel: =(0.2/B2)*(B4-B3)+B4 mit R in B2, Schüttungstemperatur in B3 und Ziel in B4. Für metrisch (L/kg, °C) ersetze die 0.2 durch 0.41.

**Brauche ich spezielle Brausoftware für diese Berechnungen?**
Nein. Jede Berechnung hier — Dichte, Effizienz, IBU, Farbe, Anstellrate, Karbonisierung, ABV — ist nur Arithmetik, die Brausoftware unter der Haube ausführt. Ein einziges Excel-Blatt mit diesen Formeln bildet das nach, und weil du jede Zelle sehen kannst, verstehst du das Ergebnis und vertraust ihm.

*Teil des [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }})-Tracks.*
