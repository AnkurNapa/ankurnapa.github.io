---
layout: post
lang: de
title: "Ein LLM-Copilot für den Brennblasenbediener: RAG über SOPs, Read-only-Tools, keine Sollwerte"
image: /assets/og/llm-copilot-still-operator.png
description: "Teil 3 von The Still and the Model. Was ein GenAI-Copilot im Brennhaus tun sollte und was nicht: aus gelenkten SOPs und Brennprotokollen mit Quellenangabe antworten, Live-Werte über Read-only-Tools lesen, die Schichtübergabe schreiben und niemals einen Sollwert, eine Verriegelung oder einen Schnitt anfassen."
date: 2026-08-01 09:00:00 -0700
updated: 2026-08-01
permalink: /de/2026/llm-copilot-still-operator/
tags: [distilling-maturation, still-and-model, generative-ai, rag, ai-agents]
faq:
  - q: "Was kann ein LLM-Copilot für einen Bediener in der Brennerei tun?"
    a: "Er kann Verfahrensfragen aus den gelenkten SOPs beantworten und den Absatz zitieren, vergangene Brennprotokolle nach ähnlichen Situationen durchsuchen, Live-Prozesswerte über Read-only-Tools lesen und die Schichtübergabe aus Historian und Bedienernotizen entwerfen. Er spart Zeit beim Suchen und Schreiben, und das ist ein großer Teil einer Schicht."
  - q: "Sollte ein KI-Copilot Sollwerte an der Brennblase ändern dürfen?"
    a: "Nein. Der Copilot sollte überhaupt keine schreibenden Tools haben. Sollwerte, Verriegelungen und Schnittentscheidungen bleiben beim Bediener und beim Leitsystem. Das einfachste Sicherheitskonzept ist das Tool, das es nicht gibt: Wenn das Modell set_setpoint nicht aufrufen kann, kann auch kein Prompt es dazu bringen."
  - q: "Wie verhindert man, dass ein Copilot im Brennhaus falsche Verfahrensantworten gibt?"
    a: "Das Retrieval nur auf die aktuellen gelenkten Versionen der SOPs richten, das Modell den verwendeten Absatz zitieren und verlinken lassen, die Antwort verweigern, wenn keine Quelle gefunden wird, und es vor und nach jeder Änderung gegen einen Satz echter Bedienerfragen mit geprüften Antworten testen. Bei allem, was die Sicherheit betrifft, liest der Bediener die Quelle, bevor er handelt."
---

**Kurze Antwort: Ein Copilot im Brennhaus lohnt sich, wenn er das Lesen und Schreiben übernimmt, das eine Schicht auffrisst, und sonst nichts. Richte ihn auf die gelenkten SOPs und die Brennprotokolle aus mehreren Jahren, lass ihn den verwendeten Absatz zitieren, gib ihm Read-only-Tools für Live-Werte aus dem Historian und lass ihn am Schichtende die Übergabe entwerfen. Gib ihm überhaupt keine schreibenden Tools. Sollwerte, Verriegelungen und Schnitte bleiben beim Bediener und beim Leitsystem. Das sicherste Tool an einer Brennblase ist das, das dem Modell nie gegeben wurde.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Ein LLM-Copilot in der Mitte. Links seine Quellen: gelenkte SOPs, Brennprotokolle und Schichtnotizen über Retrieval sowie Live-Werte aus dem Historian über Read-only-Tools namens get_value, get_trend und get_run_summary. Rechts seine Ergebnisse: Antworten mit zitiertem SOP-Absatz, ein Entwurf der Schichtübergabe und ein Entwurf einer Abweichungsmeldung, den ein Mensch vervollständigt. Unten ein durchgestrichenes Tool namens set_setpoint mit dem Hinweis, dass Sollwerte, Verriegelungen und Schnitte beim Bediener bleiben.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">EIN COPILOT, DER WÖRTER LIEST UND SCHREIBT, NIE SOLLWERTE</text>
<g font-family="sans-serif">
<rect x="30" y="56" width="270" height="90" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="165" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Retrieval</text>
<text x="165" y="102" text-anchor="middle" font-size="10.5" fill="#4a6b64">gelenkte SOPs (aktuelle Versionen)</text>
<text x="165" y="120" text-anchor="middle" font-size="10.5" fill="#4a6b64">Brennprotokolle &#183; Schichtnotizen</text>
<rect x="30" y="160" width="270" height="90" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="165" y="186" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">Read-only-Tools</text>
<text x="165" y="206" text-anchor="middle" font-size="10.5" fill="#4a6b64">get_value &#183; get_trend</text>
<text x="165" y="224" text-anchor="middle" font-size="10.5" fill="#4a6b64">get_run_summary</text>
<line x1="300" y1="101" x2="400" y2="140" stroke="#4db6a2" stroke-width="2"/>
<line x1="300" y1="205" x2="400" y2="170" stroke="#4db6a2" stroke-width="2"/>
<rect x="400" y="110" width="200" height="90" rx="12" fill="#06483f"/>
<text x="500" y="150" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">LLM-Copilot</text>
<text x="500" y="172" text-anchor="middle" font-size="10.5" fill="#cfe6df">antwortet, zitiert, entwirft</text>
<line x1="600" y1="140" x2="700" y2="85" stroke="#4db6a2" stroke-width="2"/>
<line x1="600" y1="155" x2="700" y2="155" stroke="#4db6a2" stroke-width="2"/>
<line x1="600" y1="170" x2="700" y2="225" stroke="#4db6a2" stroke-width="2"/>
<rect x="700" y="60" width="270" height="50" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="90" text-anchor="middle" font-size="11.5" fill="#06483f">Antwort + zitierter SOP-Absatz</text>
<rect x="700" y="130" width="270" height="50" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="160" text-anchor="middle" font-size="11.5" fill="#06483f">Entwurf der Schichtübergabe</text>
<rect x="700" y="200" width="270" height="50" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="835" y="230" text-anchor="middle" font-size="11.5" fill="#06483f">Entwurf der Abweichungsmeldung</text>
<rect x="30" y="272" width="940" height="44" rx="10" fill="#06483f"/>
<text x="180" y="299" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ff4081" text-decoration="line-through">set_setpoint()</text>
<text x="600" y="299" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">SOLLWERTE, VERRIEGELUNGEN UND SCHNITTE BLEIBEN BEIM BEDIENER</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Alles auf der linken Seite wird gelesen. Alles auf der rechten Seite ist ein Entwurf. Das fehlende Tool unten ist das Sicherheitskonzept.</figcaption>
</figure>

Es ist sechs Uhr morgens, Schichtwechsel. Der Nachtbediener hat eine Seite Notizen, einen Brennlauf, der gegen zwei Uhr etwas langsam lief, und einen Kondensatableiter, der gezischt hat. Der Tagbediener bekommt fünf Minuten Übergabe, und die Hälfte davon geht dafür drauf, herauszufinden, welche Laufnummer die langsame war. Später am Vormittag fragt ein Auszubildender, wie der Wechsel des Nachlaufvorlagebehälters nach einer CIP-Reinigung gemacht wird, und die Antwort steht in einer SOP, die auf dem gemeinsamen Laufwerk niemand findet.

Nichts davon ist ein Regelungsproblem. Es ist ein Lese- und Schreibproblem, und Lesen und Schreiben ist genau das, worin große Sprachmodelle wirklich gut sind. In diesem Beitrag geht es um einen Copiloten für diese Aufgabe und um die eine Sache, die er niemals können darf.

## Wofür der Copilot da ist

Vier Aufgaben, grob nach Nutzen geordnet:

**1. Verfahrensfragen, beantwortet aus der Quelle.** Retrieval-Augmented Generation (RAG) über die gelenkten SOPs: Der Bediener fragt in einfachen Worten, der Copilot findet den passenden Absatz, antwortet und zitiert ihn mit Dokumentnummer und Version. Findet er keine Quelle, sagt er das, statt zu improvisieren.

**2. 'Ist das schon einmal passiert?'** Brennprotokolle und Schichtnotizen aus mehreren Jahren dokumentieren jeden ungewöhnlichen Lauf und was ihn behoben hat. Eine semantische Suche darüber macht aus 'langsamer Lauf nach Kesselausfall, Stärke fällt früh' eine Liste ähnlicher früherer Läufe und dessen, was der Bediener damals notiert hat. Das ist oft der nützlichste Punkt auf der Liste, und es ist vergrabener Text, den heute niemand liest.

**3. Die Schichtübergabe.** Am Schichtende holt der Copilot die Brennläufe aus dem Historian, die Bandmeldungen aus dem [Beitrag zu Soft Sensoren]({{ '/de/2026/soft-sensors-proactive-bands-spirit-safe/' | relative_url }}), die Notizen des Bedieners und alle offenen Arbeitsaufträge und entwirft eine einseitige Übergabe. Der Bediener bearbeitet und unterschreibt sie. Die Tagschicht bekommt eine einheitliche Zusammenfassung statt dessen, was die Nachtschicht um 5:45 Uhr noch an Energie zum Schreiben hatte.

**4. Den Papierkram entwerfen.** Abweichungsmeldungen, Beinahe-Unfall-Berichte und Wartungsanforderungen beginnen mit einem Entwurf, an dem Laufnummer, Zeitstempel und Werte schon hängen.

## Die Tools: von Grund auf read-only

Damit der Copilot über die laufende Anlage sprechen kann, braucht er Daten, und der saubere Weg, sie 2026 bereitzustellen, ist ein kleiner Satz von Tools (meist über MCP bereitgestellt), die auf dem Historian aufsetzen:

```text
get_value(tag)                      -> current value, unit, timestamp, quality
get_trend(tag, from, to)            -> time series, downsampled
get_run_summary(still, run_id)      -> charge, cuts, fractions, alcohol balance
search_run_logs(query, still)       -> matching notes with run ids
```

Jedes Tool liest. Keines schreibt. Es gibt kein `set_setpoint`, kein `acknowledge_alarm`, kein `open_valve`. Das ist keine Richtlinie im Prompt, um die sich ein ausreichend geschickter Prompt herumreden kann. Es ist das Fehlen der Fähigkeit. Ein Modell kann kein Tool aufrufen, das es nicht gibt.

Die Verbindung zum Historian selbst sollte aus demselben Grund auch auf Netzwerk- und Kontoebene read-only sein. Das Leitsystem hat seine eigene Sicherheitsebene, seine Verriegelungen und seine Ingenieure, und ein Sprachmodell hat dort nichts verloren.

## Die Antworten vertrauenswürdig machen

Ein Copilot, der sicher klingt und bei einem Verfahren falschliegt, ist schlimmer als gar keiner. Ein paar Regeln erledigen den Großteil der Arbeit:

1. **Nur aktuelle, gelenkte Dokumente im Index.** Wird eine SOP überarbeitet, fliegt die alte Version noch am selben Tag aus dem Retrieval. Überholte Verfahren im Index sind der häufigste Grund, warum solche Systeme selbstsicher falsche Antworten geben.
2. **Zitieren oder verweigern.** Jede Verfahrensantwort zitiert den Absatz und verlinkt das Dokument. Keine Quelle, keine Antwort.
3. **Zahlen aus Tools, nie aus dem Modell.** Fragt der Bediener nach der Austrittstemperatur am Kondensator, ruft der Copilot `get_value` auf und meldet, was zurückkam, mit Zeitstempel. Er schätzt nicht.
4. **Ein echter Evaluationsdatensatz.** Sammle fünfzig Fragen, die Bediener tatsächlich gestellt haben, mit vom Schichtleiter geprüften Antworten, und lass sie jedes Mal laufen, wenn sich Modell, Prompt oder Dokumentindex ändern. Bewerte das Ergebnis. Es ist die einzige ehrliche Antwort auf die Frage, ob er gut genug ist.

## Wo das an Grenzen stößt

**Sicherheitskritische Fragen brauchen die Quelle, nicht die Zusammenfassung.** Bei allem, was Freischaltung, enge Räume, Heißarbeiten oder Ethanoldampf betrifft, besteht die Aufgabe des Copiloten darin, die richtige SOP zu öffnen, nicht sie zu umschreiben. Mach das zur harten Regel im Design und in der Schulung.

**Brennprotokolle sind unordentlich und manchmal falsch.** Die semantische Suche findet bereitwillig eine Notiz von 2021, in der steht 'behoben durch mehr Dampf', und das war vielleicht die falsche Lösung. Frühere Notizen sind Hinweise, keine Anweisungen.

**Übergabeentwürfe können Probleme glätten.** Eine ordentliche Zusammenfassung kann eine unruhige Nacht nach Routine klingen lassen. Der Bediener, der die Schicht erlebt hat, muss sie bearbeiten und unterschreiben, und der Entwurf sollte Bandmeldungen und offene Punkte ausdrücklich auflisten, statt sie wegzufassen.

**Die Leute werden ihm mit der Zeit mehr vertrauen.** Je besser er wird, desto weniger prüft jemand nach. Das ist das Argument dafür, den Evaluationsdatensatz dauerhaft laufen zu lassen, nicht nur beim Start.

## Das Fazit

Im Brennhaus steckt in dem Betriebsproblem ein Lese- und Schreibproblem: Verfahren, die niemand findet, Brennprotokolle, die niemand liest, und Übergaben, die im Halbschlaf geschrieben werden. Genau darin ist ein Sprachmodell gut. Gib ihm die gelenkten Dokumente, die Protokolle und Read-only-Tools, lass es zitieren, teste es mit echten Fragen, und es spart der Schicht echte Zeit. Gib ihm nichts, was schreibt. Der Bediener fährt die Brennblase. Der Copilot erledigt den Papierkram.

Den breiteren Blick auf die Anthropic-Tools in einer Brennerei gibt es in [Claude AI und Claude Code für Brennereien]({{ '/de/2026/claude-ai-claude-code-for-distilleries/' | relative_url }}). Dieselbe Regel, nur vorzuschlagen und nie zu schreiben, taucht in der Weinserie beim [Event Sourcing des Weinkellers]({{ '/de/2026/event-sourced-cellar-records-winery/' | relative_url }}) auf. Als Nächstes in dieser Serie: [Fassbestand als Data Engineering]({{ '/de/2026/cask-inventory-data-engineering-scd2/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite von The Still and the Model]({{ '/series/still-and-model/' | relative_url }}).

## Häufig gestellte Fragen

**Was kann ein LLM-Copilot für einen Bediener in der Brennerei tun?**
Er kann Verfahrensfragen aus den gelenkten SOPs beantworten und den Absatz zitieren, vergangene Brennprotokolle nach ähnlichen Situationen durchsuchen, Live-Prozesswerte über Read-only-Tools lesen und die Schichtübergabe aus Historian und Bedienernotizen entwerfen. Er spart Zeit beim Suchen und Schreiben, und das ist ein großer Teil einer Schicht.

**Sollte ein KI-Copilot Sollwerte an der Brennblase ändern dürfen?**
Nein. Der Copilot sollte überhaupt keine schreibenden Tools haben. Sollwerte, Verriegelungen und Schnittentscheidungen bleiben beim Bediener und beim Leitsystem. Das einfachste Sicherheitskonzept ist das Tool, das es nicht gibt: Wenn das Modell set_setpoint nicht aufrufen kann, kann auch kein Prompt es dazu bringen.

**Wie verhindert man, dass ein Copilot im Brennhaus falsche Verfahrensantworten gibt?**
Das Retrieval nur auf die aktuellen gelenkten Versionen der SOPs richten, das Modell den verwendeten Absatz zitieren und verlinken lassen, die Antwort verweigern, wenn keine Quelle gefunden wird, und es vor und nach jeder Änderung gegen einen Satz echter Bedienerfragen mit geprüften Antworten testen. Bei allem, was die Sicherheit betrifft, liest der Bediener die Quelle, bevor er handelt.
