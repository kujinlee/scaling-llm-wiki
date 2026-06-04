---
concept: Progressive Disclosure Retrieval
category: Memory & Knowledge Systems
summary: Structuring memory recall as an ordered escalation of increasingly expensive tiers — in-context check, hybrid search, expand, raw transcript — stopping as soon as a cheaper tier suffices.
aliases: [progressive disclosure retrieval, tiered memory retrieval, multi-tier recall, escalating retrieval, three-tier retrieval, cheapest-first recall]
related: ["[[persistent-agent-memory]]", "[[memory-storage-injection-recall]]", "[[llm-knowledge-wiki]]", "[[lazy-context-loading]]", "[[auto-correction-loop]]", "[[context-rot]]", "[[tool-integration-hierarchy]]"]
sources: [master-claude-memory-in-23-minutes]
---

# Progressive Disclosure Retrieval

Progressive disclosure retrieval is the technique of structuring an agent's memory recall as an ordered escalation of increasingly expensive tiers, stopping as soon as a cheaper tier returns enough context. Instead of always paying for the most thorough (and most token-intensive) retrieval, the system tries the cheapest source first — context already in the window — and only descends to semantic search, then context expansion, then full raw-transcript retrieval when the prior tier proves insufficient. It turns recall into a cost-disciplined cascade, spending retrieval budget only where the question actually demands it, the same "only pay when you must" economy seen in `[[lazy-context-loading]]` and the "success silent, failure loud" rule of the `[[auto-correction-loop]]`.

## Key Mechanics

- **Tier 0 — in-context check (zero cost)**: first search the curated memory files and recent daily logs *already loaded* in the conversation window. If the answer is present, retrieval is instant and free — no search at all.
- **Tier 1 — hybrid semantic + keyword search**: convert the query to a vector and search a vector store for matches by *meaning* (e.g. "monetization" matching "pricing"), combined with lexical keyword matching (BM25). This is the workhorse tier — relevance ranking over the full indexed history.
- **Tier 2 — expand**: if Tier 1's hits are insufficient, surface more surrounding context and metadata around the candidate matches, giving the agent enough to judge relevance without yet pulling everything.
- **Tier 3 — raw dialogue (last resort)**: retrieve the full raw session transcript behind the summarized bullets. This is the most token-expensive option and is reached only when the condensed tiers cannot answer.
- **Escalation is the whole point**: each tier is more thorough and more expensive than the last, so the cascade bounds average cost — most queries resolve at Tier 0 or 1, and the costly raw-transcript read is rare.

## How It Appears in the Corpus

The Simon Scrapes "Master Claude Memory in 23 Minutes" walkthrough presents Memarch's recall as exactly this three-tier system (search query → expand → raw dialogue) and frames it explicitly as "progressive disclosure." The recommended hybrid prepends a "Tier 0" zero-cost check of the `memory.md` and daily-log files already in context before falling through to Memarch's vector tiers, so recent curated facts are answered instantly and only deep history pays for semantic search. It is contrasted with Claude's default recall, which "trolls" through past conversations with no methodology — token-intensive and unstructured — the failure mode tiered retrieval is built to replace.

## Tensions & Tradeoffs

- **Retrieval quality still bounds every tier**: progressive disclosure controls *cost*, not *correctness* — if the embeddings or keyword index surface the wrong chunks at Tier 1, the cascade confidently feeds bad context, the same retrieval-quality bottleneck noted for `[[llm-knowledge-wiki]]` and `[[persistent-agent-memory]]`.
- **The escalation threshold is a judgment call**: deciding when a tier is "insufficient" and should escalate is itself a heuristic; too eager and it wastes the cheaper tiers' work, too reluctant and it answers from thin context — a tuning problem the pattern introduces.
- **Cost discipline as a sibling of other token-economy levers**: it trims tokens on *recall* the way `[[tool-integration-hierarchy]]` trims them on *plumbing* and `[[lazy-context-loading]]` trims them on *loading* — three levers on the same finite context budget, attacked from different sides.
- **Last-resort raw retrieval is still a backstop, not a guarantee**: pulling the full transcript recovers detail the summaries dropped, but only if the summarization preserved enough to know the transcript is relevant — so the quality of upstream storage (`[[memory-storage-injection-recall]]`) silently caps what the deepest tier can find.