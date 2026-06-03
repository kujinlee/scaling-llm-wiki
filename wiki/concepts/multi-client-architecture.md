---
concept: Multi-Client Architecture
category: Harness & Context Engineering
summary: Organizing an agent setup so one root config carries shared methodology while per-client folders supply client-specific overrides, brand context, and memory — keeping projects cleanly separated while reusing common process, with outputs filed in predictable locations.
aliases: [multi-client architecture, multi-project agent setup, config inheritance for agents, per-client overrides, root and client CLAUDE.md, output management, client folder structure]
related: [claude-md, agentic-operating-system, static-identity-context, persistent-agent-memory, context-engineering, compound-engineering, harness-engineering, context-reset, subagent-context-isolation]
sources: [creating-your-own-agentic-os-is-easy-insanely-powerful]
---

# Multi-Client Architecture

Multi-client architecture is the pattern of structuring an agent setup so that an operator serving several clients or projects keeps each one cleanly separated while still reusing a single shared methodology — achieved through config inheritance plus organized output management. The problem it solves is twofold: without separation, one client's context, brand, and memory leak into another's work; without sharing, the operator re-creates the same process for every client. The architecture resolves both by layering a *root* configuration that holds the common instructions and methodology over *per-client* folders that override and extend it with client-specific context, then filing every deliverable in a predictable place so the growing body of outputs does not collapse into disorder.

## Key Mechanics

- **Config inheritance — root plus overrides**: a root `[[claude-md]]` carries the instructions and methodology shared across all clients, while each client folder holds its own `claude.md` override plus that client's brand context (`[[static-identity-context]]`) and agent context (memory, learnings). The agent reads the shared base and the local override together, so common process is written once and client-specific behavior is layered on top — the DRY counterpart to copying a whole setup per client.
- **Per-client context isolation**: giving each client its own brand and memory files keeps one client's voice, facts, and decisions from bleeding into another's work — context separation by *directory boundary*, a standing-folder analogue of the per-task `[[context-reset]]` and the delegation-boundary isolation of `[[subagent-context-isolation]]`.
- **Shared methodology as the reused asset**: the root layer is where accumulated process and hard-won method live, so improving the shared methodology improves every client at once — `[[compound-engineering]]` operating across the whole client portfolio rather than one project.
- **Output management by predictable structure**: generated deliverables are stored in an organized, predictable hierarchy (e.g. a `projects` folder structured by client, then by skill or brief) so outputs are findable and the system does not drift into disorganization as volume grows.

## How It Appears in the Corpus

The Simon Scrapes "Creating Your Own Agentic OS" tutorial presents multi-client architecture as the scaling layer of the OS for operators managing multiple clients: a root `Claude.md` for shared instructions plus individual client folders carrying client-specific `Claude.md` overrides, brand context, and agent context (memory, learnings), with outputs stored in predictable, organized places (a `projects` folder structured by client, then skill/brief) to prevent disorganization.

## Tensions & Tradeoffs

- **Separation vs. sharing**: the architecture's whole value is holding two goals in tension — clean per-client isolation *and* a single reused methodology — so the line between what belongs in the shared root and what belongs in a client override is the central design judgment; put too much in the root and clients diverge awkwardly, too little and the methodology fragments.
- **Override precedence must be unambiguous**: inheritance only works if it is clear which layer wins when root and client configs conflict — an underspecified precedence rule lets a client silently inherit the wrong instruction, the same coverage caveat that bounds any layered-context scheme.
- **Maintenance scales with the client count**: every client folder's brand, memory, and learnings is another artifact to keep current, so the architecture multiplies the standing upkeep cost that already bounds `[[claude-md]]` and `[[persistent-agent-memory]]` — separation localizes problems but does not reduce their number.
- **Output organization fights entropy, but only by discipline**: a predictable output hierarchy prevents deliverables from scattering, yet it depends on every run actually filing into the right place — a convention the system must enforce rather than hope for, or the organized structure rots back into a flat pile.
