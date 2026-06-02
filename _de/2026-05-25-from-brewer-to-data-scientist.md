---
layout: post
lang: de
title: "Vom Brauer zum Data Scientist: Warum ich das Sudhaus gegen KI eintauschte (und es nie wirklich verließ)"
image: /assets/og/from-brewer-to-data-scientist.png
description: "Wie ich vom Bierentwickler bei AB InBev und SABMiller zum KI-Bauer für Brauereien wurde — und warum ein Brauhintergrund in der Data Science ein Vorteil ist, kein Handicap."
date: 2026-05-25 12:00:00 -0700
updated: 2026-05-25
permalink: /de/2026/from-brewer-to-data-scientist/
tags: [brewer-to-ai, career, data-science, brewing]
faq:
  - q: "Kann ein Brauer Data Scientist werden?"
    a: "Ja. Brauen ist bereits eine datenreiche Prozesssteuerungsdisziplin, also verstehen Brauer die Domäne besser, als es die meisten Data Scientists je tun werden. Die Lücke sind Werkzeuge und Statistik, die erlernbar sind — die hart erarbeitete Domänenintuition ist es nicht."
  - q: "Muss man das Brauen aufgeben, um in der KI zu arbeiten?"
    a: "Nein. Die nützlichste KI-Arbeit bei Getränken kommt von Menschen, die noch wie Brauer denken. Ich habe das Brauen nicht aufgegeben; ich habe Datenfähigkeiten obendrauf gepackt."
  - q: "Was macht Brauer gut in der Data Science?"
    a: "Brauer denken bereits über Variablen, Prozesssteuerung, Messung und Ursache-Wirkung unter Unsicherheit nach. Diese Denkweise überträgt sich direkt auf die Datenarbeit — oft leichter, als Data Scientists das Brauen aufgreifen."
---

**Kurze Antwort: Ja, ein Brauer kann Data Scientist werden — und Brauen ist eine ungewöhnlich gute Startrampe dafür. Ich habe rund ein Jahrzehnt in Brauereien verbracht, bevor Daten meine Karriere übernahmen, und die Wahrheit ist, dass ich das Brauen nie hinter mir gelassen habe. Das Domänenwissen erwies sich als der schwer zu erwerbende Teil; die Datenfähigkeiten waren der Teil, den ich lernen konnte.** So ist es passiert.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Von Rohdaten zu einer Entscheidung, auf die das Team reagieren kann — die Pipeline hinter diesem Beitrag."><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">DATEN → ENTSCHEIDUNG</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Vom Brauer zum Data Scientist: Warum ich das Sudhaus gegen KI eintauschte (und es nie wirklich…</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Daten</text><text x="90.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">Sensoren, Protokolle</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="289.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Merkmale</text><text x="289.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">bereinigen &amp; formen</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="488.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Modell</text><text x="488.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">trainieren / bewerten</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="687.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Vorhersage</text><text x="687.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">was als Nächstes passiert</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="886.0" y="151.0" text-anchor="middle" font-size="15" font-weight="700" fill="#1c1a17">Aktion</text><text x="886.0" y="175.0" text-anchor="middle" font-size="12.5" fill="#6b6258">das Team handelt</text></g><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Von Rohdaten zu einer Entscheidung, auf die das Team reagieren kann — die Pipeline hinter diesem Beitrag.</figcaption>
</figure>

## Ich begann dort, wo die meisten Brauer beginnen

Ich habe mich durch Mikrobrauereien hochgearbeitet, bevor ich mit den großen Namen arbeitete: AB InBev, SABMiller, United Breweries. Unterwegs habe ich ein Dutzend Biere für den indischen Markt entwickelt. Meine Ausbildung war klassisch: ein B.Tech in Biotechnologie, dann ein MSc in Brewing Science & Technology.

Das ist der Lebenslauf eines Brauers. Nichts daran sagt „KI".

## Daten schlichen durch die Seitentür herein

Hier ist das, was dir niemand sagt: Brauen *ist* eine Datendisziplin. Jeder Sud ist ein kontrolliertes Experiment — Temperaturkurven, Stammwürzemessungen, Anstellraten, Sensorikpanels. Ich lebte bereits in Tabellenkalkulationen und Prozessprotokollen. Mit der Zeit verschob sich meine Rolle vom Bierbrauen zum Sinnstiften der Zahlen dahinter, und ich bewegte mich vom Trainee hin zu einer Senior-Datenanalysten-Rolle.

Ich entschied nicht, „Data Scientist zu werden". Ich folgte den Fragen, die das Bier mir immer wieder stellte — *warum hat dieser Sud anders vergoren? welche Biere werden sich nächsten Monat verkaufen?* — und diese Fragen führten geradewegs in die Daten.

## Warum Brauen einem Informatikstudium dafür überlegen ist

Die Überraschung meiner Karriere: Mein Brauhintergrund war ein *Vorteil*, kein Handicap. Ein reiner Data Scientist kann ein Modell bauen, aber er weiß nicht, wie sich eine steckengebliebene Gärung anfühlt oder warum ein Verkaufsanstieg im Sommer kein Zufall ist. Ich wusste es. Domänenintuition ist das teure, langsam zu erwerbende Gut — und ich hatte es bereits. Die Statistik und Python waren der erlernbare Teil.

Wenn du Brauer bist und diesen Weg ins Auge fasst, ist das die Umdeutung: Du startest nicht bei null. Du startest mit der Hälfte, die am schwersten zu lehren ist.

## Was diese Serie ist

Das ist die ehrliche, achtteilige Geschichte dieser Verwandlung — und ein praktischer Leitfaden, falls du sie gehen willst. Wir behandeln, [was KI tatsächlich für einen Brauer bedeutet]({{ '/de/2026/what-ai-means-for-a-brewer/' | relative_url }}), die unglamourösen ersten Schritte, meine echten Projekte und — ebenso wichtig — [wo KI mich verbrannt hat]({{ '/de/2026/where-ai-burned-me/' | relative_url }}). Sie baut auf dem größeren Bild auf, [was KI für eine Brauerei kann und nicht kann]({{ '/de/2026/what-can-ai-do-for-a-brewery/' | relative_url }}).

Ich denke immer noch wie ein Brauer. Das ist der ganze Punkt.

*Vom Brauer zur KI — Teil 1 von 8. [Die ganze Serie ansehen]({{ '/de/series/brewer-to-ai/' | relative_url }}) · [Weiter: Was KI tatsächlich für einen Brauer bedeutet →]({{ '/de/2026/what-ai-means-for-a-brewer/' | relative_url }})*

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 260" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Die wenigen Zahlen, auf die es ankommt."><rect x="0" y="0" width="720" height="260" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">DIE ZAHLEN</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Vom Brauer zum Data Scientist: Warum ich das Sudhaus gegen KI eintauschte (und es nie…</text><rect x="70" y="90" width="160" height="120" rx="10" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="90" y="120" font-family="sans-serif" font-size="12" fill="#6b6258">Kennzahl 1</text><rect x="90" y="135" width="120" height="22" rx="3" fill="#b45309"/><text x="90" y="190" font-family="sans-serif" font-size="11.5" fill="#6b6258">vs. Ziel</text><rect x="280" y="90" width="160" height="120" rx="10" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="300" y="120" font-family="sans-serif" font-size="12" fill="#6b6258">Kennzahl 2</text><rect x="300" y="135" width="100" height="22" rx="3" fill="#b45309"/><text x="300" y="190" font-family="sans-serif" font-size="11.5" fill="#6b6258">vs. Ziel</text><rect x="490" y="90" width="160" height="120" rx="10" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="510" y="120" font-family="sans-serif" font-size="12" fill="#6b6258">Kennzahl 3</text><rect x="510" y="135" width="80" height="22" rx="3" fill="#b45309"/><text x="510" y="190" font-family="sans-serif" font-size="11.5" fill="#6b6258">vs. Ziel</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Die wenigen Zahlen, auf die es ankommt.</figcaption>
</figure>

## Häufig gestellte Fragen

**Kann ein Brauer Data Scientist werden?**
Ja. Brauen ist bereits eine datenreiche Prozesssteuerungsdisziplin, also verstehen Brauer die Domäne besser, als es die meisten Data Scientists je tun werden. Die Lücke sind Werkzeuge und Statistik, die erlernbar sind — die hart erarbeitete Domänenintuition ist es nicht.

**Muss man das Brauen aufgeben, um in der KI zu arbeiten?**
Nein. Die nützlichste KI-Arbeit bei Getränken kommt von Menschen, die noch wie Brauer denken. Ich habe das Brauen nicht aufgegeben; ich habe Datenfähigkeiten obendrauf gepackt.

**Was macht Brauer gut in der Data Science?**
Brauer denken bereits über Variablen, Prozesssteuerung, Messung und Ursache-Wirkung unter Unsicherheit nach. Diese Denkweise überträgt sich direkt auf die Datenarbeit — oft leichter, als Data Scientists das Brauen aufgreifen.
