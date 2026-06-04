---
concept: Prefill and Decode
category: LLM Internals & Training
summary: The two-stage structure of Transformer inference — a parallel prefill pass that processes the whole prompt and builds the KV cache, then a sequential decode pass that generates tokens one at a time reusing it — with opposite compute/memory bottlenecks.
aliases: [prefill, decode, prefill and decode, prefill vs decode, two-stage inference, prefill-decode, prompt processing vs token generation, inference stages]
related: ["[[kv-cache-economics]]", "[[kv-cache-paging]]", "[[inference-batching-economics]]", "[[compute-memory-tradeoff]]", "[[serving-parallelism]]", "[[tokens-to-think]]", "[[next-token-prediction]]"]
sources: [ep-96-llm-추론-인프라와-토큰-경제학]
---

# Prefill and Decode

Prefill and decode are the two distinct stages every Transformer inference passes through, and they have *opposite* performance characteristics — which is why understanding them is the key to LLM serving economics. **Prefill** processes the entire input prompt at once: because all prompt tokens are known up front, they are pushed through the model *in parallel* in a single pass that computes and stores the attention Key/Value (KV) representations for every token — the initial `[[kv-cache-economics|KV cache]]`. **Decode** then generates the output one token at a time: each new token is produced from only the *last* token as input, reusing the pre-computed KV cache instead of recomputing attention over the whole sequence. The split matters because prefill is *compute-bound* (a large batch of tokens saturating the GPU's FLOPs) while decode is *memory-bandwidth-bound* (one token per step, dominated by streaming weights and the growing cache out of memory) — the same roofline two-sidedness that governs `[[inference-batching-economics]]`.

## Key Mechanics

- **Prefill — parallel prompt ingestion**: a long input (the source's example is 1,000 lines of code) has all its tokens processed simultaneously in one forward pass, producing the KV cache that the rest of the generation will reuse. Because many tokens are computed at once, prefill saturates the GPU's compute units and is *compute-limited*.
- **Decode — sequential token generation**: output tokens are emitted one by one, each conditioned on the accumulated KV cache plus the single previous token, so each step does little compute but must stream the full weights and cache from memory — making decode *memory-bandwidth-limited*.
- **The KV cache is the bridge between the stages**: prefill *builds* it, decode *consumes and extends* it; this reuse is exactly what avoids recomputing attention over all prior tokens at every step — a store-to-save-compute instance of the `[[compute-memory-tradeoff]]`.
- **Opposite bottlenecks, one pipeline**: because prefill is compute-bound and decode is memory-bound, a serving system that optimizes one can starve the other, so providers schedule and batch the two phases differently rather than treating inference as one homogeneous workload.
- **Why inference now dominates**: long contexts and agentic "reasoning token" workloads (Claude Code, GPT-5.5-class tools) inflate both the prefill cost (huge prompts) and the decode cost (long generations over a growing cache), which is why the corpus frames efficient inference as having overtaken training in practical importance.

## How It Appears in the Corpus

The 노정석 "EP 96. LLM 추론 인프라와 토큰 경제학" analysis (built on Dwarkesh Patel's lecture with Reiner Pope) devotes a section to demystifying Transformer inference as prefill (a long prompt processed in parallel to generate the initial KV cache) versus decode (subsequent tokens generated one by one, with only the last token as input, leveraging the pre-computed cache). It frames this split as the foundation for the economics that follow — `T_compute` versus `T_mem` roofline analysis, optimal batch size, and the per-token pricing structure — and motivates the whole discussion with the claim that inference has surpassed training in importance as context lengths and agentic workloads explode.

## Tensions & Tradeoffs

- **The KV cache is the cost that grows with the conversation**: decode reuses the cache to save compute, but the cache's memory footprint grows with every generated token and with context length, so the memory saving of caching turns into the dominant *memory* cost of long-context serving — the driver behind `[[kv-cache-economics]]`'s context-length pricing tiers.
- **Prefill compute vs. decode memory pull in opposite directions**: a batch tuned to amortize decode's weight fetch (`[[inference-batching-economics]]`) may not be the batch that best saturates prefill's compute, so the two phases resist a single optimal operating point and are managed separately.
- **Decode's per-token limit is the same one `[[tokens-to-think]]` describes**: sequential token-by-token generation is exactly why spreading reasoning across many output tokens is costly — each decode step pays the memory-bandwidth toll, so long reasoning chains are expensive at the infrastructure layer, not just the API price.
- **Vantage caveat**: the framing comes from a third-party analysis of a single lecture, so the prefill/decode split is presented as the canonical mental model rather than an independently measured result — though it is the standard industry decomposition.
