---
layout: post
lang: de
title: "Whiskey-Verkostung, erfasst und analysiert: Power Apps, Power BI und KI"
image: /assets/og/whiskey-tasting-ai-power-apps-power-bi.png
description: "Erfasse Fassmuster- und Vatting-Bewertungen in Power Apps, verknüpft mit dem ERP, verfolge die Reifung in Power BI und nutze KI, um Fässer zu clustern und Fehlaromen zu markieren — die Nase entscheidet weiterhin."
date: 2024-08-15
updated: 2024-08-15
permalink: /de/2024/whiskey-tasting-ai-power-apps-power-bi/
tags: [distilling-maturation, tasting, power-apps, power-bi]
faq:
  - q: "Wie verfolge ich das Aroma eines Fasses über Jahre der Reifung?"
    a: "Erfasse jede Fassmuster-Verkostung in einer Power-Apps-App, die mit dem Fassdatensatz im ERP verknüpft ist, und stelle dann die Attributhistorie in Power BI dar. Mit der Zeit baust du eine Aromatrajektorie pro Fass auf — unbezahlbar für die Entscheidung, wann zu vatten, zu verlängern oder Spirituose zu bewegen ist."
  - q: "Kann KI die Fässer für ein Vatting auswählen?"
    a: "Sie kann Fässer nach Aromaprofil clustern und Ausreißer oder Fehlaromen markieren, was das Feld schnell eingrenzt. Sie kann den Verschnitt nicht entscheiden. Die Nase des Master Blenders bleibt das Instrument; KI organisiert die Kandidaten und die Daten dahinter."
  - q: "Was ist der Haken bei der Nutzung von KI in langer Reifung?"
    a: "Das Feedback ist langsam. Ein Fass reift über Jahre, daher lernen Modelle aus spärlichen, nachhinkenden Daten, und jede Vorhersage trägt echte Unsicherheit. Behandle KI-Ausgaben als Anstoß, die richtigen Fässer zu nosen, niemals als Ersatz für das Muster."
---

**Kurze Antwort: Erfasse jedes Fassmuster als strukturierten, verschlüsselten Datensatz, und du baust eine Aromatrajektorie pro Fass auf, die Vatting-Entscheidungen belegbasiert macht — aber die Nase des Master Blenders wählt weiterhin den Verschnitt.** Die Reifung ist die langsamste Rückkopplungsschleife in der Getränkeproduktion. Die Fässer, die nicht konsistent gemessen werden, sind die, die dich beim Vatting überraschen.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Whiskey-Produktionsablauf sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Whiskey-Verkostung, erfasst und analysiert: Power Apps, Power BI und KI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Destillieren</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Reifen</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllen</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Whiskey-Produktionsablauf sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Das Problem: Jahre an Mustern, kein Gedächtnis
Eine Destillerie nost Fässer über Jahre, bevor sie gevattet werden. Wenn jedes Muster auf einem Papierblatt oder in einer einmaligen Tabelle lebt, geht die Historie faktisch verloren — du erinnerst dich an die herausragenden Fässer und vergisst die Trajektorie des Rests. Wenn es Zeit ist, ein Vatting zu bauen, arbeitest du aus jüngsten Eindrücken statt aus der vollständigen Geschichte des Fasses.

Das Ziel ist ein sauberer, kontinuierlicher Datensatz pro Fass. Kein Forschungsinstrument — nur konsistente Erfassung, dem Fass zugeordnet, jedes Mal, wenn jemand ein Muster zieht.

## Erfassung im Lager, dem Fass zugeordnet
Eine **Power Apps**-App auf **Dataverse** lässt das Team Fassmuster und Vatting-Versuche auf einem Tablet im Lager bewerten — wähle das Fass, bewerte die Reifeattribute auf der Hausskala (Eiche, Würze, Frucht, Schwefel, Fehlaromen) und protokolliere es. Es funktioniert offline zwischen den Regalen und synchronisiert später.

Entscheidend ist, dass jede Bewertung auf den Fass- und Chargendatensatz im **ERP** (Dynamics 365 Business Central oder ähnlich) verweist, neben Befülldatum, Holzart, Vorbelegung und Spirituose. Diese Verknüpfung gibt dir Rückverfolgbarkeit vom Korn ins Glas und bindet die sensorische Historie an den physischen Vermögenswert. Ein Verkostungsergebnis ist keine Notiz mehr; es ist Teil des Fassdatensatzes und stützt die Entscheidung, zu vatten, zu halten oder zu verlängern.

## Die Reifung in Power BI in Bewegung sehen
In **Power BI** wird die langsame Geschichte sichtbar:

- **Aroma im Zeitverlauf pro Fass** — Attributtrajektorien über Jahre der Musterung, sodass du ein Fass sich entwickeln oder stagnieren sehen kannst.
- **Fassübergreifender Vergleich** — kontrastiere Fässer derselben Befüllung oder Holzart und decke die konstanten Performer und die Ausreißer auf.
- **Fehlaroma-Verfolgung** — überwache markierte Fehler über das Lager hinweg, bevor sie sich durch ein Vatting ausbreiten.

Weil jeder Punkt einem Fass im ERP zugeordnet ist, führen die Diagramme zurück zum physischen Vermögenswert. Der Copilot in Power BI beantwortet Fragen in einfacher Sprache — „welche First-Fill-Fässer haben dieses Jahr am schnellsten Würze gewonnen?" — und gibt ein Diagramm zur Überprüfung zurück.

## KI: die Fässer clustern, die Fehlaromen markieren
**Maschinelles Lernen** passt zu diesen Daten gut, sobald du genug davon hast. Clustering gruppiert Fässer nach Aromaprofil, was ein echter Vorsprung ist, wenn man ein Vatting aus Hunderten von Kandidaten zusammenstellt. Modelle können Fehlaromen und Ausreißer markieren — Schwefel, übermäßiges Holz, Oxidation — sodass das Team die Fässer nost, die zählen. Wo du Instrumentendaten hast, können Modelle helfen, Attribute vorherzusagen, wobei die Musterung zur Validierung dient.

Die ehrlichen Grenzen sind hier schärfer als bei Bier oder Wein. **KI und Dashboards schmecken nicht.** Clustering schlägt Kandidaten vor; die Nase des Master Blenders komponiert das Vatting und beurteilt Balance und Hauscharakter. Und die langsame Rückkopplungsschleife der Reifung bedeutet, dass Modelle auf spärlichen, nachhinkenden Daten trainieren — eine Vorhersage über ein Fass drei Jahre in der Zukunft trägt echte Unsicherheit. Nutze KI, um zu priorisieren, welche Fässer zu nosen sind, niemals, um das Muster zu ersetzen. Für eine kleine Destillerie mit ein paar hundert Fässern ist eine disziplinierte, nach Fassnummern verschlüsselte Tabelle vielleicht alles, was du brauchst; die Lizenzierung und Governance der Power Platform pro Nutzer zahlen sich erst im Maßstab aus.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Was die Reifung treibt und was es nachgelagert verändert."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WAS ES TREIBT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Whiskey-Verkostung, erfasst und analysiert: Power Apps, Power BI und KI</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Reifung</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Qualität</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Kosten / Risiko</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Was die Reifung treibt und was es nachgelagert verändert.</figcaption>
</figure>

## Das Fazit
Die Whiskey-Verkostung wird zum Vermögenswert, wenn jedes Fassmuster ein strukturierter, verschlüsselter Datensatz ist statt einer verblassenden Erinnerung. Power Apps erfasst es im Lager, das ERP verankert es am Fass, Power BI offenbart die Reifetrajektorie, und KI clustert Profile und markiert Fehlaromen. **Generative KI** kann dann konsistente Verkostungsnotizen im Hausstil und eine erste Verschnittbegründung aus den Bewertungen entwerfen — vom Team geprüft. Die Nase entscheidet weiterhin; der Stack merkt sich alles andere.

*Teil des Tracks [Destillation & Reifung]({{ '/de/tracks/distilling-maturation/' | relative_url }}).* Verwandt: [KI-Verkostungsnotizen für Bier, Wein und Whiskey]({{ '/de/2026/ai-tasting-notes-beer-wine-whiskey/' | relative_url }}) und [ein digitales Verkostungsprogramm aufbauen]({{ '/de/2024/digital-tasting-program-power-platform-erp-genai/' | relative_url }}).

## Häufig gestellte Fragen

**Wie verfolge ich das Aroma eines Fasses über Jahre der Reifung?**
Erfasse jede Fassmuster-Verkostung in einer Power-Apps-App, die mit dem Fassdatensatz im ERP verknüpft ist, und stelle dann die Attributhistorie in Power BI dar. Mit der Zeit baust du eine Aromatrajektorie pro Fass auf — unbezahlbar für die Entscheidung, wann zu vatten, zu verlängern oder Spirituose zu bewegen ist.

**Kann KI die Fässer für ein Vatting auswählen?**
Sie kann Fässer nach Aromaprofil clustern und Ausreißer oder Fehlaromen markieren, was das Feld schnell eingrenzt. Sie kann den Verschnitt nicht entscheiden. Die Nase des Master Blenders bleibt das Instrument; KI organisiert die Kandidaten und die Daten dahinter.

**Was ist der Haken bei der Nutzung von KI in langer Reifung?**
Das Feedback ist langsam. Ein Fass reift über Jahre, daher lernen Modelle aus spärlichen, nachhinkenden Daten, und jede Vorhersage trägt echte Unsicherheit. Behandle KI-Ausgaben als Anstoß, die richtigen Fässer zu nosen, niemals als Ersatz für das Muster.
