---
concept: Software 3.0
category: Industry, Strategy & Careers
summary: The paradigm shift where writing a prompt is the act of programming, with the pre-trained neural network replacing hand-written code as the medium of software expression.
aliases: [software 3.0, prompt-as-source-code, prompts as programming, prompt as program, neural net as the program]
related: ["[[context-engineering]]", "[[harness-engineering]]", "[[claude-md]]", "[[vibe-coding-vs-agentic-engineering]]", "[[verifiability-law]]", "[[jagged-intelligence]]", "[[agent-native-infrastructure]]"]
sources: [꼭-알아야할-안드레-카파시-30분-인터뷰-완전정리-ai시대의-필수-인사이트]
---

# Software 3.0

Software 3.0 is the paradigm — attributed in the corpus to Andrej Karpathy — in which writing a prompt *is* the act of programming. It is the third step in a progression: Software 1.0 is humans writing explicit code; Software 2.0 is training neural networks (curating datasets and designing model architectures so the learned weights become the program); Software 3.0 is steering a pre-trained model in natural language so the prompt becomes the source code and the neural network performs the information processing that hand-written code used to. The shift is not a speed-up of the old way — it is code *disappearing*, replaced by direct neural-net invocation.

## Key Mechanics

- Three paradigms: 1.0 (write code by hand) → 2.0 (train a net: build the dataset, design the architecture) → 3.0 (write a prompt; the model is the program).
- A single LLM call can stand in for complex code or several app-level services — the corpus cites installing tools and small apps (an "OpenClaude" install, a "MenuGen"-style app) collapsing into one model invocation.
- It is a foundational change in *what software is*, not merely faster authoring: the neural network directly handles the information processing the code formerly encoded.
- A practical diagnostic for builders: when making an app, ask "could this whole thing be a single neural-net call?" — if so, the conventional implementation is the wrong abstraction.

## How It Appears in the Corpus

The Kimflip (김플립) summary of Andrej Karpathy's interview opens with the 1.0/2.0/3.0 taxonomy and frames December 2022 as the inflection point after which agents began running whole workflows. It illustrates Software 3.0 with examples of complex code and multi-service apps being replaced by one LLM call, and urges builders to question whether their app reduces to a single neural-net invocation.

## Tensions & Tradeoffs

- Prompts-as-program inherit the model's `[[jagged-intelligence]]`: a natural-language "source" is non-deterministic and unreliable exactly where the task is hard to verify (`[[verifiability-law]]`), so the surrounding `[[harness-engineering]]` and `[[context-engineering]]` become the reliability layer the disappeared code used to provide.
- It is the substrate beneath the corpus's prompt → context → harness maturity ladder: Software 3.0 makes the prompt the unit of work, while `[[claude-md]]` and harnesses are what make that unit dependable.
- Boundary with `[[vibe-coding-vs-agentic-engineering]]`: Software 3.0 lowers the floor for building, but responsible engineering (security, system correctness) does not vanish with the code — it migrates to human supervision.
