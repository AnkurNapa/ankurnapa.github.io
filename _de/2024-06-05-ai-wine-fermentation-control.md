---
layout: post
lang: de
title: "KI zur Steuerung der Weingärung (und bei steckengebliebenen Gärungen)"
image: /assets/og/ai-wine-fermentation-control.png
description: "Wie KI die Kinetik der Weingärung und das Risiko steckengebliebener Gärungen aus YAN, Zucker und Temperatur modelliert — zur Steuerung von Nährstoff- und Temperaturentscheidungen bei Weiß- und Rotweinen und zum Management der BSA."
date: 2024-06-05
updated: 2024-06-05
permalink: /de/2024/ai-wine-fermentation-control/
tags: [winemaking, fermentation, process-optimization]
faq:
  - q: "Kann KI eine steckengebliebene Gärung vorhersagen, bevor sie passiert?"
    a: "Oft ja — früh in der Gärung. Ein Modell, das die Zuckerabbaukurve neben YAN, Temperatur und Anfangszucker beobachtet, kann einen Hochrisikotank markieren, während du noch mit Nährstoffen oder Temperatur eingreifen kannst."
  - q: "Was ist YAN und warum kümmert sich das Modell darum?"
    a: "Hefeverwertbarer Stickstoff (yeast-assimilable nitrogen), üblicherweise auf etwa 150-250 mg/L angepeilt. Niedriges YAN ist eine Hauptursache für träge und steckengebliebene Gärungen, daher ist es einer der stärksten Prädiktoren in jedem Modell."
  - q: "Funktioniert das bei Wild- oder Spontangärungen?"
    a: "Weniger gut. Spontangärungen werden von einer wechselnden Mischung wilder Hefen angetrieben, daher sind sie weitaus schwerer zu modellieren als eine saubere Beimpfung mit einem bekannten Saccharomyces-Stamm."
---

**Kurze Antwort: KI kann eine steckengebliebene oder träge Gärung früh erkennen und eine Nährstoff- oder Temperaturkorrektur empfehlen — aber nur, wenn dein Tank tatsächlich instrumentiert ist und deine Gärung eine saubere, beimpfte ist.** Die Gärung ist der Punkt, an dem Chemie zu Wein wird, und ein steckengebliebener Tank ist eines der teuersten Dinge, die schiefgehen können.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Weinproduktionsablauf sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">KI zur Steuerung der Weingärung (und bei steckengebliebenen Gärungen)</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Lese</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Mahlen / Pressen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Gären</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Ausbauen</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Abfüllen</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Wo dies im Weinproduktionsablauf sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Was ein Gärungsmodell tatsächlich vorhersagt
Die meisten Moste werden mit Weinstämmen von *Saccharomyces cerevisiae* beimpft, und eine gesunde Gärung folgt einer erkennbaren Zuckerabbaukurve. Die Aufgabe des Modells ist, zwei Dinge vorherzusagen: die Form dieser Kurve und das Risiko, dass sie stockt. Steckengebliebene und träge Gärungen kommen aus einer bekannten kurzen Liste von Ursachen — niedriger hefeverwertbarer Stickstoff (YAN, oft auf etwa 150-250 mg/L angepeilt), hoher Zucker und der dadurch entstehende osmotische Stress, Temperaturextreme und Ethanoltoxizität, wenn der Alkohol steigt. Ein auf vergangenen Gärungen trainiertes Modell lernt, wie diese Faktoren zusammenwirken und wie die frühe Kurve Schwierigkeiten verrät, bevor der Tank sichtbar stockt.

Es hat auch eine Rolle bei der malolaktischen Gärung (BSA), bei der *Oenococcus oeni* scharfe Äpfelsäure in weichere Milchsäure umwandelt und butteriges Diacetyl freisetzen kann. Vorherzusagen, ob und wie schnell die BSA läuft, hilft dir, den Kellerkalender zu planen.

## Erst messen: die Daten, die das Modell braucht
Die Eingaben sind die Hebel, die ein Winzer ohnehin zieht. Anfangszucker (°Brix), YAN, Gärtemperatur und die Zeitreihe des Zuckerabbaus sind der Kern. Temperatur ist keine einzelne Zahl, sondern eine Steuerungsentscheidung: Weißweine gären kühler, etwa 12-18 °C, um Aromatik zu erhalten, während Rotweine wärmer laufen, um die 25-30 °C, um Farb- und Tanninextraktion zu fördern. Das Modell lernt, wie sich derselbe Nährstoff- oder Temperaturzug über diese Regime hinweg unterschiedlich auswirkt.

Der Haken sind die Sensoren. Ein Modell, das eine Gärung in Echtzeit beobachtet, braucht, dass die Daten existieren — Temperaturfühler und idealerweise Dichte- oder Zuckerverfolgung an jedem Tank. Viele Keller messen ein- oder zweimal täglich von Hand, was genügt, um ein Stocken zu erkennen, aber für ein kinetisches Modell dünn ist. Der ehrliche Ausgangspunkt ist eine häufigere, konsistente Protokollierung zuerst an deinen Problemtanks.

## Wo es scheitert
Steckengebliebene Gärungen sind glücklicherweise selten — was genau der Grund ist, warum sie schwer zu modellieren sind. Die Ereignisse, die du am meisten vorhersagen möchtest, sind jene, von denen du die wenigsten Beispiele hast, sodass ein Modell beim ungewöhnlichen Tank selbstsicher falsch liegen kann. Spontan- oder Wildgärungen verschärfen dies: Mit einer wechselnden Gemeinschaft wilder Hefen statt eines einzelnen bekannten Stamms ist die Kinetik wirklich weniger vorhersehbar, und ein auf sauberen Beimpfungen trainiertes Modell überträgt sich nicht sauber. Und kein Modell rettet einen Tank, den du nicht misst. Die realistische Haltung ist, KI als Frühwarnsystem bei instrumentierten, beimpften Gärungen zu nutzen und die Rettungsprotokolle — rehydrierte Hefe, Nährstoffzugaben, Temperaturkorrektur — fest in menschlicher Hand zu behalten.

## Wie generative KI hineinpasst
Der nützlichste generative Aspekt ist ein Keller-Copilot, der eine träge Gärung in Worten erklärt und eine Rettung vorschlägt. Statt eines Winzers, der um 23 Uhr auf eine abflachende Kurve blinzelt, liest der Copilot die Daten des Tanks und sagt: „Der Zuckerabbau in Tank 12 hat sich bei 32 g/L Restzucker auf unter 0,5 °Brix/Tag verlangsamt; YAN kam mit 110 mg/L niedrig herein und die Temperatur ist auf 31 °C gedriftet. Wahrscheinlich stickstofflimitiert mit thermischem Stress. Erwäge eine gestaffelte Nährstoffzugabe und ein Absenken der Temperatur Richtung 26 °C; prüfe die Dichte in 12 Stunden erneut." Es nennt die Begründung, nicht nur eine Warnung, und kann die Kellernotiz entwerfen, damit der Eingriff dokumentiert ist. Synthetische Daten haben hier ebenfalls eine stille Rolle — weil echte steckengebliebene Gärungen rar sind, können simulierte Stressszenarien einem Modell helfen, die Warnzeichen zu lernen, die es sonst selten sähe, vorausgesetzt, du validierst gegen echte Tanks.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Die meisten Messwerte liegen im normalen Band; das Modell markiert den, der es nicht tut."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">ANOMALIEERKENNUNG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">KI zur Steuerung der Weingärung (und bei steckengebliebenen Gärungen)</text><rect x="60" y="120" width="620" height="70" fill="#2e9e7c" opacity="0.12"/><line x1="60" y1="120" x2="680" y2="120" stroke="#2e9e7c" stroke-width="1" stroke-dasharray="4 3"/><line x1="60" y1="190" x2="680" y2="190" stroke="#2e9e7c" stroke-width="1" stroke-dasharray="4 3"/><circle cx="110" cy="150" r="5" fill="#4a6b64"/><circle cx="160" cy="140" r="5" fill="#4a6b64"/><circle cx="210" cy="165" r="5" fill="#4a6b64"/><circle cx="265" cy="148" r="5" fill="#4a6b64"/><circle cx="320" cy="158" r="5" fill="#4a6b64"/><circle cx="380" cy="143" r="5" fill="#4a6b64"/><circle cx="440" cy="168" r="5" fill="#4a6b64"/><circle cx="500" cy="150" r="5" fill="#4a6b64"/><circle cx="560" cy="160" r="5" fill="#4a6b64"/><circle cx="620" cy="146" r="5" fill="#4a6b64"/><circle cx="345" cy="92" r="7" fill="#06483f"/><text x="345" y="80" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">Anomalie</text><text x="668" y="138" text-anchor="end" font-family="sans-serif" font-size="11" fill="#2e9e7c">normales Band</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die meisten Messwerte liegen im normalen Band; das Modell markiert den, der es nicht tut.</figcaption>
</figure>

## Das Fazit
Der wahre Wert eines Gärungsmodells liegt darin, einen steckengebliebenen oder trägen Tank früh genug zu erwischen, um ihn zu beheben — wenn Nährstoff- oder Temperaturkorrekturen noch wirken. Dieser Ertrag ist real für saubere, instrumentierte Gärungen und schwach für spärlich gemessene oder spontane. Instrumentiere deine Problemtanks, modelliere die frühe Kurve und lass einen Copilot die Daten in eine Entscheidung verwandeln, auf die der Winzer noch heute Abend reagieren kann.

*Teil des Tracks [Weinbereitung & KI]({{ '/de/tracks/winemaking-ai/' | relative_url }}).* Verwandt: [KI zur Optimierung des Weinverschnitts]({{ '/de/2024/ai-wine-blending-optimization/' | relative_url }}).

## Häufig gestellte Fragen

**Kann KI eine steckengebliebene Gärung vorhersagen, bevor sie passiert?**
Oft ja — früh in der Gärung. Ein Modell, das die Zuckerabbaukurve neben YAN, Temperatur und Anfangszucker beobachtet, kann einen Hochrisikotank markieren, während du noch mit Nährstoffen oder Temperatur eingreifen kannst.

**Was ist YAN und warum kümmert sich das Modell darum?**
Hefeverwertbarer Stickstoff (yeast-assimilable nitrogen), üblicherweise auf etwa 150-250 mg/L angepeilt. Niedriges YAN ist eine Hauptursache für träge und steckengebliebene Gärungen, daher ist es einer der stärksten Prädiktoren in jedem Modell.

**Funktioniert das bei Wild- oder Spontangärungen?**
Weniger gut. Spontangärungen werden von einer wechselnden Mischung wilder Hefen angetrieben, daher sind sie weitaus schwerer zu modellieren als eine saubere Beimpfung mit einem bekannten Saccharomyces-Stamm.
