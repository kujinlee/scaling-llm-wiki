---
tags:
  - video-summary
  - en
  - ai agents
  - llm development
  - software engineering
  - agent challenges
  - api design
  - evaluations
  - deepmind
video_id: "3_gYbhABcAE"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Intermediate
score: 4.4
---

# Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind

**Channel:** AI Engineer | **Duration:** 10:40 | **URL:** https://www.youtube.com/watch?v=3_gYbhABcAE

> [!summary] Quick Reference
> **TL;DR:** This video explains five key differences and paradigm shifts engineers face when building AI agents compared to traditional software development.
>
> **Key Takeaways:**
> - Embrace text as the primary state to capture semantic meaning dynamically.
> - Delegate control to LLMs; design for adaptive, non-deterministic workflows.
> - Treat agent errors as inputs to enable recovery and preserve context.
> - Shift from deterministic unit tests to evaluations for agent reliability.
> - Design self-documenting APIs explicitly for agent comprehension and use.
>
> **Concepts:** ai agents · llm development · software engineering · agent challenges · api design · evaluations · deepmind

---

## 1. Text is the New State
Traditionally, software relied on structured data, booleans, and flags. However, with agents, text (and other context like images, audio) has become the primary state representation. This allows agents to understand semantic meaning dynamically, enabling more flexible responses, like approving a research plan with additional custom instructions or handling user preferences (e.g., Celsius vs. Fahrenheit) based on conversational context rather than predefined flags.

---

## 2. Handing Over Control to Agents
Building agents requires a shift from strictly deterministic, predefined workflows (like a customer support intent classification leading to a fixed script). Instead, developers must trust the LLM to understand dynamic meaning and react adaptively. Agents can offer unexpected solutions or change direction based on evolving user intent, making it impossible to model all unique scenarios with traditional stateful workflows.

---

## 3. Treating Errors as Normal Inputs
Unlike traditional software where re-running a failed HTTP request is cheap, agent workflows can be long (5-15 minutes) and resource-intensive. Restarting upon failure is inefficient and leads to loss of context. Therefore, errors must be treated as regular inputs to the agent model, prompting it to recover, find workarounds, or continue the flow rather than simply failing or restarting from scratch.

-----