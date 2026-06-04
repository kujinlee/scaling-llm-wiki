---
concept: Permission Tiering
category: Harness & Context Engineering
summary: Graded allow/ask/deny authority model for agents: auto-allow known-safe commands, require explicit approval for sensitive ones, and outright forbid dangerous ones.
aliases: [permission tiering, granular permissions, allow-ask-deny permissions, scoped agent permissions, no-auto-accept, permission management]
related: ["[[lifecycle-hooks]]", "[[auto-correction-loop]]", "[[graduated-autonomy]]", "[[plan-first-workflow]]", "[[claude-md]]", "[[harness-engineering]]", "[[agent-checkpoint-rollback]]"]
sources: [claude-code-창시자-boris의-ai-에이전트-셋업-전부-다-까보자, 12-claude-code-features-every-engineer-should-know-subagents]
---

# Permission Tiering

Permission tiering is the practice of governing what an agent may do through a graded permission model — automatically allowing known-safe commands, requiring explicit human approval for sensitive ones, and outright forbidding dangerous ones — instead of granting blanket "do anything" autonomy. Its purpose is to bound the agent's blast radius without forcing a human to approve every keystroke: routine work flows freely, risky work pauses for sign-off, and destructive work is structurally impossible. The contrast it warns against is the all-or-nothing posture of a fully permissive auto-run mode, where a single bad command can do irreversible damage.

## Key Mechanics

- **Three tiers of authority**: a set of commands is auto-allowed (run without prompting), a set requires approval (the agent pauses and asks before executing), and a set is denied (the agent is forbidden from running them at all).
- **Reject blanket auto-accept**: the explicitly-named anti-pattern is a dangerous auto-execute mode that hands the agent too much freedom; tiering replaces "trust everything" with "trust the safe subset."
- **Static structure, not step-by-step review**: the operator encodes the policy once as lists rather than adjudicating each action live — the permission layer does the gating, conserving human attention for the approval tier only.
- **Composes with mechanical gates**: it sits alongside linters and formatters wired into the automation pipeline (the `[[auto-correction-loop]]`) and deterministic `[[lifecycle-hooks]]` — together they form the environment-level guardrails a `[[harness-engineering]]` harness relies on, independent of the model's judgment.

## How It Appears in the Corpus

The 김플립 (LLM 코딩) breakdown of Boris's Claude Code setup names granular permission management as a pillar of safe automation: rather than enabling a risky auto-execute mode, the operator allows specific commands, requires approval for others, and forbids dangerous ones, and folds linters and formatters into the pipeline to catch small style and format issues the agent might miss. It frames this as part of pursuing "manageable automation" rather than maximal autonomy.

The ByteByteAI "12 Claude Code Features" overview corroborates the model from a second source: `/permissions` lets the operator pre-approve known-safe actions (e.g. running tests) and block dangerous ones (e.g. deleting files), the same allow/deny structure framed explicitly as balancing automation speed against project safety.

## Tensions & Tradeoffs

- **Coverage equals what you anticipated**: the deny and ask lists only protect against the dangers someone thought to enumerate; an unlisted destructive command can still slip through the auto-allow tier — the same coverage-gap caveat noted for `[[lifecycle-hooks]]` and `[[auto-correction-loop]]`.
- **Safety vs. friction**: a tight ask-list interrupts the agent frequently and slows throughput, while a loose one approaches the auto-accept mode it was meant to avoid — the placement of the line is the whole game.
- **Prevention vs. recovery**: permission tiering *prevents* dangerous actions, while `[[agent-checkpoint-rollback]]` *recovers* from merely-wrong ones — the two are complementary safety layers, since checkpointing cannot undo a destructive command that should never have run.
- **Static structure vs. temporal trust**: permission tiering is the *fixed* allow/ask/deny structure at any moment, whereas `[[graduated-autonomy]]` is the discipline of *widening* that structure over time as the agent earns trust — the two compose, tiering being the lever graduated autonomy adjusts.