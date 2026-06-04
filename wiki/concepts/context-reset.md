---
concept: Context Reset
category: Harness & Context Engineering
summary: Deliberately wiping a session's conversation history when switching to an unrelated task — preventing accuracy degradation from stale context and reclaiming the token budget.
aliases: [context reset, clear context, conversation reset, context wipe, fresh context, clear between tasks, /clear]
related: ["[[context-compaction]]", "[[context-rot]]", "[[context-decay]]", "[[subagent-context-isolation]]", "[[persistent-agent-memory]]", "[[reasoning-effort-control]]"]
sources: [7-secret-prompts-that-make-claude-code-10x-better]
---

# Context Reset

Context reset is the practice of deliberately discarding a session's accumulated conversation history when moving from one distinct task to another, so the agent starts the next task on a clean window. Its dual purpose is accuracy and economy: irrelevant prior turns both *degrade* the model's performance (it processes stale, off-topic material as if it were relevant) and *cost* tokens (every retained turn is re-read on each prompt). Resetting between unrelated tasks removes both burdens at once. It is the blunt counterpart to `[[context-compaction]]`: where compaction *condenses* the history to preserve key decisions while freeing space, a reset *throws the history away* entirely — appropriate precisely when nothing in it is worth carrying forward.

## Key Mechanics

- **Full discard, not summarization**: a reset command (the corpus's instance is `/clear`) deletes all prior conversation history rather than summarizing it, returning the window to empty — the right move only when the next task shares no useful context with the last.
- **Two payoffs**: it prevents the accuracy degradation that creeps in when an overloaded or off-topic context dilutes the relevant signal, and it saves tokens by ensuring the model does not re-process irrelevant history on the new task.
- **Task-boundary trigger**: the discipline is to reset *when switching between distinct tasks*, making the task boundary the natural place to clear — analogous to how `[[subagent-context-isolation]]` keeps unrelated work out of the main thread, but applied temporally to one session rather than by delegation.
- **Targets both finite-window failure modes at the boundary**: by emptying the window it pre-empts `[[context-rot]]` (dilution by volume) and `[[context-decay]]` (loss over length) for the *next* task, trading away all continuity for a maximally clean slate.

## How It Appears in the Corpus

The Sabrina Ramonov "7 Secret Prompts" tutorial presents `/clear` as a context-reset command that deletes all previous conversation history, recommended explicitly when switching between distinct tasks — framed as serving two ends at once: preventing AI accuracy degradation from excessive context and saving tokens by not re-processing irrelevant past information.

## Tensions & Tradeoffs

- **Lossy by design, and more so than compaction**: a reset keeps *nothing*, so any decision, constraint, or fact still relevant to the next task is gone unless it was externalized first — `[[context-compaction]]` exists precisely to avoid this by preserving key decisions, making the two complementary choices rather than substitutes.
- **Reset vs. persist**: clearing the window does not erase durable knowledge held in `[[persistent-agent-memory]]` or a re-read `[[claude-md]]`-style file, so the safe pattern is to push anything worth keeping into a standing store *before* resetting — the reset only clears the volatile conversation, not the grounding tier.
- **Boundary judgment**: the benefit assumes the next task truly is unrelated; resetting mid-task, or between tasks that secretly share context, throws away signal the agent then has to reconstruct — the cost of a mistimed clear is the inverse of the cost of never clearing.
- **A cost lever too**: like `[[reasoning-effort-control]]`, it is partly a token-economy move, and matters most on lower-tier or metered plans where re-reading a bloated history is pure waste.
