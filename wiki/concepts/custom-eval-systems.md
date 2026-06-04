---
concept: Custom Evaluation Systems
category: Workflows & Methodology
summary: Domain-specific test suites that judge AI output against operator-defined criteria — instruction adherence, correctness, business goals — as a standing, machine-checkable quality gate.
aliases: [custom evals, evals, eval-driven development, cross-modal eval, product evals, evaluation systems]
related: ["[[engineering-taste]]", "[[cross-model-critique]]", "[[self-verification-loop]]", "[[reward-hacking]]", "[[holdout-validation]]", "[[auto-research]]", "[[ai-native-company]]", "[[thin-harness-fat-skills]]"]
sources: [stanford-cs153-frontier-systems-the-ai-native-company-how-on]
---

# Custom Evaluation Systems

A custom evaluation system is a rigorous, domain-specific test suite an operator builds to judge whether an AI product actually does what users want — distinct from generic capability benchmarks (e.g. MMLU) that say nothing about a particular product's efficacy. As the cost of shipping code approaches zero, the binding constraint becomes *discerning good output from bad*, and evals are how that discernment is made measurable and repeatable: they assess the system against criteria the operator cares about rather than against a leaderboard. They are the executable form of `[[engineering-taste]]` — taste turned into a standing gate inside an agentic workflow.

## Key Mechanics

- **Beyond generic benchmarks**: MMLU-style scores measure raw capability, not product fit; custom evals target specific criteria — adherence to instructions and domain rules, correctness and preservation of customer trust, and achievement of business goals.
- **Human failure-labeling**: humans remain crucial for labeling incorrect interactions and tracing failures back to their cause, supplying the ground truth the eval optimizes toward.
- **Cross-modal eval**: multiple frontier models (e.g. Opus, GPT-5.5) independently assess inputs and outputs and provide iterative feedback for self-improvement — model diversity recruited as the evaluator, the product-quality analogue of `[[cross-model-critique]]`.
- **A first-class workflow component**: founders are urged to actively build and integrate these evals into their agentic systems, so quality measurement is wired into the loop rather than bolted on after.

## How It Appears in the Corpus

The Garry Tan / Diana Hu Stanford CS153 lecture devotes a section to "the enduring value of taste and advanced evaluation systems": with shipping cost near zero, taste — discerning good from bad and building what users truly want — cannot be delegated, and it manifests as rigorous custom evals judging instruction/domain-rule adherence, correctness/trust, and business goals. The lecture describes human labeling of bad interactions and a cross-modal eval in which several frontier models score I/O and feed iterative self-improvement, and exhorts founders to build these systems themselves.

## Tensions & Tradeoffs

- **The eval is the verifier — and only as good as its criteria**: a wrong or gameable eval confidently certifies the wrong product, the `[[reward-hacking]]` ceiling and the "quality of the check bounds the trust" caveat of `[[self-verification-loop]]` applied to product quality.
- **Taste does not vanish, it moves up**: evals scale a human's judgment across agent output, but authoring the eval still requires the very `[[engineering-taste]]` it is meant to operationalize — so the human bottleneck relocates to defining the check.
- **Distinct from one-off critique**: `[[cross-model-critique]]` and `[[holdout-validation]]` harvest disagreement or defeat bias on a single artifact; a custom eval system is a *standing* product-quality gate run continuously, and is what lets an `[[ai-native-company]]` close its loop with trust.
