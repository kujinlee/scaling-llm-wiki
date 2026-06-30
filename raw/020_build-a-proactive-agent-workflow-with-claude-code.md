---
tags:
  - video-summary
  - en
  - claude code
  - ai agents
  - workflow automation
  - developer tools
  - github integration
  - documentation automation
  - software engineering
video_id: "eSP7PLTXNy8"
channel: "Claude"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# Build a proactive agent workflow with Claude Code

**Channel:** Claude | **Duration:** 22:04 | **URL:** https://www.youtube.com/watch?v=eSP7PLTXNy8

> [!summary] Quick Reference
> **TL;DR:** This video introduces Claude Code Routines, enabling proactive AI agents to automate developer workflows like documentation and monitoring, freeing engineers from infrastructure management.
>
> **Key Takeaways:**
> - Claude Code Routines simplify agent hosting by managing infrastructure, state, and authentication for you.
> - Automate tasks with Routines using time-based schedules or event-based triggers like GitHub activity.
> - Interact with and steer active routine sessions via web, CLI, or desktop for quality control.
> - Automate documentation creation by setting routines to review code and propose updates via pull requests.
> - Apply Routines to verify deployments, investigate incidents, or prioritize backlogs in your engineering workflow.
>
> **Concepts:** claude code · ai agents · workflow automation · developer tools · github integration · documentation automation · software engineering

---

## 1. The Challenge with Proactive Agents
Building proactive AI agents today presents several hurdles for developers. These include deciding where to host agents (managing infrastructure, data persistence, and authentication), figuring out when to trigger sessions (requiring custom cron jobs or API endpoints), and the difficulty of real-time monitoring and steering of headless agent sessions.

---

## 2. Introducing Claude Code Routines
Anthropic developed "Routines" within Claude Code to transform it from a reactive tool into a proactive coding teammate. Routines allow users to kick off remote Claude Code sessions by simply defining a prompt, connected repositories, available connectors, and a trigger. Claude Code manages the underlying infrastructure, hosting, session state, and connector authentication.

---

## 3. Key Benefits and Decisions for Routines
Routines offer three main advantages: they are always available, running on Anthropic's managed infrastructure; they work proactively with customizable triggers (time-based schedules or event-based, like GitHub events or custom webhooks); and their sessions are interactive and steerable, just like terminal sessions, accessible via web, CLI, or desktop. When creating a routine, users must decide:
1.  **Trigger:** When the routine should run (e.g., weekly, on a GitHub issue open).
2.  **Context:** What information Claude needs (e.g., codebases, documentation repos, marketing briefs, Slack connector).
3.  **Steerability:** How to ensure output quality (e.g., agent-on-agent review, human monitoring/nudge, verification of outputs).

---

## 4. Automating Documentation Creation: An Internal Use Case
Anthropic's engineering team leverages Routines to automate documentation. With a 200% increase in PRs for Claude Code, a single documentation engineer faced an overwhelming workload. By setting up routines, Claude Code can now automatically review new code changes against the documentation repository weekly, identify gaps, and create pull requests to update the docs. Event-based triggers can also automate doc updates when releases are cut or specific PRs are merged.

---

## 5. Expanding Routines to Developer Workflows
Routines can be applied to numerous common software engineering challenges. Examples include:
*   **Deploy Verifier:** Triggered post-deployment to ensure service health by analyzing source code and monitoring tools, potentially suggesting rollbacks.
*   **On-call Investigator:** Automatically investigating incidents.
*   **PM Backlog Prioritizer:** A weekly job to analyze GitHub issues or Slack conversations, prioritize tasks, and create related PRs.

---

## Conclusion
Routines empower developers to build proactive AI agents without the burden of infrastructure management, allowing them to focus on domain expertise. By transforming Claude Code into a teammate that reacts to problems and initiates actions, developers can significantly enhance their workflows. The call to action is to begin using Routines today with a simple `/schedule` command in Claude Code.