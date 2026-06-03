---
concept: Smart Truncation Memory
category: Harness & Context Engineering
summary: Truncating the middle of a large context entry while preserving its head and tail in the window and storing the full content in a retrievable memory store, so the agent keeps a usable handle and can pull back specifics on demand.
aliases: [smart truncation, smart truncation memory, boundary-preserving truncation, first-100-last-100, head-tail truncation, truncate-and-store, retrievable truncation]
related: [context-compaction, tool-output-virtualization, context-engineering, progressive-disclosure-retrieval, memory-storage-injection-recall, persistent-agent-memory, subagent-context-isolation, context-decay]
sources: [how-we-solved-context-management-in-agents-sally-ann-delucia]
---

# Smart Truncation Memory

Smart truncation memory is the technique of shrinking a large context entry by keeping only its *head and tail* in the active window — the corpus's instance is the first and last ~100 characters — truncating the verbose middle, while storing the *full* middle in an accessible memory store the agent can query when it actually needs the detail. It is the answer to a specific failure pair: naive truncation (just take the first 100 characters) makes the agent silently *forget* the discarded content, breaking its reasoning and its ability to handle follow-ups, while LLM summarization of the same content is inconsistent and gives the operator no control over which parts are deemed important. Smart truncation splits the difference — the head and tail preserve enough of a handle for the agent to recognize *what* the entry is and *that* more exists, and the stored middle preserves *everything* for retrieval — so the window stays lean without the data being lost. It is the entry-level counterpart to `[[tool-output-virtualization]]`: where that intercepts a whole tool output and returns only a reference, smart truncation keeps the boundaries inline and offloads only the middle.

## Key Mechanics

- **Two failed baselines motivate it**: *naive truncation* (keep the first N characters, drop the rest) loses information the agent later needs, producing broken reasoning and failed follow-ups; *summarization* (have an LLM condense the entry) is unreliable and cedes control over what survives. Smart truncation is the third option that keeps control and loses nothing recoverable.
- **Preserve the boundaries, offload the middle**: the head and tail of the entry stay in the window (the corpus cites first/last 100 characters) so the agent retains a recognizable, reasoning-usable fragment; the truncated middle is written to a memory store rather than discarded.
- **Retrieve on demand**: the agent pulls specific information back from the store when a task requires it — e.g. a particular tool call or an earlier message — so detail is fetched into the window only when needed, the same query-on-demand discipline as `[[progressive-disclosure-retrieval]]`.
- **Applied to accumulating tool/observability data**: the technique was built for an agent operating over large datasets (AI-observability traces / spans) whose context multiplies rapidly toward the token limit — exactly the runaway-growth case where in-window storage is unaffordable.
- **A heuristic, by the team's own admission**: "first 100, last 100" is an empirical rule of thumb, not a principled budget — and the corpus notes that even advanced models (Claude) employ similar truncation/compression strategies under the hood, so the pattern is industry-wide rather than bespoke.

## How It Appears in the Corpus

The Sally-Ann Delucia (Arize, "AI Engineer" channel) talk "How we solved Context Management in Agents" recounts a "vicious loop" in which Alex — an AI agent Arize used to build itself — kept failing as observability spans grew and hit the token limit. Naive truncation (first 100 characters) made the agent forget crucial information and break on follow-ups; LLM summarization was inconsistent and uncontrollable. The breakthrough was "Smart Truncation Memory": keep the first and last 100 characters of the context, truncate the middle, but store the full middle in an accessible memory store from which Alex retrieves specific tool calls or past messages when needed — giving more control and improving reasoning across the conversation. The talk frames the "first 100, last 100" split as a heuristic still under research and notes that even Claude uses comparable truncation/compression.

## Tensions & Tradeoffs

- **Distinct from `[[context-compaction]]` and summarization**: compaction (and LLM summarization) *condense* history into a shorter, lossy synthesis; smart truncation *preserves the full content verbatim* in a store and only hides the middle from the window — trading the summarizer's compression for exact recoverability, at the cost of keeping the bulk data around to be queried.
- **Distinct from `[[tool-output-virtualization]]`**: virtualization intercepts an entire tool output and returns a tiny reference, indexing the whole blob; smart truncation keeps the head and tail *inline* and offloads only the middle — a lighter, per-entry move that still leaves recognizable boundaries in the window rather than a bare handle.
- **Recoverability is bounded by retrieval**: the stored middle only helps if the agent's retrieval actually surfaces the relevant slice — a truncated-away detail that the store cannot return on query is effectively lost, the same "retrieval quality is the new bottleneck" caveat as `[[persistent-agent-memory]]` and the recall axis of `[[memory-storage-injection-recall]]`.
- **The boundary heuristic is unprincipled**: "first 100, last 100" assumes the important signal lives at the edges, which is not always true — the middle of a trace may hold the decisive value. The corpus names principled context budgeting and clear context-quality metrics as open research, so the heuristic is a working stopgap, not a solved design.
- **Storage substrate is required, not optional**: smart truncation presupposes a retrievable memory store behind the window (the storage axis of `[[memory-storage-injection-recall]]`), so it inherits that store's growth, indexing, and recall costs rather than eliminating them — it relocates the bulk data rather than removing it.
