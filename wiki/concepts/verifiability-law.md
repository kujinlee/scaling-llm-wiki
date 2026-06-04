---
concept: Verifiability Law
category: LLM Internals & Training
summary: LLM competence tracks how cleanly a task can be scored: reliable automatable verifiers enable autonomous trust; absent them, capability turns jagged and human oversight is required.
aliases: [verifiability law, verifier's law, scoreable-task principle, checkable equals automatable, verifiability of tasks]
related: ["[[jagged-intelligence]]", "[[hill-climbing]]", "[[self-verification-loop]]", "[[reward-hacking]]", "[[exploratory-spec-discovery]]", "[[auto-research]]", "[[agentic-issue-resolution]]", "[[reasoning-reinforcement-learning]]", "[[rlhf]]"]
sources: [꼭-알아야할-안드레-카파시-30분-인터뷰-완전정리-ai시대의-필수-인사이트, deep-dive-into-llms-like-chatgpt]
---

# Verifiability Law

The verifiability law is the principle that an LLM's competence tracks how cleanly a task can be *scored*: where there is a reliable, automatable check on correctness, the model performs brilliantly; where there is no such check, capability turns jagged and unreliable. Verifiability — not raw difficulty — is the dividing line between what AI can be trusted to do autonomously and what it cannot. It is the positive statement underlying much of this corpus: nearly every autonomous-agent pattern works precisely because it manufactures a verifier the agent can climb against.

## Key Mechanics

- **Scoreable means strong**: domains with a definitive check — math with a known answer, code that must compile and pass tests — are exactly where the model is genius-level; absence of a clear check is where it stumbles (the failure side is `[[jagged-intelligence]]`).
- **A verifier is the entry condition for autonomy**: it is why `[[hill-climbing]]` and `[[exploratory-spec-discovery]]` insist on a *verifiable goal* (a completable plan or a measurable metric), why `[[self-verification-loop]]` and `[[auto-research]]` demand the agent produce evidence before claiming success, and why `[[agentic-issue-resolution]]` gates on a fail-then-pass regression test.
- **It is a training-time law, not only a usage-time one**: the same dividing line governs how models are *built*. Reinforcement learning in verifiable domains (`[[reasoning-reinforcement-learning]]`) can reach superhuman strategy — math, code, AlphaGo's Go — because the reward is true correctness; unverifiable domains (creative writing, humor) must fall back to `[[rlhf]]`, whose learned reward model is a gameable proxy. Capability scales further exactly where verification is clean.
- **Verifiability is constructible**: tasks once thought "intuitive" can sometimes be decomposed into evaluable dimensions (`[[auto-research]]`), expanding the region where the law makes automation possible.
- **Hiring and design implication**: as scoreable work is absorbed by agents, the human value concentrates in the unverifiable judgments — what to build and why — and in designing systems robust enough to survive adversarial agents (the corpus's "build a Twitter clone that ten hacking agents can't breach" hiring test).

## How It Appears in the Corpus

The Kimflip (김플립) summary of Karpathy's interview states the law directly: LLMs are geniuses only in "채점 가능한" (scoreable) domains — math, code that compiles and passes tests — and turn jagged wherever verification criteria are ambiguous. The summary makes verifiability the explanatory hinge for both the model's strengths and its blunders, and for why humans must supervise the unverifiable parts.

The Andrej Karpathy "Deep Dive into LLMs like ChatGPT" tutorial supplies the training-side evidence for the same law: reinforcement learning produces strong, even superhuman, reasoning in *perfectly verifiable* domains (math, code, the game of Go via AlphaGo), while *unverifiable* domains require `[[rlhf]]`, whose reward model can be gamed and therefore cannot scale indefinitely — making verifiability the property that decides how far a model can be pushed.

## Tensions & Tradeoffs

- **A verifier is only as good as what it measures**: the law cuts both ways with `[[reward-hacking]]` — a clean but *wrong* or gameable check produces confidently incorrect output, so verifiability enables trust only when the check actually captures the real goal (the "quality of the check bounds the trust" caveat of `[[self-verification-loop]]`). A *learned* verifier (the RLHF reward model) is the most gameable case.
- **The valuable-but-unverifiable frontier**: many high-value tasks (taste, strategy, system understanding) resist clean scoring, so the law marks the boundary where `[[engineering-taste]]` and `[[thinking-vs-understanding]]` keep humans in charge rather than a region AI will soon absorb.
- **Constructing verifiers has limits**: decomposing intuitive quality into metrics (`[[auto-research]]`) extends the law's reach but cannot rescue a goal whose true property — robustness, generalization — is not directly measurable.