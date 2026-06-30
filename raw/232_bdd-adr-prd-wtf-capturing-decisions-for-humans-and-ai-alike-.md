---
tags:
  - video-summary
  - en
  - decision capture
  - ai agents
  - software development
  - architecture decisions
  - behavior-driven development
  - design systems
  - consistency
  - enforcement loop
video_id: "504PvfXou5Y"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Intermediate
score: 4.2
---

# BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence

**Channel:** AI Engineer | **Duration:** 12:49 | **URL:** https://www.youtube.com/watch?v=504PvfXou5Y

> [!summary] Quick Reference
> **TL;DR:** This video outlines a framework for capturing decisions and ensuring consistency in software development with AI agents using ADRs, PRDs, BDD, design systems, and an
>
> **Key Takeaways:**
> - Document architectural decisions (ADRs) to provide crucial context for future development and AI agents.
> - Use Behavior-Driven Development (BDD) with tools like Cucumber for executable, human-readable specifications.
> - Establish a robust enforcement loop with Git hooks and CI to automate consistency checks and provide immediate feedback.
> - Leverage design systems to define and enforce UI consistency for both human and AI-driven development.
> - Focus agent workflows with "skills" to efficiently apply relevant checks and context for different development tasks.
>
> **Concepts:** decision capture · ai agents · software development · architecture decisions · behavior-driven development · design systems · consistency · enforcement loop

---

## 1. The Challenge of Context in Software Development
Limited context plagues both humans (forgetting) and Large Language Models (LLMs) (no memory), leading to a constant need to re-understand past decisions in evolving products. This issue is significantly amplified when working with AI agents, requiring a structured approach to decision capture.

---

## 2. Capturing Architectural and Product Intent
Architecture Decision Records (ADRs) document the "why" behind architectural choices and how they are enforced, preventing common issues like N+1 queries. Product Requirements Documents (PRDs) offer a lighter approach for features, describing the problem, goal, and user journey, serving as a vital reference for teams and AI agents alike.

---

## 3. Executable Specifications with Behavior-Driven Development (BDD)
Spec-driven development often lacks validation that the product adheres to the specification. BDD, particularly with tools like Cucumber, provides an executable and human-readable layer that describes product behavior. These scenarios can directly link to PRDs and critical user journeys, making tests reviewable, understandable, and closing the specification loop.

---

## 4. Ensuring UI Consistency with Design Systems
Achieving consistent user interfaces remains critical, even with AI agents. Design systems and pattern libraries define UI language, rules (e.g., one primary button per page), components, and usage patterns. This documentation enables automated enforcement of design principles, promotes reuse, and prevents UI inconsistencies and chaos.

---

## 5. Implementing a Robust Enforcement Loop (Harness)
A "harness" or enforcement loop is crucial to ensure both human teams and AI agents adhere to documented decisions and rules. This loop integrates Git hooks, CI/CD, linters, and other automated checks for formatting, type checking, code duplication, and architectural compliance. Automated feedback on rejected commits guides agents back to relevant documentation for iteration and correction.

---

## 6. Dynamic Focus Through Task-Specific Skills
While the core enforcement loop is generic, specific "skills" (e.g., ADR skill, PRD skill, UI skill, Test skill) provide dynamic focus for agents based on the task at hand. These skills help agents efficiently look up relevant context, apply appropriate checks, and optimize operations (e.g., running focused test suites), even in context-heavy environments.

---

## Conclusion
Capturing decisions through ADRs, PRDs, and executable BDD specifications, supported by design systems and a robust enforcement loop, is essential for building consistent and maintainable products, especially when integrating AI agents. This structured approach ensures that both humans and AI operate with the necessary context and guidance to maintain quality and avoid common development pitfalls.