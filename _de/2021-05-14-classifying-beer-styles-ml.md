---
layout: post
lang: de
title: "Bierstile mit maschinellem Lernen klassifizieren"
image: /assets/og/classifying-beer-styles-ml.png
description: "Wie maschinelles Lernen Bierstile aus OG, FG, ABV, IBU und Farbe klassifiziert, wo es bei QC und Wettbewerbssortierung hilft und wo Stile verschwimmen."
date: 2021-05-14
updated: 2021-05-14
permalink: /de/2021/classifying-beer-styles-ml/
tags: [brewing-science, machine-learning, recipe]
faq:
  - q: "Welche Merkmale nutzt ein Bierstil-Klassifikator?"
    a: "Vor allem die messbaren Kennwerte, die Stilrichtlinien wie das BJCP definieren: Stammwürze und Restextrakt, ABV, IBU sowie Farbe in SRM oder EBC, oft mit Zutaten-Markern wie Hopfensorte oder Malztyp. Das Modell ordnet diese Zahlen einem Stil-Label zu."
  - q: "Warum wird mein Bier als zwei verschiedene Stile klassifiziert?"
    a: "Weil sich Stilrichtlinien überschneiden. Ein American Pale Ale und ein Session IPA teilen einen großen Teil desselben OG-, IBU- und Farbraums, sodass ein Bier nahe der Grenze tatsächlich zwischen zwei Labels liegt — und ein guter Klassifikator beide mit Wahrscheinlichkeiten ausweist."
  - q: "Kann ein Klassifikator beurteilen, ob mein Bier gut ist?"
    a: "Nein. Er beurteilt die Stiltreue, also ob dein Bier auf dem Papier seinem deklarierten Stil entspricht. Qualität, Balance und Aroma sind eine separate Frage, die nur ein kalibriertes Sensorikpanel beantworten kann."
---

**Kurze Antwort: Maschinelles Lernen kann den Stil eines Biers aus seinen Kernkennwerten mit brauchbarer Genauigkeit benennen, aber die Stile selbst sind unscharf — behandle die Ausgabe also als Orientierung, nicht als Urteil.** Die Stilklassifizierung ist eines der saubersten Probleme überwachten Lernens, die das Brauen zu bieten hat.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Bierstile mit maschinellem Lernen klassifizieren</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllung</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende.</figcaption>
</figure>

## Stil als Feature-Mapping-Problem
Bierstile werden durch Richtlinien wie das BJCP definiert, die Bereiche für messbare Parameter festlegen: Stammwürze (OG), Restextrakt (FG), ABV, Bitterkeit (IBU) und Farbe in SRM oder EBC, dazu Erwartungen an die Zutaten und sensorische Beschreibungen. Aus datenwissenschaftlicher Sicht ist das unkompliziert: Jedes Bier ist ein Punkt in einem Merkmalsraum, und Klassifizierung ist die Aufgabe, diesen Punkt dem nächstgelegenen Stil-Label zuzuordnen.

Weil die Eingaben Zahlen sind, die ein Brauer ohnehin erfasst, sind die Daten günstig. QC-Laborprotokolle, Wettbewerbs-Anmeldeformulare und Rezeptdatenbanken tragen alle OG, FG, ABV, IBU und Farbe. Das macht die Stilklassifizierung zu einem ungewöhnlich zugänglichen Einstieg ins maschinelle Lernen, denn du kannst zuerst messen und einen Trainingsdatensatz aus Aufzeichnungen zusammenstellen, die du bereits führst.

## Wofür ein Klassifikator wirklich gut ist
Drei Aufgaben stechen heraus. Erstens die Stiltreue-QC: Ein Klassifikator meldet, wenn die Kennwerte einer Charge von ihrem deklarierten Stil abgedriftet sind, und erwischt etwa ein IPA, das in der Bitterkeit nach unten oder in der Farbe nach oben gerutscht ist, bevor es ausgeliefert wird. Zweitens die Wettbewerbs- und Kellersortierung: Bei Tausenden von Einreichungen kann ein Modell Biere in wahrscheinliche Kategorien vorsortieren und falsch deklarierte Einreichungen für einen menschlichen Steward markieren. Drittens das Rezept-Tagging: Eine unbeschriftete Rezeptdatenbank kann automatisch getaggt werden, sodass Brauer „zeig mir die Saisons" durchsuchen können, ohne manuell zu kuratieren.

Ein einfaches Modell bringt einen hier weit. Logistische Regression oder ein kleines Entscheidungsbaum-Ensemble, trainiert auf ein paar Hundert beschrifteten Beispielen, trennt die gut definierten Stile sauber. Der Wert liegt nicht in algorithmischer Raffinesse; er liegt in sauberen, konsistent gemessenen Merkmalen und einem ehrlichen, gut kuratierten Satz von Labels.

## Ein generativer-KI-Blickwinkel: die Grenze erklären
Das vorhergesagte Label ist nur die halbe Geschichte. Ein nützlicheres Werkzeug umhüllt den Klassifikator mit einem Sprachmodell, das erklärt, *warum* ein Bier dort liegt, wo es liegt. Frage „warum liegt dieses Rezept zwischen einem American Pale Ale und einem Session IPA?", und der Assistent kann auf die konkreten Merkmale verweisen, die die Mehrdeutigkeit verursachen: „Dein IBU von 38 und die Farbe von 8 EBC passen zu einem Pale Ale, aber die Stopfhopfen-Rate und 4,4 % ABV ziehen es in Richtung Session IPA." Das verwandelt eine nackte Wahrscheinlichkeit in einen Lehrmoment, auf den ein Brauer oder Juror reagieren kann, während der Mensch die letzte Entscheidung behält.

## Wo es versagt
Stile überschneiden sich und verschwimmen, und die Richtlinien sind bewusst unscharf. Die Grenze zwischen vielen benachbarten Kategorien ist eine Frage der Absicht und des sensorischen Charakters, keine saubere Linie im IBU-Raum. Hybride und experimentelle Biere passen per Definition nirgendwo hin. Die Kennwerte allein verfehlen auch die Aroma- und Geschmacksbeschreibungen, die einen Stil oft definieren, sodass zwei Biere mit identischen Zahlen zu verschiedenen Kategorien gehören können. Und die Labels in deinem Trainingsdatensatz tragen ihre eigene menschliche Verzerrung, denn sie spiegeln wider, wie Brauer ihre Biere eingereicht haben, nicht die tatsächliche Wahrheit.

Die tiefste Grenze ist dieselbe wie überall im Brauen: Das Modell klassifiziert messbare Eingaben, nicht Geschmack. Stiltreue auf dem Papier ist nicht dasselbe wie ein Bier, das ein gutes Beispiel seines Stils ist — und nur ein kalibriertes Panel klärt das.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Das Modell sortiert jede Probe anhand ihrer gemessenen Merkmale in eine Klasse."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">KLASSIFIZIERUNG</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Bierstile mit maschinellem Lernen klassifizieren</text><rect x="120" y="120" width="150" height="120" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="195" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#b45309">Klasse A</text><circle cx="145" cy="145" r="6" fill="#b45309"/><circle cx="177" cy="145" r="6" fill="#b45309"/><circle cx="209" cy="145" r="6" fill="#b45309"/><rect x="330" y="120" width="150" height="120" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="405" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#5b7a1f">Klasse B</text><circle cx="355" cy="145" r="6" fill="#5b7a1f"/><circle cx="387" cy="145" r="6" fill="#5b7a1f"/><circle cx="419" cy="145" r="6" fill="#5b7a1f"/><circle cx="451" cy="145" r="6" fill="#5b7a1f"/><rect x="540" y="120" width="150" height="120" rx="8" fill="#f7ece0" stroke="#7a1f3d" stroke-width="1.5"/><text x="615" y="232" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#7a1f3d">Klasse C</text><circle cx="565" cy="145" r="6" fill="#7a1f3d"/><circle cx="597" cy="145" r="6" fill="#7a1f3d"/><circle cx="629" cy="145" r="6" fill="#7a1f3d"/><circle cx="661" cy="145" r="6" fill="#7a1f3d"/><circle cx="565" cy="175" r="6" fill="#7a1f3d"/><text x="360" y="92" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">neue Probe → in die am besten passende Klasse sortiert</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Das Modell sortiert jede Probe anhand ihrer gemessenen Merkmale in eine Klasse.</figcaption>
</figure>

## Das Fazit
Bierstile aus OG, FG, ABV, IBU und Farbe zu klassifizieren ist eine saubere, zugängliche Aufgabe für maschinelles Lernen, die sich bei QC, Wettbewerbssortierung und Rezept-Tagging auszahlt. Eine generative Schicht kann erklären, warum ein Bier zwischen zwei Stilen liegt. Aber Stile sind unscharf und Kennwerte sind kein Geschmack — nutze das Label also als Anstoß für menschliches Urteilen statt als Ersatz dafür.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [Bierfarbe aus einem Rezept vorhersagen]({{ '/de/2021/predicting-beer-colour-recipe/' | relative_url }})

## Häufig gestellte Fragen

**Welche Merkmale nutzt ein Bierstil-Klassifikator?**
Vor allem die messbaren Kennwerte, die Stilrichtlinien wie das BJCP definieren: Stammwürze und Restextrakt, ABV, IBU sowie Farbe in SRM oder EBC, oft mit Zutaten-Markern wie Hopfensorte oder Malztyp. Das Modell ordnet diese Zahlen einem Stil-Label zu.

**Warum wird mein Bier als zwei verschiedene Stile klassifiziert?**
Weil sich Stilrichtlinien überschneiden. Ein American Pale Ale und ein Session IPA teilen einen großen Teil desselben OG-, IBU- und Farbraums, sodass ein Bier nahe der Grenze tatsächlich zwischen zwei Labels liegt — und ein guter Klassifikator beide mit Wahrscheinlichkeiten ausweist.

**Kann ein Klassifikator beurteilen, ob mein Bier gut ist?**
Nein. Er beurteilt die Stiltreue, also ob dein Bier auf dem Papier seinem deklarierten Stil entspricht. Qualität, Balance und Aroma sind eine separate Frage, die nur ein kalibriertes Sensorikpanel beantworten kann.
