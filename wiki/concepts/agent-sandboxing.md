---
concept: Agent Sandboxing
category: Harness & Context Engineering
summary: Constraining an autonomous agent's execution environment and permissions — via isolated machines, containers, and least-privilege scoping — so that when it acts without supervision, the damage it can do and the data it can leak are bounded.
aliases: [Agent Isolation, Agent Containment]
related: ["[[permission-tiering]]", "[[graduated-autonomy]]", "[[ralph-loop]]", "[[agent-as-infrastructure]]", "[[dark-factory]]"]
sources: [ralph-loops-build-dumb-ai-loops-that-ship-chris-parsons-cher, 한글자막-현재-codex-에서-제일-핫한-기능-goal]
---

# Agent Sandboxing

Agent sandboxing is the practice of running an autonomous agent inside a constrained
execution environment so that its blast radius is bounded by construction, not by trust.
When an agent acts without a human in the loop — re-running headlessly, holding
credentials, reaching the internet — the question stops being "will it behave?" and
becomes "what is the worst it can do if it doesn't?" Sandboxing answers that by limiting
the machine it runs on, the permissions it holds, and the network it can reach. It is the
containment layer that makes unattended autonomy survivable.

## Key Mechanics

- **Isolated execution environment.** Run the agent on a throwaway VPS or inside a Docker
  container rather than your primary machine, so filesystem, process, and network access
  are contained and a bad run can be discarded rather than cleaned up.
- **Least-privilege permissions.** Scope tool, file, and credential access to the minimum
  the task needs — the fine-grained side of [[permission-tiering]]. Sandboxing bounds
  *where* the agent runs; permission tiering bounds *what* it may invoke.
- **Network containment.** Restrict or gate outbound access. Internet reach is one leg of
  the "lethal trifecta" — untrusted input, internet access, and sensitive data — whose
  combination is what turns a prompt-injected agent into an exfiltration path.
- **Disposability.** Pair the sandbox with throwaway state so exploratory or "scrappy"
  runs leave no residue on systems you care about.

## How It Appears in the Corpus

The Ralph Loops workshop (`ralph-loops-build-dumb-ai-loops-that-ship-chris-parsons-cher`)
gives the fullest treatment: once you run an agent in a `while true` loop, you must
sandbox it with "VPS, fine-grained permissions, Docker" to mitigate security risks,
"especially the 'lethal trifecta' of untrusted tokens, internet access, and sensitive
data." This is the safety counterpart to the unattended-loop autonomy of [[ralph-loop]],
[[agent-as-infrastructure]], and the [[dark-factory]]. The Codex `/goal` tutorial
(`한글자막-현재-codex-에서-제일-핫한-기능-goal`) makes the same move for long-running
objectives: running Codex in a VPS is advised for "dangerous or resource-intensive goals,"
since a goal-run can contaminate a codebase or consume resources unpredictably.

## Tensions & Tradeoffs

- **Safety vs. capability.** A sandbox shrinks the agent's "surface" — but the `/goal`
  material notes effectiveness is proportional to the surface (logs, metrics, codebase)
  the agent can act on. Too tight a sandbox starves the agent of what it needs to succeed;
  the boundary must be drawn at risk, not convenience.
- **Containment is not trust.** Sandboxing bounds the damage of a bad action but does not
  decide which actions are acceptable — it complements, rather than replaces, approval
  gates and [[permission-tiering]] for high-stakes, irreversible operations.
- **The more autonomy, the more it matters.** Sandboxing is what lets
  [[graduated-autonomy]] escalate safely: each step up in unattended scope widens the
  blast radius, and the sandbox is what keeps that radius survivable.
