---
layout: post
lang: de
title: "Bevor du KI anfasst, sammle deine Daten: der unglamouröse erste Schritt"
image: /assets/og/collect-your-data-before-ai.png
description: "Der erste Schritt auf der KI-Reise jeder Brauerei ist kein Modell — es ist die Datensammlung. Was zu protokollieren ist, welche Sensoren zählen und warum saubere Aufzeichnungen jedes Mal cleveren Algorithmen schlagen."
date: 2026-05-25 14:00:00 -0700
updated: 2026-05-25
permalink: /de/2026/collect-your-data-before-ai/
tags: [brewer-to-ai, brewing-data, data-collection]
faq:
  - q: "Was ist der erste Schritt für eine Brauerei, die in KI einsteigt?"
    a: "Saubere, konsistente Daten zu sammeln — kein Modell zu kaufen. Protokolliere Gärtemperatur, Dichte, Anstellrate, Sudergebnisse und Verkäufe über die Zeit. Ohne diese Historie hat kein KI-Tool etwas, woraus es lernen kann."
  - q: "Welche Daten sollte eine Brauerei sammeln?"
    a: "Prozessdaten (Temperatur über die Zeit, Dichte, pH-Wert, gelöster Sauerstoff, Anstellrate), Sudergebnisse (was richtig oder falsch lief) und kommerzielle Daten (Verkäufe nach Produkt, Zeit und Ort). Konsistenz zählt mehr als Menge."
  - q: "Brauche ich teure Sensoren, um anzufangen?"
    a: "Nein. Beginne damit, konsistent zu protokollieren, was du bereits misst. Kontinuierliche Sensoren helfen, aber eine disziplinierte manuelle Aufzeichnung schlägt einen schicken Sensor, den niemand abliest."
---

**Kurze Antwort: Der erste Schritt auf der KI-Reise einer Brauerei ist kein Modell und kein Sensor — es ist das Sammeln sauberer, konsistenter Daten. Jedes Projekt, das ich je gebaut habe, lebte oder starb an der Qualität der Aufzeichnungen, die es speisten. So langweilig es klingt, disziplinierte Datensammlung schlägt clevere Algorithmen jedes einzelne Mal.** Hier ist, was ich gerne früher protokolliert hätte.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Von Rohdaten zu einer Entscheidung, auf die das Team reagieren kann — die Pipeline hinter diesem Beitrag."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DATEN → ENTSCHEIDUNG</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Bevor du KI anfasst, sammle deine Daten: der unglamouröse erste Schritt</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Daten</text><text x="90.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Sensoren, Protokolle</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Merkmale</text><text x="289.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">bereinigen &amp; formen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Modell</text><text x="488.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">trainieren / bewerten</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Vorhersage</text><text x="687.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">was als Nächstes passiert</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Aktion</text><text x="886.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Team handelt</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Von Rohdaten zu einer Entscheidung, auf die das Team reagieren kann — die Pipeline hinter diesem Beitrag.</figcaption>
</figure>

## Der Fehler, den jeder macht (mich eingeschlossen)

Als ich mich zum ersten Mal für Daten begeisterte, wollte ich Modelle bauen. Was ich auf die harte Tour lernte: Ein Modell ist nur so gut wie die Historie dahinter, und die meisten Brauereien — meine eingeschlossen — hatten überall Lücken. Messwerte, die genommen wurden, „wenn sich jemand erinnerte“, nie erfasste Ergebnisse, Verkaufsdaten, die in einem völlig anderen System lebten.

Du kannst nicht vorhersagen, was du nie gemessen hast. Also instrumentierst und protokollierst du vor jeglicher KI.

## Was du tatsächlich sammeln solltest

Drei Kategorien decken das meiste ab:

1. **Prozessdaten** — Gärtemperatur *über die Zeit*, Dichte, pH-Wert, gelöster Sauerstoff, Anstellrate. Der Teil „über die Zeit“ zählt: Eine Kurve lehrt ein Modell weit mehr als ein einzelner Messwert. Das ist die Grundlage für Dinge wie [Gärungsprognose]({{ '/de/2026/can-ai-predict-beer-fermentation/' | relative_url }}) und [Qualitätskontrolle]({{ '/de/2026/ai-quality-control-in-brewing/' | relative_url }}).
2. **Sudergebnisse** — was tatsächlich passiert ist. War er stilgerecht? Ist er stecken geblieben? Irgendein Fehlaroma? Ohne beschriftete Ergebnisse kann ein Modell nicht lernen, wie „gut“ und „schlecht“ aussehen.
3. **Kommerzielle Daten** — Verkäufe nach Produkt, Zeit und Ort. Das ist der Treibstoff für [Nachfrageprognose]({{ '/de/2026/ai-demand-forecasting-for-breweries/' | relative_url }}), eine der ertragsstärksten Anwendungen überhaupt.

## Konsistenz schlägt Raffinesse

Du brauchst keine Wand teurer Sensoren, um anzufangen. Du musst *konsistent* protokollieren, was du bereits misst. Ein günstiges Setup, das bei jedem Sud treu erfasst wird, ist mehr wert als ein Sensor in Forschungsqualität, dessen Daten niemand vertraut, weil die Hälfte der Einträge fehlt.

Wenn ich heute Brauereien berate, ist die unglamouröse Wahrheit, mit der ich beginne, diese: Verbringe deine ersten Monate mit Messdisziplin, nicht mit Modellen. Die Modelle können warten. Die Daten lassen sich im Nachhinein nicht zurückholen.

## Der Ertrag

Tu das, und alles Nachgelagerte wird einfacher und billiger. Lass es aus, und du wirst Geld für KI ausgeben, die nichts Verlässliches hat, woraus sie lernen kann — die häufigste Art, wie Brauereien ihr erstes KI-Budget verschwenden.

Als Nächstes: wie ich mir die Datenseite beigebracht habe, während ich noch als Brauer arbeitete.

*From Brewer to AI — Teil 3 von 8. [Vollständige Serie]({{ '/de/series/brewer-to-ai/' | relative_url }}) · [Weiter: Wie ich mir Data Science selbst beigebracht habe →]({{ '/de/2026/learning-data-science-as-a-brewer/' | relative_url }})*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 260" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Die wenigen Zahlen, auf die es ankommt."><rect x="0" y="0" width="720" height="260" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">DIE ZAHLEN</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Bevor du KI anfasst, sammle deine Daten: der unglamouröse erste Schritt</text><rect x="70" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">Kennzahl 1</text><rect x="90" y="135" width="120" height="22" rx="3" fill="#00695c"/><text x="90" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs. Ziel</text><rect x="280" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="300" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">Kennzahl 2</text><rect x="300" y="135" width="100" height="22" rx="3" fill="#00695c"/><text x="300" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs. Ziel</text><rect x="490" y="90" width="160" height="120" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="510" y="120" font-family="sans-serif" font-size="12" fill="#4a6b64">Kennzahl 3</text><rect x="510" y="135" width="80" height="22" rx="3" fill="#00695c"/><text x="510" y="190" font-family="sans-serif" font-size="11.5" fill="#4a6b64">vs. Ziel</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die wenigen Zahlen, auf die es ankommt.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist der erste Schritt für eine Brauerei, die in KI einsteigt?**
Saubere, konsistente Daten zu sammeln — kein Modell zu kaufen. Protokolliere Gärtemperatur, Dichte, Anstellrate, Sudergebnisse und Verkäufe über die Zeit. Ohne diese Historie hat kein KI-Tool etwas, woraus es lernen kann.

**Welche Daten sollte eine Brauerei sammeln?**
Prozessdaten (Temperatur über die Zeit, Dichte, pH-Wert, gelöster Sauerstoff, Anstellrate), Sudergebnisse (was richtig oder falsch lief) und kommerzielle Daten (Verkäufe nach Produkt, Zeit und Ort). Konsistenz zählt mehr als Menge.

**Brauche ich teure Sensoren, um anzufangen?**
Nein. Beginne damit, konsistent zu protokollieren, was du bereits misst. Kontinuierliche Sensoren helfen, aber eine disziplinierte manuelle Aufzeichnung schlägt einen schicken Sensor, den niemand abliest.
