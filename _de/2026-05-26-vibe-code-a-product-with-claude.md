---
layout: post
lang: de
title: "Wie man ein Produkt mit Claude vibe-codet (es ist eine Schleife, keine Magie)"
image: /assets/og/vibe-code-a-product-with-claude.png
description: "Vibe-Coding mit Claude ist nicht, dass die KI deine App schreibt, während du zusiehst. Es ist eine Bauen-Verifizieren-Beheben-Schleife — und der Verifizierer ist das, was ein auslieferbares Produkt von einer selbstsicheren Demo trennt."
date: 2026-05-26
updated: 2026-05-26
permalink: /de/2026/vibe-code-a-product-with-claude/
tags: [vibe-coding, claude, ai-tools, building-with-ai]
faq:
  - q: "Was ist Vibe-Coding?"
    a: "Vibe-Coding heißt, in einfacher Sprache zu beschreiben, was man will, und einen KI-Agenten das eigentliche Tippen erledigen zu lassen — Dateien bearbeiten, Befehle ausführen, Fehler lesen. Mit einem Werkzeug wie Claude Code beaufsichtigst du eine Schleife, statt jede Zeile selbst zu schreiben."
  - q: "Kann Claude ein ganzes Produkt allein bauen?"
    a: "Es kann viel vom Bauen übernehmen, aber nicht unbeaufsichtigt. Das verlässliche Muster ist eine Schleife: Du beschreibst die Absicht, Claude baut, etwas verifiziert das Ergebnis, Claude liest den Fehler und behebt ihn. Ohne Verifizierer bekommst du eine Demo, die beim Kontakt mit echter Nutzung zerbricht."
  - q: "Was ist der wichtigste Teil beim Vibe-Coding mit Claude?"
    a: "Die Prüfung. Etwas einzurichten, das die Arbeit automatisch verifiziert — ein Test, ein Validator, ein Skript, das bestätigt, dass die Ausgabe korrekt ist — ist das, was aus 'sieht fertig aus' ein 'ist fertig' macht. Der Prompt ist weit weniger wichtig als der Verifizierer."
---

**Kurze Antwort: Vibe-Coding mit Claude ist nicht, dass die KI deine App schreibt, während du zusiehst — es ist eine Schleife. Du beschreibst, was du willst, Claude baut es, etwas prüft das Ergebnis, Claude liest den Fehler und behebt ihn, und das wiederholt sich, bis die Sache tatsächlich funktioniert. Die Fähigkeit ist nicht der Prompt. Es ist das Einrichten der Prüfung. Mach den Verifizierer richtig, und du kannst echte Software ausliefern; lass ihn weg, und du hast eine selbstsichere Demo, die umfällt, sobald ein echter Nutzer sie berührt.** Hier ist, wie es tatsächlich läuft.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Von Rohdaten zu einer Entscheidung, auf die das Team reagieren kann — die Pipeline hinter diesem Beitrag."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DATEN → ENTSCHEIDUNG</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Wie man ein Produkt mit Claude vibe-codet (es ist eine Schleife, keine Magie)</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Daten</text><text x="90.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Sensoren, Protokolle</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Merkmale</text><text x="289.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">bereinigen &amp; formen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Modell</text><text x="488.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">trainieren / bewerten</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Vorhersage</text><text x="687.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">was als Nächstes passiert</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Aktion</text><text x="886.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Team handelt</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Von Rohdaten zu einer Entscheidung, auf die das Team reagieren kann — die Pipeline hinter diesem Beitrag.</figcaption>
</figure>

## „Vibe-Coding" muss als Begriff zu viel leisten

Das Wort beschwört eine Fantasie herauf: Du tippst einen Wunsch, eine fertige App erscheint, du nippst an deinem Kaffee. So läuft es nicht, und so zu tun, als ob, ist die Art, wie Leute kaputte Dinge ausliefern.

Die ehrliche Version: Vibe-Coding heißt, Absicht in einfacher Sprache zu beschreiben und einen KI-Agenten — ich nutze Claude Code, das im Terminal läuft — das Tippen erledigen zu lassen. Er liest deine Dateien, schreibt Code, führt Befehle aus und liest die Fehler, die zurückkommen. Du schreibst nicht jede Zeile. Du steuerst, und du prüfst. Dieser zweite Teil ist der ganze Job.

## Die Schleife ist das Produkt

Streift man das Marketing ab, sieht jede nützliche Sitzung wie dieselben vier Schritte aus:

1. **Beschreiben** — sag Claude in einfacher Sprache das Ergebnis, das du willst.
2. **Bauen** — er bearbeitet die Dateien und führt die Befehle aus.
3. **Verifizieren** — etwas prüft das Ergebnis: ein Test, ein Validator, ein Skript, die echte App.
4. **Beheben** — Claude liest den Fehler und legt erneut los.

Hier ist ein echtes Beispiel aus dieser Woche. Ich bat Claude, einer Sales-Pipeline-Dashboard einen Schwung berechneter Kennzahlen hinzuzufügen — eine tatsächliche Tableau-Arbeitsmappe mit einem echten Datenmodell, kein Spielzeug. Es öffnete die Datei, las das Datenmodell und fand 92 numerische Felder. Es warf die 58 weg, deren Aggregation Unsinn ist (Breitengrad, Längengrad, Geschäftsjahr-Ganzzahlen, Login-Zähler), und baute **173 berechnete Kennzahlen** — Summen, Mittelwerte, Verhältnisse, laufende Summen, Jahr-über-Jahr — auf den 34, auf die es tatsächlich ankommt.

Dann versuchte es, die Datei zu speichern, und **Tableau lehnte sie ab.** Der erste Versuch setzte die neuen Felder an die falsche Stelle in der Struktur der Datei, und Tableau warf einen Schemafehler und weigerte sich, sie zu laden.

Diese Ablehnung ist der wichtigste Moment der Geschichte. Weil es einen Verifizierer gab — Tableau selbst, plus ein Skript, das prüfte, dass jede Formel auf ein echtes Feld zeigt — *sah* Claude, dass es gescheitert war. Es las den genauen Fehler, verschob die Felder an die korrekte Position und prüfte erneut, bis die Struktur gültig war. Ohne diese Prüfung hätte ich fröhlich eine Datei ausgeliefert, die sich schlicht nicht öffnen ließe.

## Dieselbe Schleife, ganz verschiedene Aufgaben

Der Schleife ist es egal, was du baust. In einem Abschnitt dieser Woche lief sie über vier Aufgaben, die nichts gemeinsam haben:

- Ein **Tableau-Dashboard-Werkzeug** (die 173 Kennzahlen oben).
- Ein **Bauplan für ein ERP-Feature** — eine vollständige Durchführung, wie man eine interne App aufsetzt, wobei die gesamte Methode dieselbe Schleife war: die Änderung schreiben, sie deployen, einen Browser-Test die echten Bildschirme bedienen lassen, die Fehler lesen, beheben.
- Ein **34-seitiges PDF, verwandelt in sauberes Markdown**, mit Tabellen und Checklisten und allem.
- Eine **neu verdrahtete Wissensdatenbank**, sodass ein neues Dokument korrekt in alles Verwandte verlinkt wurde.

Verschiedene Werkzeuge, verschiedene Dateitypen, identischer Rhythmus: beschreiben, bauen, verifizieren, beheben.

## Der Verifizierer ist das ganze Spiel

Das ist der Teil, den der Hype überspringt. Ein KI-Agent, der Code schreibt, ohne diesen Code prüfen zu können, ist eine sehr schnelle Art, plausible Fehler zu erzeugen. Der Agent wird dir sagen, er sei fertig. Er glaubt es. Er liegt oft falsch.

Was die Schleife vertrauenswürdig macht, ist das Ding auf der anderen Seite von „bauen":

- Beim Dashboard war es Tableaus eigener Validator plus ein Skript, das bestätigte, dass jede Formel auf eine echte Spalte verwies.
- Bei einer App sind es Tests — oder ein Werkzeug wie Playwright, das die tatsächliche Benutzeroberfläche bedient und meldet, was kaputtging.
- Beim PDF war ich es, der die Ausgabe gegen das Original las.

Das ist dieselbe Disziplin, auf die ich immer wieder zurückkomme in [warum du jede Zahl prüfen musst, die KI berührt]({{ '/de/2026/can-ai-write-your-ttb-reports/' | relative_url }}). Eine selbstsichere falsche Antwort ist der Standard-Fehlerfall dieser Modelle. Der Verifizierer ist das, was ihn abfängt, bevor deine Nutzer es tun. Baue die Prüfung zuerst, und der Rest der Schleife wird sicher genug, um schnell zu laufen.

## Wenn du derjenige bist, der es baut

Wenn du das praktisch machen willst, ist das Setup klein und es geht meist darum, die Schleife laufen zu lassen, ohne dass du sie hütest:

- **Führe Claude Code in deinem Projekt aus.** Richte es auf das Repo. Es arbeitet an den echten Dateien, nicht in einem Chatfenster.
- **Schreibe auf, wie man baut und verifiziert** in einem `CLAUDE.md` im Projektstamm — die genauen Befehle zum Kompilieren, Deployen und Testen. Das ist das Wirksamste, was du tun kannst. Jetzt ist „bauen und prüfen" etwas, das Claude selbst ausführen kann.
- **Setze die sicheren Befehle auf die Allowlist** (deinen Test-Runner, dein Build-Werkzeug), damit die Schleife nicht in jedem Zyklus stehenbleibt, um um Erlaubnis zu fragen.
- **Prompte Absicht *plus* die Prüfung.** Nicht „füge das Feature hinzu", sondern „füge das Feature hinzu, dann bestätige es, indem du die Tests ausführst und alles Rote behebst." Die zweite Klausel ist das, was die Schleife schließt. Mein Tableau-Prompt war im Wesentlichen: *füge diese Kennzahlen hinzu, dann verifiziere, dass die Datei gültig ist und jede Formel auflöst.* Die Verifizierungs-Klausel ist der Grund, warum der Schemafehler abgefangen und behoben statt ausgeliefert wurde.

Das war's. Der Agent ist fähig; die Struktur ist das, was ihn verlässlich macht.

## Wo die Vibes lügen

Sei klaräugig hinsichtlich der Fehlerfälle, denn sie sind real:

- **Es scheitert beim ersten Versuch, routinemäßig.** Die Tableau-Datei wurde abgelehnt, bevor sie funktionierte. Das ist völlig in Ordnung, *sofern* du einen Verifizierer hast — und ein ernstes Problem, wenn nicht, denn du wirst es nicht wissen.
- **Es kann nicht alles sehen.** Jenes PDF hatte zwei Seiten, die reine Diagramme waren, ohne extrahierbaren Text. Claude markierte sie und ließ stattdessen eine Vorlage zurück, statt Inhalt zu erfinden — was genau das richtige Verhalten ist und genau die Art Lücke, auf die du prüfen musst.
- **Es produziert selbstsichere, falsche Ausgaben.** Halluzinierte Zahlen, falsch zitierte Regeln, Felder, die nicht existieren. Das ist die [ehrliche Grenze dieser Werkzeuge]({{ '/de/2026/the-honest-limits-of-ai-in-brewing/' | relative_url }}), und kein noch so gutes Prompten beseitigt sie. Sie wird nur stromabwärts abgefangen.
- **Es trifft Ermessensentscheidungen, die du prüfen solltest.** Es entschied, welche 58 Felder zu verwerfen sind. Gute Entscheidungen, dieses Mal — aber ich habe sie geprüft. Solltest du auch.

Nichts davon ist ein Grund, es nicht zu nutzen. Es ist ein Grund, die Ausgabe niemals unverifiziert auszuliefern.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 260" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Die wenigen Zahlen, auf die es ankommt."><rect x="0" y="0" width="720" height="260" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">DIE ZAHLEN</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Wie man ein Produkt mit Claude vibe-codet (es ist eine Schleife, keine Magie)</text><rect x="70" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">Kennzahl 1</text><rect x="90" y="135" width="120" height="22" rx="3" fill="#00695c"/><text x="90" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs. Ziel</text><rect x="280" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="300" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">Kennzahl 2</text><rect x="300" y="135" width="100" height="22" rx="3" fill="#00695c"/><text x="300" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs. Ziel</text><rect x="490" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="510" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">Kennzahl 3</text><rect x="510" y="135" width="80" height="22" rx="3" fill="#00695c"/><text x="510" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs. Ziel</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die wenigen Zahlen, auf die es ankommt.</figcaption>
</figure>

## Das Fazit

Ein Produkt mit Claude zu vibe-coden funktioniert, und es ist wirklich schnell — aber die Geschwindigkeit kommt aus der Schleife, nicht daraus, der ersten Antwort zu vertrauen. Der Zug ist einfach:

1. **Wähle etwas mit einer klaren Prüfung** — einen Test, einen Validator, einen Bildschirm, den du bedienen kannst.
2. **Schreibe die Bauen-und-Verifizieren-Befehle auf**, damit der Agent sie selbst ausführen kann.
3. **Prompte die Absicht und die Prüfung zusammen.**
4. **Lass die Schleife laufen und überprüfe das grüne Ergebnis** — nicht jeden Tastenanschlag.
5. **Verifiziere die Substanz selbst, bevor sie ausgeliefert wird.**

Vibe-code das Tippen. Vibe-code niemals die Verifizierung. Diese Grenze ist der Unterschied zwischen einer Wochenend-Demo und etwas, das du tatsächlich einem Kunden vorlegen würdest.

## Häufig gestellte Fragen

**Was ist Vibe-Coding?**
Vibe-Coding heißt, in einfacher Sprache zu beschreiben, was man will, und einen KI-Agenten das eigentliche Tippen erledigen zu lassen — Dateien bearbeiten, Befehle ausführen, Fehler lesen. Mit einem Werkzeug wie Claude Code beaufsichtigst du eine Schleife, statt jede Zeile selbst zu schreiben.

**Kann Claude ein ganzes Produkt allein bauen?**
Es kann viel vom Bauen übernehmen, aber nicht unbeaufsichtigt. Das verlässliche Muster ist eine Schleife: Du beschreibst die Absicht, Claude baut, etwas verifiziert das Ergebnis, Claude liest den Fehler und behebt ihn. Ohne Verifizierer bekommst du eine Demo, die beim Kontakt mit echter Nutzung zerbricht.

**Was ist der wichtigste Teil beim Vibe-Coding mit Claude?**
Die Prüfung. Etwas einzurichten, das die Arbeit automatisch verifiziert — ein Test, ein Validator, ein Skript, das bestätigt, dass die Ausgabe korrekt ist — ist das, was aus „sieht fertig aus" ein „ist fertig" macht. Der Prompt ist weit weniger wichtig als der Verifizierer.
