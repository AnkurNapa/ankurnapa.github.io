---
layout: post
lang: de
title: "Kannibalisierung: Frisst alkoholfreies Bier den Absatz deines Lagers?"
image: /assets/og/cannibalization-na-beer-lager.png
description: "Ein Rahmen zur Messung der Kannibalisierung zwischen alkoholfreiem Bier und konventionellem Lager — und wie man kannibalisiertes Volumen von echter Kategorieexpansion trennt."
date: 2025-11-14
updated: 2025-11-14
permalink: /de/2025/cannibalization-na-beer-lager/
tags: [forecasting, cannibalization-analysis]
faq:
  - q: "Was ist Kannibalisierung in der Getränkenachfrageprognose?"
    a: "Kannibalisierung tritt auf, wenn ein neues Produkt in einem Portfolio Absatz von einem bestehenden Produkt abzieht, statt zusätzliche Käufer oder Anlässe anzuziehen. Im Bierkontext ist die Frage, ob NA-Biertrinker konventionelle Lagerkäufe ersetzen oder neue Trinkanlässe hinzufügen."
  - q: "Kannibalisiert alkoholfreies Bier wirklich konventionelles Lager?"
    a: "Die Belege über Märkte hinweg sind gemischt und stark markenabhängig. Manche Forschung legt nahe, dass NA-Bier in erster Linie ein zusätzliches Anlassprodukt ist — gekauft für bestimmte Situationen, in denen Alkohol ungeeignet ist —, während andere Daten ein bedeutsames Wechselverhalten zeigen, besonders unter gesundheitsbewussten häufigen Lagertrinkern. Eine Analyse auf Markenebene ist informativer als eine Kategorieverallgemeinerung."
  - q: "Wie misst man die Kannibalisierungsrate in einem Bierportfolio?"
    a: "Der Standardansatz ist ein kontrolliertes Markt- oder Test-and-Learn-Design: Verfolge das Volumen konventionellen Lagers in Märkten oder Accounts, in denen NA neu eingeführt wird, gegenüber abgeglichenen Kontrollmärkten, in denen NA noch nicht distribuiert ist. Der Unterschied in der Lagerleistung über diese Gruppen hinweg, unter Kontrolle von Saisonalität und anderen Faktoren, liefert eine Schätzung der Kannibalisierungsrate."
---

**Kurze Antwort:** Die Auswirkung von alkoholfreiem Bier auf konventionelles Lager ist eine der kommerziell folgenreichsten Fragen, mit denen Bierportfolio-Manager heute konfrontiert sind, und die ehrliche Antwort lautet: Sie hängt erheblich von der Marke, dem Distributionskanal und dem Konsumentensegment ab. Einen Messrahmen aufzubauen ist wertvoller, als sich auf Kategorieverallgemeinerungen zu verlassen — die Varianz über Markenportfolios hinweg ist breit genug, um generische Behauptungen irreführend zu machen.

---

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 280" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Der Betriebskreislauf, den dieser Beitrag beschreibt"><rect x="0" y="0" width="1000" height="280" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DER BETRIEBSKREISLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Kannibalisierung: Frisst alkoholfreies Bier den Absatz deines Lagers?</text><g font-family="sans-serif"><rect x="40" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="140.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Messen</text><text x="140.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Daten rein</text><rect x="260" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="360.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Analysieren</text><text x="360.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Signal finden</text><rect x="500" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="600.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Entscheiden</text><text x="600.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">wählen</text><rect x="740" y="96" width="200" height="140" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="840.0" y="162.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Handeln</text><text x="840.0" y="186.0" text-anchor="middle" font-size="12.5" fill="#6b6258">die Fläche ändern</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="240" y1="166.0" x2="253" y2="166.0"/><polygon points="253,161.0 260,166.0 253,171.0" stroke="none"/><line x1="460" y1="166.0" x2="493" y2="166.0"/><polygon points="493,161.0 500,166.0 493,171.0" stroke="none"/><line x1="700" y1="166.0" x2="733" y2="166.0"/><polygon points="733,161.0 740,166.0 733,171.0" stroke="none"/></g><path d="M840,96 C840,74 840,74 800,74 L160,74 C140,74 140,74 140,96" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="135,90 140,98 145,90" fill="#7a1f3d"/><text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">wiederholen</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Der Betriebskreislauf, den dieser Beitrag beschreibt: messen, analysieren, entscheiden, handeln — dann wiederholen.</figcaption>
</figure>

## Warum Kannibalisierungsanalyse nicht optional ist

Wenn ein großer Brauer eine NA-Variante seines Flaggschiff-Lagers einführt, geht das Finanzmodell fast sicher davon aus, dass die neue SKU additiv sein wird — neue Anlässe und neue Käufer erfasst, ohne den Absatz konventionellen Lagers nennenswert zu reduzieren. Diese Annahme wird bei der Einführung fast nie rigoros geprüft.

Ist die Annahme falsch, ändert sich die kommerzielle Rechnung erheblich. Eine NA-SKU, die $X an inkrementellem Umsatz erzeugt, aber 0,7X des konventionellen Lagerumsatzes verdrängt, schafft $0,3X an Nettowert — und diese Nettozahl muss gegen die zusätzliche Lieferkettenkomplexität, die Verpackungsinvestition und die Regalplatz-Kompromisse abgewogen werden, die die neue SKU erfordert.

Die Analyse ist unbequem, was genau der Grund ist, warum sie vermieden wird. Sie in den Prognoseprozess einzubringen ist ein Zeichen kommerzieller Reife.

---

## Die Hypothese des zusätzlichen Anlasses

Die optimistische Sicht auf NA-Bier — und die in Wachstumserzählungen der Kategorie am häufigsten zitierte — ist, dass es grundlegend andere Anlässe bedient als konventionelles Bier. Der designierte Fahrer, der Erholungsanlass am Wochenabend, das gesellige Mittagsambiente, der gesundheitsbewusste Moment der Mäßigung: Das sind Zeiten, in denen viele konventionelle Biertrinker ohnehin keinen Alkohol gekauft hätten. NA-Bier erfasst einen zuvor unbedienten Moment.

Wenn die Hypothese des zusätzlichen Anlasses zutrifft, liegt die Kannibalisierungsrate nahe null und die NA-SKU ist wirklich additiv zum Portfoliovolumen. Die Distribution von NA fügt Accounts und Anlässe hinzu; die Geschwindigkeit konventionellen Lagers in bestehenden Accounts bleibt unberührt.

Diese Hypothese stützt: die Tatsache, dass das schnellste Wachstum von NA-Bier in Anlässen und Tageszeiten zu liegen scheint, in denen konventionelles Bier historisch abwesend oder marginal war.

---

## Das Risiko des Wechselverhaltens

Die pessimistische Sicht — gestützt von zumindest einigen Scannerdaten und Belegen aus Konsumentenpanels in reiferen NA-Märkten — ist, dass ein bedeutsamer Anteil des NA-Biervolumens von Konsumenten kommt, die zuvor konventionelles Lager kauften und ihre Anlassverteilung verschoben haben. Das ist besonders plausibel für markentreue Trinker eines Flaggschiff-Lagers, die nun gelegentlich die NA-Variante derselben Marke wählen.

Für diese Käufer ist jeder NA-Kauf eine direkte Substitution. Die markeninterne Wechselrate — der Anteil des NA-Volumens, der von bestehenden konventionellen Lagerkäufern gekauft wird — ist die Schlüsselkennzahl, die zu verfolgen ist. Konsumentenpanels oder Kundenkartendaten, wo verfügbar, liefern das sauberste Signal.

Die Geschichte des markeninternen Wechsels ist verschieden von der markenübergreifenden Kannibalisierung (bei der eine NA-Einführung eines Brauers Volumen von den konventionellen Produkten eines Wettbewerbers abzieht) — ein komplexerer und im Allgemeinen kleinerer Effekt.

---

## Ein Messrahmen

Ein praktischer Ansatz zur Kannibalisierungsmessung für eine Brauerei mit angemessenen Depletion-Daten:

1. **Definiere die Test- und Kontrollmärkte.** Wenn du NA-Bier in neue Distributions-Accounts oder Regionen einführst, identifiziere abgeglichene Accounts oder Regionen, in denen die Einführung noch nicht stattfindet. Diese dienen als Kontrollen.

2. **Verfolge die Geschwindigkeit konventionellen Lagers in beiden Gruppen.** Geschwindigkeit (Volumen pro Distributionspunkt) isoliert den Leistungseffekt vom Distributionseffekt. Wenn die Geschwindigkeit konventionellen Lagers in den Accounts sinkt, in denen NA hinzugefügt wurde, aber in den Kontroll-Accounts stabil bleibt, ist Kannibalisierung vorhanden.

3. **Miss über ein ausreichendes Zeitfenster.** Anfängliche Einführungsphasen zeigen oft, dass konventionelles Lager stabil bleibt, weil NA Probekäufer anzieht. Das Kannibalisierungssignal, falls vorhanden, kann sechs bis zwölf Monate brauchen, um sichtbar zu werden, während sich die Kaufmuster stabilisieren.

4. **Schätze die Rate und den Nettowert.** Ein Geschwindigkeitsrückgang von 5 % beim konventionellen Lager in Accounts, in denen NA distribuiert ist, gegenüber einer Basisgeschwindigkeit von X Kisten je Account, liefert eine in Dollar bezifferte Kannibalisierungsschätzung, die gegen den inkrementellen Beitrag von NA abgewogen werden kann.

Zu den Auswirkungen von Kannibalisierungsschätzungen auf die Lieferplanung siehe [Hierarchische Prognose: SKU-, Marken- und Gesamtvolumen abgleichen]({{ '/de/2025/hierarchical-forecasting-beverage/' | relative_url }}) — das Netto-Portfoliovolumen nach Kannibalisierung ist die Zahl, die in die Kapazitätsplanung einfließen muss, nicht das Brutto-NA-Volumen isoliert.

---

## Promotions als Beschleuniger

Promotionsmechaniken können Kannibalisierungseffekte verstärken oder maskieren. Eine Preispromotion auf die NA-Variante, die starke Probekäufe von konventionellen Lagerkäufern antreibt, erzeugt in den Daten ein scheinbares Kannibalisierungssignal, das bei vollem Preis möglicherweise nicht anhält. Umgekehrt kann eine Promotion auf konventionelles Lager die NA-Kannibalisierungsrate vorübergehend unterdrücken, indem sie konventionelle Käufer zurückzieht.

Promotions-Lift-Analyse über das Portfolio hinweg — behandelt in [Promotions-Lift: Echte Nachfrage vom Rabattrauschen trennen]({{ '/de/2025/promotional-lift-forecasting/' | relative_url }}) — sollte stets promotete Zeiträume isolieren, bevor Kannibalisierungsschlüsse gezogen werden.

---

## Der ehrliche Vorbehalt

Kannibalisierung ist innerhalb von Getränkeorganisationen politisch heikel. Kommerzielle Teams mit NA-Vertriebszielen haben Anreize, sie zu untertreiben; konventionelle Markenmanager haben Anreize, sie zu übertreiben. Ein Messprozess, der von Finanzen oder Lieferkette gestaltet wird — mit kommerziellen Eingaben, aber ohne kommerzielle Kontrolle über die Methodik —, liefert glaubwürdigere Ergebnisse als einer, der vollständig innerhalb eines einzelnen Markenteams angesiedelt ist.

Die Datenanforderungen sind ebenfalls real: Scannerdaten, Konsumentenpanels oder sorgfältig abgeglichene Test-und-Kontroll-Märkte. Die meisten regionalen und Craft-Brauereien werden keinen Zugang zu den Scannerdaten haben, die große nationale Brauer nutzen. In diesem Fall ist eine ehrliche qualitative Einschätzung der Konsumentenüberschneidung — informiert durch Kundengespräche und Distributor-Feedback — einem fragwürdigen quantitativen Modell vorzuziehen, das auf unzureichenden Daten aufgebaut ist.

*Teil des Tracks Sales Forecasting — [alle durchsuchen]({{ '/de/tags/' | relative_url }}#forecasting).*

---

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 310" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall liegt."><rect x="0" y="0" width="720" height="310" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">FUNNEL</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Kannibalisierung: Frisst alkoholfreies Bier den Absatz deines Lagers?</text><polygon points="140.0,78 580.0,78 530.0,126 190.0,126" fill="#b45309" opacity="1.0"/><text x="360" y="109" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Reichweite · 100%</text><polygon points="190.0,134 530.0,134 480.0,182 240.0,182" fill="#b45309" opacity="0.8200000000000001"/><text x="360" y="165" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Interesse · 52%</text><polygon points="240.0,190 480.0,190 430.0,238 290.0,238" fill="#b45309" opacity="0.64"/><text x="360" y="221" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Probe · 24%</text><polygon points="290.0,246 430.0,246 380.0,294 340.0,294" fill="#b45309" opacity="0.45999999999999996"/><text x="360" y="277" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#ffffff">Gewinn · 9%</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Jede Stufe verliert etwas — der Funnel zeigt, wo der Abfall liegt.</figcaption>
</figure>

## Häufig gestellte Fragen

**Was ist Kannibalisierung in der Getränkenachfrageprognose?**  
Kannibalisierung tritt auf, wenn ein neues Produkt in einem Portfolio Absatz von einem bestehenden Produkt abzieht, statt zusätzliche Käufer oder Anlässe anzuziehen. Im Bierkontext ist die Frage, ob NA-Biertrinker konventionelle Lagerkäufe ersetzen oder neue Trinkanlässe hinzufügen.

**Kannibalisiert alkoholfreies Bier wirklich konventionelles Lager?**  
Die Belege über Märkte hinweg sind gemischt und stark markenabhängig. Manche Forschung legt nahe, dass NA-Bier in erster Linie ein zusätzliches Anlassprodukt ist — gekauft für bestimmte Situationen, in denen Alkohol ungeeignet ist —, während andere Daten ein bedeutsames Wechselverhalten zeigen, besonders unter gesundheitsbewussten häufigen Lagertrinkern. Eine Analyse auf Markenebene ist informativer als eine Kategorieverallgemeinerung.

**Wie misst man die Kannibalisierungsrate in einem Bierportfolio?**  
Der Standardansatz ist ein kontrolliertes Markt- oder Test-and-Learn-Design: Verfolge das Volumen konventionellen Lagers in Märkten oder Accounts, in denen NA neu eingeführt wird, gegenüber abgeglichenen Kontrollmärkten, in denen NA noch nicht distribuiert ist. Der Unterschied in der Lagerleistung über diese Gruppen hinweg, unter Kontrolle von Saisonalität und anderen Faktoren, liefert eine Schätzung der Kannibalisierungsrate.
