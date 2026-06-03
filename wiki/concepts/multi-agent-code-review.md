---
concept: Multi-Agent Code Review
category: Workflows & Methodology
summary: Dividing code review across specialized AI agents (style vs. deep context, spec vs. implementation) that interact through the PR comment cycle without a human driving each step.
aliases: [multi-agent review, automated code review pipeline]
related: [agentic-issue-resolution, self-verification-loop, engineering-taste, claude-md, spec-review-loop, cross-model-critique]
sources: [live-coding-session-with-boris-cherny-and-jarred-sumner, the-claude-code-plugin-every-developer-must-learn-superpower]
---

# Multi-Agent Code Review

Multi-agent code review divides the review task across several specialized AI agents, each responsible for a different layer of quality, and lets them interact through the normal PR comment cycle. By assigning style to one agent and deep, context-dependent reasoning to another, the system automates routine review work while reserving harder judgment for more capable agents.

## Key Mechanics

- Division of labor: one agent enforces stylistic and standards compliance, while another focuses on subtle edge cases that require deep contextual understanding of the codebase.
- Agents communicate through the PR itself — leaving comments and resolving them in back-and-forth — so the review cycle runs without a human driving each step.
- Reviews target the spec: a dedicated review sub-agent checks each implementation against the agreed design specification, catching divergences before they compound.
- Receiving review with rigor: the agent under review must not blindly agree with feedback — it verifies each comment technically and only acts on what holds up, preventing performative "yes" loops between agents.
- Removes mundane toil (lint errors, context switching), freeing human attention for genuinely complex problems, which matters especially for a low-level systems codebase.

## How It Appears in the Corpus

The Boris Cherny and Jarred Sumner session describes Bun pairing a style-focused reviewer (Code Rabbit) with `[[claude-md]]`-grounded deep review from Claude Code, the two agents leaving and resolving comments on each other's work.

The Superpowers plugin (GritAI Studio walkthrough) generalizes the pattern across the lifecycle: sub-agents review each implementation against the spec during execution, a "Receiving Code Review" skill instructs Claude to verify feedback rather than accept it blindly, and a `[[spec-review-loop]]` applies the same reviewer pattern to the design document before any code is written.

## Tensions & Tradeoffs

- Agreement and termination: relying on agents to leave and resolve each other's comments raises the question of when a review cycle is genuinely "done" — addressed in the spec phase by an explicit iteration cap (see `[[spec-review-loop]]`).
- Same-model reviewers share the author's blind spots; `[[cross-model-critique]]` harvests disagreement by switching vendors.
- Human judgment is still retained for strategic calls — see `[[engineering-taste]]`.
