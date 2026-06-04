---
concept: Disaggregated Inference
category: LLM Internals & Training
summary: Splitting the compute-bound prefill phase and the memory-bound decode phase of LLM inference onto separate, specialized hardware pools so each runs on the resource it is actually bottlenecked by — a serving architecture that raises token throughput.
aliases: [disaggregated inference, prefill-decode disaggregation, split prefill and decode, phase-disaggregated serving, memory wall, specialized inference hardware]
related: ["[[prefill-decode-inference]]", "[[inference-batching-economics]]", "[[serving-parallelism]]", "[[kv-cache-economics]]", "[[kv-cache-paging]]", "[[compute-memory-tradeoff]]", "[[mixture-of-experts]]"]
sources: [fast-models-need-slow-developers-sarah-chieng-cerebras]
---

# Disaggregated Inference

Disaggregated inference is the serving architecture of running the two stages of LLM inference — **prefill** and **decode** — on *separate, specialized hardware* rather than on one homogeneous pool, because the two stages are bottlenecked by opposite resources. Prefill processes the whole prompt in parallel and is *compute-bound*; decode generates tokens one at a time and is *memory-bandwidth-bound* (see `[[prefill-decode-inference]]`). Forcing both onto the same hardware means each stage spends part of its time starved of the resource it needs while idling on the one it does not. Disaggregation splits them so prefill runs where compute is abundant and decode runs where memory bandwidth is abundant, letting each operate near its own roofline — one of the optimizations behind the dramatic token-throughput gains of recent fast models. It is the serving-topology sibling of `[[serving-parallelism]]`: where that splits a model *spatially* across GPUs, disaggregation splits inference *by phase* across hardware tuned to each phase's bottleneck.

## Key Mechanics

- **The memory wall as the motivating problem**: a large share of inference latency (the corpus cites 50–80%) is *memory movement*, not computation — the "memory wall." Attacking it is what drives both novel hardware (bringing memory physically closer to the compute, e.g. on-chip SRAM on a wafer-scale chip) and the disaggregation strategy.
- **Prefill and decode have opposite bottlenecks**: prefill is parallel and compute-limited; decode is sequential and memory-bandwidth-limited. A single hardware configuration optimal for one is suboptimal for the other, so co-locating them wastes whichever resource is not binding at each moment.
- **Split the phases onto specialized hardware**: disaggregated inference routes prefill to compute-optimized hardware and decode to memory-bandwidth-optimized hardware, so each phase runs on the substrate matched to its constraint — a hardware-level realization of the per-phase scheduling that `[[prefill-decode-inference]]` describes providers doing.
- **Composes with the other speed levers**: disaggregation sits alongside architecture optimizations like `[[mixture-of-experts]]` (and expert pruning such as REAP, removing inactive experts to shrink the model) and serving optimizations like `[[kv-cache-economics|KV-cache]]` reuse (avoiding recomputation of attention) — together these stack across the inference stack to produce the ~20x speedups that motivate fast-model workflows.

## How It Appears in the Corpus

The Sarah Chieng (Cerebras, "AI Engineer" channel) talk "Fast Models Need Slow Developers" attributes the AI speed revolution to simultaneous optimizations across the inference stack. On hardware, it names the "memory wall" (memory movement as 50–80% of inference latency) and two responses: bringing memory closer to the chip (Cerebras's wafer with on-chip SRAM) and **disaggregated inference**, which splits the compute-bound, parallel prefill step and the memory-bound, sequential decode step onto specialized hardware for optimal performance. It situates this alongside Mixture-of-Experts (with REAP-style expert pruning) and KV-cache reuse as the combined drivers behind models like Codex Spark reaching ~1,200 tokens/second.

## Tensions & Tradeoffs

- **It is the hardware realization of the `[[prefill-decode-inference]]` split**: that page notes prefill (compute-bound) and decode (memory-bound) "resist a single optimal operating point" and are managed separately; disaggregation takes that to its physical conclusion by putting them on different machines — gaining per-phase efficiency at the cost of coordinating a handoff (the KV cache built in prefill must reach the decode hardware).
- **More moving parts in the serving stack**: separating phases adds inter-stage transfer and scheduling complexity, the same "orchestration layer as moat" engineering burden flagged for `[[kv-cache-paging]]` — the throughput gain is real but non-trivial to build, concentrating the advantage with operators who can.
- **It optimizes throughput, not the cost physics**: like paging, disaggregation makes better use of hardware but does not repeal the `[[compute-memory-tradeoff]]` — it places each phase where its binding resource is slack, rather than eliminating the bottleneck.
- **Vantage caveat**: the framing and the specific figures (50–80% memory-movement latency, ~1,200 tok/s, wafer-scale SRAM) come from a hardware-vendor talk, so disaggregated inference is presented as an exemplar of phase-specialized serving rather than independently measured — the durable idea is *splitting inference by phase onto hardware matched to each phase's bottleneck*, not any single vendor's implementation.
