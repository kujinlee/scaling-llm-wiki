---
concept: Meta Skills
category: Skills, Plugins & Automation
summary: Reusable prompts whose job is to design other agents, packaging the agent-architecture workflow so new agent creation is a templated, repeatable, and shareable activity.
aliases: [meta skill, agent-design skills, skill-authoring prompts]
related: [github-as-blueprint, harness-engineering, auto-research, compound-engineering]
sources: [나의-ai-에이전트-전환기-w-클로드-코드-오픈클로]
---

# Meta Skills

A meta skill is a reusable prompt (or skill) whose job is to *design other agents* — packaging the prompts used to architect, specify, and refine an agent so the design process itself can be invoked repeatedly. Instead of hand-crafting each new agent from scratch, the operator runs a meta skill to generate and improve the agent's blueprint.

## Key Mechanics

- The design workflow — the prompts that lay out an agent's overall blueprint and iteratively improve it — is captured as a standing, reusable skill.
- Meta skills are applied repeatedly across agents, making agent creation a templated, compounding activity (see `[[compound-engineering]]`).
- They are shareable artifacts: the corpus's meta skills are published via GitHub for others to reuse, complementing `[[github-as-blueprint]]`.

## How It Appears in the Corpus

In the Korean agent-transition talk, the speaker turns the prompts used to design agents into "meta skills," uses them to produce and refine each agent's full blueprint, and shares the skills on GitHub.

## Tensions & Tradeoffs

- Abstraction drift: a generic design skill may not fit a specific agent's needs, requiring case-by-case tuning.
- Maintenance: as with other reusable artifacts, meta skills must be kept current or they propagate stale design patterns across every agent built from them.
