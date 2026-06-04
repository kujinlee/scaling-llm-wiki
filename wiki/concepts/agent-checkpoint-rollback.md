---
concept: Agent Checkpoint Rollback
category: Coding Tools & IDEs
summary: Automatic snapshotting of project files before each agent edit, with a rewind command to restore any earlier state — enabling fearless experimentation without losing working code.
aliases: [checkpoints, rewind, agent checkpoints, snapshot and rewind, edit-time snapshots, fearless experimentation, undo for agents]
related: ["[[graduated-autonomy]]", "[[parallel-isolated-agents]]", "[[permission-tiering]]", "[[self-verification-loop]]", "[[exploratory-spec-discovery]]"]
sources: [12-claude-code-features-every-engineer-should-know-subagents]
---

# Agent Checkpoint Rollback

Agent checkpoint rollback is the safety mechanism in which the coding environment automatically snapshots the project's files *before each edit* an agent makes, and exposes a command to view those snapshots and restore the project to any earlier state. It makes autonomous agent work recoverable by default: an approach that goes wrong is not a loss of working code but a one-command revert, so the operator can let the agent experiment aggressively without fear. Where `[[parallel-isolated-agents]]` isolates risk in a separate workspace, checkpointing makes the *single active workspace* itself reversible.

## Key Mechanics

- **Snapshot before every edit**: the environment captures project file state automatically prior to each modification, with no explicit action required from the operator — distinct from version control, where a human must deliberately commit.
- **Rewind to any point**: a command (e.g. `/rewind`) lists the captured checkpoints and restores the project to a selected earlier state, undoing one or many edits at once.
- **Fearless experimentation**: because any wrong turn is recoverable, the operator can let the agent try bold approaches and roll back cleanly if they fail, lowering the cost of an attempt to near zero.
- **Fine-grained and automatic**: checkpoints are per-edit and implicit, giving a denser, lower-ceremony safety net than branch-and-commit workflows — complementary to, not a replacement for, git.

## How It Appears in the Corpus

The ByteByteAI "12 Claude Code Features" overview presents Checkpoints as a robust undo mechanism: before each edit Claude Code automatically snapshots the project files, and if an approach goes wrong the user types `/rewind` to view the checkpoint list and restore the project to any earlier state, enabling experimentation without fear of losing working code.

## Tensions & Tradeoffs

- **Distinct from git-worktree isolation**: `[[parallel-isolated-agents]]` and `[[exploratory-spec-discovery]]` isolate risky work in a separate branch/worktree to be discarded; checkpoint rollback instead makes the in-place workspace reversible at edit granularity — automatic and fine-grained versus deliberate and coarse. They cover different recovery needs and compose.
- **Lowers the stakes that gate autonomy**: cheap reversibility is exactly what lets an operator widen agent authority under `[[graduated-autonomy]]` — a recoverable mistake is a low-stakes one — and pairs with `[[permission-tiering]]` (which prevents dangerous actions) by cleaning up the merely-wrong ones.
- **Only file state is captured**: checkpoints restore project files, but they cannot undo external side effects an edit may have triggered — database writes, deploys, API calls, sent messages — so rollback is not a substitute for the *prevention* that permission tiering and `[[self-verification-loop]]` provide.
- **Not version history**: per-edit snapshots are a session-scoped undo, not durable, shareable version control; they reduce fear of experimentation but do not replace committing meaningful states to git.