---
concept: Auto-Correction Loop
category: Harness & Context Engineering
summary: Deterministic gates (linters, type checks, pre-commit hooks) block rule violations and feed errors back to the agent, iterating until the check passes — "success silent, failure loud."
aliases: [auto-correction loop, automatic correction loop, mechanical enforcement, linter-driven correction, lint-fix loop, success silent failure loud]
related: ["[[lifecycle-hooks]]", "[[self-verification-loop]]", "[[harness-engineering]]", "[[agent-tdd]]", "[[deterministic-workflow-orchestration]]"]
sources: [하네스-공식문서-100번-읽은-것처럼-만들어드림]
---

# Auto-Correction Loop

An auto-correction loop is the mechanism by which deterministic gates — linters, type checks, pre-commit hooks — automatically inspect what an AI agent produces, *block* the action when a rule is violated, and feed the error back to the agent so it fixes the code and retries, repeating until the check passes. It is the enforcement half of a harness made dynamic: rather than asking the model nicely to follow the rules, the environment mechanically refuses to let it proceed when it doesn't, turning rule compliance from a request into a precondition.

## Key Mechanics

- Gate-on-action: a check fires automatically when the agent tries to save or commit — a type check, syntax check, or lint pass — and on failure the save/commit itself is blocked.
- Block-and-feedback closes the loop: the blocked action surfaces the error to the agent, the agent rewrites the code, and the gate re-runs, iterating to a clean state without a human in the loop.
- **"Success silent, failure loud."** Only failures emit feedback to the agent; passing checks say nothing. This conserves the agent's attention and context budget, spending signal only where correction is needed.
- Enforcement, not advice: the posture is "violate the rule and you cannot proceed," the mechanical-constraint stance that distinguishes a `[[harness-engineering]]` harness from a prompt. The gates run in the environment (`[[lifecycle-hooks]]`), independent of the model's judgment.

## How It Appears in the Corpus

The 캐슬 (아는 개발자) harness explainer names the automatic enforcement system as the second of three harness pillars: linters and pre-commit hooks mechanically force the agent to follow defined rules, and the linter-detects → agent-self-corrects cycle is called the core mechanism of the whole harness. The "success quietly, failure loudly" principle is given as the efficiency rule that keeps the loop from flooding the agent with noise.

## Tensions & Tradeoffs

- Coverage equals the gates you wired: a check only catches the failure someone thought to encode, so an unguarded failure mode passes silently — the same coverage gap noted for `[[lifecycle-hooks]]`.
- Only as good as the check: passing lint and type checks is not the same as being correct, so a green loop can still ship wrong behavior — the "quality of the check bounds the trust" caveat of `[[self-verification-loop]]`.
- Relationship to `[[self-verification-loop]]`: there the agent *chooses* to run a check before declaring success; here the environment *forces* the check deterministically. The auto-correction loop is more reliable but limited to mechanizable rules, while self-verification can target arbitrary, agent-interpreted success criteria.
- Rigidity: a false-positive or overly strict gate blocks legitimate work, the same flexibility cost as any hard-coded scaffold (`[[deterministic-workflow-orchestration]]`).
