---
layout: post
lang: de
title: "Eine Brauerei in 3D modellieren: prozedurale Tanks und Prozessfluss (Teil 2)"
image: /assets/og/brewery-digital-twin-part-2-modeling-vessels.png
description: "Teil 2 des Brauerei-Digital-Twins: wie ich jeden Tank — Maischbottich, Läuterbottich, Sudpfanne, zylindrokonische Gärtanks — aus Code statt in Blender modelliert, die ganze Anlage aus einer einzigen Prozessdatei getrieben und den Fluss zwischen den Tanks animiert habe. Mit einer ehrlichen Einordnung, wann Blender die richtige Wahl ist."
date: 2026-06-14 11:00:00 -0700
updated: 2026-06-14
permalink: /de/2026/brewery-digital-twin-part-2-modeling-vessels/
tags: [digital-twin, microsoft-fabric, threejs, data-visualization, brewing]
faq:
  - q: "Braucht man Blender, um eine Brauerei in 3D zu modellieren?"
    a: "Nein. Sudhaustanks sind größtenteils Zylinder, Kegel und Kuppeln, lassen sich also prozedural im Code mit React Three Fiber und Three.js-Primitiven bauen. Das hält das Bündel winzig, entfernt die Asset-Pipeline und bedeutet, dass die Geometrie von Daten statt von Dateien getrieben wird. Blender verdient seinen Platz, wenn du organische Formen, Markendetails oder fotorealistische Materialien brauchst, die Primitive nicht ausdrücken können — dann exportierst du glTF und lädst es. Für einen Prozess-Twin, bei dem Klarheit über Realismus geht, gewinnt prozedural."
  - q: "Wie lässt man verschiedene Tanks wie verschiedene Gefäße aussehen?"
    a: "Funktionsspezifisches Detail. Ein Maischbottich bekommt ein Rührwerksgetriebe obendrauf, ein Läuterbottich eine Hackwerk-Antriebsbrücke, eine Sudpfanne einen hohen Brüdenkamin, Gärtanks sind zylindrokonisch auf Beinen mit Glykolbändern. Ich habe diese als ein 'Topper'-Feld pro Tank kodiert, sodass die Geometrie dem entspricht, was der Tank tatsächlich tut — man liest das Sudhaus auf einen Blick, ganz ohne Etiketten."
  - q: "Wie wird der Fluss zwischen den Tanks animiert?"
    a: "Jede Verbindung ist eine Kante in einer Datendatei mit einem 'from', einem 'to' und dem, was fließt (Heißwasser, Maische, Würze, Bier). Die 3D-Schicht zeichnet ein Rohr zwischen den beiden Tankpositionen und lässt kleine Partikel daran entlanglaufen, nach Inhalt eingefärbt, indem sie ihre Position im Render-Loop interpoliert. Es liest sich, als bewege sich Produkt physisch durch die Anlage, und ein neues Rohr hinzuzufügen ist eine Zeile Daten, keine neue Geometrie."
  - q: "Warum alles aus einer einzigen Datendatei treiben?"
    a: "Weil ein Digital-Twin nur wartbar ist, wenn das Modell die Quelle der Wahrheit ist. Eine Datei listet jeden Tank — id, Name, Position, Größe, Inhalt, Topper — und jede Flusskante. Die Szene, die Etiketten, die Flussanimation und die Diagramme lesen alle daraus. Ändere die Anlage an einer Stelle, und der ganze Twin aktualisiert sich, was einen wartbaren Twin von einer handplatzierten 3D-Szene unterscheidet, die verrottet."
---

**Kurze Antwort: Jeder Tank im Brauerei-Twin — Maischbottich, Läuterbottich, Sudpfanne, Whirlpool, die zylindrokonischen Gärtanks, die Drucktanks — wurde im Code mit React Three Fiber modelliert, nicht in Blender geformt. Sudhausgerät besteht größtenteils aus Zylindern, Kegeln und Kuppeln, also hält prozedurale Geometrie das Bündel winzig, killt die Asset-Pipeline und macht die Geometrie datengetrieben. Der eigentliche Trick sind nicht die Meshes; es ist, dass eine Datei die ganze Anlage beschreibt — jeden Tank und jede Flusskante — und Szene, Etiketten, fließende Rohre und Diagramme alle daraus lesen. Einmal modellieren, überall rendern. Und ja, es gibt eine klare Linie, ab der Blender das richtige Werkzeug ist — die ziehe ich am Ende ehrlich.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Von Primitiven zur lebendigen Anlage: prozedurale Geometrie (Zylinder, Kegel, Kuppeln plus Funktions-Topper) und eine Prozessdatei aus Tanks und Flusskanten speisen eine React-Three-Fiber-Szene, die Tanks rendert, Produktfluss animiert und Diagramme pro Tank zeichnet."><rect width="1000" height="320" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">EINMAL MODELLIEREN, &#220;BERALL RENDERN</text><g font-family="sans-serif"><rect x="40" y="56" width="290" height="216" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="185" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#06483f">PROZEDURALE GEOMETRIE</text><text x="185" y="104" text-anchor="middle" font-size="10.5" font-style="italic" fill="#06483f">kein Blender, keine Dateien</text><text x="185" y="134" text-anchor="middle" font-size="11" fill="#4a6b64">Zylinder &#183; Kegel &#183; Kuppeln</text><text x="185" y="158" text-anchor="middle" font-size="11" fill="#4a6b64">Beine, Isolierung, Reifenb&#228;nder</text><text x="185" y="182" text-anchor="middle" font-size="11" fill="#4a6b64">Topper: R&#252;hrwerk &#183; Hackwerk &#183; Kamin</text><text x="185" y="206" text-anchor="middle" font-size="11" fill="#4a6b64">winziges B&#252;ndel, sofort geladen</text><text x="185" y="244" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">Form aus Code</text><rect x="355" y="56" width="290" height="216" rx="10" fill="#06483f"/><text x="500" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#ffffff">EINE PROZESSDATEI</text><text x="500" y="104" text-anchor="middle" font-size="10.5" font-style="italic" fill="#f3c6d3">die Quelle der Wahrheit</text><text x="500" y="134" text-anchor="middle" font-size="11" fill="#cfe6df">Tanks: id, Position, Gr&#246;&#223;e</text><text x="500" y="158" text-anchor="middle" font-size="11" fill="#cfe6df">Inhalt &amp; Topper pro Tank</text><text x="500" y="182" text-anchor="middle" font-size="11" fill="#cfe6df">Flusskanten: from &#8594; to</text><text x="500" y="206" text-anchor="middle" font-size="11" fill="#cfe6df">Anlage an einer Stelle &#228;ndern</text><text x="500" y="244" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">Daten treiben alles</text><rect x="670" y="56" width="290" height="216" rx="10" fill="#ffffff" stroke="#06483f" stroke-width="1.5"/><text x="815" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#06483f">DIE LEBENDIGE SZENE</text><text x="815" y="104" text-anchor="middle" font-size="10.5" font-style="italic" fill="#06483f">React Three Fiber</text><text x="815" y="134" text-anchor="middle" font-size="11" fill="#4a6b64">rendert jeden Tank</text><text x="815" y="158" text-anchor="middle" font-size="11" fill="#4a6b64">Flusspartikel nach Inhalt</text><text x="815" y="182" text-anchor="middle" font-size="11" fill="#4a6b64">Klick &#8594; Diagramm pro Tank</text><text x="815" y="206" text-anchor="middle" font-size="11" fill="#4a6b64">Etiketten &amp; Status aus Daten</text><text x="815" y="244" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">eine Anlage zum Lesen</text></g><text x="500" y="300" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">die Datei in der Mitte ist der Twin — Geometrie und Szene sind nur ihr Ausdruck</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Geometrie aus Code, Anlage aus Daten, Szene aus beidem. Ändere eine Datei, und der ganze Twin bewegt sich mit.</figcaption>
</figure>

Dies ist Teil 2 der Serie. [Teil 1]({{ '/de/2026/brewery-3d-digital-twin-microsoft-fabric/' | relative_url }}) behandelte das Warum und das Gerüst — eine Fabric-gehostete App an einem Nachmittag mit dem Rayfin SDK live zu bekommen. Hier bauen wir das, was die Leute tatsächlich ansehen: die Tanks und den Fluss zwischen ihnen.

## Die Entscheidung: die Tanks coden, nicht formen

Der Serien-Teaser sagte „die Tanks in Blender modellieren", und das ist der Instinkt, den jeder hat. Aber sieh dir ein Sudhaus ehrlich an: Ein Maischbottich ist ein Zylinder mit Kuppeldach und einem Motor obendrauf. Ein Gärtank ist ein Zylinder mit einem darunter geschweißten Kegel. Eine Sudpfanne ist ein Zylinder mit einem Kamin. Das sind *Primitive* — und Three.js gibt dir Primitive gratis.

Also ging ich prozedural vor. Jeder Tank ist aus `cylinderGeometry`, `coneGeometry` und einer Halb-`sphereGeometry`-Kuppel gebaut, in React Three Fiber zusammengesetzt. Der Gewinn ist konkret:

- **Keine Asset-Pipeline** — kein glTF-Export, keine Texturdateien, keine Draco-Kompression, nichts mit dem Code synchron zu halten.
- **Ein winziges Bündel** — der schwere Teil der App ist die Three.js-Bibliothek selbst, nicht die Modelle, was zählt, weil das Ganze als statische Assets zu Microsoft Fabric ausgeliefert wird.
- **Datengetriebene Geometrie** — Größe und Form eines Tanks kommen aus Zahlen, dieselbe Komponente rendert also einen gedrungenen Läuterbottich und einen hohen HLT, nur durch andere Argumente.

## Jeden Tank wie sich selbst aussehen lassen

Eine Brauerei, in der jeder Tank ein identischer silberner Zylinder ist, ist nutzlos — man kann sie nicht lesen. Die Lösung ist **funktionsspezifisches Detail**: die Teile, die einem Brauer sagen, was er ansieht.

- **Maischbottich** → ein Rührwerksgetriebe und Antriebsmotor obendrauf.
- **Läuterbottich** → eine Hackwerk-Antriebsbrücke quer über den Tank.
- **Sudpfanne** → ein hoher Brüdenkamin und Kondensator.
- **Whirlpool** → ein kurzer Kamin mit tangentialem Einlaufrohr.
- **Gärtanks** → zylindrokonisch, auf Beinen stehend, mit Glykol-Mantelbändern umwickelt.
- **Drucktanks** → druckkuppelig und schlanker.

Ich habe diese als `topper` pro Tank kodiert, sodass die Geometrie der *Funktion* folgt. Füge den Tanks Beine, Isolierung und Reifenbänder hinzu, und das Sudhaus wird auf einen Blick lesbar — du findest die Sudpfanne an ihrem Kamin, bevor du je ein Etikett liest.

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/anbc-twin-overview.png' | relative_url }}" alt="Das aus Primitiven gerenderte Sudhaus: jeder Tank trägt funktionsspezifisches Detail — Rührwerk, Hackwerksantrieb, Sudpfannenkamin, zylindrokonische Gärtanks auf Beinen — sodass die Tanks auf einen Blick unterscheidbar sind." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">All das sind Zylinder, Kegel und Kuppeln aus Code — die Topper und Proportionen machen jeden Tank lesbar.</figcaption>
</figure>

## Der eigentliche Trick: eine Datei beschreibt die ganze Anlage

Hier ist der Teil, der einen wartbaren Twin von einer 3D-Szene unterscheidet, die verrottet. Es gibt eine einzige Prozessdatei. Sie listet jeden Tank — id, Anzeigename, Position auf dem Boden, Radius, Höhe, was er hält und seinen Topper — und jede **Flusskante**: einen `from`-Tank, einen `to`-Tank und das, was zwischen ihnen fließt (Heißwasser, Schrot, Maische, Würze, Bier).

Alles liest aus dieser Datei:

- die **Szene** platziert jeden Tank an seiner Position,
- die **Etiketten** und Statusringe kommen aus denselben Datensätzen,
- die **Rohre** werden zwischen den `from`- und `to`-Positionen jeder Kante gezeichnet,
- selbst die **Diagramme pro Tank** schlüsseln auf die Tank-id.

Verschiebe einen Tank, benenne ihn um oder füge eine neue Transferleitung hinzu, und du editierst *Daten*, keine Geometrie. Das Modell ist die Quelle der Wahrheit; das 3D ist nur eine Art, es auszudrücken. (Der andere Ausdruck — die Live-Zahlen — kommt in Teil 3.)

## Den Fluss animieren

Eine statische Anlage ist ein Diagramm. Was sie zu einem *Twin* macht, ist zu sehen, wie Produkt sich bewegt. Für jede Flusskante zeichnet die Szene ein dünnes Rohr zwischen den beiden Tanks und lässt ein paar kleine Partikel daran entlanglaufen, **nach Inhalt eingefärbt** — Bernstein für Maische, Gold für Würze, Kupfer für Bier, Blau für Kaltwasser. Der Render-Loop interpoliert die Position jedes Partikels von `from` nach `to` und lässt sie kreisen.

Weil Fluss Daten ist, ist das Hinzufügen eines Transfers — sagen wir, eine neue Leitung von einem Drucktank zu einem vierten Hahn — ein Eintrag in der Kantenliste. Kein neues Mesh, keine manuelle Platzierung. Das Rohr und sein fließendes Produkt erscheinen automatisch.

## Diagramme pro Tank, die zum Prozess passen

Wenn du einen Tank anklickst, bekommst du keine generische Anzeige — du bekommst das Diagramm, das dieser Tank verdient: ein **Maische-Rastprofil** für den Maischbottich, **Läuterabfluss** für den Läuterbottich, eine Kurve aus **fallender Stammwürze und steigendem ABV** für einen Gärtank, **Karbonisierung** für einen Drucktank. Das sind leichte, handgezeichnete SVG-Liniendiagramme statt einer Diagrammbibliothek, aus demselben Grund wie die prozedurale Geometrie — die Last klein und die Kontrolle vollständig halten. Jedes Diagramm ist nur eine Funktion der Tank-id, sodass die richtige Kurve für den richtigen Tank erscheint.

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/anbc-twin-mash-profile.png' | relative_url }}" alt="Der Maischbottich ausgewählt, mit einem Maische-Rastprofil-Diagramm, das Eiweißrast, Verzuckerungsrast und Abmaisch-Rampen zeigt." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Maischbottich ausgewählt: ein Rasttemperaturprofil — Eiweißrast, Verzuckerung, Abmaischen — keine generische Anzeige.</figcaption>
</figure>

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/anbc-twin-fermentation.png' | relative_url }}" alt="Ein Gärtank ausgewählt, der eine Gärkurve mit fallender Stammwürze und steigendem ABV über die Zeit zeigt." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Gärtank ausgewählt: die Stammwürze fällt, während der ABV steigt — das Diagramm, das dieser Tank wirklich verdient.</figcaption>
</figure>

## Wo das an Grenzen stößt

Die ehrlichen Grenzen, denn „einfach coden" ist nicht immer richtig. **Prozedurale Geometrie hat eine Decke** — sie ist perfekt für Zylinder, Kegel und Kuppeln, aber sobald du ein gebrandetes, organisches oder fotorealistisches Asset willst (ein geformtes Logo, ein realistischer Gabelstapler, eine texturierte Backsteinwand), wehren sich Primitive, und **Blender plus glTF-Export ist das richtige Werkzeug**; die Entscheidungsregel ist Realismus-und-Einzigartigkeit gegen Klarheit-und-Gewicht. **Detail kostet Frames** — jedes Bein, Band und jeder Topper ist mehr Mesh zum Zeichnen, bei einer großen Anlage willst du also Instancing oder zusammengeführte Geometrie, bevor die Bildrate leidet; ich habe das noch nicht gebraucht, aber eine Anlage mit 200 Tanks schon. **Ein sauberes Modell kann trotzdem lügen** — Geometrie, die richtig aussieht, sagt nichts darüber, ob sie an echte Daten angebunden ist; ein schöner Twin auf falschen Zahlen ist ein Bildschirmschoner, und genau diese Lücke schließt Teil 3. Und **„datengetrieben" stimmt nur, wenn man diszipliniert ist** — in dem Moment, in dem jemand eine Position in der Szene statt in der Datendatei hartkodiert, bricht das Versprechen der einen Quelle der Wahrheit still.

## Fazit

Greif nicht zu Blender, weil Modellieren „dort" passieren „sollte". Sieh dir an, was du modellierst: Ein Sudhaus sind Primitive, also code die Tanks, gib jedem das Detail, das seine Funktion signalisiert, und — am wichtigsten — treibe die ganze Anlage aus einer einzigen Prozessdatei, damit Szene, Fluss und Diagramme sich mitbewegen, wenn du sie editierst. Reserviere Blender für die Formen, die Primitive wirklich nicht ausdrücken können. Die Geometrie ist der einfache Teil; die Disziplin einer einzigen Quelle der Wahrheit macht einen Twin, den man tatsächlich warten kann. Als Nächstes Teil 3: ihn an Echtzeitdaten und Klartext-Sprache anbinden, damit der Twin aufhört zu simulieren und anfängt zu berichten.

## Häufige Fragen

**Braucht man Blender, um eine Brauerei in 3D zu modellieren?**
Nein. Sudhaustanks sind größtenteils Zylinder, Kegel und Kuppeln, lassen sich also prozedural im Code mit React Three Fiber und Three.js-Primitiven bauen. Das hält das Bündel winzig, entfernt die Asset-Pipeline und bedeutet, dass die Geometrie von Daten statt von Dateien getrieben wird. Blender verdient seinen Platz, wenn du organische Formen, Markendetails oder fotorealistische Materialien brauchst, die Primitive nicht ausdrücken können — dann exportierst du glTF und lädst es. Für einen Prozess-Twin, bei dem Klarheit über Realismus geht, gewinnt prozedural.

**Wie lässt man verschiedene Tanks wie verschiedene Gefäße aussehen?**
Funktionsspezifisches Detail. Ein Maischbottich bekommt ein Rührwerksgetriebe obendrauf, ein Läuterbottich eine Hackwerk-Antriebsbrücke, eine Sudpfanne einen hohen Brüdenkamin, Gärtanks sind zylindrokonisch auf Beinen mit Glykolbändern. Ich habe diese als ein 'Topper'-Feld pro Tank kodiert, sodass die Geometrie dem entspricht, was der Tank tatsächlich tut — man liest das Sudhaus auf einen Blick, ganz ohne Etiketten.

**Wie wird der Fluss zwischen den Tanks animiert?**
Jede Verbindung ist eine Kante in einer Datendatei mit einem 'from', einem 'to' und dem, was fließt (Heißwasser, Maische, Würze, Bier). Die 3D-Schicht zeichnet ein Rohr zwischen den beiden Tankpositionen und lässt kleine Partikel daran entlanglaufen, nach Inhalt eingefärbt, indem sie ihre Position im Render-Loop interpoliert. Es liest sich, als bewege sich Produkt physisch durch die Anlage, und ein neues Rohr hinzuzufügen ist eine Zeile Daten, keine neue Geometrie.

**Warum alles aus einer einzigen Datendatei treiben?**
Weil ein Digital-Twin nur wartbar ist, wenn das Modell die Quelle der Wahrheit ist. Eine Datei listet jeden Tank — id, Name, Position, Größe, Inhalt, Topper — und jede Flusskante. Die Szene, die Etiketten, die Flussanimation und die Diagramme lesen alle daraus. Ändere die Anlage an einer Stelle, und der ganze Twin aktualisiert sich, was einen wartbaren Twin von einer handplatzierten 3D-Szene unterscheidet, die verrottet.
