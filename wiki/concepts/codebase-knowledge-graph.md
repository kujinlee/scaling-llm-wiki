---
concept: Codebase Knowledge Graph
category: Memory & Knowledge Systems
summary: A structured, queryable representation of a codebase's files, dependencies, and relationships, generated automatically so agents and humans can navigate it without file-by-file scanning.
aliases: [code knowledge base, codebase knowledge base, interactive code graph, code dependency graph, code-to-knowledge-base]
related: [llm-knowledge-wiki, context-engineering, claude-md, compound-engineering, token-maxing]
sources: [understand-anything-vs-graphify-i-tested-both-on-my-saas]
---

# Codebase Knowledge Graph

A codebase knowledge graph is a structured, queryable representation of a codebase — its files, components, per-file summaries, and the parent-child and usage relationships between them — generated automatically by an AI tool so that both humans and agents can research and understand the code without scanning it file-by-file. It is a specialization of the `[[llm-knowledge-wiki]]` idea aimed squarely at source code: rather than indexing arbitrary documents, it maps code *structure and dependencies* into navigable layers, surfaces unused code, and answers questions with located, contextualized, often visual explanations — a far richer retrieval surface than `grep`.

## Key Mechanics

- A generation pass analyzes candidate files; scoping (e.g. core applications vs. libraries) and an ignore file that excludes tests, mocks, and other noise bound what gets indexed — trading token spend against coverage.
- The graph captures hierarchy and relationships: a project overview decomposes into architecture layers and then components, with drill-down to trace where a component is used, identify parent-child links, and read per-file summaries and definitions. This is what makes dependencies and dead/unused code visible at a glance.
- Queries return *located, contextualized* answers — file paths, source context (e.g. the originating workflow), step-by-step algorithm breakdowns, and flowcharts — instead of flat text, making it a structured alternative to literal full-text scanning.
- Freshness via auto-update: the graph is regenerated on git commits or branch checkouts so it does not drift stale relative to the code it describes.
- Onboarding artifact: the tool can emit a single markdown summary (project overview + architecture layers) or a multi-article wiki — a *generated* counterpart to a hand-written `[[claude-md]]`.
- The richer the structure, the heavier the build: hierarchical, visual graphs consume more tokens to generate than a flatter single-graph representation.

## How It Appears in the Corpus

The Eric Tech video compares two codebase-to-knowledge-base tools — Understand Anything (installed as a Claude Code marketplace plugin) and Graphy AI (installed via `uv` plus skills). Understand Anything produces a superior, hierarchical drill-down dashboard and more visualized query answers (file locations, algorithms, flowcharts) but consumes roughly double the tokens to build the initial graph. Graphy AI produces a flatter, more cluttered single-graph HTML view, costs fewer tokens, generates a multi-article wiki for onboarding, and — crucially — supports local LLMs (Ollama, Bedrock) for privacy and cost control. Both tools offer auto-update workflows that refresh the graph on git events. The video's recommendation is tool-by-priority: Understand Anything for visualization quality, Graphy AI for lower token cost or when local-model support is required.

## Tensions & Tradeoffs

- Build cost vs. richness: hierarchical, visual graphs cost more tokens to generate than flat ones — a concrete instance of the `[[token-maxing]]` vs. cost-minimization tension, here decided by whether the operator values visualization or budget.
- Privacy: indexing a codebase by default may send code to external AI providers; local-model support (Ollama/Bedrock) keeps code on-premises at some capability cost, a tradeoff one tool documents and the other does not.
- Freshness: like `[[llm-knowledge-wiki]]`'s embedded index and `[[compound-engineering]]`'s accumulated knowledge, the graph drifts stale relative to its source and depends on the auto-update hooks actually firing on commit/checkout.
- Relationship depth bounds understanding: a flat graph reveals only direct neighbors, limiting dependency reasoning beyond one hop — the same "retrieval/structure quality is the new bottleneck" caveat noted for `[[llm-knowledge-wiki]]` and `[[context-engineering]]`.
