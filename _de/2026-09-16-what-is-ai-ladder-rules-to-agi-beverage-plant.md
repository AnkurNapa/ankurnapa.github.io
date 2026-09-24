---
layout: post
lang: de
title: "Was ist KI wirklich? Die Leiter von Regeln bis AGI, erzählt in einem Getränkebetrieb"
image: /assets/og/what-is-ai-ladder-rules-to-agi-beverage-plant.png
description: "Teil 1 von KI für Operational Excellence in Getränkebetrieben. Regeln, Machine Learning, Deep Learning, generative KI, agentische KI und AGI, eine Sprosse nach der anderen, jede mit einem echten Beispiel aus Brauerei, Weingut, Brennerei oder Abfülllinie. Ehrlich zu AGI: Es gibt sie noch nicht, und die Montagsschicht braucht sie nicht."
date: 2026-09-16 09:00:00 -0700
updated: 2026-09-16
permalink: /de/2026/what-is-ai-ladder-rules-to-agi-beverage-plant/
tags: [brewing-science, ai-opex, ai-basics, generative-ai, operational-excellence]
faq:
  - q: "Was ist der Unterschied zwischen KI, Machine Learning und generativer KI?"
    a: "KI ist der Oberbegriff für jede Software, die eine Aufgabe erledigt, die wir intelligent nennen würden. Machine Learning ist der Teil der KI, der Muster aus Daten lernt, statt Regeln zu befolgen, die jemand geschrieben hat. Generative KI ist eine Form von Machine Learning, die neue Inhalte wie Text oder Bilder erzeugt statt einer Vorhersage oder eines Labels. Jede davon ist eine Sprosse auf derselben Leiter, keine separate Technologie."
  - q: "Gibt es AGI im Jahr 2026?"
    a: "Nein. AGI, Artificial General Intelligence, bezeichnet ein System, das jede geistige Aufgabe, die ein Mensch kann, über alle Fachgebiete hinweg zuverlässig lernen und ausführen kann. Die heutigen großen Sprachmodelle sind beeindruckend und breit aufgestellt, machen aber immer noch grundlegende Fehler, sind ohne Prüfung nicht vertrauenswürdig und lernen nicht im Arbeitsalltag, wie ein Mensch es tut. Für einen Getränkebetrieb ist AGI eine Debatte, die man verfolgt, kein Werkzeug, mit dem man plant."
  - q: "Mit welcher Art von KI sollte eine Brauerei oder ein Abfüllbetrieb anfangen?"
    a: "In der Regel mit der niedrigsten Sprosse, die das Problem löst. Viele Probleme im Betrieb lassen sich mit besseren Regeln und statistischer Prozesskontrolle lösen. Machine Learning hilft, wo Muster zu komplex für Regeln sind, etwa bei der Vorhersage eines Pumpenausfalls. Generative KI hilft bei Text: SOPs, Schichtübergaben und Ursachennotizen. Agentische KI kommt zuletzt, wenn die Daten und die Freigaben stehen."
---

**Kurze Antwort: 'KI' ist nicht eine Sache. Es ist eine Leiter. Die unterste Sprosse sind einfache Regeln, wie sie schon in deiner SPS laufen. Darüber sitzt Machine Learning, das Muster aus Daten lernt, dann Deep Learning, das aus Bildern, Ton und langen Sensordatenströmen lernt. Generative KI erzeugt Text und Bilder. Agentische KI nutzt Tools und geht Schritte auf ein Ziel zu. Ganz oben steht AGI, eine allgemeine Intelligenz, die alles kann, was ein Mensch kann, und die es noch nicht gibt. Ein Getränkebetrieb zieht Nutzen aus jeder Sprosse außer der obersten. Die Kunst besteht darin, die niedrigste Sprosse zu wählen, die das anstehende Problem löst.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Eine KI-Leiter mit sechs Sprossen. Von unten: Regeln, etwa eine SPS-Verriegelung, die den Füller stoppt, wenn der Luftdruck fällt; Machine Learning, etwa die Vorhersage eines Pumpenausfalls aus Vibration; Deep Learning, etwa eine Kamera, die schiefe Etiketten erkennt; generative KI, etwa der Entwurf einer Schichtübergabe aus dem Protokoll; agentische KI, etwa ein Agent, der Linienstopps liest und einen Instandhaltungsauftrag entwirft; und ganz oben AGI, gestrichelt dargestellt, weil es sie noch nicht gibt.">
<rect width="1000" height="380" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DIE KI-LEITER IM GETRÄNKEBETRIEB</text>
<g font-family="sans-serif">
<rect x="60" y="48" width="880" height="42" rx="8" fill="#ffffff" stroke="#4a6b64" stroke-width="1.5" stroke-dasharray="6 4"/>
<text x="80" y="74" font-size="12.5" font-weight="700" fill="#4a6b64">AGI</text>
<text x="300" y="74" font-size="11.5" fill="#4a6b64">kann alles, was ein Mensch kann, fachübergreifend &#183; gibt es noch nicht</text>
<rect x="60" y="98" width="880" height="42" rx="8" fill="#06483f"/>
<text x="80" y="124" font-size="12.5" font-weight="700" fill="#ffffff">Agentische KI</text>
<text x="300" y="124" font-size="11.5" fill="#cfe6df">liest Linienstopps, entwirft einen Instandhaltungsauftrag zur Freigabe</text>
<rect x="60" y="148" width="880" height="42" rx="8" fill="#00695c"/>
<text x="80" y="174" font-size="12.5" font-weight="700" fill="#ffffff">Generative KI</text>
<text x="300" y="174" font-size="11.5" fill="#ffffff">entwirft die Schichtübergabe aus Protokoll und Bedienernotizen</text>
<rect x="60" y="198" width="880" height="42" rx="8" fill="#4db6a2"/>
<text x="80" y="224" font-size="12.5" font-weight="700" fill="#06483f">Deep Learning</text>
<text x="300" y="224" font-size="11.5" fill="#06483f">eine Kamera erkennt schiefe Etiketten und Unterfüllungen bei Liniengeschwindigkeit</text>
<rect x="60" y="248" width="880" height="42" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="80" y="274" font-size="12.5" font-weight="700" fill="#06483f">Machine Learning</text>
<text x="300" y="274" font-size="11.5" fill="#06483f">sagt einen Ausfall der Pasteurpumpe aus Vibration und Strom voraus</text>
<rect x="60" y="298" width="880" height="42" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="80" y="324" font-size="12.5" font-weight="700" fill="#06483f">Regeln</text>
<text x="300" y="324" font-size="11.5" fill="#06483f">SPS-Verriegelung stoppt den Füller, wenn der Luftdruck fällt</text>
<text x="500" y="366" text-anchor="middle" font-size="11" fill="#4a6b64">jede Sprosse enthält die darunter &#183; wähle die niedrigste Sprosse, die das Problem löst</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Sechs Sprossen, ein Betrieb. Fünf davon sind schon nützlich. Die oberste ist noch eine Forschungsfrage.</figcaption>
</figure>

Ein Betriebsleiter hat mich einmal gefragt, ob das neue Kamerasystem an der Etikettiermaschine 'KI oder nur eine Kamera' sei. Berechtigte Frage. Der Anbieter nannte es KI. Der Instandhaltungsleiter nannte es eine Kamera. Die Qualitätsmanagerin nannte es das Ding, das die Linie ohne Grund anhält. Alle drei hatten recht, und keiner von ihnen hatte ein gemeinsames Bild davon, was KI eigentlich ist.

Dies ist der erste Beitrag von **KI für Operational Excellence in Getränkebetrieben**, einer achtteiligen Serie, die bei den Grundlagen beginnt und mit Agenten endet, die Arbeitsaufträge entwerfen. Sie deckt Brauereien, Weingüter, Brennereien und die Abfülllinien ab, die sie alle gemeinsam haben. Bevor wir zu OEE und Agenten kommen, brauchen wir ein klares Bild davon, was die Begriffe bedeuten. Hier ist es, Sprosse für Sprosse.

## Sprosse 1: Regeln

Jeder Getränkebetrieb läuft bereits mit künstlicher Intelligenz der ältesten Art: Regeln, die ein Mensch geschrieben hat. Fällt der Luftdruck unter einen Sollwert, stoppe den Füller. Fällt der PU-Wert des Pasteurs unter das Minimum, schleuse das Gebinde aus. Hat die Leitfähigkeit im CIP-Rücklauf ihr Ziel nicht erreicht, verlängere den Laugenschritt.

Niemand nennt das heute noch KI, aber im Lehrbuchsinn ist es welche. Ein regelbasiertes System trifft Entscheidungen, für die sonst ein Mensch nötig wäre, mit einer Logik, die ein Mensch aufgeschrieben hat.

Regeln haben zwei große Stärken. Sie sind vorhersehbar, und sie sind prüfbar. Wenn der Füller stoppt, kannst du auf die Logikzeile zeigen, die ihn gestoppt hat. Für Sicherheits- und Lebensmittelsicherheitsentscheidungen ist das genau das, was man will, und deshalb verschwindet die unterste Sprosse nicht.

Ihre Schwäche ist, dass jemand die Regel kennen muss. Wenn das Muster zu kompliziert ist, um es aufzuschreiben, braucht man die nächste Sprosse.

## Sprosse 2: Machine Learning

Machine Learning ist Software, die die Regel aus Daten lernt, statt sie gesagt zu bekommen.

Nimm eine Pasteurpumpe. Niemand kann eine Regel schreiben, die besagt: 'Diese Kombination aus Vibration, Motorstrom und Temperatur bedeutet, dass das Lager in etwa zehn Tagen ausfällt.' Aber wenn du ein paar Jahre Sensordaten und ein Instandhaltungsprotokoll hast, das festhält, wann Lager ausgefallen sind, kann ein Machine-Learning-Modell dieses Muster finden. Es lernt, wie 'normal' aussieht, und meldet die Abweichung vor dem Ausfall.

Das ist die Kernidee, und sie deckt den Großteil der heute nützlichen KI in Betrieben ab: Stillstände vorhersagen, Nachfrage prognostizieren, einen Wert schätzen, den man nicht direkt messen kann, einen ungewöhnlichen Sud erkennen. Eine längere, allgemein verständliche Fassung für Brenner habe ich in [What Is Machine Learning?]({{ '/2026/what-is-machine-learning-distillery/' | relative_url }}) geschrieben, und sie gilt für eine Dosenlinie genauso.

Der Haken steckt im Halbsatz 'wenn du die Daten hast'. Machine Learning braucht Beispiele, gut gelabelt, aus einem Prozess, der sich darunter nicht verändert hat. Das erweist sich in jedem Betrieb, in dem ich gearbeitet habe, als der schwierige Teil.

## Sprosse 3: Deep Learning

Deep Learning ist Machine Learning mit neuronalen Netzen aus vielen Schichten. Es verdient eine eigene Sprosse, weil es aus unordentlichen, voluminösen Signalen lernen kann, mit denen ältere Methoden kämpfen: Bilder, Ton und lange Sensordatenströme.

An einer Abfülllinie ist das die Kamera, die bei 40.000 Flaschen pro Stunde jede Flasche auf Füllhöhe, Verschlusssitz und Etikettenausrichtung prüft. An einem Füller könnte es ein akustisches Modell sein, das hört, wie ein Ventil zu klemmen beginnt. In einer Mälzerei zählt es vielleicht Blattkeime unter dem Mikroskop.

Deep Learning braucht noch mehr Daten als klassisches Machine Learning, und es ist schwerer zu erklären. Wenn ein Kamerasystem eine Flasche ausschleust, kann es dir nicht in Worten sagen, warum. Es kann dir das Bild zeigen. Dieser Unterschied zählt, wenn eine Qualitätsmanagerin eine Ausschussquote verteidigen muss.

## Sprosse 4: Generative KI

Generative KI ist Deep Learning, das darauf trainiert ist, neue Inhalte zu erzeugen: Text, Bilder, Code, Sprache. Die großen Sprachmodelle hinter ChatGPT, Claude, Gemini und Copilot sind die bekanntesten Beispiele.

Der Unterschied hier: Die Ausgabe ist keine Zahl und kein Label. Sie ist Sprache. Im Betrieb ist das an Stellen nützlich, die die unteren Sprossen nie erreicht haben:

- das Protokoll und die Bedienernotizen einer Nachtschicht in eine klare Übergabe verwandeln
- 'Welche Laugenkonzentration gilt für die CIP des Drucktanks?' aus der SOP beantworten, mit Seitenangabe
- eine erste Fassung einer 5-Why-Analyse nach einem Linienstopp entwerfen
- eine Ein-Punkt-Lektion für eine mehrsprachige Mannschaft übersetzen

Bei generativer KI kommt auch die Halluzination ins Spiel. Diese Modelle erzeugen flüssigen, selbstsicheren Text, ob er stimmt oder nicht. Der [nächste Beitrag]({{ '/de/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}) erklärt anhand eines CIP-Protokolls und einer SOP, warum.

## Sprosse 5: Agentische KI

Ein Agent ist ein Sprachmodell, das Tools nutzen und Schritte auf ein Ziel hin gehen kann. Statt eine Frage zu beantworten, plant es, ruft ein Tool auf, schaut sich das Ergebnis an und entscheidet, was als Nächstes zu tun ist.

Im Betrieb könnte ein einfacher Agent das Linienstopp-Protokoll beobachten, bemerken, dass dieselbe Etikettierstörung die Linie diese Woche sechsmal gestoppt hat, die Anlage im Instandhaltungssystem nachschlagen, prüfen, ob schon ein Arbeitsauftrag existiert, und falls nicht, einen entwerfen, den ein Planer freigibt.

Dieser letzte Halbsatz ist das ganze Design. Ein Agent, der Entwürfe schreibt, ist nützlich. Ein Agent, der in eine SPS schreibt, ist ein Sicherheitsvorfall, der nur darauf wartet, zu passieren. Beitrag 3 dieser Serie behandelt, wie Agenten funktionieren, Beitrag 7 die Leitplanken im Detail.

## Sprosse 6: AGI

AGI, Artificial General Intelligence, bezeichnet ein System, das jede geistige Aufgabe, die ein Mensch kann, in jedem Fachgebiet zuverlässig lernen und erledigen kann. Das ist die Sprosse mit den Schlagzeilen.

Im Jahr 2026 gibt es sie nicht. Die besten Sprachmodelle sind breit aufgestellt und oft beeindruckend, machen aber immer noch grundlegende Fehler, müssen immer noch geprüft werden und lernen nicht aus einem Arbeitstag, wie es ein neuer Bediener tut. Ernsthafte Forscher sind sich uneinig, wie weit AGI entfernt ist und ob der heutige Ansatz überhaupt dorthin führt.

Hier ist, warum diese Debatte meiner Meinung nach für einen Betriebsleiter am Montagmorgen wenig zählt: Alles Nützliche in dieser Serie funktioniert auf den Sprossen unterhalb von AGI. Der Füller braucht keine allgemeine Intelligenz. Er braucht eine gute Regel, ein Modell, das Lagerverschleiß erkennt, eine Kamera, die schiefe Etiketten sieht, und einen Assistenten, der eine ordentliche Übergabe schreibt. Falls AGI kommt, braucht sie dieselben sauberen Daten und dieselben Freigaben. Diese jetzt aufzubauen ist so oder so keine Verschwendung.

## Wie man die Leiter nutzt

Wenn jemand 'KI' für ein Problem im Betrieb vorschlägt, frag, welche Sprosse. Dann frag, ob eine niedrigere reichen würde.

- Eine Temperaturabweichung braucht eine Regel und einen Alarm, kein Modell.
- Eine Pumpe, die ohne Vorwarnung ausfällt, braucht vielleicht Machine Learning.
- Ein schiefes Etikett bei Liniengeschwindigkeit braucht Deep Learning.
- Ein Schichtprotokoll, das niemand liest, braucht vielleicht generative KI.
- Ein Verlust, bei dem mehrere Systeme geprüft werden müssen, bevor jemand handelt, braucht vielleicht einen Agenten.

Je niedriger die Sprosse, desto günstiger, vorhersehbarer und leichter prüfbar die Lösung. Die Betriebe, die Nutzen aus KI ziehen, sind meist die, die hier ehrlich sind. Mein früherer Beitrag [AI vs Machine Learning vs Generative AI]({{ '/2026/ai-vs-machine-learning-vs-generative-ai-distillery/' | relative_url }}) macht denselben Punkt für Brennereien.

## Wo es bricht

**In echten Produkten verschwimmen die Sprossen.** Ein modernes Kamerasystem nutzt vielleicht Deep Learning, um den Fehler zu finden, und Regeln, um über das Ausschleusen zu entscheiden. Ein 'GenAI-Assistent' ruft darunter vielleicht ein Machine-Learning-Modell auf. Die Leiter ist eine Denkhilfe, keine Produktkategorie.

**Anbieter nennen alles KI.** Ein Schwellwertalarm mit neuem Dashboard bleibt ein Schwellwertalarm. Zu fragen, auf welcher Sprosse ein Produkt sitzt, ist der schnellste Weg herauszufinden, was man tatsächlich kauft.

**Höher ist nicht besser.** Eine Lebensmittelsicherheitsentscheidung von einer Regel in ein Modell zu verschieben, macht sie schwerer prüfbar. Manche Entscheidungen sollten bewusst auf der untersten Sprosse bleiben.

**AGI-Gerede kann Entscheidungen einfrieren.** 'Warum jetzt investieren, wenn AGI kommt?' ist eine häufige und teure Frage. Die Datengrundlagen, die Sensorqualität und die Freigabeprozesse, die du heute aufbaust, sind genau das, was jedes künftige System brauchen wird.

## Das Fazit

KI ist eine Leiter, keine einzelne Technologie. Regeln, Machine Learning, Deep Learning, generative KI und Agenten haben alle echte Aufgaben im Getränkebetrieb. AGI gibt es noch nicht, und sie wird für nichts davon gebraucht. Wähle die niedrigste Sprosse, die das Problem löst, und steig nur höher, wenn das Problem und die Daten es verlangen.

Als Nächstes: [was generative KI und große Sprachmodelle tatsächlich sind]({{ '/de/2026/what-is-genai-llm-tokens-rag-cip-log/' | relative_url }}), erklärt an einem CIP-Protokoll. Die Brennerei-Fassung dieser Grundlagen steht in [What Is AI, Really? A Distiller's Plain-Language Guide]({{ '/2026/what-is-ai-distilling-plain-language/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist der Unterschied zwischen KI, Machine Learning und generativer KI?**
KI ist der Oberbegriff für jede Software, die eine Aufgabe erledigt, die wir intelligent nennen würden. Machine Learning ist der Teil der KI, der Muster aus Daten lernt, statt Regeln zu befolgen, die jemand geschrieben hat. Generative KI ist eine Form von Machine Learning, die neue Inhalte wie Text oder Bilder erzeugt statt einer Vorhersage oder eines Labels. Jede davon ist eine Sprosse auf derselben Leiter, keine separate Technologie.

**Gibt es AGI im Jahr 2026?**
Nein. AGI, Artificial General Intelligence, bezeichnet ein System, das jede geistige Aufgabe, die ein Mensch kann, über alle Fachgebiete hinweg zuverlässig lernen und ausführen kann. Die heutigen großen Sprachmodelle sind beeindruckend und breit aufgestellt, machen aber immer noch grundlegende Fehler, sind ohne Prüfung nicht vertrauenswürdig und lernen nicht im Arbeitsalltag, wie ein Mensch es tut. Für einen Getränkebetrieb ist AGI eine Debatte, die man verfolgt, kein Werkzeug, mit dem man plant.

**Mit welcher Art von KI sollte eine Brauerei oder ein Abfüllbetrieb anfangen?**
In der Regel mit der niedrigsten Sprosse, die das Problem löst. Viele Probleme im Betrieb lassen sich mit besseren Regeln und statistischer Prozesskontrolle lösen. Machine Learning hilft, wo Muster zu komplex für Regeln sind, etwa bei der Vorhersage eines Pumpenausfalls. Generative KI hilft bei Text: SOPs, Schichtübergaben und Ursachennotizen. Agentische KI kommt zuletzt, wenn die Daten und die Freigaben stehen.
