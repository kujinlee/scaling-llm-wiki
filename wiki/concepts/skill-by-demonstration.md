---
concept: Skill by Demonstration
category: Skills, Plugins & Automation
summary: Authoring a reusable agent skill by performing the workflow once and then having the agent reverse-engineer that worked run into repeatable steps, rather than writing the skill cold from a blank page.
aliases: [Perform-Then-Reverse-Engineer, Demonstrated Skill Authoring]
related: ["[[procedural-knowledge-skills]]", "[[meta-skills]]", "[[persistent-agent-memory]]"]
sources: [learn-80-of-claude-cowork-in-under-20-minutes]
---

# Skill by Demonstration

Skill by demonstration is a way to *create* a reusable agent skill: you do the task with
the agent once — a real, worked run — and then instruct it to reverse-engineer that run
into a named, repeatable skill. Instead of authoring procedure from a blank page (cold),
you produce a concrete example first and let the agent generalize the steps from it. In
Claude Cowork, this is how skills like "clear and concise" (rewrite text with a change
log) or "weekly report" (combine team updates into a structured PDF) get built: perform
the workflow, then say "turn that into a skill."

## Key Mechanics

- **Demonstrate, then distill.** Run the workflow to completion with the agent, then ask
  it to capture the steps it just executed as a reusable skill. The worked run is the
  specification; the skill is the generalization of it.
- **Produces a [[procedural-knowledge-skills]] artifact.** The output is a standard,
  reusable skill — the demonstration is the *authoring method*, not a different kind of
  artifact. The skill can then be invoked to repeat the process reliably.
- **Iterative refinement and reinstallation.** Skills can be updated after creation, but
  changes require manual reinstallation; backing them up (e.g. to Google Drive) is
  recommended so demonstrated skills survive across machines and sessions.
- **Leans on persistent memory.** Because the agent has [[persistent-agent-memory]] and
  local file access, the worked run and its learned preferences persist, which is what
  makes "do it once, then reuse" practical rather than ephemeral.

## How It Appears in the Corpus

Described in Jeff Su's "Learn 80% of Claude Cowork in Under 20 Minutes"
(`learn-80-of-claude-cowork-in-under-20-minutes`): "Skills are created by first
performing the workflow and then instructing Co-work to reverse-engineer the steps into a
reusable skill." The tutorial demonstrates it on text-refinement and multi-team weekly-
report workflows. It is distinct from [[procedural-knowledge-skills]] (the resulting skill
artifact itself) and from [[meta-skills]] (skills whose job is to design or improve other
agents/skills) — skill-by-demonstration names the *bootstrapping technique* by which a
skill comes into being.

## Tensions & Tradeoffs

- **Fidelity of generalization.** Reverse-engineering one worked run risks overfitting to
  that instance — the agent may encode incidental choices as if they were the rule. A
  single demonstration may need review or a second example before the skill is robust.
- **Maintenance friction.** Manual reinstallation after edits and the lack of automatic
  versioning make demonstrated skills easy to create but easy to let drift out of date.
