---
concept: Memory Storage, Injection & Recall
category: Memory & Knowledge Systems
summary: The three axes every agent-memory system must design explicitly: how information is saved, how it is brought back into the active context window, and how past facts are retrieved on demand.
aliases: [three pillars of LLM memory, storage injection recall, memory system pillars, memory architecture pillars, three questions of agent memory]
related: ["[[persistent-agent-memory]]", "[[progressive-disclosure-retrieval]]", "[[claude-md]]", "[[llm-knowledge-wiki]]", "[[lifecycle-hooks]]", "[[context-rot]]", "[[ingest-vs-query-time-synthesis]]", "[[cross-tool-memory]]"]
sources: [master-claude-memory-in-23-minutes]
---

# Memory Storage, Injection & Recall

Memory storage, injection, and recall are the three questions every agent-memory system must answer, and decomposing a memory architecture along these axes is a durable framework for designing and comparing such systems. **Storage** is how and when information is saved — from a critical decision to routine conversational context. **Injection** is how saved information is brought back into the LLM's active context window leanly and at the right time. **Recall** is how past information — recent or months old — is efficiently found and retrieved on demand. A system can be strong on one pillar and weak on another, so the framework's value is that it forces each axis to be designed deliberately rather than collapsing all of memory into a single undifferentiated store.

## Key Mechanics

- **Storage — complete-capture vs. curated-save**: two opposite strategies. *Complete capture* saves everything (e.g. a stop hook summarizing every conversation turn with a cheap fast model into date-stamped markdown treated as the source of truth, then vectorized into a rebuildable index) and prioritizes coverage. *Curated save* has the agent decide what is "memory worthy" via explicit add/replace/remove tools under character caps, prioritizing leanness. The two are complementary, not exclusive — the recommended design runs both.
- **Injection — the frozen snapshot**: rather than injecting whatever is convenient, a rich but bounded bundle of key context (project file, consolidated facts, user profile, persona) is loaded and *cached per session* as a "frozen snapshot" — a few thousand tokens that ground the session, with any updates written to disk and loaded only in the *next* session. Injection is about feeding the *right* context at the *right time*, not loading more.
- **Recall — tiered escalation**: retrieval is layered cheapest-first — check context already in the window, then hybrid keyword + semantic search, then expansion, then raw dialogue as a last resort — the `[[progressive-disclosure-retrieval]]` pattern, so token-expensive retrieval fires only when cheaper tiers fail.
- **The pillars trade off independently**: a system optimized for complete storage and deep recall (Memarch) may have *no* dedicated injection layer, while a system optimized for curated injection (Hermes) may lack semantic recall — the framework exposes exactly these gaps so a hybrid can cover all three.

## How It Appears in the Corpus

The Simon Scrapes "Master Claude Memory in 23 Minutes" walkthrough builds its entire analysis on these three pillars, arguing that Claude Code's default memory is outmatched on each by open-source systems. It evaluates Memarch and Hermes pillar by pillar — Memarch excels at storage (capturing every turn) and recall (a three-tier search) but has no injection layer and leans on Claude's defaults; Hermes excels at injection (a cached ~1,300-token frozen snapshot of `claude.md`/`memory.md`/`user.md`/`soul.md`) and fast in-context lookup but lacks semantic search — and recommends a hybrid that takes the best of each axis. The same framing recurs across the broader memory corpus, where `[[persistent-agent-memory]]` is the tiered architecture that operationalizes all three.

## Tensions & Tradeoffs

- **Coverage vs. cost on every axis**: complete storage maximizes what *can* be recalled but spends indexing tokens and risks burying signal in noise; curated storage stays lean but depends on the agent correctly judging relevance — the same coverage gap noted for `[[context-rot]]`. The framework names the tradeoff per pillar rather than resolving it.
- **Injection competes with the very file that grounds the session**: a richer frozen snapshot improves grounding but enlarges standing context, re-raising the `[[context-rot]]` dilution risk that bounds `[[claude-md]]` — so the snapshot must be consolidated, not exhaustive.
- **It is the operational decomposition of memory, distinct from the synthesis-timing question**: where `[[ingest-vs-query-time-synthesis]]` asks *when* the hard thinking happens, this framework asks *how* facts are saved, re-injected, and found — orthogonal axes that compose (a query-time store still needs a recall strategy and an injection layer).
- **No single system wins all three**: the empirical finding of the corpus is that real systems are strong on some pillars and weak on others, so the practical recommendation is always a hybrid — which adds the most infrastructure (a stop hook, a nightly consolidation job, a vector store, and snapshot injection logic all at once).