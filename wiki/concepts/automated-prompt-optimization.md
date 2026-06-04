---
concept: Automated Prompt Optimization
category: Workflows & Methodology
summary: Using an algorithmic search (genetic/evolutionary, GEPA-style) to iteratively rewrite an agent's prompt against an eval dataset, breeding higher-scoring candidates until accuracy on a golden set improves.
aliases: [automated prompt optimization, prompt optimization, GEPA, Jeppa, genetic pareto optimization, evolutionary prompt search, prompt tuning, eval-driven prompt optimization, prompt breeding]
related: ["[[custom-eval-systems]]", "[[auto-research]]", "[[hill-climbing]]", "[[self-verification-loop]]", "[[reward-hacking]]", "[[runtime-config-hot-swapping]]", "[[per-node-model-routing]]", "[[token-maxing]]", "[[verifiability-law]]"]
sources: [agent-optimization-with-pydantic-ai-gepa-evals-feedback-loop]
---

# Automated Prompt Optimization

Automated prompt optimization is the technique of treating an agent's prompt as a search variable to be improved by an algorithm rather than hand-tuned by a human: an optimizer repeatedly generates candidate prompts, scores each against a curated evaluation dataset, and keeps the best performers, converging on a prompt that maximizes a measured accuracy. The corpus's instance is a *genetic Pareto* optimizer (GEPA, branded "Jeppa") that "breeds" the best candidates from a Pareto frontier — analogous to selecting top racehorses for reproduction — and can optimize not just plain text but structured strings (complex JSON that defines agent behavior). It is the eval-driven, search-based way to close the gap between an agent that works and an agent that works *reliably* on a specific task, and it only functions where the task has a checkable score — the constructible-verifier precondition of `[[verifiability-law]]`.

## Key Mechanics

- **Golden dataset as ground truth**: optimization is anchored to a curated "golden" set of correct input/output pairs (the corpus's example: ancestral political relations extracted from MP Wikipedia articles, filtering out spouses and children). The dataset *is* the objective function — the optimizer climbs whatever it encodes.
- **Genetic Pareto search**: rather than a single greedy hill-climb, the optimizer maintains a Pareto frontier of candidate prompts and "breeds" the strongest, exploring multiple trade-off dimensions at once instead of optimizing a single scalar — a structured, population-based form of the metric-driven iteration in `[[hill-climbing]]`.
- **An LLM proposes the candidates**: the optimizer uses an agent as its "proposer" to generate and mutate new prompt candidates each round, so the search itself is LLM-driven while the *selection* is eval-driven — an agent improving an agent's instructions, a focused application of the criteria-based self-improvement of `[[auto-research]]`.
- **Optimizes structured config, not just prose**: because candidates can be complex JSON, the same machinery tunes whole behavioral configurations, not merely a text instruction — widening "prompt" to mean the agent's full specification.
- **Measured payoff**: in the demonstration a simple prompt scored ~85% and an expert hand-written prompt ~92% on the golden set, while optimization lifted accuracy to ~96.7% — at the cost of discovering effective but sometimes verbose, less human-legible prompts.
- **Cheaper-model recovery**: optimization is framed as especially valuable for pushing a cheaper or faster model up to acceptable accuracy on domain-specific private data, recovering capability without paying for the strongest model — the inverse lever to `[[token-maxing]]`'s spend-up stance.

## How It Appears in the Corpus

The Samuel Colvin / Pydantic ("AI Engineer" channel) talk demonstrates Jeppa — a genetic-Pareto optimization library — applied to a Pydantic AI agent extracting political ancestral relations from MP Wikipedia articles. Initial simple and expert prompts scored ~85% and ~92% against a golden dataset; Jeppa, using a Pydantic AI agent as its proposer to iteratively generate and evaluate new prompts, raised accuracy to 96.7%. The talk frames prompt optimization as most worthwhile for cheaper/faster models and for large volumes of private, domain-specific data, while flagging variance, model specificity, and the difficulty of optimizing open-ended tasks as real limits.

## Tensions & Tradeoffs

- **Only as good as the golden dataset**: the optimizer maximizes exactly what the eval encodes, so a thin, biased, or wrong golden set yields a confidently over-fit prompt — the `[[reward-hacking]]` ceiling and the "quality of the check bounds the trust" caveat of `[[self-verification-loop]]` and `[[custom-eval-systems]]`, here aimed at the prompt rather than the code.
- **Optimized ≠ legible**: discovered prompts can be effective but verbose and opaque, trading human readability for score — a maintainability cost when an operator later needs to understand or edit the instruction.
- **Open-ended tasks resist it**: optimization needs a scoreable objective, so tasks without a clean verifier (the unverifiable side of `[[verifiability-law]]`) cannot be optimized this way — the same boundary that limits `[[hill-climbing]]` and `[[auto-research]]`.
- **Variance and model specificity**: a prompt optimized for one model may not transfer to another, and run-to-run variance means a single improved score is not a guarantee — so the optimization is coupled to the deployed model, complicating a clean `[[model-abstraction-layer]]` and arguing for re-optimization per model rather than a portable prompt.
- **It is the offline half of a self-driving loop**: optimization discovers a better configuration, but realizing the gain in production without redeploying code requires `[[runtime-config-hot-swapping]]`; the two compose into an autonomous eval → optimize → deploy feedback loop, the corpus's "self-driving" vision.
