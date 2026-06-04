---
concept: KV Cache Paging
category: LLM Internals & Training
summary: Managing the dynamically-sized per-request KV cache like operating-system virtual memory — allocating it in fixed-size pages (PagedAttention) so diverse concurrent sequences pack into GPU memory with minimal fragmentation, maximizing batch size and utilization.
aliases: [PagedAttention, KV cache paging, vLLM PagedAttention, paged attention, kv cache memory management, kv cache fragmentation, serving orchestration layer]
related: ["[[kv-cache-economics]]", "[[prefill-decode-inference]]", "[[inference-batching-economics]]", "[[compute-memory-tradeoff]]", "[[serving-parallelism]]", "[[mixture-of-experts]]"]
sources: [ep-96-llm-추론-인프라와-토큰-경제학]
---

# KV Cache Paging

KV cache paging is the technique of managing each request's attention Key/Value cache the way an operating system manages virtual memory — allocating it in small fixed-size *pages* rather than as one contiguous block — so that many concurrent user sequences of wildly different lengths pack into GPU memory with minimal waste. The canonical implementation is vLLM's **PagedAttention**. The problem it solves is that the `[[kv-cache-economics|KV cache]]` for each user grows unpredictably (short prompts, long prompts, short and long generations), and naive contiguous allocation forces the system to reserve worst-case space per request, fragmenting GPU memory and leaving expensive HBM idle. By paging the cache, the serving system reclaims that wasted space, fits more sequences into memory at once, and thereby raises the achievable batch size — which is the dominant cost lever of `[[inference-batching-economics]]`. It is the serving-software counterpart to the hardware story: where bigger HBM and faster interconnect (`[[serving-parallelism]]`) raise the memory ceiling, paging makes better use of the ceiling that exists.

## Key Mechanics

- **Virtual-memory analogy**: the KV cache is split into fixed-size pages that need not be physically contiguous, so a sequence's cache can grow page-by-page on demand — exactly how an OS grows a process's memory — instead of pre-reserving a contiguous worst-case region.
- **Handles dynamic, diverse cache lengths**: because real traffic mixes short and long requests whose caches grow at different rates during `[[prefill-decode-inference|decode]]`, paging lets the system allocate only the pages each sequence actually uses, eliminating the internal fragmentation contiguous allocation creates.
- **More packing → bigger batches → lower cost-per-token**: reclaimed memory means more concurrent sequences share each weight fetch, pushing the system toward the high-batch regime where `[[inference-batching-economics]]` makes per-token cost collapse — paging is how the *memory* side of the roofline stops bottlenecking the *batch* the compute side could otherwise serve.
- **Orchestration layer as a frontier-lab moat**: efficient serving stacks (the source cites vLLM and SGLang) that manage paging, scheduling, and request routing are framed as critical competitive "moats" — they let a provider maximize GPU utilization across diverse requests and undercut rivals on price, so serving software, not just the model, is a source of advantage.

## How It Appears in the Corpus

The 노정석 "EP 96. LLM 추론 인프라와 토큰 경제학" analysis (on Dwarkesh Patel's lecture with Reiner Pope) highlights the KV cache as a major memory consumer and singles out vLLM's PagedAttention for managing the diverse, dynamic lengths of user-specific KV caches efficiently — reducing memory waste and maximizing GPU utilization. It frames efficient orchestration layers like vLLM and SGLang as critical infrastructure "moats" for frontier labs, enabling them to handle heterogeneous user requests, maximize utilization, and offer competitive pricing.

## Tensions & Tradeoffs

- **It optimizes memory use, not the underlying cost physics**: paging packs more sequences into existing HBM but does not change the fundamental `[[compute-memory-tradeoff]]` — once memory is full, the only further levers are more hardware or a smaller cache, so paging raises utilization toward the ceiling rather than removing it.
- **Software complexity as the price of utilization**: a paged cache plus the scheduler that drives it is real systems engineering, which is precisely why the corpus treats the orchestration layer as a moat — the gain is non-trivial to build, so it concentrates with the labs that can.
- **Couples to architecture**: how much paging helps depends on the cache size per token and on `[[mixture-of-experts]]` sparsity and context-length distribution, so it cannot be tuned in isolation from the model and the traffic it serves.
- **Vantage caveat**: the framing comes from a third-party analysis citing specific serving stacks, so PagedAttention is presented as the exemplar of the pattern (paging the KV cache) rather than the only valid implementation — the durable idea is *paged KV-cache management*, not one library.
