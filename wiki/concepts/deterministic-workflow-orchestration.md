---
concept: Deterministic Workflow Orchestration
category: Agent Architecture & Patterns
summary: Encoding a development process as a declarative workflow that interleaves deterministic commands (validation, approval gates) with LLM prompt nodes, making AI coding repeatable and reliable.
aliases: [declarative agent workflows, workflow-as-code, YAML workflow definitions, deterministic-plus-LLM workflows, AI coding workflow builder]
related: [harness-engineering, per-node-model-routing, context-engineering, parallel-isolated-agents, spec-driven-development, agent-router, dark-factory, governance-layer, harness-debugging]
sources: [the-next-evolution-of-ai-coding-is-harnesses-here-s-how-to-b, i-m-building-an-ai-dark-factory-that-ships-its-own-code-publ, the-ai-dark-factory-is-alive-a-codebase-that-writes-its-own-]
---

# Deterministic Workflow Orchestration

Deterministic workflow orchestration is the technique of encoding a development process as a reusable, declarative workflow — a sequence of nodes defined in a config file such as YAML — that interleaves *deterministic* commands (context creation, validation, human-approval gates) with *non-deterministic* LLM prompt nodes for the parts that need reasoning. By scripting the steps an agent would otherwise forget or skip, it makes AI coding repeatable and reliable: the probabilistic agent supplies intelligence at specific nodes, while a deterministic scaffold guarantees the critical structure around it.

## Key Mechanics

- A workflow is a declarative file (e.g. YAML) describing a sequence of nodes: a description for agent understanding, provider details, and steps that can branch based on decisions.
- Nodes are of two kinds — deterministic commands (curate context, run validation, pause for human approval) and LLM-driven prompt steps (planning, classification, implementation) — combined so guaranteed steps are enforced rather than left to the agent's discretion.
- Workflows are reusable and portable across codebases, and can be invoked from multiple surfaces (CLI, GitHub, chat) and run in parallel (see `[[parallel-isolated-agents]]`) to address several issues or features concurrently.
- The pattern is meta-programmable: a "workflow builder workflow" can author new workflows, echoing the `[[meta-skills]]` idea of artifacts that design other artifacts.
- It is the executable embodiment of a `[[harness-engineering]]` harness, and each node carries its own engineered context (`[[context-engineering]]`) and can run on a different model (`[[per-node-model-routing]]`).

## How It Appears in the Corpus

The Cole Medin tutorial presents Archon, billed as the first open-source "harness builder" for AI coding, whose workflows are defined in YAML mixing deterministic commands with coding-agent prompts. It ships pre-packaged workflows for common tasks (fixing GitHub issues, creating PRs, comprehensive PR review) and supports custom ones — including a Beads-inspired persistent-memory workflow with exploration, task decomposition, and iterative implementation. The presenter frames the goal as an "N8N-like builder for AI coding," with a web UI and CLI for monitoring node-by-node execution.

The Cole Medin "AI Dark Factory" experiment puts the same Arkon/Archon harness builder at the center of a fully autonomous coding loop: a *scheduled* triage workflow fetches and labels incoming GitHub issues, each accepted issue spawns a *parallel* implement workflow (research → classify → plan → implement → open PR), and a separate validation workflow gates the merge. It is a concrete deterministic triage-implement-validate orchestration whose nodes mix scheduled deterministic steps with LLM reasoning and route a cheaper model to the triage node (`[[per-node-model-routing]]`), showing the pattern scaled from on-demand task workflows to a continuous, self-feeding factory loop (`[[dark-factory]]`) bounded by a standing `[[governance-layer]]`.

The "AI Dark Factory is ALIVE" live stream runs those Archon workflows in production on a VPS — triage → implement → validate (with browser automation) → merge → deploy — and demonstrates a point the tutorials only assert: the workflows themselves are fallible artifacts that must be debugged. A validation node failed to start the application (missing `DATABASE_URL`) and carried too permissive a verdict, and the presenter live-edited and re-ran the YAML workflow to harden it — the orchestration-side instance of `[[harness-debugging]]`.

## Tensions & Tradeoffs

- Determinism vs. flexibility: hard-coding steps buys reliability but can over-constrain tasks that need the agent to improvise, the same rigidity tradeoff seen in `[[spec-driven-development]]`'s "no shortcuts" gates.
- Authoring and maintenance cost: workflows are another artifact to write, debug, and keep current as codebases and tools change — and the live dark-factory run shows this is not hypothetical, with workflow nodes failing open and needing live correction (`[[harness-debugging]]`).
- Maturity caveat: the corpus's flagship examples are explicitly works in progress — an ongoing passion project and a public dark-factory experiment debugged on air — so the pattern's robustness at scale is asserted and tested in the open more than independently demonstrated.
