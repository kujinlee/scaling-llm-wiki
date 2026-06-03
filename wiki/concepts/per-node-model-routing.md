---
concept: Per-Node Model Routing
category: Agent Architecture & Patterns
summary: Assigning a specific model to each workflow step by task difficulty: cheap fast models for classification nodes, stronger models reserved for those requiring genuine reasoning.
aliases: [per-node model selection, model routing, tiered model assignment, mixed-model workflows, model specification per node, capability-based routing]
related: [deterministic-workflow-orchestration, harness-engineering, agent-router, cross-model-critique, token-maxing, dark-factory, plan-first-workflow]
sources: [the-next-evolution-of-ai-coding-is-harnesses-here-s-how-to-b, tokenmaxxing-how-top-builders-use-ai-to-do-the-work-of-400-e, every-level-of-claude-explained-in-21-minutes, i-m-building-an-ai-dark-factory-that-ships-its-own-code-publ, claude-code-창시자-boris의-ai-에이전트-셋업-전부-다-까보자]
---

# Per-Node Model Routing

Per-node model routing is the practice of assigning a specific model to each step of an agent workflow according to that step's cognitive difficulty, rather than running the entire process on one model. Cheap, fast models handle low-stakes nodes (classification, routing, simple transforms) while more capable, expensive models are reserved for the nodes that demand genuine reasoning. The result is a deliberate cost/quality tradeoff made at the granularity of individual steps, optimizing total token spend without sacrificing capability where it actually matters.

## Key Mechanics

- Each node in a workflow can declare which model it uses, so model choice becomes a per-step configuration rather than a global setting.
- The heuristic is to match model strength to task difficulty: e.g. a small model (Haiku) for a classification or decision node, a stronger model (Sonnet) for complex reasoning or implementation.
- Routing can be by *capability fit* as well as by cost: assign each step to whichever model is strongest at that kind of work — not only the cheapest model that suffices.
- Speed is a routing variable too: for complex, error-prone steps a slower but more capable model that "wanders" less can be the economical choice, because reducing mistakes shrinks total task time and rework cost more than raw speed would.
- It is a feature of `[[deterministic-workflow-orchestration]]`: because the process is decomposed into explicit nodes, each node is a natural seam at which to swap models.
- The optimization target is the economics of inference — minimizing token cost and latency across a multi-step run while preserving end-to-end output quality.

## How It Appears in the Corpus

The Cole Medin / Archon tutorial highlights model specification per workflow node as a key efficiency lever: a cheaper Haiku model is used for classification while a more powerful Sonnet handles complex reasoning, cutting token consumption and cost without weakening the steps that need a strong model.

The Garry Tan / Y Combinator "Tokenmaxxing" talk shows the *capability-based* variant in G-Stack, which switches models by aptitude — Claude Code for high-level direction and Codex (described as a "200 IQ nearly non-verbal" engine) for the hardest problems — swapping agents seamlessly so each task lands on the best-suited model rather than the cheapest.

The Nate Herk "Every Level of Claude" overview shows the same split inside Claude Code's Plan Mode, which uses the stronger Opus model to draft the plan and the cheaper Sonnet model to execute it — routing the *phases of a single task* across model tiers by difficulty rather than running the whole task on one model.

The Cole Medin "AI Dark Factory" experiment shows cost-driven routing inside an autonomous loop: the issue-*triage* node runs Claude Code routed to a cheaper model (MiniMax M2.7) to classify and prioritize incoming issues, reserving stronger models for the implementation nodes — the same match-cheap-model-to-low-stakes-node heuristic applied to a continuously running factory (`[[dark-factory]]`).

The 김플립 (LLM 코딩) breakdown of Boris's Claude Code setup makes the slower-but-more-reliable case explicitly: for complex work, choose a powerful model like Opus even though it is slower, because it makes fewer mistakes and so reduces overall task time and the cost of rework — picking, for hard tasks, the model that wanders least rather than the one that responds fastest.

## Tensions & Tradeoffs

- Misrouting risk: under-provisioning a node that turns out to need deeper reasoning silently degrades quality, so the difficulty estimate per node must itself be sound.
- Added configuration surface: optimizing model choice per node is another dimension to tune and maintain as models and prices change.
- Cost vs. capability framing: cost-based routing minimizes spend, while the `[[token-maxing]]` philosophy argues for always reaching for the strongest model; capability-based routing reconciles the two by reserving the most powerful (and expensive) model for the hardest nodes — and the Boris setup adds that on complex tasks the strong-but-slow model can be the *cheaper* choice overall once rework is counted, so speed and cost can point in opposite directions.
- Distinct from `[[cross-model-critique]]`, which runs the *same* task on different vendors to harvest disagreement; per-node routing instead splits *different* tasks across models for either cost efficiency or capability fit.
