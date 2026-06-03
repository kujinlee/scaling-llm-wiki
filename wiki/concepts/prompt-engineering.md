---
concept: Prompt Engineering
category: Harness & Context Engineering
summary: Clear, iterative communication with an LLM that treats natural language as code — the first stage of the prompt → context → harness maturity ladder, focused on getting one model call to do what you mean.
aliases: [prompt engineering, prompt design, prompting, prompt-as-code, prompt crafting, prompt iteration]
related: [context-engineering, harness-engineering, software-3-0, theory-of-mind-for-llms, chain-of-thought-prompting, escape-hatch-prompting, collaborative-prompt-elicitation, claude-md, reasoning-effort-control]
sources: [ai-prompt-engineering-a-deep-dive]
---

# Prompt Engineering

Prompt engineering is the practice of communicating with a large language model clearly and iteratively to extract the maximum capability from a single call. The "engineering" is the disciplined loop — trial, reset, experiment — applied to natural language as if it were code: with precision, version control, and experimental tracking, embedded in a system that accounts for data sources, latency, and how the prompt fits a larger architecture. It is the foundational, first stage of this corpus's AI-coding maturity ladder — prompt engineering (tune a single output) → `[[context-engineering]]` (curate one agent's window) → `[[harness-engineering]]` (chain many well-contexted calls) — and the act that `[[software-3-0]]` reframes as programming itself.

## Key Mechanics

- **Clear communication plus relentless iteration**: the core skill is articulating intent precisely and then refining through trial and error, exploiting the ability to reset and re-run cheaply — the same prompt rarely lands first try.
- **Natural language as code**: prompts deserve the same care as source — precision of wording, version control, and tracked experiments — rather than being typed ad hoc, because in production a prompt is a component of a larger system (data sources, latency budgets, downstream integration).
- **Anticipate imperfect inputs**: good prompting plans for edge cases and the messy, real-world user inputs the model will actually face, not just the clean case the author imagined.
- **Read the outputs closely**: verifying that the model interpreted instructions as intended — and diagnosing where it didn't — is central, which is the discipline named in `[[theory-of-mind-for-llms]]`.
- **Know when to abandon**: if the model fundamentally "doesn't get it," chasing a "mythical better prompt" is wasted effort; recognizing an unwinnable task is itself a skill.
- **Technique obsolescence**: many early prompting "hacks" (e.g. explicitly instructing "think step by step," see `[[chain-of-thought-prompting]]`) have been trained directly into models, so the *best* specific techniques are often short-lived as models internalize them — while the durable principles (clarity, iteration, output-reading) persist.
- **Trust the model with more**: as models matured, engineers stopped "babying" them or hiding complexity; a notable shift is handing the model an academic paper and instructing it to apply the technique directly rather than painstakingly paraphrasing it — a "respect for the model" as an intelligent, non-human collaborator.

## How It Appears in the Corpus

The Anthropic "AI prompt engineering: A deep dive" panel defines the craft as clear communication akin to understanding the model's "psychology," with the engineering rigor coming from iterative experimentation. It catalogs the traits of a skilled prompter (clarity, willingness to iterate, edge-case anticipation, close output-reading), traces how early techniques get absorbed into model training, and stresses the growing practice of trusting models with full context — up to feeding them primary literature to apply.

## Tensions & Tradeoffs

- **First rung, not the whole ladder**: prompt engineering optimizes a *single* output, so it hits a reliability ceiling on complex work — which is exactly why the corpus stacks `[[context-engineering]]` (what the model knows when you ask) and `[[harness-engineering]]` (enforcement across many calls) on top. A prompt is a *request*; reliability comes from the structure around it.
- **Self-erasing techniques vs. durable principles**: because specific tricks get trained into models, any "best prompt" list dates quickly; the lasting skill is the meta-practice of clear communication and iteration, not a fixed bag of hacks.
- **Persistence vs. abandonment**: investing care in prompts pays off, but there is a point past which no rewording helps — distinguishing "needs another iteration" from "the model can't do this" is judgment the method presupposes.
- **Non-determinism inherited from the model**: treating the prompt as source code runs into `[[software-3-0]]`'s caveat — a natural-language "program" is probabilistic and least reliable exactly where the task is hard to verify, so prompt engineering shades into context and harness engineering precisely where stakes rise.