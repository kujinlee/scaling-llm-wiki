---
concept: Spec-Driven Development
category: Workflows & Methodology
summary: Forcing an agent through ordered phases — explore, brainstorm, spec, plan, implement, verify — with hard gates between them to prevent premature coding and reduce downstream rework.
aliases: [spec-driven development, brainstorm-plan-execute workflow, explore-plan-code, plan-before-code]
related: ["[[agent-tdd]]", "[[spec-review-loop]]", "[[visual-brainstorming]]", "[[self-verification-loop]]", "[[harness-engineering]]", "[[explicit-gears]]", "[[parallel-isolated-agents]]"]
sources: [the-claude-code-plugin-every-developer-must-learn-superpower]
---

# Spec-Driven Development

Spec-driven development is a methodology in which an agent is forced through an ordered sequence of phases — explore, brainstorm, write a design spec, plan, implement, verify — with hard gates between them, rather than jumping straight from a prompt to code. The premise is that front-loading understanding and design produces dramatically better plans and lets the agent often complete a task in a single "one-shot" implementation pass, sharply cutting downstream debugging and rework.

## Key Mechanics

- Ordered phases with explicit gates: brainstorming explores project context and requirements; a design spec is produced and approved; only then is a detailed implementation plan written; implementation and verification follow.
- "Hard gate": coding cannot begin until the design is explicitly approved — the workflow refuses to skip ahead even for tasks that look trivial ("no shortcuts").
- Plans are written to be concrete enough for a junior engineer to follow: granular tasks, file inventories, verification commands, success criteria, and rollback procedures.
- Work is isolated in a git worktree so the main branch stays clean and a botched attempt can be rolled back (see `[[parallel-isolated-agents]]`).
- Each phase composes with other concepts: `[[visual-brainstorming]]` during design, `[[spec-review-loop]]` before planning, `[[agent-tdd]]` during implementation, and `[[self-verification-loop]]` before claiming completion.

## How It Appears in the Corpus

The GritAI Studio walkthrough of the Superpowers plugin (created by Jesse Vincent / "Obra") presents a seven-phase pipeline — brainstorm → git-worktree isolation → plan → sub-agent dispatch → TDD → code review → branch completion — aligned with Claude Code's official "explore, then plan, then code" guidance. The presenter argues that investing in brainstorming and planning yields "tenfold better" plans and frequent one-shot implementations, packaged as the plugin's three core commands (`brainstorm`, `write plan`, `execute plan`).

## Tensions & Tradeoffs

- Up-front cost vs. payoff: the discipline front-loads time into exploration and design, which feels slower on simple tasks; the claimed return is far less rework — the same bet as `[[harness-engineering]]`'s front-loaded investment.
- "No shortcuts" rigidity: enforcing every phase even on trivial work can be overkill, trading flexibility for consistency.
- Boundary with `[[explicit-gears]]`: that concept switches the agent between cognitive modes per kind of work; spec-driven development sequences the phases of a single task. They compose — each phase can run in its own gear.
