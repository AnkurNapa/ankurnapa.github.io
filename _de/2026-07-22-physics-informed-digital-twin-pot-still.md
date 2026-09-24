---
layout: post
lang: de
title: "Ein physikbasierter digitaler Zwilling einer Pot Still: Warum reine ML-Zwillinge driften"
image: /assets/og/physics-informed-digital-twin-pot-still.png
description: "Teil 1 von The Still and the Model. Eine Batch-Pot-Still folgt der Rayleigh-Gleichung, und der Alkohol, der hineingeht, muss auch wieder herauskommen. Warum ein rein datengetriebener Zwilling dieses Gesetz stillschweigend bricht und wie ein hybrides Modell, mit Physik für die Struktur und Destillationsdaten für einige wenige angepasste Parameter, ehrlich bleibt."
date: 2026-07-22 09:00:00 -0700
updated: 2026-07-22
permalink: /de/2026/physics-informed-digital-twin-pot-still/
tags: [distilling-maturation, still-and-model, digital-twin, machine-learning, data-engineering]
faq:
  - q: "Was ist ein physikbasierter digitaler Zwilling einer Brennblase?"
    a: "Ein Modell, dessen Struktur aus der Physik der Destillation stammt, etwa aus der Rayleigh-Gleichung und dem Dampf-Flüssigkeits-Gleichgewicht, und bei dem nur wenige Parameter aus den eigenen Destillationsdaten der Brennerei angepasst werden. Die Physik garantiert Dinge wie die Alkoholerhaltung. Die Daten stimmen das Modell auf genau diese Brennblase, ihre Wärmezufuhr und ihren Kondensator ab."
  - q: "Warum driftet ein rein datengetriebener Zwilling einer Brennblase?"
    a: "Ein Machine-Learning-Modell, das nur auf vergangenen Brennläufen trainiert wurde, lernt Korrelationen, keine Gesetze. Es kann Mengen für Vorlauf, Mittellauf und Nachlauf vorhersagen, die zusammen mehr Alkohol ergeben, als eingefüllt wurde, und es weiß nicht, was zu tun ist, wenn Füllstärke oder Wärmezufuhr den Bereich verlassen, auf dem es trainiert wurde. Nichts in seiner Struktur hindert es daran, die Erhaltung zu verletzen."
  - q: "Welche Daten braucht man, um ein hybrides Pot-Still-Modell anzupassen?"
    a: "Für jeden Brennlauf: Füllvolumen und Füllstärke, Wärmezufuhr oder Dampfmenge über die Zeit, Destillatfluss und Destillatstärke am Spirit Safe sowie die Schnittzeitpunkte. Ein paar Dutzend sauber dokumentierte Brennläufe reichen meist aus, um die Handvoll Parameter anzupassen, die ein hybrides Modell braucht, denn die Physik erledigt den Großteil der Arbeit."
---

**Kurze Antwort: Eine Batch-Pot-Still gehorcht zwei Regeln, über die ein Data Scientist nicht verhandeln kann. Die Rayleigh-Gleichung beschreibt, wie sich Blaseninhalt und Dampf im Lauf des Brandes verändern, und der eingefüllte Alkohol muss dem Alkohol entsprechen, den man über Vorlauf, Mittellauf, Nachlauf und Rückstand auffängt. Ein digitaler Zwilling, der nur per Machine Learning aus vergangenen Brennläufen gebaut wurde, kennt keine dieser Regeln. Er driftet, sobald sich die Bedingungen ändern, und kann Fraktionen vorhersagen, die mehr Alkohol enthalten, als hineingegangen ist. Baue den Zwilling andersherum: Physik für die Struktur, Destillationsdaten für einige wenige angepasste Parameter. Er braucht weniger Daten, extrapoliert vernünftig und kann keinen Alkohol erfinden.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 330" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Ein beispielhafter Feinbrand. Eine Füllung von 10.000 Litern Raubrand mit 22 Prozent enthält 2.200 Liter reinen Alkohol. Der hybride Zwilling teilt ihn auf in Vorlauf 60, Mittellauf 1.050, Nachlauf 1.070 und Rückstand 20, zusammen 2.200. Ein reiner ML-Zwilling sagt Vorlauf 60, Mittellauf 1.120, Nachlauf 1.110 und Rückstand 20 voraus, zusammen 2.310, also mehr Alkohol als eingefüllt.">
<rect width="1000" height="330" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">ALKOHOL REIN MUSS GLEICH ALKOHOL RAUS SEIN (BEISPIELLAUF, LITER REINALKOHOL)</text>
<g font-family="sans-serif">
<rect x="40" y="110" width="200" height="90" rx="10" fill="#06483f"/>
<text x="140" y="140" text-anchor="middle" font-size="12" fill="#cfe6df">Füllung</text>
<text x="140" y="166" text-anchor="middle" font-size="20" font-weight="700" fill="#ffffff">2.200 LAA</text>
<text x="140" y="187" text-anchor="middle" font-size="10.5" fill="#cfe6df">10.000 L bei 22%</text>
<line x1="240" y1="155" x2="300" y2="100" stroke="#4db6a2" stroke-width="2"/>
<line x1="240" y1="155" x2="300" y2="220" stroke="#4db6a2" stroke-width="2"/>
<text x="310" y="62" font-size="11" font-weight="700" letter-spacing="1" fill="#2e9e7c">HYBRIDER ZWILLING</text>
<rect x="300" y="72" width="660" height="56" rx="9" fill="#f0f6f5" stroke="#2e9e7c" stroke-width="2"/>
<text x="330" y="106" font-size="12" fill="#06483f">Vorlauf 60 &#183; Mittellauf 1.050 &#183; Nachlauf 1.070 &#183; Rückstand 20</text>
<text x="940" y="106" text-anchor="end" font-size="15" font-weight="700" fill="#2e9e7c">= 2.200 &#10003;</text>
<text x="310" y="172" font-size="11" font-weight="700" letter-spacing="1" fill="#ff4081">REINER ML-ZWILLING</text>
<rect x="300" y="182" width="660" height="56" rx="9" fill="#ffffff" stroke="#ff4081" stroke-width="2"/>
<text x="330" y="216" font-size="12" fill="#06483f">Vorlauf 60 &#183; Mittellauf 1.120 &#183; Nachlauf 1.110 &#183; Rückstand 20</text>
<text x="940" y="216" text-anchor="end" font-size="15" font-weight="700" fill="#ff4081">= 2.310 &#10007;</text>
<rect x="40" y="272" width="920" height="42" rx="10" fill="#06483f"/>
<text x="500" y="298" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">EIN ZWILLING, DER 110 LITER ALKOHOL ERFINDEN KANN, IST KEIN ZWILLING</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Beispielzahlen. Jede Fraktion für sich wirkt plausibel. Erst die Summe verrät den reinen ML-Zwilling.</figcaption>
</figure>

Jede Brennerei, die ein Projekt für einen digitalen Zwilling startet, bekommt denselben Pitch: Füttere ein Modell mit ein paar Jahren Destillationsdaten, und es sagt den Brennlauf voraus. Vorlaufmenge, Mittellaufmenge, Schnittzeitpunkte, alles gelernt. Die Demo auf den Brennläufen des Vorjahres sieht hervorragend aus. Dann kommt eine Füllung, die anderthalb Prozentpunkte stärker ist als üblich, oder die Dampfversorgung ändert sich nach einer Kesselreparatur, und der Zwilling fängt an, Dinge zu sagen, von denen der Brennmeister weiß, dass sie Unsinn sind.

Dies ist der erste Beitrag in **The Still and the Model**, einer Serie über das Data Engineering und die GenAI hinter den Zahlen einer Brennerei. Sie beginnt mit dem Zwilling, denn am Zwilling zeigt sich zuerst die Lücke zwischen einem Modell, das Daten abbildet, und einem Modell, das die Physik respektiert.

## Was eine Pot Still tatsächlich tut

Eine Batch-Pot-Still ist ein Lehrbuchfall, und das Lehrbuch kennt die Antwort seit mehr als einem Jahrhundert. Während die Füllung siedet, ist der Dampf reicher an Alkohol als die Flüssigkeit, die er zurücklässt. Die Blase wird also stetig schwächer, und die Destillatstärke fällt über den Lauf. Lord Rayleigh hat den Zusammenhang 1902 aufgeschrieben: In jedem kleinen Abschnitt des Laufs entspricht der Alkohol, der mit dem Dampf entweicht, dem Alkohol, den die Blase verliert.

Im Code ist ein Schritt davon fast peinlich kurz:

```python
def rayleigh_step(W, x, dW, vle, eff):
    # W: moles in pot, x: alcohol mole fraction in pot, dW: moles boiled off
    y = x + eff * (vle(x) - x)        # vapour composition, eff fitted from runs
    x_new = (W * x - y * dW) / (W - dW)
    return W - dW, x_new, y
```

`vle(x)` ist das Dampf-Flüssigkeits-Gleichgewicht für Ethanol und Wasser, das aus veröffentlichten Daten stammt, nicht aus deinen Brennläufen. `eff` beschreibt, wie nah deine konkrete Brennblase mit ihrem Rücklauf aus dem Hals, dem Winkel des Geistrohrs und ihrem Kondensator an dieses Gleichgewicht herankommt. Und man beachte die eingebaute Erhaltung: Der Alkohol in der Blase vor dem Schritt entspricht dem Alkohol in der Blase danach plus dem Alkohol im Dampf. Das Modell kann das nicht verletzen, weil die Mathematik es nicht zulässt.

Eine echte Brennblase bringt Rücklauf, wechselnde Wärmezufuhr und eine Kupferoberfläche mit, die für das Aroma zählt. Ein Produktionszwilling trägt deshalb ein paar Terme mehr. Die Form bleibt gleich: bekannte Physik und eine Handvoll Parameter, die deine Brennblase beschreiben.

## Warum ein reiner ML-Zwilling driftet

Ein Machine-Learning-Modell, das auf vergangenen Brennläufen trainiert wurde, tut etwas ganz anderes. Es lernt, dass bei den Läufen, die es gesehen hat, eine Füllung wie diese tendenziell einen Mittellauf wie jenen ergeben hat. Das ist eine Korrelation, und Korrelationen haben an einer Brennblase zwei Schwächen.

**Sie erhalten nichts.** Sagt man Vorlauf, Mittellauf und Nachlauf mit drei getrennten Modellen voraus, oder mit einem Modell mit drei Ausgaben, zwingt nichts sie dazu, sich aufzusummieren. Im Beispiellauf oben liegt jede vorhergesagte Fraktion innerhalb ihres historischen Bereichs. Zusammen enthalten sie 110 Liter Reinalkohol, die nie in der Füllung waren. Auf einem Dashboard rechnet das niemand zusammen. Bei einer Abstimmung mit der Zollverwaltung wird es jemand tun.

**Sie extrapolieren nicht.** Die Läufe im Trainingsdatensatz decken die Füllstärken, Wärmezufuhren und Füllmengen ab, die die Brennerei zufällig verwendet hat. Ändert sich einer dieser Werte, rät das Modell. Das physikalische Modell nicht: Der Rayleigh-Gleichung ist es egal, ob die Füllung 21% oder 24% hat, sie rechnet einfach weiter.

Das tiefere Problem ist, dass ein reiner Datenzwilling genau dann an Vertrauenswürdigkeit verliert, wenn man ihn am meisten braucht, nämlich beim ungewöhnlichen Brennlauf.

## Der Hybrid: Physik für die Struktur, Daten für die Parameter

Der Ansatz, der funktioniert, ist ein Hybrid, manchmal Grey-Box-Modellierung genannt. Die Physik gibt die Struktur vor: Massen- und Alkoholbilanzen, Rayleigh, Dampf-Flüssigkeits-Gleichgewicht, eine einfache Wärmebilanz. Destillationsdaten passen die wenigen Zahlen an, die die Physik nicht kennen kann:

- **den Anreicherungswirkungsgrad** dieser Brennblase (`eff` oben),
- **die effektive Wärmezufuhr** für eine bestimmte Dampfventilstellung oder Brennereinstellung,
- **die Verzögerung durch Kondensator und Safe**, also die Zeit zwischen dem Moment, in dem der Dampf die Blase verlässt, und dem Moment, in dem das Destillat das Aräometer erreicht.

Drei oder vier Parameter, angepasst an ein paar Dutzend sauber dokumentierte Brennläufe, bilden eine echte Brennblase in der Regel eng ab. Ein reiner ML-Zwilling braucht innerhalb des Trainingsbereichs weit mehr Läufe für dieselbe Genauigkeit, und außerhalb davon ist er trotzdem verloren.

Machine Learning hat im Hybrid durchaus seinen Platz: bei der Modellierung des Residuums, also der Lücke zwischen dem, was die Physik vorhersagt, und dem, was die Brennblase tatsächlich getan hat. Hat das Residuum ein Muster (es driftet mit der Umgebungstemperatur oder nach jeder CIP-Reinigung), kann ein kleines Modell es lernen. Der Unterschied ist, dass das ML ein solides Modell korrigiert, statt es zu ersetzen.

## Das Data Engineering darunter

Ein Zwilling ist nur so gut wie seine Brennprotokolle, und hier stellen die meisten Brennereien fest, was sie tatsächlich aufgezeichnet haben:

1. **Füllvolumen und Füllstärke, gemessen.** Nicht die geplante Füllung. Die Stärke bei 20 Grad C, von Aräometer oder Dichtemessgerät, aufgezeichnet zusammen mit dem Messgerät.
2. **Wärmezufuhr als Zeitreihe.** Dampfmenge oder Ventilstellung alle paar Sekunden aus dem Historian, nicht ein Sollwert, der auf dem Brennprotokoll notiert ist.
3. **Destillatfluss und Destillatstärke am Spirit Safe.** Genug Messwerte, um die Stärkekurve zu zeichnen, einschließlich der Schnittzeitpunkte und wer sie gesetzt hat.
4. **Jede Fraktion, gemessen.** Mengen und Stärken von Vorlauf, Mittellauf und Nachlauf am Ende des Laufs, damit sich die Alkoholbilanz für jeden Brennlauf prüfen lässt.

Der letzte Punkt liefert einen Datenqualitätstest gratis. Für jeden Brennlauf sollte der Füllalkohol minus der Summe der Fraktionen nahe null liegen. Ein Lauf, der um 5% danebenliegt, ist kein Modellierungsproblem. Es ist ein Problem mit Zähler, Aräometer oder Aufzeichnung, und es sollte behoben werden, bevor dieser Lauf zum Anpassen von irgendetwas verwendet wird. Das [Kellerbuch in der Weinserie]({{ '/de/2026/event-sourced-cellar-records-winery/' | relative_url }}) macht dasselbe Argument für Volumen: Zeichne die Bewegungen auf und lass die Bilanzen sich selbst prüfen.

## Wofür der Zwilling da ist

Mit einem vertrauenswürdigen Zwilling sind die nützlichen Dinge eher bescheiden:

- **Den Brennlauf aus der Füllung prognostizieren:** erwartete Schnittzeitpunkte und Fraktionsmengen, damit Brennmeister und Planer dieselben Zahlen sehen.
- **Eine Änderung zuerst am Modell testen.** Eine andere Füllstärke oder ein anderes Heizprofil lässt sich auf dem Zwilling fahren, bevor es auf der Brennblase läuft.
- **Einen Brennlauf erkennen, der sich nicht so verhält, wie die Physik es verlangt.** Darum geht es im [nächsten Beitrag]({{ '/de/2026/soft-sensors-proactive-bands-spirit-safe/' | relative_url }}).

Was er nicht tut, ist den Schnitt zu wählen. Der Schnitt ist eine sensorische und kommerzielle Entscheidung, die der [Beitrag zu den Schnittpunkten]({{ '/de/2024/predicting-distillation-cut-points-ai/' | relative_url }}) im Detail behandelt. Der Zwilling sagt dir, wohin der Lauf geht. Wo er endet, entscheidet weiterhin der Brennmeister.

## Wo das an Grenzen stößt

**Kongenere sind kein Ethanol.** Rayleigh mit dem Ethanol-Wasser-Gleichgewicht bildet Alkohol gut ab. Ester, höhere Alkohole und die Schwefelverbindungen, die Kupfer entfernt, verhalten sich anders, und genau diese Verbindungen bestimmen das Aroma. Ein Zwilling, der die Stärke abbildet, ist kein Zwilling des Aromas.

**Gleichgewichtsdaten haben Grenzen.** Veröffentlichte Dampf-Flüssigkeits-Daten gelten für reines Ethanol und Wasser. Raubrand enthält weitere flüchtige Stoffe, und ganz am Anfang und Ende eines Laufs ist das einfache Modell am ungenauesten. Passe den Zwilling am mittleren Teil des Laufs an und beurteile ihn dort.

**Angepasste Parameter driften.** Kupfer wird dünner, Heizflächen verschmutzen, ein Kondensator wird ersetzt. Passe die Parameter regelmäßig neu an und beobachte sie über die Zeit. Ein Parameter, der sich stetig bewegt, erzählt dir etwas über die Brennblase, nicht über das Modell.

**Schlechte Protokolle ergeben einen selbstsicheren schlechten Zwilling.** Sind die Füllstärken geplant statt gemessen, passt sich der Zwilling an Fiktion an und meldet sie mit zwei Nachkommastellen.

## Das Fazit

Eine Brennblase ist einer der wenigen Orte in einem Getränkeunternehmen, an dem die Physik vollständig bekannt ist und die Daten lückenhaft sind. Das ist genau das Gegenteil dessen, was reines Machine Learning braucht. Nutze die Physik für die Struktur, damit Alkohol erhalten bleibt und das Modell sich auch bei Läufen vernünftig verhält, die es noch nicht gesehen hat. Nutze die Daten für die wenigen Parameter, die daraus deine Brennblase machen. Das Modell sieht das Brennprotokoll. Der Brennmeister sieht das Kupfer, den Dampf und die ungewöhnliche Füllung. Ein hybrider Zwilling ist die Variante, die beides respektiert.

Zu den Sensoren, die einen Zwilling speisen, siehe [IoT in der Brennerei]({{ '/de/2026/iot-in-the-distillery-sensors-process/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite von The Still and the Model]({{ '/series/still-and-model/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist ein physikbasierter digitaler Zwilling einer Brennblase?**
Ein Modell, dessen Struktur aus der Physik der Destillation stammt, etwa aus der Rayleigh-Gleichung und dem Dampf-Flüssigkeits-Gleichgewicht, und bei dem nur wenige Parameter aus den eigenen Destillationsdaten der Brennerei angepasst werden. Die Physik garantiert Dinge wie die Alkoholerhaltung. Die Daten stimmen das Modell auf genau diese Brennblase, ihre Wärmezufuhr und ihren Kondensator ab.

**Warum driftet ein rein datengetriebener Zwilling einer Brennblase?**
Ein Machine-Learning-Modell, das nur auf vergangenen Brennläufen trainiert wurde, lernt Korrelationen, keine Gesetze. Es kann Mengen für Vorlauf, Mittellauf und Nachlauf vorhersagen, die zusammen mehr Alkohol ergeben, als eingefüllt wurde, und es weiß nicht, was zu tun ist, wenn Füllstärke oder Wärmezufuhr den Bereich verlassen, auf dem es trainiert wurde. Nichts in seiner Struktur hindert es daran, die Erhaltung zu verletzen.

**Welche Daten braucht man, um ein hybrides Pot-Still-Modell anzupassen?**
Für jeden Brennlauf: Füllvolumen und Füllstärke, Wärmezufuhr oder Dampfmenge über die Zeit, Destillatfluss und Destillatstärke am Spirit Safe sowie die Schnittzeitpunkte. Ein paar Dutzend sauber dokumentierte Brennläufe reichen meist aus, um die Handvoll Parameter anzupassen, die ein hybrides Modell braucht, denn die Physik erledigt den Großteil der Arbeit.
