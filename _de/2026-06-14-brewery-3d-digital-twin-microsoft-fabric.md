---
layout: post
lang: de
title: "Ich habe meine Brauerei in einen 3D-Digital-Twin auf Microsoft Fabric verwandelt"
image: /assets/og/brewery-3d-digital-twin-microsoft-fabric.png
description: "Kein Dashboard, das man liest — eine Brauerei, durch die man geht. Wie ich die Ankur Napa Brewing Company als lebendigen 3D-Digital-Twin auf Microsoft Fabric neu gebaut habe, an einem Nachmittag mit dem Rayfin SDK ausgeliefert, mit jedem Tank und POS an Echtzeitdaten angebunden."
date: 2026-06-14 09:00:00 -0700
updated: 2026-06-14
permalink: /de/2026/brewery-3d-digital-twin-microsoft-fabric/
tags: [digital-twin, microsoft-fabric, data-visualization, real-time, brewing]
faq:
  - q: "Was ist ein Brauerei-Digital-Twin?"
    a: "Ein Digital-Twin ist ein lebendiges 3D-Abbild eines physischen Betriebs, das an Echtzeitdaten angebunden ist. Für eine Brauerei heißt das: jeder Tank — Mühle, Heiß- und Kaltwassertank, Maischbottich, Läuterbottich, Sudpfanne, Whirlpool, Plattenwärmetauscher, Gärtanks und Drucktanks — plus Schankraum und Kasse, in 3D modelliert und auf einem Bildschirm überwacht. Statt ein Diagramm über die Brauerei zu lesen, gehst du durch die Brauerei und klickst einen Tank an, um seine Live-Zahlen zu sehen."
  - q: "Kann man eine 3D-Web-App wirklich auf Microsoft Fabric hosten?"
    a: "Ja. Fabric ist vor allem als Analyseplattform bekannt, aber das neue Rayfin SDK ergänzt eine code-first App-Schicht mit verwalteter Datenbank, Authentifizierung und statischem Hosting. Eine mit React und Three.js gebaute 3D-Erfahrung besteht nur aus statischen Frontend-Assets, baut also zu einem Ordner, wird paketiert und mit einem CLI-Befehl auf Fabric ausgeliefert — inklusive Fabric-Governance und Entra-Anmeldung. Es ist nicht dasselbe wie Power BI; es ist eine gehostete Anwendung, die neben deinen Fabric-Daten sitzen kann."
  - q: "Braucht man Monate und ein großes BI-Team dafür?"
    a: "Nein. Die erste lauffähige Version ging an einem Nachmittag von der Idee zur live erreichbaren, unternehmenstauglichen URL, weil das Rayfin SDK Datenbank, Auth und Hosting fertig mitbringt. Die Zeit fließt in das, was wirklich zählt — den Prozess korrekt zu modellieren und zu entscheiden, was jeder Tank zeigen soll — nicht in das Verkabeln der Infrastruktur."
  - q: "Sind die Daten in der Demo echt?"
    a: "In der Demo sind Telemetrie und Verkäufe mit einem sanften Random Walk simuliert, damit der Twin lebendig erkundbar ist. Wichtig ist die Nahtstelle: Es gibt einen einzigen Daten-Hook, den heute die Simulation und morgen ein echtes Fabric-Datenmodell speist — ohne Änderung an der 3D-Schicht. Die Architektur ist echt, auch wo die Zahlen Platzhalter sind."
---

**Kurze Antwort: Ich habe die Ankur Napa Brewing Company (ANBC) als lebendigen, begehbaren 3D-Digital-Twin auf Microsoft Fabric neu gebaut — und der Punkt ist nicht das 3D, und es ist nicht Fabric. Der Punkt ist: Eine Brauerei ist ein Fluss, und ein Dashboard, das ein flaches Diagramm ist, wirft diesen Fluss weg. Also habe ich die echte Anlage modelliert — Mühle zu Maischbottich zu Läuterbottich zu Sudpfanne zu Gärtanks zu Drucktanks bis zur Schankraum-Kasse — jeden Tank angeklickt, um sein Live-Profil zu sehen, und das Ganze an einem Nachmittag mit dem Rayfin SDK ausgeliefert, weil Fabric mir Datenbank, Auth und Hosting geschenkt hat. Die Lektion darunter: Passe das Bild an den Prozess an, und investiere deine Zeit in das Modell, nicht in die Klempnerei.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Von der Brauereihalle zum Digital-Twin: der physische Brauereifluss speist Microsoft Fabric über das Rayfin SDK mit Datenbank, Auth und Hosting, das einen lebendigen 3D-Digital-Twin ausliefert, in dem jeder Tank und jede Kasse für Echtzeit-Einblick anklickbar ist."><rect width="1000" height="320" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">VOM KORN INS GLAS ZU EINEM LIVE-3D-TWIN</text><g font-family="sans-serif"><rect x="40" y="56" width="290" height="216" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="185" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#06483f">DIE BRAUEREIHALLE</text><text x="185" y="104" text-anchor="middle" font-size="10.5" font-style="italic" fill="#06483f">ein Fluss, keine Tabelle</text><text x="185" y="134" text-anchor="middle" font-size="11" fill="#4a6b64">M&#252;hle &#183; HLT &#183; CLT</text><text x="185" y="158" text-anchor="middle" font-size="11" fill="#4a6b64">Maische &#183; L&#228;uter &#183; Sudpfanne</text><text x="185" y="182" text-anchor="middle" font-size="11" fill="#4a6b64">G&#228;rtanks &#183; Drucktanks</text><text x="185" y="206" text-anchor="middle" font-size="11" fill="#4a6b64">Schankraum &amp; POS</text><text x="185" y="244" text-anchor="middle" font-size="11.5" font-weight="700" fill="#00695c">Prozess modellieren</text><rect x="355" y="56" width="290" height="216" rx="10" fill="#06483f"/><text x="500" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#ffffff">MICROSOFT FABRIC</text><text x="500" y="104" text-anchor="middle" font-size="10.5" font-style="italic" fill="#f3c6d3">&#252;ber das Rayfin SDK</text><text x="500" y="134" text-anchor="middle" font-size="11" fill="#cfe6df">verwaltete Datenbank</text><text x="500" y="158" text-anchor="middle" font-size="11" fill="#cfe6df">Entra-Authentifizierung</text><text x="500" y="182" text-anchor="middle" font-size="11" fill="#cfe6df">statisches App-Hosting</text><text x="500" y="206" text-anchor="middle" font-size="11" fill="#cfe6df">Governance inklusive</text><text x="500" y="244" text-anchor="middle" font-size="11.5" font-weight="700" fill="#ffffff">Klempnerei sparen</text><rect x="670" y="56" width="290" height="216" rx="10" fill="#ffffff" stroke="#06483f" stroke-width="1.5"/><text x="815" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#06483f">DER 3D-DIGITAL-TWIN</text><text x="815" y="104" text-anchor="middle" font-size="10.5" font-style="italic" fill="#06483f">begehen, nicht lesen</text><text x="815" y="134" text-anchor="middle" font-size="11" fill="#4a6b64">Tank anklicken f&#252;r Einblick</text><text x="815" y="158" text-anchor="middle" font-size="11" fill="#4a6b64">Maische-, Gravit&#228;ts- &amp; ABV-Kurven</text><text x="815" y="182" text-anchor="middle" font-size="11" fill="#4a6b64">Live-POS: Essen &amp; Bier in &#8377;</text><text x="815" y="206" text-anchor="middle" font-size="11" fill="#4a6b64">animierter Produktfluss</text><text x="815" y="244" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">Entscheidungen zum Sehen</text></g><text x="500" y="300" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">der Wert ist das Modell in der Mitte — das 3D ist nur, wie man es liest</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Der Fluss, der zählt: Prozess modellieren, Fabric trägt die Klempnerei, als begehbaren Ort lesen.</figcaption>
</figure>

## Zuerst ansehen

Hier ist der Twin in Bewegung — ein Rundflug durch die ANBC-Sudhausanlage, hinein in den Schankraum, mit Live-Tankdetails und Kassenzahlen.

<figure style="margin:1.6rem 0;text-align:center">
<div style="position:relative;width:100%;max-width:1000px;margin:0 auto;aspect-ratio:16/9;border-radius:10px;overflow:hidden;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<iframe src="https://www.youtube-nocookie.com/embed/uZ1r0_0EW4Y" title="Ankur Napa Brewing Company — 3D-Digital-Twin auf Microsoft Fabric" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe>
</div>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die Ankur Napa Brewing Company als lebendiger 3D-Digital-Twin auf Microsoft Fabric — vom Korn ins Glas bis zur Schankraum-Kasse. <a href="https://youtu.be/uZ1r0_0EW4Y">Auf YouTube ansehen</a>.</figcaption>
</figure>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Ich habe meine Brauerei in einen 3D-Digital-Twin auf Microsoft Fabric verwandelt",
  "description": "Die Ankur Napa Brewing Company (ANBC) als lebendiger, begehbarer 3D-Digital-Twin auf Microsoft Fabric — vom Korn ins Glas bis zur Schankraum-Kasse, mit anklickbarem Tank-Einblick und Live-Kasse, ausgeliefert mit dem Rayfin SDK.",
  "thumbnailUrl": "https://i.ytimg.com/vi/uZ1r0_0EW4Y/maxresdefault.jpg",
  "uploadDate": "2026-06-14",
  "contentUrl": "https://youtu.be/uZ1r0_0EW4Y",
  "embedUrl": "https://www.youtube-nocookie.com/embed/uZ1r0_0EW4Y"
}
</script>

## Warum ein flaches Dashboard das falsche Bild war

Ich habe Jahre auf einer Sudhausfläche verbracht, und was ein normales Dashboard nie einfängt, ist, dass eine Brauerei ein *Fluss* ist. Heißwasser speist die Maische; die Maische läutert in die Sudpfanne; gekühlte Würze fällt in die Gärtanks; fertiges Bier wandert in Drucktanks, dann in Fässer, dann an drei Hähne, wo es tatsächlich verkauft wird. Ein Raster aus KPIs plattet das alles zu Zahlen, die ihre Geografie verloren haben. Du siehst, dass Gärtank 3 bei 18 °C steht, aber du *siehst* nicht, dass er zwei Schritte stromabwärts der Sudpfanne und einen Schritt stromaufwärts des Drucktanks sitzt, der die belebteste Bar speist.

Das Ziel war also nicht „etwas in 3D machen, weil 3D cool ist". Es war: den Fluss bewahren. Das Bild bauen, das zur tatsächlichen Funktionsweise der Anlage passt, damit die Daten dort landen, wo deine Intuition ohnehin lebt.

## Was tatsächlich im Twin steckt

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/anbc-twin-overview.png' | relative_url }}" alt="Der 3D-Digital-Twin der Ankur Napa Brewing Company: Sudhaustanks links, Schankraum und Kasse rechts, mit einem Head-up-Display, das Umsatz und Live-Verkaufsstellen zeigt." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die ganze Anlage auf einem Bildschirm — Sudhaus, Gärkeller und Schankraum, mit Live-Umsatz und Verkaufsstellen im HUD.</figcaption>
</figure>

Jeder Tank im echten Prozess ist modelliert und anklickbar:

- **Heiße Seite** — Mühle, Heißwassertank (HLT), Kaltwassertank (CLT), Maischbottich, Läuterbottich, Sudpfanne, Whirlpool, Plattenwärmetauscher (PHE).
- **Kalte Seite** — vier zylindrokonische Gärtanks und drei Drucktanks (Bright Beer Tanks).
- **Front of House** — Verpackung und Lager, dann ein voller Schankraum mit drei Barstationen, Kassen, Tischen, Stühlen und einer offenen Küche.

Klicke einen Tank an, und du bekommst das Diagramm, das dieser Tank wirklich verdient: ein **Maische-Rastprofil** für den Maischbottich, **Läuterabfluss** für den Läuterbottich, eine Kurve aus **fallender Stammwürze und steigendem ABV** für einen Gärtank, **Karbonisierung** für einen Drucktank. Klicke eine Bar an, und du bekommst **Live-Kasse** — Essens- und Bierumsatz, pro Station, in Rupien, mit einem Verkaufstrend, der hochtickt, während die Simulation läuft. Sechs Biere, eine Küche mit fünfzig Gerichten, drei Verkaufsstellen, Produkt sichtbar durch die Rohre zwischen den Tanks fließend.

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/img/anbc-twin-taproom-pos.png' | relative_url }}" alt="Die Schankraum-Bar im Twin ausgewählt, mit Bier- und Essensumsatz, verkauften Pints, einem Live-Verkaufsdiagramm und POS-Anzeigen über jeder Barstation." width="100%" style="max-width:1000px;height:auto;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18)">
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die Schankraum-Bar angeklickt: Bier- und Essensumsatz in ₹, ein Live-Verkaufstrend und POS-Anzeigen an jeder Barstation.</figcaption>
</figure>

## Der überraschende Teil: Fabric trug die Klempnerei

Hier hört es auf, ein Hobby-Render zu sein, und wird etwas, das man tatsächlich betreiben würde. Microsoft Fabric ist als Analyseplattform bekannt, aber das neue **Rayfin SDK** ergänzt eine code-first Anwendungsschicht darauf: eine verwaltete Datenbank, Entra-Authentifizierung und statisches App-Hosting. Eine mit React und Three.js gebaute 3D-Erfahrung ist am Ende nur ein Bündel statischer Frontend-Assets — sie baut also zu einem Ordner, wird paketiert und mit einem einzigen Befehl ausgeliefert:

- die App scaffolden, das 3D-Frontend bauen, und
- `rayfin up` — was die Assets baut, paketiert, hochlädt und eine Live-URL zurückgibt.

Von der Idee zur live erreichbaren, unternehmenstauglichen URL war es ein **Nachmittag**, kein monatelanges BI-Projekt — weil ich keine Zeile Auth-, Datenbank- oder Hosting-Code geschrieben habe. Das ist der eigentliche Hebel: Die Zeit floss in das Modellieren des Prozesses und die Entscheidung, was jeder Tank zeigen soll, und genau dort liegt der Wert. Der vollständige Aufbau in Teil 1 ist eine eigene kurze Serie; dies ist das Warum und das Was.

Teil 2 zeigt, wie ich jeden Tank modelliert habe: [Eine Brauerei in 3D modellieren — prozedurale Tanks und Prozessfluss]({{ '/de/2026/brewery-digital-twin-part-2-modeling-vessels/' | relative_url }}).

## Wo das an Grenzen stößt

Die ehrlichen Vorbehalte, weil ein schickes Video sie verbirgt. **Die Demo-Daten sind simuliert** — Telemetrie und Verkäufe sind ein Random Walk, damit der Twin durchklickbar lebt; die Architektur hat einen einzigen Daten-Hook, den ein echtes Fabric-Datenmodell ohne Änderung an der 3D-Schicht ersetzt, aber heute sind die Zahlen Platzhalter, nicht deine SCADA. **3D ist ein Kostenfaktor, keine kostenlose Deko** — die Three.js-Last ist der schwere Teil des Bündels, und ein Twin, der seine Interaktivität nicht verdient, ist nur ein langsames Diagramm; wenn ein Balkendiagramm die Frage beantwortet, liefere das Balkendiagramm. **Ein Modell ist nur so wahr wie seine Verkabelung** — ein an nichts angebundener Twin ist ein Bildschirmschoner, und die unglamouröse Arbeit, jeden Tank zu vermessen und zu verschlagworten, macht aus der Demo ein Instrument. Und **die Anmeldung ist auf der ausgelieferten App echt** — Fabric nutzt Entra-SSO, ein öffentlicher „jeder darf zusehen"-Link braucht also bewusste Überlegung, wen du wirklich hineinlassen willst.

## Fazit

Bau keinen 3D-Twin, weil er beeindruckend aussieht, und greif nicht zu Fabric, weil es auf der Folie steht. Bau das Bild, das zur tatsächlichen Funktionsweise deines Betriebs passt, damit Daten dort landen, wo deine Intuition schon ist — für eine Brauerei ist das vom Korn ins Glas, kein Kachelraster. Lass dann die Plattform die langweilige, kritische Klempnerei tragen, damit deine Zeit ins Modell und in die Bedeutung fließt, nicht in die Infrastruktur. Das 3D ist nur, wie man es liest; Fabric ist nur, was es stützt; die echte Arbeit — und der echte Wert — ist, den Prozess ehrlich zu modellieren und ihn an Zahlen anzubinden, denen du vertraust. Einmal Brauer, immer Brauer: Jetzt brauen die Dashboards unterwegs.

## Häufige Fragen

**Was ist ein Brauerei-Digital-Twin?**
Ein Digital-Twin ist ein lebendiges 3D-Abbild eines physischen Betriebs, das an Echtzeitdaten angebunden ist. Für eine Brauerei heißt das: jeder Tank — Mühle, Heiß- und Kaltwassertank, Maischbottich, Läuterbottich, Sudpfanne, Whirlpool, Plattenwärmetauscher, Gärtanks und Drucktanks — plus Schankraum und Kasse, in 3D modelliert und auf einem Bildschirm überwacht. Statt ein Diagramm über die Brauerei zu lesen, gehst du durch die Brauerei und klickst einen Tank an, um seine Live-Zahlen zu sehen.

**Kann man eine 3D-Web-App wirklich auf Microsoft Fabric hosten?**
Ja. Fabric ist vor allem als Analyseplattform bekannt, aber das neue Rayfin SDK ergänzt eine code-first App-Schicht mit verwalteter Datenbank, Authentifizierung und statischem Hosting. Eine mit React und Three.js gebaute 3D-Erfahrung besteht nur aus statischen Frontend-Assets, baut also zu einem Ordner, wird paketiert und mit einem CLI-Befehl auf Fabric ausgeliefert — inklusive Fabric-Governance und Entra-Anmeldung. Es ist nicht dasselbe wie Power BI; es ist eine gehostete Anwendung, die neben deinen Fabric-Daten sitzen kann.

**Braucht man Monate und ein großes BI-Team dafür?**
Nein. Die erste lauffähige Version ging an einem Nachmittag von der Idee zur live erreichbaren, unternehmenstauglichen URL, weil das Rayfin SDK Datenbank, Auth und Hosting fertig mitbringt. Die Zeit fließt in das, was wirklich zählt — den Prozess korrekt zu modellieren und zu entscheiden, was jeder Tank zeigen soll — nicht in das Verkabeln der Infrastruktur.

**Sind die Daten in der Demo echt?**
In der Demo sind Telemetrie und Verkäufe mit einem sanften Random Walk simuliert, damit der Twin lebendig erkundbar ist. Wichtig ist die Nahtstelle: Es gibt einen einzigen Daten-Hook, den heute die Simulation und morgen ein echtes Fabric-Datenmodell speist — ohne Änderung an der 3D-Schicht. Die Architektur ist echt, auch wo die Zahlen Platzhalter sind.
