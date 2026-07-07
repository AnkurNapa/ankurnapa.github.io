---
layout: post
lang: de
title: "Wie eine Brennerei mit KI und generativer KI starten sollte: Die Phasen"
image: /assets/og/how-a-distillery-starts-with-ai-and-gen-ai.png
description: "Ein phasenweiser Fahrplan für eine Brennerei, die KI und generative KI einführt — vom Sammeln der Daten über Dashboards, Vorhersagemodelle und GenAI-Copiloten bis zu Agenten — mit dem, was in jeder Phase zu tun, nötig und zu beachten ist."
date: 2026-02-04 09:00:00 -0700
updated: 2026-02-04
permalink: /de/2026/how-a-distillery-starts-with-ai-and-gen-ai/
tags: [distilling-maturation, ai-adoption, generative-ai, data-strategy, whiskey]
faq:
  - q: "Wie sollte eine Brennerei mit KI starten?"
    a: "Nicht mit KI — mit Daten. Phase 0 ist Messen und Sammeln: Erfasse jede Nachpeilung, damit das Fassbuch real ist, nicht geschätzt. Erst wenn du eine saubere, einzige Quelle der Wahrheit hast, zahlen sich Dashboards (Phase 1), Vorhersagemodelle (Phase 2), generative KI (Phase 3) und Agenten (Phase 4) aus. Das Fundament zu überspringen, ist der häufigste und teuerste Fehler."
  - q: "Was sind die Phasen der KI-Einführung für eine Brennerei?"
    a: "Fünf: Phase 0 sammeln und messen; Phase 1 sehen (Dashboards/BI); Phase 2 vorhersagen (maschinelles Lernen); Phase 3 generieren und unterstützen (generative KI-Copiloten); Phase 4 automatisieren (Agenten mit menschlicher Aufsicht). Jede Phase baut auf der vorherigen auf."
  - q: "Wo passt generative KI für eine Brennerei hin?"
    a: "In Phase 3, sobald Daten und Analytik existieren: ein Claude-Copilot, der den Bericht zur reifenden Ware entwirft und Fassfragen beantwortet. Generative KI entwirft, erklärt und antwortet in Klartext, aber sie muss in deinen Daten verankert sein, und ein Mensch verantwortet alles, was Sicherheit, Compliance oder eine maßgebliche Messung berührt."
---

**Kurze Antwort: Eine Brennerei sollte mit Daten starten, nicht mit KI. Der Weg hat fünf Phasen — sammeln und messen, sehen (Dashboards), vorhersagen (maschinelles Lernen), generieren und unterstützen (generative KI) und automatisieren (Agenten) — jede auf der vorherigen aufbauend. Unten steht, was in jeder Phase zu tun ist, was du brauchst und was du beachten musst. Der teuerste Fehler ist, KI zu kaufen, bevor das Datenfundament existiert.**

Jede Brennerei will wissen, wo sie mit KI anfangen soll. Die ehrliche Antwort enttäuscht und zahlt sich dann aus: Beginne damit, jede Nachpeilung zu erfassen, damit das Fassbuch real ist, nicht geschätzt. KI ist die Spitze einer Pyramide, die auf gemessenen Daten steht — überspringe die Basis, und der clevere Teil hat nichts, worauf er stehen kann. Das baut auf [deine Daten sammeln, bevor du KI nutzt]({{ '/de/2026/collect-your-data-before-ai/' | relative_url }}) auf.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 360" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Die Phasen der KI-Einführung für eine Brennerei"><rect x="0" y="0" width="1000" height="360" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Die Phasen der KI-Einführung für eine Brennerei</text><g font-family="sans-serif"><rect x="16" y="274" width="176" height="46" rx="6" fill="#f0f6f5" stroke="#06483f" stroke-width="1.5"/><text x="104" y="298" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">Phase 0</text><text x="104" y="318" text-anchor="middle" font-size="11.5" fill="#06483f">Sammeln &amp; messen</text><rect x="202" y="228" width="176" height="92" rx="6" fill="#f0f6f5" stroke="#06483f" stroke-width="1.5"/><text x="290" y="252" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">Phase 1</text><text x="290" y="272" text-anchor="middle" font-size="11.5" fill="#06483f">Sehen (BI)</text><rect x="388" y="182" width="176" height="138" rx="6" fill="#f0f6f5" stroke="#06483f" stroke-width="1.5"/><text x="476" y="206" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">Phase 2</text><text x="476" y="226" text-anchor="middle" font-size="11.5" fill="#06483f">Vorhersagen (ML)</text><rect x="574" y="136" width="176" height="184" rx="6" fill="#f0f6f5" stroke="#06483f" stroke-width="1.5"/><text x="662" y="160" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">Phase 3</text><text x="662" y="180" text-anchor="middle" font-size="11.5" fill="#06483f">Generieren (GenAI)</text><rect x="760" y="90" width="176" height="230" rx="6" fill="#f0f6f5" stroke="#06483f" stroke-width="1.5"/><text x="848" y="114" text-anchor="middle" font-size="12.5" font-weight="700" fill="#06483f">Phase 4</text><text x="848" y="134" text-anchor="middle" font-size="11.5" fill="#06483f">Automatisieren (Agenten)</text></g><line x1="16" y1="334" x2="936" y2="334" stroke="#4a6b64" stroke-width="1"/><text x="30" y="352" font-family="sans-serif" font-size="11.5" fill="#4a6b64">hier starten</text><text x="970" y="352" text-anchor="end" font-family="sans-serif" font-size="11.5" fill="#4a6b64">mehr Wert, mehr Strenge →</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Klettere der Reihe nach — jede Phase steht auf den Daten und dem Vertrauen, die die vorherige aufgebaut hat.</figcaption>
</figure>

## Phase 0 — Sammeln und messen

Vor jedem Modell: Schaffe eine saubere, einzige Quelle der Wahrheit. Für eine Brennerei bedeutet das, jede Nachpeilung zu erfassen, damit das Fassbuch real ist, nicht geschätzt — Messgeräte, Protokolle und Aufzeichnungen, die vertrauenswürdig sind. Du kannst nicht optimieren, was du nicht misst, und die meisten gescheiterten KI-Projekte sterben hier, nicht im Algorithmus.

## Phase 1 — Sehen (Dashboards und BI)

Sobald die Daten existieren, mache sie sichtbar: eine Power-BI-Sicht auf reifende Ware, Fassbestand und Bewertung. Dashboards verwandeln Daten in Entscheidungen und fördern die Fragen zutage, die es später zu modellieren lohnt. Allein diese Phase bezahlt das Fundament.

## Phase 2 — Vorhersagen (maschinelles Lernen)

Mit vorhandener Historie füge Vorhersage hinzu: ein Modell für den Angels' Share oder die Abfüllreife. Modelle verdienen sich ihr Geld beim Routinemäßigen und Stetigen; sie sagen den seltenen Ausfall schlecht voraus, also behandle sie als Entscheidungsunterstützung, nicht als Autopilot.

## Phase 3 — Generieren und unterstützen (generative KI)

Jetzt passt generative KI: ein Claude-Copilot, der den Bericht zur reifenden Ware entwirft und Fassfragen beantwortet. In deinen Daten verankert — siehe den Leitfaden [das Claude-Ökosystem für Brennereien]({{ '/de/2026/claude-ai-claude-code-for-distilleries/' | relative_url }}) — entwirft, erklärt und antwortet er in Klartext, mit einem Menschen, der alles prüft, was eine Behörde, ein Etikett oder einen Kunden erreicht.

## Phase 4 — Automatisieren (Agenten)

Schließlich schließen Agenten Routineschleifen: ein Agent, der den wöchentlichen Lager- und Bewertungsbericht zur Abzeichnung zusammenstellt. Das ist die mächtigste und die am stärksten überverkaufte Phase — behalte einen Menschen, der alles Folgenreiche genehmigt, und automatisiere nur, was du bereits von Hand vertraust.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Alles steht auf den Daten"><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360" y="30" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Alles steht auf den Daten</text><g font-family="sans-serif"><polygon points="330.0,70 390.0,70 430.0,132 290.0,132" fill="#06483f" stroke="#06483f"/><text x="360" y="98" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">KI &amp; GenAI</text><text x="360" y="116" text-anchor="middle" font-size="11" fill="#fff">Copiloten, Agenten, Modelle</text><polygon points="290.0,138 430.0,138 490.0,200 230.0,200" fill="#06483f" stroke="#06483f"/><text x="360" y="166" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">Analytik</text><text x="360" y="184" text-anchor="middle" font-size="11" fill="#fff">Dashboards &amp; KPIs</text><polygon points="230.0,206 490.0,206 560.0,268 160.0,268" fill="#f0f6f5" stroke="#06483f"/><text x="360" y="234" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">Datenfundament</text><text x="360" y="252" text-anchor="middle" font-size="11" fill="#06483f">Messgeräte, Protokolle, eine Quelle der Wahrheit</text></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die Pyramide ist der Punkt: GenAI an der Spitze ist nur so gut wie die gemessenen Daten an der Basis.</figcaption>
</figure>

## Wo Unternehmen es falsch machen

Drei ehrliche Grenzen. Erstens: **überspringe keine Phasen** — einen GenAI-Copiloten zu kaufen, bevor du saubere Daten hast, liefert selbstsichere Antworten über Müll. Zweitens: **ein Modell verantwortet nie eine maßgebliche Messung** — Verbrauchsteuer-, Sicherheits- und Etikettzahlen führen auf Instrumente und Abzeichnung zurück, nicht auf Vorhersagen. Drittens: **die Plattform ist nicht der Punkt** — ob du auf [Microsoft Fabric für Brennereien]({{ '/de/2026/microsoft-fabric-for-distilleries-20-use-cases/' | relative_url }}) oder einer Tabelle baust, die Phasen sind dieselben; Werkzeuge dienen dem Fahrplan, nicht umgekehrt.

## Das Fazit

Die KI-Reise einer Brennerei ist eine Leiter, kein Sprung: sammeln, sehen, vorhersagen, generieren, automatisieren. Beginne in Phase 0 — erfasse jede Nachpeilung, damit das Fassbuch real ist, nicht geschätzt — und verdiene dir jede Sprosse vor der nächsten. Die Unternehmen, die mit KI gewinnen, sind die, die zuerst langweilig über Daten geworden sind.

## Häufig gestellte Fragen

**Wie sollte eine Brennerei mit KI starten?**
Nicht mit KI — mit Daten. Phase 0 ist Messen und Sammeln: Erfasse jede Nachpeilung, damit das Fassbuch real ist, nicht geschätzt. Erst wenn du eine saubere, einzige Quelle der Wahrheit hast, zahlen sich Dashboards (Phase 1), Vorhersagemodelle (Phase 2), generative KI (Phase 3) und Agenten (Phase 4) aus. Das Fundament zu überspringen, ist der häufigste und teuerste Fehler.

**Was sind die Phasen der KI-Einführung für eine Brennerei?**
Fünf: Phase 0 sammeln und messen; Phase 1 sehen (Dashboards/BI); Phase 2 vorhersagen (maschinelles Lernen); Phase 3 generieren und unterstützen (generative KI-Copiloten); Phase 4 automatisieren (Agenten mit menschlicher Aufsicht). Jede Phase baut auf der vorherigen auf.

**Wo passt generative KI für eine Brennerei hin?**
In Phase 3, sobald Daten und Analytik existieren: ein Claude-Copilot, der den Bericht zur reifenden Ware entwirft und Fassfragen beantwortet. Generative KI entwirft, erklärt und antwortet in Klartext, aber sie muss in deinen Daten verankert sein, und ein Mensch verantwortet alles, was Sicherheit, Compliance oder eine maßgebliche Messung berührt.

*Teil des Tracks [Distilling &amp; Maturation]({{ '/de/tracks/distilling-maturation/' | relative_url }}).*
