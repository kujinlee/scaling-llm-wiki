---
concept: Explicit Gears
category: Workflows & Methodology
summary: Switching an agent deliberately between distinct cognitive modes (CEO review, architecture, paranoid code review, QA, ship) rather than leaving it in an undifferentiated generalist state.
aliases: [explicit gears, AI gears, cognitive mode switching, specialized AI modes, explicit roles]
related: ["[[harness-engineering]]", "[[meta-skills]]", "[[multi-agent-code-review]]", "[[agentic-issue-resolution]]", "[[engineering-taste]]", "[[parallel-isolated-agents]]", "[[aspirational-prompting]]"]
sources: [yc-ceo-shipped-100-prs-week-for-50-days-his-8-claude-code-sk, tokenmaxxing-how-top-builders-use-ai-to-do-the-work-of-400-e]
---

# Explicit Gears

Explicit gears is the principle that an AI coding assistant should be switched deliberately between distinct, specialized cognitive modes — one per kind of work — rather than left in a single generic "machine mode" that blurs planning, coding, reviewing, and testing together. Each gear activates a different "brain": a different role, set of priorities, and standard of judgment. The move turns a generalist model into an on-demand team of specialists, and is offered as the lever behind dramatic, sustained productivity gains.

## Key Mechanics

- Diagnosis of the failure mode: a single undifferentiated mode mixes incompatible mindsets — product vision, engineering rigor, adversarial review, fast execution — so none is done well. Naming and separating them is the fix.
- Each gear is packaged as a discrete, invokable skill with an explicit role and prompt, so the operator chooses *which kind of intelligence* to apply at each step. This makes the gears concrete `[[harness-engineering]]` artifacts and a form of `[[meta-skills]]` (skills that shape how the agent thinks).
- Observed gears span the development lifecycle: a founder/CEO-review mode (product taste, user empathy, challenging whether the right problem is being solved — an applied form of `[[engineering-taste]]`), an engineering-rigor mode (architecture, failure modes, system design), a paranoid code-review mode hunting real bugs, security flaws, and race conditions rather than style (see `[[multi-agent-code-review]]`), a QA/test-engineer mode, an automated release/ship mode (sync, test, push, open PR — overlapping `[[agentic-issue-resolution]]`), and a retrospective manager mode.
- The gears are sequenced into a workflow: plan → product validation → architecture → implement → bug-catching review → ship → end-to-end QA, applying the right mindset at each stage.

## How It Appears in the Corpus

The Garry Tan / gstack ("Gist") talk presents explicit gears as the core insight behind shipping ~100 PRs per week for 50 days: an open-sourced toolkit of eight specialized Claude Code skills, each a distinct mode, replacing the "mushy" single-mode default. The stated underlying principle generalizes beyond the toolkit — define clear roles and contexts for the model to maximize results.

The same G-Stack toolkit reappears in the Garry Tan / Y Combinator "Tokenmaxxing" talk, where the gears surface as named review modes — CEO, design, dev, and eng — queued through a Conductor instance, alongside a "CEO plan" meta-prompt (`[[aspirational-prompting]]`) that raises the agent's ambition. This confirms the gears pattern across talks and ties it to the toolkit's parallel-agent orchestration.

## Tensions & Tradeoffs

- Overhead vs. quality: maintaining and correctly switching between many modes is more effort than one-shot prompting, and the operator must know which gear a task needs — a judgment the framework presupposes (related to `[[engineering-taste]]`).
- Boundary with `[[multi-agent-code-review]]`: there, separate agents divide a single review; here, separate *modes* of (potentially) one agent divide the whole lifecycle. The two compose — gears can themselves run as parallel specialized agents (see `[[parallel-isolated-agents]]`).
- Open question: how much of the productivity gain comes from the explicit-mode structure itself versus the operator's decades of engineering experience driving it well.