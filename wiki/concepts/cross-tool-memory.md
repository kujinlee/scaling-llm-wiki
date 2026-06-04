---
concept: Cross-Tool Memory
category: Memory & Knowledge Systems
summary: A single user-owned memory store shared across all AI tools via an MCP server, so context and facts follow the operator across assistants without vendor lock-in.
aliases: [universal AI memory, portable memory, cross-tool AI memory, user-owned memory, universal memory layer]
related: ["[[persistent-agent-memory]]", "[[llm-knowledge-wiki]]", "[[claude-md]]", "[[ingest-vs-query-time-synthesis]]"]
sources: [every-claude-code-memory-system-compared-so-you-don-t-have-t, karpathy-s-wiki-vs-open-brain-one-fails-when-you-need-it-mos]
---

# Cross-Tool Memory

Cross-tool memory is a single, user-owned memory store that every AI tool — coding agent, chat assistant, IDE, phone app — can read and write in real time, so context follows the user across tools instead of being siloed inside each one. The defining goals are portability (no lock-in to one assistant) and ownership (the data lives in infrastructure the user controls), achieved by centralizing memory in a shared database fronted by a universal query interface.

## Key Mechanics

- Central store: each "thought"/memory is a row holding text, an embedding vector, tags, and a timestamp, kept in a user-owned database (e.g. Postgres) rather than inside any one tool.
- Universal front door: an MCP server (optionally backed by serverless edge functions) exposes the store so any MCP-capable tool can query the same memory — the integration seam that makes the layer tool-agnostic.
- Ownership vs hosted split: a self-hosted build maximizes control, portability, and low running cost at the price of setup complexity, while managed alternatives are turnkey but keep the data on a vendor's servers.
- Raw-faithful storage: the store keeps raw facts (and unresolved contradictions) tagged and categorized at input rather than pre-synthesized, which is what lets the same data serve structured queries and many agents without forcing it into one narrative — the query-time side of `[[ingest-vs-query-time-synthesis]]`.

## How It Appears in the Corpus

The Simon Scrapes comparison's Level 6 presents Open Brain (by Nate Jones): a user-owned Postgres store (e.g. hosted on Supabase) where each thought is an embedded, tagged, timestamped row, queried through an MCP server wired to Supabase edge functions so Claude Code, ChatGPT, Cursor, and phone apps all share one memory in real time. Mem0 is cited as a production-ready, well-funded hosted alternative offering similar cross-tool memory but storing data on its own servers; the video favors Open Brain for ownership and portability despite its heavier setup.

The Nate B Jones ("AI News & Strategy Daily") comparison revisits Open Brain as the *query-time* counterpart to Karpathy's ingest-time wiki: it stores raw information faithfully and does its heavy synthesis only when a question is asked, reading the relevant rows on demand to produce a fresh, precise answer while preserving raw facts and contradictions. That faithful-raw-store property is what makes it scale to structured queries, high data volume, and multi-agent access where a single-narrative wiki would hit merge conflicts. The video then proposes a hybrid built on Open Brain's extensibility — the structured store stays the authoritative single source of truth while a scheduled compilation agent reads its graph and generates a browsable wiki layer on top — the synthesis-timing tradeoff resolved in `[[ingest-vs-query-time-synthesis]]`.

## Tensions & Tradeoffs

- Ownership vs convenience: self-hosting (Open Brain) maximizes control and portability but is more complex to stand up; hosted services (Mem0) are easier but cede data custody.
- Generality vs fit: a universal store shared across very different tools may not carry the tool-specific operational context that a tailored `[[claude-md]]` or a within-tool `[[persistent-agent-memory]]` tier provides.
- Raw integrity vs pre-built understanding: faithfully storing raw facts (and leaving contradictions unforced) is exactly what protects a query-time store from the "active misinformation" of a synthesized wiki, but it historically meant less pre-built synthesis depth, so deep understanding is re-derived per query — the synthesis-timing tradeoff of `[[ingest-vs-query-time-synthesis]]`, which the hybrid resolves by generating a wiki view over the store.
- Same retrieval caveat: a cross-tool store is still only as useful as its embeddings and tagging surface the right memories to each querying tool — the retrieval-quality bottleneck of `[[llm-knowledge-wiki]]` carries over.
