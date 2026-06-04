---
concept: Governance Layer
category: Harness & Context Engineering
summary: Standing documents (mission, rules, global context) that constrain an autonomous coding system by encoding purpose and policy once rather than requiring per-action approval.
aliases: [governance layer, factory governance, mission and rules files, agent governance files, mission.md, factory_rules.md]
related: ["[[claude-md]]", "[[harness-engineering]]", "[[dark-factory]]", "[[deterministic-workflow-orchestration]]", "[[context-engineering]]", "[[lifecycle-hooks]]"]
sources: [i-m-building-an-ai-dark-factory-that-ships-its-own-code-publ]
---

# Governance Layer

A governance layer is the set of standing, high-level documents that constrain and direct an autonomous coding system — defining its mission, its operating rules, and its global codebase context — so that an agent left to write and ship its own code stays aligned with intent and within bounds. It is the operator's console for steering a system they no longer review step-by-step: instead of approving each action, the operator encodes purpose and policy once, and every workflow loads that governance before it acts.

## Key Mechanics

- Three constraint documents, each answering a different question: a *mission* file (purpose, in-scope and out-of-scope features, boundaries) governs *what* may be built; a *rules* file (issue-triage procedure, label system, implementation requirements such as concise PRs and mandatory testing, and the quality gates for auto-merge) governs *how* work is done; and a *global-context* file (tech stack, repository layout, test commands, code conventions) supplies the operational knowledge to act in the codebase.
- The global-context file is the `[[claude-md]]` of the system — the same role of giving the agent its build/test/convention knowledge — while the mission and rules files add the scope and policy constraints that hands-off operation specifically requires.
- All three are loaded into context for *every* workflow run, so the system's understanding of its mission and guardrails stays consistent across triage, implementation, and validation rather than being re-derived each time.
- It is the constraint half of a `[[harness-engineering]]` harness — the written rules-and-specification artifacts — distinct from the executable workflow scaffold (`[[deterministic-workflow-orchestration]]`) that carries out the process.

## How It Appears in the Corpus

The Cole Medin "AI Dark Factory" experiment defines a governance layer of three markdown files — `mission.md` (app purpose, scope, boundaries), `factory_rules.md` (issue triaging, label system, implementation and auto-merge quality gates), and `claw.md` (global tech-stack, repo layout, testing, and convention rules) — loaded into context for every Arkon workflow, framed as the console of high-level instructions that keeps the autonomous factory (`[[dark-factory]]`) building only what is intended.

## Tensions & Tradeoffs

- Completeness vs. context budget: loading all three governance files into every workflow re-raises the `[[context-rot]]` tension — the more the governance layer specifies, the more standing context every run pays for, so the files must stay high-signal.
- It is prose policy, not enforcement: a governance document states the rules but cannot guarantee the agent follows them, unlike deterministic `[[lifecycle-hooks]]` or workflow gates — so governance is necessary but not sufficient for safe autonomy, and must pair with the validation gate to be trustworthy.
- Scope drift: a mission's in/out-of-scope boundary is only as good as how well it anticipates edge requests; an underspecified boundary lets an unsupervised system build the wrong thing confidently.
