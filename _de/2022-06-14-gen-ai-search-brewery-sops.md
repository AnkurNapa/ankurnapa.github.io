---
layout: post
lang: de
title: "Wissenssuche über Brauerei-SOPs mit Gen AI"
image: /assets/og/gen-ai-search-brewery-sops.png
description: "Wie retrieval-gestützte LLMs Brauereipersonal Fragen in einfacher Sprache über SOPs, Chargenprotokolle und Handbücher stellen lassen — mit belegten Antworten — und worauf zu achten ist."
date: 2022-06-14
updated: 2022-06-14
permalink: /de/2022/gen-ai-search-brewery-sops/
tags: [brewing-science, generative-ai, knowledge]
faq:
  - q: "Was ist Retrieval-Augmented Generation, einfach erklärt?"
    a: "Es ist ein Aufbau, bei dem das Sprachmodell zuerst die relevantesten Passagen aus deinen eigenen Dokumenten abruft — SOPs, Chargenprotokolle, Handbücher — und dann ausschließlich anhand dieser Passagen antwortet, mit Verweisen zurück auf die Quelle. Der Abrufschritt verankert das Modell in deiner Realität statt in seinem allgemeinen Training."
  - q: "Kann es trotzdem halluzinieren?"
    a: "Ja, auch wenn die Verankerung das stark reduziert. Wenn die Antwort nicht in deinen Dokumenten steht oder der Abruf die falsche Passage zieht, kann das Modell trotzdem etwas Selbstsicheres und Falsches produzieren. Deshalb muss jede Antwort ihre Quelle nennen, damit eine Person sie vor dem Handeln überprüfen kann."
  - q: "Welche Governance braucht das?"
    a: "Vor allem Versionskontrolle und Zugriffsberechtigungen. Du brauchst eine maßgebliche Version jedes Dokuments, damit das Modell keine überholte SOP zitiert, und du brauchst Berechtigungsregeln, damit das Personal nur Antworten aus Dokumenten erhält, für die es freigegeben ist. Ohne das wird das Werkzeug zu einem schnellen Weg, veraltete oder eingeschränkte Informationen zu verbreiten."
---

**Kurze Antwort: Ein retrieval-gestütztes LLM lässt das Personal Fragen in einfacher Sprache über eure SOPs, Chargenprotokolle und Handbücher stellen und belegte Antworten erhalten — der stärkste echte Gen-AI-Anwendungsfall, den eine Brauerei hat.** Das Wissen existiert bereits; es ist nur über PDFs, geteilte Laufwerke und die Erinnerungen einiger weniger Menschen verstreut. Das ist der Anwendungsfall, der das behebt.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo das im Bierproduktionsfluss sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSFLUSS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Wissenssuche über Brauerei-SOPs mit Gen AI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Korn</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllung</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo das im Bierproduktionsfluss sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Das Problem des verstreuten Wissens
Frag eine neue Kellerhilfe „Was ist die CIP-Spezifikation für FV3?" und die ehrliche Antwort ist oft eine Suche: Die richtige SOP liegt in einem Ordner, eine Ausnahmenotiz steht in einem Chargenprotokoll, und das maßgebliche Wort liegt bei demjenigen, der das Verfahren geschrieben hat. Multipliziere das über Hunderte von Dokumenten und ein Dutzend Verfahren, und du hast einen echten Bremsklotz in jeder Schicht. Wissen, das existiert, aber nicht schnell auffindbar ist, könnte genauso gut nicht existieren.

Retrieval-Augmented Generation geht das direkt an. Das Personal stellt eine Frage in einfacher Sprache; das System ruft die relevantesten Passagen aus deinem eigenen Dokumentenbestand ab; das LLM verfasst aus diesen Passagen eine Antwort und zitiert sie. Das Zitat ist der entscheidende Teil — es verwandelt das Modell von einem Orakel, dem du vertrauen musst, in einen Assistenten, den du überprüfen kannst. „Die CIP-Spezifikation für FV3 ist X, gemäß SOP-CIP-04, Abschnitt 3" ist etwas, das eine Person in Sekunden überprüfen kann.

## Erst messen: in deinen echten Dokumenten verankern
Anders als bei den übrigen Anwendungen in diesem Track sind die „Daten" hier dein schriftliches Wissen, und dieselbe Disziplin gilt: Bring das Quellmaterial in Ordnung, bevor du irgendetwas einschaltest. Das bedeutet zu wissen, welche Dokumente maßgeblich sind, überholte Versionen zu entfernen oder klar zu archivieren und den Zugriff so zu strukturieren, dass der Abruf sauberes Material zur Verfügung hat. Das umfassendere Argument, zuerst die Datengrundlage zu ordnen, gilt hier genauso — siehe [Aufbau einer Brauerei-Datengrundlage für KI]({{ '/de/2024/building-brewery-data-foundation-ai/' | relative_url }}).

Ein Abrufsystem ist nur so vertrauenswürdig wie das Korpus dahinter. Richte es auf einen Ordner mit duplizierten, halb überarbeiteten PDFs und es wird treu das falsche zitieren. Die unglamouröse Vorarbeit — Deduplizieren, Versionieren, Aufräumen — ist das, was den cleveren Teil zum Funktionieren bringt.

## Wo es bricht
Sieh drei Risiken klar ins Auge. Erstens Halluzination. Die Verankerung reduziert sie stark, aber nie auf null; wenn die Antwort nicht in deinen Dokumenten steht oder der Abruf die falsche Passage greift, kann das Modell trotzdem selbstsicher klingen und falsch liegen. Zitate sind die Abhilfe, weshalb einer Antwort ohne überprüfbare Quelle nicht zu trauen ist.

Zweitens Versionskontrolle. Wenn zwei Versionen einer SOP existieren, kann das Modell die veraltete zitieren, und eine schnelle, flüssige Antwort aus einem überholten Verfahren ist gefährlicher als gar keine Antwort. Drittens Zugriffsberechtigungen. Chargenprotokolle und manche Verfahren sind sensibel; das System muss respektieren, wer was sehen darf, sonst wird es zu einem reibungslosen Leck. Keines davon ist ein Grund, es nicht zu tun — es sind Gründe, es ordentlich zu steuern.

## Ein praktischer Gen-AI-Blickwinkel
Dieser Beitrag *ist* der Gen-AI-Blickwinkel, daher lohnt es sich, die konkrete Einordnung klar zu sagen: Setze es als internen, gesteuerten Assistenten ein, nicht als öffentlichen Chatbot. Beschränke ihn auf geprüfte Dokumente, verlange Zitate bei jeder Antwort, setze Zugriffsregeln durch und halte eine einzige maßgebliche Version jeder SOP. So gemacht, dauert eine Frage, die früher zehn Minuten Ordnerwühlerei brauchte, zehn Sekunden, und die Antwort verweist direkt auf das Verfahren, aus dem sie stammt.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Freitext rein, ein strukturiertes Signal raus — Stimmung und Themen aus den Wörtern bewertet."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">TEXT → SIGNAL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Wissenssuche über Brauerei-SOPs mit Gen AI</text><rect x="80" y="90" width="200" height="150" rx="6" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><rect x="100" y="118" width="160" height="9" rx="3" fill="#f7ece0"/><rect x="100" y="140" width="120" height="9" rx="3" fill="#f7ece0"/><rect x="100" y="162" width="160" height="9" rx="3" fill="#f7ece0"/><rect x="100" y="184" width="120" height="9" rx="3" fill="#f7ece0"/><rect x="100" y="206" width="160" height="9" rx="3" fill="#f7ece0"/><text x="180" y="262" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Bewertungen / Notizen</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="300" y1="165" x2="350" y2="165"/><polygon points="350,158 362,165 350,172" stroke="none"/></g><rect x="385" y="150" width="200" height="26" rx="4" fill="#5b7a1f"/><rect x="525" y="150" width="60" height="26" rx="4" fill="#7a1f3d"/><text x="485" y="200" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Stimmung / Themen bewertet</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Freitext rein, ein strukturiertes Signal raus — Stimmung und Themen aus den Wörtern bewertet.</figcaption>
</figure>

## Das Fazit
Die Wissenssuche über SOPs und Chargenprotokolle ist der überzeugendste Gen-AI-Einsatz in einer Brauerei, weil der Nutzen unmittelbar ist und das Wissen bereits existiert — es muss nur gefunden werden. Der Eintrittspreis ist Governance: maßgebliche Quellen, Versionskontrolle, Zugriffsberechtigungen und verpflichtende Zitate, um Halluzination in Schach zu halten. Räum zuerst das Korpus auf, verankere jede Antwort, und du verwandelst verstreute Dokumente in etwas, das das Personal tatsächlich abfragen kann.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).*

## Häufig gestellte Fragen

**Was ist Retrieval-Augmented Generation, einfach erklärt?**
Es ist ein Aufbau, bei dem das Sprachmodell zuerst die relevantesten Passagen aus deinen eigenen Dokumenten abruft — SOPs, Chargenprotokolle, Handbücher — und dann ausschließlich anhand dieser Passagen antwortet, mit Verweisen zurück auf die Quelle. Der Abrufschritt verankert das Modell in deiner Realität statt in seinem allgemeinen Training.

**Kann es trotzdem halluzinieren?**
Ja, auch wenn die Verankerung das stark reduziert. Wenn die Antwort nicht in deinen Dokumenten steht oder der Abruf die falsche Passage zieht, kann das Modell trotzdem etwas Selbstsicheres und Falsches produzieren. Deshalb muss jede Antwort ihre Quelle nennen, damit eine Person sie vor dem Handeln überprüfen kann.

**Welche Governance braucht das?**
Vor allem Versionskontrolle und Zugriffsberechtigungen. Du brauchst eine maßgebliche Version jedes Dokuments, damit das Modell keine überholte SOP zitiert, und du brauchst Berechtigungsregeln, damit das Personal nur Antworten aus Dokumenten erhält, für die es freigegeben ist. Ohne das wird das Werkzeug zu einem schnellen Weg, veraltete oder eingeschränkte Informationen zu verbreiten.
