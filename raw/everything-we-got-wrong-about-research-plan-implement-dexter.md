---
tags:
  - video-summary
  - en
  - coding agents
  - llm workflows
  - instruction budget
  - prompt engineering
  - developer productivity
  - crispy framework
  - rpi methodology
video_id: "YwZR6tc7qYg"
channel: "MLOps.community"
lang: EN
type: Analysis
audience: Advanced
score: 4.4
---

# Everything We Got Wrong About Research-Plan-Implement -  Dexter Horthy

**Channel:** MLOps.community | **Duration:** 26:46 | **URL:** https://www.youtube.com/watch?v=YwZR6tc7qYg

> [!summary] Quick Reference
> **TL;DR:** This video explains evolving AI coding agent workflows, stressing LLM instruction limits, human code ownership, and modular planning for reliable productivity.
>
> **Key Takeaways:**
> - LLMs have an instruction budget; exceeding it causes inconsistent adherence and poor results.
> - Human developers must read and own generated code for production quality and professional standards.
> - Break down monolithic prompts into smaller, focused prompts (<40 instructions) for better LLM adherence.
> - Use artifacts like Design Discussions and Structure Outlines for early human-agent alignment and architectural review.
> - Prioritize "vertical plans" with checkpoints over horizontal plans for easier debugging and integration.
>
> **Concepts:** coding agents · llm workflows · instruction budget · prompt engineering · developer productivity · crispy framework · rpi methodology

---

## 1. Initial RPI Methodology & Its Flaws
The original "Research Plan Implement" (RPI) methodology aimed to boost AI developer productivity. Early findings by Eigor showed that while RPI increased shipping speed by 50%, half of that was rework due to "slop." RPI was effective for low-complexity, greenfield tasks but struggled with high-complexity, brownfield projects. Key initial "rights" included avoiding "magic prompts," not outsourcing thinking, and seeking leverage. However, the original RPI promoted not reading the code and relying on long plan files, which proved problematic.

---

## 2. Unpacking the Problems: Research, Plans, and "Magic Words"
*   **Poor Research**: Engineers struggled to get objective research. If told "what to build," the model would generate opinions rather than pure facts about the codebase. Good research requires specific questions to extract objective truths.
*   **Suboptimal Plans**: The planning phase used a single, monolithic prompt with 85+ instructions. This often led to the model skipping crucial steps like presenting design options or getting user feedback, resulting in plans that didn't align with user intent.
*   **The "Magic Words" Conundrum**: Users often had to include specific phrases like "work back and forth with me" to get the desired interactive planning behavior, indicating a flaw in the tool's design rather than user error.

---

## 3. The Instruction Budget and The "Read The Code" Realization
A major revelation was the concept of an "instruction budget." Frontier LLMs can consistently follow only 150-200 instructions. Prompts with too many instructions (e.g., 85+ in a single planning prompt, plus system prompts and tools) lead to inconsistent adherence. The presenter admitted a previous error in advocating *against* reading the code. After six months, this approach led to significant rework and system replacements. For production-grade, regulated, or user-facing code, reading and owning the code is crucial to uphold professional standards and avoid "slop." The goal is 2-3x speedup with human-level quality, not 10x faster "slop."

---

## 4. Introducing Crispy: A Refined Workflow
The RPI methodology evolved into "Crispy" (Questions, Research, Design, Structure, Outline, Plan, Work, Implement, PR) by breaking down the monolithic prompts and steps. The planning phase is now split into separate, smaller prompts for "Design Discussion," "Structure Outline," and "Plan." Each prompt has fewer than 40 instructions, greatly improving adherence. This approach uses "control flow for control flow" (e.g., if statements) to classify input and feed it to specialized, focused prompts, rather than relying on a single, overburdened prompt. The "dumb zone" concept for context windows (degrading results beyond 40% usage) remains relevant for new users, emphasizing smaller, more focused contexts.

---

## 5. Achieving Leverage Through Human-Agent Alignment
*   **Design Discussion (200 lines)**: A key new artifact where the agent brain-dumps its understanding of the problem, desired end state, patterns to follow (allowing human correction of bad patterns), resolved decisions, and open questions. This forces early human-agent alignment and allows "brain surgery" on the agent's approach *before* code is written.
*   **Structure Outline (2-ish pages)**: This artifact provides a high-level overview of development phases, the order of changes, and testing strategies. It serves as a "C header file" for the code, allowing review of the agent's architectural thinking.
*   **Vertical Plans**: The new workflow encourages "vertical plans" (e.g., mock API, then frontend, then service, then database) with checkpoints for testing, in contrast to "horizontal plans" (all database, then all service, etc.) which are harder to debug.
*   **Team Collaboration**: These shorter, focused documents (design and outline) facilitate early team review, reducing rework and speeding up code reviews significantly, mirroring a strong team's architecture review process.

---

## Conclusion
The evolution from RPI to Crispy represents a significant learning curve in building robust AI coding agent workflows. Key takeaways include respecting the instruction budget of LLMs, the critical importance of human oversight (reading and owning the code), and leveraging modular, interactive artifacts (design discussions, structure outlines) to achieve deep human-agent alignment and better team collaboration, ultimately leading to more reliable 2-3x productivity gains rather than fast but sloppy output. The field continues to iterate and refine best practices for integrating AI into the software development lifecycle.