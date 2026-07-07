---
layout: post
lang: de
title: "Mit Vorhersagemodellen auf CO2-Engpässe vorbereiten"
image: /assets/og/planning-co2-shortages-predictive.png
description: "Den CO2-Bedarf gegen Gärungsrückgewinnung und Beschaffung prognostizieren, um Puffer und Rückgewinnungsinvestitionen zu dimensionieren — eine Lektion, die der Versorgungsengpass 2022 verschärft hat."
date: 2022-01-14
updated: 2022-01-14
permalink: /de/2022/planning-co2-shortages-predictive/
tags: [brewing-science, planning, sustainability]
faq:
  - q: "Wie können Vorhersagemodelle bei der CO2-Versorgung helfen?"
    a: "Indem sie prognostizieren, wie viel CO2 du zum Spülen, Karbonisieren und Verpacken brauchst, und das gegen das CO2 stellen, das deine Gärungen zurückgewinnen und das du zukaufen kannst, helfen Modelle dir, den Pufferspeicher zu dimensionieren und zu entscheiden, ob sich eine Investition in die Rückgewinnung lohnt."
  - q: "Kann ein Modell einen CO2-Engpass vorhersagen?"
    a: "Es kann deinen eigenen Bedarf und deine Rückgewinnung recht gut vorhersagen, weil diese deinem Produktionsplan folgen, aber externe Versorgungsschocks wie der Engpass 2022 werden von Märkten und Ausfällen getrieben, die wirklich schwer zu prognostizieren sind. Das realistische Ziel ist Resilienz, nicht perfekte Vorhersage."
  - q: "Lohnt sich die Rückgewinnung von Gärungs-CO2?"
    a: "Das hängt von deinen Mengen, deinem Bedarfsmuster und den Investitionskosten der Rückgewinnungsanlage ab. Eine Prognose von Bedarf gegen Rückgewinnungspotenzial ist genau der Input, der diesen Business Case klar macht, statt eine Schätzung."
---

**Kurze Antwort: Du kannst deinen eigenen CO2-Bedarf und die Gärungsrückgewinnung genau genug prognostizieren, um Puffer zu dimensionieren und Rückgewinnungstechnik zu rechtfertigen — aber externe Versorgungsschocks bleiben schwer vorhersehbar.** Der Engpass 2022 hat diese Lücke unübersehbar gemacht.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsablauf sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Mit Vorhersagemodellen auf CO2-Engpässe vorbereiten</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Gären</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Verpacken</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Wo dies im Bierproduktionsablauf sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Warum CO2 ein Planungsproblem ist
CO2 steht auf beiden Seiten der Bilanz einer Brauerei. Die Gärung erzeugt es — und dieses CO2 lässt sich zurückgewinnen und wiederverwenden. Zugleich kaufen Brauereien CO2 zum Spülen von Tanks, zum Karbonisieren von Bier und zum Verpacken. Du bist also gleichzeitig Produzent und Verbraucher desselben Gases, und die beiden Flüsse decken sich selten sauber miteinander oder mit dem, was Lieferanten liefern können.

Das ist im Kern ein Prognose- und Bilanzierungsproblem, und es bildet sich sauber auf Daten ab, die du bereits hast. Dein Produktionsplan treibt den Bedarf: wie viele Tanks du spülst, wie viel Bier du karbonisierst, wie viel du verpackst. Deine Gärungsmengen treiben das Rückgewinnungspotenzial. Bring beides zusammen, und du hast das Material für eine CO2-Bilanz, die du in die Zukunft projizieren kannst.

## Was modellieren, und wie
Beginne mit dem Messen, denn du kannst nicht gegen Zahlen planen, die du nie erfasst hast — dieselbe Disziplin gilt für jedes KI-Vorhaben, wie in [Sammle deine Daten vor der KI]({{ '/de/2026/collect-your-data-before-ai/' | relative_url }}) behandelt. Erfasse zugekauftes CO2, CO2-Verbrauch je Prozessschritt und das CO2, das deine Gärungen erzeugen.

Mit dieser Historie ist eine Bedarfsprognose ein recht gewöhnliches Zeitreihen- und Planungsproblem: künftige Sude und Verpackungsläufe übersetzen sich in künftigen CO2-Bezug. Lege das Rückgewinnungspotenzial obendrauf — getrieben von Gärungsmenge und -timing — und du erhältst eine projizierte Nettoposition für die kommenden Wochen. Von da an werden die Planungsfragen konkret. Wie groß muss ein Puffer an gespeichertem CO2 sein, um eine Lieferlücke zu überbrücken? Bei welchem Produktionsmaßstab amortisiert die Vor-Ort-Rückgewinnung ihre Investitionskosten? Das sind Entscheidungen, die eine Prognose von Bauchgefühl in eine dimensionierte, belastbare Zahl verwandelt.

## Wo es bricht: Schocks und Capex
Hier ist die ehrliche Grenze. Deine internen Flüsse sind vorhersehbar, weil sie deinem eigenen Plan folgen, aber die externe Versorgungsseite ist es nicht. Der Engpass 2022 wurde von vorgelagerten Anlagenausfällen und Marktdynamiken getrieben, die weit außerhalb der Daten jeder Brauerei liegen. Kein auf deiner Produktionshistorie trainiertes Modell wird das kommen sehen, und das Gegenteil vorzugaukeln ist gefährlich.

Also verschiebt sich das Ziel von Vorhersage zu Resilienz. Nutze die Prognose, um deinen Bedarf präzise zu kennen und Puffer und Rückgewinnung so zu dimensionieren, dass eine Versorgungslücke überstehbar ist, nicht katastrophal. Die andere Grenze ist Kapital: Rückgewinnungstechnik ist eine echte Investition, und die Prognose sagt dir, ob deine Mengen sie rechtfertigen — für einen kleinen Produzenten kann die Antwort ehrlicherweise Nein lauten, und ein größerer Puffer plus Lieferantendiversifizierung ist die bessere Wette.

Ein generativer KI-Assistent stiftet hier Nutzen, indem er die Prognose in einen Plan verwandelt: „Bei einer zweiwöchigen Versorgungsunterbrechung nächsten Monat siehst du hier deinen projizierten Fehlbetrag, den Puffer, den du abbauen würdest, und die Karbonisierungsläufe, die zuerst umzuplanen sind." Er übersetzt eine numerische Projektion in ein Notfall-Drehbuch, dem Menschen unter Druck tatsächlich folgen können.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 320" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein fortlaufender Zyklus — jeder Schritt speist den nächsten, dann von vorn."><rect x="0" y="0" width="720" height="320" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">DER ZYKLUS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Mit Vorhersagemodellen auf CO2-Engpässe vorbereiten</text><circle cx="360" cy="190" r="95" fill="none" stroke="#d8e6e1" stroke-width="1.5" stroke-dasharray="5 5"/><circle cx="360" cy="95" r="34" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360" y="100" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">Plan</text><circle cx="455" cy="190" r="34" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="455" y="195" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">Umsetzen</text><circle cx="360" cy="285" r="34" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360" y="290" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">Prüfen</text><circle cx="265" cy="190" r="34" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="265" y="195" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#06483f">Handeln</text><circle cx="428" cy="140" r="4" fill="#00695c"/><circle cx="410" cy="258" r="4" fill="#00695c"/><circle cx="292" cy="240" r="4" fill="#00695c"/><circle cx="310" cy="122" r="4" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein fortlaufender Zyklus — jeder Schritt speist den nächsten, dann von vorn.</figcaption>
</figure>

## Das Fazit
Vorhersagemodelle helfen beim CO2 wirklich, weil Bedarf und Rückgewinnung deinem Produktionsplan folgen, also Daten, die du erfassen und projizieren kannst. Das erlaubt dir, Puffer zu dimensionieren und einen klaren Fall für Rückgewinnungsinvestitionen zu bauen. Was sie nicht können, ist externe Versorgungsschocks vorauszusehen — also plane für Resilienz, miss zuerst deine Flüsse und lass einen Gen-KI-Assistenten die Prognose in einen Notfallplan verwandeln.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [Was KI für eine Brauerei tun kann]({{ '/de/2026/what-can-ai-do-for-a-brewery/' | relative_url }}).

## Häufig gestellte Fragen

**Wie können Vorhersagemodelle bei der CO2-Versorgung helfen?**
Indem sie prognostizieren, wie viel CO2 du zum Spülen, Karbonisieren und Verpacken brauchst, und das gegen das CO2 stellen, das deine Gärungen zurückgewinnen und das du zukaufen kannst, helfen Modelle dir, den Pufferspeicher zu dimensionieren und zu entscheiden, ob sich eine Investition in die Rückgewinnung lohnt.

**Kann ein Modell einen CO2-Engpass vorhersagen?**
Es kann deinen eigenen Bedarf und deine Rückgewinnung recht gut vorhersagen, weil diese deinem Produktionsplan folgen, aber externe Versorgungsschocks wie der Engpass 2022 werden von Märkten und Ausfällen getrieben, die wirklich schwer zu prognostizieren sind. Das realistische Ziel ist Resilienz, nicht perfekte Vorhersage.

**Lohnt sich die Rückgewinnung von Gärungs-CO2?**
Das hängt von deinen Mengen, deinem Bedarfsmuster und den Investitionskosten der Rückgewinnungsanlage ab. Eine Prognose von Bedarf gegen Rückgewinnungspotenzial ist genau der Input, der diesen Business Case klar macht, statt eine Schätzung.
