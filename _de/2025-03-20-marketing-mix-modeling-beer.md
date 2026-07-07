---
layout: post
lang: de
title: "Marketing-Mix-Modeling: Was das Biervolumen wirklich treibt"
image: /assets/og/marketing-mix-modeling-beer.png
description: "Marketing-Mix-Modeling für Biermarken — ein Rahmen, um zu verstehen, welche Ausgaben Volumen treiben und welche nur Rauschen sind."
date: 2025-03-20
updated: 2025-03-20
permalink: /de/2025/marketing-mix-modeling-beer/
tags: [marketing, marketing-analytics, mmm]
faq:
  - q: "Was ist Marketing-Mix-Modeling und warum ist es für Bier wichtig?"
    a: "Marketing-Mix-Modeling (MMM) ist eine statistische Technik, die das Verkaufsvolumen in Beiträge jedes Marketing- und Handelshebels zerlegt — Medienausgaben, Promotions, Distributionsänderungen, Preisgestaltung und externe Faktoren wie Wetter oder Saisonalität. Bei Bier, wo das Volumen je nach Saison und Anlass dramatisch schwankt, ist das Verständnis des wahren Beitrags jedes Hebels entscheidend, um Sommergewinne nicht einer Medienkampagne zuzuschreiben, die lediglich zur gleichen Zeit lief."
  - q: "Wie viele Daten braucht eine Brauerei, um ein Marketing-Mix-Modell zu betreiben?"
    a: "Ein zuverlässiges MMM benötigt in der Regel mindestens zwei bis drei Jahre wöchentlicher Verkaufsdaten neben den entsprechenden Ausgaben-, Preis- und Distributionsaufzeichnungen. Kleinere unabhängige Brauereien mit begrenzten historischen Daten können einfachere regressionsbasierte Versionen betreiben, aber die Konfidenzintervalle weiten sich unterhalb von 18 Monaten Daten erheblich. Jetzt mit der Datenerfassung zu beginnen — auch unvollkommen — ist besser, als auf den idealen Datensatz zu warten."
  - q: "Was ist der größte Fehler, den Brauereien bei der Interpretation von MMM-Ergebnissen machen?"
    a: "Der häufigste Fehler ist, die historischen Koeffizienten des Modells als vorausschauendes Planungswerkzeug zu behandeln, ohne abnehmende Erträge zu berücksichtigen. Ein TV- oder Digitalkanal, der bei einem bestimmten Ausgabenniveau starke Erträge zeigte, wird bei doppelter Investition nicht zwangsläufig denselben Ertrag liefern. Jede MMM-Ausgabe sollte mit einer Response-Curve-Analyse gepaart werden, bevor Budgetentscheidungen getroffen werden."
---

**Kurze Antwort:** Für die meisten Biermarken sind die drei wichtigsten Volumentreiber Distributionsgewinne, die Tiefe der Preispromotion und die saisonale Basislinie — nicht Medien. Marketing-Mix-Modeling macht das sichtbar, sodass Budget zu dem fließen kann, was tatsächlich Produkt bewegt, statt zu dem, was sich in einer Planungspräsentation strategisch anfühlt.

---

Jede Biermarke hat eine Theorie darüber, was Volumen treibt. Vertriebsteams schreiben es ihrer Beziehungsarbeit zu. Markenteams schreiben es der neuesten Kampagne zu. Trade Marketing schreibt es dem Display-Programm zu. Marketing-Mix-Modeling ersetzt diese konkurrierenden Erzählungen durch eine einzige zerlegte Sicht auf den tatsächlichen Beitrag. Das Unbehagen, das es erzeugt, ist in der Regel proportional zu seinem Wert.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Marketing-Mix-Modeling: Was das Biervolumen wirklich treibt</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#06483f">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#4a6b64">den Betrieb ändern</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#06483f"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Was MMM tatsächlich misst

Im Kern ist ein Marketing-Mix-Modell eine multivariate Regression, die den inkrementellen Beitrag jeder Eingangsvariablen zu einer abhängigen Variablen isoliert — typischerweise verkauftes Volumen oder Umsatz. Für eine Biermarke umfassen die Eingangsvariablen typischerweise:

- **Medienausgaben nach Kanal** (Rundfunk, Digital, Out-of-Home, Audio)
- **Handelspromotions** (Tiefe der Preisreduktion, Häufigkeit von Features, Display-Ausgaben)
- **Distribution** (gewichtete oder numerische Distributionsänderungen)
- **Preisgestaltung** (Basispreis und Regalpreis)
- **Externe Variablen** (Temperatur, Sportereignisse, Feiertage, Wettbewerbsaktivität)
- **Basislinie** (das Volumen, das die Marke ganz ohne Marketing verkaufen würde)

Das Modell trennt diese Beiträge statistisch. Die Basislinienzahl — oft 60–75 % des Gesamtvolumens bei etablierten Marken — neigt dazu, Führungskräfte zu überraschen, die glauben, ihre Marke sei stärker marketinggetrieben, als sie es tatsächlich ist.

## Die bierspezifischen Komplikationen

Bier stellt drei Modellierungsherausforderungen dar, die generische MMM-Rahmen untergewichten.

**Die Saisonalität ist extrem.** Ein Warmwetter-Anstieg im Lagervolumen kann jeden Medieneffekt in den Schatten stellen. Wenn das Modell Temperatur und Tageslichtstunden nicht richtig kontrolliert, schreibt es Warmsommergewinne dem zu, was zufällig im zweiten Quartal an Medien lief.

**Distribution treibt überproportionales Volumen.** Den Gewinn oder Verlust eines großen Lebensmittelketten-Accounts oder eines prominenten Zapfhahns kann das Volumen um Vielfache bewegen, die kein Medienbudget erreichen kann. Distribution sollte als separater Hebel modelliert werden, nicht in einen generischen "alles andere"-Term eingebacken.

**Alkoholfreies Bier erfordert ein separates Modell oder ein sorgfältig spezifiziertes Teilmodell.** Käufer alkoholfreien Biers reagieren auf andere Anlässe und Auslöser. Alkoholfreie SKUs in ein Gesamtportfolio-Modell zu werfen, verschleiert die eigene Dynamik des am schnellsten wachsenden Segments. Brauereien mit nennenswertem alkoholfreiem Volumen sollten es separat modellieren oder Subkategorie-Interaktionsterme bauen.

## Die Ausgabe lesen: Drei Fragen, die man stellen sollte

Sobald ein Modell gebaut ist, trennen drei Fragen nützliche Erkenntnis von einem schönen Diagramm, das Staub ansetzt.

**Was ist der marginale ROI meines nächsten Euros je Kanal?** Das Modell erzeugt Response-Curves, die zeigen, wie sich der Ertrag pro Euro mit steigenden Ausgaben verändert. Die meisten Marken entdecken, dass ein oder zwei Kanäle weit über ihrer effizienten Grenze operieren — sie geben in steil abnehmende Erträge hinein aus, ohne es zu wissen.

**Was passiert mit dem Volumen, wenn ich die Promotionstiefe kürze?** Für viele Biermarken sind tiefe Preispromotions der größte einzelne Treiber inkrementellen Volumens — und auch der margenschädlichste. Das Modell kann den Volumen-/Margen-Tradeoff einer 5%igen Reduktion der durchschnittlichen Promotionstiefe quantifizieren.

**Was ist der Halo-Effekt von Markenmedien auf die Handelsperformance?** Manche Medienkanäle treiben Verbraucher in Geschäfte, vorbereitet darauf, auf ein Display zu reagieren. MMM kann diesen Interaktionseffekt schätzen, der routinemäßig unterbewertet wird, wenn Kanäle isoliert beurteilt werden.

## Die Anpassung für Craft-Brauereien

Nationale MMM-Rahmen erfordern Daten in einem Umfang, den viele unabhängige Brauereien nicht erreichen können. Eine praktische Anpassung für regionale und Craft-Betreiber: Betreibe ein vereinfachtes Zwei-Variablen-Modell mit wöchentlichen POS-Scandaten eines wichtigen Handelspartners neben dokumentierten Promotionsdaten und -tiefen. Selbst eine grobe Zerlegung von "Promo-Volumen" gegenüber "Basislinien-Volumen" ist nützlicher als Intuition allein.

Speziell für alkoholfreies Bier ist die Verfolgung des Monat-für-Monat-Basislinientrends besonders wertvoll. Eine steigende Basislinie bei alkoholfrei deutet auf organische Kategorieübernahme hin; eine flache Basislinie trotz starker Promotion zeigt an, dass die Marke Volumen kauft, statt es aufzubauen.

Siehe auch: [Attribution: Ausgaben mit dem Zapfhahn verbinden]({{ '/de/2025/marketing-attribution-beverage/' | relative_url }}) für die Spannung zwischen Last-Touch und Multi-Touch, die MMM auflösen soll.

## Wo dieser Ansatz bricht

MMM ist ein rückblickendes Werkzeug. Es sagt dir, was Volumen in der Vergangenheit getrieben hat, unter vergangenen Wettbewerbsbedingungen, bei vergangenen Ausgabenniveaus. Die Koeffizienten des Modells direkt auf einen Markt mit einem neuen Wettbewerber, einer neuen Distributionsabdeckung oder einem deutlich anderen Verbraucherkontext anzuwenden, birgt das Risiko systematischer Über- oder Unterschätzung. Modelle sollten mindestens jährlich neu geschätzt werden und nach jeder größeren strukturellen Änderung an Marke oder Kategorie.

*Teil des Marketing-Tracks — [alle durchsuchen]({{ '/de/tags/' | relative_url }}#marketing).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">BEITRAG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Marketing-Mix-Modeling: Was das Biervolumen wirklich treibt</text><text x="60" y="109" font-family="sans-serif" font-size="12.5" fill="#06483f">Kanal A</text><rect x="180" y="90" width="300" height="26" rx="4" fill="#00695c"/><text x="60" y="153" font-family="sans-serif" font-size="12.5" fill="#06483f">Kanal B</text><rect x="180" y="134" width="230" height="26" rx="4" fill="#00695c"/><text x="60" y="197" font-family="sans-serif" font-size="12.5" fill="#06483f">Kanal C</text><rect x="180" y="178" width="150" height="26" rx="4" fill="#00695c"/><text x="60" y="241" font-family="sans-serif" font-size="12.5" fill="#06483f">Kanal D</text><rect x="180" y="222" width="90" height="26" rx="4" fill="#00695c"/></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Wie viel jeder Kanal beiträgt — je länger der Balken, desto größer der Effekt.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist Marketing-Mix-Modeling und warum ist es für Bier wichtig?**
Marketing-Mix-Modeling (MMM) ist eine statistische Technik, die das Verkaufsvolumen in Beiträge jedes Marketing- und Handelshebels zerlegt — Medienausgaben, Promotions, Distributionsänderungen, Preisgestaltung und externe Faktoren wie Wetter oder Saisonalität. Bei Bier, wo das Volumen je nach Saison und Anlass dramatisch schwankt, ist das Verständnis des wahren Beitrags jedes Hebels entscheidend, um Sommergewinne nicht einer Medienkampagne zuzuschreiben, die lediglich zur gleichen Zeit lief.

**Wie viele Daten braucht eine Brauerei, um ein Marketing-Mix-Modell zu betreiben?**
Ein zuverlässiges MMM benötigt in der Regel mindestens zwei bis drei Jahre wöchentlicher Verkaufsdaten neben den entsprechenden Ausgaben-, Preis- und Distributionsaufzeichnungen. Kleinere unabhängige Brauereien mit begrenzten historischen Daten können einfachere regressionsbasierte Versionen betreiben, aber die Konfidenzintervalle weiten sich unterhalb von 18 Monaten Daten erheblich. Jetzt mit der Datenerfassung zu beginnen — auch unvollkommen — ist besser, als auf den idealen Datensatz zu warten.

**Was ist der größte Fehler, den Brauereien bei der Interpretation von MMM-Ergebnissen machen?**
Der häufigste Fehler ist, die historischen Koeffizienten des Modells als vorausschauendes Planungswerkzeug zu behandeln, ohne abnehmende Erträge zu berücksichtigen. Ein TV- oder Digitalkanal, der bei einem bestimmten Ausgabenniveau starke Erträge zeigte, wird bei doppelter Investition nicht zwangsläufig denselben Ertrag liefern. Jede MMM-Ausgabe sollte mit einer Response-Curve-Analyse gepaart werden, bevor Budgetentscheidungen getroffen werden.
