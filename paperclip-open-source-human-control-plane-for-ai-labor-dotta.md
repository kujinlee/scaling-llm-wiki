---
tags:
  - video-summary
  - en
  - ai agents
  - agent orchestration
  - open-source
  - workflow automation
  - llm applications
  - developer tools
  - organizational ai
video_id: "h403btjldDQ"
channel: "AI Engineer"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa

**Channel:** AI Engineer | **Duration:** 24:34 | **URL:** https://www.youtube.com/watch?v=h403btjldDQ

> [!summary] Quick Reference
> **TL;DR:** This video introduces Paperclip, an open-source AI agent orchestrator acting as a human control plane to manage AI organizations for business tasks.
>
> **Key Takeaways:**
> - Get started by running `NPX Paperclip AI onboard` in your terminal to initialize the system.
> - Design an organizational chart, assigning specific roles, skills, and preferences to your AI agents.
> - Implement QA agents and routines to ensure consistent, reliable work output and automate tasks.
> - Provide detailed instructions and regular feedback to agents for high-quality, expected results.
> - Manage costs by tracking spending and integrating cheaper AI models for less critical tasks.
>
> **Concepts:** ai agents · agent orchestration · open-source · workflow automation · llm applications · developer tools · organizational ai

---

## 1. Introducing Paperclip: The AI Agent Orchestrator
Paperclip is an open-source agent orchestrator designed as a "human control plane for AI labor," aiming to enable "zero-human companies." It allows users to establish an organizational chart of AI agents, manage their operations, and imbue them with specific preferences and 'taste' to accomplish real-world tasks. Unlike fully automated solutions, Paperclip integrates human oversight at key stages, from high-level design to execution.

---

## 2. Getting Started and Real-World Application
To begin with Paperclip, users simply run `NPX Paperclip AI onboard` in their terminal. The video demonstrates Paperclip by showcasing its use in managing the Paperclip project itself. This involves a CEO agent, CTO, multiple coders (e.g., Codex, Claude), and a marketing organization. A key feature is "bring your own agent," allowing integration of various models like Gemini, Pi, or Hermes. The speaker illustrates this with a use case: celebrating 40,000 GitHub stars by having the CEO agent hire a video writer, who then, using specialized skills (like Remotion best practices) and existing brand context, creates an animated video in minutes, significantly faster than manual processes.

---

## 3. Core Features: Organization, Workflows, and Skills
Paperclip’s architecture is built around an organizational chart where users configure and assign tasks to agents. It emphasizes reliability through advanced workflows:
*   **Quality Assurance (QA):** Agents with `agent browser` skills can test work. Tasks can be configured to require reviewer or approver roles, ensuring agents complete instructions reliably, overcoming common challenges of inconsistent agent behavior across different models.
*   **Routines:** Users can define reusable, templated tasks that run on schedules or manually, such as generating release notes or processing pull requests. These routines can integrate specific skills, like using Greptile for automated code reviews, providing a structured approach to common operations.

---

## 4. Beyond Coding: Broad Application and Cost Management
While powerful for coding tasks, Paperclip is designed as a universal tool for creating and managing businesses, extending to marketing, sales lead generation, and finance operations. It aims to be accessible to anyone in an organization, regardless of their coding expertise. Paperclip also includes features for cost management, allowing users to track monthly spending and set budgets per agent and project. It supports integrating cheaper models via services like OpenRouter (e.g., Quinn 3.6+ often free), enabling cost-effective deployment for less intelligence-intensive tasks, while still allowing the use of premium models for critical work.

---

## 5. Strategic Organization Building and Agent Instruction
When building an organization within Paperclip, the recommendation is to start small, adding agents one by one. Importing large pre-built templates is discouraged initially to ensure careful crafting of agent instructions and expected behaviors. Regular feedback and detailed instructions are crucial for high-quality results; for instance, instructing a coding agent to suggest solutions if blocked, rather than just stating the problem. The platform also hints at future organizational learning, where "skill consultants" (or automated systems) will optimize how agents use their skills within the organization.

---

## 6. Roadmap and Future Vision
Paperclip is a very early-stage product, released in early March and rapidly evolving. The roadmap includes experimental support for workspaces, a CEO chat feature, "maximizer mode" for relentless agent work, crucial multi-human user support (in progress), cloud and sandboxing agent deployments (E2B, dev.exe), a free open-source desktop app, and enhanced stability, memory, and knowledge base features. The project recently crossed 50,000 GitHub stars, indicating strong community interest and active development.

---

## Conclusion
Paperclip positions humans as the controllers of AI labor, empowering them to manage thousands of agents to build and run businesses. It's a free, open-source tool that helps debug, guide, and provide context to individual AI employees, ensuring work meets brand quality standards. The speaker encourages users, even non-technical ones, to download Paperclip at `paperclip.ing` and start orchestrating their AI agents today, emphasizing that it helps manage the "chaos of work" rather than displacing human roles.