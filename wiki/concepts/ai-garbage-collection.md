---
concept: AI Code Garbage Collection
category: Harness & Context Engineering
summary: Periodically and automatically pruning bad code patterns an agent accumulates, keeping the codebase environment optimal so future runs do not build on cruft.
aliases: [garbage collection, AI garbage collection, code pattern cleanup, AI code hygiene, bad-pattern pruning]
related: [harness-engineering, compound-engineering, persistent-agent-memory, context-rot, dark-factory, auto-correction-loop]
sources: [하네스-공식문서-100번-읽은-것처럼-만들어드림]
---

# AI Code Garbage Collection

AI code garbage collection is the practice of periodically and automatically cleaning up the bad, duplicated, or dead code patterns an AI agent accumulates over time, so that every new task starts from an optimal codebase rather than building atop the agent's own cruft. It is the entropy-fighting counterpart to `[[compound-engineering]]`: where compound engineering deliberately *accumulates* hard-won knowledge into the environment, garbage collection deliberately *prunes* the low-quality artifacts the agent generates, and the two together keep the working environment both knowledgeable and clean.

## Key Mechanics

- A scheduled or automatic pass removes problematic code patterns the AI produced, preventing them from compounding into a degraded codebase the next agent run would imitate.
- Keeping the environment optimal is the goal: a clean codebase is itself part of the context an agent reads, so pruning bad patterns improves future generations the way good docs do.
- It is reflexive with harness refinement: each detected agent mistake is converted into a new harness rule, so cleanup feeds back into a more precise `[[harness-engineering]]` over time.
- It is one of the three harness pillars in the source's framing, alongside the context file (`[[claude-md]]`) and the automatic enforcement system (`[[auto-correction-loop]]`).

## How It Appears in the Corpus

The 캐슬 (아는 개발자) harness explainer presents garbage collection as the third harness pillar: a system that periodically and automatically clears away the accumulating bad code the AI generates, so the agent always works in an optimal environment, with each AI mistake transformed into a new rule that sharpens the harness.

## Tensions & Tradeoffs

- Mirror image of `[[compound-engineering]]`: one accumulates good knowledge, the other prunes bad artifacts — both are needed to keep an agent's environment from drifting, and the memory-side analogue is the prune-and-merge consolidation of `[[persistent-agent-memory]]`.
- Defining "bad pattern" for automated removal is hard: aggressive collection risks deleting intentional or context-dependent code, so the cleanup criteria are themselves a quality bottleneck.
- It guards against the code-side analogue of `[[context-rot]]` — cruft buildup that quietly degrades the environment — but only as well as its detection rules surface what actually counts as garbage.
