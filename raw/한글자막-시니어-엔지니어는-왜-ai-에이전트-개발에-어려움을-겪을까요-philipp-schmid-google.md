---
tags:
  - video-summary
  - en
  - agent development
  - llm agents
  - software engineering
  - prompt engineering
  - api design
  - evaluation
  - deepmind
video_id: "vUL5DWs-hIQ"
channel: "Tech Bridge"
lang: EN
type: Analysis
audience: Intermediate
score: 4.4
---

# [한글자막] 시니어 엔지니어는 왜 AI 에이전트 개발에 어려움을 겪을까요? — Philipp Schmid, Google DeepMind

**Channel:** Tech Bridge | **Duration:** 10:40 | **URL:** https://www.youtube.com/watch?v=vUL5DWs-hIQ

> [!summary] Quick Reference
> **TL;DR:** This video explains five key paradigm shifts for engineers building reliable AI agents, moving from traditional software development to an iterative, trust-based approach.
>
> **Key Takeaways:**
> - Treat text and semantic meaning as the primary state for agent interactions.
> - Hand over control to LLMs, moving beyond deterministic workflows.
> - Design agent systems to recover from errors, rather than restarting.
> - Evaluate agent performance through evals, not just deterministic unit tests.
> - Create agent-ready APIs with clear, self-documenting semantic interfaces.
>
> **Concepts:** agent development · llm agents · software engineering · prompt engineering · api design · evaluation · deepmind

---

## 1. Text is Our New State
Traditionally, software relied on structured data and boolean flags. With agents, semantic meaning derived from text (or other media like images/audio) is the new state. LLMs can understand context and nuances, allowing for dynamic adjustments and rich personalization that couldn't be mapped to fixed data structures previously. We must embrace this shift from clear, structured data concepts to more fluid, context-driven text.

---

## 2. Hand Over Control
Unlike traditional deterministic software with predefined workflows, agents require developers to hand over control to the LLM. Instead of classifying intents and following rigid steps (e.g., in customer support), agents can dynamically react and offer solutions based on deeper understanding. Building agents means trusting the LLM to navigate complex, non-deterministic environments and achieve goals without explicit step-by-step instructions.

---

## 3. Errors Are Just Inputs
In agent flows, errors should be treated as normal inputs, similar to user queries, rather than fatal failures. While traditional software might simply retry cheap HTTP requests, long-running agent processes (5-15 minutes) cannot afford to restart from scratch. Designing for recovery involves feeding errors back to the model, implementing workarounds, and performing additional checks to maintain context and allow the agent to continue progressing through its task.

---

## 4. Move from Unit Tests to Evals
Traditional unit and integration tests assume deterministic outcomes (input A always yields output C). However, agents are non-deterministic; the same input might lead to different steps or results. Therefore, agent evaluation must shift from rigid unit tests to 'evals' that measure reliability and success rate over many runs. Results are often subjective, requiring qualitative feedback, LLM-as-a-judge, or human expert evaluations, focusing on the ultimate outcome rather than intermediate steps.

---

## 5. Agents Evolve, APIs Don't
APIs designed for human developers often assume shared context and long-term expertise. Agents, however, only perceive function schemas and docstrings. To be agent-ready, APIs and tools must be self-documenting and feature semantic interfaces that clearly explain their purpose and usage without relying on human interpretation. This ensures agents can effectively discover and utilize tools without prior knowledge of the underlying code or system.

---

## Conclusion
Building robust AI agents requires a fundamental shift in software development paradigms. Engineers must embrace the non-deterministic nature of LLMs, viewing text as the primary state and designing systems that trust the model, recover gracefully from errors, and are evaluated based on outcomes rather than fixed steps. Crucially, tools and APIs must be explicitly designed for agent consumption, fostering an iterative development process that prioritizes semantic understanding and adaptive behavior over rigid control.