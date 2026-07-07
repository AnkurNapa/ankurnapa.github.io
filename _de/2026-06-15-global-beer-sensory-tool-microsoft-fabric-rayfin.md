---
layout: post
lang: de
title: "Ich habe ein globales Bier-Sensorik-Tool auf Microsoft Fabric gebaut (mit Rayfin)"
image: /assets/og/global-beer-sensory-tool-microsoft-fabric-rayfin.png
description: "Ein funktionierendes Tool, in dem die Verkoster von Brauereien Sensorik-Feedback teilen und alle sehen, wie weit jede Charge vom Welt-Ideal ihres Stils abweicht. Gebaut auf Microsoft Fabric, mit einem Backend, das per Rayfin in einem einzigen Befehl ausgeliefert wird."
date: 2026-06-15 10:30:00 -0700
updated: 2026-06-15
permalink: /de/2026/global-beer-sensory-tool-microsoft-fabric-rayfin/
tags: [microsoft-fabric, sensory-analysis, rayfin, data-visualization, brewing]
faq:
  - q: "Was ist ein Tool für sensorische Abweichung bei Bier?"
    a: "Es ist ein Analyse-Tool, das jede Bier-Charge über einen festen Satz von Geschmacksachsen bewertet (süß, bitter, Hopfen, röstig, Körper und so weiter) und misst, wie weit diese Charge vom vereinbarten 'Ideal'-Profil ihres Stils abweicht. Die Abweichungszahl zeigt einem Brauer auf einen Blick, ob eine Charge stilgerecht ist oder wegdriftet, und das Netzdiagramm zeigt genau, welche Aromen daneben liegen."
  - q: "Was ist Rayfin und wie hängt es mit Microsoft Fabric zusammen?"
    a: "Rayfin ist Microsofts Open-Source-SDK und -CLI, vorgestellt auf der Build 2026, mit dem man ein Anwendungs-Backend (Datenmodelle, APIs, Authentifizierung, Zugriffsregeln) in TypeScript definiert und mit einem einzigen Befehl (npx rayfin up) direkt auf Microsoft Fabric ausliefert. Es stellt Datenbank, GraphQL-API, Entra-Anmeldung und Row-Level-Security als verwaltetes Fabric-Element mit direktem Zugriff auf OneLake bereit, sodass App und Analytik auf derselben Plattform leben."
  - q: "Kann eine Brauerei das mit eigenen Verkostungsdaten nutzen?"
    a: "Ja, genau darum geht es. Das Tool nutzt für die Demo einen synthetischen globalen Datensatz, aber das 16-Achsen-Modell und die Abweichungsrechnung funktionieren mit beliebigen Panel-Daten. Eine Brauerei landet ihre eigenen Verkostungswerte in OneLake, richtet das semantische Modell darauf aus und erhält dieselben Abweichungs-Einblicke für ihre Produkte, während Row-Level-Security die Rohdaten jeder Brauerei privat hält."
---

**Kurze Antwort: Ich habe ein funktionierendes globales Bier-Sensorik-Tool gebaut. Die Verkoster von Brauereien geben Geschmackswerte ein, und alle sehen, wie weit jede Charge vom Welt-„Ideal" ihres Stils abweicht. Es läuft auf Microsoft Fabric, und das gesamte Backend (Datenbank, API, Anmeldung, Row-Level-Security, Hosting) wurde mit einem einzigen Befehl per Rayfin ausgeliefert, dem neuen Fabric-Apps-SDK von Microsoft aus der Build 2026. Das Interessante sind nicht die Netzdiagramme; es ist, dass die operative App und das Analysemodell auf derselben Plattform sitzen und ein einziges 16-Achsen-Sensorikmodell teilen, sodass „Was hält die Welt von diesem Stil" und „Ist meine Charge in der Spur" aus denselben Zahlen beantwortet werden.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 300" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wie das globale Sensorik-Tool funktioniert: Verkoster überall geben Geschmackswerte ein, Microsoft Fabric speichert und liefert sie aus, und das Ergebnis ist eine Abweichungs-Erkenntnis, die zeigt, wie weit jede Charge vom Stil-Ideal driftet."><rect width="1000" height="300" fill="#ffffff"/><text x="500" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">GLOBALE BIER-SENSORIK: VOM GAUMEN ZUR ERKENNTNIS</text><g font-family="sans-serif"><rect x="40" y="70" width="250" height="170" rx="10" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="165" y="100" text-anchor="middle" font-size="13" font-weight="700" fill="#06483f">VERKOSTER, &#220;BERALL</text><text x="165" y="130" text-anchor="middle" font-size="11" fill="#4a6b64">bewerten 16 Geschmacksachsen</text><text x="165" y="152" text-anchor="middle" font-size="11" fill="#4a6b64">pro Charge, pro Brauerei</text><text x="165" y="184" text-anchor="middle" font-size="11" fill="#4a6b64">1.828 Verkostungen</text><text x="165" y="206" text-anchor="middle" font-size="11" fill="#4a6b64">29.248 Sensorik-Werte</text><rect x="375" y="70" width="250" height="170" rx="10" fill="#06483f"/><text x="500" y="100" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">MICROSOFT FABRIC</text><text x="500" y="130" text-anchor="middle" font-size="11" fill="#cfe6df">OneLake + semantisches Modell</text><text x="500" y="152" text-anchor="middle" font-size="11" fill="#cfe6df">Rayfin-App: SQL + GraphQL</text><text x="500" y="174" text-anchor="middle" font-size="11" fill="#cfe6df">Entra SSO + Row-Level-Security</text><text x="500" y="206" text-anchor="middle" font-size="11" fill="#cfe6df">ein Befehl zum Ausliefern</text><rect x="710" y="70" width="250" height="170" rx="10" fill="#06483f"/><text x="835" y="100" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">DIE ERKENNTNIS</text><text x="835" y="130" text-anchor="middle" font-size="11" fill="#cfe6df">Abweichung vom Stil-Ideal</text><text x="835" y="152" text-anchor="middle" font-size="11" fill="#cfe6df">Charge vs. Welt-Durchschnitt</text><text x="835" y="174" text-anchor="middle" font-size="11" fill="#cfe6df">QC-Wachliste + Perzentil</text><text x="835" y="206" text-anchor="middle" font-size="11" fill="#cfe6df">welches Aroma daneben liegt, und wie weit</text><text x="320" y="160" text-anchor="middle" font-size="20" fill="#00695c">&#8594;</text><text x="655" y="160" text-anchor="middle" font-size="20" fill="#00695c">&#8594;</text></g><text x="500" y="282" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#4a6b64">App und Analytik teilen ein 16-Achsen-Modell auf einer Plattform; dieselben Zahlen beantworten beide Fragen</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Verkoster-Feedback rein, Abweichungs-Erkenntnis raus, mit Fabric als Speicher, Governance und Auslieferung dazwischen.</figcaption>
</figure>

Ich habe darüber geschrieben, Brauereibetriebe auf Microsoft Fabric zu bringen: den [3D-Brauerei-Digital-Twin]({{ '/de/2026/brewery-3d-digital-twin-microsoft-fabric/' | relative_url }}) und das [Modellieren der Tanks]({{ '/de/2026/brewery-digital-twin-part-2-modeling-vessels/' | relative_url }}). Hier geht es um die andere Hälfte der Qualität: nicht um Tanks und Temperaturen, sondern um den *Geschmack*. Hier ist, was ich gebaut habe, was es zeigt und wie man es tatsächlich nutzt.

## Was es ist

Jede Verkostung im Tool bewertet ein Bier auf **16 Geschmacksachsen** (süß, sauer, bitter, umami, fruchtig, blumig, röstig, Hopfen, Malz, Karamell, Hefe, Körper und ein paar mehr), jeweils von 0 bis 100. Für jeden Stil gibt es ein vereinbartes **„Ideal"-Profil**: wie ein Doppelbock oder ein New England IPA schmecken *soll*. Die eine Zahl, die zählt, ist die **Abweichung**: der durchschnittliche Abstand zwischen dem gemessenen Profil einer Charge und ihrem Stil-Ideal. Niedrige Abweichung heißt stilgerecht; hohe Abweichung heißt, die Charge driftet, und das Netzdiagramm zeigt genau, welche Aromen sie weggezogen haben.

Der Startbildschirm ist eine globale Rangliste. Zwölf Brauereien, sechsunddreißig Produkte, jede Charge danach sortiert, wie weit sie abweicht, mit einer Wachliste, die die schlimmsten Ausreißer weltweit markiert.

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/sensory/global-overview.png' | relative_url }}" alt="Die Übersicht des globalen Sensorik-Tools: ein Kopf mit Summen (12 Brauereien, 36 Produkte, 181 Chargen, 60 Verkoster, 1.828 Verkostungen, 29.248 Werte), Filter für Region, Stil und Brauerei, eine Abweichungs-Wachliste und eine nach sensorischer Abweichung sortierte Produkttabelle." style="width:100%;max-width:900px;height:auto;border:1px solid #dcede8;border-radius:8px"/>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Die globale Ansicht: nach Region, Stil oder Brauerei filtern und dann jedes Produkt danach sortieren, wie weit es vom Stil abweicht.</figcaption>
</figure>

## Wie man es nutzt

Wähle ein Produkt, und du bekommst die Diagnose. Das Netzdiagramm legt drei Dinge übereinander: die **betrachtete Charge** (durchgezogen), das **Stil-Ideal**, an dem sie gemessen wird (rot gestrichelt), und den **Welt-Durchschnitt** für diesen Stil (grau gepunktet). Wo die durchgezogene Linie über die gestrichelte hinausragt, ist dieses Aroma zu stark; wo sie einsinkt, ist es zu schwach. Ein Brauer liest das in etwa drei Sekunden, viel schneller als eine Tabelle mit sechzehn Zahlen.

<figure style="margin:1.6rem 0;text-align:center">
<img src="{{ '/assets/sensory/global-deviation-detail.png' | relative_url }}" alt="Eine Produkt-Detailansicht: Chargen-Kennzahlen (wahrgenommene Qualität, Bewertungen, Abweichung, Datum) neben einem Netzdiagramm, das das Chargenprofil gegen das Stil-Ideal und den weltweiten Stil-Durchschnitt über alle 16 Geschmacksachsen legt." style="width:100%;max-width:900px;height:auto;border:1px solid #dcede8;border-radius:8px"/>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Eine Charge, diagnostiziert: durchgezogen ist diese Charge, rot gestrichelt das Stil-Ideal, grau gepunktet, wie der Rest der Welt diesen Stil schmeckt.</figcaption>
</figure>

Dasselbe 16-Achsen-Modell treibt auch eine brauerseitige Produzentenansicht: zwei der eigenen Produkte nebeneinander, oder ein einzelnes Produkt gegen die Welt. Das Netzdiagramm ist die Lingua franca der Sensorik-Arbeit, und alle Ansichten auf denselben Achsen zu halten ist das, was „deine Charge" und „die Welt" direkt vergleichbar macht.

## Der wirklich neue Teil: Rayfin

Die Diagramme sind der einfache Teil. Interessant ist, wie es gehostet wird. Auf der Build 2026 hat Microsoft **Rayfin** veröffentlicht, ein Open-Source-SDK und -CLI für [Fabric Apps](https://learn.microsoft.com/fabric/apps/overview). Du beschreibst dein Backend in TypeScript (die Datenmodelle, wer was lesen darf), und ein Befehl stellt alles davon auf Microsoft Fabric bereit.

Mein gesamtes Datenmodell besteht aus einer Handvoll dekorierter TypeScript-Klassen:

```ts
@entity()
@role('authenticated', '*')
export class FlavorScore {
  @uuid() id!: string;
  @one(() => Tasting) tasting!: Tasting;
  @text({ max: 16 }) axis!: string;
  @int() score!: number;          // 0 bis 100
}
```

Dann:

```bash
npx rayfin up
```

Dieser eine Befehl hat eine SQL-Datenbank erstellt, eine GraphQL-API generiert, Entra-Single-Sign-on verkabelt, Row-Level-Security angewandt und das Frontend gehostet, alles als verwaltetes Fabric-Element mit direktem Zugriff auf OneLake. Kein Portal-Klicken, keine Infrastruktur-Tickets. Die App ging in deutlich unter einer Minute unter einer `fabricapps.net`-URL live. Das ist derselbe Instinkt wie hinter der [Digital-Twin-Arbeit]({{ '/de/2026/brewery-3d-digital-twin-microsoft-fabric/' | relative_url }}): App und Analytik auf einer Plattform halten, damit die Daten zum Vertrauen nie kopiert werden müssen.

Warum das gerade für Sensorikdaten zählt: Row-Level-Security heißt, jede Brauerei sieht nur ihre eigenen Roh-Verkostungswerte, während alle weiterhin den anonymisierten globalen Benchmark sehen. Genau dieses Vertrauensmodell braucht eine geteilte, brauereiübergreifende Sensorik-Datenbank: privat, wo es muss, gemeinschaftlich, wo es hilft.

## Wo das bricht

Die ehrlichen Vorbehalte, denn die Demo ist hübscher als die Realität. **Die Daten sind synthetisch.** Ich habe zwölf Brauereien und ~29.000 Werte mit festem Seed erzeugt, damit die Abweichungsanalytik Signal hat; echte Panel-Daten sind unordentlicher, dünner und voller Verkoster, die sich uneinig sind. **Ein „Stil-Ideal" ist eine Meinung, kein Gesetz.** Jemand muss entscheiden, wie ein Doppelbock schmecken soll, und diese Zahl ist eine Ermessensfrage, über die man streiten wird; das Tool macht den Streit sichtbar, es entscheidet ihn nicht. **Abweichung markiert Unterschied, nicht Schlechtigkeit.** Eine Charge kann absichtlich vom Stil-Ideal abweichen und trotzdem ein großartiges Bier sein, also ist die Zahl ein Anstoß zu verkosten, nie ein Urteil. **Verkoster sind Messinstrumente, die driften.** Ohne Kalibrierung kann „Abweichung" die Inkonsistenz deines Panels messen statt deines Biers; das Modell verfolgt die Verkoster-Zuverlässigkeit genau deshalb, aber handeln musst du trotzdem. Und **Fabric Apps ist Preview.** Rayfin ist neu, nach dem Ausliefern nur Entra-SSO, und nicht der Ort, an den man regulierte Daten ohne das Kleingedruckte legt.

## Das Fazit

Ein globales Bier-Sensorik-Tool ist nicht wegen der Mathematik schwer; der durchschnittliche Abstand von einem Ideal ist Arithmetik. Es ist schwer, weil es einen vertrauenswürdigen Ort braucht, an dem viele Brauereien sensible Geschmacksdaten zusammenlegen können: privat, wo es zählt, und mit einem geteilten Benchmark, wo es hilft. Das waren früher Wochen an Backend-Klempnerei. Mit Rayfin auf Microsoft Fabric war es ein Befehl, und das Ergebnis sitzt auf derselben Plattform wie die Analytik und teilt ein Sensorikmodell. Das Netzdiagramm sagt einem Brauer, welches Aroma daneben liegt und wie weit; die Plattform macht es sicher, diese Frage über die ganze Branche auf einmal zu stellen. Wenn du darauf hinarbeitest, fang dort an, wo ich immer sage, bei [einem Datenfundament, dem du vertraust]({{ '/de/2024/building-brewery-data-foundation-ai/' | relative_url }}), und lass die Sensorik-Schicht dann auf Zahlen sitzen, die schon sauber sind.

## Häufig gestellte Fragen

**Was ist ein Tool für sensorische Abweichung bei Bier?**
Es ist ein Analyse-Tool, das jede Bier-Charge über einen festen Satz von Geschmacksachsen bewertet (süß, bitter, Hopfen, röstig, Körper und so weiter) und misst, wie weit diese Charge vom vereinbarten „Ideal"-Profil ihres Stils abweicht. Die Abweichungszahl zeigt einem Brauer auf einen Blick, ob eine Charge stilgerecht ist oder wegdriftet, und das Netzdiagramm zeigt genau, welche Aromen daneben liegen.

**Was ist Rayfin und wie hängt es mit Microsoft Fabric zusammen?**
Rayfin ist Microsofts Open-Source-SDK und -CLI, vorgestellt auf der Build 2026, mit dem man ein Anwendungs-Backend (Datenmodelle, APIs, Authentifizierung, Zugriffsregeln) in TypeScript definiert und mit einem einzigen Befehl (`npx rayfin up`) direkt auf Microsoft Fabric ausliefert. Es stellt Datenbank, GraphQL-API, Entra-Anmeldung und Row-Level-Security als verwaltetes Fabric-Element mit direktem Zugriff auf OneLake bereit, sodass App und Analytik auf derselben Plattform leben.

**Kann eine Brauerei das mit eigenen Verkostungsdaten nutzen?**
Ja, genau darum geht es. Das Tool nutzt für die Demo einen synthetischen globalen Datensatz, aber das 16-Achsen-Modell und die Abweichungsrechnung funktionieren mit beliebigen Panel-Daten. Eine Brauerei landet ihre eigenen Verkostungswerte in OneLake, richtet das semantische Modell darauf aus und erhält dieselben Abweichungs-Einblicke für ihre Produkte, während Row-Level-Security die Rohdaten jeder Brauerei privat hält.
