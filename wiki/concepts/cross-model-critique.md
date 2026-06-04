---
concept: Cross-Model Critique
category: Workflows & Methodology
summary: Improving output by having the primary agent self-critique, then routing the same task to a different vendor's model to harvest divergent perspectives and blind-spot coverage.
aliases: [cross-model self-critique, multi-model review, model-vs-model critique]
related: ["[[auto-research]]", "[[multi-agent-code-review]]", "[[self-verification-loop]]"]
sources: [나의-ai-에이전트-전환기-w-클로드-코드-오픈클로]
---

# Cross-Model Critique

Cross-model critique is the practice of improving an agent's output by having it self-critique and then routing the same task to a *different* AI model so the two exchange divergent opinions. Because models from different vendors have different blind spots, comparing their critiques raises the internal completeness and robustness of the result beyond what a single model's self-review achieves.

## Key Mechanics

- First pass: the primary agent runs a self-critique prompt to surface its own weaknesses.
- Second pass: the same task and critique prompt are given to a different model, and the two sets of feedback are compared and reconciled.
- The value comes from model *diversity* — distinct training and failure modes mean each catches issues the other misses, unlike same-model review.

## How It Appears in the Corpus

The Korean agent-transition talk pairs a Claude Code agent with Codex: the Claude agent self-critiques to find improvements, and Codex is asked to perform the same critique, with the differing opinions exchanged to tighten the result's internal coherence.

## Tensions & Tradeoffs

- Reconciliation cost: divergent critiques must still be adjudicated, which can reintroduce a human or another arbiter.
- Distinct from `[[multi-agent-code-review]]`, which divides labor among specialized agents on a PR; here the same task is duplicated across vendors specifically to harvest disagreement.
