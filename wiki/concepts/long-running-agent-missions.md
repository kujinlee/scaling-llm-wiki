---
concept: Long-Running Agent Missions
category: Agent Architecture & Patterns
summary: A structured orchestration pattern for multi-day agent tasks using a three-role architecture — orchestrator, workers, validators — with validation contracts agreed before coding, serial execution with internal parallelization, and structured handoffs to preserve correctness and context.
aliases: [missions, agent missions, multi-day agent orchestration, orchestrator-worker-validator, validation contracts, creator-verifier, droid whispering]
related: [deterministic-workflow-orchestration, parallel-isolated-agents, holdout-validation, agent-router, per-node-model-routing, subagent-context-isolation, harness-engineering, agent-swarm-orchestration, context-decay]
sources: [aie-europe-keynotes-coding-agents-ft-pi-google-deepmind-anth]
---

# Long-Running Agent Missions

Long-running agent missions is an orchestration pattern for tasks too large and too long for a single agent session — multi-day work that would otherwise lose its thread to `[[context-decay]]` — built around a fixed three-role architecture and a contract agreed *before* any code is written. An *orchestrator* decomposes the work and coordinates; *workers* implement the pieces; *validators* check each result against a pre-defined "validation contract." By committing the success criteria up front, executing in an ordered sequence while parallelizing internally, and passing structured handoffs between phases, a mission keeps a sprawling task correct and coherent over a duration no single context window could span.

## Key Mechanics

- **Three-role architecture**: the work is split across distinct roles — an orchestrator that plans and coordinates, workers that do the implementation, and validators that verify — so generation and checking are structurally separated rather than left to one agent grading itself.
- **Validation contracts defined before coding**: the criteria a result must satisfy are agreed *up front*, turning "is this done?" into a checkable contract — a creator-verifier split that makes verification a precondition, not an afterthought, and a mission-scale analogue of the `[[holdout-validation]]` separation of roles.
- **Serial execution with internal parallelization**: phases run in order to preserve dependencies and correctness, while independent work *within* a phase is parallelized — the controlled middle ground between fully sequential and the uncoordinated concurrency of `[[parallel-isolated-agents]]`.
- **Structured handoffs preserve context**: each phase passes a deliberate, structured summary to the next, maintaining the task's state across a multi-day horizon rather than relying on one ever-growing conversation — the same summary-return economy as `[[subagent-context-isolation]]` applied across time.
- **Composes delegation, creator-verifier, broadcast, and negotiation**: missions combine several coordination primitives into one system for extended autonomy.
- **"Droid whispering" — model per role**: each role can be assigned the model best suited to it (cheap for coordination, strong for hard implementation, careful for validation), a role-granular instance of `[[per-node-model-routing]]`.

## How It Appears in the Corpus

The AIE Europe keynotes (AI Engineer channel) introduce "Missions" as a structured system for multi-day, long-running agent tasks, combining delegation, creator-verifier, broadcast, and negotiation. Its three-role architecture (orchestrator, workers, validators) leverages validation contracts defined before coding, serial execution with internal parallelization, and structured handoffs to ensure correctness and maintain context over extended periods — and enables "droid whispering," choosing the right model for each role. The same conference surfaces adjacent orchestration tooling — AgentCraft's "campaigns" for decomposed, containerized task execution, and unified "Command and Control" / GitHub Copilot entry points for driving local, background, and cloud agent sessions from one interface — situating missions within a broader move toward managing fleets of long-running agents.

## Tensions & Tradeoffs

- **Distinct from a self-organizing swarm**: where `[[agent-swarm-orchestration]]` lets many agents *self-organize* around work with shared memory, a mission imposes *fixed roles* and an ordered, contract-gated flow — structure and predictability traded for emergent coordination, closer to a `[[deterministic-workflow-orchestration]]` scaffold than to a swarm.
- **The contract bounds the correctness**: a validator can only enforce the validation contract it was given, so a thin or wrong contract confidently approves the wrong result — the "quality of the check bounds the trust" caveat of `[[holdout-validation]]` and `[[self-verification-loop]]`, here fixed before coding begins.
- **Coordination is the new workload**: an orchestrator dispatching workers and reconciling validators is itself a management problem that grows with mission size, the same supervision cost flagged for `[[agent-router]]` and `[[parallel-isolated-agents]]`.
- **Serial phases bound the speedup**: ordering phases for correctness limits how much wall-clock parallelism is available, so missions deliberately buy reliability over raw throughput — the inverse bet from maximally-parallel isolated agents.
