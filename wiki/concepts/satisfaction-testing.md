---
concept: Satisfaction Testing
category: Workflows & Methodology
summary: Validating a change by exercising entire end-to-end user journeys through browser automation on the running application, asking "would a user be satisfied?" rather than asserting on units.
aliases: [satisfaction testing, user-journey validation, end-to-end satisfaction testing, journey-based testing, satisfaction-based validation]
related: [holdout-validation, self-verification-loop, computer-use-automation, agent-tdd, dark-factory, harness-debugging]
sources: [i-m-building-an-ai-dark-factory-that-ships-its-own-code-publ, the-ai-dark-factory-is-alive-a-codebase-that-writes-its-own-]
---

# Satisfaction Testing

Satisfaction testing is the practice of validating a change by exercising entire end-to-end user journeys — driving the real application the way a user would, typically through browser automation — to confirm the experience is actually correct, rather than asserting on isolated units. It reframes "does it pass?" as "would a user be satisfied?": the unit of verification is a complete journey through the running product, so the test certifies real-world functionality instead of the internal behavior of a function.

## Key Mechanics

- The unit of validation is a user journey, not a function: the system asks whether the end-to-end experience the user cares about works, exercising the deployed application end to end.
- Browser automation is the vehicle: the validator drives the running app through its UI to reproduce the journey — a purpose-built application of the same GUI-driving capability as `[[computer-use-automation]]`.
- It complements rather than replaces unit tests: in the corpus it is preferred over relying on unit tests alone, because unit coverage can pass while the assembled journey is broken.
- It is what makes hands-off merging plausible: validating the *experience* end to end is a stronger trust signal than green unit tests for a system that ships with no human review.

## How It Appears in the Corpus

The Cole Medin "AI Dark Factory" experiment focuses its validation stage on "satisfaction testing" of entire user journeys via browser automation rather than just unit tests, ensuring real-world functionality and user experience are correct before code merges autonomously. It runs inside the held-out validation agent (`[[holdout-validation]]`) that gates the `[[dark-factory]]` merge.

The "AI Dark Factory is ALIVE" live stream exposes the failure mode that most threatens this gate: the validation workflow could not start the application (a missing `DATABASE_URL` environment variable), so its browser-automation journey never actually ran — yet an overly permissive verdict still let the change through. The end-to-end check silently did not happen and the gate failed open, debugged live as `[[harness-debugging]]`.

## Tensions & Tradeoffs

- Coverage vs. cost: end-to-end browser journeys are slower, flakier, and more expensive to run and maintain than unit tests, so they validate the experience at the price of the fast, deterministic feedback `[[agent-tdd]]` relies on per increment — the two operate at different granularities and compose.
- Journey completeness is the new ceiling: satisfaction testing only certifies the journeys someone defined; an unmodeled user path passes silently — the same coverage-gap caveat that bounds `[[self-verification-loop]]`.
- Fail-open risk: the journey test is only a trust signal if it actually executes — when the validation environment is broken the browser run can be skipped while a permissive verdict still approves the change, so the gate must be hardened to fail *closed* (treat an un-runnable check as a failure), a `[[harness-debugging]]` lesson.
- It still rests on the quality of the journey definition — a wrong notion of "satisfied" confidently approves the wrong behavior.
