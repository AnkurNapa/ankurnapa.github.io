---
layout: post
lang: de
title: "Ein digitales Verkostungsprogramm aufbauen: Power Platform, ERP und Gen AI"
image: /assets/og/digital-tasting-program-power-platform-erp-genai.png
description: "Eine praktische Reihenfolge für Bier, Wein und Spirituosen: zuerst das Datenmodell, Erfassung in Power Apps, Verankerung im ERP, Analyse in Power BI, dann KI und generative KI obendrauf."
date: 2024-10-15
updated: 2024-10-15
permalink: /de/2024/digital-tasting-program-power-platform-erp-genai/
tags: [brewing-science, tasting, power-platform, generative-ai]
faq:
  - q: "Was ist die richtige Reihenfolge, um ein digitales Verkostungsprogramm aufzubauen?"
    a: "Datenmodell, dann Erfassung, dann Dashboards, dann KI, dann generative KI. Definiere zuerst Attribute, Skalen und Sud-/Partieschlüssel; erfasse in Power Apps auf Dataverse; verankere Stammdaten im ERP; analysiere in Power BI; füge erst dann KI und Gen AI auf saubere, strukturierte Daten hinzu."
  - q: "Wann sollte ich das nicht aufbauen?"
    a: "Wenn du noch kein kalibriertes Panel und kein sauberes Datenmodell hast — Software behebt das nicht — oder wenn du klein genug bist, dass eine ordentliche Tabelle die Arbeit erledigt. Power-Platform-Lizenzierung und Governance verursachen echte Kosten; kaufe den Stack, wenn die Skalierung es rechtfertigt."
  - q: "Was macht generative KI hier eigentlich?"
    a: "Sie entwirft Verkostungsnotizen im Hausstil aus den Bewertungen, fasst eine Sitzung zusammen, schreibt eine erste Fassung einer QC-Freigabenotiz und beantwortet klar formulierte Fragen über Copilot. Alles wird von Menschen geprüft. Sie kommuniziert, was das Panel produziert hat — sie verkostet nicht."
---

**Kurze Antwort: Baue es in der richtigen Reihenfolge — Datenmodell, Erfassung, Dashboards, KI, generative KI — und kaufe den Stack nicht, bevor du ein kalibriertes Panel und ein sauberes Datenmodell dahinter hast.** Ein digitales Verkostungsprogramm scheitert auf dieselbe Weise, wie die meisten Datenprojekte scheitern: Leute beginnen mit dem Dashboard und entdecken, dass die Daten darunter es nicht tragen. Drehe die Reihenfolge um.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsfluss sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSFLUSS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Ein digitales Verkostungsprogramm aufbauen: Power Platform, ERP und Gen AI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllung</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Bierproduktionsfluss sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Schritt eins: Das Datenmodell entscheidet alles
Vor jedem Werkzeug klärst du die **Data-Science**-Grundlagen. Einige dich auf die Attributliste und Skalen für jeden Produkttyp. Definiere deine sensorischen Methoden — Unterschiedstests (Dreieck, Duo-Trio, paarweise), beschreibendes Profilieren, Sortentreue — und wie Ergebnisse statistisch behandelt werden, um Panel-Übereinstimmung und Signifikanz zu prüfen. Am wichtigsten: Lege die Schlüssel fest: Jede Sitzung muss auf einen Sud, eine Partie, einen Jahrgang oder ein Fass verweisen.

Diese Schlüssel liegen in deinem **ERP** (Dynamics 365 Business Central, Finance & Operations oder ähnlich), das bereits Produkte, Sude und Partien, Rezepte, Lieferanten und Bestand hält. Verkostungsergebnisse mit dem Partie-Datensatz zu verknüpfen, ist das, was Rückverfolgbarkeit liefert und die Freigabeentscheidung Bestehen/Halten/Ablehnen unterstützt. Überspringe diesen Schritt und alles stromabwärts wackelt.

## Schritt zwei und drei: Erfassen, dann visualisieren
Mit fixiertem Modell kommt als Nächstes die **Erfassung**. Eine **Power Apps**-Canvas- oder modellgesteuerte App auf **Dataverse** lässt Panelteilnehmer am Probiertisch auf einem Handy oder Tablet bewerten — über Bier, Wein und Spirituosen hinweg ist das Muster dasselbe: Wähle die Probe, bewerte die Attribute, markiere Fehler aus einer kontrollierten Liste, speichere offline, synchronisiere später. Strukturierte Daten, einmal eingegeben, korrekt verknüpft.

Dann **Dashboards**. **Power BI** macht aus den Bewertungen die Ansichten, die Entscheidungen treiben: Attributtrends, Kontrollkarten gegen Spezifikation, Panel-Übereinstimmung und -Varianz, Partie- und Verschnittvergleiche, Fehlerverfolgung — alle aufgeschlüsselt bis zum Sud oder zur Partie aus dem ERP. Widerstehe dem Hinzufügen von KI, bis dieser Ebene vertraut wird. Wenn die Dashboards stimmen, ist die Analytik solide; wenn sie falsch sind, rettet dich kein Modell.

## Schritt vier und fünf: KI, dann generative KI
Erst jetzt schichtest du **Machine Learning** auf. Nutze es, um Panelteilnehmer gegen Aromastandards zu kalibrieren und zu prüfen (gespiktes Diacetyl um 0,10 mg/L, Acetaldehyd nahe 10 mg/L, DMS, T2N für Alterung) und Drift über die Zeit zu erkennen. Nutze es, um wahrscheinliche Fehler zu markieren — Brett, flüchtige Säure, TCA, Diacetyl, Oxidation — und, wo du NIR- oder FTIR-Daten hast, um sensorische Eigenschaften mit Chemometrie vorherzusagen, sodass das Panel zuerst die Prioritäten verkostet.

Dann **generative KI** ganz obenauf. Aus den strukturierten Bewertungen kann sie eine konsistente Verkostungsnotiz im Hausstil entwerfen, eine Sitzung für das Team zusammenfassen, eine erste Fassung einer QC-Freigabenotiz schreiben und klar formulierte Fragen über Copilot in Power BI oder einen Copilot-Studio-Assistenten beantworten — "zeige mir Sude, bei denen die Bittere in diesem Quartal über Spezifikation abdriftete." Jede Ausgabe wird von Menschen geprüft, bevor sie zählt.

## Wo das bricht
Das häufigste Versagen ist die Reihenfolge: die Power Platform zu kaufen, bevor das Panel kalibriert oder das Datenmodell sauber ist. Software verstärkt, was immer du sie fütterst, also verstärkt sie ein chaotisches Panel schneller zu chaotischen Dashboards. Das zweite Versagen ist Kostenblindheit — Lizenzierung pro Nutzer und pro App plus der Governance-Aufwand, den ein sauberes Dataverse-Modell verlangt. Für einen kleinen Erzeuger mit ein oder zwei Produkten ist eine ordentliche Tabelle, die mit Partienummern verknüpft ist, oft die richtige Antwort, und der Stack ist übertrieben.

Und die Grenze, die sich nie bewegt: **KI und Dashboards verkosten nicht.** Das kalibrierte menschliche Panel bleibt das Instrument. Alles in diesem Programm — Erfassung, ERP-Schlüssel, Power BI, ML, Gen AI — existiert, um zu erfassen, zu strukturieren, zu analysieren und zu kommunizieren, was das Panel produziert. Der Tag, an dem du ein Modell statt des Panels den Freigaberuf treffen lässt, ist der Tag, an dem das Programm schiefgegangen ist.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Was den Prozess treibt und was es stromabwärts verändert."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WAS ES TREIBT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Ein digitales Verkostungsprogramm aufbauen: Power Platform, ERP und Gen AI</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Der Prozess</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Qualität</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Kosten / Risiko</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Was den Prozess treibt und was es stromabwärts verändert.</figcaption>
</figure>

## Das Fazit
Ein digitales Verkostungsprogramm ist eine Reihenfolge, kein Kauf: Datenmodell, Erfassung, Dashboards, KI, generative KI — jeder Schritt verdient den nächsten. Verankere es im ERP, erfasse in Power Apps, analysiere in Power BI und füge KI und Gen AI nur auf sauberen, kalibrierten Daten hinzu. Baue es in dieser Reihenfolge und der Stack zahlt sich aus; überspringe einen Schritt und er tut es nicht. Das Panel verkostet weiterhin.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [Ein Brauerei-Datenfundament für KI aufbauen]({{ '/de/2024/building-brewery-data-foundation-ai/' | relative_url }}) und [KI und NIR-Spektroskopie für schnelle QC]({{ '/de/2024/ai-nir-spectroscopy-rapid-qc/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist die richtige Reihenfolge, um ein digitales Verkostungsprogramm aufzubauen?**
Datenmodell, dann Erfassung, dann Dashboards, dann KI, dann generative KI. Definiere zuerst Attribute, Skalen und Sud-/Partieschlüssel; erfasse in Power Apps auf Dataverse; verankere Stammdaten im ERP; analysiere in Power BI; füge erst dann KI und Gen AI auf saubere, strukturierte Daten hinzu.

**Wann sollte ich das nicht aufbauen?**
Wenn du noch kein kalibriertes Panel und kein sauberes Datenmodell hast — Software behebt das nicht — oder wenn du klein genug bist, dass eine ordentliche Tabelle die Arbeit erledigt. Power-Platform-Lizenzierung und Governance verursachen echte Kosten; kaufe den Stack, wenn die Skalierung es rechtfertigt.

**Was macht generative KI hier eigentlich?**
Sie entwirft Verkostungsnotizen im Hausstil aus den Bewertungen, fasst eine Sitzung zusammen, schreibt eine erste Fassung einer QC-Freigabenotiz und beantwortet klar formulierte Fragen über Copilot. Alles wird von Menschen geprüft. Sie kommuniziert, was das Panel produziert hat — sie verkostet nicht.
