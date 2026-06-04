---
concept: Agent as Infrastructure
category: Agent Architecture & Patterns
summary: Deployment pattern in which a coding agent runs as an always-on, cloud-hosted service triggered by schedules, API calls, or repository events, independent of the operator's local machine.
aliases: [agent as infrastructure, always-on agents, cloud-hosted routines, autonomous agent infrastructure, Claude routines, event-triggered agents, scheduled agent tasks]
related: ["[[agentic-capability-ladder]]", "[[graduated-autonomy]]", "[[lifecycle-hooks]]", "[[agent-router]]", "[[subscription-vs-metered-pricing]]", "[[agentic-issue-resolution]]"]
sources: [every-level-of-claude-explained-in-21-minutes, 26년-5월-업데이트-클로드-핵심-기능-300-활용법ㅣ코워크-skills-커넥터-어플, 7-secret-prompts-that-make-claude-code-10x-better]
---

# Agent as Infrastructure

Agent as infrastructure is the deployment pattern in which a coding agent runs as an always-on, cloud-hosted service — triggered by schedules, API calls, or repository events — so it performs work autonomously even when the operator's own computer is off. The agent stops being an interactive tool you sit and drive and becomes standing infrastructure that reacts to events, the top rung of the `[[agentic-capability-ladder]]`.

## Key Mechanics

- Cloud-hosted configurations run independent of any local machine, removing the always-on-desktop dependency that constrained earlier scheduled tasks.
- Triggers are event-driven: time schedules (daily backlog triage), API calls, or version-control events (a PR opened) — for example automated PR review, which overlaps `[[agentic-issue-resolution]]`.
- **Local vs. cloud execution locality**: recurring automation splits along *where it runs*. A *local* recurring task lives on the operator's own machine — it can fire at short intervals but only while the computer stays on and the session stays active, and it expires after a few days. A *cloud* scheduled task runs independently of the local machine (the computer can be off), suits work that needs no local file access (daily stand-ups, recurring reports), accepts only longer intervals and per-plan daily run limits, but does not expire. The cloud variant is what actually crosses the line into "infrastructure"; the local variant is a same-machine convenience that still depends on the operator's box being awake.
- Control surfaces decouple from the terminal: chat channels (Discord, Telegram, iMessage) issue one-way event triggers or two-way interaction from anywhere — the same chat-as-control-surface idea as the `[[agent-router]]`'s Telegram front end. The consumer-grade instance is "Dispatch," which lets the operator drive a desktop app's local agent (its file-and-folder "Co-work" automation) from a phone — remote control of an agent acting on a machine you are away from.
- Headless mode and an agent SDK let the engine be embedded inside other products, while deterministic `[[lifecycle-hooks]]` provide the safety rails that make unattended runs trustworthy.

## How It Appears in the Corpus

The Architect (Level 5) section of the Nate Herk overview describes Claude Routines as cloud-hosted Claude Code configurations triggered by schedule, API, or GitHub events — "turning Claude into infrastructure" — alongside channels for external control and headless / Agent-SDK modes for building products on the engine.

The 이동훈의 루트AI ("Claude core-features 300% guide") tutorial surfaces the consumer-facing seed of the same pattern: the desktop app's "Co-work" feature wires Claude to local files and folders to run automations, and the paired "Dispatch" feature lets the user command that local agent remotely from a phone — a step toward agents that act and are steered independent of where the operator is sitting.

The Sabrina Ramonov "7 Secret Prompts" tutorial draws the local-vs-cloud line concretely with two commands: a `/loop` for *local* recurring tasks (intervals as short as a minute, lasting up to three days, but only while the computer is on and the session active) and a `/schedule` for *cloud-based* recurring tasks that run with the computer off (longer minimum intervals and per-plan daily run limits, but no three-day expiry, suited to stand-ups and recurring reports that need no local file access). The contrast makes explicit that only the cloud-hosted variant achieves true always-on infrastructure, while the local loop remains tethered to the operator's machine.

## Tensions & Tradeoffs

- Autonomy gated by trust: running unattended infrastructure is precisely where `[[graduated-autonomy]]` applies — start with low-stakes routines before scaling stakes and scope.
- Cost exposure: always-on, event-triggered, headless agents consume inference at a scale interactive use never approaches, straining flat-rate plans — the metered-programmatic-use boundary dissected in `[[subscription-vs-metered-pricing]]`. The per-plan daily run limits on cloud scheduling are one concrete expression of that economic pressure.
- Operational surface: cloud hosting, event triggers, and external channels are infrastructure to secure, monitor, and maintain, not merely a chat window.
- Locality is a capability tradeoff, not just a setting: local loops buy short intervals and direct file access at the price of needing the machine on and expiring quickly, while cloud schedules buy true independence at the price of coarser timing, run caps, and no local-file reach — so the choice between them is dictated by whether the task needs local access and how often it must fire.
