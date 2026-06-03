---
concept: Value Functions
category: LLM Internals & Training
summary: Continuous internal estimates of state quality — analogized to human emotion — that enable data-efficient generalization, a capacity current reinforcement-learning systems lack.
aliases: [value function, emotion as value function, human value function, innate value function]
related: [reward-hacking, continuous-learning, age-of-research, hill-climbing]
sources: [ilya-sutskever-we-re-moving-from-the-age-of-scaling-to-the-a]
---

# Value Functions

A value function continuously estimates how good a given state or decision is, letting a learner improve from moment-to-moment signal rather than waiting for a sparse, explicit final reward. In human cognition — especially emotions — such value functions are proposed as the missing ingredient behind people's ability to generalize deeply from very little data. Current machine learning lacks a robust analogue, which is offered as a root cause of AI's sample inefficiency.

## Key Mechanics

- A value function supplies intermediate guidance toward good outcomes, so learning does not depend on rare end-of-episode rewards.
- Humans appear to carry innate, evolutionarily derived priors — emotions acting as value functions — that enable efficient, data-light generalization.
- This contrasts sharply with today's reinforcement learning, which leans on explicit and often sparse external rewards, a major source of the data appetite that separates AI from human learners.

## How It Appears in the Corpus

The Ilya Sutskever / Dwarkesh Patel interview introduces value functions and emotions as a blueprint for the sample efficiency and generalization that AI currently lacks, hinting that evolutionary priors are what let humans learn so much from so little.

## Tensions & Tradeoffs

- Origin problem: the human priors are hypothesized to be evolutionary, but how to confer equivalent priors on a machine is unresolved.
- Relation to `[[reward-hacking]]`: a richer internal value function could reduce dependence on gameable external rewards, yet a poorly grounded value function would misguide learning just as confidently — the quality of the signal still bounds the result.