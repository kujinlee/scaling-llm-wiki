---
concept: Curated Design-System Skills
category: Workflows & Methodology
summary: Equipping an agent with curated brand-grade reference design systems plus multi-dimensional self-critique so generated interfaces inherit professional aesthetics instead of a generic AI look.
aliases: [design system skills, curated design references, brand-grade design generation, multi-dimensional design critique, design self-critique, avoiding generic AI aesthetics]
related: [github-as-blueprint, auto-research, visual-brainstorming, custom-eval-systems, interactive-artifacts, vibe-coding-vs-agentic-engineering, engineering-taste, verifiability-law, token-maxing]
sources: [6-claude-code-github-repos-that-change-everything]
---

# Curated Design-System Skills

Curated design-system skills is the technique of lifting an agent's design output from a generic "AI look" to professional, brand-grade quality by equipping it with two things: a library of curated, exemplary reference design systems to draw from, and a multi-dimensional self-critique pass that scores and revises its own output before shipping. It is the design-domain marriage of `[[github-as-blueprint]]` (learn from high-fidelity exemplars) and `[[auto-research]]` (iterate against explicit evaluation criteria), aimed at the specific failure mode that an agent left to its own defaults produces visually generic, homogeneous interfaces.

## Key Mechanics

- **Curated reference systems as imitable exemplars**: a pre-built set of brand-grade design systems (the corpus cites systems inspired by Stripe, Apple, and Airbnb) gives the agent professional references to draw from — the design analogue of `[[github-as-blueprint]]`, where pointing at high-quality examples is the highest-fidelity way to transmit intent.
- **Direction-first, then options**: the agent picks a design direction and builds "reels" of options before committing, surfacing alternatives — overlapping the option-exploration of `[[visual-brainstorming]]`.
- **Multi-dimensional self-critique**: a "five-dimensional" self-critiquing pass scores and revises the output against several aesthetic axes — criteria-based self-improvement applied to design, the visual instance of `[[auto-research]]` and `[[custom-eval-systems]]`.
- **Packaged and token-conscious**: the capability ships as installable design skills and agents (`[[plugin-packaging]]`), positioned as an open-source alternative to a first-party design feature, with managing token consumption a stated design goal.

## How It Appears in the Corpus

The Nuno Tavares "6 Claude Code GitHub Repos" overview presents "Open Design" as a tool for crafting modern, aesthetically pleasing websites and artifacts: 13 coding agents, 31 design skills, and 72 brand-grade design systems inspired by companies like Stripe, Apple, and Airbnb. It lets the agent pick design directions, build project reels, run five-dimensional self-critiquing, and ship design artifacts — billed as an open-source alternative to Claude Design that manages token consumption more efficiently.

## Tensions & Tradeoffs

- **Floor-raising that risks homogeneity**: curated exemplars reliably raise the baseline, but every agent drawing from the same fixed library of systems tends to converge on a recognizable house style — the design-domain version of the floor-raising effect of `[[vibe-coding-vs-agentic-engineering]]`, where accessible quality and distinctiveness pull in opposite directions.
- **Self-critique is only as good as its dimensions**: a fixed set of critique axes scores what it measures and ignores what it does not, so a confident "passed" verdict can still ship a flawed design — the "quality of the check bounds the trust" caveat of `[[custom-eval-systems]]`.
- **Aesthetic quality resists clean scoring**: design sits near the unverifiable end of `[[verifiability-law]]`, so multi-dimensional self-critique *approximates* taste but does not replace the human `[[engineering-taste]]` that makes the final aesthetic call.
- **Richer generation costs tokens**: building option reels and running a multi-axis critique consume more inference than a single-shot render — the `[[token-maxing]]`-versus-economy tradeoff, here spent on visual quality, and the same artifact-delivery surface as `[[interactive-artifacts]]`.
