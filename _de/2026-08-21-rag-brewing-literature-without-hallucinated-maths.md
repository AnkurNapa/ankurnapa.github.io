---
layout: post
lang: de
title: "RAG über die Brauliteratur ohne halluzinierte Mathematik"
image: /assets/og/rag-brewing-literature-without-hallucinated-maths.png
description: "Teil 1 von The Brewer's Agent. Retrieval-Augmented Generation ist gut darin, zu finden, was in der Brauliteratur steht, und schlecht darin, es auszurechnen. Wie man Formeln und Tabellen chunkt, warum das Brauen hybride Suche braucht, warum jede Antwort eine Quellenangabe braucht und warum die Arithmetik an ein Werkzeug geht."
date: 2026-08-21 09:00:00 -0700
updated: 2026-08-21
permalink: /de/2026/rag-brewing-literature-without-hallucinated-maths/
tags: [brewing-science, brewers-agent, generative-ai, rag, data-engineering]
faq:
  - q: "Was ist RAG und warum nutzt man es für Brauwissen?"
    a: "Retrieval-Augmented Generation bedeutet, dass das Modell vor der Antwort Passagen aus deinen eigenen Dokumenten nachschlägt und aus diesen Passagen antwortet. Beim Brauen bleiben die Antworten so an den Lehrbüchern, Fachartikeln und Labormethoden, denen du vertraust, statt an dem, was das Modell halb aus dem Internet erinnert, und jede Antwort kann ihre Quelle angeben."
  - q: "Kann ein RAG-System ABV oder IBU korrekt berechnen?"
    a: "Es kann die richtige Formel finden, sollte die Rechnung aber nicht selbst ausführen. Sprachmodelle sind bei mehrstufiger Arithmetik unzuverlässig, und Brauformeln haben Einheiten- und Temperaturkonventionen, die leicht verwechselt werden. Hole die Formel für die Erklärung und schicke die Zahlen an ein getestetes Rechenwerkzeug."
  - q: "Wie sollte man Braudokumente für das Retrieval in Chunks zerlegen?"
    a: "Halte Formeln, ihre Variablendefinitionen und ihre Einheiten in einem Chunk zusammen, und lass Tabellen samt Kopfzeilen und Fußnoten vollständig. Speichere Metadaten wie Temperaturbasis und Einheiten mit jedem Chunk. Wer nach einer festen Zeichenzahl trennt, reißt regelmäßig eine Formel von der Zeile los, die erklärt, was ihre Symbole bedeuten."
---

**Kurze Antwort: RAG ist sehr gut darin, zu finden, was in der Brauliteratur steht, und ziemlich schlecht darin, es auszurechnen. Richte es auf deine Lehrbücher, Fachartikel und Labormethoden, zerlege sie so in Chunks, dass eine Formel nie von ihren Einheiten getrennt wird, nutze hybride Suche, weil das Brauen voller Abkürzungen ist, die Embeddings verwischen, und sorge dafür, dass jede Antwort die Passage zitiert, aus der sie stammt. Dann nimm dem Modell die Arithmetik komplett ab. Es holt die Formel für die Erklärung. Ein getestetes Werkzeug berechnet die Zahl.**

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 320" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Eine Brauerfrage geht in eine Pipeline. Hybrides Retrieval kombiniert Stichwortsuche und Vektorsuche über zerlegte Lehrbücher, Fachartikel und Labormethoden, dann wählt ein Reranker die besten Passagen. Das Sprachmodell schreibt die Erklärung mit Quellenangaben. Alle Zahlen in der Frage gehen über einen eigenen Zweig an ein Rechenwerkzeug, das den berechneten Wert mit Methode und Einheiten zurückgibt. Ein Banner sagt: Wissen abrufen, Zahlen berechnen.">
<rect width="1000" height="320" fill="#ffffff"/>
<text x="500" y="28" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00695c">ZWEI WEGE FÜR EINE FRAGE: WORTE AUS DEM RETRIEVAL, ZAHLEN AUS WERKZEUGEN</text>
<g font-family="sans-serif">
<rect x="30" y="110" width="160" height="70" rx="9" fill="#06483f"/>
<text x="110" y="140" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">Frage des Brauers</text>
<text x="110" y="160" text-anchor="middle" font-size="10.5" fill="#cfe6df">"ABV bei 13 &#176;P, 64,9% RDF?"</text>
<line x1="190" y1="130" x2="240" y2="85" stroke="#4db6a2" stroke-width="2"/>
<line x1="190" y1="160" x2="240" y2="215" stroke="#4db6a2" stroke-width="2"/>
<rect x="240" y="55" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="340" y="81" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">hybrides Retrieval</text>
<text x="340" y="99" text-anchor="middle" font-size="10.5" fill="#4a6b64">Stichwort + Vektor, dann Rerank</text>
<line x1="440" y1="86" x2="480" y2="86" stroke="#4db6a2" stroke-width="2"/>
<rect x="480" y="55" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="580" y="81" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">LLM erklärt</text>
<text x="580" y="99" text-anchor="middle" font-size="10.5" fill="#4a6b64">aus Passagen, mit Quellen</text>
<rect x="240" y="185" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="340" y="211" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">Rechenwerkzeug</text>
<text x="340" y="229" text-anchor="middle" font-size="10.5" fill="#4a6b64">getesteter Code, Basiseinheiten</text>
<line x1="440" y1="216" x2="480" y2="216" stroke="#4db6a2" stroke-width="2"/>
<rect x="480" y="185" width="200" height="62" rx="9" fill="#f0f6f5" stroke="#00695c" stroke-width="1.5"/>
<text x="580" y="211" text-anchor="middle" font-size="11.5" font-weight="700" fill="#06483f">5,46% ABV</text>
<text x="580" y="229" text-anchor="middle" font-size="10.5" fill="#4a6b64">Methode und Einheiten mitgeliefert</text>
<line x1="680" y1="86" x2="740" y2="140" stroke="#4db6a2" stroke-width="2"/>
<line x1="680" y1="216" x2="740" y2="165" stroke="#4db6a2" stroke-width="2"/>
<rect x="740" y="115" width="230" height="66" rx="9" fill="#ffffff" stroke="#2e9e7c" stroke-width="2"/>
<text x="855" y="142" text-anchor="middle" font-size="12" font-weight="700" fill="#2e9e7c">Antwort</text>
<text x="855" y="162" text-anchor="middle" font-size="10.5" fill="#4a6b64">erklärt, belegt, berechnet</text>
<rect x="30" y="270" width="940" height="38" rx="10" fill="#06483f"/>
<text x="500" y="294" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff">WISSEN ABRUFEN &#183; ZAHLEN BERECHNEN &#183; NIE UMGEKEHRT</text>
</g>
</svg>
<figcaption style="font-size:.85rem;color:#4a6b64;margin-top:.4rem">Modell und Rechner bekommen jeweils die Aufgabe, die sie gut können. Der Brauer bekommt eine Antwort mit Quelle und Methode.</figcaption>
</figure>

Frag einen allgemeinen Chatbot, wie man den Alkoholgehalt eines Biers aus Stammwürze und wirklichem Vergärungsgrad berechnet. Du bekommst einen selbstsicheren Absatz und eine Formel. Manchmal ist es die richtige Formel. Manchmal ist es die Hobbybrauer-Abkürzung, die mit spezifischer Dichte arbeitet, garniert mit Plato-Werten, für die sie nie gedacht war. So oder so wurde die Zahl am Ende im Kopf des Modells ausgerechnet, und genau dort beginnt das Problem.

Dies ist der erste Beitrag in **The Brewer's Agent**, einer Serie über GenAI-Werkzeuge für das Brauen, denen ein Brauer tatsächlich vertrauen kann. Sie knüpft dort an, wo [The Cellar Ledger]({{ '/series/cellar-ledger/' | relative_url }}) im Weingut aufgehört hat: Das Modell ist nur so gut wie die Daten und Werkzeuge darunter.

## Was RAG tatsächlich macht

Retrieval-Augmented Generation ist eine einfache Idee. Bevor das Modell antwortet, holt ein Suchschritt die relevantesten Passagen aus einer Sammlung, die du kontrollierst. Das Modell antwortet dann aus diesen Passagen statt aus dem Gedächtnis.

Für eine Brauerei könnte diese Sammlung Folgendes umfassen:

- einige Lehrbücher und die Kapitel, die tatsächlich genutzt werden
- veröffentlichte Fachartikel zu Hopfenchemie, Maischen und Gärung
- deine eigenen Labormethoden und SOPs
- Lieferantenspezifikationen und Analysenzertifikate

Der Gewinn ist nicht, dass das Modell klüger wird. Er besteht darin, dass die Antwort aus einem Dokument stammt, das du ausgewählt hast, und dass die Antwort dir sagen kann, aus welchem. Ein Brauer kann die Seite aufschlagen und nachprüfen. Diese Gewohnheit, die Quelle zu prüfen, ist das gesamte Sicherheitssystem.

## Chunking: wo Braudokumente zerbrechen

Dokumente werden vor der Indexierung in Chunks zerlegt, und die meisten RAG-Fehler in technischen Fachgebieten beginnen genau hier.

Der Standardansatz trennt den Text etwa alle tausend Zeichen. Die Brauliteratur ist voller Formeln, auf die eine Zeile folgt, die Symbole, Einheiten und Temperaturbasis erklärt. Trennt man an der falschen Stelle, enthält ein Chunk die Formel und der nächste "wobei OG in Grad Plato bei 20/20 Grad C angegeben ist". Das Modell ruft den ersten ab und rät den zweiten.

Regeln, die das meiste davon beheben:

1. **Halte eine Formel mit ihren Definitionen zusammen.** Trenne an Abschnittsgrenzen, nicht nach Zeichenzahl, und behandle eine Gleichung samt dem folgenden Absatz als eine Einheit.
2. **Lass Tabellen vollständig.** Eine Tabelle zur Hopfenausbeute ohne Kopfzeile ist eine Liste von Zahlen. Speichere die ganze Tabelle mit Kopfzeilen, Fußnoten und allem als einen Chunk, auch wenn er lang wird.
3. **Leg die Konventionen in die Metadaten.** Speichere Einheiten, Temperaturbasis und Ausgabe der Quelle zu jedem Chunk. Plato bei 20/20 Grad C und spezifische Dichte bei 60/60 Grad F sind nicht austauschbar, und das Modell muss sehen, womit es gerade arbeitet.
4. **Parent Retrieval für lange Herleitungen.** Indexiere kleine Chunks für präzise Treffer, gib dem Modell aber den ganzen Abschnitt, aus dem sie stammen.

## Hybride Suche, weil das Brauen in Akronymen spricht

Vektorsuche findet Passagen mit ähnlicher Bedeutung. Das ist großartig, wenn "warum schmeckt mein Lager nach gekochtem Mais" bei DMS landet. Weniger gut ist sie bei Begriffen, in denen ein einzelner Buchstabe zählt.

RDF und ADF sind zwei verschiedene Maße für den Vergärungsgrad, und beim selben Bier können sie mehr als zehn Punkte auseinanderliegen. Für ein Embedding-Modell sehen sie fast gleich aus: kurz, großgeschrieben, irgendwas mit Gärung. Eine Stichwortsuche (BM25 oder Ähnliches) behandelt sie als die unterschiedlichen Wörter, die sie sind.

Also beides laufen lassen, die Ergebnisse zusammenführen und dann einen Reranker die relevantesten Passagen nach oben stellen lassen. Die meisten Vektordatenbanken und Suchdienste unterstützen das inzwischen direkt. Es ist die günstigste Einzelverbesserung, die du an einem technischen RAG-System vornehmen kannst.

## Retrieval für Wissen, Werkzeuge für Arithmetik

Hier ist die Regel, auf der diese ganze Serie ruht. **Das Modell darf eine Formel erklären. Es darf sie nicht auswerten.**

Nimm die Frage aus der Abbildung. Eine Würze mit 13,0 Grad Plato wird auf einen wirklichen Vergärungsgrad von 64,9% vergoren. Wie hoch ist der ABV?

Richtig gerechnet geht das über Ballings Beziehung zwischen verbrauchtem Extrakt und gebildetem Alkohol, ergibt einen wirklichen Extrakt von etwa 4,77% und einen Alkohol von etwa 4,27% nach Gewicht und rechnet dann Gewicht in Volumen um, mit der eigenen Dichte des Biers. Die Antwort lautet 5,46% ABV. Jeder Schritt hat eine Konstante mit vier Nachkommastellen und eine Einheitenkonvention.

Ein Sprachmodell, das das im Kopf rechnen soll, kommt oft nah heran. Nah ist das Problem. Gelegentlich lässt es einen Schritt aus, nimmt die falsche Dichte oder vertauscht Gewicht und Volumen, und es präsentiert 4,3% mit genau derselben Sicherheit wie 5,46%. Nichts im Text verrät dir, welche Antwort du bekommen hast.

Die Lösung ist architektonisch, kein besserer Prompt. Der Retrieval-Schritt liefert die Erklärung: was RDF ist, warum sich Gewicht und Volumen unterscheiden, woher die Konstanten kommen. Ein Rechenwerkzeug, gewöhnlicher getesteter Code, liefert die Zahl. Der [nächste Beitrag]({{ '/de/2026/brewing-agent-calculation-tools-not-sums/' | relative_url }}) baut diese Werkzeuge. Für diesen hier gilt: Das RAG-System sollte die Arithmetik auslagern und das in der Antwort auch sagen: "berechnet vom ABV-Werkzeug aus OG und RDF".

## Quellenangaben sind das Feature

Jede Antwort sollte ihre Quellen mitführen: das Dokument, den Abschnitt und idealerweise die Seite. Mach das zur harten Anforderung im System-Prompt und prüfe es beim Testen. Eine Antwort ohne Quellenangabe sollte als gescheiterte Antwort gelten, so gut sie auch klingt.

Zwei Kleinigkeiten machen Quellenangaben deutlich nützlicher:

- **Zeig die Passage, nicht nur den Titel.** Ein Brauer, der einen Blick auf den zitierten Absatz wirft, erkennt eine falsche Ausgabe oder eine Hobbybrauer-Quelle schneller als jede automatische Prüfung.
- **Sag es, wenn nichts gefunden wurde.** Liefert das Retrieval nichts Relevantes, lautet die richtige Antwort "Dafür habe ich keine Quelle", nicht eine flüssige Vermutung aus Allgemeinwissen. Teste dieses Verhalten gezielt, denn Modelle sind darauf trainiert, hilfsbereit zu sein, und füllen die Lücke, wenn man sie lässt.

## Wo das an Grenzen stößt

**Dein Korpus hat Meinungen.** Lehrbücher widersprechen sich bei der Hopfenausbeute, Hobbybrauer-Quellen nutzen Abkürzungen, die kommerzielle Labore nicht nutzen würden, und ältere Ausgaben enthalten überholte Methoden. RAG ruft getreu die Passage ab, die am besten passt. Kuratiere die Sammlung, kennzeichne die Art der Quelle und bevorzuge deine eigenen Labormethoden, wo es sie gibt.

**Gescannte PDFs verlieren die Mathematik.** OCR macht aus tiefgestellten Zeichen, griechischen Buchstaben und Brüchen Rauschen. Eine Formel, die im Buch "E = P/100" lautet, kann als "E - Pl100" herauskommen. Prüfe den extrahierten Text deiner meistgenutzten Formeln mit eigenen Augen, bevor du dem Index vertraust.

**Das Urheberrecht gilt weiterhin.** Ein Lehrbuch für den internen Gebrauch zu indexieren ist eine Sache. Das Modell lange Passagen an Personen außerhalb des Unternehmens zitieren zu lassen, ist eine andere. Wisse, welche Lizenz die Dokumente abdeckt, die du indexierst.

**Auch Quellenangaben können erfunden sein.** Ein Modell kann eine Referenz erzeugen, die richtig aussieht und nie abgerufen wurde. Baue die Quellenangabe im Code aus den Retrieval-Metadaten, nicht aus dem Text des Modells.

## Das Fazit

RAG macht aus einem Stapel Brauliteratur etwas, dem man Fragen stellen kann, und die Antworten verweisen zurück auf die Seite. Das ist wirklich nützlich. Was es nicht tut: das Modell gut in Arithmetik machen, und Brauen ist größtenteils Arithmetik mit Konventionen. Zerlege so, dass Formeln ihre Einheiten behalten, suche nach Stichworten wie nach Bedeutung, bestehe auf Quellenangaben und schicke jede Zahl an ein Werkzeug. Das Modell liest das Buch. Der Rechner macht die Rechnung.

Für das größere Bild dessen, was KI heute in Brauereien tut, siehe [What AI in Beer Actually Looks Like in 2026]({{ '/2026/what-ai-in-beer-actually-looks-like-2026/' | relative_url }}). Die vollständige Liste steht auf der [Serienseite von The Brewer's Agent]({{ '/series/brewers-agent/' | relative_url }}).

## Häufig gestellte Fragen

**Was ist RAG und warum nutzt man es für Brauwissen?**
Retrieval-Augmented Generation bedeutet, dass das Modell vor der Antwort Passagen aus deinen eigenen Dokumenten nachschlägt und aus diesen Passagen antwortet. Beim Brauen bleiben die Antworten so an den Lehrbüchern, Fachartikeln und Labormethoden, denen du vertraust, statt an dem, was das Modell halb aus dem Internet erinnert, und jede Antwort kann ihre Quelle angeben.

**Kann ein RAG-System ABV oder IBU korrekt berechnen?**
Es kann die richtige Formel finden, sollte die Rechnung aber nicht selbst ausführen. Sprachmodelle sind bei mehrstufiger Arithmetik unzuverlässig, und Brauformeln haben Einheiten- und Temperaturkonventionen, die leicht verwechselt werden. Hole die Formel für die Erklärung und schicke die Zahlen an ein getestetes Rechenwerkzeug.

**Wie sollte man Braudokumente für das Retrieval in Chunks zerlegen?**
Halte Formeln, ihre Variablendefinitionen und ihre Einheiten in einem Chunk zusammen, und lass Tabellen samt Kopfzeilen und Fußnoten vollständig. Speichere Metadaten wie Temperaturbasis und Einheiten mit jedem Chunk. Wer nach einer festen Zeichenzahl trennt, reißt regelmäßig eine Formel von der Zeile los, die erklärt, was ihre Symbole bedeuten.
