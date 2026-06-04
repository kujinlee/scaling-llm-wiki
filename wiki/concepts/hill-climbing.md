---
concept: Hill Climbing
category: Workflows & Methodology
summary: Giving an agent a concrete metric and a verification mechanism, then letting it iterate autonomously toward the target with anti-proxy-signal discipline to prevent false completion.
aliases: [metric-driven iteration, agent optimization loop]
related: ["[[self-verification-loop]]", "[[agentic-issue-resolution]]", "[[shifting-bottlenecks]]", "[[exploratory-spec-discovery]]", "[[reward-hacking]]", "[[generator-verifier-loop]]", "[[verifiability-law]]"]
sources: [live-coding-session-with-boris-cherny-and-jarred-sumner, 한글자막-현재-codex-에서-제일-핫한-기능-goal, claude-code-just-dropped-goal-master-it-in-8-minutes]
---

# Hill Climbing

Hill climbing is the technique of giving an agent a concrete target metric together with a mechanism to verify its own results, then letting it iterate autonomously until the target is met. Because the agent can measure each attempt, it can improve step by step toward a performance goal without human guidance at each iteration.

## Key Mechanics

- Two ingredients: (1) a well-defined metric to optimize, and (2) a verification mechanism the agent can run to check progress.
- The agent loops — try, measure, adjust — climbing toward the goal; this is what lets a single objective be pursued to completion unattended.
- Combined with cheap parallelism, many agents can hill-climb concurrently on the same or related goals.
- The goal must be genuinely *verifiable* — completable as a plan or measurable against a metric — or the loop never terminates; a vague target ("make this better") has no stopping condition and runs indefinitely.
- Anti-proxy-signal hardening: a robust hill-climb instructs the agent to reject proxy signals and "treat uncertainty as not achieved," so it does not declare victory on a measurement that merely correlates with the real goal.
- The verifier can be a *separate agent*: rather than the climbing agent self-scoring, a dedicated supervisor judges each step against the goal — the `[[generator-verifier-loop]]` productization of the same try-measure-adjust cycle.

## How It Appears in the Corpus

In the Boris Cherny and Jarred Sumner session, hill climbing is presented as the engine behind agents independently building complex components for Bun — for example an image-processing library and an HTTP/3 server — by iterating against measurable performance targets. It depends on the `[[self-verification-loop]]` for its feedback signal.

The Tech Bridge tutorial on OpenAI Codex's `/goal` command is a concrete productized hill-climb: the agent maps the repo, explores, and self-tests until a verifiable objective (e.g. "reduce P95 latency by 20%") is achieved, with explicit "do not accept proxy signals" / "treat uncertainty as not achieved" guardrails and the warning that vague goals run forever. Its distinctive extension — climbing toward a goal whose *solution shape* is unknown and then distilling the result into a spec — is treated as `[[exploratory-spec-discovery]]`.

The Tristen O'Brien tutorial on Claude Code's `/goal` command shows the same hill-climb with the verification role split into a second agent: a *worker* iterates while a *boss* agent checks "is the goal met?" after every step and continues until a verifiable finish line is reached — the `[[generator-verifier-loop]]` form of metric-driven iteration. It reiterates that the finish condition must be specific and verifiable or the loop wastes tokens, and adds a *safety cap* (a turn or time limit) as a hard stop against a runaway climb.

## Tensions & Tradeoffs

- Only as good as the metric: hill climbing optimizes exactly what is measured, so a poorly chosen or gameable metric yields the wrong result confidently — the failure mode generalized in `[[reward-hacking]]`, which the anti-proxy-signal discipline is the harness-level defense against.
- Requires a trustworthy verifier — goals without an automatable check cannot be hill-climbed, and an unverifiable goal turns autonomous iteration into an unbounded, token-burning run that a safety cap (`[[generator-verifier-loop]]`) can only blunt, not fix.
