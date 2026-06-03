---
concept: Reasoning Effort Control
category: Workflows & Methodology
summary: Dialing the model's per-prompt thinking budget up for hard tasks and down for simple ones — concentrating deep reasoning where it pays and economizing tokens everywhere else.
aliases: [reasoning effort control, ultra think, thinking budget, per-prompt reasoning, effort dialing, extended thinking control, output verbosity control]
related: [token-maxing, per-node-model-routing, plan-first-workflow, context-reset, explicit-gears, verifiability-law]
sources: [7-secret-prompts-that-make-claude-code-10x-better]
---

# Reasoning Effort Control

Reasoning effort control is the operator discipline of explicitly setting *how much* a model thinks on a given prompt — instructing it to apply maximum reasoning on a hard, technical task while leaving everyday prompts at a lighter default — so deep deliberation is concentrated where correctness matters and token spend is conserved everywhere else. It is the *within-model* analogue of routing decisions made *across* models: where `[[per-node-model-routing]]` swaps a stronger model in for a difficult step, reasoning effort control turns the same dial inside one model, raising its thinking budget for the prompts that earn it.

## Key Mechanics

- **Per-prompt effort override**: a trigger (the corpus's instance is an "ultra think" instruction) tells the model to spend more time reasoning on *this* query regardless of the session's default effort setting — a deliberate, local escalation rather than a global one.
- **Match effort to difficulty**: the payoff is selective — reserve maximum reasoning for complex or technical prompts and let simple, routine ones run cheaply, so the deep-thinking budget is not wasted on tasks that do not need it.
- **Output-side counterpart lever**: trimming the model's *output* verbosity (the corpus cites a `/caveman` skill that shortens responses) is the complementary token control — effort control governs how much the model *thinks*, verbosity control governs how much it *writes*, and both are knobs on the same per-prompt token bill.
- **Cost is the motivation**: the explicit framing is token economy — spend reasoning tokens on the prompts where deeper thought changes the answer, and save them on the ones where it would not, which matters most on lower-tier or metered plans.

## How It Appears in the Corpus

The Sabrina Ramonov "7 Secret Prompts" tutorial presents "ultra think" as a command that makes the model apply its maximum reasoning effort to a specific complex prompt while letting simpler everyday prompts run at lower effort to save tokens, and pairs it with a `/caveman` skill that reduces output length — together framing per-prompt reasoning and verbosity as deliberate, dialable token levers rather than fixed settings.

## Tensions & Tradeoffs

- **Reconciles with `[[token-maxing]]` by being selective**: token-maxing argues it is expensive *not* to burn tokens on high-value work, while effort control says dial *down* on low-value work — they agree once read as "spend reasoning where it pays," the same capability-based reconciliation `[[per-node-model-routing]]` reaches.
- **Operator must judge difficulty up front**: the lever only helps if the operator correctly anticipates which prompts need deep reasoning; under-dialing a deceptively hard task silently degrades the answer, the same misrouting risk `[[per-node-model-routing]]` carries.
- **More thinking is not more correctness**: extra reasoning effort raises the *chance* of a good answer but does not guarantee it — on tasks without a clean check (`[[verifiability-law]]`), a confidently-wrong result can still emerge, so effort control is a quality lever, not a verifier.
- **A knob, not a workflow**: it tunes a single call, complementing structural moves like `[[plan-first-workflow]]` (route the plan to deep reasoning, execution to less) and `[[explicit-gears]]` (switch the *kind* of thinking), which decide *when* deep reasoning belongs rather than merely turning it on.
