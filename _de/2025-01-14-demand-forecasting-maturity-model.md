---
layout: post
lang: de
title: "Das Reifegradmodell für die Getränke-Nachfrageprognose: Von der Tabelle zum ML"
image: /assets/og/demand-forecasting-maturity-model.png
description: "Ein praktisches Reifegradmodell für die Nachfrageprognose von Brauereien und Getränkemarken — von Tabellen bis zum maschinellen Lernen, mit ehrlichen Kompromissen."
date: 2025-01-14
updated: 2025-01-14
permalink: /de/2025/demand-forecasting-maturity-model/
tags: [forecasting, maturity-model]
faq:
  - q: "Was ist ein Reifegradmodell für die Nachfrageprognose?"
    a: "Ein Reifegradmodell beschreibt die Stufen, die ein Unternehmen durchläuft, während sich seine Prognosefähigkeit entwickelt — typischerweise von manuellen Tabellen über statistische Modelle bis zum maschinellen Lernen — wobei jede Stufe bessere Genauigkeit bietet, aber mehr Daten und organisatorische Investitionen erfordert."
  - q: "Ab welcher Stufe sollte eine Brauerei maschinelles Lernen für die Prognose in Betracht ziehen?"
    a: "Die meisten Brauereien profitieren von maschinellem Lernen erst, nachdem sie saubere, konsistente historische Daten auf SKU-Wochen-Ebene, eine funktionierende statistische Basislinie und organisatorische Prozesse haben, um auf die Prognoseausgabe zu reagieren. Der Sprung zu ML, bevor diese Grundlagen existieren, enttäuscht meist."
  - q: "Wie verändert alkoholfreies Bier den Reifegrad-Weg der Prognose?"
    a: "Alkoholfreie SKUs haben oft wenig oder keine Verkaufshistorie, was bedeutet, dass die frühen statistischen Stufen nicht verfügbar sind. Brauereien, die AF-Linien prognostizieren, müssen unabhängig von ihrem allgemeinen Reifegrad analogiebasierte oder Bayes'sche Methoden nutzen."
---

**Kurze Antwort:** Die meisten Getränkeunternehmen befinden sich auf Stufe 1 oder 2 eines vierstufigen Reifegradmodells — reaktive Tabellen oder grundlegende statistische Glättung. Der Wechsel zu Stufe 3 (treiberbasierte Modelle) oder Stufe 4 (ML) liefert messbare Genauigkeitsgewinne, aber nur, wenn die Daten- und organisatorischen Voraussetzungen bereits vorhanden sind. Stufen zu überspringen ist teuer.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Das Reifegradmodell für die Getränke-Nachfrageprognose: Von der Tabelle zum ML</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Daten herein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">die Halle verändern</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Warum Reifegradmodelle bei der Prognose zählen

Nachfrageprognose ist kein einzelnes Werkzeug — sie ist ein Fähigkeitsstapel. Ein Reifegradmodell zwingt kommerzielle und Lieferketten-Verantwortliche, ehrlich darüber zu sein, wo sie tatsächlich stehen, nicht wo sie hinstreben. Es verhindert auch den häufigsten Fehler in der Getränkeplanung: fortschrittliche Software für ein Problem zu kaufen, das noch saubere Daten und einen leistungsfähigen Prozess braucht.

Das untenstehende Modell gilt gleichermaßen für konventionelles Bier und für das rasch wachsende alkoholfreie (AF) Segment, wobei AF auf jeder Stufe einzigartige Komplikationen einführt — mehr dazu weiter unten.

---

## Stufe 1: Reaktive Tabellen

Auf dieser Stufe werden Prognosen erstellt, indem man die Lieferungen des Vorjahres kopiert, nach Bauchgefühl anpasst und per E-Mail verteilt. Genauigkeit wird selten gemessen. Über- und Unterproduktionsentscheidungen werden informell getroffen.

**Typische Indikatoren:** gleitender 12-Monats-Durchschnitt, keine SKU-Granularität, Prognose monatlich fixiert.  
**Obergrenze:** unmöglich, Promotionen, Vertriebsänderungen oder Saisonalität systematisch zu berücksichtigen.

Für alkoholfreies Bier auf Stufe 1 ist die Lage schlimmer: Es gibt kein Vorjahr zum Kopieren, daher ist die Prognose im Wesentlichen ein als Nachfragesignal verkleidetes Verkaufsziel.

---

## Stufe 2: Statistische Basislinien

Stufe 2 führt Zeitreihenmethoden ein — exponentielle Glättung, ARIMA oder einfache saisonale Zerlegung. Diese Modelle sind gut verstanden, schnell auszuführen und bei etablierten SKUs deutlich genauer als Stufe 1.

**Voraussetzungen:** mindestens 24 Monate saubere, wöchentliche Liefer- oder Abverkaufsdaten je SKU.  
**Typische Genauigkeitsverbesserung:** richtungsweisend reduzieren Stufe-2-Modelle den MAPE um 15–25 % gegenüber naiven Basislinien bei reifen SKUs (Ergebnisse variieren erheblich nach Kategorie und Datenqualität).

Das Problem mit alkoholfreiem Bier zeigt sich hier deutlich. Eine vor 18 Monaten eingeführte Marke hat unzureichende Historie für ARIMA. Die richtige Antwort ist ein analogiebasierter Ansatz: Finde drei bis fünf vergleichbare historische Neuprodukteinführungen, indexiere die frühe Entwicklung der AF-SKU gegen diese Analogien und nutze die resultierende Kurve als Prior. Das ist näher an Stufe-3-Denken, angewendet auf Stufe-2-Reife.

---

## Stufe 3: Treiberbasierte Modelle

Stufe 3 bringt externe Signale in die Prognose ein: Promotionskalender, Vertrieb (numerisch oder gewichtet), Wetterindizes, Preisänderungen und makroökonomische Indikatoren. Hier beginnt sich die Prognose eher wie kommerzielle Intelligenz anzufühlen als wie Backoffice-Planung.

Treiberbasierte Modelle können in Regressions-Frameworks oder strukturierteren kausalen Werkzeugen gebaut werden. Die erforderliche Disziplin ist Prozess, nicht Technologie: Promotionspläne müssen genau erfasst und in das Modell eingespeist werden, bevor die Lieferungen anlaufen, nicht im Nachhinein abgeglichen.

Siehe [Promotion-Lift: Echte Nachfrage vom Rabatt-Rauschen trennen]({{ '/de/2025/promotional-lift-forecasting/' | relative_url }}) für eine tiefere Behandlung der Isolierung promotionsgetriebenen Volumens von der Basisnachfrage — ein Stufe-3-Essential.

---

## Stufe 4: Maschinelles Lernen und Ensemble-Methoden

Stufe 4 wendet Gradient-Boosted Trees, neuronale Netze oder Ensemble-Methoden an, die mehrere Modellfamilien verschmelzen. Die Gewinne gegenüber einem gut gebauten Stufe-3-Modell sind real, aber inkrementell — typischerweise einstellige MAPE-Verbesserungen bei gutmütigen SKUs. Der Wert von ML ist am größten in Portfolios mit vielen SKUs, komplexen Wechselwirkungen oder unregelmäßigen Nachfragemustern.

**Nicht-triviale Voraussetzungen:** über 3 Jahre SKU-Wochen-Daten, Feature-Engineering-Pipelines, MLOps-Infrastruktur und — entscheidend — kommerzielle Nutzer, die verstehen, was das Modell kann und was nicht.

AF-Bier-SKUs qualifizieren sich beim Start selten für Stufe 4. Ein realistischer Weg ist, neue Produkte durch eine analogiebasierte oder Bayes'sche Methode zu leiten, bis sich 18–24 Monate Historie ansammeln, und sie dann in die breitere ML-Pipeline zu überführen.

---

## Der ehrliche Vorbehalt

Reifegradmodelle können Organisationen dazu verleiten zu glauben, Fortschritt sei gleichbedeutend mit Genauigkeit. Das ist er nicht automatisch. Eine saubere Stufe-2-Umsetzung übertrifft oft eine schlecht geführte Stufe-4-Umsetzung. Bevor du in neue Werkzeuge investierst, prüfe Datenqualität, Prozessdisziplin und Prognosenutzung — die drei Hebel, die am häufigsten erklären, warum Prognosen ignoriert werden, selbst wenn sie technisch solide sind.

Für das vollständige Bild dessen, was KI-gestützte Prognose liefern kann und nicht kann, siehe [KI-Nachfrageprognose für Brauereien]({{ '/de/2026/ai-demand-forecasting-for-breweries/' | relative_url }}).

*Teil des Tracks Sales Forecasting — [alle durchsuchen]({{ '/de/tags/' | relative_url }}#forecasting).*

---

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">PROGNOSE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Das Reifegradmodell für die Getränke-Nachfrageprognose: Von der Tabelle zum ML</text><g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#b45309" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#b45309" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#7a1f3d" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">heute</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Historie</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">Prognose</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist ein Reifegradmodell für die Nachfrageprognose?**  
Ein Reifegradmodell beschreibt die Stufen, die ein Unternehmen durchläuft, während sich seine Prognosefähigkeit entwickelt — typischerweise von manuellen Tabellen über statistische Modelle bis zum maschinellen Lernen — wobei jede Stufe bessere Genauigkeit bietet, aber mehr Daten und organisatorische Investitionen erfordert.

**Ab welcher Stufe sollte eine Brauerei maschinelles Lernen für die Prognose in Betracht ziehen?**  
Die meisten Brauereien profitieren von maschinellem Lernen erst, nachdem sie saubere, konsistente historische Daten auf SKU-Wochen-Ebene, eine funktionierende statistische Basislinie und organisatorische Prozesse haben, um auf die Prognoseausgabe zu reagieren. Der Sprung zu ML, bevor diese Grundlagen existieren, enttäuscht meist.

**Wie verändert alkoholfreies Bier den Reifegrad-Weg der Prognose?**  
Alkoholfreie SKUs haben oft wenig oder keine Verkaufshistorie, was bedeutet, dass die frühen statistischen Stufen nicht verfügbar sind. Brauereien, die AF-Linien prognostizieren, müssen unabhängig von ihrem allgemeinen Reifegrad analogiebasierte oder Bayes'sche Methoden nutzen.
