---
concept: In-Context Learning
category: Workflows & Methodology
summary: Steering a foundation model's behavior at inference time by including zero, one, or a few input/output examples in the prompt — teaching the task through demonstration rather than weight updates.
aliases: [in-context learning, ICL, few-shot prompting, one-shot prompting, zero-shot prompting, few-shot learning, learning from examples, prompt examples, shot-based prompting]
related: [prompt-engineering, chain-of-thought-prompting, foundation-models, model-adaptation-methods, collaborative-prompt-elicitation, escape-hatch-prompting, automated-prompt-optimization]
sources: [introduction-to-vertex-ai-studio]
---

# In-Context Learning

In-context learning is the technique of teaching a foundation model a task *at inference time* by placing examples of the desired behavior directly in the prompt, rather than changing the model's weights. The number of worked examples supplied defines a spectrum: **zero-shot** gives the model only a task description and no examples; **one-shot** supplies a single input/output example; and **few-shot** supplies a small handful. The model infers the pattern from the demonstrations and applies it to the new input — so the *prompt itself* carries the specialization that fine-tuning would otherwise bake into parameters. It is the cheapest, fastest rung of `[[model-adaptation-methods]]`: no training run, no dataset pipeline, just examples assembled into the context window.

## Key Mechanics

- **The prompt's three parts**: an effective prompt decomposes into an *input* (the core request — a question, a task, or an entity to operate on), *context* (instructions that guide the model's behavior, set its role, or scope its responses), and *examples* (input/output pairs demonstrating the desired response format). The examples are what turn a bare instruction into few-shot learning.
- **The shot spectrum**: zero-shot relies entirely on the model's pretrained knowledge plus a task description; one-shot anchors the format with a single demonstration; few-shot supplies several, sharpening both the task semantics and the exact output shape. More shots generally improve adherence to the desired format, at the cost of more context-window tokens.
- **Examples pin down format, not just task**: a recurring payoff is that demonstrations fix the *response structure* (length, fields, style) far more reliably than a prose description of it — the model imitates the shape it was shown.
- **Convert generation into classification**: a cited best practice is to reframe an open-ended generative task as a constrained classification task where possible, narrowing the model's output space so it is easier to steer and verify.
- **One task at a time, concisely**: prompts work best when they are specific, define a single task, and stay concise — overloading one prompt with multiple tasks degrades adherence, the in-context-learning face of the broader instruction-load limit.

## How It Appears in the Corpus

The Google Cloud "Introduction to Vertex AI Studio" tutorial presents prompt design as the primary lever for eliciting good responses from foundation models like Gemini Multimodal. It defines the anatomy of a prompt (input, context, examples) and the zero-shot / one-shot / few-shot methods, noting that Vertex AI Studio offers a "structured mode" for assembling few-shot input/output pairs. Its best practices — be concise and specific, define one task at a time, turn generative tasks into classification tasks, and include examples — frame example-driven prompting as the route to higher-quality output, with experimentation as the way to find the optimal prompt.

## Tensions & Tradeoffs

- **Cheapest adaptation, shallowest reach**: in-context learning specializes a model with zero training cost, but it only reshapes behavior the base model can already approximate — for genuinely new capability or large, private datasets it gives way to the heavier rungs of `[[model-adaptation-methods]]` (parameter-efficient tuning, distillation). It is the no-weight-change end of the same adapt-the-base continuum as `[[foundation-models]]`.
- **Examples cost context budget**: every demonstration consumes window tokens, so few-shot prompting trades context space for adherence — a large example set competes with the actual task for room, the same finite-window pressure that bounds standing context elsewhere.
- **Distinct from `[[chain-of-thought-prompting]]`**: shot-based prompting supplies *examples of the answer*; chain-of-thought supplies *examples or instructions to reason step by step*. They compose — a few-shot prompt can demonstrate worked reasoning — but one teaches the task by demonstration and the other teaches the *process*.
- **Manual examples vs. searched-for prompts**: hand-assembling examples is a human judgment about what demonstrates the task well; `[[automated-prompt-optimization]]` instead searches for high-scoring prompts against a golden set, and `[[collaborative-prompt-elicitation]]` has the model help compose the prompt — in-context learning is the manual, example-first baseline those automate or assist.
- **Vantage caveat**: the framing and the structured-mode/best-practice specifics come from a beginner-oriented vendor tutorial, so they illustrate the *pattern* — adapt behavior by placing examples in the prompt — rather than measured results; the durable idea is example-driven, weight-free specialization, not any one platform's UI.
