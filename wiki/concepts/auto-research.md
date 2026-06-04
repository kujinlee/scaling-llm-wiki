---
concept: Auto Research
category: Workflows & Methodology
summary: Providing an agent with explicit evaluation criteria and letting it verify and improve its own output iteratively until those criteria are met, unattended.
aliases: [auto research, automated research loop, Karpathy auto-research]
related: ["[[self-verification-loop]]", "[[hill-climbing]]", "[[cross-model-critique]]", "[[engineering-taste]]"]
sources: [나의-ai-에이전트-전환기-w-클로드-코드-오픈클로]
---

# Auto Research

Auto research is a methodology — attributed in the corpus to Andrej Karpathy — in which an agent is given explicit evaluation criteria and then repeatedly verifies and improves its own output until it meets them. Its central claim is that even work seemingly requiring human intuition can be decomposed into measurable evaluation dimensions, letting an AI climb toward quality unattended.

## Key Mechanics

- Provide the agent with clear, explicit success criteria rather than a one-shot instruction.
- The agent runs its own verify-and-improve loop, scoring each attempt against the criteria and revising — a focused application of the `[[self-verification-loop]]` toward a quality target, closely related to `[[hill-climbing]]`.
- The key move is decomposing "intuitive" quality into evaluable metrics, so subjective goals become iterable.

## How It Appears in the Corpus

In the Korean agent-transition talk, auto research is applied to a lecture-slide (PPT) generation agent: by the tenth iteration the output quality had improved dramatically over the first version, illustrating that design quality once thought to need human taste could be driven by an automated, criteria-based loop.

## Tensions & Tradeoffs

- Only as good as the criteria: if the evaluation dimensions are wrong or gameable, the loop confidently optimizes the wrong thing — the same failure mode noted for `[[hill-climbing]]`.
- Boundary with human judgment: the method presses against `[[engineering-taste]]`, claiming more "intuitive" quality is automatable than previously assumed, while not establishing where that boundary stops.
