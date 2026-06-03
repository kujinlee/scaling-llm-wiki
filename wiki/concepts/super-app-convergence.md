---
concept: Super App Convergence
category: Harness & Context Engineering
summary: The trend of foundation models absorbing the best features of external harnesses and meta-harnesses, so the model itself becomes a general-purpose "super app" — collapsing the gap that third-party orchestration tooling once filled.
aliases: [super apps, harness absorption, harness war, meta-harness absorption, feature absorption into models, capability convergence, oh-my-claude, oh-my-codex]
related: [harness-engineering, thin-harness-fat-skills, self-modifying-agent-harness, agentic-coding-tool-selection, model-abstraction-layer, inference-batching-economics, distributed-systems-literacy, distribution-over-features]
sources: [ep-97-ai-psychosis-시대의-사람들]
---

# Super App Convergence

Super app convergence is the pattern in which the best features of external harnesses and "meta-harnesses" are progressively absorbed directly into the foundation models, so the model and its first-party tool (Codex, Claude Code) grow into general-purpose "super apps" that handle diverse tasks natively — collapsing the gap that third-party orchestration tooling was built to fill. It is the concrete mechanism behind `[[harness-engineering]]`'s forecast that harnesses *simplify* as models improve: a positive feedback loop in which models get more capable, harnesses evolve to exploit them, and the most useful harness innovations are then folded back into the next model release, leaving the standalone tool thinner each cycle.

## Key Mechanics

- **Meta-harnesses get absorbed**: orchestration layers built on top of coding agents (the source cites `oh-my-claude` and `oh-my-codex`) gain traction by chaining and coordinating tasks, but their best capabilities are then integrated directly into the foundational tools — so the external layer's edge is temporary by construction.
- **Model-as-super-app**: as features accumulate inside it, the model stops being a narrow code-completion engine and becomes a general-purpose system able to handle diverse tasks with broad ability — the "super app" framing.
- **A competitive "harness war"**: the absorption is driven by rivalry among the labs (OpenAI and Anthropic racing on harness features), with Google framed as less aggressive on incremental harness features but aiming for a "game changer" goal-oriented-completion approach (e.g. via an AI Studio platform) rather than conversational back-and-forth.
- **Compute disparity sets the pace**: which lab can absorb features fastest is gated by computational resources — the source notes Codex rapidly catching up to (and potentially surpassing) Claude Code, whose service quality fluctuated under Anthropic's tighter compute, tying the convergence race to the serving economics of `[[inference-batching-economics]]`.
- **Shrinking release cycles**: frontier models now ship significant updates every couple of months, so the absorb-and-release loop turns fast enough that a harness feature can be commoditized within a single cycle.

## How It Appears in the Corpus

The 노정석 "EP 97. AI Psychosis 시대의 사람들" analysis traces the rapid evolution of AI harnesses: popular meta-harnesses like `oh-my-claude` and `oh-my-codex` orchestrated tasks, but their best features are being pulled directly into Codex and Claude Code, which are becoming "super apps" with general task ability. It frames a "harness war" between OpenAI and Anthropic (with Google pursuing a goal-completion game-changer instead), names compute resources as the decisive lever — Codex catching up to a compute-constrained Claude Code — and notes the shrinking frontier-model release cycle as what makes the absorb-and-ship loop so fast.

## Tensions & Tradeoffs

- **Building on the gap is precarious**: a harness or meta-harness that thrives by filling a model's current shortfall is competing against the entity that ships the model — the same "road that arrives nowhere" risk `[[distribution-over-features]]` and the expert-vs-model-domain split warn about, here aimed at orchestration tooling. The durable value migrates to whatever the model does *not* absorb (proprietary data, vertical workflows), not to the harness itself.
- **Reinforces the thin-harness bet, complicates the fat-harness one**: convergence is direct evidence for `[[thin-harness-fat-skills]]` and `[[self-modifying-agent-harness]]` (keep the loop minimal; behavior migrates into the model and editable skills), and in tension with elaborate multi-workflow harness systems whose value erodes as the model internalizes their function — the unresolved "do harnesses trend simpler or more complex?" question `[[harness-engineering]]` raises.
- **Convergence narrows tool differentiation**: as rival super apps absorb the same features, capability parity sharpens the `[[agentic-coding-tool-selection]]` point that the choice turns on workflow fit, not feature checklists — and strengthens the case for a `[[model-abstraction-layer]]` since the leaders keep leapfrogging.
- **Vantage caveat**: the harness-war framing and the Codex-vs-Claude-Code trajectory come from a point-in-time discussion podcast, so specific tool standings are perishable — the durable idea is *capability absorption into the model*, not which lab is currently ahead.
