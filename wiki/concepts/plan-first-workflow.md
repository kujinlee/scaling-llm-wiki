---
concept: Plan-First Workflow
category: Workflows & Methodology
summary: Agent produces an explicit plan, the human reviews and amends it, and only then does execution proceed — catching misread requirements at the cheapest possible correction point.
aliases: [plan-first workflow, plan mode, plan before execute, plan-review-execute, planning before coding]
related: [spec-driven-development, self-verification-loop, permission-tiering, per-node-model-routing, parallel-isolated-agents, harness-engineering]
sources: [claude-code-창시자-boris의-ai-에이전트-셋업-전부-다-까보자, 12-claude-code-features-every-engineer-should-know-subagents]
---

# Plan-First Workflow

The plan-first workflow is the discipline of having the agent produce an explicit plan of action *before* it executes anything, letting the human review and amend that plan, and only then turning it loose to implement. It is the lightweight, per-task embodiment of the principle that good execution flows from a good plan: the cheapest place to catch a misunderstanding is in the proposed plan, not in the code the agent has already written. Rather than firing a prompt straight at execution, the operator inserts a review checkpoint at the plan stage.

## Key Mechanics

- **Plan, then review, then execute**: the agent first drafts how it intends to approach the task; the human inspects and corrects that plan; execution proceeds only against the approved version.
- **Mirrors real development**: the loop deliberately reproduces how a human engineer works — think and plan before writing — on the premise that the quality of the result is largely determined by the quality of the plan.
- **A cheap correction point**: surfacing the agent's intended approach exposes misread requirements or wrong assumptions while they are still words in a plan, before they compound into code that must be debugged or discarded.
- **Read-only planning as a structural guarantee**: confining the planning phase to read-only tools means nothing can be changed while the plan is being formed, so the review checkpoint is enforced by the environment rather than by the agent's restraint.
- **Composes with model routing**: the planning step benefits from a stronger reasoning model while execution can run on a cheaper one — the phase-split form of `[[per-node-model-routing]]` (e.g. Plan Mode drafting with a powerful model, executing with a lighter one).

## How It Appears in the Corpus

The 김플립 (LLM 코딩) breakdown of Boris's Claude Code setup presents the "plan first" workflow as a core safe-automation practice: rather than executing immediately, the operator has Claude lay out a plan, reviews and revises it, and then proceeds — explicitly invoking the principle that good execution comes from good planning and noting the parallel to a real development process.

The ByteByteAI "12 Claude Code Features" overview describes Plan Mode (entered with Shift+Tab) as the productized form of this discipline: the agent reads files, asks questions, and proposes a step-by-step plan using only *read-only* tools, and execution begins only after the user approves the plan and switches back to normal mode — explicitly to prevent token waste and incorrect edits. The read-only constraint makes "plan before you touch anything" a structural property of the mode, not just an instruction.

## Tensions & Tradeoffs

- **Lighter sibling of `[[spec-driven-development]]`**: both front-load design to cut downstream rework, but plan-first is a single review checkpoint per task, whereas spec-driven development imposes an ordered sequence of hard gates (explore → spec → plan → implement → verify). Plan-first is the same bet at smaller scale and lower ceremony.
- **Plan quality bounds the result**: an approved-but-wrong plan is executed confidently, so the review step only helps insofar as the human (or a reviewer agent) actually catches the flaw — the design-time analogue of the "verifies the wrong thing" risk in `[[self-verification-loop]]`.
- **Overhead on trivial work**: inserting a plan-and-review step feels like friction for small, obvious changes — the same flexibility-vs-rigor tension that the "no shortcuts" gating of `[[spec-driven-development]]` faces more sharply.