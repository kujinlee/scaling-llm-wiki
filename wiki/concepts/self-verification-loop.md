---
concept: Self-Verification Loop
category: Workflows & Methodology
summary: An agent independently confirms its own changes are correct by running checks it can interpret and producing evidence — not a claim — before declaring success.
aliases: [agent self-verification, autonomous correctness checking, verification before completion]
related: ["[[hill-climbing]]", "[[agentic-issue-resolution]]", "[[multi-agent-code-review]]", "[[shifting-bottlenecks]]", "[[agent-tdd]]", "[[spec-review-loop]]", "[[holdout-validation]]", "[[satisfaction-testing]]", "[[plan-first-workflow]]", "[[generator-verifier-loop]]"]
sources: [live-coding-session-with-boris-cherny-and-jarred-sumner, the-claude-code-plugin-every-developer-must-learn-superpower, claude-code-창시자-boris의-ai-에이전트-셋업-전부-다-까보자, claude-code-just-dropped-goal-master-it-in-8-minutes]
---

# Self-Verification Loop

A self-verification loop is the capability for an agent to independently confirm that its own changes are correct, without waiting on a human to check. This is the mechanism that makes large-scale autonomous and parallel agent work viable: if each agent can prove its own result, hundreds can run at once and only trustworthy output reaches the human.

## Key Mechanics

- The agent runs a check it can interpret — tests, builds, metrics — to confirm correctness before declaring success.
- Verification before completion: the agent must produce *evidence* — run the check and show its output — before asserting that work is done, rather than claiming success from inspection alone.
- The task assignment must include the review criteria: just as you would hand a human collaborator a standard for judging the work, the agent is given how to test, debug, and refine its own output — making verification an explicit part of the instruction, not an afterthought.
- Self-verification is the enabling substrate for both `[[hill-climbing]]` (it supplies the progress signal) and `[[agentic-issue-resolution]]` (the fail-then-pass regression test is a verification step); `[[agent-tdd]]` supplies it at the per-increment level.
- Reliable self-checking unlocks parallelism: with verification per agent, many autonomous agents can execute simultaneously.

## How It Appears in the Corpus

The Boris Cherny and Jarred Sumner session ties recent model advances (cited as "Opus 47") to running hundreds of autonomous agents in parallel, made possible because each can self-verify its changes.

The Superpowers plugin (GritAI Studio walkthrough) operationalizes this as an explicit "Verification Before Completion" skill: Claude must run the plan's verification commands and confirm passing output before reporting completion. Its `[[agent-tdd]]` enforcement supplies the per-increment signal, and its `[[spec-review-loop]]` applies the same verify-before-proceeding logic to the design document.

The 김플립 (LLM 코딩) breakdown of Boris's Claude Code setup makes the verification loop its headline: the operator must hand the agent not just the task but the *checking* of the task — writing and running tests, analyzing errors, and fixing them — turning Claude from a code generator into an agent that confirms and improves its own work. It stresses that, exactly as when delegating to a person, you must supply the review criteria along with the task.

The Tristen O'Brien tutorial on Claude Code's `/goal` command shows the verification step *externalized* into a second agent: a supervisor ("boss") checks "is the goal met?" after each step the worker takes, rather than the worker grading itself — the `[[generator-verifier-loop]]` variant that converts a self-check into a separate-checker loop while preserving the same evidence-before-completion discipline.

## Tensions & Tradeoffs

- Depth of verification is the frontier: the corpus notes that surface-level checks are no longer the bottleneck — establishing *sufficient* proof of correctness for automated merges is (see `[[shifting-bottlenecks]]`).
- A loop that verifies the wrong thing gives false confidence; the quality of the check bounds the trust.
- Self-checking is vulnerable to bias when the verifier is the implementer: the `[[holdout-validation]]` pattern hardens the loop against AI sycophancy by handing the check to an agent withheld from the development context, the `[[generator-verifier-loop]]` separates the checker into a distinct supervisor agent within the live loop, and `[[satisfaction-testing]]` raises the bar from unit checks to whole end-to-end user journeys — all responses to the "verifies the wrong thing" failure mode, and the substrate that lets a `[[dark-factory]]` merge with no human in the loop.
