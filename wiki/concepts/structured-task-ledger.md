---
concept: Structured Task Ledger
category: Memory & Knowledge Systems
summary: A persistent set of external files (plan, progress, verify, agents) that holds a task's decomposition and completion state on disk, so fast sessions stay within context limits and any new session or agent resumes exactly where the last left off without re-processing old context.
aliases: [four-file system, structured task ledger, plan progress verify files, external task memory, progress tracking files, plan.md progress.md, task-state ledger, external context files]
related: ["[[persistent-agent-memory]]", "[[claude-md]]", "[[context-compaction]]", "[[context-decay]]", "[[subagent-context-isolation]]", "[[long-running-agent-missions]]", "[[ralph-loop]]", "[[fast-models-slow-developers]]", "[[agent-alignment-artifacts]]"]
sources: [fast-models-need-slow-developers-sarah-chieng-cerebras]
---

# Structured Task Ledger

A structured task ledger is a small, persistent set of plain-text files that externalize a task's *plan and live completion state* onto disk, so that the agent's working context stays small and any fresh session — or a different agent — can pick the work up exactly where the previous one stopped, without re-reading the entire prior conversation. The corpus's concrete instance is a "four-file system": `plan.md` (the initial overall plan and a step-by-step checklist), `progress.md` (which steps are done and which remain), `verify.md` (the checks applied at each step), and `agents.md` (definitions of the sub-agents involved). The ledger's purpose is continuity under tight context budgets: it lets large tasks be decomposed into small, bounded goals whose status lives outside the window, so the agent never has to hold the whole task — or the whole history — in context to know what to do next. It is the task-management counterpart to `[[persistent-agent-memory]]`: where that carries *facts* across sessions, the ledger carries *task state*.

## Key Mechanics

- **Four files, four roles**: `plan.md` stores the overall plan and a step-by-step checklist; `progress.md` tracks completed and pending tasks; `verify.md` holds the per-step checks for correctness and quality; `agents.md` defines the sub-agents. Together they separate *what to do*, *what is done*, *how it is checked*, and *who does it*.
- **Progress on disk, not in context**: because completion state lives in `progress.md`, a new session or agent reads the ledger and resumes precisely where the last left off — no re-processing of old conversation, no dependence on a context window that may have been compacted away. The filesystem is the durable task memory, the same files-as-state move as the `[[ralph-loop]]`.
- **Forces small, bounded goals**: the ledger is paired with the discipline of breaking large tasks into small bounded steps, each tracked as a checklist item, so context utilization stays well below capacity rather than ballooning toward 80–100%.
- **A defense against fast compaction**: under hyper-fast generation the context window overflows far sooner (the corpus cites ~30 seconds versus ~10 minutes), so an external ledger is what keeps a long task coherent across the many short context lifetimes that fast inference produces — the durable record that survives each `[[context-compaction]]`.

## How It Appears in the Corpus

The Sarah Chieng (Cerebras, "AI Engineer" channel) talk "Fast Models Need Slow Developers" prescribes a persistent external memory system to manage context in a fast-paced AI environment, where compaction can occur in ~30 seconds instead of ~10 minutes. It names a "four-file system": `agents.md` (defines sub-agents), `plan.md` (the initial overall plan and step-by-step checklist), `progress.md` (tracks completed and pending tasks so new sessions or agents pick up exactly where left off without re-processing old context), and `verify.md` (used at each step to ensure code quality and correctness) — framed as the structure that lets developers break work into small, focused tasks with continuous progress tracking.

## Tensions & Tradeoffs

- **Distinct from `[[persistent-agent-memory]]` and `[[claude-md]]`**: the ledger holds *task state* (plan, progress, verification status), not durable facts or project conventions — it answers "where am I in this task?" rather than "what do I know about this project?". It is a per-task working record, discarded or archived when the task completes, whereas memory and the context file persist across tasks.
- **A lighter cousin of `[[long-running-agent-missions]]`**: missions impose a formal orchestrator/worker/validator architecture with validation contracts for multi-day work; the four-file ledger is the minimal, file-based version of the same idea — structured handoffs and a verification step without the heavier role machinery, suited to a single developer's fast iterative sessions.
- **The ledger is only as good as it is updated**: resumability depends on `progress.md` actually reflecting reality — a stale or unwritten progress file confidently misleads a resuming session, the same maintenance burden that bounds every standing-context artifact.
- **It overlaps the design artifacts of `[[agent-alignment-artifacts]]`**: a `plan.md` checklist is close to the structure-outline/plan documents that methodology produces, but the ledger emphasizes *live state tracking for resumption* over up-front human alignment — the two compose when a reviewed plan becomes the seed of the tracked ledger.
- **Vantage caveat**: the specific four filenames are one talk's convention, not a standard; the durable idea is an *external, file-based task-state ledger that decouples progress from the context window*, not those exact files.
