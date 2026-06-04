---
concept: Context Compaction
category: Harness & Context Engineering
summary: Actively monitoring context-window consumption and compacting conversation history — summarizing to preserve key decisions while freeing space — so a long session does not hit the window's hard limit.
aliases: [compaction, context compaction, compact, conversation summarization, context window management, history compression]
related: [context-decay, context-rot, persistent-agent-memory, lifecycle-hooks, progressive-disclosure-retrieval, claude-md, tool-output-virtualization, context-reset]
sources: [12-claude-code-features-every-engineer-should-know-subagents, every-claude-code-memory-system-compared-so-you-don-t-have-t, claude-code-is-expensive-this-mcp-server-fixes-it-context-mo, live-코덱스로-바이브-코딩하기-feat-하네스-엔지니어링]
---

# Context Compaction

Context compaction is the active management of a finite context window during a long session: monitoring how much of the window has been consumed, then compacting the conversation history — summarizing accumulated turns to preserve the critical decisions while discarding the redundant detail — so space is freed before the window reaches capacity. Where `[[context-decay]]` names the *failure* of a long task crowding out earlier instructions, compaction is one of the active *remedies*: rather than re-grounding from a standing file, it condenses the live history in place so the session can continue without truncating.

## Key Mechanics

- **Monitor consumption**: a command (e.g. `/context`) reports token usage so the operator can see how close the conversation is to filling the window — making the otherwise invisible budget legible.
- **Compact the history**: a compaction step (e.g. `/compact`) summarizes the conversation so far, aiming to retain key decisions and state while dropping the verbose intermediate exchanges, recovering window space mid-session.
- **Preserve decisions, drop noise**: the design goal is selective — keep what future turns will need (commitments, conclusions, constraints) and shed what they will not (resolved tool chatter, superseded drafts).
- **Hookable at boundaries**: pre-compaction `[[lifecycle-hooks]]` let a system persist memory to disk *before* compaction runs, so durable facts survive the summarization into `[[persistent-agent-memory]]` rather than being lost with the discarded turns.
- **Re-inject a checkpoint after compaction**: a complementary pattern rebuilds a small *priority-tiered snapshot* at compaction time and injects it back into the window, so the post-compaction session resumes with the key state (recent edits, git operations, sub-agent tasks, and past errors/decisions) rather than a flattened summary — the survival mechanism that `[[tool-output-virtualization]]` adds on top of compaction.
- **`compact` vs `clear` as two distinct operations**: `compact` summarizes conversation history to recover window space while preserving key decisions — the right move mid-task when the window is filling; `clear` performs a full context reset, reclaiming the entire budget at the cost of all session state, appropriate when switching to an unrelated task (see `[[context-reset]]`). Both are active management moves that occupy opposite ends of the continuity-vs-budget tradeoff.
- **Target utilization heuristic**: keeping context usage in the 20–30% range — rather than waiting until near-full — is offered as an operational guide for proactive compaction, leaving a comfortable recovery window before pressure forces a rushed compact or the window truncates a task mid-execution.

## How It Appears in the Corpus

The ByteByteAI "12 Claude Code Features" overview describes Context Window Management — `/context` to monitor token consumption and `/compact` to manually compact the conversation history — as a way to preserve critical decisions while freeing space before the window reaches capacity, since Claude Code operates within a fixed context window. The Simon Scrapes memory-systems comparison uses *pre-compaction* hooks as one of the boundaries at which memory systems silently persist conversation state, so compaction does not erase facts that should endure.

The Better Stack "Claude Code is Expensive" tutorial treats compaction as the moment session continuity is most at risk and engineers around it: its "Context Mode" layer (`[[tool-output-virtualization]]`) uses hooks to track every file edit, git operation, and sub-agent task, and *when the context compacts* it automatically builds a priority-tiered snapshot (under ~2 KB) and re-injects it as a "save checkpoint" — also recording past errors and decisions so the agent does not repeat failed attempts even after a reset. It reframes compaction from pure loss into a checkpoint boundary that a snapshot can carry the agent across, claiming an extension of effective session time from ~30 minutes to ~3 hours.

The 실밸개발자 Korean Codex CLI tutorial operationalizes both `compact` and `clear` in a live session: a customized status line displays real-time token usage so the operator can see consumption at a glance, `compact` is invoked mid-session to compress history when the window fills while preserving planning context, and `clear` performs a full reset when switching to an unrelated task. The tutorial recommends actively targeting 20–30% context utilization as a practical working guide for when to compact proactively, making the invisible budget discipline explicit and visible.

## Tensions & Tradeoffs

- **Distinct remedy from re-grounding**: compaction attacks `[[context-decay]]` by *condensing the live history*, whereas an always-read `[[claude-md]]` attacks it by *re-injecting durable rules*; the two are complementary — compaction frees space, the grounding file restores constraints the summary may have flattened.
- **Lossy by construction**: summarizing turns can drop a detail a later step needed, so over-eager compaction trades window space for silent context loss — the same coverage risk that `[[progressive-disclosure-retrieval]]`'s raw-transcript tier and a re-injected snapshot exist to backstop.
- **In-session vs. across-session**: compaction manages one conversation's window, while `[[persistent-agent-memory]]` carries facts across sessions; compaction without a memory layer (or a pre-compaction hook) means anything summarized away is gone for good.
- **Manual vs. automatic timing**: deciding *when* to compact is a judgment call — too early wastes recoverable context, too late risks hitting the hard limit mid-task — the same escalation-threshold tuning problem seen in tiered retrieval. The 20–30% heuristic addresses this by making proactive compaction the default rather than a reactive measure.
