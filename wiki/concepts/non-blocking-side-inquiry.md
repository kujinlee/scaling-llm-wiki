---
concept: Non-Blocking Side Inquiry
category: Agent Architecture & Patterns
summary: Posing a secondary question to an agent while it stays busy on a long-running primary task — getting an answer without interrupting the main operation or losing its context.
aliases: [non-blocking side inquiry, by the way, parallel inquiry, side-channel query, parallel task management, in-session side question, /btw, side session, side sub-session]
related: ["[[subagent-context-isolation]]", "[[parallel-isolated-agents]]", "[[context-compaction]]", "[[exploratory-spec-discovery]]", "[[context-reset]]", "[[session-context-forking]]"]
sources: [7-secret-prompts-that-make-claude-code-10x-better, live-코덱스로-바이브-코딩하기-feat-하네스-엔지니어링]
---

# Non-Blocking Side Inquiry

A non-blocking side inquiry is the ability to ask an agent a secondary question — or run a separate prompt — *while it is still working on a long-running primary task*, having it answer the aside without interrupting, derailing, or discarding the main operation. It preserves workflow continuity: instead of cancelling a lengthy job to ask something or spawning a whole new session and losing the thread, the operator interleaves a quick query into the same conversation and the agent handles both. The defining property is that the primary task's context survives the interruption intact.

## Key Mechanics

- **Aside without interruption**: a side-query trigger (the corpus's instances are a `/btw` / "by the way" command in Claude Code and a `side` sub-session in Codex) lets the operator inject a secondary question that the agent answers while its main, long-running task continues unaffected.
- **Context preservation**: the ongoing conversation's context is kept rather than reset, so the aside neither pollutes nor erases the primary task's state — the inverse of a deliberate `[[context-reset]]`, which is what you use when you *do* want the slate wiped.
- **Isolated side state**: in the Codex variant the aside runs in a *separate sub-session* so the side work is answered without writing into the main session's context at all — the question is handled adjacent to, rather than inside, the primary thread.
- **Parallel task management within one session**: it provides lightweight concurrency *inside* a single conversation, distinct from running separate sessions — the operator manages two threads of thought in one place.
- **Workflow continuity is the payoff**: the value is not raw parallelism but not having to choose between waiting out a long task and breaking it to handle a sudden question.

## How It Appears in the Corpus

The Sabrina Ramonov "7 Secret Prompts" tutorial presents a `/btw` ("by the way") command for asking a secondary question or running a separate prompt while the agent is busy with a main, long-running task — answering the aside without interrupting the primary operation and preserving the ongoing conversation's context, framed as parallel task management within a single session.

The 실밸개발자 live Codex CLI session corroborates the same pattern under a different name: its `side` feature lets the operator pose a question or run a task in a *separate sub-session* without affecting the main session's context, so a query can be answered mid-build without derailing the primary work. The two sources mark the pattern across both major coding agents — a `/btw` aside that stays in-thread (Claude Code) and a `side` sub-session that runs adjacent to the thread (Codex) — converging on the same goal of answering a side question without disturbing the long-running main task.

## Tensions & Tradeoffs

- **Distinct from `[[subagent-context-isolation]]` and `[[parallel-isolated-agents]]`**: those isolate work in *separate* contexts or sessions for hygiene and throughput; a non-blocking side inquiry deliberately keeps the aside connected to the live task to preserve continuity — opposite choices about where the side work lives. The Codex `side` sub-session sits between them: it isolates the aside's state while still being driven from the same live operation.
- **Same-window mixing risks dilution**: when the aside shares the primary task's context window (the in-thread `/btw` case), frequent or large side-queries reintroduce exactly the crowding that `[[context-compaction]]` and `[[context-reset]]` exist to relieve — the convenience of staying in one thread trades against context cleanliness, which the separate-sub-session variant sidesteps.
- **Distinct from `[[session-context-forking]]`**: a fork *branches the whole conversation* to preserve a state and revert; a side inquiry *answers an aside* without branching or reverting the main thread — one is reversibility insurance, the other is in-flight multitasking.
- **A focused instance of side-threading**: it is the productized form of the "side threads let the operator ask questions without derailing the main goal" capability noted for long autonomous runs in `[[exploratory-spec-discovery]]` — handy for quick asides, not a substitute for true isolation when the side work is substantial.
