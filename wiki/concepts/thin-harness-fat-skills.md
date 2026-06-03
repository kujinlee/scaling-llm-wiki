---
concept: Thin Harness, Fat Skills
category: Skills, Plugins & Automation
summary: Keeping the agent's core interaction loop thin and generic while embedding task-specific behavior in thick natural-language skill files (markdown), backed by rigorous automated test coverage.
aliases: [thin harness fat skills, fat skills, thin harness, generic harness natural-language skills, skills as runbooks, Skillify, markdown as code]
related: [harness-engineering, claude-md, context-engineering, deterministic-workflow-orchestration, explicit-gears, meta-skills, lazy-context-loading, custom-eval-systems, self-modifying-agent-harness]
sources: [tokenmaxxing-how-top-builders-use-ai-to-do-the-work-of-400-e, stanford-cs153-frontier-systems-the-ai-native-company-how-on, aie-europe-keynotes-coding-agents-ft-pi-google-deepmind-anth]
---

# Thin Harness, Fat Skills

Thin harness, fat skills is a design principle for agentic systems: keep the harness — the LLM's core interaction loop — thin and generic, and put the bulk of behavior into "fat" skills written in natural language (markdown). Because LLMs excel at interpreting context, intent, and the general case, instructions are best expressed in prose rather than hard-coded; brittle, deterministic code is reserved only for the specific tool calls where exactness genuinely matters.

## Key Mechanics

- Two layers: a thin, generic harness loop plus thick natural-language skill files that carry the task-specific intelligence.
- Markdown over code for instructions — natural language is the right medium for specifying intent and generic cases because the model understands it directly and it stays flexible as needs change.
- Deterministic code is minimized to where it earns its brittleness (concrete tool calls), instead of encoding judgment that the model can interpret from prose.
- Pairs with rigorous 80–90% automated test coverage, so a flexible, prose-driven system is still pinned down by machine-checkable verification.

## How It Appears in the Corpus

The Garry Tan / Y Combinator "Tokenmaxxing" talk names "thin harness, fat skills" as a core philosophy behind G-Stack: keep the harness generic, push behavior into fat natural-language skills, and back the whole thing with heavy automated testing for robustness.

The Garry Tan / Diana Hu Stanford CS153 lecture sharpens what a "fat skill" is: a **skill is an executable runbook** (markdown that can call underlying code) distilled from human expertise, and it is built through "Skillify" — a ten-step process that writes unit tests for the code, LLM evals for the skill file, integration tests, sets `[[lazy-context-loading|resolver]]` triggers, and runs a "check resolvable" compliance/audit step. The lecture maps these primitives onto a company: a skill is an employee's capability, a `[[lazy-context-loading|resolver]]` is the org chart, the brain is internal process, "check resolvable" is audit/compliance, and trigger evals are performance reviews — a concrete instance of the prose-skill-plus-rigorous-testing philosophy, with the testing made explicit via `[[custom-eval-systems]]`.

The AIE Europe keynotes (AI Engineer channel) supply a striking production instance: Cursor reimplemented its "worktrees" feature entirely in simple markdown skills and sub-agents, cutting roughly 15,000 lines of maintenance code. This "markdown as code" approach is credited with greater flexibility, multi-repo support, and improved multi-model comparisons — a real product collapsing a large hard-coded feature into editable prose skills, the same conference where "Pi" pushes the idea further into a `[[self-modifying-agent-harness]]` the agent edits itself. It is direct evidence of behavior migrating out of compiled features and into the fat-skill layer.

## Tensions & Tradeoffs

- Tension with `[[harness-engineering]]` as framed in the Korean agent-transition talk, which emphasizes rigorously pre-defining scripts, rules, and reference files up front — a comparatively "fat harness" stance. Both agree the surrounding artifacts are decisive; they disagree on whether reliability should live in deterministic scaffold or in flexible prose skills.
- Flexibility vs. guarantees: prose skills adapt readily but are less enforceable than deterministic steps (`[[deterministic-workflow-orchestration]]`); the bet is that heavy test coverage compensates for the lost determinism.
- Capability-dependent: "fat skills in markdown" works only because a strong model reliably interprets intent — weaker models would need more deterministic scaffolding to stay reliable.
- Maintenance moves, it does not vanish: cutting 15,000 lines of feature code into markdown skills (Cursor) trades compiled-code maintenance for skill-file maintenance and the reliance on the model reading those skills correctly — cheaper to change, but the correctness burden shifts onto prose and its tests rather than disappearing.
- The Skillify lifecycle answers the "prose is unenforceable" worry head-on: a fat skill is pinned down by unit tests, LLM evals, and integration tests before it ships, so flexibility is bounded by machine-checkable `[[custom-eval-systems]]` rather than left to trust.
