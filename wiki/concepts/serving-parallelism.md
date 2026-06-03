---
concept: Serving Parallelism & Interconnect Topology
category: LLM Internals & Training
summary: Strategies for splitting large models across GPUs, where interconnect topology — fast intra-rack vs. slow inter-rack networks — is the binding constraint on expert-layer size.
aliases: [serving parallelism, model parallelism, expert parallelism, pipeline parallelism, rack boundaries, interconnect topology, scale-up vs scale-out, NVLink, NVL72, all-to-all communication, Blackwell]
related: [mixture-of-experts, inference-batching-economics, kv-cache-economics, kv-cache-paging, prefill-decode-inference, compute-memory-tradeoff]
sources: [how-gpt-claude-and-gemini-are-actually-trained-and-served-re, ep-96-llm-추론-인프라와-토큰-경제학]
---

# Serving Parallelism & Interconnect Topology

Serving parallelism is the set of strategies for splitting a model too large for one GPU across many — and the central, underappreciated fact is that *interconnect speed*, not raw GPU count, dictates how those splits can be drawn. Communication between GPUs falls into two sharply different regimes: fast, fully-connected "scale-up" networks *within* a rack (e.g. Nvidia NVLink) and much slower "scale-out" networks *between* racks (datacenter switches, often ~8× slower). Because of this gap, the physical rack boundary becomes a hard architectural constraint that bounds the size of a model's expert layers and shapes which parallelism strategy pays off.

## Key Mechanics

- **Expert parallelism**: different experts of a `[[mixture-of-experts]]` model are assigned to different GPUs, so each GPU stores only a subset. Routing tokens to their experts produces an **all-to-all communication pattern** across the cluster — every GPU may need to send tokens to every other.
- **Rack boundary as the limit**: GPUs inside one rack share the fast scale-up network; crossing racks drops onto the ~8× slower scale-out network. This makes a single rack effectively *bound the size of an expert layer*, a limit driven by physical realities — power, cooling, and the extreme density of cabling required for full connectivity.
- **Hardware chasing the boundary**: successive GPU generations involve increasingly elaborate rack designs specifically to overcome cabling limits and *expand the scale-up domain* — i.e. fit more GPUs inside the fast-interconnect island. The concrete current instance is Nvidia's **Blackwell** generation (GB200/GB300) with **NVL72** connectivity linking up to **72 GPUs in a single rack** over the fast scale-up fabric, each GPU carrying large HBM (cited at ~192–288 GB). This leap is what makes serving *giant* models tractable — discussion has moved from 1–2 T parameters a year or two ago to prospective 5 T and 10 T models — because more model fits inside one fast-interconnect domain at once.
- **Pipeline parallelism**: a different split — distributing successive model *layers* across racks. In inference it is largely **latency-neutral** (it does not speed up or slow down a single inference); its payoff is **memory-capacity saving**, since each rack stores only a fraction of the weights.
- **Why pipelining's value has faded for inference**: its memory saving is undercut by the `[[kv-cache-economics|KV cache]]`, whose per-GPU footprint stays constant regardless of pipeline depth, and by modern racks carrying enough HBM to hold trillion-parameter models outright — reducing the need to pipeline purely for weight storage.

## How It Appears in the Corpus

Reiner Pope's lecture (Dwarkesh Patel channel) devotes two segments to physical layout: it details expert parallelism and its all-to-all pattern, names the rack boundary (fast NVLink scale-up vs. ~8× slower scale-out) as what bounds expert-layer size under power/cooling/cabling constraints, cites Blackwell→Rubin rack redesigns aimed at enlarging the scale-up domain, and analyzes pipeline parallelism as latency-neutral-but-memory-saving — with that saving now diminished by constant KV-cache footprint and large modern HBM.

The 노정석 "EP 96. LLM 추론 인프라와 토큰 경제학" analysis grounds the same topology story in concrete current hardware: it emphasizes NVIDIA's Blackwell generation (GB200/GB300) with ~192–288 GB HBM per GPU and NVL72 connecting up to 72 GPUs in a single rack, and argues these leaps in memory and intra-rack connectivity are what enable the deployment of 5 T–10 T parameter models — a major jump from the 1 T–2 T scale of a year or two prior. It frames the hardware evolution as dictating "the very architecture and economic viability of modern LLMs," tying the scale-up domain directly to which models can be served at all.

## Tensions & Tradeoffs

- **Topology dictates architecture**: the model designer does not freely choose expert-layer size — the interconnect hierarchy does, so `[[mixture-of-experts]]` scaling is constrained by datacenter physics, not just algorithms.
- **Pipelining trades memory for compute**: distributing layers saves per-rack memory but requires multiple in-flight "micro-batches" to keep the pipeline full, spending compute to buy memory capacity — one instance of the universal `[[compute-memory-tradeoff]]`.
- **Diminishing returns for inference pipelining**: because the KV cache's footprint is invariant to pipeline depth and modern HBM is large, the classic reason to pipeline (fit the weights) is weakening — the binding memory cost is migrating from weights to the cache, where `[[kv-cache-paging]]` rather than pipelining is the lever.
- **Couples to batching**: all-to-all expert traffic and the cost of crossing rack boundaries feed back into the achievable batch size and thus the cost curve of `[[inference-batching-economics]]`.
- **Vendor-roadmap caveat**: the specific generation names and per-GPU HBM/connectivity figures (Blackwell GB200/GB300, NVL72, 192–288 GB, prospective 5–10 T models) are point-in-time hardware claims from product roadmaps, so the durable idea is *interconnect topology bounds model architecture*, not any single chip's numbers.
