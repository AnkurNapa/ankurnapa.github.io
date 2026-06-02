---
layout: post
lang: de
title: "CO2-Bilanzierung für Getränkehersteller: Scope 1, 2 und 3 mit Daten"
image: /assets/og/carbon-accounting-beverage-ai-data.png
description: "Der größte Teil des CO2 eines Getränkeherstellers ist Scope 3 — Verpackung und Transport. Wie Daten und KI eine glaubwürdige Scope-1/2/3-Bilanz aufbauen und wo generative KI die Offenlegung entwirft."
date: 2026-04-20 09:00:00 -0700
updated: 2026-04-20
permalink: /de/2026/carbon-accounting-beverage-ai-data/
tags: [esg, sustainability, carbon, esg-reporting]
faq:
  - q: "Wie können Daten und KI CO2-Emissionen senken?"
    a: "ML und Data Engineering bringen unordentliche Lieferanten- und Logistikdaten in Einklang, wenden Emissionsfaktoren konsistent an und schätzen Lücken, wo Primärdaten fehlen — und markieren, welche Annahmen die Gesamtsumme am stärksten bewegen."
  - q: "Wo passen Claude und ChatGPT in die Nachhaltigkeit?"
    a: "Ein Claude- oder ChatGPT-Copilot entwirft das Narrativ der CSRD-, SECR- oder freiwilligen Offenlegung und beantwortet ‚Was hat unser Scope 3 letztes Jahr getrieben?' — aber die Zahlen müssen sich auf Daten zurückführen lassen, und ein Mensch verantwortet die Offenlegung."
  - q: "Was ist die größte CO2-Quelle für eine Brauerei oder ein Weingut?"
    a: "Üblicherweise Scope 3 — Verpackung (besonders Glas) und Transport —, nicht die Energie, die zur Herstellung des Getränks verbraucht wird. Deshalb verfehlt eine CO2-Bilanzierung, die bei Scope 1 und 2 aufhört, den größten Teil des Fußabdrucks."
---

**Kurze Antwort: Das CO2 eines Getränkeherstellers teilt sich in Scope 1 (Brennstoff vor Ort), Scope 2 (zugekaufte Energie) und Scope 3 (Verpackung, Transport, Lieferkette) auf — und Scope 3 ist üblicherweise der größte und der schwierigste. Baue die Bilanz auf echten Messern und Lieferantendaten auf; nutze KI, um Lücken zu füllen, und generative KI, um die Offenlegung zu entwerfen, niemals die Zahlen.**

Du kannst nicht managen, was du nicht gezählt hast, und bei Getränken wird die Zählung von Glas, Dosen und Fracht dominiert, nicht vom Sudhaus. Eine glaubwürdige CO2-Bilanz ist das Fundament jeder anderen Nachhaltigkeitsaussage.

Verwandt: [CO2-Bilanzierung für Brauereien]({{ '/de/2025/carbon-accounting-breweries-scope/' | relative_url }}) · [Greenwashing mit KI vermeiden]({{ '/de/2026/avoiding-greenwashing-ai-verify/' | relative_url }}).

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 270" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Eine CO2-Bilanz aufbauen"><rect x="0" y="0" width="1000" height="270" fill="#fdfbf7"/><text x="500" y="34" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Eine CO2-Bilanz aufbauen</text><g font-family="sans-serif"><rect x="20" y="80" width="172" height="150" rx="8" fill="#eef2e3" stroke="#5b7a1f" stroke-width="1.5"/><circle cx="106" cy="114" r="15" fill="#5b7a1f"/><text x="106" y="119" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">1</text><text x="106" y="173" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1c1a17">Erfassen</text><text x="106" y="195" text-anchor="middle" font-size="11.5" fill="#6b6258">Energie, Material, Fracht</text><rect x="216" y="80" width="172" height="150" rx="8" fill="#eef2e3" stroke="#5b7a1f" stroke-width="1.5"/><circle cx="302" cy="114" r="15" fill="#5b7a1f"/><text x="302" y="119" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">2</text><text x="302" y="173" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1c1a17">Zuordnen</text><text x="302" y="195" text-anchor="middle" font-size="11.5" fill="#6b6258">zu Scope 1/2/3</text><rect x="412" y="80" width="172" height="150" rx="8" fill="#eef2e3" stroke="#5b7a1f" stroke-width="1.5"/><circle cx="498" cy="114" r="15" fill="#5b7a1f"/><text x="498" y="119" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">3</text><text x="498" y="173" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1c1a17">Faktorisieren</text><text x="498" y="195" text-anchor="middle" font-size="11.5" fill="#6b6258">Emissionsfaktoren</text><rect x="608" y="80" width="172" height="150" rx="8" fill="#eef2e3" stroke="#5b7a1f" stroke-width="1.5"/><circle cx="694" cy="114" r="15" fill="#5b7a1f"/><text x="694" y="119" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">4</text><text x="694" y="173" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1c1a17">Modellieren</text><text x="694" y="195" text-anchor="middle" font-size="11.5" fill="#6b6258">die Lücken füllen</text><rect x="804" y="80" width="172" height="150" rx="8" fill="#eef2e3" stroke="#5b7a1f" stroke-width="1.5"/><circle cx="890" cy="114" r="15" fill="#5b7a1f"/><text x="890" y="119" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">5</text><text x="890" y="173" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1c1a17">Berichten</text><text x="890" y="195" text-anchor="middle" font-size="11.5" fill="#6b6258">UK/EU/US/Indien</text></g><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="192" y1="155" x2="209" y2="155"/><polygon points="209,150 216,155 209,160" stroke="none"/><line x1="388" y1="155" x2="405" y2="155"/><polygon points="405,150 412,155 405,160" stroke="none"/><line x1="584" y1="155" x2="601" y2="155"/><polygon points="601,150 608,155 601,160" stroke="none"/><line x1="780" y1="155" x2="797" y2="155"/><polygon points="797,150 804,155 797,160" stroke="none"/></g></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Von verstreuten Daten zu einer Scope-1/2/3-Bilanz, die du verteidigen kannst.</figcaption>
</figure>

## Erst messen, dann modellieren

Ziehe Energiemesser (Scope 1/2) sowie Material- und Frachtaufzeichnungen (Scope 3) an einen Ort zusammen, mit Aktivitätsdaten je produzierter Einheit. Scope 3 ist der Ort, an dem sich das CO2 und die Messschwierigkeit beide konzentrieren.

## Wo KI und Daten CO2-Emissionen senken

ML und Data Engineering bringen unordentliche Lieferanten- und Logistikdaten in Einklang, wenden Emissionsfaktoren konsistent an und schätzen Lücken, wo Primärdaten fehlen — und markieren, welche Annahmen die Gesamtsumme am stärksten bewegen.

## Wo generative KI (Claude, ChatGPT) hilft

Ein Claude- oder ChatGPT-Copilot entwirft das Narrativ der CSRD-, SECR- oder freiwilligen Offenlegung und beantwortet ‚Was hat unser Scope 3 letztes Jahr getrieben?' — aber die Zahlen müssen sich auf Daten zurückführen lassen, und ein Mensch verantwortet die Offenlegung. Die Regel gilt: Sie entwirft und erklärt, ein Mensch verifiziert alles, was eine Aufsichtsbehörde erreicht.

## Die Regeln, Region für Region

Über die Regionen hinweg sind die Hebel dieselben, aber die Regeln unterscheiden sich: das **UK** (SECR-Energie-/Carbon-Berichterstattung, Verpackungs-EPR), die **EU** (CSRD, das EU ETS und die Verpackungs- und Verpackungsabfall-Verordnung), die **USA** (EPA-Wasser und Energy Star, Bundesstaatsprogramme wie das kalifornische und TTB für die Kennzeichnung) und **Indien** (das PAT-Programm des Bureau of Energy Efficiency und die CPCB-Abwassernormen). Miss zuerst an deinen eigenen Messern; bilde dann auf den jeweils anwendbaren Rahmen ab.

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="Wo die Emissionen sitzen — nach Scope"><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360" y="30" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Wo die Emissionen sitzen — nach Scope</text><rect x="280" y="70" width="120" height="40" fill="#5b7a1f"/><rect x="280" y="110" width="120" height="40" fill="#b45309"/><rect x="280" y="150" width="120" height="100" fill="#7a1f3d"/><rect x="440" y="84" width="14" height="14" fill="#5b7a1f"/><text x="462" y="96" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Scope 1 — direkter Brennstoff &amp; Prozess</text><rect x="440" y="124" width="14" height="14" fill="#b45309"/><text x="462" y="136" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Scope 2 — zugekaufte Energie</text><rect x="440" y="188" width="14" height="14" fill="#7a1f3d"/><text x="462" y="200" font-family="sans-serif" font-size="12.5" fill="#1c1a17">Scope 3 — Verpackung, Transport, Lieferkette (größter)</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">Der größte Teil des Fußabdrucks eines Getränkeherstellers ist Scope 3 (Verpackung, Transport, Lieferkette) — miss ihn, rate ihn nicht.</figcaption>
</figure>

## Wo es scheitert

Scope 3 beruht auf Schätzungen und Lieferantendaten unterschiedlicher Qualität, sodass die Zahl Unsicherheit trägt — sei transparent über die Methode und lass generative KI niemals eine Zahl oder eine Reduktion erfinden, die du nicht belegen kannst.

## Das Fazit

CO2-Bilanzierung ist Data Engineering, bevor sie Klimawissenschaft ist: erfassen, dem Scope zuordnen, faktorisieren und offenlegen. KI füllt Lücken und entwirft den Bericht; die Glaubwürdigkeit lebt in den gemessenen Daten.

## Häufig gestellte Fragen

**Wie können Daten und KI CO2-Emissionen senken?**
ML und Data Engineering bringen unordentliche Lieferanten- und Logistikdaten in Einklang, wenden Emissionsfaktoren konsistent an und schätzen Lücken, wo Primärdaten fehlen — und markieren, welche Annahmen die Gesamtsumme am stärksten bewegen.

**Wo passen Claude und ChatGPT in die Nachhaltigkeit?**
Ein Claude- oder ChatGPT-Copilot entwirft das Narrativ der CSRD-, SECR- oder freiwilligen Offenlegung und beantwortet ‚Was hat unser Scope 3 letztes Jahr getrieben?' — aber die Zahlen müssen sich auf Daten zurückführen lassen, und ein Mensch verantwortet die Offenlegung.

**Was ist die größte CO2-Quelle für eine Brauerei oder ein Weingut?**
Üblicherweise Scope 3 — Verpackung (besonders Glas) und Transport —, nicht die Energie, die zur Herstellung des Getränks verbraucht wird. Deshalb verfehlt eine CO2-Bilanzierung, die bei Scope 1 und 2 aufhört, den größten Teil des Fußabdrucks.

*Teil des Tracks [ESG-Analytik für Getränke]({{ '/de/tracks/esg/' | relative_url }}).*
