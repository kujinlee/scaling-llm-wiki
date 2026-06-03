---
concept: Lifecycle Hooks
category: Agent Architecture & Patterns
summary: Custom logic that fires at defined agent execution events (pre-tool-use, post-edit, session-stop), enforcing deterministic guardrails the model cannot skip or forget.
aliases: [lifecycle hooks, agent hooks, event hooks, safety-rail hooks, pre-tool-use hook, stop hook, hooks as middleware, tool-call interceptor]
related: [persistent-agent-memory, agent-as-infrastructure, graduated-autonomy, self-verification-loop, deterministic-workflow-orchestration, plugin-packaging, context-compaction, agentic-loop, distributed-systems-literacy]
sources: [every-level-of-claude-explained-in-21-minutes, every-claude-code-memory-system-compared-so-you-don-t-have-t, 12-claude-code-features-every-engineer-should-know-subagents, claude-s-internal-architecture-revealed-how-ai-agents-actual]
---

# Lifecycle Hooks

Lifecycle hooks are custom pieces of logic that fire automatically at defined points in an agent's execution — before a tool runs, after an edit, when the session stops — letting the operator wrap deterministic guardrails and side effects around an otherwise non-deterministic agent. Because the harness, not the model, executes them, they enforce behavior the agent cannot skip or forget, making them the mechanism that turns risky autonomous operation into something trustworthy. Architecturally they are *middleware*: a layer that intercepts every tool call between the model's decision and the environment's execution.

## Key Mechanics

- Hooks bind code to lifecycle events: a *pre-tool-use* hook to block dangerous commands, a *post-edit* hook to auto-format, a *stop* hook to send a completion notification.
- **Middleware over the tool boundary**: because the `[[agentic-loop]]` routes every environmental action through a tool call, a hook can sit on that boundary and *inspect, modify, or block* each call before it executes — the classic middleware role applied to agent tool use, and the interception point that the model-thinks/tools-do separation of concerns makes possible.
- Deterministic enforcement: hooks run regardless of the agent's judgment, supplying guarantees that prose instructions in `[[claude-md]]` cannot — a safety rail independent of what the model decides to do.
- Observability as well as control: intercepting every tool call is also how the system gains visibility into what the agent is doing, so hooks serve monitoring and logging, not only blocking.
- Same primitive, memory use: session-start, user-prompt-submit, session-end, and pre-compaction hooks inject or persist memory automatically (see `[[persistent-agent-memory]]` and `[[context-compaction]]`), so recall does not depend on the model choosing to call a search tool.
- Hooks are what raise trust and reliability in unattended deployments, pairing naturally with `[[agent-as-infrastructure]]` and supplying the guardrails that enable `[[graduated-autonomy]]`.

## How It Appears in the Corpus

The Architect (Level 5) section of the Nate Herk overview presents hooks as custom logic firing at lifecycle events — pre-tool-use blocks, post-edit formatting, stop-event notifications — explicitly framed as safety rails that build trust in production systems. The Simon Scrapes memory-systems comparison uses the same hook primitive for the opposite end: automatically injecting and persisting memory at session and compaction boundaries.

The ByteByteAI "12 Claude Code Features" overview presents hooks as scripts that run automatically at specific points in the agent's workflow loop (e.g. before or after a tool run), ensuring deterministic actions — code formatting, security checks, logging — are always performed regardless of the model's choices, and notes that hooks are among the artifacts a `[[plugin-packaging|plugin]]` can bundle for sharing.

The ByteMonk "Claude's Internal Architecture Revealed" analysis casts hooks explicitly as *middleware*: every tool call is intercepted by hooks that provide critical points for inspection, modification, or even blocking of commands, significantly enhancing safety and observability. It maps the hook layer onto the middleware tier of a distributed system (`[[distributed-systems-literacy]]`), reinforcing that hooks sit on the model-to-environment tool boundary the `[[agentic-loop]]` creates.

## Tensions & Tradeoffs

- Deterministic enforcement vs flexibility: hooks reliably constrain the agent but, like all hard-coded scaffold, can block legitimate actions and add maintenance burden — the same rigidity tradeoff as `[[deterministic-workflow-orchestration]]`.
- Coverage gap: a hook only guards the event someone thought to wire; an unhooked failure mode passes silently, so the safety net is exactly as complete as the hook set.
- Always-on injection hooks spend context budget on every event — the automatic-injection-vs-tool-call tradeoff noted in `[[persistent-agent-memory]]`.
- Middleware on the critical path: because a hook intercepts every matching tool call, a slow, buggy, or overly aggressive hook becomes a bottleneck or a false-positive blocker on the loop itself — the cost of inserting a layer between every decision and its execution.
