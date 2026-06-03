---
concept: Exploratory Spec Discovery
category: Workflows & Methodology
summary: Pointing an agent at a verifiable goal on a throwaway branch, letting it explore until the goal is reached, then distilling the lessons into a clean spec for proper re-implementation.
aliases: [exploratory spec discovery, scrappy branch then respec, discover a spec, goal-driven exploration, exploratory goal autonomy, spec discovery through exploration]
related: [spec-driven-development, hill-climbing, self-verification-loop, ai-garbage-collection, reward-hacking, auto-research, deterministic-workflow-orchestration]
sources: [한글자막-현재-codex-에서-제일-핫한-기능-goal]
---

# Exploratory Spec Discovery

Exploratory spec discovery is the workflow of pointing a long-running autonomous agent at a *verifiable goal* whose solution shape is unknown, letting it explore and self-test on a throwaway "scrappy branch" until it hits the goal, and then distilling the lessons of that run into a clean specification that is re-implemented properly. It is the deliberate inverse of `[[spec-driven-development]]`: rather than writing the design up front and gating implementation behind it, the agent's exploration *produces* the spec that could not have been written in advance — turning open-ended problems (performance optimization, cross-platform feature parity) into a discovered, then formalized, design.

## Key Mechanics

- **Verifiable goal, not a vague wish**: the objective must be checkable either by completing a predefined plan or by hitting a concrete metric (e.g. "reduce P95 latency by 20%"). A vague goal like "make this better" has no termination condition and drives indefinite, token-burning execution — so the recommended first step is to brainstorm *with* the agent to sharpen the goal before launching it.
- **Anti-proxy-signal discipline**: the agent is instructed to "not accept proxy signals" and to "treat uncertainty as not achieved" — a built-in guard against declaring victory on a measurement that merely correlates with success, the harness-level defense against the failure mode named in `[[reward-hacking]]`.
- **Exploratory vs. well-defined split**: the pattern is reserved for *exploratory* work where the final solution is unknown and iteration is required, as opposed to *well-defined* tasks whose solution is predictable and better served by a direct plan.
- **Surface drives effectiveness**: the goal is only as solvable as the resources the agent can act on — real logs, staging environments, cost data, the codebase, flame graphs, existing metrics. Effectiveness is proportional to this actionable "surface," so feeding rich context is the main lever on success.
- **Scrappy branch, then re-spec**: the exploratory run is treated as disposable. Once the goal is reached, the discovered solution and lessons are distilled into a clean spec/PRD and re-implemented, so the explored hacks never become the shipped code.
- **Operational controls**: long runs are managed with pause/resume/clear and inspected for current objective and token usage; side threads let the operator ask questions without derailing the main goal; dangerous or resource-heavy goals are isolated (e.g. run in a VPS).

## How It Appears in the Corpus

The Tech Bridge tutorial on OpenAI Codex's `/goal` command presents exactly this pattern: enabling `features.goals` lets a user hand Codex a verifiable objective, which it pursues by mapping the repo, exploring solutions, and self-testing until the goal is met. The video stresses that goals must be verifiable ("do not accept proxy signals," "treat uncertainty as not achieved") or execution runs indefinitely, that effectiveness scales with the resources/surface provided, and — most distinctively — that the right way to use it for exploratory work is as a "scrappy branch" whose result is then distilled into a clean specification and re-implemented, letting the agent "discover a spec" that could not be written up front.

## Tensions & Tradeoffs

- **Codebase contamination**: an exploring agent leaves behind debug prints, random hacks, and "scar tissue." Treating the run as disposable and re-implementing from the distilled spec is the mitigation, and the cleanup it implies is the same entropy-fighting motive as `[[ai-garbage-collection]]` — the difference is that here contamination is *expected* and quarantined to a throwaway branch rather than pruned in place.
- **Inverse of `[[spec-driven-development]]`, not a replacement**: spec-driven development front-loads design to avoid rework; exploratory spec discovery accepts a messy first pass *because* the design is not yet knowable, then feeds back into a spec-driven re-implementation. The two compose as a loop — discover, then build properly — rather than competing.
- **Verifier quality bounds the result**: like `[[hill-climbing]]` and `[[auto-research]]`, the loop optimizes exactly what its goal encodes; the anti-proxy-signal rule hardens this but cannot rescue a goal that verifies the wrong thing. A confidently "achieved" goal can still be the wrong goal.
- **Cost and runtime exposure**: long-running, exploratory autonomy consumes large amounts of tokens and time, so a poorly scoped or unverifiable goal is expensive as well as unbounded — making up-front goal refinement and isolation (VPS) practical necessities, not niceties.
