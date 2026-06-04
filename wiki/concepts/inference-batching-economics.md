---
concept: Inference Batching Economics
category: LLM Internals & Training
summary: Batch size is the dominant cost lever for LLM serving: amortizing weight fetches across concurrent requests cuts cost-per-token by orders of magnitude, with optimal batch size tied to model sparsity.
aliases: [batching, batch size economics, inference batching, roofline inference, amortizing weight fetches, optimal batch size, fast mode pricing]
related: ["[[mixture-of-experts]]", "[[kv-cache-economics]]", "[[kv-cache-paging]]", "[[prefill-decode-inference]]", "[[serving-parallelism]]", "[[compute-memory-tradeoff]]", "[[subscription-vs-metered-pricing]]", "[[per-node-model-routing]]", "[[token-maxing]]"]
sources: [how-gpt-claude-and-gemini-are-actually-trained-and-served-re, ep-96-llm-추론-인프라와-토큰-경제학]
---

# Inference Batching Economics

Inference batching economics is the principle that the dominant lever on the cost and latency of serving an LLM is the *batch size* — how many user requests are processed concurrently — because batching amortizes the fixed cost of fetching the model's weights from memory across many requests at once. A single request must pay to stream the entire weight matrix through the compute units just for itself; a batch of two thousand requests pays that same fetch once and splits it, so cost-per-token collapses by orders of magnitude as the batch grows. This is the hidden machinery behind consumer-facing oddities like "Fast Mode" pricing, where paying more buys faster token streaming.

## Key Mechanics

- **Roofline framing**: each inference step's latency is bounded by the *maximum* of two times — compute time (set by active parameters × FLOPs per token) and memory-fetch time (streaming the weights *and* the KV cache out of HBM). Whichever is larger is the binding constraint, and the goal is to operate where they balance. The `[[prefill-decode-inference|prefill]]` phase sits on the compute side of this roofline and `[[prefill-decode-inference|decode]]` on the memory side.
- **Amortization curve**: at small batch sizes the per-token cost is astronomically high because the weight fetch is unamortized — one user pays to move the whole model. As batch size rises, that fetch is split across more sequences, so cost-per-token falls steeply, then *plateaus* once the system becomes compute-limited rather than memory-limited.
- **The Goldilocks batch size**: the optimum sits where weight-fetch time and compute time are equal, derived in the source as roughly **300 × the model's sparsity factor**. For a frontier MoE like DeepSeek (sparsity 8 — 32 active experts of 256), that is ~2,400 unique sequences; in practice operators run 2–3× higher to absorb real-world inefficiency.
- **The 300 ratio is roughly constant across hardware generations**: the second corpus source notes that the ratio of a GPU's FLOPs to its memory bandwidth stays approximately constant generation to generation (cited at ~300× for FP4 precision), so the *same* "optimal batch ≈ 300 ÷ sparsity" rule holds across hardware — DeepSeek's 1/8 sparsity again yielding B ≈ 2,400 — making the heuristic durable rather than tied to one chip.
- **Throughput translation**: a batch of ~2,000 sequences at a ~20 ms "train departure" / "drain time" interval yields on the order of 128,000 tokens/second — the scale a competitive AI service must reach to be economical, and the number that ties batch size to how many users a GPU serves per cycle.
- **A fundamental floor**: for a given hardware configuration, batching sets a hard lower bound on achievable latency and cost; "fast mode" is selling a *smaller, lower-latency* batching regime at a higher per-token price.

## How It Appears in the Corpus

Reiner Pope's blackboard lecture (Dwarkesh Patel channel, "How GPT, Claude, and Gemini are actually trained and served") opens by deriving the cost-per-token-vs-batch-size curve from a roofline analysis, showing the steep early drop and eventual compute-limited plateau, and computes the optimal batch size as ~300× sparsity (≈2,400 sequences for DeepSeek). It uses this to explain why batching improves efficiency by orders of magnitude and why fast-mode pricing exists.

The 노정석 "EP 96. LLM 추론 인프라와 토큰 경제학" analysis re-derives the same economics in `T_compute` versus `T_mem` terms — total generation time bounded by the *maximum* of compute time (active parameters × batch ÷ FLOPs) and memory time (total parameters + KV-cache access ÷ bandwidth) — and finds the optimal operating point where the two balance. It adds the generalizing observation that the FLOPs-to-bandwidth ratio is roughly constant across hardware generations (~300× for FP4), so optimal batch ≈ 300 ÷ sparsity (B ≈ 2,400 for 1/8 sparsity) at a ~20 ms drain time, directly translating sparsity into how many concurrent users a GPU can serve. It situates this inside the Blackwell-era hardware leap (`[[serving-parallelism]]`) and the serving-software stacks (vLLM/SGLang, `[[kv-cache-paging]]`) that realize the batching in practice.

## Tensions & Tradeoffs

- **Latency–cost–throughput trilemma**: small batches give low latency but ruinous cost-per-token; large batches are cheap per token but make any individual user wait longer for the batch to fill. There is no setting that optimizes all three, so providers segment it into pricing tiers — the technical substrate beneath `[[subscription-vs-metered-pricing]]`.
- **It is the cost floor under `[[token-maxing]]`**: the "tokens are cheap" stance holds only because batched serving amortizes weight fetches; the same tokens consumed at batch size 1 would be wildly expensive, so the economics depend on the provider's batching scale, not the operator's.
- **Couples tightly to architecture**: optimal batch size is a function of `[[mixture-of-experts]]` sparsity and of `[[kv-cache-economics]]` (the KV cache competes with weights for memory bandwidth), so batching cannot be tuned in isolation from the model's design — and realizing a large batch in practice depends on `[[kv-cache-paging]]` packing diverse caches into memory without fragmentation.
- **Hardware-bounded**: the floor it sets is per-configuration; changing the GPU, interconnect, or memory tier (`[[serving-parallelism]]`, `[[compute-memory-tradeoff]]`) moves the whole curve — though the ~300 FLOPs/bandwidth ratio staying constant across generations means the *batch-size rule* survives the hardware change even as the absolute throughput rises.
