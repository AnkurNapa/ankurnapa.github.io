---
layout: post
lang: de
title: "Bier-Verkostungspanels digitalisieren: Power Apps, Power BI und KI"
image: /assets/og/digitising-beer-tasting-panels-ai-power-bi.png
description: "Wie Brauereien Verkostungspanels mit einer Power-Apps-Erfassungs-App, Power-BI-Analytik und KI-gestützter Fehler- und Drifterkennung digitalisieren können — ohne den Gaumen zu verlieren."
date: 2024-02-15
updated: 2024-02-15
permalink: /de/2024/digitising-beer-tasting-panels-ai-power-bi/
tags: [brewing-science, tasting, power-apps, power-bi]
faq:
  - q: "Brauche ich den vollen Microsoft-Stack, um mein Verkostungspanel zu digitalisieren?"
    a: "Nein. Eine gut strukturierte Tabelle schlägt unordentliche Software, und viele kleine Brauereien fahren gut damit, dabei zu bleiben. Wechsle zu Power Apps und Power BI, wenn Papier oder Tabellen nicht mehr skalieren — mehrere Verkoster, mehrere Sitzungen pro Woche und ein echter Bedarf, Ergebnisse mit Chargen zu verknüpfen."
  - q: "Kann KI das Verkostungspanel ersetzen?"
    a: "Nein. KI und Dashboards schmecken nicht. Das kalibrierte menschliche Panel bleibt das Instrument; der Stack erfasst, strukturiert, analysiert und kommuniziert, was das Panel produziert. KI markiert Drift und Fehler und entwirft Notizen — sie trifft nicht die Entscheidung."
  - q: "Was sollte ich richtig machen, bevor ich Dashboards hinzufüge?"
    a: "Die Grundlagen der Sensorikwissenschaft: eine konsistente Attributliste und Skalen, ein gescreentes und kalibriertes Panel und ein sauberes Datenmodell, das jede Sitzung an eine Charge oder Partie schlüsselt. Dashboards, die auf inkonsistenten Daten bauen, visualisieren das Chaos nur schneller."
---

**Kurze Antwort: Ersetze das Klemmbrett durch ein Tablet, schlüssele jede Bewertung an eine Charge und lass die Analytik Drift und Fehler ans Licht holen — aber behalte das kalibrierte Panel als Instrument.** Die meisten Brauereien betreiben bereits ein Verkostungspanel. Weit weniger können eine einfache Frage beantworten: Ist die Bitterkeit über die Sude dieses Quartals hinweg über die Spezifikation gedriftet, und welcher Verkoster hat es zuerst gemeldet?

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Bier-Verkostungspanels digitalisieren: Power Apps, Power BI und KI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Gärung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Abfüllung</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende.</figcaption>
</figure>

## Warum Papier und Tabellen dich still teuer zu stehen kommen
Ein Papier-Bewertungsbogen ist schnell zu starten und langsam, um daraus zu lernen. Bewertungen werden abgeschrieben (oder nicht), Sitzungen liegen in getrennten Dateien, und die Verbindung zwischen einem Verkostungsergebnis und der tatsächlichen Charge im Sudhaus ist eine Erinnerung statt einer Aufzeichnung. Wenn eine Kundenbeschwerde eintrifft, kannst du nicht einfach alle Panel-Ergebnisse für diese Partie herausziehen.

Die Lösung ist keine forschungstaugliche Sensorik-Suite. Es ist strukturierte Erfassung. Eine **Power Apps**-Canvas-App auf **Dataverse** lässt Panellisten Proben am Tisch auf einem Handy oder Tablet bewerten — die Probe auswählen, Attribute auf der Hausskala bewerten, Fehler aus einer kontrollierten Liste notieren. Sie funktioniert offline in einem kalten Keller und synchronisiert später, sodass du nicht ans WLAN gekettet bist. Der Punkt ist, dass die Daten in dem Moment sauber und strukturiert sind, in dem sie eingegeben werden, nicht eine Woche später.

## Verankere jede Sitzung an der Charge im ERP
Verkostungsdaten sind nur im Kontext nützlich. Der Kontext lebt in deinem **ERP** — Dynamics 365 Business Central oder ähnlich — das bereits deine Produkte, Rezepte, Chargen und Partien sowie Lieferanten enthält. Wenn die Erfassungs-App den Chargen- oder Partiendatensatz referenziert, wird jede Sitzung Teil der Spur vom Korn ins Glas.

Diese Verbindung verwandelt die Verkostung von einem Ritual in eine Freigabekontrolle. Ein Panel-Ergebnis, das an eine Partie gebunden ist, stützt die Entscheidung über Freigabe, Sperre oder Ablehnung und gibt dir Rückverfolgbarkeit, wenn etwas schiefgeht. Du kannst die Daten fragen, welche Malzlieferung, welche Hefegabe oder welcher Gärtank mit einer Fehlnote korreliert — weil die Schlüssel alle da sind.

## Verwandle Bewertungen in Trends in Power BI
Sobald Erfassung und Stammdaten geregelt sind, leistet **Power BI** die sichtbare Arbeit. Nützliche Ansichten für ein Brauerei-Panel umfassen:

- **Attributtrends** — wie Bitterkeit, Körper, Estercharakter oder DMS über Sude desselben Biers im Zeitverlauf verfolgen.
- **Regelkarten gegen Spezifikation** — jedes Attribut gegen deinen Hausbereich aufgetragen, sodass Drift offensichtlich ist, bevor sie zur Beschwerde wird.
- **Panellisten-Übereinstimmung und -Varianz** — wo das Panel übereinstimmt, wo es sich spaltet und welcher Verkoster konsistent hoch oder niedrig liegt.

Weil die Daten an Partien aus dem ERP geschlüsselt sind, führt jedes Diagramm zu einer bestimmten Charge zurück. Der Copilot in Power BI lässt dich in einfacher Sprache fragen — „zeig mir Chargen, bei denen die Bitterkeit dieses Quartal über die Spezifikation gedriftet ist" — und ein Diagramm zurückbekommen, wobei du immer prüfen solltest, was er zurückgibt.

## Wo KI hilft und wo sie nicht kann
Hier verdient sich **maschinelles Lernen** seinen Platz — eng begrenzt. Auf genügend bewerteten Sitzungen trainiert, können Modelle Panellisten-**Drift** markieren (ein Verkoster, dessen Bewertungen über Monate abdriften), ungewöhnliche Ergebnisse screenen und helfen, wahrscheinliche **Fehler** zu markieren: Diacetyl, Acetaldehyd, DMS oder Alterungsmarker wie T2N. Die Kalibrierung gegen Geschmacksstandards — gespiktes Diacetyl um 0,10 mg/L, Acetaldehyd nahe 10 mg/L — hält das Panel ehrlich, und das Modell lernt aus dieser kalibrierten Basislinie. Weiter draußen kannst du Sensorik-Attribute aus Instrumentendaten wie NIR vorhersagen und das Panel nutzen, um die Vorhersage zu validieren, nicht zu ersetzen.

Hier ist die ehrliche Grenze. **KI und Dashboards schmecken nicht.** Sie erkennen Muster in Zahlen, die das Panel produziert hat. Wenn das Panel unkalibriert oder die Attributliste inkonsistent ist, lernt das Modell Rauschen. Der kalibrierte menschliche Gaumen ist das Instrument; alles im Stack erfasst, strukturiert, analysiert und kommuniziert seine Ausgabe. Und für eine kleine Brauerei mit einem Bier und einem wöchentlichen Panel mag eine ordentliche Tabelle die ganze Strenge sein, die du brauchst — der Lizenz- und Governance-Aufwand der Power Platform zahlt sich erst im großen Maßstab aus.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Das Modell sortiert jede Probe anhand ihrer gemessenen Merkmale in eine Klasse."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">KLASSIFIZIERUNG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Bier-Verkostungspanels digitalisieren: Power Apps, Power BI und KI</text><rect x="120" y="120" width="150" height="120" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="195" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#00695c">Klasse A</text><circle cx="145" cy="145" r="6" fill="#00695c"/><circle cx="177" cy="145" r="6" fill="#00695c"/><circle cx="209" cy="145" r="6" fill="#00695c"/><rect x="330" y="120" width="150" height="120" rx="8" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="1.5"/><text x="405" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#2e9e7c">Klasse B</text><circle cx="355" cy="145" r="6" fill="#2e9e7c"/><circle cx="387" cy="145" r="6" fill="#2e9e7c"/><circle cx="419" cy="145" r="6" fill="#2e9e7c"/><circle cx="451" cy="145" r="6" fill="#2e9e7c"/><rect x="540" y="120" width="150" height="120" rx="8" fill="#f0f6f5" stroke="#06483f" stroke-width="1.5"/><text x="615" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Klasse C</text><circle cx="565" cy="145" r="6" fill="#06483f"/><circle cx="597" cy="145" r="6" fill="#06483f"/><circle cx="629" cy="145" r="6" fill="#06483f"/><circle cx="661" cy="145" r="6" fill="#06483f"/><circle cx="565" cy="175" r="6" fill="#06483f"/><text x="360" y="92" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#4a6b64">neue Probe → in die am besten passende Klasse sortiert</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Das Modell sortiert jede Probe anhand ihrer gemessenen Merkmale in eine Klasse.</figcaption>
</figure>

## Das Fazit
Ein Bier-Verkostungspanel zu digitalisieren ist überwiegend eine Übung in Disziplin: konsistente Attribute, ein kalibriertes Panel und ein sauberes Datenmodell, das Bewertungen an Partien bindet. Power Apps erfasst es, das ERP verankert es, Power BI deckt die Trends auf, und KI markiert, was einen zweiten Schnüffler verdient. **Generative KI** kann dann aus den strukturierten Bewertungen eine konsistente Verkostungsnotiz im Hausstil oder eine QC-Freigabezusammenfassung entwerfen — von einem Menschen geprüft, bevor sie ausgeliefert wird. Nichts davon schmeckt für dich; das ist immer noch Aufgabe des Panels.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [KI und Verkoster-Kalibrierung]({{ '/de/2024/ai-sensory-panel-taster-calibration/' | relative_url }}) und [Whiskey-Verkostung mit Power Apps und Power BI]({{ '/de/2024/whiskey-tasting-ai-power-apps-power-bi/' | relative_url }}).

## Häufig gestellte Fragen

**Brauche ich den vollen Microsoft-Stack, um mein Verkostungspanel zu digitalisieren?**
Nein. Eine gut strukturierte Tabelle schlägt unordentliche Software, und viele kleine Brauereien fahren gut damit, dabei zu bleiben. Wechsle zu Power Apps und Power BI, wenn Papier oder Tabellen nicht mehr skalieren — mehrere Verkoster, mehrere Sitzungen pro Woche und ein echter Bedarf, Ergebnisse mit Chargen zu verknüpfen.

**Kann KI das Verkostungspanel ersetzen?**
Nein. KI und Dashboards schmecken nicht. Das kalibrierte menschliche Panel bleibt das Instrument; der Stack erfasst, strukturiert, analysiert und kommuniziert, was das Panel produziert. KI markiert Drift und Fehler und entwirft Notizen — sie trifft nicht die Entscheidung.

**Was sollte ich richtig machen, bevor ich Dashboards hinzufüge?**
Die Grundlagen der Sensorikwissenschaft: eine konsistente Attributliste und Skalen, ein gescreentes und kalibriertes Panel und ein sauberes Datenmodell, das jede Sitzung an eine Charge oder Partie schlüsselt. Dashboards, die auf inkonsistenten Daten bauen, visualisieren das Chaos nur schneller.
