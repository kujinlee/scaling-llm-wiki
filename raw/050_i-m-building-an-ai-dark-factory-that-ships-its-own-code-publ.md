---
tags:
  - video-summary
  - en
  - ai coding
  - dark factory
  - autonomous software
  - arkon workflows
  - generative ai
  - software engineering
  - agentic development
video_id: "6woc6ii-zoE"
channel: "Cole Medin"
lang: EN
type: Framework
audience: Advanced
score: 4.8
---

# I'm Building an AI Dark Factory That Ships Its Own Code (Public Experiment)

**Channel:** Cole Medin | **Duration:** 25:12 | **URL:** https://www.youtube.com/watch?v=6woc6ii-zoE

> [!summary] Quick Reference
> **TL;DR:** This video details building a "Dark Factory," an autonomous AI coding system managing its entire codebase lifecycle, aiming for fully human-free software development and deployment.
>
> **Key Takeaways:**
> - Autonomous AI coding progresses through levels, with "Dark Factory" representing fully human-free development.
> - A governance layer (mission, rules, global context) is vital to guide and constrain AI's self-coding efforts.
> - Arkon workflows enable a continuous loop of AI-driven issue triage, implementation, and validation.
> - The "holdout pattern" uses an independent validation agent to prevent AI bias and ensure reliable code.
> - Focus validation on end-to-end user journeys using browser automation for true satisfaction testing.
>
> **Concepts:** ai coding · dark factory · autonomous software · arkon workflows · generative ai · software engineering · agentic development

---

## 1. Introduction to the Dark Factory Experiment
This video details a public experiment to build a "Dark Factory" – an autonomous AI-driven coding system that manages an entire codebase lifecycle without human intervention. The speaker aims to push the limits of AI coding assistance, taking inspiration from "lights out manufacturing." The ultimate goal is to create a system where AI handles planning, implementing, pushing changes, and pull requests directly to production. The underlying application being built by this dark factory is an agentic, RAG-powered AI tutor that answers questions based on the speaker's YouTube content.

---

## 2. The Evolution of AI Coding Autonomy
The video draws a compelling analogy between the levels of self-driving cars and the progressive use of generative AI in coding. It outlines five levels:
*   **Level 0: Spicy Autocomplete:** AI as a reference tool or enhanced search, like a smarter Stack Overflow, with the developer manually writing code.
*   **Level 1: Coding Intern:** AI handles basic or boilerplate code, akin to cruise control.
*   **Level 2: Junior Developer:** An interactive pair programmer partnership where AI assists with tasks, but developers still write some code.
*   **Level 3: Developer (Human-in-the-Loop):** AI generates the majority of the code, but human review is mandatory for every plan and code piece before shipping to production. This is recommended for reliable production-grade software.
*   **Level 4: Harness (Overnight Work):** AI runs unattended tasks for long periods using frameworks like Anthropic's Relf loop, with humans reviewing final results much later.
*   **Level 5: Dark Factory:** The ultimate stage where AI defines implementation, writes, tests, fixes bugs, and ships to production with no human review before merging, making it a truly autonomous system.

---

## 3. The Governance Layer: Guiding the AI
For the Dark Factory to operate effectively and align with its mission, a robust "governance layer" is crucial. This layer acts as the console for high-level instructions, comprising three key markdown files:
*   `mission.md`: Outlines the application's purpose, scope (in and out of scope features for the AI tutor app), and boundaries, ensuring the AI builds only what's intended.
*   `factory_rules.md`: Dictates the operational procedures, including issue triaging, label systems, implementation requirements (e.g., concise pull requests, mandatory testing), and quality gates for auto-merging.
*   `claw.md`: Provides global rules regarding the tech stack, repository layout, testing commands, and code conventions, offering the AI comprehensive codebase context.
These three files are loaded into context for every workflow, ensuring the system consistently understands its mission and operational guidelines.

---

## 4. The Factory Loop: Arkon Workflows in Action
The entire Dark Factory operation revolves around a continuous loop managed by Arkon, an open-source harness builder for deterministic and repeatable AI coding workflows. The loop consists of:
*   **Entry Point (GitHub Issue):** An issue is created either manually or by the Dark Factory itself (e.g., from regression testing).
*   **Triage Workflow:** A scheduled Arkon workflow fetches recent issues, uses an AI agent (Claude Code routed to MiniMax M2.7 for cost-efficiency) to classify and prioritize them based on `mission.md` and `factory_rules.md`, and applies labels (accepted/rejected, priority).
*   **Implement Workflow:** For each accepted issue, a separate Arkon workflow is kicked off in parallel. This elaborate workflow includes research, classification (bug fix or new feature), planning, implementation, creating a pull request, and parallel validation.
*   **Validation Workflow:** This crucial separate workflow ensures reliability and prevents AI sycophancy by following the "holdout pattern." A dedicated validation agent is given the user journey and code diffs but no context from the development process, minimizing bias. It performs comprehensive end-to-end testing with browser automation to ensure the user experience is correct.
Upon successful validation, the code is theoretically confident enough to be merged directly into the main branch without human approval, creating a continuous autonomous development cycle.

---

## 5. Ensuring Reliability: The Holdout Pattern
To counter common AI problems like sycophancy and bias, the speaker implements the "holdout pattern" for validation, a technique inspired by StrongDM. This involves a strict separation between the implementation and validation agents. The validation agent is provided only with the user journey/fix and the exact code diffs, deliberately withholding any context from the development process. This prevents the validation agent from developing a bias towards the implementation agent's work or lazily rewriting tests to match flawed code. Instead of just unit tests, the system focuses on "satisfaction testing" entire user journeys using browser automation, ensuring real-world functionality and user experience are correctly handled without human review.

---

## Conclusion
The Dark Factory experiment represents a significant step towards truly autonomous software development, demonstrating what's possible when AI takes full control of a codebase. By meticulously defining a governance layer and leveraging Arkon workflows for a continuous triage-implement-validate loop, the speaker is building a system designed for reliability and efficiency. The ongoing public experiment, including a deployable application for public testing and issue submission, promises to offer unprecedented insights into the future of AI-driven software engineering.