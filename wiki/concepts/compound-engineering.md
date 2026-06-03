---
concept: Compound Engineering
category: Workflows & Methodology
summary: Continuously feeding solved problems and hard-won knowledge back into the agent's environment so automation capability accumulates over time rather than being re-solved from scratch.
aliases: [compounding engineering, iterative environment improvement, self-healing layer, root-cause system improvement]
related: [claude-md, self-verification-loop, agentic-issue-resolution, harness-debugging, ai-garbage-collection, parallel-environment-isolation, deterministic-workflow-orchestration]
sources: [live-coding-session-with-boris-cherny-and-jarred-sumner, claude-code와-git-worktree-병렬-구성-배포-방식이-달라집니다]
---

# Compound Engineering

Compound engineering is the practice of continuously feeding solved problems and hard-won knowledge back into the agent's environment so that capability accumulates over time. Each fix, workaround, or clarification is encoded once and thereafter available to every future agent run, producing compounding returns on automation investment.

## Key Mechanics

- Recurring issues and their resolutions are written back into the project's documentation (e.g. `[[claude-md]]`), so the same problem is never solved twice from scratch.
- The development environment is treated as a system to be improved, not a fixed backdrop — better docs, better scripts, and better verification all raise the ceiling on autonomy.
- The effect is cumulative: each increment makes the next automated task more likely to succeed unattended.
- **Self-healing — fix the system, not just the symptom**: when a bug is discovered, the response is not only to patch that bug but to improve the *underlying AI system* that produced it — the global rules, workflows, and skills — so the entire class of error stops recurring. Over time this self-healing layer raises the agent's reliability and self-sufficiency and steadily reduces the need for human intervention, the same "fix the harness, not the prompt" reflex that `[[harness-debugging]]` applies to a harness's own defects.

## How It Appears in the Corpus

The Boris Cherny and Jarred Sumner session names "compound engineering" explicitly as the discipline behind Bun's automation: the living documentation is updated with each new solution, steadily expanding what the agent can do without help.

The Tech Bridge "Claude Code & Git worktree parallel configuration" tutorial frames the same idea as a "self-healing layer" — one of five principles for parallel-agent productivity. Rather than merely fixing a bug an agent introduced, the operator improves the root system (global rules, workflows, skills) that allowed it, so the system grows more reliable and autonomous over time and human review (a noted bottleneck) shrinks. It treats a heavy human review burden as a *signal* that the self-healing/validation layer needs strengthening, not as a permanent cost.

## Tensions & Tradeoffs

- Requires discipline: the compounding only happens if teams consistently capture learnings rather than fixing-and-forgetting.
- Open question: how to keep accumulated knowledge from bloating context and becoming noise over time — the same dilution risk that `[[context-rot]]` names and that `[[ai-garbage-collection]]` prunes from the code side.
- Self-healing can compound the wrong lesson: improving the root system from an observed failure only helps if the diagnosis is right — a mis-attributed root cause hardens a bad rule into the environment, the inverse of the intended effect, so the practice presupposes accurate failure analysis.
