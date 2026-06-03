---
concept: Mixture of Experts
category: LLM Internals & Training
summary: Architecture that holds a large total parameter count while activating only a small fraction per token, decoupling model capacity from per-token compute at the cost of larger weight memory.
aliases: [MoE, mixture-of-experts, sparse models, sparsity, expert parallelism, active vs total parameters, sparse activation]
related: [inference-batching-economics, serving-parallelism, kv-cache-economics, compute-memory-tradeoff, per-node-model-routing, age-of-research]
sources: [how-gpt-claude-and-gemini-are-actually-trained-and-served-re]
---

# Mixture of Experts

Mixture of Experts (MoE) is the architecture that lets a model hold an enormous total parameter count while only *activating* a small fraction of those parameters for any given token, routing each token to a handful of specialized "expert" sub-networks instead of running it through the whole model. The ratio of total to active parameters is the model's **sparsity factor**, and from a systems perspective increasing sparsity is close to a "pure win" for compute: the model gets the representational capacity of a far larger dense network while paying compute only for the active experts — provided the serving system can muster batches large enough to amortize the memory cost of all those parameters.

## Key Mechanics

- **Active vs. total parameters**: a token passes through only its routed experts, so compute (FLOPs/token) scales with *active* parameters while model capacity scales with *total* parameters. DeepSeek is cited at sparsity 8 — 32 active experts out of 256.
- **Sparsity as a compute lever**: raising sparsity adds capacity without proportionally adding per-token compute, a near-free gain on the compute axis — the open question is how far sparsity can be pushed before model quality degrades.
- **The batching catch**: more total parameters means more weight bytes that must be fetched from memory, so the *only* reason high sparsity stays cheap is that large batch sizes amortize that fetch (see `[[inference-batching-economics]]`). Sparsity and batch size are coupled: optimal batch size ≈ 300 × sparsity.
- **Expert parallelism**: experts are physically distributed across GPUs so each holds a subset, which is what makes serving a 256-expert model tractable — but it creates an all-to-all routing communication pattern (detailed under `[[serving-parallelism]]`).
- **Routing**: a gating mechanism decides which experts each token visits, making the architecture sparse *per token* rather than sparse on average.

## How It Appears in the Corpus

Reiner Pope's lecture (Dwarkesh Patel channel) uses MoE as the connective tissue of the whole talk: it defines the sparsity factor (DeepSeek's 8), ties optimal batch size directly to it (300× sparsity), frames raising sparsity as a systems "pure win" bounded only by quality and by the ability to scale batches, and details how expert layers are laid out across GPU racks with all-to-all communication.

## Tensions & Tradeoffs

- **Compute win vs. memory bill**: sparsity cuts per-token compute but inflates the *total* weights that must be stored and streamed, so the saving is real only when batch size is large enough to amortize the extra memory fetch — a `[[mixture-of-experts]]`/`[[inference-batching-economics]]` coupling, not a standalone gain.
- **Quality ceiling on sparsity**: "how far can sparsity be pushed?" is unresolved — past some point routing too few active parameters degrades model quality, so the pure-win framing has an empirical limit the source flags but does not pin down.
- **Physical layout constraints**: expert parallelism's all-to-all traffic is bounded by GPU interconnect topology, so the size of an expert layer is dictated by rack boundaries (`[[serving-parallelism]]`) rather than by the model designer's preference alone.
- **Distinct from `[[per-node-model-routing]]`**: MoE routes *tokens* to expert sub-networks *inside* one model; per-node routing routes *workflow steps* to entirely different models. Both exploit the idea that not every part of a task needs the full heavyweight compute, at very different granularities.