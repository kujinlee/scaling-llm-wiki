---
concept: LLM Hallucination
category: LLM Internals & Training
summary: LLMs confidently fabricate information when uncertain because they imitate the style of correct answers without the underlying knowledge — mitigated by training refusal and by external tool use.
aliases: [hallucination, hallucinations, LLM hallucination, confabulation, fabrication, swiss cheese capabilities, vague recollection]
related: ["[[llm-tool-augmentation]]", "[[sycophantic-agreement]]", "[[jagged-intelligence]]", "[[tokens-to-think]]", "[[escape-hatch-prompting]]", "[[next-token-prediction]]"]
sources: [deep-dive-into-llms-like-chatgpt]
---

# LLM Hallucination

Hallucination is the failure mode in which an LLM fabricates information — stating something false with full confidence — most often when it is uncertain. Its root cause is structural: the model's knowledge is a *vague recollection* stored implicitly in its parameters from `[[next-token-prediction]]`, and `[[supervised-fine-tuning]]` taught it to confidently imitate the *style* of correct answers. So when factual knowledge is thin, the model still produces a fluent, authoritative-sounding answer rather than admitting ignorance — it is pattern-matching the shape of a good answer, not checking whether it knows. This is one face of the "Swiss cheese" capability surface: impressive fluency riddled with surprising factual holes.

## Key Mechanics

- **Vague parametric recollection**: facts live lossily in the weights, so the model often "sort of" remembers — enough to generate plausible text, not enough to be reliably correct.
- **Confident style imitation**: training rewards answers that *look* like correct answers, so the model defaults to a confident register even with no factual basis — the fabrication wears the costume of knowledge.
- **Mitigation 1 — train refusal**: models can be explicitly trained to recognize and *decline* when they don't know ("I don't know"), converting a confident fabrication into an honest non-answer — the training-side analogue of `[[escape-hatch-prompting]]`.
- **Mitigation 2 — external tools**: equipping the model to call a web search or other tool (`[[llm-tool-augmentation]]`) lets it retrieve real facts into its working memory instead of inventing them, sharply improving factuality.

## How It Appears in the Corpus

The Andrej Karpathy "Deep Dive into LLMs like ChatGPT" tutorial treats hallucination as a central cognitive trait: models fabricate when uncertain because they confidently imitate the style of correct training answers despite lacking the knowledge. It prescribes two mitigations — explicitly training the model to refuse when it doesn't know, and giving it tools (search) to ground answers in retrieved fact — and folds hallucination into the broader "Swiss cheese" picture of advanced skills alongside surprising deficiencies.

## Tensions & Tradeoffs

- **Distinct from but kin to `[[sycophantic-agreement]]`**: hallucination is fabricating *facts*; sycophancy is going along with a flawed *premise* — both stem from a model optimized to produce satisfying-looking output rather than to verify truth, two surfaces of the same reward-shaped behavior.
- **It is what `[[jagged-intelligence]]` looks like on knowledge**: brilliant on what it knows, confidently wrong on what it doesn't, with no smooth signal marking the boundary — which is exactly why a human must stay in the loop.
- **Refusal trades coverage for honesty**: training the model to decline reduces fabrication but risks it bailing on questions it *could* answer — the same threshold-tuning problem as `[[escape-hatch-prompting]]`, and it only works where the model can recognize its own uncertainty.
- **Tools mitigate but add dependency**: retrieval grounds answers in fact, yet shifts trust to the tool and the retrieved source — and tool use itself depends on the model emitting the right call at the right time (`[[llm-tool-augmentation]]`).