---
layout: post
lang: de
title: "Den Chatbot nach dem Alkohol fragen, drei Antworten bekommen: GenAI braucht eine semantische Schicht"
image: /assets/og/genai-winery-semantic-layer-potential-alcohol.png
description: "Teil 1 von The Cellar Ledger. Ein Chat-mit-deinen-Daten-Assistent, der in einem Weingut nach dem potenziellen Alkohol gefragt wird, liefert drei verschiedene Zahlen, weil die Umrechnung in drei Tabellen steckt. Warum Text-to-SQL-Agenten undefinierte Kennzahlen verstärken und wie eine gesteuerte semantische Schicht, instrumentbewusste Pipelines und ein kleines Eval-Set das beheben."
date: 2026-06-22 09:00:00 -0700
updated: 2026-06-22
permalink: /de/2026/genai-winery-semantic-layer-potential-alcohol/
tags: [winemaking, cellar-ledger, generative-ai, data-engineering, semantic-layer]
faq:
  - q: "Warum gibt ein Chat-mit-deinen-Daten-Assistent auf dieselbe Frage unterschiedliche Antworten?"
    a: "Meist, weil die Kennzahl nirgends definiert ist, wo der Assistent sie sehen kann. Ein Text-to-SQL-Agent schreibt eine Abfrage gegen die Spalten, die plausibel aussehen. Wird der potenzielle Alkohol in drei Arbeitsmappen mit drei verschiedenen Faktoren berechnet, wählt der Agent einen davon, und ein leicht anders formulierter Prompt wählt einen anderen. Die Lösung: die Kennzahl einmal in einer gesteuerten semantischen Schicht definieren und den Assistenten dorthin zeigen lassen, nicht auf Rohtabellen."
  - q: "Was sollte ein Weingut zuerst in seine semantische Schicht aufnehmen?"
    a: "Die Zahlen, über die gestritten wird: potenzieller Alkohol, Restzucker, Bestandsvolumen, Verlust und Ausbeute pro Tonne. Jede bekommt eine Definition, offen genannte Parameter wie den Zucker-zu-Alkohol-Ausbeutefaktor und einen benannten Verantwortlichen. Das sind auch die Fragen, die einem GenAI-Assistenten am häufigsten gestellt werden, also richtet eine falsche Antwort dort den größten Schaden an."
  - q: "Wie testet man einen GenAI-Datenassistenten, bevor der Winzer ihn nutzt?"
    a: "Etwa zwanzig echte Fragen aus dem Keller aufschreiben, mit Antworten, die jemand von Hand geprüft hat, und sie bei jeder Änderung an Modell, Prompt oder semantischem Modell erneut ausführen. Bewertet wird die exakte Übereinstimmung der Zahlen. Es ist ein kleines Evaluationsset, und es fängt die meisten Regressionen ab, bevor ein Winzer sie bemerkt."
---

**Kurze Antwort: Setzt du einen GenAI-Assistenten ohne gesteuerte Kennzahlenschicht auf die Daten eines Weinguts, beantwortet er die Frage 'Wie hoch ist der potenzielle Alkohol bei den Shiraz-Partien?' mit dem Umrechnungsfaktor, den er zufällig zuerst findet, von drei versteckten. Bei 24 Brix liegen diese Faktoren 1,7 Prozentpunkte Alkohol auseinander, mehr als eine Etikettentoleranz. Das Modell ist nicht das Problem. Die undefinierte Kennzahl ist es. Definiere den potenziellen Alkohol einmal, mit offen gelegten Parametern, baue die Pipeline so, dass jeder Messwert sein Messgerät mitführt, lass den Assistenten auf die semantische Schicht statt auf Rohtabellen zugreifen und teste ihn mit zwanzig Fragen, die der Keller tatsächlich stellt.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Zwei Wege für dieselbe Frage. Auf dem oberen Weg fragt ein GenAI-Assistent drei Tabellen direkt ab und liefert 13,2, 14,2 und 14,9 Prozent potenziellen Alkohol. Auf dem unteren Weg fließen Rohmesswerte in eine Bronze-Tabelle, dann in eine Silver-Tabelle, die Messgerät und Gärphase ergänzt, dann in eine einzige gesteuerte Kennzahl für potenziellen Alkohol in der semantischen Schicht, und der Assistent liefert eine einzige Antwort, 14,2 Prozent, mit genannter Methode.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">GLEICHE FRAGE, ZWEI ARCHITEKTUREN</text>
<g font-family="sans-serif">
<text x="40" y="60" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">OHNE SEMANTISCHE SCHICHT</text>
<rect x="40" y="72" width="170" height="60" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="125" y="98" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">GenAI-Assistent</text>
<text x="125" y="116" text-anchor="middle" font-size="10.5" fill="#4a6b64">Text-to-SQL</text>
<line x1="210" y1="102" x2="290" y2="102" stroke="#4db6a2" stroke-width="2"/>
<rect x="290" y="72" width="380" height="60" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="480" y="98" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">harvest.xlsx &#183; lab.xlsx &#183; labels.xlsx</text>
<text x="480" y="116" text-anchor="middle" font-size="10.5" fill="#4a6b64">&#215;0.55, &#215;0.59, &#215;0.62 in Zellen vergraben</text>
<line x1="670" y1="102" x2="740" y2="102" stroke="#4db6a2" stroke-width="2"/>
<rect x="740" y="72" width="220" height="60" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="850" y="98" text-anchor="middle" font-size="14" font-weight="700" fill="#ff4081">13,2 / 14,2 / 14,9%</text>
<text x="850" y="116" text-anchor="middle" font-size="10.5" fill="#4a6b64">hängt vom Prompt ab</text>
<text x="40" y="170" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">MIT SEMANTISCHER SCHICHT</text>
<rect x="40" y="182" width="170" height="66" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="125" y="208" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">Bronze</text>
<text x="125" y="226" text-anchor="middle" font-size="10.5" fill="#4a6b64">Rohwerte, wie gemessen</text>
<line x1="210" y1="215" x2="240" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="240" y="182" width="190" height="66" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="335" y="208" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">Silver</text>
<text x="335" y="226" text-anchor="middle" font-size="10.5" fill="#4a6b64">+ Messgerät, + Gärphase</text>
<line x1="430" y1="215" x2="460" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="460" y="182" width="220" height="66" rx="9" fill="#06483f"/>
<text x="570" y="208" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">semantische Schicht</text>
<text x="570" y="226" text-anchor="middle" font-size="10.5" fill="#cfe6df">ein potential_alcohol, ein Owner</text>
<line x1="680" y1="215" x2="740" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="740" y="182" width="220" height="66" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="850" y="208" text-anchor="middle" font-size="14" font-weight="700" fill="#2e9e7c">14,2%</text>
<text x="850" y="226" text-anchor="middle" font-size="10.5" fill="#4a6b64">Methode und Parameter genannt</text>
<rect x="40" y="276" width="920" height="44" rx="10" fill="#06483f"/>
<text x="500" y="303" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">NICHT DAS MODELL IST DAS PROBLEM &#183; DIE UNDEFINIERTE KENNZAHL IST ES</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein Assistent, der auf Tabellen zeigt, findet den Faktor, den er zuerst erreicht. Zeigt er auf eine gesteuerte Kennzahl, kann er nur einen finden.</figcaption>
</figure>

Eine Winzerin tippt in den neuen Datenassistenten: 'Wie hoch ist der potenzielle Alkohol bei den Shiraz-Partien?' Die Antwort kommt nach zwei Sekunden, als ordentliche Tabelle. Der Assistent hat recht, in dem Sinne, dass die Zahl irgendwo existiert. Er liegt auch falsch, denn die Arbeitsmappe des Labors hätte etwas anderes gesagt und die Datei mit den Etikettenentwürfen wieder etwas anderes.

Niemand in diesem Gebäude hat einen Fehler gemacht. Jemand hat vor Jahren einen Umrechnungsfaktor in eine Zelle getippt, die Zelle wurde in die Arbeitsmappe des nächsten Jahrgangs kopiert, und jetzt leben drei Versionen derselben Kennzahl in drei Dateien. Ein Mensch weiß, welcher Datei er trauen kann. Ein Text-to-SQL-Agent weiß es nicht. Dies ist der erste Beitrag von **The Cellar Ledger**, einer Serie über die Data-Engineering- und GenAI-Arbeit unter den Zahlen eines Weinguts, und sie beginnt mit der Zahl, die alle nutzen und niemand definiert hat.

## Warum GenAI ein altes Problem lauter macht

Jedes Chat-mit-deinen-Daten-Produkt auf dem Markt funktioniert 2026 ungefähr gleich. Du stellst eine Frage in natürlicher Sprache. Der Assistent liest eine Beschreibung deiner Daten, schreibt eine Abfrage, führt sie aus und fasst das Ergebnis zusammen. Power BI Copilot, Databricks AI/BI Genie und Snowflake Cortex Analyst folgen alle diesem Muster, und alle drei lesen zuerst ein semantisches Modell oder eine Reihe kuratierter Anweisungen, wenn du ihnen eines gibst.

Gibst du ihnen keines, lesen sie die Tabellen. Und eine Tabellenspalte namens `pot_alc` verrät dem Modell nichts darüber, welcher Faktor sie erzeugt hat.

Dann gehen zwei Dinge gleichzeitig schief:

- **Die Antwort ist instabil.** Formuliere die Frage leicht um, und der Agent verknüpft vielleicht eine andere Tabelle, wählt eine andere Spalte und liefert eine andere Zahl, im selben selbstsicheren Ton.
- **Die Antwort wirkt verbindlich.** Eine Tabelle mit einer falschen Zahl sieht aus wie eine Tabelle. Ein Chatbot mit einer falschen Zahl sieht aus wie das System. Tabellen werden geprüft. Den Chatbot prüft meist niemand.

Das alte Problem war: drei Leute arbeiten mit drei Versionen der Wahrheit. Das neue Problem ist, dass der Assistent jedem die Version schickt, die der Prompt zufällig erreicht hat.

## Die Kennzahl darunter: was die Umrechnung wirklich ist

Um den potenziellen Alkohol einmal zu definieren, musst du wissen, was die Faustregeln verbergen. Brix mal 0,55, 0,59 oder 0,62 ist eine Abkürzung für eine Berechnung in vier Schritten, und jeder Schritt ist ein Parameter, für den jemand verantwortlich sein sollte.

**1. Brix zu Dichte.** Grad Brix sind Gramm Saccharose pro 100 Gramm Lösung, Masse pro Masse. Ein Standardpolynom für Saccharoselösungen ergibt bei 24 Brix eine relative Dichte von etwa 1,101.

**2. Gelöste Feststoffe pro Liter.** Brix mal SG mal 10. Für unseren Most etwa 264 g/L.

**3. Abziehen, was kein Zucker ist.** Traubenmost besteht aus Glucose und Fructose plus Säuren, Mineralstoffen und Phenolen. Die zuckerfreien Feststoffe liegen in reifen Trauben typischerweise bei etwa 20 bis 30 g/L. Nimm 25, und du hast etwa 239 g/L vergärbaren Zucker.

**4. Zucker zu Alkohol.** Theoretisch ergibt ein Glucosemolekül zwei Moleküle Ethanol und zwei CO2, also ergeben etwa 15,4 g/L Zucker 1% Alkohol nach Volumen. Echte Hefe baut Zellen auf, bildet Glycerin und verliert etwas Ethanol mit dem Gas, daher liegen die Arbeitswerte höher. Die EU verwendet 16,83 g/L pro 1% vol. 239 geteilt durch 16,83 ergibt 14,2%.

Als Funktion geschrieben ist das Ganze kurz:

```python
def potential_alcohol(brix, non_sugar_gl=25.0, yield_gl_per_pct=16.83):
    sg = 1 + brix / (258.6 - (brix / 258.2) * 227.1)
    sugar_gl = brix * sg * 10 - non_sugar_gl
    return sugar_gl / yield_gl_per_pct
```

Es geht nicht um den Code. Es geht darum, dass `non_sugar_gl` und `yield_gl_per_pct` jetzt benannt, sichtbar und zugeordnet sind. Die Kurzfaktoren verstecken beide, deshalb weichen sie voneinander ab.

Das ist wichtig, weil Toleranzen in einzelnen Prozentpunkten gemessen werden. In den USA darf ein Wein mit bis zu 14% innerhalb von 1,5 Punkten der tatsächlichen Angabe etikettiert werden, oberhalb von 14% innerhalb von 1 Punkt, und das Etikett darf die 14%-Grenze nicht überschreiten, weil sich dort der Verbrauchsteuersatz ändert. Eine Spanne von 1,7 Punkten im Betrieb ist größer als die Toleranz, innerhalb derer sie bleiben muss.

## Die Data-Engineering-Lösung: instrumentbewusste Schichten

Die Kennzahl zu definieren ist die eine Hälfte. Die andere Hälfte besteht darin sicherzustellen, dass die Eingangswerte das bedeuten, was die Kennzahl voraussetzt. Genau hier scheitern viele Weingutsdaten, bevor überhaupt eine KI in die Nähe kommt.

Ein Refraktometer ist im Weinberg in Ordnung. Sobald die Gärung beginnt, erhöht Alkohol den Brechungsindex, sodass ein Refraktometer den verbleibenden Zucker überschätzt, umso stärker, je trockener der Wein wird. Ein Hydrometer misst die Dichte, und Ethanol ist leichter als Wasser, daher zeigt ein trockener Rotwein etwa minus 1 bis minus 2 Brix. Beides sind korrekte Messungen dessen, was das Gerät misst. Beide werden in dem Moment falsch, in dem eine Pipeline sie in einer einzigen Spalte namens `brix` ablegt.

Eine einfache Medallion-Struktur löst das ohne Heldentaten:

- **Bronze** hält jeden Messwert genau so, wie er erfasst wurde: Wert, Einheit, Messgerät, wer, wann, welcher Tank. Nichts wird umgerechnet, nichts wird verworfen.
- **Silver** ergänzt Kontext, den die Pipeline ableiten kann: die Gärphase (vor dem Beimpfen, aktiv, trocken) aus den eigenen Ereignissen des Tanks und eine Markierung für jede Refraktometermessung nach dem Beimpfen. Hydrometerwerte während der Gärung werden in das umbenannt, was sie sind, nämlich Dichte, und dürfen negativ werden.
- **Gold und die semantische Schicht** enthalten die gesteuerten Kennzahlen. `potential_alcohol` liest nur Zuckermesswerte vor dem Beimpfen. Sobald eine fertige Partie einen gemessenen Alkoholwert aus dem Labor hat, übernimmt eine separate Kennzahl `alcohol_measured`, und die Vorhersage wird für diese Partie stillgelegt.

Lege auf die Bronze-Tabelle einen Datenvertrag, der einen Messwert ohne Messgerät ablehnt. Das ist eine einzige Validierungszeile, und es ist die Zeile, die die Mehrdeutigkeit des nächsten Jahrgangs an der Tür aufhält statt erst in einem Vorstandsbericht.

## Den Assistenten auf die richtige Schicht zeigen lassen

Ist die Kennzahl definiert, wird der GenAI-Teil deutlich weniger spannend, und genau das willst du. Drei Einstellungen erledigen den Großteil der Arbeit:

1. **Beschränke den Assistenten auf das semantische Modell.** Gib ihm die Rohtabellen überhaupt nicht. Wenn er `potential_alcohol` nur als Measure sehen kann, kann er keine vierte Version erfinden.
2. **Schreibe die Anweisungen wie ein Kellerhandbuch.** Die meisten dieser Werkzeuge akzeptieren Anweisungen im Klartext. Nutze sie für die Fachfakten, die das Modell nicht erraten kann: 'Brix nach dem Beimpfen ist Dichte, nicht Zucker', 'Alkohol bei einer fertigen Partie kommt aus `alcohol_measured`', 'Volumen sind in Litern bei 20 Grad C'.
3. **Lass ihn die Methode nennen.** Verlange unter jeder Antwort den Namen der Kennzahl und ihre Parameter. Eine Winzerin, die 'potenzieller Alkohol, EU-Ausbeute 16,83 g/L, zuckerfreier Extrakt 25 g/L' sieht, kann über die Annahme streiten statt über die Zahl.

## Ein Eval-Set mit zwanzig Fragen

Der letzte Schritt ist der, den Teams überspringen. Bevor sich jemand auf den Assistenten verlässt, schreib etwa zwanzig Fragen auf, die der Keller tatsächlich stellt, mit Antworten, die jemand von Hand geprüft hat. 'Potenzieller Alkohol bei Partie 24-SH-03.' 'Welche Tanks liegen noch über 5 Brix?' 'Gemessener Alkohol beim Viognier vom letzten Jahr.' Führe das Set bei jeder Änderung an Modell, Prompt oder semantischem Modell aus und bewerte exakte numerische Übereinstimmungen.

Es ist eine kleine Datei. Es ist auch die einzige ehrliche Antwort auf 'Können wir dem Chatbot vertrauen?' Du vertraust ihm nicht. Du testest ihn, so wie das Labor ein neues Messgerät gegen eine Referenz prüft, bevor es in Betrieb geht.

Und es gibt einen Bonus. Jede fertige Partie liefert dir ein Paar: Ausgangszucker und gemessener Alkohol. Ein paar Jahrgänge solcher Paare, nach Rebsorte, erlauben es dir, deinen eigenen Ausbeutefaktor an deine Trauben, deine Hefe und deinen Keller anzupassen. Das ist das erste wirklich nützliche Modell im Betrieb, und es existiert nur, weil die Pipeline beide Zahlen aufbewahrt hat.

## Wo das an Grenzen stößt

**Der zuckerfreie Anteil bleibt eine Schätzung.** Er verschiebt sich mit Rebsorte, Reife, Fäulnis und Pressfraktion. Ein offen genannter Standardwert ist besser als ein versteckter, aber miss ihn jedes Jahr an einigen Mosten und behandle ihn als vorläufig.

**Eine semantische Schicht behebt keine schlechte Probenahme.** Saft vom sonnigen Ende einer einzigen Zeile beschreibt keine Parzelle. Keine Kennzahldefinition korrigiert den Eimer.

**Anweisungen driften.** Die Klartextanweisungen, die du dem Assistenten gibst, sind Konfiguration. Versioniere sie, prüfe Änderungen und führe das Eval-Set erneut aus, wenn sie sich ändern, sonst werden sie still zur vierten Tabelle.

**Regeln unterscheiden sich je nach Markt.** Die oben genannten US-Toleranzwerte sind die, die ich am besten kenne. Prüfe den Markt, in den du verkaufst, bevor du eine Etikettenprüfung darauf aufbaust.

## Das Fazit

Der Chatbot gab drei Antworten, weil das Weingut drei Antworten hatte. GenAI hat dieses Problem nicht geschaffen. Es hat nur aufgehört, es zu verstecken. Definiere die Kennzahl einmal mit offen gelegten Parametern, bewahre jeden Messwert zusammen mit seinem Messgerät auf, lass den Assistenten nur die gesteuerte Schicht sehen und miss ihn an einem kleinen Satz geprüfter Fragen. Dann ist die Antwort nach zwei Sekunden etwas wert.

Für das größere Argument, warum Dashboards in Weingütern das Vertrauen des Kellers verlieren, siehe [Why Power BI Dashboards Die in Wineries]({{ '/2026/why-power-bi-dashboards-fail-wineries/' | relative_url }}). Was ein Modell mit einer sauberen Gärkurve anfangen kann, steht in [KI für die Steuerung der Weingärung]({{ '/de/2024/ai-wine-fermentation-control/' | relative_url }}). Als Nächstes in dieser Serie: [Event Sourcing im Keller]({{ '/de/2026/event-sourced-cellar-records-winery/' | relative_url }}), das Datenmodell, mit dem Volumen aufgehen. Die vollständige Liste steht auf der [Seite zur Cellar-Ledger-Serie]({{ '/series/cellar-ledger/' | relative_url }}).

## Häufig gestellte Fragen

**Warum gibt ein Chat-mit-deinen-Daten-Assistent auf dieselbe Frage unterschiedliche Antworten?**
Meist, weil die Kennzahl nirgends definiert ist, wo der Assistent sie sehen kann. Ein Text-to-SQL-Agent schreibt eine Abfrage gegen die Spalten, die plausibel aussehen. Wird der potenzielle Alkohol in drei Arbeitsmappen mit drei verschiedenen Faktoren berechnet, wählt der Agent einen davon, und ein leicht anders formulierter Prompt wählt einen anderen. Die Lösung: die Kennzahl einmal in einer gesteuerten semantischen Schicht definieren und den Assistenten dorthin zeigen lassen, nicht auf Rohtabellen.

**Was sollte ein Weingut zuerst in seine semantische Schicht aufnehmen?**
Die Zahlen, über die gestritten wird: potenzieller Alkohol, Restzucker, Bestandsvolumen, Verlust und Ausbeute pro Tonne. Jede bekommt eine Definition, offen genannte Parameter wie den Zucker-zu-Alkohol-Ausbeutefaktor und einen benannten Verantwortlichen. Das sind auch die Fragen, die einem GenAI-Assistenten am häufigsten gestellt werden, also richtet eine falsche Antwort dort den größten Schaden an.

**Wie testet man einen GenAI-Datenassistenten, bevor der Winzer ihn nutzt?**
Etwa zwanzig echte Fragen aus dem Keller aufschreiben, mit Antworten, die jemand von Hand geprüft hat, und sie bei jeder Änderung an Modell, Prompt oder semantischem Modell erneut ausführen. Bewertet wird die exakte Übereinstimmung der Zahlen. Es ist ein kleines Evaluationsset, und es fängt die meisten Regressionen ab, bevor ein Winzer sie bemerkt.
