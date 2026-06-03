---
concept: KV Cache Economics
category: LLM Internals & Training
summary: How the attention KV cache's growing memory footprint shapes serving cost, and how published API pricing tiers can be reverse-engineered to reveal a provider's underlying hardware.
aliases: [KV cache, kv cache economics, prefill vs decode, context-length pricing, memory tiers, API pricing as architecture signal, cache hit vs miss pricing]
related: [inference-batching-economics, kv-cache-paging, prefill-decode-inference, serving-parallelism, compute-memory-tradeoff, subscription-vs-metered-pricing, per-node-model-routing, token-maxing]
sources: [how-gpt-claude-and-gemini-are-actually-trained-and-served-re, ep-96-llm-추론-인프라와-토큰-경제학]
---

# KV Cache Economics

KV cache economics is the study of how the memory used to store an LLM's attention key/value cache shapes serving cost — and the striking insight that publicly posted **API pricing can be reverse-engineered to expose a provider's underlying hardware**. The KV cache holds the per-token attention state so the model need not recompute it for every new token, but that state must be stored in (and streamed from) memory, and its footprint grows with both context length and batch size. Because providers price context length, input vs. output tokens, and cache retention differently, the pricing table becomes a window onto KV-cache size, memory-bandwidth limits, and even the storage media the cache spills onto.

## Key Mechanics

- **The cache is built in prefill, consumed in decode**: the KV cache is produced when the prompt is processed in parallel (`[[prefill-decode-inference|prefill]]`) and then reused as each output token is generated one at a time (`[[prefill-decode-inference|decode]]`), so its size and the cost of streaming it are inseparable from the two-stage inference structure.
- **Context-length tiers reveal KV-cache cost**: when pricing jumps at a context threshold (the source cites a model ~50% more expensive beyond 200K tokens), it signals that past that length the *memory cost of the KV cache* begins to dominate the compute cost. The crossover point implies a plausible **~2 KB per token** of KV-cache storage.
- **Prefill vs. decode asymmetry**: output (decode) tokens often cost 3–5× more than input (prefill) tokens. This implies decode is **memory-bandwidth-limited** (one token at a time, dominated by streaming weights + cache) while prefill is **compute-limited** (a whole prompt processed in parallel, saturating FLOPs) — the same roofline split as `[[inference-batching-economics]]`.
- **Cache hit vs. miss and retention tiers expose storage media**: differential pricing for cached-context hits vs. misses, and different retention windows (e.g. 5 minutes vs. 1 hour), let one *deduce the memory tiers* a provider uses. The retention "drain times" (capacity ÷ bandwidth) align with the characteristics of flash storage and even spinning disk — implying the KV cache is tiered down to cheaper, slower media as it ages.
- **The cache competes with weights**: KV-cache bytes share memory bandwidth with weight fetches, so a large cache eats into the batching headroom that amortizes weights — coupling cache size directly to the cost curve, and making efficient cache packing (`[[kv-cache-paging]]`) a direct lever on serving cost.

## How It Appears in the Corpus

Reiner Pope's lecture (Dwarkesh Patel channel) closes its applied section by decoding real LLM API pricing: context-length tiers (Gemini cited ~50% pricier over 200K tokens) imply ~2 KB/token KV cache; the 3–5× output-over-input gap implies memory-bandwidth-limited decode vs. compute-limited prefill; and cache hit/miss pricing with 5-minute vs. 1-hour retention implies a memory hierarchy descending to flash and spinning disk, with drain times matching the observed durations.

The 노정석 "EP 96. LLM 추론 인프라와 토큰 경제학" analysis corroborates the pricing-as-architecture reading and grounds it in the cache's mechanics: it identifies the KV cache (storing K and V for all prior tokens) as a major memory consumer, explains the prefill/decode structure behind the input-vs-output price gap, and attributes context-length tiers (e.g. below vs. above 200K tokens) and cache-duration tiers (5 minutes vs. 1 hour) directly to the underlying `T_compute`/`T_mem` dynamics — short-context workloads allowing higher concurrency and lower cost, long-context coding tasks demanding more resources and costing more. It adds that vLLM's PagedAttention (`[[kv-cache-paging]]`) is what manages the diverse, dynamic per-user cache lengths efficiently so this memory cost does not balloon through fragmentation.

## Tensions & Tradeoffs

- **Cache is the store side of a `[[compute-memory-tradeoff]]`**: the KV cache spends memory to avoid recomputing attention — the mirror of recomputation strategies that spend compute to avoid storing. Which wins depends on the relative price of memory bandwidth vs. FLOPs at a given context length.
- **It is the long-context cost driver**: because cache footprint grows with context length while compute does not as steeply, very long contexts are bounded by *memory*, not reasoning — the technical reason long-context tiers exist in `[[subscription-vs-metered-pricing]]`.
- **Erodes pipeline parallelism's payoff**: the cache's per-GPU footprint is invariant to pipeline depth, which is precisely why distributing layers for memory saving has diminishing returns (`[[serving-parallelism]]`).
- **Pricing as a leaky abstraction**: the fact that hardware tiers can be inferred from a price sheet means providers' cost structure is partly observable — useful for operators choosing models or building a `[[model-abstraction-layer|provider-agnostic seam]]`, though the inferences are estimates, not disclosed specs.
