---
concept: Test-Driven Development for Agents
category: Workflows & Methodology
summary: Enforcing the red-green-refactor cycle for AI-written code: no production code before a failing test exists and has been confirmed to fail, giving the agent a machine-checkable definition of done.
aliases: [agent TDD, TDD enforcement, the iron law, red-green-refactor for agents]
related: [self-verification-loop, spec-driven-development, agentic-issue-resolution, hill-climbing]
sources: [the-claude-code-plugin-every-developer-must-learn-superpower]
---

# Test-Driven Development for Agents

Test-driven development for agents applies the classic red-green-refactor discipline to AI-written code and enforces it as an inviolable rule: no production code may be written before a failing test exists. By making the agent write a test, watch it fail, write the minimal code to pass, and repeat, TDD gives the agent a machine-checkable definition of "done" for each increment and prevents it from declaring success on code that was never actually exercised.

## Key Mechanics

- The "iron law": write a failing test first, confirm it fails (red), write the minimal code to make it pass (green), then refactor — repeated per increment.
- Watching the test fail first is essential: it proves the test *can* fail and is therefore meaningful, guarding against vacuous tests that pass trivially.
- The failing-then-passing transition is the unit of verification that feeds the `[[self-verification-loop]]` and underpins `[[agentic-issue-resolution]]`'s fail-then-pass regression gate.
- Applied even to meta-work: the same discipline is used when authoring new skills, treating skill creation as code to be test-driven.

## How It Appears in the Corpus

The GritAI Studio Superpowers walkthrough describes TDD as a core enforced skill — its "no production code without a failing test first" iron law — and notes a "Writing Skills" skill that applies TDD to the creation of new skills. The plugin frames this enforcement as a major reason it produces more robust initial implementations than raw Claude Code.

## Tensions & Tradeoffs

- Only as good as the test: a TDD loop optimizes toward passing the written test, so a weak or wrong test gives false confidence — the same "quality of the check bounds the trust" caveat noted for `[[self-verification-loop]]` and `[[hill-climbing]]`.
- Rigidity vs. speed: the "no shortcuts" stance slows trivial changes and assumes the task is expressible as a test up front, which is not always natural.
