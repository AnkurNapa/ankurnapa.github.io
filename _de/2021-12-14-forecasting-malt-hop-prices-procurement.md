---
layout: post
lang: de
title: "Malz- und Hopfenpreise prognostizieren für eine klügere Beschaffung"
image: /assets/og/forecasting-malt-hop-prices-procurement.png
description: "Wie die Prognose von Malz- und Hopfenpreisen den Beschaffungszeitpunkt und die Vertragsgrößen für Brauereien steuert und warum Hedging das Restrisiko managt, das Prognosen nicht beseitigen können."
date: 2021-12-14
updated: 2021-12-14
permalink: /de/2021/forecasting-malt-hop-prices-procurement/
tags: [fpna, procurement, forecasting]
faq:
  - q: "Wie hilft die Prognose von Malz- und Hopfenpreisen der Beschaffung?"
    a: "Sie liefert die Grundlage dafür, wann und wie viel kontrahiert wird. Indem eine Brauerei antizipiert, wohin sich Getreide- und Hopfenpreise mit Ernte, Wetter und Vertragszyklen bewegen könnten, kann sie Einkäufe terminieren und Mengen dimensionieren, statt reaktiv zu kaufen."
  - q: "Ist Preisprognose dasselbe wie Szenarioplanung?"
    a: "Nein. Eine Prognose schätzt den wahrscheinlichen Verlauf eines Preises, um Beschaffungszeitpunkt und -menge zu steuern. Szenarioplanung untersucht 'Was-wäre-wenn'-Ergebnisse für das Gesamtgeschäft. Sie ergänzen sich, sind aber verschieden."
  - q: "Kann eine Prognose das Rohstoffpreisrisiko beseitigen?"
    a: "Nein. Rohstoffpreise sind von Natur aus verrauscht, eine Prognose verringert also die Unsicherheit, beseitigt sie aber nie. Hedging und Lieferverträge managen das Restrisiko, das die Prognose übrig lässt."
---

**Kurze Antwort: Die Prognose von Malz- und Hopfenpreisen sagt dir, wann und wie viel du kontrahieren solltest, und macht aus reaktivem Einkauf eine bewusste Beschaffungssteuerung.** Sie ist ein Finanz- und Beschaffungswerkzeug, unterscheidet sich von der Szenarioplanung und funktioniert am besten, wenn du akzeptierst, dass das Restrisiko gehedgt werden muss.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Malz- und Hopfenpreise prognostizieren für eine klügere Beschaffung</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">den Betrieb ändern</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Was Malz- und Hopfenpreise bewegt
Getreide- und Hopfenpreise sind nicht zufällig; sie reagieren auf identifizierbare Kräfte. Ernteerträge legen die Angebotsbasis fest. Wetter — Dürre, Frost, eine schlechte Wachstumssaison — verschiebt diese Basis, manchmal stark. Vertragszyklen und die breitere Nachfrage üben ihren eigenen Druck aus. Ein Prognosemodell lernt aus dieser Historie und aus aktuellen Signalen, um abzuschätzen, wohin sich die Preise über einen Einkaufshorizont wahrscheinlich bewegen.

Es geht nicht darum, eine einzelne Zahl auf den Cent genau vorherzusagen. Es geht darum, der Beschaffung eine belastbare Sicht auf den wahrscheinlichen Verlauf und dessen Unsicherheit zu geben, damit Entscheidungen über Zeitpunkt und Menge auf Belegen beruhen statt auf Bauchgefühl oder der Rechnung des Vorjahres.

## Von der Prognose zur Einkaufsentscheidung
Eine Preisprognose zählt nur, wenn sie eine Entscheidung verändert, und hier ist die Entscheidung konkret: wann kontrahieren und wie viel. Wenn das Modell und seine Treiber vor einer knappen Ernte auf steigende Malzpreise hindeuten, kann frühere oder größere Kontrahierung die Marge schützen. Sehen die Preise weich aus, kannst du vielleicht abwarten und näher am Bedarf kaufen. Die Prognose steuert Beschaffungszeitpunkt und Vertragsgröße — das ist ihre Aufgabe.

Das ist es wert, von der Szenarioplanung getrennt zu werden. Szenarioplanung fragt "Was passiert mit dem Geschäft, wenn die Inputkosten um 20 Prozent springen?" — ein strategischer Stresstest. Prognose fragt "Wohin gehen die Preise wahrscheinlich, also wann und wie viel sollten wir jetzt kaufen?" — eine Beschaffungsentscheidung. Beide gehören in ein FP&A-Werkzeug, aber sie zu vermengen verwischt die Handlung.

Wie immer gilt: zuerst messen. Verfolge deine tatsächlichen Einkaufspreise und -zeitpunkte gegen das, was ein naiver "bei Bedarf kaufen"-Ansatz gekostet hätte. Diese Basislinie ist der Beweis, dass die Prognose Mehrwert geschaffen hat, und sie hält dich ehrlich darüber, ob das Modell schlägt, einfach gleichmäßig einzukaufen. Für einen breiteren Blick darauf, wo Analytik in einer Brauerei hineinpasst, siehe [was KI für eine Brauerei tun kann]({{ '/de/2026/what-can-ai-do-for-a-brewery/' | relative_url }}).

## Ein generativer KI-Copilot für die Beschaffung
Rohe Prognosen sind unter Zeitdruck schwer umzusetzen. Ein generativer KI-Copilot kann das Bild zusammenfassen: welche Treiber die Preise schieben — etwa eine schlechte Hopfenernte plus feste Nachfrage —, was die Prognose impliziert und eine klare Einkaufsempfehlung mit ihrer Begründung. Er komprimiert eine dichte Analyse in etwas, das eine Beschaffungsleitung in Minuten umsetzen oder infrage stellen kann.

Der Copilot empfiehlt; der Einkäufer entscheidet. Er könnte ein verrauschtes Signal übergewichten, also gehört der finale Ruf dem Menschen, der die Lieferantenbeziehungen und die Liquiditätslage kennt. Der Wert liegt in Klarheit und Tempo, nicht in der Delegation des Urteils.

## Wo es bricht
Die ehrliche Grenze ist, dass Rohstoffe verrauscht sind. Wetterschocks, Geopolitik und plötzliche Nachfrageschwankungen können jede Prognose durchschlagen, und Agrarpreise insbesondere neigen zu Überraschungen, die kein Modell kommen sah. Eine Prognose als Gewissheit zu behandeln, ist die Art, wie Brauereien erwischt werden.

Die Prognose ist also ein Ausgangspunkt, keine Garantie. Das Restrisiko, das sie nicht beseitigen kann, managst du mit den Werkzeugen, die genau dafür gebaut sind: Hedging und Lieferverträge, die Preise oder Mengen festschreiben. Die Prognose sagt dir, wann diese Werkzeuge den Einsatz wert sind; sie ersetzt sie nicht. Zusammen eingesetzt — eine Prognose zur Steuerung des Zeitpunkts, Verträge zur Begrenzung des Abwärtsrisikos — bekommst du eine Beschaffungsstrategie, die hält, wenn die Ernte enttäuscht.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Von Anfang bis Ende, zerlegt in die Bausteine, die die Zahl bewegen."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">BRÜCKE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Malz- und Hopfenpreise prognostizieren für eine klügere Beschaffung</text><line x1="60" y1="250" x2="680" y2="250" stroke="#06483f" stroke-width="1.5"/><rect x="90" y="100" width="80" height="150" fill="#00695c"/><text x="130" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">Start</text><rect x="230" y="140" width="80" height="40" fill="#06483f"/><text x="270" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">−40</text><rect x="350" y="170" width="80" height="30" fill="#06483f"/><text x="390" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">−30</text><rect x="470" y="130" width="80" height="40" fill="#2e9e7c"/><text x="510" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">+40</text><rect x="590" y="130" width="80" height="120" fill="#00695c"/><text x="630" y="268" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">Ende</text><line x1="170" y1="100" x2="230" y2="100" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="310" y1="140" x2="350" y2="140" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="430" y1="170" x2="470" y2="170" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/><line x1="550" y1="130" x2="590" y2="130" stroke="#4a6b64" stroke-width="1" stroke-dasharray="3 3"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Von Anfang bis Ende, zerlegt in die Bausteine, die die Zahl bewegen.</figcaption>
</figure>

## Das Fazit
Die Prognose von Malz- und Hopfenpreisen schärft Beschaffungszeitpunkt und Vertragsgröße, was eine andere und umsetzbarere Aufgabe ist als die Szenarioplanung. Setze eine Basislinie gegen naives Einkaufen, ergänze einen Copilot, der Prognosen in Empfehlungen übersetzt, und kopple jede Prognose mit Hedging oder Verträgen, um das Rauschen zu managen, das kein Modell wegprognostizieren kann.

*Teil des Tracks [Financial Planning & Analytics]({{ '/de/tracks/financial-planning-analytics/' | relative_url }}).*

## Häufig gestellte Fragen

**Wie hilft die Prognose von Malz- und Hopfenpreisen der Beschaffung?**
Sie liefert die Grundlage dafür, wann und wie viel kontrahiert wird. Indem eine Brauerei antizipiert, wohin sich Getreide- und Hopfenpreise mit Ernte, Wetter und Vertragszyklen bewegen könnten, kann sie Einkäufe terminieren und Mengen dimensionieren, statt reaktiv zu kaufen.

**Ist Preisprognose dasselbe wie Szenarioplanung?**
Nein. Eine Prognose schätzt den wahrscheinlichen Verlauf eines Preises, um Beschaffungszeitpunkt und -menge zu steuern. Szenarioplanung untersucht 'Was-wäre-wenn'-Ergebnisse für das Gesamtgeschäft. Sie ergänzen sich, sind aber verschieden.

**Kann eine Prognose das Rohstoffpreisrisiko beseitigen?**
Nein. Rohstoffpreise sind von Natur aus verrauscht, eine Prognose verringert also die Unsicherheit, beseitigt sie aber nie. Hedging und Lieferverträge managen das Restrisiko, das die Prognose übrig lässt.
