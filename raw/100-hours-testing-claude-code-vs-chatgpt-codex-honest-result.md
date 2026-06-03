---
tags:
  - video-summary
  - en
  - ai coding agents
  - claude code
  - openai codex
  - ai development tools
  - code generation
  - developer tools
  - large language models
video_id: "RLjaUES9P8A"
channel: "Nate Herk | AI Automation"
lang: EN
type: Analysis
audience: Intermediate
score: 4.8
---

# 100 Hours Testing Claude Code vs ChatGPT Codex (honest results)

**Channel:** Nate Herk | AI Automation | **Duration:** 26:34 | **URL:** https://www.youtube.com/watch?v=RLjaUES9P8A

> [!summary] Quick Reference
> **TL;DR:** This video compares Claude Code and OpenAI Codex, detailing their features, performance benchmarks, and best use cases for AI coding agents.
>
> **Key Takeaways:**
> - Claude Code excels in complex front-end tasks, visual design, and custom workflow automation.
> - OpenAI Codex is better for research, structured document generation, and direct code execution.
> - Leverage Claude for creative planning and brainstorming, then Codex for efficient code execution.
> - Claude Code offers deep workflow customization; Codex provides a unified, opinionated shipping experience.
> - Economic considerations matter: Claude often consumes more tokens, impacting usage costs.
>
> **Concepts:** ai coding agents · claude code · openai codex · ai development tools · code generation · developer tools · large language models

---

## 1. Introduction to AI Coding Agents: Claude Code vs. OpenAI Codex
The video introduces Claude Code (Anthropic) and the new OpenAI Codex as leading AI coding agents, both offering agentic systems for tasks like bug fixing, feature building, and pull request reviews. They operate across various platforms including terminal, VS Code extensions, desktop apps, and web versions. Both utilize advanced models (Claude Code: Opus, Sonnet, Haiku; Codex: GPT family, GPT-Codex, GPT-Codex-Spark) and share numerous commonalities like local code editing, desktop apps, VS Code extensions, command-line support, MCP protocol, skills format, plugin marketplaces, cloud delegation, hooks, and sub-agents. The core question is not *if* they have a feature, but *which provides a better workflow*.

---

## 2. Claude Code: The Customizable Workflow System
Claude Code distinguishes itself with profound customization capabilities, offering 30 hook events (vs. Codex's 6) for granular control over the agent's workflow. It features auto-delegating sub-agents that can self-spawn based on task complexity. Key slash commands include `/ultra plan` (cloud-based plan review with inline comments), `/ultra review` (multi-agent code review with reproduced findings), and `/loop` (recurring prompts or maintenance mode). Additional features include "channels" for external event integration (e.g., texting your agent) and the Claude agent SDK for building custom agents. For enterprise users, Claude Code supports Bedrock, Vertex AI, and Microsoft Foundry for robust authentication flexibility.

---

## 3. OpenAI Codex: The Unified Shipping Machine
OpenAI Codex is designed as an opinionated, end-to-end shipping pipeline, built around native Git work trees for parallel task execution. It offers a unified desktop app experience for reviewing, staging, committing, and pushing code. A standout feature is its in-app browser for directly viewing and commenting on agent-shipped work. Codex's "computer use" is particularly sharp, enabling product QA where it clicks around an app, finds bugs, and logs them with detailed reports. It also boasts a seamless GitHub integration (e.g., `@Codex` mentions for PR handling) and an experimental `/goal` command for long-running, verifiable objectives. Crucially, as an OpenAI product, it provides direct access to GPT Image 2 for in-app image generation.

---

## 4. Philosophical Differences & Economic Considerations
A significant divergence lies in their stance on third-party tools. OpenAI maintains a permissive approach, publicly endorsing tools like Open Claw that allow users to route Codex usage through their ChatGPT subscription, potentially saving costs. Anthropic, conversely, restricts third-party developers from offering Claude.ai login or rate limits for their products without explicit approval, impacting economic decisions for users relying on external agent tools.

Pricing: Both are included with parent subscriptions. Claude offers Pro ($20/month) and Max tiers ($100-$200/month). Codex is included with ChatGPT Free, Plus ($20/month), and Pro ($200/month). While base prices are similar, the video highlights that users often hit Claude Code limits faster. Context windows: Claude's Opus/Sonnet offer 1 million tokens, while Codex's latest GPT model is around 256,000. Despite similar input pricing, Claude Code often costs more in actual usage due to higher output token consumption.

---

## 5. Live Performance Benchmarks & Key Findings
A side-by-side comparison across three tasks (research report PDF, landing page, interactive dashboard) revealed mixed results:
-   **Dashboard:** Claude Code excelled, completing the complex build in ~2 minutes (4x faster than Codex) and using ~283k tokens (6x fewer than Codex's 1.64M). Its visual design quality was also preferred.
-   **Research Report:** Codex was slightly faster (~8 min vs. 8 min 15 sec) and significantly more token-efficient (2.8M tokens vs. Claude's 4.7M). Visually, it was a close call, but Codex's spacing was marginally preferred.
-   **Landing Page:** Codex was faster (3 min vs. Claude's 4 min 39 sec). However, Claude's underlying design for the landing page was preferred despite minor execution flaws.

Overall, Claude tended to plan tasks tightly, while Codex often ground through more iterations, leading to higher input tokens for complex builds. Claude consumed more output tokens across all tests, impacting cost and session limits.

---

## 6. When to Use Each: Practical Recommendations
-   **Reach for Claude Code when:** working on complex front-end tasks, visual design quality is paramount, deep planning or auto-delegation is needed, building custom workflows with extensive hooks/skills/channels, using the Claude agent SDK, or in enterprise environments requiring Bedrock/Vertex authentication. Claude feels more creative and is a better brainstorming partner.
-   **Reach for OpenAI Codex when:** tasks are research-heavy (web pulling), structured document production (PDFs/reports), desiring a single desktop app for shipping, using `/goal` for long-running objectives, leveraging `@Codex` for GitHub PRs, or requiring in-workflow image generation via GPT Image 2. Codex feels better at execution, following instructions, and catching code issues.

---

## Conclusion
The ultimate decision isn't about which tool is universally "better," but rather "which tool is best for the specific use case currently in front of you." Many users find success by leveraging Claude Code for planning and brainstorming, and then bringing in Codex for execution and code review. It's crucial to remember that code and projects built with these agents are largely portable (e.g., using GitHub), meaning developers are not locked into a single environment. The AI agent landscape is evolving rapidly, so users should keep an open mind and regularly check documentation for the latest features, pricing, and model updates.