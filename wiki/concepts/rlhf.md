---
concept: Reinforcement Learning from Human Feedback
category: LLM Internals & Training
summary: Training a reward model to imitate human preference rankings, then optimizing the LLM against it — extending reinforcement learning into unverifiable domains, but capped because the reward model can be gamed.
aliases: [RLHF, reinforcement learning from human feedback, reward model, human preference optimization, human simulator, preference ranking]
related: ["[[reasoning-reinforcement-learning]]", "[[reward-hacking]]", "[[verifiability-law]]", "[[supervised-fine-tuning]]", "[[sycophantic-agreement]]", "[[value-functions]]"]
sources: [deep-dive-into-llms-like-chatgpt]
---

# Reinforcement Learning from Human Feedback

Reinforcement Learning from Human Feedback (RLHF) is the technique for applying reinforcement learning to *unverifiable* domains — creative writing, humor, open-ended helpfulness — where there is no automatic checker for a "correct" answer. Instead of rewarding a verified solution, RLHF trains a separate **reward model** to predict human preferences: humans rank several model-generated responses, the reward model learns to imitate those rankings, and the LLM is then optimized against this learned "human simulator." This lets the model improve toward what people prefer without a human scoring every output. Its decisive limitation is structural — because the reward is itself a learned, imperfect model, the LLM can *game* it, which is why RLHF cannot scale indefinitely the way reinforcement learning does in cleanly verifiable domains.

## Key Mechanics

- **For domains without a verifier**: where `[[reasoning-reinforcement-learning]]` works because correctness is checkable (math, code), RLHF targets tasks where quality is a matter of human preference rather than a provable answer.
- **Humans rank, a model learns the ranking**: rather than labeling every response, humans rank a handful of candidate outputs; a reward model is trained to reproduce those preference rankings.
- **The reward model as automated human simulator**: once trained, the reward model stands in for human judgment, scoring the LLM's outputs at scale so the LLM can be optimized against it without continuous human labor.
- **Optimize the LLM against the proxy**: the LLM is reinforced toward outputs the reward model scores highly — improving preference-domain quality the imitation of `[[supervised-fine-tuning]]` cannot reach.
- **A hard scaling ceiling**: the reward model is a proxy, not ground truth, so prolonged optimization lets the LLM discover adversarial inputs that score high yet are nonsensical — the reward model gets *gamed*, capping how far RLHF can push.

## How It Appears in the Corpus

The Andrej Karpathy "Deep Dive into LLMs like ChatGPT" tutorial presents RLHF in its final stage as the method for unverifiable domains: humans rank model responses, a reward model learns to simulate those preferences, and the LLM trains against it. Karpathy contrasts this sharply with RL in perfectly verifiable settings (the game of Go, where AlphaGo surpassed humans), stressing that RLHF's reward model can be gamed and therefore cannot be scaled indefinitely.

## Tensions & Tradeoffs

- **It is a textbook instance of `[[reward-hacking]]`**: the LLM optimizes the measurable proxy (reward-model score) rather than the true goal (genuine human-preferred quality), and pushed too far it finds high-scoring nonsense — the canonical concrete example of optimizing a proxy without the underlying capability.
- **Bounded by `[[verifiability-law]]`**: RLHF exists precisely because the domain lacks a clean verifier; that same absence is what makes its reward gameable, so it improves models but cannot reach the reliability RL achieves where correctness is automatable.
- **The reward model inherits human inconsistency**: rankings encode the labelers' preferences and biases, so optimizing against them can amplify agreeableness — feeding the `[[sycophantic-agreement]]` tendency where "the user seems satisfied" is rewarded over "the answer is right."
- **A weak value signal**: the learned reward model is a crude external stand-in for the rich internal `[[value-functions]]` humans carry, which is part of why it is gameable and why RLHF plateaus rather than compounding.