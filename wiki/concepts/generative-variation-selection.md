---
concept: Generative Variation Selection
category: Workflows & Methodology
summary: Using inference speed to generate many variations of an artifact (e.g. 15–75 versions of a UI component) in the time one used to take, then cherry-picking the best — injecting human taste and variety by selection rather than by up-front specification.
aliases: [cherry-picking, generative variation selection, generate-and-select, many variations cherry-pick, variation sampling, taste by selection, parallel variation generation]
related: [fast-models-slow-developers, curated-design-systems, engineering-taste, visual-brainstorming, aspirational-prompting, cross-model-critique, token-maxing, free-validation-at-speed]
sources: [fast-models-need-slow-developers-sarah-chieng-cerebras]
---

# Generative Variation Selection

Generative variation selection — "cherry-picking" — is the technique of exploiting fast inference to generate *many* alternative versions of an artifact (the corpus cites 15–75 versions of a UI component) in roughly the time it once took to produce a single one, then selecting the best. The defining move is that the developer supplies *taste and variety by selection* rather than by specification: instead of trying to articulate the perfect result in a prompt up front, they let the fast model produce a wide spread of candidates and exercise judgment by picking the strongest, effectively inducing taste and desired variety into the model's output after the fact. It converts speed into *exploration breadth* — sampling the space of possible outputs and curating it — rather than into raw throughput on one path.

## Key Mechanics

- **Generate wide, then select**: rather than one attempt, the fast model produces a batch of distinct variations (15–75 cited for a UI component) cheaply, turning a single-shot generation into a curated set the developer chooses from.
- **Taste enters by curation, not specification**: the hard-to-articulate quality the developer wants is supplied by *recognizing* it among candidates rather than by describing it in advance — the human contributes `[[engineering-taste]]` as a selector, sidestepping the difficulty of fully specifying intent in a prompt.
- **Variety is induced, not prompted**: because the candidates differ, the batch surfaces options the developer would not have thought to ask for — the selection step harvests serendipity the way `[[visual-brainstorming]]` harvests design choices, but driven by sheer generation volume.
- **Enabled by the speed dividend**: cherry-picking is only affordable because generation is nearly free — it is one of the quality reinvestments of `[[fast-models-slow-developers]]`, spending speed on breadth-of-options instead of on more unverified single outputs.

## How It Appears in the Corpus

The Sarah Chieng (Cerebras, "AI Engineer" channel) talk "Fast Models Need Slow Developers" presents "cherry-picking" as a core speed-era tactic: leverage 1,200-tokens/second generation to produce many variations (e.g. 15–75 versions of a UI component) in the time it previously took to generate one, then pick the best output — explicitly framed as a way to "induce taste and desired variety" into the model's creations by selecting among a wide set rather than relying on a single attempt.

## Tensions & Tradeoffs

- **Selection quality bounds the result**: generating 75 variations only helps if the developer can recognize the best one — the value rests entirely on human `[[engineering-taste]]`, so a weak selector confidently picks a weak option, and a batch of bad variations cannot be cherry-picked into a good outcome.
- **Distinct from `[[cross-model-critique]]`**: that pattern runs the *same* task on different vendors to harvest disagreement and reconcile it; cherry-picking generates *many candidates from one fast model* and keeps one, with no critique loop — selection replaces reconciliation.
- **Complements `[[curated-design-systems]]`'s self-critique**: a multi-dimensional self-critique scores and revises a single output toward criteria, whereas variation selection produces a spread and lets a human judge — the two compose (generate many, critique each, then pick), but selection-by-taste resists the convergence-to-a-house-style risk that a fixed critique rubric carries.
- **The token-spend reading**: generating dozens of variations is the `[[token-maxing]]` stance applied to exploration — it buys breadth at the cost of inference, justified only where the artifact's quality genuinely benefits from a wide search rather than a single competent attempt.
- **Vantage caveat**: the 15–75 figure is illustrative of the *generate-wide-then-select* pattern from one talk, not a measured optimum — the durable idea is curating taste from a fast-generated spread, not a specific count.
