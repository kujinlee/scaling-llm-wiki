---
concept: Sampling Parameters
category: LLM Internals & Training
summary: Inference-time controls — temperature, top-k, top-p — that govern the randomness and diversity of token selection, trading deterministic precision against creative variety.
aliases: [sampling parameters, decoding parameters, temperature, top-k, top-p, nucleus sampling, output randomness control, generation parameters, decoding controls]
related: ["[[next-token-prediction]]", "[[reasoning-effort-control]]", "[[tokens-to-think]]", "[[llm-hallucination]]", "[[generative-variation-selection]]", "[[escape-hatch-prompting]]"]
sources: [introduction-to-vertex-ai-studio]
---

# Sampling Parameters

Sampling parameters are the inference-time controls that decide *how* a language model turns its predicted probability distribution over the next token into an actual choice. Because `[[next-token-prediction]]` produces not a single answer but a *distribution* across the whole vocabulary, the system must select one token to emit — and parameters like **temperature**, **top-k**, and **top-p** govern that selection, tuning the output along a spectrum from rigidly deterministic to freely creative. They are a knob on the *decoding* step, distinct from the model's weights or the prompt: the same model on the same prompt produces tightly repeatable output at one setting and varied, exploratory output at another.

## Key Mechanics

- **Temperature — scaling the randomness**: temperature reshapes the probability distribution before sampling. Near 0 it makes selection effectively deterministic (always the most probable token), yielding precise, repeatable output; near 1 it flattens the distribution so lower-probability tokens become viable, yielding more creative and varied output. It is the master dial on the precision-vs-creativity tradeoff.
- **Top-k — restrict to the k most probable**: the model considers only the *k* highest-probability tokens and samples from among them, cutting off the long tail of unlikely words. A small k keeps output focused; a larger k admits more variety.
- **Top-p (nucleus sampling) — a dynamic cumulative threshold**: rather than a fixed count, top-p selects from the *smallest set of tokens whose cumulative probability exceeds p*, so the size of the candidate pool flexes with the model's confidence — narrow when one token dominates, wider when probability is spread out. This gives more adaptive vocabulary control than a fixed k.
- **They shape selection, not knowledge**: these parameters only govern *which* of the model's own predicted tokens gets chosen — they cannot add information the model lacks, only widen or narrow the band of outputs it draws from.

## How It Appears in the Corpus

The Google Cloud "Introduction to Vertex AI Studio" tutorial presents temperature, top-k, and top-p as the parameters for controlling a foundation model's response. It frames temperature as the randomness dial (0 for deterministic, 1 for creative), top-k as selecting from the k most probable words, and top-p as selecting from the smallest set of words whose cumulative probability exceeds p — positioning them alongside prompt design as the levers an operator tunes to match output style to the task.

## Tensions & Tradeoffs

- **Precision vs. creativity, with no universal best**: low settings give reliable, repeatable answers ideal for extraction or classification; high settings give the variety wanted for brainstorming or content generation — the "right" setting is task-dependent, not a global optimum.
- **Distinct from `[[reasoning-effort-control]]`**: effort control dials *how much the model thinks* per prompt; sampling parameters dial *how randomly it chooses* among the tokens it has already computed. One governs deliberation depth, the other decoding randomness — they are orthogonal knobs on output quality.
- **Higher randomness can amplify `[[llm-hallucination]]`**: raising temperature admits lower-probability tokens, which can increase fluent-but-wrong output on factual tasks, so creative settings trade away some factual reliability — sampling parameters tune variety, not correctness.
- **The decoding seam behind `[[generative-variation-selection]]`**: generating many diverse candidates to cherry-pick among them depends on enough sampling randomness to make the candidates actually differ — temperature and top-p are the controls that produce the spread a selection-by-taste workflow harvests.
- **Vantage caveat**: the definitions come from a beginner-oriented vendor tutorial, so they describe the *pattern* — decoding controls that trade determinism against diversity — rather than precise per-model behavior; the durable idea is that token selection is a tunable step separate from the model and the prompt, not any single platform's parameter ranges.
