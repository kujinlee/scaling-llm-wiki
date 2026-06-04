---
concept: Compute-Memory Tradeoff
category: LLM Internals & Training
summary: The recurring lever in LLM systems: nearly any memory pressure can be relieved by spending more compute, and vice versa — the art is placing each trade where the cheaper resource is slack.
aliases: [compute vs memory tradeoff, recompute vs store, rematerialization, RevNets, reversible networks, memory for compute, activation checkpointing, Feistel network]
related: ["[[kv-cache-economics]]", "[[serving-parallelism]]", "[[mixture-of-experts]]", "[[inference-batching-economics]]"]
sources: [how-gpt-claude-and-gemini-are-actually-trained-and-served-re]
---

# Compute-Memory Tradeoff

The compute-memory tradeoff is the recurring lever throughout LLM systems design: almost any memory pressure can be relieved by spending more compute, and almost any compute pressure by spending more memory, so engineering a serving or training stack is largely a series of choices about *which resource to trade for the other* at each point. Caching (the KV cache, pipeline weight storage) spends memory to avoid recomputation; rematerialization (recomputing activations, reversible networks) spends compute to avoid storage. The art is placing each trade where the cheaper resource absorbs the cost.

## Key Mechanics

- **The two directions**: *store-to-save-compute* — keep a result in memory so you never recompute it (the `[[kv-cache-economics|KV cache]]` is the canonical case). *Recompute-to-save-memory* — discard a result and regenerate it on demand, paying compute to free memory.
- **Pipelining as a trade**: distributing layers across racks (`[[serving-parallelism]]`) saves per-rack memory but requires multiple in-flight micro-batches, so it spends compute/coordination to buy memory capacity.
- **Reversible Networks (RevNets)** — the training-side instance: the **Feistel network**, a cryptographic construction that makes a non-invertible function invertible, was transferred into neural nets as RevNets. Making the network invertible lets the backward pass **rematerialize activations** rather than store them, *eliminating the single largest memory footprint of training* at the cost of extra compute to recompute those activations.
- **Crypto/NN parallel**: both fields "jumble" information across inputs — cryptography to make structure indistinguishable from randomness (the avalanche effect), neural nets to extract structure from complex inputs. They diverge on **differentiability**: NNs are built to be differentiable for gradient descent, whereas differential cryptanalysis is an *attack* on ciphers — yet the Feistel construction crossed over regardless.

## How It Appears in the Corpus

Reiner Pope's lecture (Dwarkesh Patel channel) surfaces the tradeoff repeatedly — pipelining (memory for compute), caching (memory to avoid recompute) — and devotes a tangential segment to the cryptography↔neural-network connection, explaining how the Feistel network's invertibility construction became RevNets, which rematerialize activations on the backward pass to remove training's largest memory footprint in exchange for more compute.

## Tensions & Tradeoffs

- **No free lunch, only a choice of currency**: every memory saving has a compute price and vice versa; the decision is purely economic — which resource is the binding constraint and which is slack — so the "right" trade flips with hardware (HBM capacity, FLOPs, interconnect).
- **Memory is increasingly the scarce side**: with modern racks holding trillion-parameter models in HBM, the pressure has shifted from storing *weights* to storing the *KV cache* (`[[kv-cache-economics]]`), changing which trades are worth making for inference.
- **Rematerialization's cost is latency/throughput**: RevNets free memory but add backward-pass compute, acceptable in training (throughput-bound, batch-amortized) but rarely worth it where latency dominates — the trade is context-specific, not universally good.
- **Cross-domain idea transfer**: the Feistel→RevNet path shows constructions migrate between fields with opposite goals (security vs. learning), a reminder that architectural ideas are often borrowed rather than invented in place.