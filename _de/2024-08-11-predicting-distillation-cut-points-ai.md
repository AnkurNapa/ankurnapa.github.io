---
layout: post
lang: de
title: "Kann KI die Brennschnitte (Vorlauf, Mittellauf, Nachlauf) wählen?"
image: /assets/og/predicting-distillation-cut-points-ai.png
description: "Kann KI Brennschnitte wählen? Wie Modelle ABV-, Temperatur-, Zeit- und Kongener-Daten nutzen, um Vorlauf-, Mittellauf- und Nachlaufschnitte konsistenter zu machen."
date: 2024-08-11
updated: 2024-08-11
permalink: /de/2024/predicting-distillation-cut-points-ai/
tags: [distilling-maturation, whiskey, process-optimization]
faq:
  - q: "Kann KI die Nase des Brennmeisters ersetzen?"
    a: "Nein. Ein Modell kann einen Schnittpunkt aus ABV-, Temperatur-, Zeit- und Kongener-Signalen empfehlen, aber das sensorische Urteil bleibt der Schiedsrichter. Behandle es als Zweitmeinung, die die Konsistenz verbessert, nicht als Ersatz."
  - q: "Welche Daten brauche ich, um Schnittpunkte zu modellieren?"
    a: "Mindestens protokollierte ABV-, Temperatur- und Zeitwerte über den Feinbrand hinweg, wobei jeder Sud damit beschriftet ist, wo der Brennmeister tatsächlich geschnitten hat. Inline-Spektroskopie oder Kongener-Sensoren helfen, sind aber zum Start nicht zwingend."
  - q: "Funktioniert das für Kolonnenbrennblasen ebenso wie für Pot Stills?"
    a: "Die Idee überträgt sich, aber das Problem unterscheidet sich. Pot-Still-Schnitte sind Chargenentscheidungen bei fallendem ABV; Kolonnenbrennblasen laufen kontinuierlich, sodass das Modell stationäre Abzugspunkte anstrebt statt diskreter Vorlauf-, Mittellauf- und Nachlaufschnitte."
---

**Kurze Antwort: Ja, ein Modell kann empfehlen, wo zu schneiden ist, aber nur als disziplinierte Zweitmeinung für einen Brennmeister, der weiterhin der Nase vertraut.** Der Schnitt definiert den Hauscharakter, also ist das Ziel Konsistenz, nicht Autonomie.

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Wo dies im Whiskey-Produktionsablauf sitzt, von Anfang bis Ende."><rect x="0" y="0" width="1000" height="270" fill="#ffffff"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">PRODUKTIONSABLAUF</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#06483f">Kann KI die Brennschnitte (Vorlauf, Mittellauf, Nachlauf) wählen?</text><g font-family="sans-serif"><rect x="4" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="90.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Maischen</text><rect x="203" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="289.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Gären</text><rect x="402" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="488.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Destillieren</text><rect x="601" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="687.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Reifen</text><rect x="800" y="80" width="172" height="150" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="886.0" y="160.0" text-anchor="middle" font-size="15.5" font-weight="700" fill="#06483f">Abfüllen</text></g><g fill="#00695c" stroke="#00695c" stroke-width="2"><line x1="176" y1="155.0" x2="196" y2="155.0"/><polygon points="196,150.0 203,155.0 196,160.0" stroke="none"/><line x1="375" y1="155.0" x2="395" y2="155.0"/><polygon points="395,150.0 402,155.0 395,160.0" stroke="none"/><line x1="574" y1="155.0" x2="594" y2="155.0"/><polygon points="594,150.0 601,155.0 594,160.0" stroke="none"/><line x1="773" y1="155.0" x2="793" y2="155.0"/><polygon points="793,150.0 800,155.0 793,160.0" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Wo dies im Whiskey-Produktionsablauf sitzt, von Anfang bis Ende.</figcaption>
</figure>

## Was der Schnitt tatsächlich entscheidet
Der Feinbrand wird in drei Teile geteilt. Vorlauf und Heads kommen zuerst: hoch im ABV, flüchtig, tragen niedrigsiedende Kongenere, Methanol, Acetaldehyd und leichte Ester, die du nicht willst. Das Herzstück, der Mittellauf, ist der Bewahrenswerte, gesammelt von einem hohen ABV hinunter auf grob 60-65 % ABV in einer Pot Still. Feints und Nachlauf kommen zuletzt: niedrig im ABV, schwer von Fuselölen und öligen Kongeneren.

Heute werden diese Schnittpunkte vom Brennmeister anhand von ABV, Temperatur, Zeit und Nase gesetzt. Das funktioniert, aber es überträgt sich schlecht. Ein neuer Bediener, eine müde Schicht oder eine leicht abweichende Maische verschiebt den Schnitt, und der Rohbrand driftet. Schnittkonsistenz ist ein messbares Qualitätsproblem, das sich in einer handwerklichen Entscheidung versteckt.

## Wo ein Modell hilft
Erst messen. Die Merkmale liegen bereits an der Brennblase vor: ABV über den Brand, Dampf- und Spirituosentemperatur, verstrichene Zeit und die Form, wie der ABV fällt. Beschrifte jeden historischen Sud damit, wo der Schnitt tatsächlich gesetzt wurde und wie der resultierende Rohbrand auf dem Prüftisch und an der Nase abschnitt. Ein überwachtes Modell lernt dann die Beziehung zwischen der Bahn des Brands und einem guten Schnitt.

Der Nutzen ist Wiederholbarkeit. Statt dass jeder Brennmeister auf private Faustregeln zurückgreift, kodiert das Modell die besten Schnitte der Brennerei selbst und markiert, wenn ein Brand von seinem üblichen Pfad abweicht. Wo das Budget es erlaubt, schärfen Inline-Spektroskopie oder Kongener-Sensoren das Signal und lassen das Modell auf die tatsächliche Chemie reagieren statt auf den ABV als Stellvertreter. Das zählt am meisten am hinteren Ende, wo die Linie zwischen einem sauberen Herzstück und fuselbeladenem Nachlauf dünn ist.

Für kontinuierliche Betriebe ändert sich die Rahmung. Eine Kolonnenbrennblase macht keine diskreten Vorlauf-, Mittellauf- und Nachlaufschnitte; sie zieht im stationären Zustand ab. Dort optimiert das Modell Abzugsböden und Rücklauf, um ein Ziel-Kongener-Profil zu halten, statt einen einzelnen Schnittmoment auszurufen.

## Wo es scheitert
Sei ehrlich über die Grenzen. Die Nase zählt weiterhin: Manche Fehlnoten, insbesondere Schwefel und bestimmte Ester, werden von einem geschulten Menschen lange erfasst, bevor irgendein bezahlbarer Sensor sie sieht. Spektroskopie und Kongener-Analysatoren sind teuer, und viele Brennereien haben sie schlicht nicht inline. Am wichtigsten: Der Schnitt ist der Ort, an dem der Hauscharakter entsteht. Ein auf den Schnitten des letzten Jahres trainiertes Modell reproduziert getreu den Stil des letzten Jahres, einschließlich seiner Fehler, und eine selbstbewusst-falsche Empfehlung bei einem hochwertigen Brand ist kostspielig. Belasse die letzte Entscheidung beim Menschen und validiere gegen das Sensorische, bevor du irgendeinem automatisierten Schnitt vertraust.

Es gibt auch ein Kaltstartproblem. Mit nur einer Handvoll beschrifteter Brände hat das Modell wenig, woraus es lernen kann, und seltene Ereignisse — eine ungewöhnlich langsame Gärung, ein Kupferfehler — sind genau dann unterrepräsentiert, wenn Anleitung am meisten helfen würde.

## Ein generativer Aspekt, den man haben sollte
Die nützlichste generative KI hier ist ein Copilot, kein Autopilot. Stell dir einen Assistenten vor, der den Brand beobachtet, einen Schnittpunkt empfiehlt und den Zielkonflikt in Klartext erklärt: „Jetzt zu schneiden behält ein fruchtigeres, esterbetontes Herzstück, opfert aber rund zwei Liter Ausbeute; 90 Sekunden zu halten fügt Körper hinzu, mit dem Risiko frühen Fuselübertrags." Diese Erklärung ist es, was ein Modell zu einem Schulungswerkzeug macht. Neue Brennmeister lernen schneller, wenn die Begründung ausbuchstabiert ist, und die Brennerei erfasst ihr stillschweigendes Wissen, statt es zu verlieren, wenn ein erfahrener Bediener in den Ruhestand geht.

Der Schnitt, den du an der Brennblase machst, formt alles Nachgelagerte, also lohnt es sich, dies damit zu verbinden, wie du den [Geschmack des Rohbrands vorhersagst]({{ '/de/2024/predicting-new-make-spirit-flavor/' | relative_url }}) und den Charakter steuerst, bevor die Spirituose je ein Fass erreicht.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen."><rect x="0" y="0" width="720" height="300" fill="#ffffff"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#00695c">REGELKREIS</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#06483f">Kann KI die Brennschnitte (Vorlauf, Mittellauf, Nachlauf) wählen?</text><rect x="70" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="130" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Sensor</text><rect x="250" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="310" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Regler</text><rect x="430" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="490" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Stellglied</text><rect x="610" y="120" width="120" height="60" rx="8" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/><text x="670" y="155" text-anchor="middle" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#06483f">Prozess</text><g fill="#00695c" stroke="#00695c" stroke-width="2.5"><line x1="190" y1="150" x2="242" y2="150"/><polygon points="242,143 250,150 242,157" stroke="none"/><line x1="370" y1="150" x2="422" y2="150"/><polygon points="422,143 430,150 422,157" stroke="none"/><line x1="550" y1="150" x2="602" y2="150"/><polygon points="602,143 610,150 602,157" stroke="none"/></g><path d="M670,180 L670,240 L130,240 L130,180" fill="none" stroke="#06483f" stroke-width="2" stroke-dasharray="5 4"/><polygon points="124,186 130,178 136,186" fill="#06483f"/><text x="400" y="234" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#06483f">Rückführung</text></svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Ein geschlossener Regelkreis: messen, berechnen, stellen — dann das Ergebnis zurückführen.</figcaption>
</figure>

## Das Fazit
KI kann Schnittpunkte konsistenter machen und das Urteil eines erfahrenen Brennmeisters in einen geteilten, lehrbaren Standard verwandeln. Sie kann und sollte die Entscheidung nicht der Person abnehmen, die das Glas hält. Beginne damit, deine Brände zu protokollieren und deine Schnitte zu beschriften; das Modell ist der einfache Teil.

*Teil des Tracks [Distilling & Maturation]({{ '/de/tracks/distilling-maturation/' | relative_url }}).*

## Häufig gestellte Fragen

**Kann KI die Nase des Brennmeisters ersetzen?**
Nein. Ein Modell kann einen Schnittpunkt aus ABV-, Temperatur-, Zeit- und Kongener-Signalen empfehlen, aber das sensorische Urteil bleibt der Schiedsrichter. Behandle es als Zweitmeinung, die die Konsistenz verbessert, nicht als Ersatz.

**Welche Daten brauche ich, um Schnittpunkte zu modellieren?**
Mindestens protokollierte ABV-, Temperatur- und Zeitwerte über den Feinbrand hinweg, wobei jeder Sud damit beschriftet ist, wo der Brennmeister tatsächlich geschnitten hat. Inline-Spektroskopie oder Kongener-Sensoren helfen, sind aber zum Start nicht zwingend.

**Funktioniert das für Kolonnenbrennblasen ebenso wie für Pot Stills?**
Die Idee überträgt sich, aber das Problem unterscheidet sich. Pot-Still-Schnitte sind Chargenentscheidungen bei fallendem ABV; Kolonnenbrennblasen laufen kontinuierlich, sodass das Modell stationäre Abzugspunkte anstrebt statt diskreter Vorlauf-, Mittellauf- und Nachlaufschnitte.
