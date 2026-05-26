---
layout: post
title: "How to Vibe-Code a Product with Claude (It's a Loop, Not Magic)"
description: "Vibe-coding with Claude isn't AI writing your app while you watch. It's a build–verify–fix loop — and the verifier is what separates a shippable product from a confident demo."
date: 2026-05-26
updated: 2026-05-26
tags: [vibe-coding, claude, ai-tools, building-with-ai]
faq:
  - q: "What is vibe coding?"
    a: "Vibe coding is describing what you want in plain language and letting an AI agent do the actual typing — editing files, running commands, reading errors. With a tool like Claude Code you supervise a loop rather than write every line yourself."
  - q: "Can Claude build a whole product on its own?"
    a: "It can do a lot of the building, but not unsupervised. The reliable pattern is a loop: you describe intent, Claude builds, something verifies the result, Claude reads the failure and fixes it. Without a verifier you get a demo that breaks on contact with real use."
  - q: "What's the most important part of vibe-coding with Claude?"
    a: "The check. Setting up something that automatically verifies the work — a test, a validator, a script that confirms the output is correct — is what turns 'looks done' into 'is done.' The prompt matters far less than the verifier."
---

**Short answer: vibe-coding with Claude isn't AI writing your app while you watch — it's a loop. You describe what you want, Claude builds it, something checks the result, Claude reads the failure and fixes it, and it repeats until the thing actually works. The skill isn't the prompt. It's setting up the check. Get the verifier right and you can ship real software; skip it and you've got a confident demo that falls over the moment a real user touches it.** Here's how it actually goes.

## "Vibe coding" is doing too much work as a phrase

The word conjures a fantasy: you type a wish, a finished app appears, you sip your coffee. That's not what happens, and pretending it does is how people ship broken things.

The honest version: vibe coding is describing intent in plain language and letting an AI agent — I use Claude Code, which runs in the terminal — do the typing. It reads your files, writes code, runs commands, and reads the errors that come back. You're not writing every line. You're steering, and you're checking. That second part is the whole job.

## The loop is the product

Strip away the marketing and every useful session looks like the same four steps:

1. **Describe** — tell Claude the outcome you want, in plain language.
2. **Build** — it edits the files and runs the commands.
3. **Verify** — something checks the result: a test, a validator, a script, the real app.
4. **Fix** — Claude reads the failure and goes again.

Here's a real one from this week. I asked Claude to add a batch of calculated measures to a sales-pipeline dashboard — an actual Tableau workbook with a real data model, not a toy. It opened the file, read the data model, and found 92 numeric fields. It threw out the 58 that are nonsense to aggregate (latitude, longitude, fiscal-year integers, login counters) and built **173 calculated measures** — sums, averages, ratios, running totals, year-over-year — on the 34 that actually matter.

Then it tried to save the file, and **Tableau rejected it.** The first attempt put the new fields in the wrong place in the file's structure, and Tableau threw a schema error refusing to load it.

That rejection is the most important moment in the story. Because there was a verifier — Tableau itself, plus a script checking that every formula pointed at a real field — Claude *saw* it had failed. It read the exact error, moved the fields to the correct position, and re-checked until the structure was valid. Without that check, I'd have happily shipped a file that simply wouldn't open.

## Same loop, very different jobs

The loop doesn't care what you're building. In one stretch this week it ran across four jobs that have nothing in common:

- A **Tableau dashboard tool** (the 173 measures above).
- A **build plan for an ERP feature** — a full walkthrough of standing up an internal app, where the entire method was the same loop: write the change, deploy it, let a browser test drive the real screens, read the failures, fix.
- A **34-page PDF turned into clean Markdown**, tables and checklists and all.
- A **knowledge base re-wired** so a new document was correctly linked into everything related to it.

Different tools, different file types, identical rhythm: describe, build, verify, fix.

## The verifier is the whole game

This is the part the hype skips. An AI agent that writes code without a way to check that code is a very fast way to generate plausible mistakes. The agent will tell you it's done. It believes it. It's often wrong.

What makes the loop trustworthy is the thing on the other side of "build":

- For the dashboard, it was Tableau's own validator plus a script confirming every formula referenced a real column.
- For an app, it's tests — or a tool like Playwright driving the actual user interface and reporting what broke.
- For the PDF, it was me reading the output against the original.

This is the same discipline I keep coming back to in [why you must check every number AI touches]({{ '/2026/can-ai-write-your-ttb-reports/' | relative_url }}). A confident wrong answer is the default failure mode of these models. The verifier is what catches it before your users do. Build the check first, and the rest of the loop becomes safe to run fast.

## If you're the one building it

If you're going to do this hands-on, the setup is small and it's mostly about making the loop run without you babysitting it:

- **Run Claude Code in your project.** Point it at the repo. It works on the real files, not a chat window.
- **Write down how to build and verify** in a `CLAUDE.md` at the project root — the exact commands to compile, deploy, and test. This is the single highest-leverage thing you can do. Now "build and check it" is something Claude can run on its own.
- **Allowlist the safe commands** (your test runner, your build tool) so the loop doesn't stop to ask permission on every cycle.
- **Prompt intent *plus* the check.** Not "add the feature" but "add the feature, then confirm it by running the tests and fixing anything red." The second clause is what closes the loop. My Tableau prompt was essentially: *add these measures, then verify the file is valid and every formula resolves.* The verification clause is why the schema error got caught and fixed instead of shipped.

That's it. The agent is capable; the structure is what makes it reliable.

## Where the vibes lie

Be clear-eyed about the failure modes, because they're real:

- **It fails on the first try, routinely.** The Tableau file was rejected before it worked. That's completely fine *if* you have a verifier — and a serious problem if you don't, because you won't know.
- **It can't see everything.** That PDF had two pages that were pure diagrams, with no extractable text. Claude flagged them and left a template instead of inventing content — which is exactly the right behavior, and exactly the kind of gap you have to check for.
- **It produces confident, wrong output.** Hallucinated numbers, misquoted rules, fields that don't exist. This is the [honest limit of these tools]({{ '/2026/the-honest-limits-of-ai-in-brewing/' | relative_url }}), and no amount of good prompting removes it. It only gets caught downstream.
- **It makes judgment calls you should audit.** It decided which 58 fields to drop. Good calls, this time — but I checked them. You should too.

None of this is a reason not to use it. It's a reason to never ship the output unverified.

## The bottom line

Vibe-coding a product with Claude works, and it's genuinely fast — but the speed comes from the loop, not from trusting the first answer. The move is simple:

1. **Pick something with a clear check** — a test, a validator, a screen you can drive.
2. **Write the build-and-verify commands down** so the agent can run them itself.
3. **Prompt the intent and the check together.**
4. **Let the loop run, and review the green result** — not every keystroke.
5. **Verify the substance yourself before it ships.**

Vibe-code the typing. Never vibe-code the verification. That line is the difference between a weekend demo and something you'd actually put in front of a customer.

## Frequently asked questions

**What is vibe coding?**
Vibe coding is describing what you want in plain language and letting an AI agent do the actual typing — editing files, running commands, reading errors. With a tool like Claude Code you supervise a loop rather than write every line yourself.

**Can Claude build a whole product on its own?**
It can do a lot of the building, but not unsupervised. The reliable pattern is a loop: you describe intent, Claude builds, something verifies the result, Claude reads the failure and fixes it. Without a verifier you get a demo that breaks on contact with real use.

**What's the most important part of vibe-coding with Claude?**
The check. Setting up something that automatically verifies the work — a test, a validator, a script that confirms the output is correct — is what turns "looks done" into "is done." The prompt matters far less than the verifier.
