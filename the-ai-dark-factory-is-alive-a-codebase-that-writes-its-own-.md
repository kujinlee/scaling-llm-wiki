---
tags:
  - video-summary
  - en
  - ai agents
  - agentic engineering
  - workflow automation
  - archon
  - dark factory
  - github issues
  - llm coding
video_id: "0PgB3EQ74OM"
channel: "Cole Medin"
lang: EN
type: Demo
audience: Advanced
score: 4.8
---

# The AI Dark Factory is ALIVE:  A Codebase That Writes Its Own Code, Live

**Channel:** Cole Medin | **Duration:** 2:21:04 | **URL:** https://www.youtube.com/watch?v=0PgB3EQ74OM

> [!summary] Quick Reference
> **TL;DR:** This video showcases the "Dark Factory," an AI-agentic application using Archon to autonomously build, test, and deploy software from GitHub issues.
>
> **Key Takeaways:**
> - AI agents can fully automate software development from issue creation to deployment.
> - Archon lets you package AI coding processes into reusable YAML workflows for flexible execution.
> - Autonomous AI systems need iterative debugging and refinement of their agentic workflows to ensure robustness.
> - AI agents can self-improve by creating workflows to triage, reproduce, and provide feedback on their own issues.
> - Agentic engineering changes the engineer's role to managing and refining AI agents, rather than direct coding.
>
> **Concepts:** ai agents · agentic engineering · workflow automation · archon · dark factory · github issues · llm coding

---

## 1. Introducing the Dark Factory: Fully Autonomous AI Development
This live stream demonstrates the "Dark Factory," an AI-agentic application designed to build, test, and deploy software based on GitHub issues without any human code review or manual deployment. The project aims to serve as a Retrieval Augmented Generation (RAG) system over the presenter's YouTube content, with plans to integrate course and workshop materials. The core idea is that AI builds everything, including merging code into the main branch and handling deployments, pushing the boundaries of autonomous software engineering.

---

## 2. Archon: The Harness for AI Coding Processes
Archon is introduced as the open-source harness builder underpinning the Dark Factory. It allows any AI coding process to be packaged into a YAML workflow, enabling execution across various codebases, even in parallel. The speaker has built elaborate Archon workflows for triaging issues, implementing features, validating pull requests (including browser automation), merging, and deploying. This structure ensures a consistent and reliable AI coding process, abstracting away the need for manual command sequences or complex prompting.

---

## 3. Issue-Driven Development: The Dark Factory in Action
The demonstration begins with the presenter identifying UI/UX issues in the Dark Factory's web application and using Claude Code to automatically create corresponding GitHub issues. The Dark Factory, hosted on a Virtual Private Server (VPS), periodically scans these issues, triages them based on predefined rules (e.g., priority, batching similar issues), and assigns them to Archon workflows for resolution. This system aims to autonomously address problems and implement new features, with changes reflecting live in the web UI within an hour or two.

---

## 4. Iterating on Reliability: Debugging Dark Factory Workflows
During the live stream, several challenges arise while the Dark Factory attempts to fix an issue. The validation workflow for pull requests fails to start the application, preventing full browser automation testing. The root cause is identified as a missing `DATABASE_URL` environment variable and an overly permissive validation verdict. The presenter live-corrects the Archon workflows for validation and orchestrates a re-run, emphasizing the iterative process of refining these agentic workflows to ensure robustness and adherence to critical steps like end-to-end testing.

---

## 5. Self-Improvement: Building an Archon Workflow for Archon Issues
In a parallel demonstration, the presenter begins to build a new Archon workflow *for* the Archon repository itself. This workflow aims to automatically reproduce reported GitHub issues by classifying them (e.g., web UI, API, CLI, database), gathering context, starting necessary services (like the Archon backend), and attempting to replicate the problem. The goal is to quickly identify user errors versus actual bugs and provide initial feedback on issues, streamlining the maintainer's workflow for the popular open-source project.

----- 

## 6. The Philosophy and Future of Agentic Engineering
The presenter discusses the experimental nature of the Dark Factory, acknowledging that full AI autonomy in coding is still a research frontier, not yet optimized for production-grade reliability without human intervention. He highlights the cost of running LLM-driven workflows (using Minimax M2.7 API), model comparisons (GLM, Quen), and the slow adoption of AI coding in large enterprises due to legacy systems and corporate red tape. The ultimate vision is for Archon to empower developers to build their custom agentic processes, evolving the role of engineers to manage and refine these AI agents rather than writing all code directly.

---

## Conclusion
The Dark Factory project, powered by Archon workflows, represents a significant step towards fully autonomous AI-driven software development. While the live demonstration reveals the complexities and ongoing need for workflow refinement and debugging, it successfully showcases the potential for AI agents to manage codebases from issue creation to deployment. The presenter's commitment to building and iterating in public underscores the challenges and immense potential of agentic engineering, positioning Archon as a crucial tool for developers seeking to customize and scale their AI coding practices.