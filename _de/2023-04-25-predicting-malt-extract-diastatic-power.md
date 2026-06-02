---
layout: post
lang: de
title: "Malzextrakt und diastatische Kraft vorhersagen, bevor du braust"
image: /assets/og/predicting-malt-extract-diastatic-power.png
description: "Sage Heißwasserextrakt und diastatische Kraft aus der Routine-Malzanalyse voraus, damit Brauer Schüttung und Maische vor einem Sud anpassen, nicht erst nach einem Ertragsausfall."
date: 2023-04-25
updated: 2023-04-25
permalink: /de/2023/predicting-malt-extract-diastatic-power/
tags: [brewing-science, malt, machine-learning]
faq:
  - q: "Was lässt sich aus einem Malz-Analysenzertifikat vorhersagen?"
    a: "Aus Routinewerten wie Eiweiß, Modifikation (Kolbach) und Feuchte lassen sich der Heißwasserextrakt — deine Ertragsobergrenze — und die diastatische Kraft, das Enzympotenzial für die Stärkeverzuckerung, vorhersagen."
  - q: "Garantiert die Vorhersage des Extrakts meinen Sudhausertrag?"
    a: "Nein. Das Modell sagt voraus, was das Malz liefern kann. Deine tatsächliche Ausbeute hängt weiterhin von Schroten, Maischen, Läutern und Transferverlusten in deinem eigenen Sudhaus ab."
  - q: "Warum ist die diastatische Kraft für die Schüttung wichtig?"
    a: "Die diastatische Kraft ist das Alpha- und Beta-Amylase-Potenzial, das Stärke umwandelt. Wenn eine Partie niedrig ist oder du viel enzymfreies Rohfrucht fährst, hast du möglicherweise nicht genug Enzym, um die Maische vollständig umzuwandeln."
---

**Kurze Antwort: Die Routine-Malzanalyse enthält bereits genug Signal, um den Heißwasserextrakt und die diastatische Kraft einer Partie vorherzusagen, sodass du Schüttung oder Maische vor dem Sud anpassen kannst statt erst nach einem Ertragsausfall.** Sie wird deine Sudhausausbeute nicht vorhersagen — nur, was das Malz zu liefern imstande ist.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsfluss sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSFLUSS</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Malzextrakt und diastatische Kraft vorhersagen, bevor du braust</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllung</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Bierproduktionsfluss sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Zwei Zahlen, die deine Obergrenze festlegen
Zwei Malzwerte prägen den ganzen Sud. Der Heißwasserextrakt ist deine Ertragsobergrenze: Er sagt dir, wie viel lösliches Material das Malz abgeben kann und damit die höchste Stammwürze, die du je aus dieser Schüttung ziehen kannst. Die diastatische Kraft ist das Enzympotenzial — die kombinierte Alpha- und Beta-Amylase-Aktivität —, das Stärke in der Maische umwandelt. Alpha-Amylase erzeugt Dextrine; Beta-Amylase erzeugt vergärbare Maltose. Ohne genug diastatische Kraft wird die Maische nicht vollständig umwandeln, und diese Grenze beißt am stärksten, wenn du dich auf enzymfreie Rohfrucht stützt.

Beide sind aus der Analyse vorhersagbar, die du ohnehin erhältst. Extrakt und diastatische Kraft korrespondieren mit Eiweiß, Modifikation (Kolbach-Index) und Feuchte auf eine Weise, die konsistent genug ist, um sie zu modellieren. Eine Partie, die übereiweißhaltig und untermodifiziert ankommt, neigt dazu, beim Extrakt unter den Erwartungen zu bleiben und sich in der Maische anders zu verhalten — und das willst du lieber an dem Tag wissen, an dem sie ankommt, als an dem Tag, an dem du im Sudkessel zu kurz kommst.

## Modellieren aus Daten, die du bereits hast
Das ist ein gut gestelltes Machine-Learning-Problem, gerade weil die Eingaben Routine sind. Jede Malzlieferung kommt mit einem Analysenzertifikat; die Merkmale — Eiweiß, Modifikation, Feuchte und, wo verfügbar, Mürbigkeit und Beta-Glucan — sind dieselben, die Mälzer berichten. Ein Modell, das auf deinen historischen Partien und ihrer tatsächlichen Leistung trainiert ist, lernt die Beziehung zwischen diesen Zahlen und dem Extrakt und der diastatischen Kraft, die du realisierst.

Die datenwissenschaftliche Disziplin besteht darin, zuerst zu messen und den Kreislauf zu erfassen. Protokolliere die Analyse jeder Partie zusammen mit den Sudergebnissen, die sie erzeugt hat, damit das Modell in deinem Malz und deiner Anlage verankert ist statt in einer generischen Regression aus dem Lehrbuch. Mit der Zeit lernt es die Eigenheiten deiner Lieferanten — welche Zahlen welches Mälzers optimistisch ausfallen, welche Sorte niedrig umwandelt — und genau dieses lokale Wissen kann ein Brauer aus einem einzelnen Zertifikat nicht gewinnen.

## Wo es bricht
Die scharfe Grenze ist der Geltungsbereich: Das Modell sagt das Malz voraus, nicht den Sud. Es sagt dir den Extrakt, den eine Partie liefern kann, und das Enzym, das sie trägt, aber es sagt nichts darüber, wie viel davon du ausbeutest. Schroten, Maischedichte, Zeit und Temperatur, Sparge- und Läuterverluste sitzen alle zwischen dem Potenzial des Malzes und der Stammwürze in deinem Sudkessel. Einen gesunden vorhergesagten Extrakt als garantierten Ertrag zu behandeln, ist der klassische Fehler — diese Frage gehört zu deinem Modell für [Maischeeffizienz und Extraktausbeute]({{ '/de/2023/predicting-mash-efficiency-extract-yield/' | relative_url }}), nicht zu diesem.

Die andere Grenze ist Data Drift. Wenn sich deine Lieferanten, Sorten oder Analysemethoden ändern, verschlechtern sich die Vorhersagen, bis das Modell neu lernt. Und ein Zertifikat misst einen beprobten Durchschnitt — echte Partien variieren innerhalb der Lieferung, eine Vorhersage ist also eine starke Erwartung, kein Versprechen.

## Ein Copilot für Schüttungs-Feinjustierungen
Der Aspekt der generativen KI ist ein Copilot, der den Kreislauf der Vorhersage schließt. Wenn der vorhergesagte Extrakt oder die diastatische Kraft einer Malzpartie von deinen Rezeptannahmen abweicht, erklärt der Copilot es klar und empfiehlt eine konkrete Anpassung: "Der vorhergesagte Extrakt von Partie 220 liegt 1,2 % unter Spezifikation und die diastatische Kraft ist eher niedrig — erhöhe die Schüttung um etwa 3 % und erwäge, enzymfreie Rohfrucht zu reduzieren, oder senke die Verzuckerungsrast, um die Umwandlung zu begünstigen." Er macht aus einer Zahl auf einem Zertifikat eine Brauentscheidung, bei der der Brauer abzeichnet, statt von Hand neu zu rechnen.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Was Malz treibt und was es stromabwärts verändert."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">WAS ES TREIBT</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Malzextrakt und diastatische Kraft vorhersagen, bevor du braust</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">Eingabe 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">Malz</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Qualität</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">Kosten / Risiko</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Was Malz treibt und was es stromabwärts verändert.</figcaption>
</figure>

## Das Fazit
Malzextrakt und diastatische Kraft aus der Routineanalyse vorherzusagen, ist eine der vertrauenswürdigeren Anwendungen von Machine Learning im Sudhaus, weil die Eingaben bereits existieren und die Physik gut verstanden ist. Nutze es, um Schüttung und Maische vor dem Sud anzupassen, halte es ehrlich darüber, ein Malzmodell zu sein statt eines Ertragsmodells, und speise es mit deiner eigenen Partienhistorie, damit es die Sprache deiner Lieferbasis spricht.

*Teil des Tracks [Brewing Science & AI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).* Verwandt: [Malzqualität aus Gerste vorhersagen]({{ '/de/2023/predicting-malt-quality-from-barley/' | relative_url }}).

## Häufig gestellte Fragen

**Was lässt sich aus einem Malz-Analysenzertifikat vorhersagen?**
Aus Routinewerten wie Eiweiß, Modifikation (Kolbach) und Feuchte lassen sich der Heißwasserextrakt — deine Ertragsobergrenze — und die diastatische Kraft, das Enzympotenzial für die Stärkeverzuckerung, vorhersagen.

**Garantiert die Vorhersage des Extrakts meinen Sudhausertrag?**
Nein. Das Modell sagt voraus, was das Malz liefern kann. Deine tatsächliche Ausbeute hängt weiterhin von Schroten, Maischen, Läutern und Transferverlusten in deinem eigenen Sudhaus ab.

**Warum ist die diastatische Kraft für die Schüttung wichtig?**
Die diastatische Kraft ist das Alpha- und Beta-Amylase-Potenzial, das Stärke umwandelt. Wenn eine Partie niedrig ist oder du viel enzymfreies Rohfrucht fährst, hast du möglicherweise nicht genug Enzym, um die Maische vollständig umzuwandeln.
