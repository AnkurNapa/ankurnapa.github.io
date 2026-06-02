---
layout: post
lang: de
title: "Herstellkosten je Hektoliter: Die Zahl, die du zuerst automatisieren solltest"
image: /assets/og/cost-of-goods-per-hectoliter.png
description: "Wie Brauereien die Herstellkosten je Hektoliter automatisieren können, um eine genaue Produktionsökonomie in Echtzeit zu erhalten — auch für alkoholfreies Bier."
date: 2025-02-18
updated: 2025-02-18
permalink: /de/2025/cost-of-goods-per-hectoliter/
tags: [fpna, cost-accounting, brewing-economics]
faq:
  - q: "Was sind die Herstellkosten je Hektoliter beim Brauen?"
    a: "Es sind die gesamten direkten Kosten — Rohstoffe, Verpackung, direkte Arbeit und das dem Produktionsvolumen zugeordnete Gemeinkosten — geteilt durch die in einem bestimmten Zeitraum produzierten Hektoliter. Es ist die grundlegende Stückkosten-Kennzahl für jede Brauerei."
  - q: "Warum sind die Herstellkosten je Hektoliter für alkoholfreies Bier schwerer zu berechnen?"
    a: "Alkoholfreies Bier umfasst typischerweise einen zusätzlichen Entalkoholisierungsschritt (Vakuumdestillation, Umkehrosmose oder gestoppte Gärung), der Energie, Anlagenabschreibung und manchmal Ausbeuteverlust hinzufügt. Diese Kosten müssen korrekt der alkoholfreien SKU zugeordnet werden, was viele Brauerei-ERP-Konfigurationen nicht standardmäßig leisten."
  - q: "Wie oft sollte eine Brauerei die Herstellkosten je Hektoliter neu berechnen?"
    a: "Best Practice ist monatlich, abgestimmt auf einen Standardkosten-Roll. Volumenstarke oder rohstoffexponierte Betriebe profitieren von einer rollierenden 13-Wochen-Sicht, die sich auffrischt, wann immer sich zentrale Inputkosten — Malz, Energie, Aluminium — um mehr als einen festgelegten Schwellenwert bewegen."
---

**Kurze Antwort:** Die Herstellkosten je Hektoliter (COGS/hl) sind die einzelne wichtigste Stückkosten-Größe im Finanz-Stack einer Brauerei, und sie werden fast immer zu selten, zu manuell oder mit Kostenpools berechnet, die die Wahrheit auf SKU-Ebene leise verzerren. Sie zu automatisieren ist kein Technologieprojekt — es ist ein Datendisziplin-Projekt, das sich innerhalb eines Budgetzyklus amortisiert.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Herstellkosten je Hektoliter: Die Zahl, die du zuerst automatisieren solltest</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">die Praxis ändern</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Warum diese Zahl der Anker jedes FP&A-Gesprächs ist

Jede materielle Planungs-, Preis- und Kapitalentscheidung, die eine Brauerei trifft, lässt sich auf COGS/hl zurückführen. Doch in den meisten Betrieben unter 200.000 hl wird die Größe einmal im Quartal aus einer Tabelle erzeugt, die selektiv aus dem ERP zieht, einen einzigen Gemeinkosten-Absorptionssatz über alle Marken anwendet und drei Wochen nach Periodenabschluss auf dem Schreibtisch des CFO landet.

Bis dahin ist die Zahl historische Trivia. Die Brauläufe, die die Abweichung trieben, wurden bereits — nach Bauchgefühl — repliziert oder verworfen.

Das Ziel der Automatisierung ist nicht, Buchhalter zu eliminieren. Es ist, die Rückkopplungsschleife von dreißig Tagen auf drei zu verkürzen, sodass die Produktions- und Vertriebsteams Entscheidungen gegen die aktuelle Ökonomie treffen, nicht gegen die des letzten Quartals.

## Der Treiberbaum hinter COGS/hl

Ein sauberer Treiberbaum hat vier Äste:

**Rohstoffe je hl** — Malz, Hopfen, Zusätze, Hefe. Die Schlüsselvariable ist die Ausbeute: die tatsächliche Extrakteffizienz gegenüber der theoretischen. Ein Rückgang der Sudhausausbeute um 1 % ist in der GuV unsichtbar, bis er sich über ein volles Quartal aufsummiert.

**Verpackung je hl** — Dosen, Glas, Kronkorken, Etiketten, Sekundärkartons. Aluminium bewegt sich besonders mit den Rohstoffmärkten; eine in ein Jahresbudget eingebackene Festpreisannahme kann innerhalb von neunzig Tagen wesentlich falsch sein.

**Direkte Arbeit je hl** — der Produktion belastete Schichtstunden, angepasst an den Volumendurchsatz. Überstundenbelastung und saisonale Personaländerungen verzerren dies, wenn die Arbeit nicht auf Braucharge-IDs gemappt ist.

**Zugeordnete Gemeinkosten je hl** — Abschreibung, Energie, Qualitätslabor, Wartung. Der Absorptionssatz sollte neu berechnet werden, wenn sich die Kapazitätsauslastung wesentlich verschiebt; den Vorjahressatz auf einen halbleeren Keller anzuwenden untertreibt die wahren Kosten systematisch.

## Wo alkoholfreies Bier das Standardmodell sprengt

Alkoholfreies Bier fügt einen fünften Kostenknoten hinzu, für den die Standard-Kontenpläne von Brauereien nicht gebaut sind: den Entalkoholisierungsschritt. Ob der Betrieb Vakuumdestillation, Umkehrosmose oder eine gestoppte Kaltkontakt-Gärung nutzt, es gibt zusätzliche Energie, zusätzliche Arbeit und — im Fall von RO oder Destillation — einen bedeutenden Ausbeuteverlust, der als Kosten des alkoholfreien Volumens erfasst werden muss, nicht über den ganzen Sud verteilt.

Die praktische Implikation: Wenn dein ERP alkoholfreie hl durch dieselbe Kostenstelle wie dein Standard-Lager leitet, ist deine alkoholfreie Marge fast sicher überzeichnet und deine Standard-Lager-Marge unterzeichnet. Das Kostenstellen-Mapping zu beheben ist eine einmalige Konfigurationsaufgabe, aber sie erfordert, dass sich das Finanzteam und der Braumeister einigen, wo die Entalkoholisierung im Produktionsablauf beginnt und endet.

## Die Automatisierungs-Roadmap

Der minimal funktionsfähige Automatisierungs-Stack tut drei Dinge:

1. **Kostenerfassung auf Chargenebene** — jede Braucharge erhält einen Fertigungsauftrag, der den tatsächlichen Getreideverbrauch, die tatsächliche Energie (nach Möglichkeit zwischengemessen) und die tatsächlichen Arbeitsstunden beim Abschluss erfasst. Das ist meist eine Konfigurationsänderung im bestehenden ERP, kein neues System.

2. **Rohstoffpreis-Aktualisierung** — Malz- und Aluminium-Vertragspreise fließen nach einem Zeitplan, der zum Einkaufszyklus passt, in die Standardkostendatei ein, sodass Abweichungen reale Preisbewegungen widerspiegeln statt veralteter Annahmen.

3. **Monatliches COGS/hl-Dashboard** — eine einzige Ansicht, nach SKU und nach Kanal, die Ist- gegen Standardkosten, die drei größten Abweichungstreiber und einen rollierenden 13-Wochen-Trend zeigt. Das lässt sich in Power BI, Tableau oder einer gut gesteuerten Tabelle bauen, die mit Live-ERP-Exporten verbunden ist.

Die ehrliche Grenze: Automatisierung legt die Zahlen schneller offen, aber sie kann die zugrunde liegende Datenqualität nicht verbessern, wenn Braucharge-Aufzeichnungen unvollständig sind oder die Logik der Gemeinkostenzuordnung zwischen Finanz und Betrieb strittig ist. Die Governance-Arbeit — sich auf Definitionen zu einigen — muss dem Werkzeug vorausgehen.

## Das „Na und" für Finanzführungskräfte

Eine Brauerei, die ihre COGS/hl nach SKU kennt, monatlich aufgefrischt, kann drei Dinge tun, die ihre Wettbewerber wahrscheinlich nicht können: mit Zuversicht bepreisen, wenn ein Händler einen Mengenrabatt verlangt; identifizieren, welche SKUs vor der nächsten Kapazitätsklemme rationalisiert werden sollten; und die wahre Ökonomie des Hinzufügens einer alkoholfreien Linie modellieren, bevor das Kapital gebunden wird. Das ist die Belohnung. Die Automatisierung ist nur das Mittel.

*Teil des Tracks Finanzplanung & Analytics — [alle durchstöbern]({{ '/de/tags/' | relative_url }}#fpna).*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Jede Stufe verliert etwas — der Trichter zeigt, wo der Abfall ist."><rect x="0" y="0" width="720" height="310" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">TRICHTER</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Herstellkosten je Hektoliter: Die Zahl, die du zuerst automatisieren solltest</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#b45309" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reichweite · 100 %</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#b45309" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interesse · 52 %</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#b45309" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Test · 24 %</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#b45309" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Gewinn · 9 %</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Jede Stufe verliert etwas — der Trichter zeigt, wo der Abfall ist.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was sind die Herstellkosten je Hektoliter beim Brauen?**
Es sind die gesamten direkten Kosten — Rohstoffe, Verpackung, direkte Arbeit und das dem Produktionsvolumen zugeordnete Gemeinkosten — geteilt durch die in einem bestimmten Zeitraum produzierten Hektoliter. Es ist die grundlegende Stückkosten-Kennzahl für jede Brauerei.

**Warum sind die Herstellkosten je Hektoliter für alkoholfreies Bier schwerer zu berechnen?**
Alkoholfreies Bier umfasst typischerweise einen zusätzlichen Entalkoholisierungsschritt (Vakuumdestillation, Umkehrosmose oder gestoppte Gärung), der Energie, Anlagenabschreibung und manchmal Ausbeuteverlust hinzufügt. Diese Kosten müssen korrekt der alkoholfreien SKU zugeordnet werden, was viele Brauerei-ERP-Konfigurationen nicht standardmäßig leisten.

**Wie oft sollte eine Brauerei die Herstellkosten je Hektoliter neu berechnen?**
Best Practice ist monatlich, abgestimmt auf einen Standardkosten-Roll. Volumenstarke oder rohstoffexponierte Betriebe profitieren von einer rollierenden 13-Wochen-Sicht, die sich auffrischt, wann immer sich zentrale Inputkosten — Malz, Energie, Aluminium — um mehr als einen festgelegten Schwellenwert bewegen.
