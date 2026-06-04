---
concept: Reasoning via Reinforcement Learning
category: LLM Internals & Training
summary: Using reinforcement learning in verifiable domains so a model discovers its own solution strategies by trial and error — producing emergent chains of thought rather than imitating expert answers.
aliases: [reasoning RL, RL for reasoning, reinforcement learning reasoning, emergent chain of thought, thinking models, DeepSeek R1, RL practice problems]
related: ["[[rlhf]]", "[[verifiability-law]]", "[[chain-of-thought-prompting]]", "[[tokens-to-think]]", "[[reward-hacking]]", "[[value-functions]]", "[[supervised-fine-tuning]]"]
sources: [deep-dive-into-llms-like-chatgpt]
---

# Reasoning via Reinforcement Learning

Reasoning via reinforcement learning is the most advanced LLM training stage, analogous to a student working *practice problems* rather than studying worked examples. Where `[[supervised-fine-tuning]]` makes the model *imitate* expert solutions, reinforcement learning lets the model *discover* good solution paths by trial and error: it generates many candidate solutions to a prompt, and the ones that reach a verified-correct answer are reinforced, iteratively refining the model's strategy. Run in domains where correctness is automatically checkable, this cultivates genuine "thinking" — the model spontaneously produces internal monologues and chains of thought ("wait, let me check my math again") that were never explicitly programmed, an *emergent* cognitive strategy that lifts accuracy on math and coding.

## Key Mechanics

- **Practice problems, not imitation**: the model attempts a problem many ways; solutions that verify as correct are reinforced, so it learns *how to reach* answers rather than copying a single expert path.
- **Emergent chains of thought**: the trained model generates longer, more reflective responses with self-correcting internal monologue (the cited DeepSeek R1 behavior) — reasoning that arises from the RL objective, not from human-written reasoning templates.
- **Requires a verifiable reward**: the loop only works where a correct answer can be automatically confirmed (math with a known result, code that passes tests) — the `[[verifiability-law]]` precondition.
- **The AlphaGo analogy**: in a perfectly verifiable game (Go), RL self-play surpassed human experts, evidence that RL in checkable domains can reach *superhuman* strategies rather than merely matching human imitation.
- **Potential for novel strategies**: because the model explores rather than imitates, RL can uncover solution approaches no human demonstrated — a live research frontier for superhuman reasoning.

## How It Appears in the Corpus

The Andrej Karpathy "Deep Dive into LLMs like ChatGPT" tutorial presents RL as the final, most advanced stage: the model generates many solutions, correct ones are reinforced, and "thinking"/reasoning emerges (DeepSeek R1's reflective monologues). It frames this as imitation-free discovery, contrasts the verifiable case (math, code, AlphaGo's Go) with the unverifiable case handled by `[[rlhf]]`, and flags the discovery of novel, possibly superhuman, reasoning as an open research direction.

## Tensions & Tradeoffs

- **Recasts `[[chain-of-thought-prompting]]`**: explicit "think step by step" prompting becomes unnecessary once reasoning is trained in by RL — the emergent monologue is the same behavior internalized into the weights, the corpus's technique-obsolescence dynamic taken to the training level.
- **Bounded by `[[verifiability-law]]`**: RL's strength is exactly proportional to how cleanly the domain can be scored; outside verifiable domains it gives way to `[[rlhf]]`, whose proxy reward is gameable — so the "discover your own strategy" power does not generalize to unverifiable tasks.
- **Still exposed to `[[reward-hacking]]`**: even verifiable rewards can be gamed if the checker is imperfect, so a clean-looking metric that does not capture the real goal yields confidently wrong reasoning — verifiability enables trust only when the verifier truly captures correctness.
- **Reasoning needs the token budget to exist**: emergent chains of thought are also a *computational* necessity — the model must spread reasoning across many intermediate tokens (`[[tokens-to-think]]`), so RL reinforces not just *what* to think but the habit of thinking *out loud* across enough tokens to compute the answer.