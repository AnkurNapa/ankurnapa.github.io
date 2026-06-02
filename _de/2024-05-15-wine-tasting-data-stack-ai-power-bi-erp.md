---
layout: post
lang: de
title: "Weinverkostung trifft den Daten-Stack: KI, Power BI und ERP"
image: /assets/og/wine-tasting-data-stack-ai-power-bi-erp.png
description: "Verknüpfe Verkostungs- und Probierbewertungen mit Jahrgang, Parzelle, Partie und Fass im ERP, analysiere in Power BI und nutze KI, um Fehler vorherzusagen und zu markieren — der Gaumen entscheidet weiterhin."
date: 2024-05-15
updated: 2024-05-15
permalink: /de/2024/wine-tasting-data-stack-ai-power-bi-erp/
tags: [winemaking, tasting, power-bi, erp]
faq:
  - q: "Wo liegen die Verkostungsdaten eigentlich?"
    a: "In Dataverse, erfasst über eine Power-Apps-App, wobei jede Bewertung mit dem Partie-, Parzellen-, Jahrgangs- oder Fass-Datensatz verknüpft ist, der in deinem ERP gehalten wird. Diese Verknüpfung gibt dem Ergebnis Kontext und Rückverfolgbarkeit — und sie lässt Power BI Gleiches mit Gleichem vergleichen."
  - q: "Kann KI die Weinqualität aus der Analyse vorhersagen?"
    a: "Sie kann sensorische Eigenschaften aus Instrumentendaten wie NIR oder FTIR mit Chemometrie vorhersagen und wahrscheinliche Fehler markieren — nützlich als Vorfilter. Qualität oder Balance kann sie nicht beurteilen. Der Gaumen des Winzers entscheidet; das Modell weist dich darauf hin, was du zuerst verkosten solltest."
  - q: "Ist das für ein kleines Weingut übertrieben?"
    a: "Oft ja. Wenn du nur eine Handvoll Partien pro Jahr machst, kann eine saubere Tabelle, die mit deinen Partienummern verknüpft ist, genügen. Der Daten-Stack rechtfertigt sich, wenn du viele Partien, Verschnittproben und Fässer über Jahrgänge hinweg zu verfolgen hast."
---

**Kurze Antwort: Der Wert liegt nicht in der Verkostungsnotiz — er liegt darin, jede Bewertung mit der Partie, der Parzelle, dem Jahrgang und dem Fass zu verknüpfen, sodass du sicher vergleichen, verschneiden und rückverfolgen kannst.** Eine Verkostungsbewertung, die frei von ihrer Partie schwebt, ist eine Meinung. Dieselbe Bewertung, verknüpft mit einem Fass und einem Jahrgang, ist ein Entscheidungsinput.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Weinproduktionsfluss sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSFLUSS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Weinverkostung trifft den Daten-Stack: KI, Power BI und ERP</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Ernte</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Mahlen / Pressen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Reifung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllung</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Weinproduktionsfluss sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Stammdaten zuerst: der Keller läuft auf Schlüsseln
Weinbereitung ist bereits ein Datenproblem — du verfolgst es nur auf Whiteboards und im Kopf. Jahrgang, Parzelle, Partie, Fass, Zugaben, Verschnittproben: Jedes ist ein Datensatz, und die Beziehungen zwischen ihnen sind das, was zählt. Dein **ERP** (Dynamics 365 Business Central, Finance & Operations oder ein weinspezifisches System) ist die natürliche Heimat für diese Stammdaten — Produkte, Partien, Jahrgänge, Fässer, Lieferanten und Bestand.

Die Disziplin, die alles stromabwärts funktionieren lässt, ist **Data Science** in ihrer am wenigsten glamourösen Form: eine konsistente Attributliste, kalibrierte Skalen und saubere Schlüssel. Vor jedem Modell oder Dashboard muss jede Verkostungs- und Probierbewertung auf eine echte Partie oder ein echtes Fass verweisen. Mach das richtig und der Rest ist meist Rohrleitung.

## Erfassen am Probiertisch, nicht zurück am Schreibtisch
Probierdurchläufe und Verkostungssitzungen finden im Keller statt, oft mit nassen Händen und ohne Signal. Eine **Power Apps**-App auf **Dataverse** lässt dich und das Panel auf einem Tablet bewerten — wähle die Partie oder Verschnittprobe, bewerte Struktur, Frucht, Eiche und Fehler auf der Hausskala, protokolliere das Ergebnis gegen das Fass. Sie erfasst offline und synchronisiert später. Die Bewertung landet strukturiert und verknüpft, statt als Gekritzel, das nächste Woche transkribiert (und falsch erinnert) wird.

Das ist am wichtigsten für Verschnittproben, bei denen du viele kleine Permutationen unter Zeitdruck vergleichst. Strukturierte Erfassung bedeutet, dass du tatsächlich rekonstruieren kannst, welche Probe gewonnen hat und warum.

## Analysieren und entscheiden in Power BI
Mit Bewertungen, die mit Partien verknüpft sind, macht **Power BI** aus der Arbeit des Panels Entscheidungen:

- **Partievergleiche** — Partien nach den Attributen, die deinen Stil treiben, einordnen und gegenüberstellen.
- **Verschnittentscheidungen** — sehen, wie Verschnittproben über Attribute hinweg abschneiden, mit den beitragenden Partien einen Klick entfernt.
- **Fehlerverfolgung** — markierte Fehler über den Keller und über Jahrgänge hinweg überwachen, sodass ein schleichendes Problem früh auftaucht.

Weil die Daten ihren Kontext vom ERP erben, lässt sich jede Visualisierung bis zu einem Fass oder einer Parzelle aufschlüsseln. Der Copilot in Power BI beantwortet klar formulierte Fragen — "welche Partien schnitten in diesem Jahrgang bei der Frucht am höchsten ab, zeigten aber flüchtige Säure?" — und liefert ein Diagramm, das du dann verifizierst.

## Was KI hinzufügt — und wo sie aufhört
**Machine Learning** hat hier zwei solide Rollen. Erstens, sensorische Ergebnisse aus Instrumentendaten vorhersagen: NIR- oder FTIR-Messwerte plus Chemometrie können Eigenschaften schätzen und priorisieren, welche Partien zu verkosten sind, wobei das Panel die Vorhersage validiert. Zweitens, Fehlermarkierung — wahrscheinliche **Brett** (4-EP/4-EG), **flüchtige Säure**, **TCA** oder Oxidation aus den Daten heraufholen, damit das Panel weiß, worauf es sich konzentrieren soll. Clustering kann Partien auch nach Aromaprofil gruppieren, um den Verschnitt zu informieren.

Die Grenze ist fest. **KI und Dashboards verkosten nicht.** Ein Modell kann dir sagen, dass eine Partie chemisch konsistent mit Brett aussieht; nur das Panel bestätigt, ob der Wein fehlerhaft und unverkäuflich ist. Der Gaumen des Winzers entscheidet über Balance, Typizität und Hausstil; der Stack organisiert und kommuniziert, was der Gaumen produziert. Schiebe das Modell über diese Linie hinaus und du wirst irgendwann einen Wein ausliefern, den ein Dashboard mochte und ein Mensch nicht.

Es gibt auch einen Kostenaspekt. Power-Platform-Lizenzierung erfolgt pro Nutzer oder pro App, und ein sauberes Datenmodell erfordert Governance-Aufwand. Für einen kleinen Erzeuger zahlt sich dieser Overhead vielleicht nicht aus — eine disziplinierte Tabelle, die mit Partienummern verknüpft ist, kann dich weit tragen.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Was den Prozess treibt und was es stromabwärts verändert."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WAS ES TREIBT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Weinverkostung trifft den Daten-Stack: KI, Power BI und ERP</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Der Prozess</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Qualität</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Kosten / Risiko</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Was den Prozess treibt und was es stromabwärts verändert.</figcaption>
</figure>

## Das Fazit
Weinverkostung trifft den Daten-Stack, wenn Bewertungen aufhören, Notizen zu sein, und anfangen, verknüpfte Datensätze zu werden. ERP hält die Stammdaten, Power Apps erfasst die Bewertungen im Keller, Power BI macht daraus Verschnitt- und Freigabeentscheidungen, und KI sagt vorher und markiert, sodass das Panel zuerst die richtigen Dinge verkostet. **Generative KI** kann eine Verkostungsnotiz im Hausstil entwerfen oder Fragen über die Kellerdaten beantworten — immer von Menschen geprüft. Der Gaumen bleibt am Steuer.

*Teil des Tracks [Winemaking & AI]({{ '/de/tracks/winemaking-ai/' | relative_url }}).* Verwandt: [Kann KI die Weinqualität vorhersagen?]({{ '/de/2026/can-ai-predict-wine-quality/' | relative_url }}) und [Weinfehler erkennen: Brett, VA, TCA]({{ '/de/2024/detecting-wine-faults-brett-va-tca/' | relative_url }}).

## Häufig gestellte Fragen

**Wo liegen die Verkostungsdaten eigentlich?**
In Dataverse, erfasst über eine Power-Apps-App, wobei jede Bewertung mit dem Partie-, Parzellen-, Jahrgangs- oder Fass-Datensatz verknüpft ist, der in deinem ERP gehalten wird. Diese Verknüpfung gibt dem Ergebnis Kontext und Rückverfolgbarkeit — und sie lässt Power BI Gleiches mit Gleichem vergleichen.

**Kann KI die Weinqualität aus der Analyse vorhersagen?**
Sie kann sensorische Eigenschaften aus Instrumentendaten wie NIR oder FTIR mit Chemometrie vorhersagen und wahrscheinliche Fehler markieren — nützlich als Vorfilter. Qualität oder Balance kann sie nicht beurteilen. Der Gaumen des Winzers entscheidet; das Modell weist dich darauf hin, was du zuerst verkosten solltest.

**Ist das für ein kleines Weingut übertrieben?**
Oft ja. Wenn du nur eine Handvoll Partien pro Jahr machst, kann eine saubere Tabelle, die mit deinen Partienummern verknüpft ist, genügen. Der Daten-Stack rechtfertigt sich, wenn du viele Partien, Verschnittproben und Fässer über Jahrgänge hinweg zu verfolgen hast.
