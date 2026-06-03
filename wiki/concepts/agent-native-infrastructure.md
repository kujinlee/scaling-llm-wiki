---
concept: Agent-Native Infrastructure
category: Agent Architecture & Patterns
summary: Redesigning documentation, APIs, and tooling so an agent — not a step-following human — is the primary consumer, collapsing multi-step procedures into single-instruction autonomous flows.
aliases: [agent-native infrastructure, agent-native design, agent-first docs and APIs, agent representatives, redefining infra for agents]
related: [computer-use-automation, agent-as-infrastructure, tool-integration-hierarchy, deterministic-workflow-orchestration, claude-md, thinking-vs-understanding]
sources: [꼭-알아야할-안드레-카파시-30분-인터뷰-완전정리-ai시대의-필수-인사이트]
---

# Agent-Native Infrastructure

Agent-native infrastructure is the redesign of documentation, APIs, and operational tooling so that an *agent* — not a clicking, step-following human — is the primary consumer. Today's infrastructure assumes a person reads the docs, navigates the UI, and executes each step; an agent-native version is shaped so the agent can absorb and run the whole process with no human touching anything. The canonical illustration is a deployment that once required a complex multi-step procedure collapsing into a single instruction ("deploy this build"), with the agent handling the rest end to end.

## Key Mechanics

- **From human-step UX to agent-absorbable form**: docs and APIs designed for manual, click-through use are rewritten so an agent can ingest and execute them directly, removing the human from the operational loop.
- **The deployment one-liner**: a complicated deploy flow (the corpus cites a Vercel-style process) becomes "deploy from the build" — the agent translates intent into the full sequence of steps.
- **Hiring is redefined alongside infra**: evaluating engineers by algorithm puzzles is obsolete; the relevant test is building a secure, robust system *with* agents — e.g. a Twitter clone that withstands ten agents ("like Codex") attempting to hack it — measuring the ability to collaborate with and direct agents safely.
- **Endgame — agent representatives**: every human organization gains an agent delegate that handles scheduling, research, and even financial transactions on its behalf, making agents standing participants in workflows rather than tools summoned per task.

## How It Appears in the Corpus

The Kimflip (김플립) summary of Karpathy's interview argues that current infra, docs, and APIs are built for humans to click and follow step-by-step and must be redefined as agent-native, citing a complex deployment reduced to a single "deploy from the build" instruction. It reframes hiring around building agent-resistant secure systems rather than solving puzzles, and forecasts a world where each organization has an agent representative handling scheduling, research, and money movement.

## Tensions & Tradeoffs

- It is the structural counterpart to `[[computer-use-automation]]`: where computer-use makes agents adapt to human-shaped GUIs (brittle, scraping the screen), agent-native infrastructure reshapes the *environment* to fit agents — more robust, but it requires every provider to rebuild for an agent consumer.
- It extends `[[agent-as-infrastructure]]` outward: not only is the agent always-on infrastructure, the surrounding world's docs and APIs become agent-first, and `[[claude-md]]` / the `[[tool-integration-hierarchy]]` are early, local instances of designing for an agent reader.
- Trust and safety scale with reach: agent representatives transacting money and acting across orgs concentrate the `[[jagged-intelligence]]` and merge-trust risks the corpus flags, so agent-native convenience presupposes the supervision that `[[thinking-vs-understanding]]` says humans must retain.
