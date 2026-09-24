---
layout: post
lang: de
title: "Ein GenAI-Blending-Assistent, bei dem die Mathematik im Code steckt: LP für den Verschnitt, Dichtetabellen für das Wasser"
image: /assets/og/genai-whisky-blending-assistant-lp.png
description: "Teil 5 von The Still and the Model. Ein Sprachmodell kann einen Blender durch einen Verschnitt begleiten, aber es sollte nie selbst rechnen. Die Fassauswahl ist ein lineares Programm, die Herabsetzung auf Trinkstärke braucht die Mathematik der Ethanol-Wasser-Kontraktion, und die Altersangabe ist eine Regel, kein Durchschnitt. Das LLM ruft die Tools auf und erklärt die Antwort."
date: 2026-08-11 09:00:00 -0700
updated: 2026-08-11
permalink: /de/2026/genai-whisky-blending-assistant-lp/
tags: [distilling-maturation, still-and-model, generative-ai, optimisation, blending]
faq:
  - q: "Warum kann man nicht einfach Volumina abziehen, um zu berechnen, wie viel Wasser in den Whisky muss?"
    a: "Weil sich Ethanol und Wasser beim Mischen zusammenziehen. Um 1.000 Liter bei 63,5% auf 40% herabzusetzen, braucht man etwa 605 Liter Wasser, nicht die 587,5 Liter, die eine einfache Volumenrechnung nahelegt. Gibt man nur 587,5 Liter zu, liegt das Destillat bei etwa 40,4%. Die richtige Methode rechnet in Masse mit Dichtetabellen bei 20 Grad C und bestätigt das Ergebnis anschließend mit einer Messung."
  - q: "Kann ein LLM Fässer für einen Whisky-Verschnitt auswählen?"
    a: "Es sollte sie nicht direkt auswählen. Die Fassauswahl ist ein Optimierungsproblem mit harten Nebenbedingungen wie Volumen, sensorischen Zielen und dem Alter des jüngsten Whiskys, und ein Solver für lineare Programmierung löst es exakt. Die Aufgabe des LLM ist, die Anfrage des Blenders in Solver-Eingaben zu übersetzen, den Solver aufzurufen und das Ergebnis zu erklären."
  - q: "Wie funktioniert eine Altersangabe bei einem Whisky-Verschnitt?"
    a: "Bei Scotch Whisky und nach EU-Recht ist das Alter auf dem Etikett das Alter des jüngsten Whiskys in der Flasche. Es ist kein Durchschnitt. Ein Blending-Tool muss jedes Fass ausschließen, das jünger ist als die Angabe, egal wie attraktiv Kosten oder Aroma sind, und der Optimierer sollte das als harte Regel durchsetzen."
---

**Kurze Antwort: GenAI ist eine gute Schnittstelle für einen Blender und ein schlechter Taschenrechner. Die Fassauswahl ist ein lineares Programm: ein Volumen und sensorische Ziele mit dem geringsten Wert an eingesetztem Bestand erreichen, mit der Altersangabe als harter Regel, weil das Etikett den jüngsten Whisky angibt, nicht den Durchschnitt. Die Herabsetzung auf Trinkstärke braucht die Mathematik der Ethanol-Wasser-Kontraktion: 1.000 Liter bei 63,5% brauchen etwa 605 Liter Wasser, um 40% zu erreichen, nicht 587,5. Pack beide Berechnungen in getesteten Code, stelle sie als Tools bereit und lass das Sprachmodell tun, was es gut kann: die Anfrage verstehen, die Tools aufrufen und die Antwort in klaren Worten erklären.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Die Architektur des Blending-Assistenten. Ein Blender fragt nach einem 12 Jahre alten Verschnitt von 300 Litern reinen Alkohols mit einem Sherry-Charakter-Wert von mindestens 6. Das LLM ruft zwei Tools auf. Der Solver für die Fassauswahl liefert 94 Liter reinen Alkohols aus Fass A, 130 aus Fass B und 76 aus Fass C und schließt Fass D aus, weil es 10 Jahre alt ist. Das Herabsetzungs-Tool ergibt, dass 1,000 Liter bei 63.5 Prozent 604.9 Liter Wasser brauchen, um 40 Prozent zu erreichen, und dass die naiven 587.5 Liter bei 40.4 Prozent enden würden. Danach erklärt das LLM das Ergebnis.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DAS LLM FRAGT, DIE TOOLS RECHNEN (BEISPIEL)</text>
<g font-family="sans-serif">
<rect x="30" y="60" width="250" height="100" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="155" y="86" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Blender fragt</text>
<text x="155" y="108" text-anchor="middle" font-size="10.5" fill="#4a6b64">12 Jahre alter Verschnitt,</text>
<text x="155" y="125" text-anchor="middle" font-size="10.5" fill="#4a6b64">300 LAA, Sherry-Wert &#8805; 6,</text>
<text x="155" y="142" text-anchor="middle" font-size="10.5" fill="#4a6b64">geringster Bestandswert</text>
<line x1="280" y1="110" x2="340" y2="110" stroke="#4db6a2" stroke-width="2"/>
<rect x="340" y="75" width="160" height="70" rx="12" fill="#06483f"/>
<text x="420" y="106" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">LLM</text>
<text x="420" y="126" text-anchor="middle" font-size="10.5" fill="#cfe6df">ruft Tools, erklärt</text>
<line x1="500" y1="100" x2="560" y2="80" stroke="#4db6a2" stroke-width="2"/>
<line x1="500" y1="125" x2="560" y2="200" stroke="#4db6a2" stroke-width="2"/>
<rect x="560" y="50" width="410" height="100" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="765" y="74" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">select_casks() &#183; lineares Programm</text>
<text x="765" y="96" text-anchor="middle" font-size="11" fill="#06483f">A 94 LAA &#183; B 130 LAA &#183; C 76 LAA</text>
<text x="765" y="116" text-anchor="middle" font-size="11" fill="#06483f">Sherry-Wert 6,0, Bestandswert 415</text>
<text x="765" y="136" text-anchor="middle" font-size="11" fill="#ff4081">D ausgeschlossen: 10 Jahre alt</text>
<rect x="560" y="165" width="410" height="100" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="765" y="189" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">reduction_water() &#183; Dichtetabellen</text>
<text x="765" y="211" text-anchor="middle" font-size="11" fill="#06483f">1.000 L bei 63,5% auf 40%: 604,9 L Wasser</text>
<text x="765" y="231" text-anchor="middle" font-size="11" fill="#06483f">Ergebnis 1.587,5 L, 635 LAA</text>
<text x="765" y="251" text-anchor="middle" font-size="11" fill="#ff4081">naive 587,5 L ergeben 40,4%</text>
<rect x="30" y="286" width="940" height="40" rx="10" fill="#06483f"/>
<text x="500" y="311" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">JEDE ZAHL KOMMT AUS EINEM TOOL &#183; DAS MODELL RECHNET NIE SELBST</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Beispielhafter Bestand und Werte. Beide Tools sind gewöhnlicher, getesteter Code. Das Sprachmodell ist die Schnittstelle.</figcaption>
</figure>

Ein Blender fragt einen GenAI-Assistenten, wie viel Wasser nötig ist, um 1.000 Liter Destillat in Fassstärke von 63,5% auf 40% herabzusetzen. Der Assistent antwortet sofort: 587,5 Liter. Er zeigt seinen Rechenweg, und der Rechenweg ist sauber. Er ist auch falsch, und der Fehler ist kein Rundungsproblem. Es ist Chemie, von der dem Modell niemand erzählt hat.

Dieser Beitrag handelt davon, einen Blending-Assistenten zu bauen, der diesen Fehler nicht machen kann, weil er überhaupt nie rechnet. Der [Fassbestand]({{ '/de/2026/cask-inventory-data-engineering-scd2/' | relative_url }}) aus dem vorherigen Beitrag liefert den Bestand. Die Mathematik steckt in Tools. Das Modell redet.

## Das Wasserproblem: warum sich Volumina nicht addieren

Nimm 1.000 Liter bei 63,5% ABV. Darin stecken 635 Liter reiner Alkohol. Bei 40% ergeben diese 635 Liter Alkohol 635 / 0,40 = 1.587,5 Liter Destillat. Die naheliegende Antwort ist also, 587,5 Liter Wasser zuzugeben.

Das Problem: Ethanol und Wasser ziehen sich beim Mischen zusammen. Die Moleküle packen sich enger als in jeder der beiden Flüssigkeiten allein, sodass 1.000 Liter Destillat plus 587,5 Liter Wasser weniger als 1.587,5 Liter ergeben. Die Alkoholstärke landet über dem Ziel, in diesem Fall bei etwa 40,4%.

Die richtige Methode rechnet in Masse, die erhalten bleibt, und nutzt die Dichte von Ethanol-Wasser-Gemischen bei 20 Grad C:

```python
def reduction_water(vol_l, abv_in, abv_out, rho20):
    # rho20(abv) -> density in kg/L at 20 C, from the official alcoholometric tables
    laa = vol_l * abv_in / 100
    vol_out = laa / (abv_out / 100)
    mass_in = vol_l * rho20(abv_in)
    mass_out = vol_out * rho20(abv_out)
    return (mass_out - mass_in) / rho20(0)   # litres of water at 20 C
```

Mit Dichten von etwa 0,901 kg/L bei 63,5% und 0,948 kg/L bei 40% lautet die Antwort rund 605 Liter Wasser, nicht 587,5. Die fehlenden 17 Liter sind die Kontraktion.

Spielen 0,4% eine Rolle? Die Toleranz für die Alkoholangabe auf dem Etikett liegt nach EU-Recht bei 0,3% vol, und die Steuer wird auf Alkohol gezahlt. Zu hohe Stärke verschenkt Destillat. In die andere Richtung zu überschießen ist schlimmer: Im Vereinigten Königreich und in der EU darf Whisky unter 40% überhaupt nicht als Whisky verkauft werden. Deshalb erfolgen echte Herabsetzungen in Stufen, mit demineralisiertem Wasser, und am Ende wird die Stärke mit einem Dichtemessgerät gemessen, statt irgendeiner Rechnung zu vertrauen, so gut sie auch sein mag.

## Die Fassauswahl ist ein lineares Programm

Fässer für einen Verschnitt auszuwählen ist ein Optimierungsproblem in Zivil. Eine einfache Fassung:

- **Entscheidung:** wie viele Liter reinen Alkohols aus jedem zulässigen Fass entnommen werden.
- **Zielfunktion:** den geringsten Gesamtwert an Bestand einsetzen, damit die wertvollsten älteren Fässer für die Stellen bleiben, an denen sie zählen.
- **Nebenbedingungen:** das Alkoholziel insgesamt; der verfügbare Alkohol jedes Fasses; sensorische Ziele als gewichtete Mittelwerte (zum Beispiel ein Sherry-Charakter-Wert von mindestens 6 über den gesamten Verschnitt); und die Altersregel.

Ein Solver für lineare Programmierung (SciPy, OR-Tools oder der in deinem Planungstool) löst das exakt in Millisekunden. Im Beispiel, mit einem 12 Jahre alten Fass A (Wert 1,0 pro LAA, Sherry 3), einem 14 Jahre alten B (1,3, Sherry 7) und einem 18 Jahre alten C (2,0, Sherry 8), nimmt der günstigste Verschnitt von 300 LAA mit einem Sherry-Wert von 6 94 LAA aus A, alle 130 aus B und 76 aus C, bei einem Bestandswert von 415.

## Die Altersangabe ist eine Regel, kein Durchschnitt

Nimm jetzt Fass D dazu: 10 Jahre alt, wunderbarer Sherry-Charakter (Wert 9), günstig mit 0,8 pro LAA. Lässt man den Solver es verwenden, fallen die Kosten auf 302,5, ein Viertel weniger. Er nimmt D komplett und deutlich weniger vom älteren Bestand.

Für ein Etikett mit 12 Jahren ist das auch unzulässig. Nach den Scotch Whisky Regulations und EU-Recht ist die Altersangabe das Alter des jüngsten Whiskys in der Flasche. Sie ist kein Durchschnitt der Alter, wie auch immer gewichtet. Ein Tool, das ein Durchschnittsalter berechnet und gegen 12 prüft, genehmigt diesen Verschnitt anstandslos.

Genau diese Art von Fachregel macht ein Sprachmodell im Gespräch falsch, und ein Solver macht sie nur richtig, wenn jemand sie kodiert. Deshalb ist die Altersregel keine Nebenbedingung in der Mathematik. Sie ist ein Filter darauf, welche Fässer überhaupt ins Problem dürfen, angewendet im Code, bevor der Solver je läuft.

## Wo das LLM hingehört

Liegen die Berechnungen in Tools, hat das Sprachmodell eine nützliche und sichere Aufgabe:

1. **Die Anfrage in Eingaben übersetzen.** "So ähnlich wie der 12er vom letzten Jahr, etwas mehr Sherry, 300 LAA, die 25-Jährigen nicht anrühren" wird zu einem Ziel, Nebenbedingungen und einer Ausschlussliste. Der Assistent zeigt die Eingaben zur Bestätigung, bevor er irgendetwas ausführt.
2. **Die Tools aufrufen.** `select_casks` für den Verschnitt, `reduction_water` für die Herabsetzung, `cask_history` aus dem Bestand für alles, was der Blender zu einem bestimmten Fass fragt.
3. **Das Ergebnis erklären.** Warum Fass B komplett verwendet wurde (es ist der günstigste Weg, den Sherry-Wert anzuheben), warum D ausgeschlossen wurde (Alter) und was sich ändern würde, wenn das Sherry-Ziel auf 5 sinkt.
4. **Nie selbst eine Zahl erzeugen.** Jede Zahl in der Erklärung stammt aus einer Tool-Ausgabe. Stellt der Blender eine quantitative Frage, die die Tools nicht beantworten können, sagt der Assistent das.

Der Blender bleibt der Entscheider, und die Nase bleibt der letzte Test. Der [Beitrag zur Blending-Konsistenz]({{ '/de/2024/ai-whiskey-blending-consistency/' | relative_url }}) behandelt das Treffen eines Hausstils anhand sensorischer und chemischer Daten. In diesem Beitrag geht es darum, dass die Arithmetik drumherum nie das schwache Glied ist.

## Wo das bricht

**Sensorische Werte sind nicht linear.** Der Solver behandelt den Sherry-Wert eines Verschnitts als gewichteten Mittelwert seiner Fässer. Aroma mischt sich nicht immer so höflich: Ein dominantes Fass kann weit über seinen Anteil hinaus prägen. Behandle das Optimum als Ausgangsrezept für einen Probeverschnitt, nicht als finalen Blend.

**Dichtetabellen müssen die amtlichen sein.** Die Skizze oben ist nur so gut wie `rho20`. Für Steuer und Etikettierung nutze die amtlichen alkoholometrischen Tabellen (OIML R22 oder das Pendant deiner Behörde) und ein kalibriertes Messgerät, keine Näherung, die jemand eingetippt hat.

**Auch das Verschneiden unterschiedlicher Stärken zieht sich etwas zusammen.** Mischt man zwei Destillate unterschiedlicher Stärke, schrumpft das Volumen ebenfalls leicht, sodass das Volumen des Verschnitts nicht exakt die Summe der Fässer ist. Bei Fässern ähnlicher Stärke ist der Effekt klein, aber rechne in Alkohol und miss das Ergebnis.

**Bestandswerte sind eine Grundsatzentscheidung.** Den Bestandswert zu minimieren, kodiert eine Sicht darauf, welche Fässer am meisten zählen. Hol dir diese Sicht von den Menschen, die für den reifenden Bestand verantwortlich sind, und lass sie sie ändern.

## Das Fazit

Ein Sprachmodell beantwortet eine Blending-Frage in flüssigen, selbstsicheren Sätzen, auch in solchen, die Chemie oder Gesetz verletzen. Halte es von den Rechnungen fern. Pack die Fassauswahl in einen Solver, mit der Altersangabe als hartem Filter. Pack die Herabsetzung in Code, der Dichtetabellen nutzt und die Masse erhält. Dann lass das Modell den Teil machen, den es wirklich gut kann: verstehen, was der Blender meinte, die richtigen Tools aufrufen und die Antwort erklären. Das Modell sieht die Zahlen. Der Blender verkostet den Verschnitt.

Als Nächstes und zum Abschluss der Serie: [wo KI in der Brennerei bricht]({{ '/de/2026/where-distillery-ai-breaks/' | relative_url }}). Zur sensorischen Seite des Blendings in einem Dashboard siehe [das Dashboard für Whisky-Blending und Sensorik]({{ '/de/2023/tableau-whisky-blending-sensory-dashboard/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite The Still and the Model]({{ '/series/still-and-model/' | relative_url }}).

## Häufig gestellte Fragen

**Warum kann man nicht einfach Volumina abziehen, um zu berechnen, wie viel Wasser in den Whisky muss?**
Weil sich Ethanol und Wasser beim Mischen zusammenziehen. Um 1.000 Liter bei 63,5% auf 40% herabzusetzen, braucht man etwa 605 Liter Wasser, nicht die 587,5 Liter, die eine einfache Volumenrechnung nahelegt. Gibt man nur 587,5 Liter zu, liegt das Destillat bei etwa 40,4%. Die richtige Methode rechnet in Masse mit Dichtetabellen bei 20 Grad C und bestätigt das Ergebnis anschließend mit einer Messung.

**Kann ein LLM Fässer für einen Whisky-Verschnitt auswählen?**
Es sollte sie nicht direkt auswählen. Die Fassauswahl ist ein Optimierungsproblem mit harten Nebenbedingungen wie Volumen, sensorischen Zielen und dem Alter des jüngsten Whiskys, und ein Solver für lineare Programmierung löst es exakt. Die Aufgabe des LLM ist, die Anfrage des Blenders in Solver-Eingaben zu übersetzen, den Solver aufzurufen und das Ergebnis zu erklären.

**Wie funktioniert eine Altersangabe bei einem Whisky-Verschnitt?**
Bei Scotch Whisky und nach EU-Recht ist das Alter auf dem Etikett das Alter des jüngsten Whiskys in der Flasche. Es ist kein Durchschnitt. Ein Blending-Tool muss jedes Fass ausschließen, das jünger ist als die Angabe, egal wie attraktiv Kosten oder Aroma sind, und der Optimierer sollte das als harte Regel durchsetzen.
