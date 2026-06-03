---
concept: Skills as On-Demand Procedural Knowledge
category: Skills, Plugins & Automation
summary: Packaging a recurring task's procedural knowledge into a self-contained skill (skill.md plus scripts and references) that an agent loads only when the task requires it, instead of pasting playbooks into every prompt.
aliases: [skills, claude code skills, procedural knowledge skills, on-demand skills, skill files, skill.md, skills as plugins, agent skills, reusable agent workflows]
related: [thin-harness-fat-skills, plugin-packaging, lazy-context-loading, meta-skills, agent-tdd, lifecycle-hooks, permission-tiering, robust-tool-design, assistant-personalization-layers, compound-engineering, harness-engineering]
sources: [claude-code-skills-are-the-new-plugins-i-tested-matt-pocock-]
---

# Skills as On-Demand Procedural Knowledge

A skill is a self-contained, reusable package of *procedural knowledge* — how to perform a specific recurring task — that an agent loads only when that task is actually at hand, rather than carrying the instructions in every prompt. The corpus frames skills as the practical "plugin layer" for AI coding agents: where a developer would otherwise paste the same playbook into the conversation again and again, a skill encapsulates that workflow once and the agent pulls it in on demand. This is what turns an agent from an intelligent chatbot that re-derives its method each time into a repeatable engineering teammate that applies a consistent, vetted procedure. It is the *artifact* form of the "fat skill" design principle (`[[thin-harness-fat-skills]]`) and the unit that `[[plugin-packaging]]` distributes.

## Key Mechanics

- **On-demand loading, not always-on**: a skill is loaded only when a specific task triggers the need for it, keeping the agent's active context lean and high-signal instead of bloated with playbooks it isn't currently using — the same trigger-based discipline as `[[lazy-context-loading]]`, applied to whole procedures.
- **Procedural knowledge over pasted prompts**: the value proposition is replacing the brittle habit of re-pasting a playbook with a packaged, repeatable workflow the agent can invoke — procedural knowledge supplied without overwhelming the agent with a giant manual in every prompt.
- **Small, focused ideas**: skills are built around narrow, single-purpose workflows rather than sprawling frameworks; each captures one well-scoped capability or behavior.
- **Folder structure — `skill.md` plus assets**: a skill is organized as a folder containing a `skill.md` file (the procedural instructions), supporting scripts, and reference material — a consistent layout that lets an agent acquire both the *knowledge* and the *executable pieces* of a task together.
- **Categories of skill**: the corpus groups skills by the kind of work they encode — *planning* (turning a conversation into a PRD or issue), *development* (enforcing test-driven development or architecture review), *tooling* (adding guardrails around dangerous operations), and *writing*.
- **Packages behavior and constraints, not just text**: a skill can encode not only a prompt but specific behaviors and safety constraints — e.g. a TDD skill that drives a strict "one test, one implementation, repeat" loop (`[[agent-tdd]]`), or a git-guardrail skill that installs hooks to block destructive commands such as `push`, `reset --hard`, and `clean` before the agent can execute them (`[[lifecycle-hooks]]`, `[[permission-tiering]]`).

## How It Appears in the Corpus

The TechWealth Hub video "Claude Code Skills Are the New Plugins" tests Matt Pocock's public skills directory (a widely-starred GitHub repository drawn straight from his personal Claude directory) as a model of simple, effective skill organization. It presents skills as the emerging plugin layer for coding agents: packaged, repeatable workflows loaded on demand rather than pasted playbooks. It walks through the `skill.md` + scripts + references folder structure, the planning/development/tooling/writing categories, and two concrete examples — a TDD skill enforcing a one-test-one-implementation loop, and a git-guardrail skill that hooks dangerous git commands to block them before execution. The video stresses evaluating skills for readability, compactness, and clear organization, and understanding the *pattern* rather than blindly installing skills from untrusted sources.

## Tensions & Tradeoffs

- **Over-constraint and false confidence**: a poorly designed skill can box the agent in — over-constraining its actions or creating false confidence that a vetted procedure is being followed when the skill is actually wrong for the situation. The skill is only as good as the procedure it encodes, the recurring "quality of the artifact bounds the trust" caveat.
- **Untrusted skills are a security surface**: because a skill can bundle executable scripts, installing one from an untrusted source can introduce unsafe behavior the operator never inspected — the same trust-surface concern that `[[plugin-packaging]]` raises for bundled hooks and MCP servers, here at the granularity of a single skill.
- **Evaluate, don't blind-copy**: the corpus's explicit guidance is to judge a skill by readability, compactness, and clear organization and to understand the underlying pattern, rather than mechanically installing community skills — adopting a skill without comprehending it is the procedural-knowledge analogue of shipping code you cannot supervise.
- **Distinct from neighboring concepts**: `[[thin-harness-fat-skills]]` is the *design philosophy* (keep the loop thin, push behavior into prose skills); `[[plugin-packaging]]` is the *distribution mechanism* (bundle skills with hooks and MCP servers for one-command install); `[[meta-skills]]` are skills that *design other agents*. This concept is the skill *artifact itself* — the packaged unit of on-demand procedural knowledge those other concepts shape, ship, and generate.
- **Method layer of personalization**: a skill standardizes *how* a recurring task is performed, the method axis of `[[assistant-personalization-layers]]`, and accumulating vetted skills over time is `[[compound-engineering]]` applied to an operator's working procedures — but a stale skill propagates an outdated method just as silently as it once standardized a good one.
