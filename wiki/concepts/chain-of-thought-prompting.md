---
concept: Chain-of-Thought Prompting
category: Workflows & Methodology
summary: Prompting the model to spell out its reasoning step by step before answering, which consistently improves results — genuine reasoning scaffolding, not a mere computational placeholder.
aliases: [chain of thought, CoT, chain-of-thought prompting, think step by step, reasoning elicitation, show your work]
related: ["[[prompt-engineering]]", "[[reasoning-effort-control]]", "[[verifiability-law]]", "[[self-verification-loop]]", "[[theory-of-mind-for-llms]]"]
sources: [ai-prompt-engineering-a-deep-dive]
---

# Chain-of-Thought Prompting

Chain-of-thought (CoT) prompting is the technique of instructing a model to explain its reasoning step by step — to "show its work" — before or while producing its answer, which consistently improves the quality of that answer. The corpus's panelists are explicit that this is *more than a computational placeholder*: the externalized reasoning genuinely helps the model arrive at better conclusions, so eliciting it is a real lever on output quality rather than a cosmetic trace. It is one of the most durable techniques in `[[prompt-engineering]]`, even as its most explicit forms get absorbed into model training.

## Key Mechanics

- **Ask for the reasoning**: prompting the model to lay out intermediate steps, rather than jump straight to a conclusion, reliably raises answer quality on tasks that benefit from deliberation.
- **Not just a placeholder**: the improvement is attributed to the reasoning itself doing work, not merely to spending extra tokens — making CoT a substantive technique, not a formatting trick.
- **Increasingly internalized**: early explicit instructions like "think step by step" (notably for math) have been trained directly into models, so models now often reason this way by default — a concrete instance of the technique-obsolescence dynamic in `[[prompt-engineering]]`.
- **An output-structure lever**: CoT shapes *how the answer is produced* (visible, staged reasoning), distinct from dialing *how much* the model deliberates.

## How It Appears in the Corpus

The Anthropic "AI prompt engineering: A deep dive" panel cites Chain of Thought — having the model explain its reasoning — as consistently improving results and stresses that it is more than a computational placeholder. It also uses explicit "think step-by-step" instructions as the canonical example of an early hack that has since been trained into models, illustrating why the best *specific* techniques tend to be short-lived.

## Tensions & Tradeoffs

- **Distinct from `[[reasoning-effort-control]]`**: effort control turns a *quantity* dial on how much the model thinks per prompt; CoT is an *output-structure* technique that makes the reasoning explicit. They compose — you can both raise the thinking budget and ask the model to externalize the result.
- **Technique fading, principle enduring**: explicit CoT instructions grow less necessary as models internalize the behavior, but the underlying principle — externalized reasoning improves answers — persists even when it no longer needs prompting.
- **More reasoning ≠ guaranteed correctness**: visible step-by-step reasoning raises the *chance* of a good answer but does not certify it; on tasks without a clean check (`[[verifiability-law]]`) a confidently-wrong chain can still emerge, so CoT pairs with, not replaces, a `[[self-verification-loop]]`.