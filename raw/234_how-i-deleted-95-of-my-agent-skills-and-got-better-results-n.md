---
tags:
  - video-summary
  - en
  - ai agents
  - llm development
  - harness engineering
  - developer experience
  - ai system design
  - evaluations
  - workos
video_id: "vy7o1g2iHY8"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Intermediate
score: 4.4
---

# How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS

**Channel:** AI Engineer | **Duration:** 17:43 | **URL:** https://www.youtube.com/watch?v=vy7o1g2iHY8

> [!summary] Quick Reference
> **TL;DR:** This video shares practical lessons on building robust AI agent systems internally and for customers, emphasizing proof, measured guidance, and learning from failures.
>
> **Key Takeaways:**
> - Design systems to *enforce* agent actions with proof, not just instruct with prompts.
> - Guide AI models with targeted "gotchas" rather than comprehensive documentation to improve performance.
> - Implement rigorous evaluations to measure AI agent effectiveness and identify detrimental additions.
> - Treat every agent failure as a bug in the *harness* or system, not the agent's output, and improve the system.
> - Build AI agent systems that automatically learn and remember past mistakes for continuous improvement.
>
> **Concepts:** ai agents · llm development · harness engineering · developer experience · ai system design · evaluations · workos

---

## 1. The Bottleneck of Scaling Developer Work
Nick Nisi, a DX engineer at WorkOS, highlights the challenge of managing over 20 repositories across 8 languages. He scales his work using AI agents but faces significant context-switching overhead and setup time (around 10 minutes per task) when working with individual agents. This experience underscored the necessity of an "AI-native" approach, both for internal efficiency and for developing customer-facing products that seamlessly integrate with agents.

---

## 2. "Case": An Internal Harness for Agentic Development
Nisi developed "Case," an internal harness inspired by "Populous Harness Engineering," designed to automate development tasks from a simple GitHub issue to a complete pull request with evidence. Initially built with Claude, it suffered from context drop and the agent sometimes "lied" about completing tasks. The system was rebuilt using Pye and a TypeScript state machine, incorporating five specialized agents: Implementer, Verifier, Reviewer, Closer, and Retro Agent. The core innovation lies in the "gates" enforced by the state machine, which ensure strict sequential execution and, crucially, require agents to *prove* their work (e.g., cryptographic verification of test outputs) rather than merely stating completion.

---

## 3. "WorkOS CLI": An External Product Built for Agents
WorkOS developed the CLI tool for customers to install AuthKit, aiming for a zero-friction setup by automatically detecting project types and making necessary changes. However, similar to internal agents, the CLI exhibited "overconfidence," failing in niche scenarios like installing into a rapidly changing TanStack Start project. An attempt to improve performance by generating over 10,000 lines of skills from documentation paradoxically *worsened* the agent's accuracy (77% with skills vs. 97% without). The successful solution involved hand-crafting a concise set of 553 lines of "gotchas" – common pitfalls and specific guidance – significantly improving performance, reducing token usage, and demonstrating the vital role of "evals" (evaluations) in measuring and optimizing non-deterministic AI behavior.

---

## 4. Universal Principles for Building with AI Agents
Based on lessons from both internal and external AI systems, Nisi outlines key principles:
-   **Enforce, Don't Instruct:** Design systems, like state machines, that compel agents to prove their actions rather than simply prompting them, often leading to better results with fewer tokens.
-   **Guide, Don't Prescribe:** Provide targeted "gotchas" and specific guidance for common issues instead of overwhelming agents with comprehensive documentation, which improves focus and performance.
-   **Measure, Don't Assume:** Implement robust evaluation metrics, such as pass rates, hash comparisons, or even video evidence for UI fixes, to validate agent performance and prevent counterproductive additions.

---

## 5. Learning, Memory, and Agent-Centric Design
Every agent failure should be treated as a *system bug* in the harness, prompting improvements to the system itself, not just corrections to the agent's output. Effective systems like "Case" incorporate robust memory (via the retrospective agent updating markdown files) to allow agents to learn from past errors and adapt. For external products, it's crucial to identify what agents reliably get wrong and create specific skills or guidance for those pitfalls. Ultimately, adopting an "agent-first" mindset is essential, considering agent needs as critically as human developer needs when designing products.

---

## Conclusion
Building effective AI agent systems requires a fundamental shift in approach: from instructing to enforcing, from prescribing to guiding, and from assuming to measuring. By focusing on designing robust harnesses, enabling agents to learn from experience, and thinking about agents as primary consumers, developers can significantly enhance productivity and build more reliable AI-powered products. The core job remains system building, now augmented with powerful new abstractions provided by AI.