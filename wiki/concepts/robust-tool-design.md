---
concept: Robust Tool Design
category: Agent Architecture & Patterns
summary: Building agent tools to survive the three tool-call failure modes — no call, wrong call, bad parameters — via descriptive descriptions, system-prompt reinforcement, on-demand syntax documentation, and self-correcting error handling.
aliases: [robust tool design, tool description engineering, agent tool design, tool calling failure modes, self-correcting tools, tool documentation as skill]
related: ["[[agentic-search]]", "[[low-floor-high-ceiling-tooling]]", "[[tool-integration-hierarchy]]", "[[model-context-protocol]]", "[[auto-correction-loop]]", "[[self-verification-loop]]", "[[lazy-context-loading]]", "[[thin-harness-fat-skills]]", "[[deterministic-workflow-orchestration]]"]
sources: [agentic-search-for-context-engineering-leonie-monigatti-elas]
---

# Robust Tool Design

Robust tool design is the discipline of building an agent's tools so they survive the ways tool calling actually breaks, rather than assuming the model will invoke them correctly. Three failure modes recur: the agent calls *no* tool when it should, calls the *wrong* tool, or calls the right tool with *incorrect parameters*. Each has a specific countermeasure — highly descriptive tool descriptions, reinforcement in the system prompt, on-demand syntax documentation, and error handling that lets the agent self-correct — so the reliability of `[[agentic-search]]` and any tool-using agent lives as much in how the tools are *authored* as in how capable the model is.

## Key Mechanics

- **The three failure modes**: (1) *no tool called* — the agent answers from parametric memory instead of retrieving; (2) *wrong tool called* — it picks an ill-suited tool from the stack; (3) *incorrect parameters* — it constructs a malformed query, especially with complex query languages.
- **Descriptive tool descriptions**: each tool description should spell out its purpose, the conditions that should trigger it, and its relationship to the other tools, so the agent can both decide *whether* to call it and *which* one to choose — the primary defense against the no-call and wrong-tool failures.
- **Reinforce in the system prompt**: tool-selection and tool-use instructions are repeated in the agent's system prompt, not left solely in the per-tool descriptions, so the guidance is present in the always-loaded context.
- **Parameter complexity drives error**: simple parameters are easy for the agent; complex query languages (the source's example is ESQL) demand far more agent intelligence and are where the bad-parameter failure concentrates.
- **Documentation as an agent skill**: when a tool needs a complex syntax the agent keeps getting wrong, supplying detailed reference documentation as a loadable *skill* (e.g. ESQL syntax, including aggregations and the correct wildcard symbol) — explicitly pointed to from the tool description and system prompt — lets the agent generate correct, complex queries. This is `[[lazy-context-loading]]` and the prose-runbook idea of `[[thin-harness-fat-skills]]` applied to tool usage.
- **Error handling for self-correction**: wrapping tool execution so failures return a readable error (e.g. `try-except`) rather than crashing lets the agent read what went wrong and retry — a per-tool instance of the block-and-feedback `[[auto-correction-loop]]`.

## How It Appears in the Corpus

The Leonie Monigatti (Elastic, "AI Engineer" channel) talk on agentic search devotes a section to fundamentals for building robust search tools, naming the three failure modes (no tool, wrong tool, incorrect parameters) and their fixes: descriptive tool descriptions covering purpose, triggers, and inter-tool relationships, reinforcement in the system prompt, and `try-except` error handling for self-correction. Its demonstrations show a vanilla semantic-search tool failing on a specific keyword, a full-query-language tool failing on a wrong wildcard symbol until an "Agent Skill Loading Tool" supplies ESQL syntax documentation, and the agent then generating correct complex queries including aggregations.

## Tensions & Tradeoffs

- **It is the substrate beneath `[[agentic-search]]`**: agent-driven retrieval only pays off if the tools are authored to be chosen and called correctly, so robust tool design is the precondition that turns the agency into reliability rather than new error.
- **Self-correction is bounded by the error message**: an error-handling wrapper helps only if the returned error is interpretable — an opaque or misleading failure leaves the agent retrying blindly, the same "quality of the signal bounds the recovery" caveat as the `[[self-verification-loop]]`.
- **Documentation-as-skill shifts the burden to retrieval**: loading syntax docs on demand keeps the window lean but means the agent must actually load them when needed — the same coverage-by-trigger gap noted for `[[lazy-context-loading]]`.
- **More description costs context**: richly descriptive tool descriptions and system-prompt reinforcement consume standing context, re-raising the `[[tool-integration-hierarchy]]` token discipline — heavy tool schemas are themselves a path to context bloat, so descriptions must be high-signal, not exhaustive.
