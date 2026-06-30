---
tags:
  - video-summary
  - en
  - ai development
  - llm workflow
  - software architecture
  - test-driven development
  - agile development
  - coding agents
  - prompt engineering
video_id: "-QFHIoCo-Ko"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Intermediate
score: 4.4
---

# Full Walkthrough: Workflow for AI Coding — Matt Pocock

**Channel:** AI Engineer | **Duration:** 1:36:30 | **URL:** https://www.youtube.com/watch?v=-QFHIoCo-Ko

> [!summary] Quick Reference
> **TL;DR:** This video presents a comprehensive AI coding workflow, integrating LLMs with TDD, structured planning, and human oversight for effective software development.
>
> **Key Takeaways:**
> - Keep AI tasks small and clear context regularly to optimize LLM performance and prevent 'dumb zone' issues.
> - Achieve shared understanding with AI using an interactive 'Grill Me' process to clarify requirements before coding.
> - Structure AI development tasks as 'vertical slices' on a Kanban board for early feedback and parallelized implementation.
> - Apply Test-Driven Development (TDD) for AI agents by writing failing tests before generating code for higher quality.
> - Design 'deep modules' with simple interfaces, delegating complex internal implementation to AI, and maintain human QA.
>
> **Concepts:** ai development · llm workflow · software architecture · test-driven development · agile development · coding agents · prompt engineering

---

## 1. Understanding LLM Constraints: Smart Zone & Memento-like Forgetting
---
Large Language Models (LLMs) operate with inherent constraints that developers must understand. A key concept is the **"smart zone"**, where the LLM performs optimally at the beginning of a conversation when attention relationships are least strained. As more tokens are added to the context window, the LLM enters a **"dumb zone"**, leading to degraded performance. The speaker suggests keeping tasks small and within approximately 100K tokens for optimal results.

Another constraint is the LLM's **"Memento-like forgetting"**, meaning it continuously resets to a base state. The speaker prefers to **clear context** rather than compacting (summarizing conversation history) because clearing provides a consistent, fresh start, preventing the accumulation of "sediment" that can also lead to the dumb zone.

## 2. The "Grill Me" Skill: Achieving Shared Understanding
---
The speaker argues against the "specs to code" movement, emphasizing that ignoring the underlying code leads to poor outcomes. Instead, the focus should be on achieving a **"shared understanding"** or **"design concept"** with the AI. This is facilitated by the custom **"Grill Me" skill**, which relentlessly interviews the user about a plan, resolving dependencies and clarifying requirements one question at a time. This interactive, human-in-the-loop process ensures alignment between the developer and the AI agent, creating a robust conversation history that serves as a valuable asset for the design concept.

## 3. From PRD to Parallelized Kanban Boards
---
Following the grilling session, the clarified design concept is formalized into a **Product Requirements Document (PRD)**. This PRD acts as a "destination document," outlining the problem, proposed solution, user stories, and key implementation/testing decisions. While the AI generates this document, the speaker advises against extensive human review, trusting the AI's summarization capability after achieving initial alignment.

The PRD is then translated into a **Kanban board** consisting of independently grabbable issues. A crucial practice here is to structure these issues as **"vertical slices"** (traceable bullets) rather than horizontal layers. This ensures that each task cuts across multiple system layers (e.g., database, API, frontend), providing early and integrated feedback, unlike horizontal slicing which delays testing of the complete flow. This structure also enables **parallelization** of tasks by multiple AI agents.

## 4. AFK Implementation with TDD and Robust Feedback Loops
---
With the Kanban board ready, the development shifts to an **"AFK" (Away From Keyboard) phase**, where AI agents autonomously implement tasks. The speaker advocates for a **Test-Driven Development (TDD)** approach for agents: write a failing test (red), implement the feature to pass the test (green), and then refactor. This method significantly improves the quality of AI-generated tests and code by forcing the AI to instrument the code before writing it.

**Strong feedback loops** (e.g., `npm run test`, `npm run typecheck`) are paramount. The quality of these loops directly determines the ceiling of AI's coding ability. Poor feedback leads to poor AI output. Post-implementation, **manual QA and code review** remain essential for human oversight, taste, and imposing specific coding standards, as completely automating these steps can result in "sloppy" or low-quality applications.

## 5. Structuring Codebases for AI Success: Deep Modules
---
To optimize AI performance and maintain a healthy codebase, the speaker recommends building **"deep modules"** (as described by John Ousterhout). Deep modules expose a small, simple interface while encapsulating a lot of internal functionality. This contrasts with "shallow modules" (many small, highly coupled files) which are difficult for AI to navigate and test. Deep modules improve testability and allow developers to design module interfaces, delegating the complex internal implementation to AI, thereby retaining a high-level understanding of the codebase without needing to review every line of AI-generated code. A custom "improve codebase architecture" skill can help identify and refactor shallow modules into deep ones.

## Conclusion
---
Leveraging AI in software development effectively means integrating it into established software engineering fundamentals rather than treating it as a completely new paradigm. By understanding LLM limitations, fostering shared understanding through structured "grilling" sessions, meticulously planning work into parallelizable vertical slices, and delegating implementation to AFK agents supported by TDD and robust feedback loops, developers can achieve high-quality results. Crucially, human oversight in QA, code review, and architectural design, particularly the emphasis on "deep modules," remains indispensable for maintaining code quality and imposing the necessary human "taste" that AI currently lacks. The process is a collaborative dance between human intentionality and AI automation.