---
layout: post
lang: de
title: "Agentic AI für OpEx: Ein OEE-Verlust-Agent, der Arbeitsaufträge entwirft, und die Leitplanken, die ihn von der SPS fernhalten"
image: /assets/og/agentic-ai-opex-oee-agent-cmms-guardrails.png
description: "Teil 7 von KI für Operational Excellence in Getränkebetrieben. Ein Agent, der jede Schicht die OEE-Verluste beobachtet, wiederkehrende Störungen findet, das CMMS prüft und Arbeitsaufträge sowie Umstellungspläne zur Freigabe durch Menschen entwirft. Dazu die Leitplanken, auf die es ankommt: das Purdue-Modell, reiner Lesezugriff auf OT-Daten, keine Schreibzugriffe auf SPS oder SCADA, Freigaben, ein Audit-Log und Replay-Evals."
date: 2026-09-22 09:00:00 -0700
updated: 2026-09-22
permalink: /de/2026/agentic-ai-opex-oee-agent-cmms-guardrails/
tags: [brewing-science, ai-opex, agentic-ai, predictive-maintenance, ot-security]
faq:
  - q: "Was kann ein KI-Agent in einem Getränkebetrieb sicher tun?"
    a: "Produktions-, Instandhaltungs- und Qualitätsdaten lesen, herausarbeiten, welche Verluste zählen, und Maßnahmen für Menschen entwerfen: Instandhaltungsaufträge, Umstellungspläne, Schichtzusammenfassungen, Nachrichten an einen Planer. Jeder Entwurf trägt seine Belege und wartet auf Freigabe. Einen Weg, auf SPS, SCADA oder Prozesssollwerte zu schreiben, sollte er nicht haben."
  - q: "Was ist das Purdue-Modell und warum ist es für KI-Agenten wichtig?"
    a: "Das Purdue-Modell ist eine Referenzarchitektur, die die Netzwerke eines Werks in Ebenen trennt, vom physischen Prozess und seinen Steuerungen unten bis zu den Geschäftssystemen oben, mit einer demilitarisierten Zone zwischen Betrieb und Unternehmens-IT. Ein Agent gehört auf die IT-Seite und liest replizierte Daten aus der DMZ. Er sollte niemals Verbindungen hinunter in die Steuerungsebenen öffnen."
  - q: "Wie testet man einen KI-Agenten, bevor man ihn auf ein Werk loslässt?"
    a: "Mit einem Replay der Historie. Man lässt den Agenten über die Schichten der letzten ein, zwei Monate laufen, mit den Daten so, wie sie damals waren, und vergleicht seine Entwürfe mit dem, was Planer und Ingenieure tatsächlich getan haben. Gemessen wird, wie viele echte Probleme er gefunden hat, wie viele Entwürfe Rauschen waren und wie viele falsch gewesen wären. Das Replay wird wiederholt, sobald sich Modell, Prompts oder Tools ändern."
---

**Kurze Antwort: Der nützlichste Agent in einem Getränkebetrieb ist kein Roboter-Bediener. Er ist ein geduldiger Analyst, der am Ende jeder Schicht das Stillstandsprotokoll liest, die OEE-Verluste ordnet, bemerkt, dass die Leimeinheit der Etikettiermaschine die Linie diese Woche sechsmal angehalten hat, das Instandhaltungssystem prüft, keinen offenen Arbeitsauftrag findet und einen entwirft, mit angehängten Belegen, zur Freigabe durch einen Planer. Derselbe Agent kann eine Umstellungsreihenfolge entwerfen, die Spülzeit spart. Sicher macht ihn nicht das Modell. Sicher macht ihn die Architektur: reiner Lesezugriff auf replizierte OT-Daten auf der IT-Seite des Purdue-Modells, kein Weg zu SPS oder SCADA, Schreib-Tools, die nur Entwürfe anlegen, ein Audit-Log jedes Tool-Aufrufs und Replay-Tests vor dem Livegang.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Das Purdue-Modell mit einem darauf platzierten KI-Agenten. Die Ebenen 0 bis 2 unten enthalten den Prozess, die SPS und SCADA. Ebene 3 enthält Historian, MES und CMMS. Eine DMZ enthält eine schreibgeschützte Replik der Historian- und MES-Daten. Die Ebenen 4 und 5 enthalten die Unternehmens-IT, in der der Agent läuft. Der Agent liest aus der DMZ-Replik und schreibt nur Entwürfe von Arbeitsaufträgen ins CMMS, die ein Planer freigibt. Ein durchgestrichener Pfeil vom Agenten zu SPS und SCADA zeigt, dass er keinen Schreibweg in die Prozesssteuerung hat. Ein Audit-Log erfasst jeden Tool-Aufruf.">
<rect width="1000" height="380" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">WO DER AGENT LEBT UND WAS ER ERREICHEN KANN</text>
<g font-family="sans-serif">
<rect x="40" y="50" width="600" height="62" rx="9" fill="#06483f"/>
<text x="60" y="76" font-size="11" font-weight="700" fill="#cfe6df">EBENEN 4-5 &#183; UNTERNEHMENS-IT</text>
<rect x="330" y="60" width="160" height="42" rx="8" fill="#ffffff"/>
<text x="410" y="86" text-anchor="middle" font-size="12" font-weight="700" fill="#06483f">OEE-Verlust-Agent</text>
<rect x="40" y="124" width="600" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5" stroke-dasharray="6 4"/>
<text x="60" y="148" font-size="11" font-weight="700" fill="#00695c">DMZ</text>
<text x="60" y="166" font-size="10.5" fill="#4a6b64">schreibgeschützte Replik: Historian-Tags, MES-Stillstände</text>
<rect x="40" y="192" width="600" height="56" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="60" y="216" font-size="11" font-weight="700" fill="#06483f">EBENE 3 &#183; STANDORTBETRIEB</text>
<text x="60" y="234" font-size="10.5" fill="#4a6b64">Historian &#183; MES &#183; CMMS &#183; LIMS</text>
<rect x="40" y="260" width="600" height="56" rx="9" fill="#ffffff" stroke="#4a6b64" stroke-width="1.5"/>
<text x="60" y="284" font-size="11" font-weight="700" fill="#06483f">EBENEN 0-2 &#183; PROZESS UND STEUERUNG</text>
<text x="60" y="302" font-size="10.5" fill="#4a6b64">Sensoren &#183; SPS &#183; SCADA &#183; HMIs</text>
<line x1="410" y1="102" x2="410" y2="124" stroke="#2e9e7c" stroke-width="2.5"/>
<text x="425" y="118" font-size="10" fill="#2e9e7c">liest</text>
<path d="M490 81 C560 81 560 220 520 220" fill="none" stroke="#2e9e7c" stroke-width="2.5"/>
<text x="566" y="150" font-size="10" fill="#2e9e7c">nur Entwürfe</text>
<text x="500" y="224" font-size="10" text-anchor="end" fill="#2e9e7c">CMMS-Entwurf</text>
<line x1="345" y1="102" x2="345" y2="260" stroke="#ff4081" stroke-width="2.5" stroke-dasharray="5 4"/>
<line x1="335" y1="244" x2="355" y2="264" stroke="#ff4081" stroke-width="3"/>
<line x1="355" y1="244" x2="335" y2="264" stroke="#ff4081" stroke-width="3"/>
<text x="352" y="188" font-size="10" font-weight="700" fill="#ff4081">kein Schreibweg zur Steuerung</text>
<rect x="680" y="50" width="280" height="266" rx="9" fill="#ffffff" stroke="#00695c" stroke-width="1.5"/>
<text x="820" y="76" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">LEITPLANKEN</text>
<g font-size="11" fill="#06483f">
<text x="700" y="106">1. OT-Daten nur lesend, über DMZ</text>
<text x="700" y="134">2. nie auf SPS oder SCADA schreiben</text>
<text x="700" y="162">3. Schreib-Tools nur für Entwürfe</text>
<text x="700" y="190">4. ein Mensch gibt jeden Entwurf frei</text>
<text x="700" y="218">5. Audit-Log jedes Tool-Aufrufs</text>
<text x="700" y="246">6. Replay-Evals vor dem Livegang</text>
<text x="700" y="274">7. Schritt-, Kosten-, Ratenlimits</text>
<text x="700" y="302">8. ein Schalter schaltet ihn ab</text>
</g>
<rect x="40" y="330" width="920" height="38" rx="10" fill="#06483f"/>
<text x="500" y="354" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">DAS MODELL KANN IRREN &#183; DIE ARCHITEKTUR SORGT DAFÜR, DASS DAS BILLIG BLEIBT</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Der Agent sitzt bei den Geschäftssystemen, liest eine Replik der Anlagendaten und kann nur Entwürfe anlegen. Die Prozesssteuerung ist bewusst außer Reichweite.</figcaption>
</figure>

Jedes Werk hat eine Liste von Verlusten, die alle kennen und denen niemand Zeit widmen kann. Die Etikettiermaschine, die ein Dutzend Mal pro Schicht für dreißig Sekunden steht. Die Umstellung, die immer zwanzig Minuten zu lang dauert. Die Pumpe, die auslöst, sobald die Umgebungstemperatur 35 Grad übersteigt. Jeder einzelne Verlust ist klein. Zusammen sind sie oft der größte Balken im [OEE-Wasserfall]({{ '/de/2026/operational-excellence-basics-oee-for-data-people/' | relative_url }}).

Der [dritte Beitrag dieser Reihe]({{ '/de/2026/what-is-agentic-ai-tools-mcp-autonomy-levels/' | relative_url }}) hat erklärt, wie Agenten funktionieren. Dieser, der siebte, setzt einen auf diese Verluste an und verwendet mindestens genauso viel Zeit auf die Zäune drumherum.

## Der OEE-Verlust-Agent, Schritt für Schritt

So arbeitet ein gut abgegrenzter Agent am Ende jeder Schicht. Jeder Schritt ist ein Tool-Aufruf an eine getestete Abfrage oder ein kontrolliertes System.

1. **Verluste ordnen.** Die Stillstände der Schicht aus der MES-Replik holen und nach den sechs großen Verlusten und nach Anlage gruppieren. Die Leimeinheit der Etikettiermaschine kommt auf 31 Minuten in sechs Stillständen.
2. **Auf Wiederholung prüfen.** Zwei Wochen zurückschauen. Derselbe Störcode taucht 23 Mal auf, mit steigender Tendenz.
3. **Die Anlage ansehen.** Das CMMS abfragen: Der letzte Arbeitsauftrag zur Leimeinheit wurde vor vier Wochen geschlossen, "Düsen gereinigt". Kein offener Auftrag.
4. **Die Signale ansehen.** Den Tag der Leimtemperatur rund um jeden Stillstand aus der Historian-Replik holen. Kurz vor den meisten Stillständen fällt er unter sein Sollwertband.
5. **Die Maßnahme entwerfen.** Im CMMS einen Arbeitsauftrag als Entwurf anlegen: Anlage, Symptom, die 23 Stillstände, das Temperaturmuster mit Link auf ein Diagramm, der vorherige Arbeitsauftrag, eine vorgeschlagene Priorität. Status: Entwurf, wartet auf Planer.
6. **Berichten.** Eine Zeile in die Schichtübergabe schreiben: "Entwurf AA für Leimeinheit Etikettierer L2 angelegt, wiederkehrende Temperatureinbrüche, siehe Link."

Ein Planer prüft den Entwurf am nächsten Morgen, passt die Priorität an und gibt ihn frei. Der Agent hat in zwei Minuten erledigt, wofür ein Ingenieur eine Stunde gebraucht hätte, und zwar in jeder Schicht, nicht nur dann, wenn gerade jemand Zeit hatte.

## Umstellungspläne: entworfen, nicht eingeplant

Dasselbe Muster funktioniert für Umstellungen, den zweiten der sechs großen Verluste. Mit dem Wochenproduktionsplan aus dem ERP und den bekannten Umstellzeiten zwischen Produkten und Formaten kann ein Agent eine Laufreihenfolge entwerfen, die Spülungen und Formatwechsel reduziert. Dunkles Bier nach hellem, nicht helles nach dunklem. Die 330-ml-Läufe zusammenlegen. Er kann auch markieren, wo der Plan eine vermeidbare Umstellung erzwingt.

Den Entwurf übergibt er an den Planer, der Dinge weiß, die der Agent nicht weiß: den Kundenauftrag, der am Donnerstag raus muss, den Bediener, der im Urlaub ist, den Tank, der nicht rechtzeitig frei wird. Der Planer bearbeitet und veröffentlicht. Den Live-Plan fasst der Agent nie an.

## Leitplanke 1: das Purdue-Modell

Die meisten Getränkebetriebe organisieren ihre Netzwerke entlang des Purdue-Modells, und OT-Sicherheitsstandards wie IEC 62443 bauen auf derselben Trennung auf. Ganz unten, auf den Ebenen 0 bis 2, liegen Prozess, SPS, SCADA und HMIs. Ebene 3 enthält den Standortbetrieb: Historian, MES, CMMS, LIMS. Die Ebenen 4 und 5 sind die Unternehmens-IT. Zwischen Betrieb und IT liegt eine demilitarisierte Zone, die DMZ, in der Daten geteilt werden können, ohne das Steuerungsnetz zu öffnen.

Ein Agent gehört auf die IT-Seite. Er liest eine Replik der Historian- und MES-Daten, die in die DMZ veröffentlicht wird. Er öffnet niemals eine Verbindung hinunter in die Ebenen 0 bis 2. Wenn Ihre Architektur das verlangen würde, ist die Architektur noch nicht bereit für einen Agenten.

## Leitplanke 2: keine Schreibzugriffe auf die Prozesssteuerung

Diese verdient eine eigene Zeile. **Nichts, was ein Agent tut, sollte eine SPS, einen SCADA-Wert oder einen Prozesssollwert verändern.** Nicht über ein Tool, nicht über ein Skript, nicht "nur für diesen einen risikoarmen Parameter". Prozesssteuerung ist aus gutem Grund ausgelegt, validiert und verriegelt, und ein Sprachmodell, das in 98 Prozent der Fälle richtig liegt, ist in einem Regelkreis nicht akzeptabel, in dem die anderen 2 Prozent eine Laugenleitung oder ein Druckbehälter sind.

Am einfachsten setzt man das durch, indem man das Tool nie baut. Wenn es auf keinem MCP-Server, den der Agent erreichen kann, eine `set_value`-Funktion gibt und sein Dienstkonto nirgendwo in der Nähe der OT Schreibrechte hat, stellt sich die Frage gar nicht.

## Leitplanken 3 bis 8: Entwürfe, Freigaben, Logs, Evals, Limits, Ausschalter

- **Schreib-Tools legen nur Entwürfe an.** Das CMMS-Tool kann einen Arbeitsauftrag im Status Entwurf anlegen. Es kann keinen freigeben, keinen schließen und keinen freigegebenen ändern.
- **Ein Mensch gibt jeden Entwurf frei.** Mit sichtbaren Belegen, nicht nur mit der Schlussfolgerung. Bearbeitungs- und Ablehnungsquoten verfolgen, denn eine Quote von null heißt meist, dass niemand liest.
- **Ein Audit-Log jedes Tool-Aufrufs.** Welches Tool, welche Eingaben, was zurückkam, was der Agent entworfen hat. Wenn jemand fragt, warum es einen Arbeitsauftrag gibt, steht die Antwort im Log.
- **Replay-Evals vor dem Livegang.** Den Agenten über die Schichten der letzten ein, zwei Monate laufen lassen, mit den Daten so, wie sie damals waren, und seine Entwürfe mit dem vergleichen, was Planer und Ingenieure tatsächlich getan haben. Die gefundenen echten Probleme zählen, das erzeugte Rauschen und die Entwürfe, die falsch gewesen wären. Wiederholen, sobald sich Modell, Prompts oder Tools ändern.
- **Schritt-, Kosten- und Ratenlimits.** Eine Obergrenze für Tool-Aufrufe pro Lauf und Entwürfe pro Schicht, damit ein verwirrter Agent das CMMS nicht fluten kann.
- **Ein Schalter schaltet ihn ab.** Jemand im Betrieb, nicht nur in der IT, kann den Agenten sofort stoppen.

Auf der Autonomieleiter aus Beitrag 3 steht dieser Agent auf **L2**: Er liest frei und entwirft, und ein Mensch gibt frei. Dort sollte er bleiben.

## Wo das bricht

**Der Agent erbt jedes Datenproblem.** Wenn die Stillstandscodes vage sind, ist die Rangfolge vage. Wenn die Anlagenhierarchie im CMMS nicht zum MES passt, kann der Agent einen Stillstand nicht mit einem Arbeitsauftrag verknüpfen. Das zuerst beheben. Es ist billiger als jedes Modell.

**Zu viele Entwürfe zerstören Vertrauen.** Ein Agent, der fünfzehn Entwürfe pro Schicht anlegt, wird innerhalb einer Woche ignoriert. Mit einer Verlustart und einer Linie beginnen und auf Präzision statt Abdeckung optimieren.

**Prompt Injection über Anlagentexte.** Der Agent liest Bedienernotizen und alte Arbeitsaufträge. All das als Daten behandeln, nie als Anweisungen, und jedes Schreib-Tool hinter einer Freigabe halten, damit aus einer seltsamen Notiz keine Aktion werden kann.

**Verzögerung der Replik.** Wenn die DMZ-Replik Stunden hinterherläuft, arbeitet der Agent mit veralteten Daten. Auf jedem Entwurf den Zeitstempel der Daten anzeigen.

**Freigabemüdigkeit.** Aufsicht, die darin besteht, am Schichtende vierzigmal auf Freigeben zu klicken, ist keine Aufsicht. Die Mengen niedrig und die Belege klar halten.

## Das Fazit

Ein guter Agent im Werk ist ein Analyst, kein Bediener. Er liest jede Schicht die Verluste, verbindet Stillstandsprotokoll, Historian und Instandhaltungshistorie und entwirft den Arbeitsauftrag oder Umstellungsplan, zu dem ein beschäftigter Ingenieur nie kommt. Sicher ist er wegen seines Platzes und dessen, was er anfassen kann: die IT-Seite des Purdue-Modells, OT-Daten nur lesend, Schreib-Tools nur für Entwürfe, ein Mensch, der freigibt, jeder Aufruf protokolliert, getestet durch das Nachspielen der Historie. Das Modell wird manchmal falsch liegen. Die Architektur sorgt dafür, dass ein Irrtum einen abgelehnten Entwurf kostet, keinen Sud.

Als Nächstes, und zum Schluss: [die Roadmap und wo sie bricht]({{ '/de/2026/ai-opex-roadmap-where-it-breaks-agi-hype/' | relative_url }}). Zur prädiktiven Seite von Linienstillständen siehe [Stillstände der Abfülllinie vorhersagen und die OEE steigern]({{ '/de/2024/packaging-line-oee-downtime-prediction/' | relative_url }}). Die vollständige Liste steht auf der [Reihenseite]({{ '/series/ai-operational-excellence/' | relative_url }}).

## Häufig gestellte Fragen

**Was kann ein KI-Agent in einem Getränkebetrieb sicher tun?**
Produktions-, Instandhaltungs- und Qualitätsdaten lesen, herausarbeiten, welche Verluste zählen, und Maßnahmen für Menschen entwerfen: Instandhaltungsaufträge, Umstellungspläne, Schichtzusammenfassungen, Nachrichten an einen Planer. Jeder Entwurf trägt seine Belege und wartet auf Freigabe. Einen Weg, auf SPS, SCADA oder Prozesssollwerte zu schreiben, sollte er nicht haben.

**Was ist das Purdue-Modell und warum ist es für KI-Agenten wichtig?**
Das Purdue-Modell ist eine Referenzarchitektur, die die Netzwerke eines Werks in Ebenen trennt, vom physischen Prozess und seinen Steuerungen unten bis zu den Geschäftssystemen oben, mit einer demilitarisierten Zone zwischen Betrieb und Unternehmens-IT. Ein Agent gehört auf die IT-Seite und liest replizierte Daten aus der DMZ. Er sollte niemals Verbindungen hinunter in die Steuerungsebenen öffnen.

**Wie testet man einen KI-Agenten, bevor man ihn auf ein Werk loslässt?**
Mit einem Replay der Historie. Man lässt den Agenten über die Schichten der letzten ein, zwei Monate laufen, mit den Daten so, wie sie damals waren, und vergleicht seine Entwürfe mit dem, was Planer und Ingenieure tatsächlich getan haben. Gemessen wird, wie viele echte Probleme er gefunden hat, wie viele Entwürfe Rauschen waren und wie viele falsch gewesen wären. Das Replay wird wiederholt, sobald sich Modell, Prompts oder Tools ändern.
