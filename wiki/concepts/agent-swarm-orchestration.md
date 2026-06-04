---
concept: Agent Swarm Orchestration
category: Agent Architecture & Patterns
summary: Scaling beyond a single conductor's isolated fleet — many specialized agents self-organize into swarms with shared memory across sessions and federated communication across machines.
aliases: [agent swarms, self-organizing agent swarms, swarm orchestration, federated agents, shared-memory swarms, cross-machine agent federation]
related: ["[[parallel-isolated-agents]]", "[[subagent-context-isolation]]", "[[agent-router]]", "[[persistent-agent-memory]]", "[[cross-tool-memory]]", "[[deterministic-workflow-orchestration]]", "[[token-maxing]]", "[[harness-engineering]]", "[[graduated-autonomy]]"]
sources: [6-claude-code-github-repos-that-change-everything]
---

# Agent Swarm Orchestration

Agent swarm orchestration is the pattern of scaling agentic work past a single human conductor's hand-dispatched fleet by letting many specialized agents *self-organize into swarms*, share memory across sessions, and communicate in a federated way across multiple machines. Where `[[parallel-isolated-agents]]` deliberately *isolates* each session — a separate workspace, no shared state, one human conducting — a swarm inverts two of those choices: the agents coordinate among themselves and read and write a *shared* memory, trading isolation's safety for emergent, large-scale collaboration aimed at heavy or team-scale workloads.

## Key Mechanics

- **Self-organizing swarms**: rather than the operator dispatching each agent to a task, a large pool of specialized agents groups itself into swarms around the work — coordination is delegated to the fleet, not held entirely by a single conductor as in `[[agent-router]]`.
- **Shared memory across sessions**: swarm members read and write a common store, so state persists and is visible across the fleet — the cross-session continuity of `[[persistent-agent-memory]]` and `[[cross-tool-memory]]` applied to many agents at once, and the deliberate opposite of per-session isolation.
- **Federated cross-machine communication**: agents running on *different machines* communicate and coordinate, so a swarm is distributed infrastructure rather than many sessions on one box.
- **Modular operational surface**: the swarm is wrapped in plugins for the things a hard-to-supervise fleet needs — security, testing, documentation, observability, and cost tracking — making the coordination governable and its token spend (`[[token-maxing]]` at fleet scale) legible.

## How It Appears in the Corpus

The Nuno Tavares "6 Claude Code GitHub Repos" overview presents "Roof Flow" as the power-user/team tier: 100 specialized agents that self-organize into swarms, with shared memory across sessions and federated communications between agents on different machines, plus 32 plugins spanning security, testing, documentation, observability, and cost tracking. It is framed as the option for heavy usage or multiple Claude instances and for maximizing token throughput across large-scale or team-based projects.

## Tensions & Tradeoffs

- **Shared memory reintroduces the risk isolation removed**: `[[parallel-isolated-agents]]` isolates precisely so concurrent agents do not collide over shared state; a swarm's shared memory brings back consistency and contention problems that the isolated model sidesteps, so the safety has to be re-engineered rather than assumed.
- **Coordination becomes the workload**: as with `[[agent-router]]` and `[[parallel-isolated-agents]]`, supervising and reconciling many agents is itself a management problem — amplified here by self-organization and cross-machine federation, which is why observability and cost-tracking plugins are bundled rather than optional.
- **Autonomy raises the trust frontier**: a self-organizing, distributed swarm acts with less per-step human oversight, so it sits exactly where `[[graduated-autonomy]]` applies — scope and stakes should widen only as the swarm proves reliable, and a standing `[[harness-engineering]]` structure is what keeps emergent coordination from drifting.
- **Maturity and vantage caveat**: the framing comes from an intermediate tutorial aimed at advanced users, and the scale figures (100 agents, 32 plugins) are product descriptions, not measured outcomes — the pattern's robustness at scale is asserted, not demonstrated.
