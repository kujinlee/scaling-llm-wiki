---
concept: Filesystem Memory Store
category: Memory & Knowledge Systems
summary: A persistent, file-system-like storage attached as a resource to ephemeral agent sessions and mounted so the agent reads, writes, and searches it with shell tools (bash, grep) across sessions.
aliases: [memory store, filesystem memory store, mounted memory store, memory store resource, per-user memory store, per-workspace memory store, file-system agent memory]
related: [persistent-agent-memory, memory-consolidation-dreaming, memory-storage-injection-recall, agentic-search, low-floor-high-ceiling-tooling, llm-knowledge-wiki, cross-tool-memory, agent-as-infrastructure]
sources: [agents-that-remember]
---

# Filesystem Memory Store

A filesystem memory store is a persistent, file-system-like storage that is attached as a *resource* to an agent's otherwise ephemeral sessions, so the agent can read and write information that survives across them. Where a session is an isolated, throwaway conversation, the memory store is durable infrastructure mounted alongside it — and crucially it is exposed not as an opaque database but as a *file system the agent navigates with ordinary shell tools*, exploring with `bash` and searching with `grep`. It is the concrete substrate that turns isolated agents into agents with long-term memory, and the storage layer beneath the tiered-file designs of `[[persistent-agent-memory]]`.

## Key Mechanics

- **Persistent resource over ephemeral sessions**: the store is attached to sessions rather than living inside one, so anything written in one session is available in the next — the cross-session continuity an isolated session cannot provide on its own.
- **Filesystem interface, driven by shell tools**: the store is mounted as a file-system interface, so the agent uses general-purpose shell capability — `bash` to explore the directory tree, `grep` to search contents, file reads/writes to persist facts — rather than a bespoke memory API. This is the high-ceiling `[[low-floor-high-ceiling-tooling|shell-tool]]` approach applied to memory.
- **Per-user / per-workspace scoping**: stores can be configured at different granularities (one per user, one per workspace), so memory is partitioned to the right boundary instead of being a single global blob.
- **Composable layer**: the store is one layer in a stack — ephemeral *session* + persistent *memory store* + background `[[memory-consolidation-dreaming|dreaming]]` — each added independently to build a robust long-term memory system.
- **Read/write loop demonstrated**: the agent writes what it learns to the store in one session and successfully recalls it in a later, separate session, closing the isolation gap the pattern exists to solve.

## How It Appears in the Corpus

The Anthropic "Agents that remember" (Claude channel) workshop motivates the store with the failure of isolated agents — on platforms like Cloud Managed Agents, individual sessions do not retain what was learned in a prior session, so an agent cannot recall information it was just told. It introduces the memory store as a persistent, file-system-like resource attached to sessions, mounted so the agent uses `bash` and `grep` to explore and search, configurable per-user or per-workspace, and walks through creating a store, attaching it, and watching an agent recall earlier-session information through it.

## Tensions & Tradeoffs

- **Unbounded growth and disorganization**: because the agent writes freely to the store, it grows without bound and drifts into disorder, degrading retrieval efficiency and the agent's intelligence — exactly the entropy the `[[memory-consolidation-dreaming]]` process exists to clean up, the same accumulation-vs-pruning tension named in `[[persistent-agent-memory]]` and `[[ai-garbage-collection]]`.
- **Literal search vs. semantic retrieval**: a `grep`-over-files interface is fast and shell-native but matches literal strings, not meaning — the very inefficiency that `[[llm-knowledge-wiki]]` and `[[agentic-search]]` were built to address, so a large store may need a semantic index layered on top to surface the *relevant* memory rather than the lexically matching one.
- **Storage substrate, not the whole system**: the store answers *where memory lives* but not *how it is injected or recalled* — the other two axes of `[[memory-storage-injection-recall]]`; a filesystem alone does not decide which slice re-enters the context window.
- **An operational surface to scope**: a persistent, agent-writable filesystem attached to sessions is infrastructure to secure and partition (the per-user/per-workspace scoping is the first lever), the same operational-surface concern as `[[agent-as-infrastructure]]`, and the ownership/portability question `[[cross-tool-memory]]` raises applies to whose infrastructure the store sits on.