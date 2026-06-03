---
tags:
  - video-summary
  - en
  - openai codex
  - ai coding
  - slash goal
  - developer tools
  - task automation
  - exploratory development
  - code agents
video_id: "VaPT2e2hCNQ"
channel: "Tech Bridge"
lang: EN
type: Tutorial
audience: Advanced
score: 4.8
---

# [한글자막] 현재 Codex 에서 제일 핫한 기능: /goal

**Channel:** Tech Bridge | **Duration:** 10:18 | **URL:** https://www.youtube.com/watch?v=VaPT2e2hCNQ

> [!summary] Quick Reference
> **TL;DR:** This video introduces OpenAI Codex's powerful `/goal` command, enabling AI agents to tackle complex, long-running, and exploratory development tasks through verifiable objectives.
>
> **Key Takeaways:**
> - Enable `/goal` in `config.toml` by setting `features.goals = true` to define long-running AI objectives.
> - Define verifiable, concrete goals; vague objectives will lead to indefinite AI execution.
> - Provide rich context (logs, codebase, metrics) to `/goal` for enhanced problem-solving effectiveness.
> - Treat `/goal` results as exploratory drafts, refining findings into clean, maintainable code specifications.
>
> **Concepts:** openai codex · ai coding · slash goal · developer tools · task automation · exploratory development · code agents

---

## 1. Introducing OpenAI Codex's `/goal` Command
OpenAI Codex has introduced a new and highly impactful `/goal` command, designed for long-running, complex tasks. This feature is generating significant excitement due to its ability to drive steady progress on challenging objectives, such as optimizing game performance or achieving feature parity across different operating systems. It's particularly useful when a task's solution isn't immediately clear and requires an AI agent to explore and iterate.

---

## 2. Setup and Core Usage of `/goal`
To enable the `/goal` feature, users must modify their `config.toml` file within the `.Codex` folder by adding `features.goals = true`. Currently, it's exclusively available in the terminal version of Codex. Once enabled, users can define a goal using `/goal` followed by a well-defined objective, such as "reduce P95 high possibility cloud latency by 20%". Codex will then map the repository, explore solutions, and self-test until the goal is achieved. Commands like `/goal pause`, `/goal resume`, and `/goal clear` allow for managing ongoing tasks, while `/goal` alone displays the current objective and token usage.

---

## 3. The Power of Exploratory Goals and Verifiable Objectives
The `/goal` command shines in "exploratory work" where the final solution shape is unknown, contrasting with "well-defined tasks" where the solution is predictable. Codex's underlying prompt for `/goal` is crucial: "do not accept proxy signals" and "treat uncertainty as not achieved." This mandates that goals must be easily verifiable, either by completing a predefined plan or hitting a specific metric. Vague goals, like "make this better," will cause indefinite execution. It's recommended to work with Codex to brainstorm and refine objectives into well-defined goals, especially given the potential for long running times and high token consumption.

---

## 4. Optimizing Goal Effectiveness: Context, Resources, and Side Threads
For `/goal` to be truly effective, particularly with vague objectives, it needs access to relevant resources. This includes real-world logs, staging environments (potentially globally distributed), cost data, the codebase, flame graphs, and existing metrics. The effectiveness of a goal is directly proportional to the "surface" it can act upon. For potentially dangerous or resource-intensive goals, running Codex in a Virtual Private Server (VPS) is advisable. Additionally, the `/side` command allows users to open temporary side threads for questions without interrupting the main goal's progress, maintaining focus on the primary task.

---

## 5. Mitigating Risks and Best Practices for Iterative Development
One significant risk with `/goal` is "codebase contamination," where the AI might leave behind debug prints, random hacks, or "scar tissue" during its exploratory process. The recommended approach for exploratory work is to treat the goal as a "scrappy branch" that aims to achieve a result. Once achieved, the lessons learned and solutions implemented should be distilled into a cleaner, well-defined specification or PRD, which can then be re-implemented. This allows `/goal` to essentially "discover a spec" that couldn't be written upfront, fostering a refine-and-decompose workflow that ensures a clean, maintainable codebase in the long term.

---

## Conclusion
The `/goal` command represents a powerful advancement in AI-driven software development, particularly for tackling complex, open-ended problems where solutions emerge through exploration. Its effectiveness is maximized by clearly defined, verifiable objectives and by providing the AI with rich contextual resources. While it offers immense potential, adopting best practices for managing generated code—such as treating exploratory outcomes as preliminary discoveries for subsequent, cleaner implementation—is crucial for maintaining code quality. This feature is poised to significantly change how developers approach challenging tasks, shifting towards more iterative and AI-assisted discovery processes.