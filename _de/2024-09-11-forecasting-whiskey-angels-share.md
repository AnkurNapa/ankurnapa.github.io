---
layout: post
lang: de
title: "Den Angels' Share prognostizieren: Verdunstungsverlust im Fass modellieren"
image: /assets/og/forecasting-whiskey-angels-share.png
description: "Wie KI und Data Science den Angels' Share, den jährlichen Fassverdunstungsverlust von etwa 2 %, prognostizieren, um Füllmengen zu planen und reifenden Whisky-Bestand zu bewerten."
date: 2024-09-11
updated: 2024-09-11
permalink: /de/2024/forecasting-whiskey-angels-share/
tags: [distilling-maturation, whiskey, inventory]
faq:
  - q: "Wie viel Whisky geht an den Angels' Share verloren?"
    a: "Rund 2 % des Fassvolumens pro Jahr, wobei es mit Lagerhaustemperatur und -feuchtigkeit, Klima, Fassgröße und -position variiert. Über eine lange Reifung summiert sich das zu einem erheblichen Anteil der ursprünglichen Füllung."
  - q: "Kann ein Modell den Verdunstungsverlust genau prognostizieren?"
    a: "Es kann den durchschnittlichen Verlust über ein Lagerhaus gut prognostizieren, weil die Treiber physikalisch und wiederholbar sind. Die Präzision je Fass ist schwerer, da Position, Holz und Dichtung von Fass zu Fass variieren und Wiegedaten meist spärlich sind."
  - q: "Welche Daten brauche ich, um den Angels' Share zu prognostizieren?"
    a: "Fass-Füllmengen und -Stärken, Fasstyp und -größe, Position im Lagerhaus und periodische Wiegungen oder Peilungen. Protokolle von Lagerhaustemperatur und -feuchtigkeit machen die Prognose erheblich zuverlässiger."
---

**Kurze Antwort: Der Angels' Share ist vorhersehbar genug, um ihn einzuplanen, denn die Verdunstung wird von Physik getrieben, die du messen kannst, selbst wenn dich ein einzelnes Fass noch überrascht.** Modelliere den Verlust, und du füllst, prognostizierst Ausbeute und bewertest Bestand mit weit weniger Raten.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Whiskey-Produktionsfluss steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSFLUSS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Den Angels&#39; Share prognostizieren: Verdunstungsverlust im Fass modellieren</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maischen</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gären</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Destillieren</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Reifen</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllen</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Whiskey-Produktionsfluss steht, von Anfang bis Ende.</figcaption>
</figure>

## Ein 2-%-Problem, das sich aufsummiert
Reifender Brand verliert durch Verdunstung über das Holz Volumen, den Angels' Share, mit rund 2 % pro Jahr. Das klingt klein, bis es sich aufsummiert. Über ein oder zwei Jahrzehnte entzieht es einen bedeutenden Anteil der ursprünglichen Füllung, und weil es mit Lagerhaustemperatur und -feuchtigkeit, Klima, Fassgröße und -position variiert, ist der Verlust ungleichmäßig und Fass für Fass schwer vorherzusagen. Ein warmes, trockenes Rackhouse verliert Brand schneller; ein kühles, feuchtes Dunnage-Lagerhaus verliert weniger, verschiebt aber die Stärke anders.

Das ist nicht nur Schwund. Es verändert, wie viel du abfüllen kannst, wann ein Fass unter eine tragfähige Füllung oder Stärke fällt und was dein reifender Bestand tatsächlich wert ist. Liegst du mit der Prognose falsch, füllst du Jahre im Voraus zu viel oder zu wenig, ohne Möglichkeit, das später zu korrigieren.

## Physik in eine Prognose verwandeln
Die Treiber der Verdunstung sind physikalisch, was genau der Grund ist, warum ein Modell sie lernen kann. Zuerst messen: Protokolliere Lagerhaustemperatur und -feuchtigkeit nach Zone und Höhe, erfasse Fasstyp, -größe, Füllstärke und -position und wiege oder peile Fässer periodisch. Diese Merkmale speisen ein Modell, das die Verlustrate als Funktion der Bedingungen vorhersagt, statt pauschale 2 % auf alles anzuwenden.

Auf Lagerhausebene sind die Prognosen wirklich nützlich, weil sich die starken Treiber, Klima, Fassgröße, Lagerhauszone, Jahr für Jahr wiederholen. Das Modell sagt dir, wie viel Brand eine bestimmte Füllung im Zielalter ergeben wird, sodass du Füllmengen planen kannst, um eine Abfüllung zu treffen, und den reifenden Bestand mit einer echten Verlustkurve statt einer Faustregel bewertest. Verbinde das damit, wie du Fässer auswählst und das Kapital im reifenden Bestand steuerst, behandelt in [KI für Fassauswahl und Bestand]({{ '/de/2024/ai-cask-selection-inventory/' | relative_url }}), und die Prognose hört auf, eine buchhalterische Kuriosität zu sein, und wird zu einem Planungshebel.

## Wo die Prognose ausfranst
Die ehrliche Grenze ist das einzelne Fass. Position, Holzqualität, Dichtungsintegrität und vorheriger Inhalt variieren, sodass zwei benachbarte Fässer, am selben Tag befüllt, mit merklich unterschiedlichen Raten verlieren können. Das Modell trifft den Durchschnitt und die Lagerhaussumme; viel schwächer ist es bei der Vorhersage, welches spezifische Fass am meisten verlieren wird.

Zwei Datenprobleme verschärfen das. Jedes Fass zu wiegen ist Arbeit, sodass die meisten Brennereien selten und spärlich wiegen und das Modell ohne genau das Signal lassen, das es braucht. Und die Horizonte sind lang: Eine Prognose über fünfzehn oder zwanzig Jahre extrapoliert weit über die Bedingungen in deinen Daten hinaus, und ein wärmer werdendes Klima entwertet still die historischen Verlustraten, aus denen das Modell gelernt hat. Behandle Langfristprognosen als Spannen, nicht als Punkte, und passe sie neu an, sobald frische Wiegungen eintreffen.

## Ein Copilot für die Bestandsnotiz
Der generative Blickwinkel ist praktisch statt glamourös. Ein Copilot kann die Verlustprojektionen des Modells nehmen und die Bestandsnotiz entwerfen, die die Finanzabteilung tatsächlich liest: projizierte Bestandsverluste nach Lagerhaus und Jahrgang, die Fässer, die sich der minimal tragfähigen Füllung nähern, und die Ausbeuteimplikationen für den Abfüllplan des nächsten Jahres, in einfacher Sprache mit angegebenen Annahmen geschrieben. Das spart dem Analysten Stunden und macht, noch wichtiger, die Prognose lesbar für Menschen, die das Modell nie öffnen werden. Das Mikroklima, das viel dieser Variation treibt, ist selbst optimierbar; siehe [Optimierung des Rackhouse-Mikroklimas]({{ '/de/2024/ai-rackhouse-microclimate-optimization/' | relative_url }}).

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">PROGNOSE</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Den Angels&#39; Share prognostizieren: Verdunstungsverlust im Fass modellieren</text><g stroke="#1c1a17" stroke-width="1.5"><line x1="60" y1="70" x2="60" y2="250"/><line x1="60" y1="250" x2="680" y2="250"/></g><polygon points="430,150 540,118 660,96 660,150 540,168 430,180" fill="#b45309" opacity="0.15"/><polyline points="60,210 150,182 240,196 330,150 430,162" fill="none" stroke="#b45309" stroke-width="3"/><polyline points="430,162 540,140 660,120" fill="none" stroke="#7a1f3d" stroke-width="3" stroke-dasharray="6 4"/><line x1="430" y1="70" x2="430" y2="250" stroke="#6b6258" stroke-width="1" stroke-dasharray="3 3"/><text x="430" y="86" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">heute</text><text x="230" y="244" text-anchor="middle" font-family="sans-serif" font-size="11.5" fill="#6b6258">Historie</text><text x="560" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">Prognose</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Historie (durchgezogen) und die Vorwärtsprognose des Modells (gestrichelt); das schattierte Band ist seine Unsicherheit.</figcaption>
</figure>

## Das Fazit
Du kannst den Angels' Share auf Lagerhaus- und Jahrgangsebene gut prognostizieren, und das reicht, um Füllungen zu planen, Ausbeute zu projizieren und reifenden Bestand mit Zuversicht zu bewerten. Die Präzision je Fass und Horizonte über mehrere Jahrzehnte bleiben wirklich schwer, also modelliere den Durchschnitt, wiege häufiger als jetzt und gib Spannen für die langen Wetten an.

*Teil des Tracks [Destillation & Reifung]({{ '/de/tracks/distilling-maturation/' | relative_url }}).*

## Häufig gestellte Fragen

**Wie viel Whisky geht an den Angels' Share verloren?**
Rund 2 % des Fassvolumens pro Jahr, wobei es mit Lagerhaustemperatur und -feuchtigkeit, Klima, Fassgröße und -position variiert. Über eine lange Reifung summiert sich das zu einem erheblichen Anteil der ursprünglichen Füllung.

**Kann ein Modell den Verdunstungsverlust genau prognostizieren?**
Es kann den durchschnittlichen Verlust über ein Lagerhaus gut prognostizieren, weil die Treiber physikalisch und wiederholbar sind. Die Präzision je Fass ist schwerer, da Position, Holz und Dichtung von Fass zu Fass variieren und Wiegedaten meist spärlich sind.

**Welche Daten brauche ich, um den Angels' Share zu prognostizieren?**
Fass-Füllmengen und -Stärken, Fasstyp und -größe, Position im Lagerhaus und periodische Wiegungen oder Peilungen. Protokolle von Lagerhaustemperatur und -feuchtigkeit machen die Prognose erheblich zuverlässiger.
