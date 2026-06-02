---
layout: post
lang: de
title: "Eine Führungs-KPI-Scorecard für eine Brauerei in Tableau"
image: /assets/og/tableau-executive-kpi-scorecard.png
description: "Baue eine einseitige Führungs-Scorecard in Tableau mit BANs, Sparklines und RAG-Status über Volumen, Marge, Ausbeute, OEE, Sicherheit und ESG, wöchentlich von Pulse geliefert."
date: 2023-10-21
updated: 2023-10-21
permalink: /de/2023/tableau-executive-kpi-scorecard/
tags: [commercial-planning, tableau, analytics]
faq:
  - q: "Was ist ein BAN in Tableau und warum auf einer Scorecard verwenden?"
    a: "Ein BAN ist eine Big Aggregate Number, eine große Einzelzahl wie das Monatsvolumen oder die Marge. Auf einer Führungs-Scorecard lässt sie eine Führungskraft die Kernaussage in Sekunden lesen, mit einer Sparkline darunter für den Trendkontext."
  - q: "Wie viele KPIs sollte eine Führungs-Scorecard haben?"
    a: "Wenige. Strebe sechs bis neun Schlüsselkennzahlen an, die ein CEO in unter einer Minute erfassen kann. Eine mit dreißig Kennzahlen überladene Scorecard ist ein Bericht, keine Scorecard, und sie wird nicht gelesen."
  - q: "Kann Tableau Pulse das wöchentliche Führungsmeeting ersetzen?"
    a: "Nein. Pulse kann einen wöchentlichen Überblick liefern und markieren, was sich bewegt hat, aber im Meeting findet das Urteilsvermögen statt. Der Überblick bereitet das Gespräch vor; er trifft nicht die Entscheidungen."
---

**Kurze Antwort: Eine Führungs-Scorecard ist eine Erklärung von Prioritäten, daher liegt die Gefahr nicht darin, sie schlecht zu bauen, sondern die falschen KPIs zu wählen und das Geschäft danach zu steuern.** Triff die Kennzahlenauswahl richtig, und das Tableau-Handwerk ist der einfache Teil.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Typisches Dashboard-Layout für „Eine Führungs-KPI-Scorecard für eine Brauerei in Tableau"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DASHBOARD-LAYOUT</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Eine Führungs-KPI-Scorecard für eine Brauerei in Tableau</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">Filter:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Trend</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">Aufschlüsselung</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein typisches Layout für dieses Dashboard: Schlüsselkennzahlen oben, ein Trend und eine Aufschlüsselung darunter, Filter zum Eingrenzen.</figcaption>
</figure>

## Wähle die sechs Zahlen, die die Brauerei steuern
Eine Scorecard ist eine erzwingende Funktion: Jede Kennzahl, die du darauf setzt, sagt der Organisation, was der Führung wichtig ist, und alles, was du weglässt, sagt das Gegenteil. Für einen Brauereieigentümer umfasst ein vertretbarer Satz die Wertschöpfungskette: Volumen (kaufmännisch), Bruttomarge (finanziell), Sudhausausbeute und OEE (betriebliche Effizienz), eine Sicherheitsrate und eine ESG-Intensitätskennzahl wie das Wasser-zu-Bier-Verhältnis. Das sind sechs Zahlen, die Wachstum, Profit, Produktivität, Menschen und Planet abdecken. Die Data-Science-Disziplin liegt hier darin, dem Drang zu widerstehen, eine siebte, dann eine achte hinzuzufügen; jede Ergänzung verwässert das Signal. Erst messen, dann gestalten.

## Bau es: BANs, Sparklines und RAG
Die visuelle Grammatik einer Führungs-Scorecard ist bewusst karg. Jeder KPI erhält ein BAN (Big Aggregate Number) für den aktuellen Wert, eine Sparkline darunter für den Trend und einen RAG-Status — rot, gelb, grün — gegen das Ziel. Baue RAG als berechnetes Feld, das den Ist-Wert mit einer Zielreferenz vergleicht und einen Status zurückgibt, der die Farbe steuert. Halte die Farblogik ehrlich: Gelb sollte Gelb bedeuten, nicht „ein Grün, über das wir lieber nicht sprechen würden".

Sparklines sind minimalistische Liniendiagramme, bei denen Achsen und Beschriftungen entfernt sind, dimensioniert, um in eine Kachel zu passen. Verwende einen Parameter, um die Vergleichsbasis zu wechseln — gegen Ziel, gegen Vorjahr, gegen Plan —, sodass dieselbe Scorecard verschiedene Führungsfragen ohne drei separate Dashboards beantwortet. LOD-Ausdrücke halten jeden KPI auf der richtigen Granularität, während die Seite zu einer Unternehmensansicht aufrollt; eine FIXED-Berechnung etwa hält das Jahresziel stabil, unabhängig vom anderswo angewendeten Datumsfilter.

Der ganze Sinn ist eine Seite. Wenn eine Führungskraft scrollen oder durch Tabs klicken muss, ist es keine Scorecard. Lass dann Tableau Pulse die Verteilung übernehmen: Konfiguriere es, die Schlüssel-KPIs zu überwachen und einen wöchentlichen Überblick in natürlicher Sprache an den Führungsposteingang zu liefern — „Marge um 1,2 Punkte gestiegen, OEE bei Standort C gesunken". Das verwandelt eine statische Seite in eine proaktive wöchentliche Lektüre und bedeutet, dass das Montagsmeeting von einem gemeinsamen, aktuellen Bild ausgeht.

## Wo es scheitert: Die Scorecard spiegelt deine Prioritäten
Die ehrliche Grenze ist unbequem: Eine Scorecard kann dir nicht sagen, ob du die richtigen Dinge misst. Wenn du Volumen wählst und den Mix ignorierst, jagt die Führung Kisten auf Kosten der Marge, und die Scorecard leuchtet grün, während der Profit erodiert. Goodharts Gesetz beißt hier hart zu: Sobald eine Zahl zum Ziel wird, optimieren Menschen die Zahl statt der zugrunde liegenden Realität. Das Diagramm ist treu; die in der Kennzahlenwahl eingebettete Strategie ist es möglicherweise nicht.

Generative KI verschärft die Falle. Ein Pulse-Überblick ist flüssig und autoritativ, und eine selbstbewusste wöchentliche Erzählung kann Führungskräfte dazu verleiten, nach Überblick statt nach Urteilsvermögen zu regieren. Der Überblick kennt deinen Wettbewerbskontext nicht, deine Covenant-Beschränkungen oder das Gespräch, das du letzte Woche mit einem Schlüsselkunden hattest. Behalte das wöchentliche Meeting als den Ort, an dem Menschen die Zahlen hinterfragen, und überdenke den KPI-Satz selbst mindestens jährlich, denn die richtigen sechs Zahlen für dieses Jahr sind nicht automatisch die richtigen für das nächste.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall ist."><rect x="0" y="0" width="720" height="310" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Eine Führungs-KPI-Scorecard für eine Brauerei in Tableau</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#b45309" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reichweite · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#b45309" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interesse · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#b45309" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Probe · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#b45309" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Gewinn · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall ist.</figcaption>
</figure>

## Das Fazit
Baue die Scorecard um sechs bis neun wirklich strategische KPIs herum, stelle sie als BANs, Sparklines und RAG auf einer einzigen Seite dar und lass Pulse den wöchentlichen Überblick an die Führung tragen. Behandle dann die Kennzahlenauswahl als die eigentliche Entscheidung, überprüfe sie bewusst und lass niemals ein ordentlich grünes Brett das Urteilsvermögen ersetzen, das die Führung eines Geschäfts erfordert.

*Teil des Tracks [Analysen zur kaufmännischen Planung]({{ '/de/tracks/commercial-planning/' | relative_url }}).* Verwandt: das [KI-Dashboard des CFO für Getränke]({{ '/de/2026/cfo-ai-dashboard-beverage/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist ein BAN in Tableau und warum auf einer Scorecard verwenden?**
Ein BAN ist eine Big Aggregate Number, eine große Einzelzahl wie das Monatsvolumen oder die Marge. Auf einer Führungs-Scorecard lässt sie eine Führungskraft die Kernaussage in Sekunden lesen, mit einer Sparkline darunter für den Trendkontext.

**Wie viele KPIs sollte eine Führungs-Scorecard haben?**
Wenige. Strebe sechs bis neun Schlüsselkennzahlen an, die ein CEO in unter einer Minute erfassen kann. Eine mit dreißig Kennzahlen überladene Scorecard ist ein Bericht, keine Scorecard, und sie wird nicht gelesen.

**Kann Tableau Pulse das wöchentliche Führungsmeeting ersetzen?**
Nein. Pulse kann einen wöchentlichen Überblick liefern und markieren, was sich bewegt hat, aber im Meeting findet das Urteilsvermögen statt. Der Überblick bereitet das Gespräch vor; er trifft nicht die Entscheidungen.
