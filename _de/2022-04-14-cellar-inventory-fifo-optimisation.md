---
layout: post
lang: de
title: "Kellerbestand und FIFO-Optimierung mit KI"
image: /assets/og/cellar-inventory-fifo-optimisation.png
description: "Wie haltbarkeitsbewusstes FIFO und Zuteilung über Brauereitanks und Fertigware hinweg Verschwendung senken und dabei die Lieferquote halten — und wo der Ansatz scheitert."
date: 2022-04-14
updated: 2022-04-14
permalink: /de/2022/cellar-inventory-fifo-optimisation/
tags: [brewing-science, inventory, process-optimization]
faq:
  - q: "Warum braucht eine Brauerei mehr als einfaches FIFO?"
    a: "Reines FIFO verschickt zuerst den ältesten Bestand, was sinnvoll, aber grob ist. Bier ist sowohl in Drucktanks als auch als Fertigware verderblich, daher gewichtet ein haltbarkeitsbewusster Ansatz auch, wie viel Frische jede Bestellung braucht, was Umrüstungen kosten und welche Zuteilung die Lieferquote hoch und die Verschwendung niedrig hält — Entscheidungen, die einfaches FIFO ignoriert."
  - q: "Was wägt der Optimierer ab?"
    a: "Er wägt drei Dinge ab, die gegeneinander ziehen: Produktfrische, Lieferquote und Umrüstkosten. Das frischeste Bier an jede Bestellung zu verschicken maximiert die Qualität, kann aber älteren Bestand stranden lassen; Umrüstungen zu minimieren ist effizient, kann aber Bestand überaltern lassen. Der Optimierer findet eine Zuteilung, die alle drei respektiert."
  - q: "Lohnt sich das für eine kleine Brauerei?"
    a: "Oft nicht. Wenn du Bestand schnell umschlägst und selten etwas abschreibst, leistet die Tabelle gute Arbeit und ein Optimierer ist überdimensioniert. Der Nutzen zeigt sich, wenn du viele SKUs führst, Bestand lange genug hältst, dass Alterung echte Kosten verursacht, und nennenswertes Produkt durch Ablauf verlierst."
---

**Kurze Antwort: Haltbarkeitsbewusstes FIFO und Zuteilung senken Verschwendung, indem sie entscheiden, welchen verderblichen Bestand man wohin verschickt — und halten dabei trotzdem deine Lieferquote.** Bier altert im Drucktank ebenso wie auf der Palette, daher sind Bestandsentscheidungen still zeitkritisch. Optimierung kann sie schärfen — wenn das Problem groß genug ist, um es zu rechtfertigen.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Kellerbestand und FIFO-Optimierung mit KI</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Getreide</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Maische</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Kochen &amp; Hopfen</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Gärung</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#1c1a17">Abfüllung</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Wo dies im Bierproduktionsablauf steht, von Anfang bis Ende.</figcaption>
</figure>

## Warum Verderblichkeit das Bestandsspiel verändert
In vielen Branchen ist Bestand fungibel: ein Bauteil ist ein Bauteil. Bier nicht. Eine Charge hat eine Haltbarkeit, und ihr Wert für einen Kunden hängt davon ab, wie frisch sie ankommt. Diese Verderblichkeit zieht sich durch Gär- und Drucktanks ebenso wie durch Fertigware, die auf den Versand wartet. Das Ergebnis ist, dass zwei Entscheidungen, die auf einem Bestandsbericht identisch aussehen — Palette A oder Palette B versenden — sehr unterschiedliche Folgen für Verschwendung und Qualität haben können.

FIFO ist der vernünftige Standard: das Älteste zuerst bewegen. Aber es ist eine grobe Regel. Sie gewichtet nicht, wie viel Frische eine bestimmte Bestellung tatsächlich braucht, was eine Umrüstung zwischen SKUs an der Linie kostet oder wie eine Zuteilung heute morgen Bestand strandet. Haltbarkeitsbewusste Optimierung berücksichtigt diese Faktoren und balanciert Frische, Lieferquote und Umrüstungen über das gesamte Auftragsbuch hinweg, statt eine Zeile nach der anderen.

Dies liegt natürlich stromabwärts deines Brauplans — was du zuteilst, hängt davon ab, was du wann gemacht hast. Falls du ihn noch nicht gelesen hast: [KI für die Brauerei-Produktionsplanung]({{ '/de/2021/ai-brewery-production-scheduling/' | relative_url }}) behandelt die vorgelagerte Entscheidung, die diese hier speist.

## Erst messen: Haltbarkeitsdaten sind das Fundament
Nichts davon funktioniert ohne vertrauenswürdige Verderblichkeitsdaten. Du brauchst echte Abfülldaten, echte Mindesthaltbarkeitslogik je Produkt und eine Bestandsaufzeichnung, die tatsächlich mit dem Keller übereinstimmt. Die Disziplin ist die vertraute — den Prozess messen, bevor man ihn modelliert. Wenn dein Bestandssystem sagt, ein Tank sei voll, obwohl er letzte Woche geleert wurde, wird der Optimierer selbstbewusst Bier zuteilen, das nicht existiert.

Die erste Aufgabe ist also nicht der Algorithmus; es sind genaue, aktuelle Bestands- und Haltbarkeitsdaten. Mach das richtig, und schon einfaches haltbarkeitsbewusstes FIFO senkt Verschwendung. Mach es falsch, und der ausgefeilteste Optimierer automatisiert schlicht deine Fehler im Tempo.

## Wo es scheitert
Zwei ehrliche Grenzen. Die erste ist Datenqualität. Verderblichkeitsoptimierung reagiert akut empfindlich auf falsche Daten und veraltete Bestandsaufzeichnungen — mehr als die Planung, denn der ganze Sinn ist es, über Alter zu schließen. Wenn diese Eingaben wacklig sind, setze noch nicht ein.

Die zweite ist Skala. Für eine kleine Brauerei, die Bestand schnell umschlägt, mit wenigen SKUs und vernachlässigbaren Abschreibungen, ist das Über-Engineering. Die ehrliche Antwort ist, dass eine saubere FIFO-Tabelle das richtige Werkzeug ist, bis Verschwendung, SKU-Anzahl und Haltezeiten so weit wachsen, dass die Abwägungen wirklich beißen. Optimierung verdient ihren Platz, indem sie Kosten senkt, die man tatsächlich messen kann; wenn diese Kosten nahe null sind, lass es bleiben.

## Ein praktischer Gen-KI-Blickwinkel
Ein bescheidener, gut geerdeter Einsatz generativer KI passt hier sauber. Ein Copilot, der Bestandsalter beobachtet, kann markieren, welche Lose Gefahr laufen, abzulaufen, bevor sie voraussichtlich verschickt werden, und den Zuteilungshinweis oder die Kundenkommunikation entwerfen, die zur Umleitung gehört — „Los 1142 ist neun Tage vom Mindesthaltbarkeitsdatum entfernt; Vorschlag: dem Großhandelslauf am Dienstag zuteilen." Es bringt den gefährdeten Bestand ans Licht, den ein vielbeschäftigter Kellermeister sonst übersehen würde, und macht die Entscheidung zu einem schnellen Ja oder Nein. Wie immer muss es aus der echten Bestandsaufzeichnung lesen und die Lose zitieren, nicht erfinden.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein geschlossener Regelkreis: messen, rechnen, stellen — dann das Ergebnis zurückspeisen."><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">REGELKREIS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Kellerbestand und FIFO-Optimierung mit KI</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Regler</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Aktor</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#1c1a17">Prozess</text><g fill="#b45309" stroke="#b45309" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#7a1f3d" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#7a1f3d"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#7a1f3d">Rückkopplung</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Ein geschlossener Regelkreis: messen, rechnen, stellen — dann das Ergebnis zurückspeisen.</figcaption>
</figure>

## Das Fazit
Haltbarkeitsbewusstes FIFO und Zuteilung senken Verschwendung und schützen zugleich die Lieferquote, indem sie Bier als das verderbliche, zeitkritische Produkt behandeln, das es ist. Der Haken ist, dass es vollständig von genauen Bestands- und Haltbarkeitsdaten abhängt und sich erst auszahlt, sobald deine SKU-Anzahl und Haltezeiten Alterung zu echten Kosten machen — kleine, schnell umschlagende Brauereien sollten beim einfachen FIFO bleiben. Erst messen, dort einsetzen, wo Verschwendung wirklich messbar ist, und einen geerdeten Copiloten die gefährdeten Lose markieren lassen.

*Teil des Tracks [Brauwissenschaft & KI]({{ '/de/tracks/brewing-science-ai/' | relative_url }}).*

## Häufig gestellte Fragen

**Warum braucht eine Brauerei mehr als einfaches FIFO?**
Reines FIFO verschickt zuerst den ältesten Bestand, was sinnvoll, aber grob ist. Bier ist sowohl in Drucktanks als auch als Fertigware verderblich, daher gewichtet ein haltbarkeitsbewusster Ansatz auch, wie viel Frische jede Bestellung braucht, was Umrüstungen kosten und welche Zuteilung die Lieferquote hoch und die Verschwendung niedrig hält — Entscheidungen, die einfaches FIFO ignoriert.

**Was wägt der Optimierer ab?**
Er wägt drei Dinge ab, die gegeneinander ziehen: Produktfrische, Lieferquote und Umrüstkosten. Das frischeste Bier an jede Bestellung zu verschicken maximiert die Qualität, kann aber älteren Bestand stranden lassen; Umrüstungen zu minimieren ist effizient, kann aber Bestand überaltern lassen. Der Optimierer findet eine Zuteilung, die alle drei respektiert.

**Lohnt sich das für eine kleine Brauerei?**
Oft nicht. Wenn du Bestand schnell umschlägst und selten etwas abschreibst, leistet die Tabelle gute Arbeit und ein Optimierer ist überdimensioniert. Der Nutzen zeigt sich, wenn du viele SKUs führst, Bestand lange genug hältst, dass Alterung echte Kosten verursacht, und nennenswertes Produkt durch Ablauf verlierst.
