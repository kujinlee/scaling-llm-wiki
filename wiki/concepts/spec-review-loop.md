---
concept: Spec Review Loop
category: Workflows & Methodology
summary: Automated iterative review of a design spec before coding begins: a reviewer sub-agent flags ambiguities and gaps, the author fixes them, and the loop repeats up to a bounded cap.
aliases: [automated spec review, iterative design review, spec review gate, design-review loop]
related: [spec-driven-development, multi-agent-code-review, self-verification-loop, cross-model-critique]
sources: [the-claude-code-plugin-every-developer-must-learn-superpower]
---

# Spec Review Loop

A spec review loop is an automated, iterative review applied to a design specification *before* implementation begins: a reviewer sub-agent inspects the spec for ambiguities, inconsistencies, and gaps; the author agent fixes them; and the reviewer is dispatched again, repeating until the spec converges or an iteration cap is reached and a human is asked to weigh in. It moves review upstream — catching design defects in the document, where they are cheap, rather than in code, where they compound.

## Key Mechanics

- A dedicated reviewer sub-agent evaluates the spec (not code) for ambiguity, inconsistency, and missing detail.
- Iterate-to-convergence: author fixes → reviewer re-checks, looping automatically up to a bounded number of rounds (e.g. five) before escalating to the user.
- Human approval remains a terminal gate: only after both automated convergence and explicit user sign-off does work proceed to implementation planning.
- The committed, reviewed spec becomes a stable reference point for the remainder of the project.

## How It Appears in the Corpus

The GritAI Studio Superpowers walkthrough describes an automated spec-review loop: after brainstorming, a design spec is written to `docs/superpowers` and committed to Git, then a sub-agent reviews it for issues, Claude fixes them, and the reviewer runs again for up to five iterations before requiring user guidance — gating implementation on a solid, agreed-upon design.

## Tensions & Tradeoffs

- Termination problem: like `[[multi-agent-code-review]]`, it needs an explicit stopping rule (the iteration cap) because agents reviewing-and-fixing can otherwise churn without a clear notion of "done."
- Quality ceiling: the reviewer catches only what it is prompted to look for, and a same-model reviewer shares the author's blind spots — a gap `[[cross-model-critique]]` addresses by using a different model.
- It is the design-time analogue of `[[self-verification-loop]]`: verifying the plan before building rather than the build after.
