---
concept: Session Context Forking
category: Harness & Context Engineering
summary: Cloning an agent session's full conversation context into an independent branch so a valuable context state (e.g. the completed planning phase) is preserved and can be returned to, letting the operator explore forward with a fallback.
aliases: [session forking, context forking, session fork, fork, context branching, conversation branching, context insurance, branch-and-revert context, fork the session]
related: ["[[context-compaction]]", "[[context-reset]]", "[[agent-checkpoint-rollback]]", "[[non-blocking-side-inquiry]]", "[[subagent-context-isolation]]", "[[parallel-isolated-agents]]", "[[exploratory-spec-discovery]]", "[[structured-task-ledger]]"]
sources: [live-코덱스로-바이브-코딩하기-feat-하네스-엔지니어링]
---

# Session Context Forking

Session context forking is the technique of *cloning an agent session's entire conversation context* into an independent branch, so a hard-won context state — most usefully the completed planning/specification phase — is preserved intact and can be returned to if a later exploration goes wrong. Where a single linear session marches forward and overwrites its own state as it works, a fork captures a snapshot of the conversation *as it stands* and lets work continue on a copy, turning an irreversible chat history into a branchable one. Its defining role in the corpus is as *insurance*: the operator forks right after establishing the expensive shared context (problem definition, architecture, decisions) so that any subsequent implementation detour can be abandoned without re-deriving that foundation. It is the conversation-state counterpart to file-level rollback — where `[[agent-checkpoint-rollback]]` snapshots the *filesystem* before each edit, forking snapshots the *context window* before each risky direction.

## Key Mechanics

- **Clone the conversation, not the files**: a fork duplicates the current session's accumulated context — the planning discussion, the agreed architecture, the resolved decisions — into a separate branch, so the original state survives whatever the copy does next. The unit preserved is the *reasoning context*, not the code on disk.
- **Preserve the expensive planning phase**: the canonical use is to fork immediately after the costly up-front planning (PRD, architecture, decisions) is settled, because that shared context is exactly what is most painful to reconstruct — a fork makes it a durable checkpoint rather than something that erodes as the session fills with implementation detail.
- **Insurance and revert**: because the pre-fork state is kept, a forward exploration that turns out wrong is not a loss — the operator returns to the forked point and tries another direction, lowering the cost of an attempt the way `[[agent-checkpoint-rollback]]` does for edits.
- **Composes with context hygiene**: forking pairs with active context management (`[[context-compaction]]` to shrink a full window, `[[context-reset]]` to wipe an unrelated one) — the difference is that forking *keeps a copy of the discarded state* rather than condensing it or throwing it away, so it is the non-lossy branch where the others are lossy moves.

## How It Appears in the Corpus

The 실밸개발자 live coding session (Codex CLI with Harness) demonstrates `fork` as one of several advanced Codex features for productive AI development: it clones the current session's context to *preserve the important context of the planning stage* and act as an "insurance" that lets the developer return to an earlier state if needed. The session frames it alongside `compact`/`clear` (context-window management, keeping usage around 20–30%) and `side` (a non-blocking sub-session) as the toolkit for managing a long, context-heavy build — forking being the move that makes the up-front planning investment recoverable rather than fragile.

## Tensions & Tradeoffs

- **Distinct from `[[agent-checkpoint-rollback]]`**: that snapshots project *files* automatically before each edit and rewinds the filesystem; forking snapshots the *conversation context* on demand and rewinds the agent's reasoning state. They cover different recovery needs — a fork preserves *what the agent knows*, a checkpoint preserves *what the agent wrote* — and compose, since a reverted context still has to reckon with whatever files an abandoned branch already changed.
- **Distinct from `[[parallel-isolated-agents]]` and `[[subagent-context-isolation]]`**: those run *separate* sessions or sub-agents for throughput or context hygiene; a fork *duplicates one session's history* as a fallback, not to parallelize work. Forking is about reversibility of a single thread, not concurrency across many.
- **The non-lossy counterpart to `[[context-compaction]]` and `[[context-reset]]`**: compaction condenses the live history and a reset discards it; a fork keeps the full prior state on a branch — so forking trades the storage of a duplicated context for the ability to return to it exactly, where the others trade fidelity for a leaner window.
- **Forks multiply context to manage**: keeping branched copies of a session is more state for the operator to track and reason about — which branch holds which decisions — so heavy forking reintroduces a coordination burden, and a stale fork can preserve an *outdated* plan just as durably as a useful one.
- **A fork preserves context, not correctness**: returning to the forked planning state recovers the agreed foundation, but if that foundation was itself flawed, every branch built from it inherits the flaw — forking makes a starting point durable without certifying it was the right starting point.
- **Vantage caveat**: the feature and the "insurance" framing come from a single live tutorial demonstrating Codex CLI, so it illustrates the *pattern* — branching an agent's conversation context to preserve a valuable state — rather than a measured result; the durable idea is reversible, branchable session context, not one tool's `fork` command.
