---
tags:
  - video-summary
  - en
  - cloud code
  - ai agents
  - autonomous development
  - verification loops
  - developer productivity
  - software automation
  - agent management
video_id: "wI0ptqCSL0I"
channel: "Claude"
lang: EN
type: Framework
audience: Advanced
score: 4.4
---

# Stop babysitting your agents

**Channel:** Claude | **Duration:** 37:07 | **URL:** https://www.youtube.com/watch?v=wI0ptqCSL0I

> [!summary] Quick Reference
> **TL;DR:** This video provides advanced strategies for developers to stop manually overseeing AI agents by implementing verification loops, multi-cloud management, and automated background routines.
>
> **Key Takeaways:**
> - Implement verification loops to enable AI agents to autonomously check and debug their own code.
> - Package verification steps into self-improving "skills" for team-wide reusability and documentation.
> - Utilize multi-cloud tools like desktop apps or agent views to effectively manage multiple concurrent agent sessions.
> - Delegate routine development tasks to background loops and routines to free up human attention.
> - Leverage remote control to monitor and interact with AI agents from any device, anytime.
>
> **Concepts:** cloud code · ai agents · autonomous development · verification loops · developer productivity · software automation · agent management

---

## 1. The Problem of "Babysitting" AI Agents and Cloud Code Prerequisites
▶ [0:13–5:13](https://www.youtube.com/watch?v=wI0ptqCSL0I&t=13s)
Sid Bisaria introduces the challenge of increasingly spending time monitoring and QA testing AI agents, which is inefficient and unsatisfactory. The goal of the talk is to provide strategies for developers to better manage their agents and reclaim time. This is positioned as an "advanced Cloud Code talk" (301 level) with several prerequisites for optimal understanding and implementation: using a high-quality Cloud MD, connecting essential developer tools (like Slack, Asana, Datadog) to provide richer context for Cloud, and setting up a remote environment on Cloud Code Web to decouple compute from the local machine.

---

## 2. Rethinking Software Tooling for AI Agents
▶ [5:13–8:32](https://www.youtube.com/watch?v=wI0ptqCSL0I&t=313s)
Traditional software tooling has been built primarily for human developers, focusing on accelerating human teams. However, with AI agents now writing a significant portion of code, there's a need to reconsider our toolchains. While many existing tools like linters and prettiers are also beneficial for agents, human developers often make assumptions about their tooling that agents don't share. This highlights a crucial question: What does an AI agent need from a codebase that a human takes for granted? The presentation will then outline three core concepts to address this: verification, multi-clouding, and background loops.

---

## 3. Verification Loops: Teaching Cloud to Check Its Own Work
▶ [8:32–25:48](https://www.youtube.com/watch?v=wI0ptqCSL0I&t=512s)
The first key strategy is teaching Cloud to verify its own work. Humans typically follow a process of designing/writing code, building, running tests, checking side effects (UI, logs, database), and finally deploying. This exact playbook can be adopted by Cloud. The core concept here is a "loop" – an autonomous circuit where Cloud writes code, checks for failures, debugs, and reiterates until a success state is achieved. This iterative process allows Cloud to "hill climb" on a given task, leading to higher-quality, functional outputs. Verification can apply to various aspects, including UX, backend, and end-to-end functionality.

To implement a concrete UX verification loop, four steps are crucial: running the application (e.g., a dev server), enabling Cloud to use the web server (e.g., via browser control tools like Chrome MCP), proving functionality (e.g., comparing screenshots before and after a fix), and unblocking common issues like authentication and pre-configuring application state dynamically. These dynamic setup scripts, while similar to traditional E2E test setups, empower Cloud with greater versatility.

---

## 4. Practical Implementation: Building Self-Improving Verification Skills (with Demo)
▶ [25:48–44:02](https://www.youtube.com/watch?v=wI0ptqCSL0I&t=1548s)
Once a verification loop is established, the next step is to package and distribute it using "skills." A skill is a way to store arbitrary context about a topic, like verification. Critically, skills can be made "self-improving" by including instructions for the agent to update the skill whenever it encounters and overcomes a blocker. This fosters a self-documenting and collaboratively improvable resource for the entire team. A live demo showcased this process using a Monkey Type application: Cloud spun up a dev server, used the Chrome MCP to interact with the frontend (typing, changing settings), and then created a verification skill based on these actions. Subsequently, when asked to implement a new feature (confetti on mistype) and verify it using the newly created skill, Cloud successfully wrote the code, debugged lint errors, and used the skill to confirm the feature's functionality, demonstrating the power of autonomous verification.

---

## 5. Scaling Agent Operations with Multi-Cloud Strategies
▶ [44:02–54:06](https://www.youtube.com/watch?v=wI0ptqCSL0I&t=2642s)
Managing multiple AI agent instances simultaneously can quickly overwhelm human attention. To scale multi-cloud operations effectively, several strategies are introduced. The Cloud Code desktop app provides a graphical user interface for managing sessions across all surfaces (local, web, Git repos), allowing users to pin, rename, and color sessions to better organize their focus. For terminal enthusiasts, "Cloud Agents" offers a similar terminal-based view, prioritizing sessions that require immediate attention. Running Cloud Code on the web decouples agent compute from your local laptop, enabling continuous operation regardless of your device's status. Finally, "remote control" allows users to monitor and interact with any agent session from their phone, receiving notifications when input is needed. These tools collectively aim to protect human attention while enabling parallel agent workflows.

---

## 6. Automating Routine Tasks with Background Loops and Routines
▶ [54:06–1:00:26](https://www.youtube.com/watch?v=wI0ptqCSL0I&t=3246s)
Beyond active development, software engineers spend significant time on "bookkeeping" tasks such as babysitting PRs (handling review comments, merge conflicts, CI failures), updating documentation, triaging feedback, and maintaining CI health. These tasks are repetitive and don't necessarily require direct human intervention. The `/loop` command in Cloud Code allows a prompt to be run at a specified interval, enabling an agent to autonomously manage these tasks (e.g., `/loop 10 minutes and babysit my open PRs`). Building on this, "routines" are essentially remote loops, managed via the web or desktop app, with time-based or event-based triggers that can spawn new Cloud Code sessions to execute predefined prompts. This enables full automation of routine operational tasks, freeing developers to focus on higher-value activities.

---

## Conclusion
▶ [1:00:26–1:01:03](https://www.youtube.com/watch?v=wI0ptqCSL0I&t=3626s)
By integrating verification loops, multi-cloud management strategies, and automated background routines, developers can establish a powerful system where AI agents perform a wide array of tasks with minimal human intervention. This framework allows for significant delegation of work to Cloud with high reliability and confidence, ultimately enabling humans to allocate their attention and time to the most critical and creative aspects of software engineering.