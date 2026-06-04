---
concept: Visual Brainstorming Companion
category: Workflows & Methodology
summary: Agent spins up a local browser surface, renders interactive mockups of design options, reads clicks and text feedback, and iterates — closing a visual feedback loop before any production code exists.
aliases: [visual brainstorming, visual companion, interactive mockup feedback, browser-based brainstorming]
related: ["[[spec-driven-development]]", "[[computer-use-automation]]", "[[engineering-taste]]", "[[spec-review-loop]]"]
sources: [the-claude-code-plugin-every-developer-must-learn-superpower]
---

# Visual Brainstorming Companion

The visual brainstorming companion is a technique for design alignment in which an agent spins up a local browser-based surface, renders interactive mockups of design options, and reads the user's clicks and text feedback to iterate — closing a visual feedback loop before any production code is written. It extends brainstorming from text into the visual domain for tasks where seeing and choosing among options conveys intent better than describing it in prose.

## Key Mechanics

- On visual decisions (UI layouts, component designs, diagrams, navigation), the agent offers to start a local server and writes HTML content fragments that the server wraps in styled, interactive frames.
- The user clicks among presented layout and design alternatives; these interactions are recorded, so the agent reads both text feedback and browser clicks and then serves updated mockups in real time.
- Reusable building blocks (built-in CSS classes for options, cards, mockups, split views, pro/con comparisons, and wireframe elements) standardize how alternatives are presented.
- It is invoked contextually rather than as a separate mode, and mockups persist on disk (e.g. a `.superpowers/brainstorm` folder) as a durable design record.

## How It Appears in the Corpus

The GritAI Studio Superpowers walkthrough highlights the browser-based visual companion as a standout feature: during brainstorming on visual topics, Claude generates clickable mockups so users get early alignment and feedback for UI work, content strategy, and information architecture before any production code exists.

## Tensions & Tradeoffs

- Scope: it only pays off for visually-decidable work; for purely logical tasks it adds overhead.
- It is a structured channel for human `[[engineering-taste]]` to enter early — surfacing design judgment as clickable choices — but alignment quality still depends on the human recognizing the right option among those the agent generated.
- Overlaps with `[[computer-use-automation]]` in driving a browser, but here the browser is a purpose-built feedback surface the agent authors, not a third-party app it operates through the GUI.
