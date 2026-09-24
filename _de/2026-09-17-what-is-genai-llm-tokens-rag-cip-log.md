---
layout: post
lang: de
title: "Was GenAI und LLMs wirklich sind: Tokens, Kontext, Halluzination und RAG, erklärt an einem CIP-Protokoll"
image: /assets/og/what-is-genai-llm-tokens-rag-cip-log.png
description: "Teil 2 von KI für Operational Excellence in Getränkebetrieben. Wie ein großes Sprachmodell wirklich funktioniert, von Tokens und Kontextfenster bis zur Vorhersage des nächsten Tokens, warum es halluziniert, wann Retrieval (RAG) statt Fine-Tuning sinnvoll ist und was multimodale Modelle hinzufügen, durchgespielt an einem CIP-Protokoll und einer SOP."
date: 2026-09-17 09:00:00 -0700
updated: 2026-09-17
permalink: /de/2026/what-is-genai-llm-tokens-rag-cip-log/
tags: [brewing-science, ai-opex, ai-basics, generative-ai, cip]
faq:
  - q: "Was ist ein großes Sprachmodell, einfach erklärt?"
    a: "Ein großes Sprachmodell ist ein neuronales Netz, das auf einer riesigen Textmenge trainiert wurde, um das nächste Stück Text vorherzusagen, ein Token nach dem anderen. Weil es so viel Sprache gesehen hat, kann es schreiben, zusammenfassen, übersetzen und Fragen beantworten. Es schlägt keine Fakten nach, solange man ihm keinen Weg dazu gibt, und es hat kein eingebautes Gespür dafür, ob das Geschriebene stimmt."
  - q: "Warum halluzinieren LLMs?"
    a: "Weil sie darauf gebaut sind, die plausibelsten nächsten Wörter zu erzeugen, nicht die richtigen. Steht die Antwort nicht im mitgegebenen Text, füllen sie die Lücke mit etwas, das richtig klingt. Wer nach einer CIP-Laugenkonzentration fragt, ohne die eigene SOP mitzugeben, bekommt einen typischen Branchenwert, selbstsicher vorgetragen, der nicht der eigene sein muss."
  - q: "Sollte ein Betrieb RAG oder Fine-Tuning nutzen?"
    a: "Für Fakten, die in Dokumenten stehen, etwa SOPs, Spezifikationen und Wartungshandbücher, ist Retrieval (RAG) das Mittel der Wahl: Das System findet die passende Textstelle und gibt sie dem Modell zusammen mit der Frage, sodass die Antworten die eigenen Dokumente zitieren und sich mit ihnen aktualisieren. Fine-Tuning verändert den Stil des Modells oder bringt ihm ein Aufgabenformat bei. Für Fakten, die sich ändern, ist es ein schlechter Speicherort."
---

**Kurze Antwort: Ein großes Sprachmodell ist ein sehr guter Vorhersager des nächsten Wortes. Es liest Text als Tokens, hält eine begrenzte Menge davon in einem Kontextfenster und schreibt ein Token nach dem anderen, jeweils das plausibelste. Deshalb ist es flüssig, und deshalb halluziniert es: Plausibel ist nicht dasselbe wie wahr. Frag es, ob die CIP von letzter Nacht an Gärtank 7 die Spezifikation erfüllt hat, und ohne deine SOP vergleicht es mit einem typischen Branchenwert und klingt dabei sicher. Gib ihm über Retrieval (RAG) die SOP-Klausel und die Protokollzeilen, und es kann gegen deinen eigenen Standard antworten, mit Quellenangabe. Diese eine Designentscheidung macht im Betrieb den größten Teil des Unterschieds aus.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 340" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Zwei Antworten auf die Frage: Hat die CIP an Gärtank 7 die Spezifikation erfüllt? Im oberen Pfad geht die Frage direkt an das Sprachmodell, das aus allgemeinem Training antwortet, 1,8 Prozent Lauge bei 78 Grad liege im typischen Bereich, also ja. Im unteren Pfad holt ein Retrieval-Schritt zuerst die SOP-Klausel des Betriebs, die 2,0 Prozent Lauge bei 80 Grad für 20 Minuten verlangt, sowie die passenden Protokollzeilen, und das Modell antwortet nein, unter der SOP bei Konzentration, Temperatur und Zeit, mit Verweis auf SOP-Abschnitt 4.2.">
<rect width="1000" height="340" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">"HAT DIE CIP VON LETZTER NACHT AN FV-7 DIE SPEZ ERFÜLLT?" (BEISPIEL)</text>
<g font-family="sans-serif">
<text x="40" y="62" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">NUR DAS MODELL</text>
<rect x="40" y="74" width="200" height="60" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="140" y="100" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">Frage</text>
<text x="140" y="118" text-anchor="middle" font-size="10.5" fill="#4a6b64">+ eingefügte Protokollzeile</text>
<line x1="240" y1="104" x2="320" y2="104" stroke="#4db6a2" stroke-width="2"/>
<rect x="320" y="74" width="200" height="60" rx="9" fill="#06483f"/>
<text x="420" y="100" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">LLM</text>
<text x="420" y="118" text-anchor="middle" font-size="10.5" fill="#cfe6df">nur allgemeines Training</text>
<line x1="520" y1="104" x2="600" y2="104" stroke="#4db6a2" stroke-width="2"/>
<rect x="600" y="74" width="360" height="60" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="780" y="100" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ff4081">"Ja, 1,8% bei 78 C liegt im typischen Bereich."</text>
<text x="780" y="118" text-anchor="middle" font-size="10.5" fill="#4a6b64">plausibel, selbstsicher, nicht dein Standard</text>
<text x="40" y="178" font-size="11" font-weight="700" letter-spacing="1" fill="#4a6b64">MIT RETRIEVAL (RAG)</text>
<rect x="40" y="190" width="200" height="72" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="140" y="216" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">Retriever</text>
<text x="140" y="234" text-anchor="middle" font-size="10.5" fill="#4a6b64">SOP 4.2 + FV-7-Protokollzeilen</text>
<text x="140" y="250" text-anchor="middle" font-size="10.5" fill="#4a6b64">2,0% NaOH, 80 C, 20 min</text>
<line x1="240" y1="226" x2="320" y2="226" stroke="#4db6a2" stroke-width="2"/>
<rect x="320" y="196" width="200" height="60" rx="9" fill="#06483f"/>
<text x="420" y="222" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">LLM</text>
<text x="420" y="240" text-anchor="middle" font-size="10.5" fill="#cfe6df">antwortet aus gegebenem Text</text>
<line x1="520" y1="226" x2="600" y2="226" stroke="#4db6a2" stroke-width="2"/>
<rect x="600" y="196" width="360" height="60" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="780" y="222" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2e9e7c">"Nein. Unter SOP 4.2 bei allen drei Grenzwerten."</text>
<text x="780" y="240" text-anchor="middle" font-size="10.5" fill="#4a6b64">zitiert die Klausel und die Protokollzeilen</text>
<rect x="40" y="284" width="920" height="40" rx="10" fill="#06483f"/>
<text x="500" y="309" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">DASSELBE MODELL &#183; DER UNTERSCHIED IST, WAS DU IHM VORLEGST</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Beispielwerte. Das Modell ohne SOP lügt nicht. Es rät gut, und das ist schlimmer.</figcaption>
</figure>

Hier ist eine Zeile aus einem erfundenen CIP-Protokoll eines Gärtanks, wie sie jede Brauerei, Weinkellerei und Brennerei tausendfach erzeugt:

```
02:14 | FV-07 | CAUSTIC STEP START | NaOH 1.8% | SUPPLY 78.0 C
02:31 | FV-07 | CAUSTIC STEP END | DURATION 17 MIN
```

Füg das in einen Chatbot ein und frag, ob die Reinigung die Spezifikation erfüllt hat. Mit ziemlicher Sicherheit bekommst du ein selbstsicheres "Ja": Lauge im Bereich von 1 bis 2 Prozent bei etwa 75 bis 85 Grad C ist für eine CIP typisch, und 17 Minuten klingen in Ordnung. Nimm nun an, deine SOP verlangt 2,0 Prozent bei 80 Grad für mindestens 20 Minuten. Die Reinigung ist in allen drei Punkten durchgefallen, und der Chatbot hat dir gerade gesagt, sie sei bestanden.

Der [erste Beitrag dieser Serie]({{ '/de/2026/what-is-ai-ladder-rules-to-agi-beverage-plant/' | relative_url }}) hat generative KI auf der Leiter eingeordnet. Dieser hier öffnet sie, denn sobald man sieht, wie ein Sprachmodell arbeitet, ist diese falsche Antwort kein Rätsel mehr.

## Tokens: wie das Modell liest

Ein Sprachmodell liest weder Buchstaben noch ganze Wörter. Es liest **Tokens**, Textstücke, die oft ein Wort, ein Wortteil oder ein Symbol sind. "Caustic" ist vielleicht ein Token. "NaOH" vielleicht zwei oder drei. Als Faustregel für Englisch entsprechen tausend Tokens etwa 750 Wörtern; deutscher Text braucht meist etwas mehr.

Tokens sind aus zwei praktischen Gründen wichtig. Kosten und Grenzen werden in Tokens gezählt, und Zahlen werden auf seltsame Weise in Tokens zerlegt. "78.0" kann zu mehreren Stücken werden. Das ist ein Grund, warum Sprachmodelle beim Rechnen unzuverlässig sind: Sie arbeiten nicht mit der Zahl, sondern mit Fragmenten ihres Textes.

## Das Kontextfenster: was das Modell sehen kann

Das **Kontextfenster** ist alles, was das Modell auf einmal sehen kann: deine Frage, alle eingefügten Dokumente, den bisherigen Gesprächsverlauf und seine eigene Antwort. 2026 akzeptieren führende Modelle Hunderttausende Tokens, manche mehr als eine Million. Das klingt, als reiche es, um jede SOP des Betriebs einzufügen.

So einfach ist es nicht ganz. Modelle verteilen ihre Aufmerksamkeit über einen sehr langen Kontext ungleichmäßig, und Details in der Mitte eines langen Dokuments werden leichter übersehen. Außerdem ist der Kontext flüchtig. Endet das Gespräch, erinnert sich das Modell an nichts. Es hat deine SOP nicht gelernt. Es hat sie einmal gelesen.

## Vorhersage des nächsten Tokens: wie das Modell schreibt

Im Kern tut ein großes Sprachmodell genau eines: Ausgehend von den bisherigen Tokens sagt es voraus, welches Token am wahrscheinlichsten als Nächstes kommt. Dann hängt es dieses Token an und macht es noch einmal. Eine ganze Antwort besteht aus Hunderten solcher Vorhersagen hintereinander.

Gelernt hat es diese Vorhersagen durch Training auf einer enormen Textmenge. Daher kommt sein Allgemeinwissen. Es hat Tausende Dokumente über CIP gelesen, also kennt es den typischen Laugenbereich. Deine SOP hat es nie gelesen, also kann es deinen Standard nicht kennen, solange du ihn nicht zeigst.

## Halluzination: warum die selbstsichere falsche Antwort entsteht

Setzt man diese Teile zusammen, wird Halluzination offensichtlich. Das Modell ist darauf gebaut, die plausibelste Fortsetzung zu erzeugen. Liegt die wahre Antwort vor ihm, decken sich plausibel und wahr meistens. Liegt sie nicht vor, erzeugt das Modell trotzdem etwas Plausibles, denn etwas anderes kann es nicht. Es gibt keinen internen Alarm, der sagt: "Diese Information habe ich nicht."

Deshalb kam bei der CIP-Frage "Ja" heraus. Der plausibelste Text, gemessen an dem, was das Modell im Training gesehen hatte, war, dass 1,8 Prozent bei 78 Grad eine normale Reinigung sind. Es hat deinen Standard nicht geprüft, weil es keinen Standard zum Prüfen hatte.

Halluzination lässt sich verringern, aber nie beseitigen. Der wichtigste Hebel ist kein besseres Modell. Es ist der richtige Text für das Modell.

## RAG: dem Modell den richtigen Text geben

**Retrieval-Augmented Generation**, kurz RAG, ist die Standardlösung. Bevor das Modell antwortet, durchsucht ein Retrieval-Schritt deine eigenen Dokumente (SOPs, Spezifikationen, Wartungshandbücher, frühere Störungsberichte) und legt die relevantesten Passagen zusammen mit der Frage in den Kontext. Das Modell wird angewiesen, aus diesen Passagen zu antworten und sie zu zitieren.

Mit RAG erneut gefragt, holt das System SOP-Abschnitt 4.2 und die FV-7-Protokollzeilen. Das Modell antwortet nun: Der Laugenschritt lag bei Konzentration, Temperatur und Dauer unter dem SOP-Minimum, siehe Abschnitt 4.2. Gleiches Modell, andere Eingaben, andere Antwort.

Zwei Verfeinerungen machen das im Betrieb vertrauenswürdig:

- **Alles belegen.** Jede Antwort nennt das Dokument und den Abschnitt, aus dem sie stammt, damit ein Bediener die SOP öffnen und nachprüfen kann.
- **Den Vergleich dem Code überlassen.** Ein Modell kann "mindestens 2,0 Prozent" aus der SOP lesen. Ob 1,8 unter 2,0 liegt, ist eine Aufgabe für eine Codezeile, nicht für ein Sprachmodell. Die besten Systeme extrahieren Grenzwerte und Messwerte und lassen gewöhnliche Software vergleichen.

Ich habe früher einen Beitrag über [die Suche in Brauerei-SOPs mit GenAI]({{ '/de/2022/gen-ai-search-brewery-sops/' | relative_url }}) geschrieben. Die Idee hat sich nicht geändert. Die Modelle sind nur so gut geworden, dass jetzt die Qualität des Retrievals das schwache Glied ist.

## Fine-Tuning: ein anderes Werkzeug

**Fine-Tuning** heißt, ein bestehendes Modell mit eigenen Beispielen noch etwas weiterzutrainieren. Viele nehmen an, so bringe man einem Modell die eigenen SOPs bei. Dafür ist es meist das falsche Werkzeug.

Fine-Tuning ist gut darin, das Verhalten eines Modells zu ändern: das Format seiner Antworten, den Ton einer Schichtübergabe, wie es eine Art von Linienstillstand klassifiziert. Schlecht ist es darin, Fakten zu speichern, die sich ändern, denn die Fakten stecken dann ohne Quellenangabe und ohne einfache Aktualisierung in den Gewichten des Modells. Wird die SOP überarbeitet, liest ein RAG-System morgen die neue Fassung. Ein feinabgestimmtes Modell zitiert weiter die alte, bis man es neu trainiert.

Eine nützliche Regel: RAG für Wissen, Fine-Tuning für Verhalten, und die meisten Betriebe brauchen das Zweite nie.

## Multimodal: wenn die Eingabe kein Text ist

Viele aktuelle Modelle sind **multimodal**: Sie nehmen neben Text auch Bilder an, manche auch Audio. In der Produktion öffnet das einige nützliche Türen. Ein Bediener fotografiert ein Manometer, eine Störungsmeldung auf einem HMI oder ein handschriftliches Sudprotokoll, und das Modell liest es. Ein Instandhaltungstechniker fotografiert ein Typenschild und bekommt den richtigen Abschnitt im Handbuch.

Es gelten dieselben Regeln. Ein Modell, das das Foto eines Manometers liest, kann sich verlesen, und es meldet seinen Lesefehler mit derselben Sicherheit. Nutze es zum Erfassen und Entwerfen, und bestätige dann die Zahlen.

## Wo es bricht

**Das Retrieval kann die falsche Passage holen.** Sind die SOP für die Drucktanks und die SOP für die Gärtanks fast identisch, zieht der Retriever vielleicht die falsche. Die Quellenangabe ist das, was es einem Menschen erlaubt, das zu bemerken.

**Dokumente sind oft veraltet.** RAG macht das Modell genau so aktuell wie deine Dokumentenbibliothek. Eine nicht überarbeitete SOP erzeugt selbstsicher veraltete Antworten.

**Zahlen bleiben riskant.** Selbst mit dem richtigen Text kann ein Modell eine Tabelle falsch lesen oder einen Wert runden. Wo eine Entscheidung an einer Zahl hängt, sollte die Zahl aus einem führenden System oder einer Berechnung kommen, nicht aus dem Fließtext des Modells.

**Das Modell klingt gleich, wenn es falsch liegt.** Zwischen einer richtigen und einer erfundenen Antwort ändert sich der Ton nicht. Menschen darin zu schulen, die Quellenangabe zu prüfen, ist so wichtig wie der Bau des Systems.

## Das Fazit

Ein Sprachmodell sagt plausiblen Text Token für Token voraus. Es weiß, was typisch ist, und nichts über deinen Betrieb, solange du es ihm nicht zeigst. Das macht es flüssig, nützlich und anfällig für selbstsichere Fehler. RAG schließt den größten Teil der Lücke, indem es deine eigenen SOPs und Protokolle vor das Modell legt und es zwingt, sie zu zitieren. Fine-Tuning ändert Verhalten, nicht Wissen. Und wenn die Antwort eine Zahl ist, auf die es ankommt, lass Code sie prüfen.

Als Nächstes: [Was agentische KI ist]({{ '/de/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}), wenn ein Modell aufhört, Fragen zu beantworten, und anfängt, Werkzeuge zu benutzen. Die Brennerei-Sicht auf diese Grundlagen steht in [Was ist generative KI? Der Unterschied, der für Brenner zählt]({{ '/2026/what-is-generative-ai-distillers/' | relative_url }}). Wie dieselbe Idee den Datenassistenten einer Weinkellerei trägt, zeigt [die Serie Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist ein großes Sprachmodell, einfach erklärt?**
Ein großes Sprachmodell ist ein neuronales Netz, das auf einer riesigen Textmenge trainiert wurde, um das nächste Stück Text vorherzusagen, ein Token nach dem anderen. Weil es so viel Sprache gesehen hat, kann es schreiben, zusammenfassen, übersetzen und Fragen beantworten. Es schlägt keine Fakten nach, solange man ihm keinen Weg dazu gibt, und es hat kein eingebautes Gespür dafür, ob das Geschriebene stimmt.

**Warum halluzinieren LLMs?**
Weil sie darauf gebaut sind, die plausibelsten nächsten Wörter zu erzeugen, nicht die richtigen. Steht die Antwort nicht im mitgegebenen Text, füllen sie die Lücke mit etwas, das richtig klingt. Wer nach einer CIP-Laugenkonzentration fragt, ohne die eigene SOP mitzugeben, bekommt einen typischen Branchenwert, selbstsicher vorgetragen, der nicht der eigene sein muss.

**Sollte ein Betrieb RAG oder Fine-Tuning nutzen?**
Für Fakten, die in Dokumenten stehen, etwa SOPs, Spezifikationen und Wartungshandbücher, ist Retrieval (RAG) das Mittel der Wahl: Das System findet die passende Textstelle und gibt sie dem Modell zusammen mit der Frage, sodass die Antworten die eigenen Dokumente zitieren und sich mit ihnen aktualisieren. Fine-Tuning verändert den Stil des Modells oder bringt ihm ein Aufgabenformat bei. Für Fakten, die sich ändern, ist es ein schlechter Speicherort.
