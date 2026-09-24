---
layout: post
lang: de
title: "Ein Agent, der Rechenwerkzeuge aufruft, statt selbst zu rechnen"
image: /assets/og/brewing-agent-calculation-tools-not-sums.png
description: "Teil 2 von The Brewer's Agent. Gib einem Brau-Assistenten Werkzeuge für Stammwürze, Vergärungsgrad, ABV und IBU, und lass ihn jedes Mal die Methode nennen. Durchgerechnete Beispiele zeigen, warum: Dasselbe Bier ist auf einer Skala zu 64,9% vergoren und auf einer anderen zu 78,6%, und drei IBU-Modelle liefern für eine einzige Hopfengabe 34, 45 und 46."
date: 2026-08-26 09:00:00 -0700
updated: 2026-08-26
permalink: /de/2026/brewing-agent-calculation-tools-not-sums/
tags: [brewing-science, brewers-agent, generative-ai, tool-use, brewing-calculations]
faq:
  - q: "Warum sollte ein KI-Brau-Assistent für Berechnungen Werkzeuge nutzen?"
    a: "Weil Sprachmodelle bei mehrstufiger Arithmetik unzuverlässig sind und Brauformeln Einheiten- und Temperaturkonventionen mitbringen, die leicht verwechselt werden. Ein Werkzeug ist gewöhnlicher, getesteter Code: Es nimmt Eingaben in festgelegten Einheiten entgegen, wendet eine dokumentierte Methode an und gibt das Ergebnis mit dem Namen dieser Methode zurück. Das Modell entscheidet, welches Werkzeug es aufruft, und erklärt die Antwort."
  - q: "Was ist der Unterschied zwischen wirklichem und scheinbarem Vergärungsgrad?"
    a: "Der scheinbare Vergärungsgrad vergleicht die Stammwürze mit dem scheinbaren Extrakt, den ein Aräometer im fertigen Bier anzeigt und den der Alkohol nach unten zieht, weil er leichter als Wasser ist. Der wirkliche Vergärungsgrad verwendet den tatsächlich verbliebenen Extrakt. Beim selben Bier ist der scheinbare Wert immer höher, hier 78,6% gegenüber 64,9%, deshalb ist eine Zahl ohne ihre Skala mehrdeutig."
  - q: "Welche IBU-Formel ist richtig, Tinseth oder Rager?"
    a: "Keine ist allgemein richtig. Beide sind empirische Anpassungen an unterschiedliche Daten, und für eine 60-Minuten-Gabe in einer Würze mit 13 Grad Plato liegen sie um etwa ein Drittel auseinander. Wähle eine für deine Brauerei, kalibriere sie gegen im Labor gemessene Bittere und lass das Werkzeug angeben, welches Modell es verwendet hat."
---

**Kurze Antwort: Das Nützlichste, was du für einen Brau-Assistenten tun kannst, ist, ihm das Rechnen abzunehmen. Gib dem Agenten eine kleine Zahl von Werkzeugen (Umrechnung der Dichte, Vergärungsgrad, Alkohol, Bittere), jedes davon gewöhnlicher, getesteter Code, der in Basiseinheiten arbeitet und seine Methode zusammen mit dem Ergebnis zurückgibt. Der Agent wählt das Werkzeug und erklärt die Antwort. Die beiden durchgerechneten Beispiele unten zeigen, warum die Methode mit der Zahl reisen muss: Ein Bier ist auf der wirklichen Skala zu 64,9% vergoren und auf der scheinbaren zu 78,6%, und drei anerkannte IBU-Modelle liefern für dieselbe Hopfengabe 34, 45 und 46.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Zwei durchgerechnete Beispiele. Links zeigt ein Bier mit 13,0 Grad Plato Stammwürze einen wirklichen Vergärungsgrad von 64,9 Prozent und einen scheinbaren Vergärungsgrad von 78,6 Prozent, eine Differenz von 13,7 Punkten beim selben Bier. Rechts ergibt eine Hopfengabe von 30 Gramm mit 10 Prozent Alphasäure in 20 Litern, 60 Minuten gekocht, 33,8 IBU nach Tinseth, 45,7 nach Rager und 45,2 nach einem kinetischen Modell erster Ordnung.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">GLEICHES BIER, ANDERE ZAHLEN: WARUM DIE METHODE MIT DEM ERGEBNIS REIST</text>
<g font-family="sans-serif">
<text x="245" y="60" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">VERGÄRUNGSGRAD, EIN BIER (13.0 &#176;P)</text>
<rect x="60" y="90" width="260" height="36" rx="5" fill="#4db6a2"/>
<text x="70" y="113" font-size="12" font-weight="700" fill="#06483f">wirklich (Vw)</text>
<text x="330" y="113" font-size="13" font-weight="700" fill="#06483f">64.9%</text>
<rect x="60" y="140" width="314" height="36" rx="5" fill="#06483f"/>
<text x="70" y="163" font-size="12" font-weight="700" fill="#ffffff">scheinbar (Vs)</text>
<text x="384" y="163" font-size="13" font-weight="700" fill="#06483f">78.6%</text>
<text x="245" y="208" text-anchor="middle" font-size="11" fill="#ff4081" font-weight="700">13,7 Punkte auseinander, gleicher Tank</text>
<text x="745" y="60" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">IBU, EINE HOPFENGABE</text>
<text x="745" y="76" text-anchor="middle" font-size="10" fill="#4a6b64">30 g mit 10% Alpha, 20 L, 60 min</text>
<rect x="560" y="90" width="203" height="36" rx="5" fill="#4db6a2"/>
<text x="570" y="113" font-size="12" font-weight="700" fill="#06483f">Tinseth</text>
<text x="773" y="113" font-size="13" font-weight="700" fill="#06483f">33.8</text>
<rect x="560" y="140" width="274" height="36" rx="5" fill="#4db6a2"/>
<text x="570" y="163" font-size="12" font-weight="700" fill="#06483f">Rager</text>
<text x="844" y="163" font-size="13" font-weight="700" fill="#06483f">45.7</text>
<rect x="560" y="190" width="271" height="36" rx="5" fill="#4db6a2"/>
<text x="570" y="213" font-size="12" font-weight="700" fill="#06483f">kinetisches Modell</text>
<text x="841" y="213" font-size="13" font-weight="700" fill="#06483f">45.2</text>
<rect x="40" y="258" width="920" height="54" rx="10" fill="#06483f"/>
<text x="500" y="282" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">KEINE DIESER ZAHLEN IST FALSCH &#183; JEDE IST OHNE IHRE METHODE BEDEUTUNGSLOS</text>
<text x="500" y="300" text-anchor="middle" font-size="10.5" fill="#cfe6df">berechnet mit getestetem Code in Basiseinheiten; IBU-Werte sind Würzeschätzungen vor Verlusten im Keller</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein Assistent, der "der Vergärungsgrad ist 78%" oder "etwa 40 IBU" ohne Methode sagt, hat die Frage nicht beantwortet.</figcaption>
</figure>

Ein Brauer fragt den Assistenten: "Welchen Vergärungsgrad hat Sud 212 erreicht?" Die ehrliche Antwort ist eine Gegenfrage: welchen Vergärungsgrad? Ein Laborbericht gibt meist den wirklichen Vergärungsgrad an. Ein Hobbybrauer oder ein Verkaufsblatt meint meist den scheinbaren. Beim Bier in der Abbildung sind das 64,9% und 78,6%. Gleicher Tank, gleicher Tag, gleiche Probe.

Ein Sprachmodell, das sich selbst überlassen ist, wählt stillschweigend einen der beiden Werte und rechnet unterwegs vielleicht noch im Kopf um. Der [erste Beitrag dieser Serie]({{ '/de/2026/rag-brewing-literature-without-hallucinated-maths/' | relative_url }}) hat argumentiert, dass Retrieval das Wissen liefern sollte und Code die Zahlen. Dieser Beitrag baut den Code.

## Was ein Werkzeug ist

In aktuellen Agenten-Frameworks (den APIs von Claude und OpenAI, dem Model Context Protocol, den meisten Orchestrierungsbibliotheken) ist ein Werkzeug eine Funktion, deren Ausführung das Modell anfordern kann. Du beschreibst sie mit einem Namen, einem Zweck und einem Schema für die Eingaben. Das Modell entscheidet, wann es sie aufruft und mit welchen Argumenten. Dein Code führt sie aus und gibt das Ergebnis zurück.

Ein Werkzeugkasten fürs Brauen muss nicht groß sein. Fünf Werkzeuge decken die meisten Fragen ab:

- **`gravity_convert`**: spezifisches Gewicht in Grad Plato und zurück, auf einer angegebenen Temperaturbasis.
- **`attenuation`**: wirklicher und scheinbarer Vergärungsgrad aus Stammwürze, wirklichem und scheinbarem Extrakt.
- **`alcohol`**: Alkohol in Gewichts- und Volumenprozent aus Stammwürze und wirklichem Vergärungsgrad.
- **`bitterness`**: IBU für eine Hopfengabe, mit dem Modell als benanntem Argument.
- **`unit_convert`**: Liter, Hektoliter, Barrel, Kilogramm, Pfund, ohne Raten.

So sieht eines davon für das Modell aus:

```json
{
  "name": "bitterness",
  "description": "Estimate IBU in wort for one hop addition. Returns the value and the model used.",
  "input_schema": {
    "type": "object",
    "properties": {
      "hop_mass_g": {"type": "number"},
      "alpha_acid_pct": {"type": "number"},
      "volume_l": {"type": "number"},
      "boil_min": {"type": "number"},
      "wort_plato": {"type": "number"},
      "model": {"type": "string", "enum": ["tinseth", "rager", "kinetic"]}
    },
    "required": ["hop_mass_g", "alpha_acid_pct", "volume_l", "boil_min", "wort_plato", "model"]
  }
}
```

Das Feld `model` ist absichtlich ein Pflichtfeld. Der Assistent kann also nicht nach "den IBU" fragen. Er muss nach den IBU nach Tinseth oder nach Rager fragen. Diese eine Designentscheidung bringt mehr für die Genauigkeit als jeder Prompt.

## Beispiel 1: die Falle der Vergärungsgrad-Skala

Nimm ein Lagerbier mit 13,0 Grad Plato Stammwürze, vergoren auf einen wirklichen Vergärungsgrad von 64,9%.

Das Alkohol-Werkzeug verwendet die Konvention nach Balling (jedes Gramm Alkohol verbraucht etwa 2,0665 Gramm Extrakt) und kommt auf einen wirklichen Extrakt von 4,77% und einen Alkoholgehalt von 4,27 Gewichtsprozent. Um von Gewicht auf Volumen zu kommen, braucht es die Dichte des fertigen Biers, die vom verbliebenen Extrakt und vom Alkohol gemeinsam abhängt. Deshalb verwendet es ein angepasstes Modell der Bierdichte statt einer Faustformel. Das ergibt ein spezifisches Gewicht von etwa 1,0109 und einen Alkoholgehalt von **5,46% ABV**.

Das Vergärungsgrad-Werkzeug berechnet dann, was ein Aräometer in diesem Bier anzeigen würde. Alkohol ist leichter als Wasser, also zeigt das Aräometer einen scheinbaren Extrakt von etwa 2,78 Grad Plato, deutlich unter den wirklichen 4,77. Der scheinbare Vergärungsgrad vergleicht die Stammwürze mit diesem Messwert: **78,6%**. Der wirkliche Vergärungsgrad vergleicht sie mit dem tatsächlich verbliebenen Extrakt: **64,9%**.

Beide Zahlen stimmen. Sie messen verschiedene Dinge. Ein Brauer, der dieses Bier mit dem Datenblatt eines Hefelieferanten vergleicht, das den scheinbaren Vergärungsgrad angibt, und mit dem Laborbericht, der den wirklichen angibt, sieht eine Lücke von 13,7 Punkten und fragt sich, was schiefgelaufen ist. Nichts ist schiefgelaufen. Jemand hat die Beschriftung weggelassen.

Ein gutes Werkzeug gibt beide zurück, jeweils benannt:

```text
attenuation(og_plato=13.0, rdf_pct=64.9)
  -> real_df_pct: 64.9, apparent_df_pct: 78.6,
     real_extract_plato: 4.77, apparent_extract_plato: 2.78,
     method: "Balling 2.0665; beer SG from extract-alcohol density model; 20/20 C"
```

## Beispiel 2: drei ehrliche IBU-Zahlen

Jetzt eine Hopfengabe: 30 Gramm eines Hopfens mit 10% Alphasäure, 60 Minuten gekocht in 20 Litern derselben Würze mit 13,0 Grad Plato (spezifisches Gewicht etwa 1,0525).

- **Tinseth** ergibt etwa 22,5% Ausnutzung und **33,8 IBU**.
- **Rager** ergibt etwa 30,4% Ausnutzung und **45,7 IBU**.
- Ein **kinetisches Modell erster Ordnung** für Isomerisierung und Abbau der Alphasäure (die Geschwindigkeitskonstanten von Malowicki und Shellhammer am Siedepunkt, mit einer Korrektur für die Dichte) ergibt etwa 30,1% isomerisierte Alphasäure in der Würze und **45,2 IBU**.

Drei veröffentlichte, weit verbreitete Methoden. Eine Spanne von etwa 12 IBU, rund ein Drittel, bei einer einzigen Gabe. Wechsle zu einer 15-Minuten-Gabe, und die Reihenfolge dreht sich um: Tinseth ergibt 11,2% Ausnutzung und Rager 8,1%.

Keine davon ist die Wahrheit. Es sind empirische Modelle, angepasst an unterschiedliche Daten, und jedes davon ist eine Schätzung in der Würze, bevor Keller- und Abfüllverluste ihren Anteil nehmen. Die Wahrheit ist das, was ein Labor im fertigen Bier misst. Für einen Assistenten zählt, dass er niemals "etwa 40 IBU" meldet, als wäre damit etwas geklärt. Er meldet "45,7 IBU nach Rager, Würzeschätzung", und ein Brauer, der gegen Tinseth kalibriert, weiß sofort, dass er den Wert abschlagen muss.

Wenn du diese Modelle nebeneinander in einer Tabelle sehen willst, geht der [IBU-Rezeptrechner in Excel]({{ '/de/2026/ibu-recipe-builder-excel/' | relative_url }}) Tinseth für mehrere Gaben durch, und [Hopfenbittere mit Machine Learning vorhersagen]({{ '/de/2023/predicting-hop-bitterness-ibu/' | relative_url }}) behandelt die Kalibrierung gegen Messwerte.

## Die Regeln, die den Agenten vertrauenswürdig machen

1. **Keine Arithmetik im Fließtext.** Der System-Prompt legt fest, dass jede Zahl, die aus anderen Zahlen abgeleitet ist, aus einem Werkzeugaufruf stammen muss. Teste das mit Fragen, die das Modell zur Abkürzung verleiten, und lass jede Antwort durchfallen, die eine berechnete Zahl ohne dahinterliegenden Werkzeugaufruf enthält.
2. **Basiseinheiten innen, Anzeigeeinheiten außen.** Werkzeuge arbeiten in Kilogramm, Litern und Grad Plato auf einer angegebenen Temperaturbasis. Die Umrechnung in Pfund, Barrel oder spezifisches Gewicht passiert einmal, am Rand.
3. **Die Methode ist Teil der Ausgabe.** Jedes Werkzeug gibt die verwendete Methode, die Konstanten und die Temperaturbasis zurück, und der Agent wiederholt sie in der Antwort.
4. **Werkzeuge werden getestet wie jeder andere Code.** Jedes Werkzeug hat Unit-Tests gegen veröffentlichte Rechenbeispiele. Das Vergärungsbeispiel oben ist eines davon: Wenn das Werkzeug für diese Eingabe nicht mehr 4,77 wirklichen Extrakt und 4,27 Alkohol zurückgibt, schlägt der Build fehl.
5. **Fragen statt annehmen.** Sagt der Brauer "Vergärungsgrad" oder "Dichte" ohne Skala, fragt der Agent nach, welche gemeint ist, oder antwortet mit beiden.

## Wo das an Grenzen stößt

**Werkzeuge kodieren Entscheidungen.** Die Wahl der Konstante nach Balling, eines Dichtemodells oder eines Ausnutzungsmodells ist eine fachliche Entscheidung. Das Werkzeug macht sie konsistent, nicht richtig. Dokumentiere die Entscheidungen und lass einen Brauer, der es besser weiß, sie ändern.

**Schlechte Eingaben liefern weiterhin schlechte Ergebnisse.** Ein Werkzeug, das eine bei falscher Temperatur abgelesene Stammwürze bekommt, gibt eine präzise falsche Antwort zurück. Der Agent sollte nachfragen, woher die Zahlen stammen, wenn sie außerhalb des üblichen Bereichs liegen.

**Der Agent kann das falsche Werkzeug aufrufen.** Ein Modell kann `alcohol` wählen, wo es `attenuation` gebraucht hätte, oder Plato übergeben, wo das spezifische Gewicht erwartet wurde. Strikte Schemas mit Einheiten in den Feldnamen und ein Testsatz echter Fragen fangen das meiste davon ab.

**Werkzeuge ersetzen nicht das Labor.** Jede Zahl hier ist eine Berechnung aus anderen Messwerten. Gerade die Bittere sollte gemessen werden, und der berechnete Wert gilt als Planungsschätzung.

## Das Fazit

Ein Assistent, der im Kopf rechnet, wird einem Brauer irgendwann eine falsche Zahl mit selbstsicherer Stimme geben. Ein Assistent, der Werkzeuge aufruft, gibt jedes Mal dieselbe Zahl, mit angehängter Methode. Die Beispiele hier sind keine Randfälle: Wirklicher und scheinbarer Vergärungsgrad liegen bei einem gewöhnlichen Lagerbier 13,7 Punkte auseinander, und drei Standard-IBU-Modelle streuen bei einer einzigen Hopfengabe um ein Drittel. Lass das Modell das Werkzeug wählen und das Ergebnis erklären. Lass getesteten Code die Mathematik machen.

Als Nächstes in der Serie: [Malz-Aromaräder als Vektoren]({{ '/de/2026/malt-aroma-wheels-as-vectors-similarity-search/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite von The Brewer's Agent]({{ '/series/brewers-agent/' | relative_url }}).

## Häufig gestellte Fragen

**Warum sollte ein KI-Brau-Assistent für Berechnungen Werkzeuge nutzen?**
Weil Sprachmodelle bei mehrstufiger Arithmetik unzuverlässig sind und Brauformeln Einheiten- und Temperaturkonventionen mitbringen, die leicht verwechselt werden. Ein Werkzeug ist gewöhnlicher, getesteter Code: Es nimmt Eingaben in festgelegten Einheiten entgegen, wendet eine dokumentierte Methode an und gibt das Ergebnis mit dem Namen dieser Methode zurück. Das Modell entscheidet, welches Werkzeug es aufruft, und erklärt die Antwort.

**Was ist der Unterschied zwischen wirklichem und scheinbarem Vergärungsgrad?**
Der scheinbare Vergärungsgrad vergleicht die Stammwürze mit dem scheinbaren Extrakt, den ein Aräometer im fertigen Bier anzeigt und den der Alkohol nach unten zieht, weil er leichter als Wasser ist. Der wirkliche Vergärungsgrad verwendet den tatsächlich verbliebenen Extrakt. Beim selben Bier ist der scheinbare Wert immer höher, hier 78,6% gegenüber 64,9%, deshalb ist eine Zahl ohne ihre Skala mehrdeutig.

**Welche IBU-Formel ist richtig, Tinseth oder Rager?**
Keine ist allgemein richtig. Beide sind empirische Anpassungen an unterschiedliche Daten, und für eine 60-Minuten-Gabe in einer Würze mit 13 Grad Plato liegen sie um etwa ein Drittel auseinander. Wähle eine für deine Brauerei, kalibriere sie gegen im Labor gemessene Bittere und lass das Werkzeug angeben, welches Modell es verwendet hat.
