---
concept: Tokens to Think
category: LLM Internals & Training
summary: Because an LLM performs a finite, fixed amount of computation per token, complex reasoning must be spread across many intermediate tokens rather than compressed into one — so step-by-step output is a computational necessity, not just a style.
aliases: [tokens to think, computation per token, cognitive deficits, distributed reasoning, sequential reasoning, mental arithmetic limit, finite compute per token]
related: ["[[chain-of-thought-prompting]]", "[[llm-tool-augmentation]]", "[[tokenization]]", "[[reasoning-reinforcement-learning]]", "[[jagged-intelligence]]", "[[next-token-prediction]]"]
sources: [deep-dive-into-llms-like-chatgpt]
---

# Tokens to Think

Tokens to think is the principle that an LLM does a *finite, fixed* amount of computation to produce each token, so any reasoning too complex to fit in that per-token budget must be *spread across many tokens* — intermediate steps the model writes out as it works. The model has no scratchpad other than the tokens it generates; demanding a hard multi-step answer in a single token forces it to compress reasoning it cannot actually perform in one forward pass, and it fails. Give it room to "think" across a sequence of intermediate tokens and accuracy on the same task improves dramatically. This reframes step-by-step output from a stylistic nicety into a *computational requirement* of how the architecture works.

## Key Mechanics

- **Fixed compute per token**: each token is produced by one pass of a fixed function (`[[next-token-prediction]]`), so the per-token "thinking" capacity is bounded — there is no way to do unboundedly hard reasoning inside a single token.
- **Distribute reasoning across tokens**: complex tasks (multi-step math, counting, intricate spelling manipulation) must be broken into intermediate steps the model emits, effectively using the output sequence as working scratch space — "mental arithmetic" needs sequential tokens.
- **Compression causes failure**: asking for the final answer directly, with no intermediate steps, is where these tasks break; the same model that fails one-shot often succeeds when allowed to reason out loud.
- **Tokenization compounds it**: character-level tasks (counting letters, spelling) are extra hard because the model sees sub-word `[[tokenization|tokens]]`, not characters — the representation hides the very units the task is about.
- **External tools as an escape**: for precise computation, offloading to a tool (a Python interpreter via `[[llm-tool-augmentation]]`) sidesteps the per-token limit entirely, trading internal reasoning for an exact external result.

## How It Appears in the Corpus

The Andrej Karpathy "Deep Dive into LLMs like ChatGPT" tutorial attributes a class of "cognitive deficits" to token-based processing with finite computation per token: models struggle with precise, distributed reasoning unless given enough "tokens to think," so explicit step-by-step reasoning — or an external Python interpreter — dramatically improves accuracy on math, counting, and spelling tasks.

## Tensions & Tradeoffs

- **A complementary framing to `[[chain-of-thought-prompting]]`**: the corpus's CoT page stresses that chain-of-thought is *more than a computational placeholder* — the reasoning genuinely helps. This source emphasizes the *computational-substrate* half: the model also literally *needs* the tokens to compute. Both are true — externalized reasoning is real cognitive work *and* the only place per-token-bounded computation can happen — so they refine rather than contradict each other.
- **Why `[[reasoning-reinforcement-learning]]` works**: RL reinforces longer, reflective outputs precisely because spreading reasoning across tokens is what lets hard problems be solved — the emergent chain of thought is the model learning to spend its token budget on thinking.
- **It is the mechanical root of part of `[[jagged-intelligence]]`**: a model that aces a problem with steps and fails it one-shot is uneven not from missing knowledge but from a compute-per-token limit — a deficit that prompting structure, not a bigger model, often fixes.
- **More tokens is not free correctness**: room to reason raises the *chance* of a right answer but does not guarantee it; on unverifiable tasks a long, confident, wrong chain can still emerge, so the budget enables reasoning without certifying it.