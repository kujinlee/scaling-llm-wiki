---
tags:
  - video-summary
  - en
  - cloud code
  - developer tools
  - ai agent
  - workflow automation
  - remote development
  - code review
  - project management
video_id: "adIV8wlAFFE"
channel: "Tech Bridge"
lang: EN
type: Demo
audience: Intermediate
score: 4.6
---

# [한글자막] Claude Code 새로운 기능 소개 | Anthropic "Code w/ Claude" 발표

**Channel:** Tech Bridge | **Duration:** 24:56 | **URL:** https://www.youtube.com/watch?v=adIV8wlAFFE

> [!summary] Quick Reference
> **TL;DR:** This video details Cloud Code's updates, enhancing developer experience, empowering AI agents, and automating workflows for more efficient individual and team development.
>
> **Key Takeaways:**
> - Remote Control allows seamless development across devices, perfect for managing tasks on the go.
> - AI agents gain autonomy through Auto Mode for permissions and Auto Memory for recalling project knowledge.
> - Routines automate workflows by triggering tasks via schedules or webhooks, minimizing manual user intervention.
> - AI-powered "ultra reviews" use multi-agent patterns to thoroughly check code and verify findings.
>
> **Concepts:** cloud code · developer tools · ai agent · workflow automation · remote development · code review · project management

---

## 1. Enhancing Developer Experience
Cloud Code introduces several features designed to make the daily developer workflow smoother and more efficient. **Remote Control** enables users to start a session on their local machine and seamlessly pick it up on the go, even from a mobile device, maintaining the same development environment. This is ideal for managing long-running tasks while away from the keyboard.

The **Flicker-free Rendering** in the terminal's full-screen TUI mode addresses a common pain point. By virtualizing scrollback, it guarantees smooth output, eliminates flickering, and keeps memory usage flat even in very long sessions. This mode also makes elements within the terminal clickable, improving interaction.

The **Revamped GUI** offers a significantly improved experience for managing single or multiple sessions. It presents all relevant context efficiently, with features like split views, aggregated comments, and a detailed files view. An experimental "pin as chapter" feature allows users to title sections of their transcript, creating a table of contents for easy navigation within long sessions.

---

## 2. Boosting Autonomy with AI Agents
Cloud Code empowers agents to operate more independently, reducing manual intervention. **Auto Mode** is a new permissions system where a classifier intelligently decides whether to allow tool calls. It checks if an action is destructive or looks like prompt injection, running safe calls automatically and blocking unsafe ones, thus eliminating frequent permission prompts.

**Work Trees** simplify working on multiple features or branches concurrently. Unlike traditional Git worktrees, Cloud Code's implementation smooths out sharp edges, allowing users to declare shared files (e.g., `node_modules`) and easily create new worktrees via command or by asking Claude. Agents can now intelligently create isolated environments for new features.

**Auto Memory** enables Claude to accumulate and recall knowledge across sessions and projects. It manages a `memory.md` file within a project directory, allowing Claude to remember key build commands, debugging insights, and project preferences, leveraging progressive disclosure to link to more detailed files. This significantly reduces token usage on repetitive context setup.

**Code Review** introduces a multi-phase, multi-agent pattern to improve review efficacy. Users can spin up a team of AI reviewers to examine different aspects of code and verify findings. This "ultra review" process can be integrated via a GitHub app or manually triggered, catching issues that might otherwise be missed or take hours to find.

---

## 3. Automating Workflows with Routines
**Routines** allow for the creation of Cloud Code sessions that trigger without direct user intervention, automating idea generation and subsequent actions. Configured once with a prompt, repo, and connectors, routines can be triggered by a cron schedule (hourly, daily), GitHub webhook events, or custom API endpoints.

Examples include a routine that triages GitHub issues daily and sends a digest to Slack, or one that runs every time an e-commerce website makes a sale. The `/loop` command provides similar in-session automation, enabling Claude to schedule recurring tasks within a single session, such as telling a joke every minute or running periodic checks.

---

## 4. Key Improvements for Teams & Enterprises
Beyond individual developer features, Cloud Code has made significant strides in supporting teams and larger organizations. This includes **much better Windows support**, addressing previous limitations for users on that platform. 

Features for administrators and team leads include **cloud provider setup**, **native installation improvements**, and advanced **admin settings management**. Additionally, **plugin features** are available to facilitate company-wide harness improvements, ensuring that Cloud Code can be tailored and deployed effectively across diverse enterprise environments.

---

## Conclusion
The latest updates to Cloud Code mark a significant evolution, focusing on both enhancing the human developer experience and expanding the autonomy of AI agents. From remote development and flicker-free terminals to intelligent permission handling, parallel feature development, and automated code reviews, these features collectively reduce manual approvals, enable more efficient parallel work, and leverage accumulated knowledge over time. The introduction of routines further empowers users to automate entire workflows, transforming how development tasks are initiated and managed. By integrating these advanced capabilities, Cloud Code aims to maximize developer productivity and free up valuable time, allowing users to focus on higher-level problem-solving while AI handles the intricacies.