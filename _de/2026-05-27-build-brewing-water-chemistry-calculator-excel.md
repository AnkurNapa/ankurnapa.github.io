---
layout: post
lang: de
title: "Einen Rechner für Brauwasser-Chemie in Excel bauen"
image: /assets/og/build-brewing-water-chemistry-calculator-excel.png
description: "Ein Schritt-für-Schritt-Excel-Wasserrechner für Brauer: Gib dein Ausgangsprofil ein, füge Salze hinzu und lies Calcium, Sulfat, Chlorid, Restalkalität und das Sulfat-zu-Chlorid-Verhältnis ab."
date: 2026-05-27 09:00:00 -0700
updated: 2026-05-27
permalink: /de/2026/build-brewing-water-chemistry-calculator-excel/
tags: [brewing-science, excel, water-chemistry, recipe-formulation]
faq:
  - q: "Wie berechne ich Brausalz-Zugaben in Excel?"
    a: "Baue eine Tabelle, in der die Gramm jedes Salzes mit seinem ppm-pro-Gramm-pro-Liter-Beitrag multipliziert, summiert und durch dein gesamtes Wasservolumen geteilt werden. Zum Beispiel fügt Gips 232,8 ppm Calcium und 557,9 ppm Sulfat pro Gramm pro Liter hinzu, also gibt =source_ppm+(gypsum_g*232.8)/litres deinen neuen Calciumwert."
  - q: "Was ist Restalkalität und wie ermittle ich sie?"
    a: "Restalkalität (RA) ist die Alkalität, die dein Calcium und Magnesium nicht ausgleichen können, und sie treibt den Maische-pH-Wert. Die Formel ist RA = Alkalität − (Calcium ÷ 3,5 + Magnesium ÷ 7), alles in ppm als CaCO₃. In Excel: =B2-(B3/3.5+B4/7)."
  - q: "Welches Sulfat-zu-Chlorid-Verhältnis sollte ich anstreben?"
    a: "Unter ~0,5 neigt es zu malzig, um 1 ist es ausgewogen, und über ~2 betont es Hopfenbittere und Trockenheit. Es ist ein Verhältnis, keine Zielkonzentration, daher können zwei Wässer mit sehr unterschiedlichen Mineralwerten dieselbe Balance teilen. Berechne es als =sulfate/chloride."
---

**Kurze Antwort: Ein Brauwasser-Rechner ist nur eine Salzzugabe-Tabelle plus vier Auslese-Formeln. Gib dein Ausgangswasserprofil ein, tippe Gramm jedes Brausalzes ein, und Excel gibt deine fertigen Calcium-, Magnesium-, Natrium-, Sulfat- und Chloridwerte zurück, die Restalkalität, die den Maische-pH-Wert setzt, und das Sulfat-zu-Chlorid-Verhältnis, das die Malz-Hopfen-Balance setzt. Keine Add-ins, und du kannst genau sehen, wie sich jede Zahl bewegt.**

Das erweitert Anwendungsfall 9 aus dem Pfeiler [20 Brauberechnungen in Excel]({{ '/de/2026/advanced-brewing-calculations-excel/' | relative_url }}) zu einem vollständigen Blatt, das du neben dem Sudhaus aufbewahren kannst. Es ist der manuelle, transparente Vetter der [KI-Wasserchemie-Modelle]({{ '/de/2023/ai-brewing-water-chemistry-optimization/' | relative_url }}) — dieselbe Arithmetik, voll sichtbar.

## Schritt 1 — das Ausgangswasser anlegen

Setze deinen Wasserbericht über eine Zeile, in ppm: Calcium (Ca), Magnesium (Mg), Natrium (Na), Sulfat (SO₄), Chlorid (Cl) und Alkalität (als CaCO₃). Wenn du auf RO- oder destilliertem Wasser braust, ist jede Zelle null, und du baust das Profil von Grund auf — der am einfachsten zu modellierende Fall. Setze dein gesamtes behandeltes Volumen (Maische plus Nachguss, in Litern) in eine eigene Zelle; dieser eine Nenner treibt das ganze Blatt.

## Schritt 2 — die Salzbeitrags-Tabelle

Jedes Salz löst sich auf und fügt eine feste Menge jedes Ions pro Gramm pro Liter hinzu. Hardcode diese Tabelle einmal:

| Salz | Fügt hinzu (ppm pro g/L) |
|---|---|
| Gips (CaSO₄·2H₂O) | Ca +232,8, SO₄ +557,9 |
| Calciumchlorid (CaCl₂·2H₂O) | Ca +272,6, Cl +482,3 |
| Bittersalz (MgSO₄·7H₂O) | Mg +98,6, SO₄ +389,7 |
| Speisesalz (NaCl) | Na +393,4, Cl +606,6 |
| Natron (NaHCO₃) | Na +273,6, Alkalität +595 |

Der Beitrag eines Salzes zur Charge ist `Gramm × ppm-pro-g/L ÷ Liter`. Calcium nach den Zugaben ist also die Quelle plus jedes calciumhaltige Salz:

`=Ca_source + (gypsum_g*232.8 + cacl2_g*272.6)/litres`

Wiederhole das Muster für jedes Ion (Sulfat bekommt Gips und Bittersalz; Chlorid bekommt Calciumchlorid und Salz; und so weiter). Lege die Salz-Gramm in eigene Eingabezellen, damit du sie einstellen kannst, während du die Auslesewerte sich ändern siehst.

Durchgerechnetes Beispiel: 5 g Gips in 30 L heben Calcium um `5*232.8/30 = 38,8 ppm` und Sulfat um `5*557.9/30 = 93 ppm`.

## Schritt 3 — die vier Auslesewerte, auf die es ankommt

Mit den fertigen Ionenwerten an Ort und Stelle sagen dir vier Formeln, ob das Wasser zum Bier passt.

- **Restalkalität** (setzt den Maische-pH-Wert): `=alkalinity-(Ca/3.5+Mg/7)`. Helle, hopfige Biere wollen niedrige oder negative RA; dunkle Biere vertragen oder brauchen sogar positive RA, damit die Säure des gerösteten Malzes etwas zum Gegenhalten hat.
- **Sulfat-zu-Chlorid-Verhältnis** (setzt die Balance): `=SO4/Cl`. Siehe das Spektrum unten.
- **Gesamt-Calcium** (Prozessgesundheit): ziele auf grob 50–150 ppm — Calcium senkt den Maische-pH-Wert, hilft der Klarheit, unterstützt die Hefeflockung und schützt am oberen Ende vor Bierstein-Problemen.
- **Prüfung der effektiven Härte**: Natrium unter ~150 ppm und Magnesium unter ~30 ppm zu halten, vermeidet einen mineralischen, harschen Abgang.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 760 180" width="100%" style="max-width:760px;height:auto" role="img" aria-label="Sulfat-zu-Chlorid-Verhältnis-Spektrum von malzig über ausgewogen bis hopfig">
<rect x="0" y="0" width="760" height="180" fill="#ffffff"/>
<text x="380" y="30" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="700" fill="#06483f">Sulfat : Chlorid-Verhältnis — der Malz-Hopfen-Regler</text>
<rect x="60" y="70" width="80" height="40" fill="#06483f"/>
<rect x="140" y="70" width="80" height="40" fill="#4db6a2"/>
<rect x="220" y="70" width="160" height="40" fill="#00695c"/>
<rect x="380" y="70" width="320" height="40" fill="#2e9e7c"/>
<polygon points="540,62 533,52 547,52" fill="#06483f"/>
<text x="540" y="46" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#06483f">du: 3.0</text>
<g font-family="sans-serif" font-size="12" fill="#4a6b64" text-anchor="middle">
<text x="100" y="128">0.5</text><text x="220" y="128">1.0</text><text x="380" y="128">2.0</text><text x="700" y="128">4.0</text>
</g>
<g font-family="sans-serif" font-size="13" font-weight="700" text-anchor="middle">
<text x="100" y="152" fill="#06483f">malzig</text><text x="300" y="152" fill="#00695c">ausgewogen</text><text x="540" y="152" fill="#2e9e7c">hopfig / trocken</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Das Verhältnis, nicht die absoluten Werte, setzt die wahrgenommene Balance. Ein Pale Ale sitzt bequem bei 2–4; ein malziges Lager nahe 0,5.</figcaption>
</figure>

## Wo das Blatt nur eine Schätzung ist

Zwei ehrliche Vorbehalte. Erstens: **Der Maische-pH-Wert ist das Ziel, nicht diese Ionen direkt** — RA und Calcium sagen die *Richtung* voraus, in die sich der pH-Wert bewegt, aber Schüttungsfarbe und -säure zählen genauso viel, daher ist die einzige Wahrheit eine kalibrierte pH-Meter-Ablesung bei Maischetemperatur. Ein vollständiges pH-Modell braucht die Säure jedes Malzes, was mehr ist, als ein einzeiliges Blatt trägt. Zweitens: **Kreide (CaCO₃) löst sich kaum** in einer kalten Maische, daher überschätzt jedes Blatt, das dich Kreide hinzufügen lässt, als wäre sie voll löslich, die Alkalität, die du tatsächlich bekommst; bevorzuge Natron zum Anheben der Alkalität und Säure (nicht Subtraktion) zum Senken. Behandle die Auslesewerte als ein Rezeptziel, das du dann mit einem Messgerät bestätigst.

## Das Fazit

Ein nützlicher Brauwasser-Rechner besteht aus drei Dingen: einer Quellzeile, einer Salztabelle und vier Auslese-Formeln. Baue ihn einmal, und du kannst in Minuten ein Wasserprofil für jeden Stil entwerfen, sofort sehen, wie 2 Gramm Gips die Balance verschieben, und aufhören zu raten. Denk nur daran, dass das Blatt *Zugaben* präzise und den *Maische-pH-Wert* nur näherungsweise vorhersagt — halte ein Messgerät in der Schleife.

## Häufig gestellte Fragen

**Wie berechne ich Brausalz-Zugaben in Excel?**
Baue eine Tabelle, in der die Gramm jedes Salzes mit seinem ppm-pro-Gramm-pro-Liter-Beitrag multipliziert, summiert und durch dein gesamtes Wasservolumen geteilt werden. Zum Beispiel fügt Gips 232,8 ppm Calcium und 557,9 ppm Sulfat pro Gramm pro Liter hinzu, also gibt =source_ppm+(gypsum_g*232.8)/litres deinen neuen Calciumwert.

**Was ist Restalkalität und wie ermittle ich sie?**
Restalkalität (RA) ist die Alkalität, die dein Calcium und Magnesium nicht ausgleichen können, und sie treibt den Maische-pH-Wert. Die Formel ist RA = Alkalität − (Calcium ÷ 3,5 + Magnesium ÷ 7), alles in ppm als CaCO₃. In Excel: =B2-(B3/3.5+B4/7).

**Welches Sulfat-zu-Chlorid-Verhältnis sollte ich anstreben?**
Unter ~0,5 neigt es zu malzig, um 1 ist es ausgewogen, und über ~2 betont es Hopfenbittere und Trockenheit. Es ist ein Verhältnis, keine Zielkonzentration, daher können zwei Wässer mit sehr unterschiedlichen Mineralwerten dieselbe Balance teilen. Berechne es als =sulfate/chloride.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).*
