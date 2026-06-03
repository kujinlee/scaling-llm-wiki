---
concept: Jagged Intelligence
category: LLM Internals & Training
summary: LLM competence is wildly uneven — genius-level on scoreable tasks, error-prone on ambiguous ones — because the model is a reward-shaped statistical simulation, not an evolved mind.
aliases: [jagged intelligence, uneven AI capability, spiky capability, ghost not animal, AI as a ghost]
related: [verifiability-law, reward-hacking, engineering-taste, value-functions, thinking-vs-understanding, graduated-autonomy, software-3-0]
sources: [꼭-알아야할-안드레-카파시-30분-인터뷰-완전정리-ai시대의-필수-인사이트]
---

# Jagged Intelligence

Jagged intelligence is the observation that an LLM's competence is wildly uneven across domains: genius-level where answers are cleanly checkable, yet capable of absurd blunders where judgment is fuzzy. A model can solve hard mathematics or write code that compiles and passes tests, then fail a piece of everyday common sense (whether to drive or walk to the car wash) or an aesthetic call. The root cause is that an LLM is not an evolved animal mind but a statistical simulation shaped by data and reward functions — Karpathy's "a ghost, not an animal" — so its capability surface is spiky rather than smoothly general, and a human must therefore stay in the loop wherever the jaggedness bites.

## Key Mechanics

- **Strong where verifiable, weak where not**: the model excels in "scoreable" domains (math, compiling/passing tests) and degrades where success criteria are ambiguous (common sense, taste) — the capability profile explained by `[[verifiability-law]]`.
- **Ghost, not animal**: because the model is a reward-shaped statistical simulation rather than an evolved organism, animal intuitions do not transfer — yelling at or pleading with it does not help. The right stance is to explore the model's "circuits" empirically to learn where it is and isn't reliable.
- **Human-in-the-loop mandate**: the operator may use the LLM as a tool but must not hand it final decision authority; as long as the intelligence is jagged, a human supervisor is required to catch the systemic mistakes (e.g. a functionally-working change that introduces a serious security flaw).
- **Intern, not expert**: the model is framed as roughly intern-level — impressive yet prone to errors that are fine functionally but broken systemically — which is why high-level human specification and supervision remain essential.

## How It Appears in the Corpus

The Kimflip (김플립) summary of Karpathy's interview names "jagged intelligence," contrasting the model's brilliance on verifiable tasks with bizarre failures on subjective ones, and traces both to the LLM being a data-and-reward statistical simulation rather than an evolutionary product. It uses the "ghost not animal" metaphor to warn against applying animal intuitions, and concludes that humans must remain in the loop, designing high-level specs and supervising while the model fills them in.

## Tensions & Tradeoffs

- It is the behavioral face of `[[reward-hacking]]`: a system shaped by proxy reward signals is exactly one that can be flawless on the measured dimension and senseless off it, so jaggedness and metric-gaming share a cause.
- The missing-ingredient framing connects to `[[value-functions]]`: humans carry evolutionary priors (emotion as a value function) that give smooth, data-light generalization, which the statistical model lacks.
- The boundary of the jagged region is moving: as more tasks become verifiable, the zone needing human `[[engineering-taste]]` shrinks — but the corpus does not claim it vanishes, and `[[graduated-autonomy]]` is the discipline for expanding trust only as the model proves reliable on each new region.
