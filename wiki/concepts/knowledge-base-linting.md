---
concept: Knowledge Base Linting
category: Memory & Knowledge Systems
summary: A periodic automated maintenance pass over an agent-maintained knowledge wiki that detects and removes contradictions, prunes staleness, flags gaps, and suggests new connections to keep the accumulated knowledge current and internally consistent.
aliases: [knowledge base linting, wiki lint, lint operation, knowledge linting, contradiction removal, knowledge integrity maintenance, wiki maintenance pass, gap detection, orphan page detection]
related: [llm-knowledge-wiki, ingest-vs-query-time-synthesis, memory-consolidation-dreaming, ai-garbage-collection, second-brain, custom-eval-systems, compound-engineering]
sources: [ai-를-위한-두-번째-뇌-세컨드-브레인-파헤치기-feat-메타-스태프-엔지니어, claude-karpathy-s-second-brain-is-insane, karpathy-s-llm-wiki-full-beginner-setup-guide]
---

# Knowledge Base Linting

Knowledge base linting is the periodic, automated maintenance operation that keeps an agent-maintained knowledge wiki internally consistent and current: a recurring pass inspects the accumulated pages, removes contradictions, updates stale knowledge, and — in its richer form — flags gaps and suggests new connections so the store does not silently rot as new material is ingested. It is the third of the three operations that constitute an LM-Wiki-style knowledge base — **Ingest** (absorb new material), **Query** (answer from it), and **Lint** (keep it healthy) — and it is the integrity counterpart to ingestion's accumulation: where ingest grows the wiki, lint guarantees that growth does not accrete conflicting or outdated claims.

## Key Mechanics

- **Scheduled, automatic inspection**: linting runs periodically over the whole knowledge base rather than on every write, examining pages for inconsistencies the way a code linter scans a codebase — a standing maintenance ritual, not a one-time cleanup.
- **Contradiction removal**: the pass surfaces and resolves claims that conflict across pages, so the wiki presents a coherent body of knowledge instead of mutually inconsistent fragments accumulated from different sources at different times.
- **Currency enforcement**: it updates or retires knowledge that has gone stale, keeping the store aligned with the most recent ingested material rather than letting old syntheses persist unchallenged.
- **Structural-integrity checks — orphan pages and unpaged concepts**: a richer lint pass audits the *graph structure* itself, flagging **orphan pages** (entries with no incoming or outgoing links, stranded from the rest of the wiki) and **unpaged concepts** (ideas referenced across the wiki but lacking their own page yet) — so the wiki stays navigable and connected rather than fragmenting into disconnected islands as it grows.
- **Gap detection and connection suggestion**: beyond pruning what is wrong, a richer lint pass identifies *missing* topics and under-linked pages, emitting warnings and actionable suggestions — close an information gap by adding an entry for an absent topic, or strengthen the graph by linking pages that should connect. Lint thus does double duty as health-check *and* growth-prompt, telling the operator not just what to fix but what to add next.
- **The third LM-Wiki operation**: it completes the Ingest → Query → Lint lifecycle of an agent-maintained `[[llm-knowledge-wiki]]`; ingestion and query alone would let the base drift, so lint is what makes long-lived agent curation viable.

## How It Appears in the Corpus

The 실밸개발자 ("Second Brain for AI") talk presents Lint as one of the three core architectural operations of an LM Wiki built for a `[[second-brain]]`: alongside Ingest (auto-generating a summary page and updating the index when new material like a YouTube link is added) and Query (answering from the processed pages), Lint is described as a process that periodically inspects the system to eliminate contradictions and keep the knowledge up to date. It is framed as essential to a knowledge base that the agent maintains itself, so the wiki stays trustworthy as it accumulates.

The Corey Ganim "Claude + Karpathy's Second Brain is INSANE" tutorial operationalizes Lint as a concrete `second brain lint` command that runs a comprehensive health check over the wiki: it identifies potential conflicts, flags outdated information, and — distinctively — highlights areas where more connections could be established, returning warnings plus actionable suggestions. The presenter then closes the loop by acting on those suggestions (adding entries for missing topics, refining existing ones) to strengthen the knowledge graph and shrink information gaps — making lint an iterative refinement step that both repairs and *grows* the base rather than only pruning it.

The Teacher's Tech "Karpathy's LLM Wiki — Full Beginner Setup Guide" tutorial reiterates Lint as the health-check operation of the three-layer LLM Wiki, and sharpens its *structural* scope: the agent can lint the wiki to check for contradictions, outdated claims, **orphan pages** (entries linked to nothing), and **unpaged concepts** (ideas referenced but without their own page). It frames this periodic review as what maintains the wiki's health and accuracy as it grows, while stressing that the AI can still make mistakes — so human review of the lint results remains essential, especially in the early stages.

## Tensions & Tradeoffs

- **The maintenance member of a family**: linting is the knowledge-wiki analogue of `[[memory-consolidation-dreaming]]` (which distills, fact-checks, and deduplicates an agent *memory* store) and of `[[ai-garbage-collection]]` (which prunes bad *code* patterns) — three instances of the same entropy-fighting discipline applied to different stores, all answering the recurring "accumulation rots without pruning" problem.
- **It is the direct mitigation for active misinformation**: because an ingest-time synthesized wiki can drift into confidently-wrong prose (`[[ingest-vs-query-time-synthesis]]`, `[[llm-knowledge-wiki]]`), a standing lint pass is what catches the contradiction or staleness before a reader trusts it — but only for the conflicts it is designed to detect.
- **Lint quality bounds integrity**: an automated pass removes exactly the inconsistencies its rules anticipate, so an unmodeled class of contradiction survives silently — the same "quality of the check bounds the trust" caveat that `[[custom-eval-systems]]` raises, here aimed at the knowledge base's internal consistency rather than at product output. The corpus is explicit that the linting agent can itself err, so human review of lint output remains necessary, especially before the base matures.
- **Suggestion is not curation**: gap-detection and connection-suggestion surface *candidate* work, but acting on every suggestion can bloat the wiki with marginal entries or force spurious links — the operator must still judge which suggested additions are worth making, so lint-as-growth-prompt presupposes the human curation it is meant to assist.
- **Aggressive linting can erase signal**: as with garbage collection, deciding what counts as a "contradiction" or "stale" entry is itself a judgment, so an over-eager pass risks deleting a deliberately retained nuance or a genuine competing perspective the wiki should keep.
