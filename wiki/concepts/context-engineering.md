---
concept: Context Engineering
category: Harness & Context Engineering
summary: Deliberately curating the exact information placed in a single agent's context window — what to include and what to exclude — so one LLM call performs as well as possible.
aliases: [context engineering, context curation, context window management]
related: ["[[harness-engineering]]", "[[claude-md]]", "[[deterministic-workflow-orchestration]]", "[[spec-driven-development]]", "[[per-node-model-routing]]", "[[agentic-search]]"]
sources: [the-next-evolution-of-ai-coding-is-harnesses-here-s-how-to-b, agentic-search-for-context-engineering-leonie-monigatti-elas]
---

# Context Engineering

Context engineering is the practice of deliberately curating the exact information placed in a single agent's context window — the instructions, references, prior state, and task framing — so that one LLM call performs as well as it can. In the corpus's evolution of AI-coding practice it sits between prompt engineering (optimizing the wording of a single output) and `[[harness-engineering]]` (chaining many agent sessions): prompt engineering tunes *how you ask*, context engineering tunes *what the model knows when you ask*, and harness engineering orchestrates *many such well-contexted calls* into a larger process.

## Key Mechanics

- The unit of optimization is the context window of one agent: what reference material, rules, and prior results are present, and what is deliberately excluded as noise.
- Separating concerns across contexts is a core move — for example, doing planning and implementation in *different* contexts so that the implementation step is not biased by the reasoning that produced the plan.
- It is the per-agent substrate a harness composes: a multi-session harness curates a distinct, purpose-built context for each node rather than carrying one ballooning context through every step.
- **Retrieval is most of the work**: deciding what relevant information to pull from diverse sources (files, databases, web, memory) into the window is largely a *search* problem — the corpus's claim is that `[[agentic-search]]` constitutes roughly 80% of context engineering, making the agent's retrieval decisions, not just static curation, the dominant lever.
- `[[claude-md]]` is a standing context-engineering artifact — a persistent, reusable slice of curated project context injected into every run.

## How It Appears in the Corpus

The Cole Medin / Archon tutorial names context engineering as the second stage of AI-coding maturity — "curating perfect context for single agents" — on the path from prompt engineering to harness engineering. Archon operationalizes it by running planning and implementation in separate contexts to reduce bias, and by having dedicated workflow nodes assemble task-specific context before a coding agent acts.

The Leonie Monigatti (Elastic, "AI Engineer" channel) talk reframes context engineering from the *retrieval* side: it defines context engineering as curating the most relevant information for the LLM's window and asserts that agentic search — the agent deciding what context to fetch from which source — is roughly 80% of the job, shifting the emphasis from static, hand-assembled context to dynamic, agent-driven retrieval (`[[agentic-search]]`).

## Tensions & Tradeoffs

- More context is not better context: over-stuffing the window dilutes the relevant signal and consumes budget, so curation means active exclusion, not accumulation — the same staleness/bloat risk noted for `[[claude-md]]`.
- Boundary with `[[harness-engineering]]`: context engineering optimizes a single call while a harness orchestrates many; the corpus treats them as successive stages, but in practice they interlock — a harness is only as good as the context engineered for each of its nodes.
- Separating planning from implementation reduces bias but adds the cost of transferring intent across context boundaries, which must itself be engineered to avoid losing detail.
- **Static curation vs. agentic retrieval**: framing context engineering as mostly `[[agentic-search]]` shifts the bottleneck from authoring good standing context to building good search tools — the agent's retrieval is only as good as the tools and descriptions it draws on (`[[robust-tool-design]]`), so the dynamic view trades authoring effort for tool-engineering effort rather than removing it.
