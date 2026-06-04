---
concept: Aspirational Prompting
category: Workflows & Methodology
summary: Instructing an agent to envision the most ambitious version of a solution — a "CEO plan" aimed at 10x value for 2x effort — rather than a minimal literal interpretation.
aliases: [CEO plan, 10-star prompting, 10x meta-prompting, meta-prompting, 11-star experience prompt]
related: ["[[explicit-gears]]", "[[engineering-taste]]", "[[auto-research]]", "[[spec-driven-development]]"]
sources: [tokenmaxxing-how-top-builders-use-ai-to-do-the-work-of-400-e]
---

# Aspirational Prompting

Aspirational prompting is the technique of deliberately instructing an agent to aim far beyond a literal request — to envision the most ambitious, high-value version of a solution — so its output clears a higher bar than a minimal interpretation would produce. The canonical instance is a "CEO plan" prompt, inspired by Brian Chesky's 10/11-star experience exercise, that pushes the AI toward solutions delivering roughly 10x value for 2x effort rather than incremental improvement.

## Key Mechanics

- Reframes the objective upward: instead of "do X," the prompt asks for the version of X a visionary leader would demand, surfacing options the agent would not propose under a literal reading.
- Borrows the "10-star / 11-star experience" design exercise — imagine an absurdly ideal outcome, then work back to what is feasible — and turns it into a reusable prompt pattern.
- A form of meta-prompting: a standing prompt that shapes the agent's *ambition and framing* before it plans, analogous to how `[[explicit-gears]]` switch its cognitive mode.
- Targets disproportionate leverage — "10x value for 2x effort" — rather than marginal gains.

## How It Appears in the Corpus

The Garry Tan / Y Combinator "Tokenmaxxing" talk presents the "CEO plan" as a G-Stack meta-prompt, inspired by Chesky's 10-star concept, used to push Claude Code toward ambitious solutions. It sits alongside the toolkit's CEO/design/dev/eng review modes as a deliberate way to raise the agent's aim.

## Tensions & Tradeoffs

- Ambition vs. scope creep: aiming for 10x can inflate scope and yield over-engineered output, so it needs a human with `[[engineering-taste]]` to keep the bigger vision grounded in what should actually be built.
- It directs *what to aim for*, not whether the result is correct — so it composes with verification loops (`[[auto-research]]`, `[[spec-driven-development]]`) that judge whether the ambitious output actually holds up.