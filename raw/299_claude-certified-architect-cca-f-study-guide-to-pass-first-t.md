---
tags:
  - video-summary
  - en
  - anthropic
  - cloud architect
  - certification prep
  - claude
  - agentic ai
  - prompt engineering
  - mcp
video_id: "akzKBQVyFEI"
channel: "Preporato | AI for Engineers"
lang: EN
type: Tutorial
audience: Advanced
score: 4.8
---

# Claude Certified Architect (CCA-F): Study Guide to Pass First Try

**Channel:** Preporato | AI for Engineers | **Duration:** 24:47 | **URL:** https://www.youtube.com/watch?v=akzKBQVyFEI

> [!summary] Quick Reference
> **TL;DR:** This video provides a comprehensive guide to passing the Anthropic Cloud Certified Architect exam, covering key domains, architectural patterns, and a detailed 4-week study plan.
>
> **Key Takeaways:**
> - Master the Claude agent loop (call, inspect, execute, append) and targeted sub-agent retries.
> - Configure Claude Code with hierarchical Claude.md files for team-wide conventions.
> - Implement structured output using tool schemas and validate/retry loops for reliability.
> - Design robust MCP tools with descriptive names and structured error responses.
> - Combat "lost in the middle" by re-anchoring durable facts in a case block.
>
> **Concepts:** anthropic · cloud architect · certification prep · claude · agentic ai · prompt engineering · mcp

---

## 1. Exam Overview and Claude Fundamentals
▶ [0:06–3:06](https://www.youtube.com/watch?v=akzKBQVyFEI&t=6s)
To pass Anthropic's Cloud Certified Architect exam, you must answer 60 multiple-choice scenario-based questions with at least 75% correctness. The exam draws from six production scenarios, presenting you with four randomly selected ones. Each question involves making architectural decisions in a simulated working system, allowing roughly two minutes per question.

Before diving into domains, understand that Claude is fundamentally a stateless language model accessed via a single HTTP endpoint, `api.anthropic.com/v1/messages`. It has no memory between calls, doesn't run loops, and doesn't execute code directly. This core engine is augmented by four layers of discipline: the Claude API (raw endpoint + SDKs), the Agent SDK (for agent loops and sub-agents), Claude Code (a terminal agent with file system access), and the Model Context Protocol (MCP) for external tool integration. The exam questions often test your understanding of which layer is responsible for specific behaviors.

---

## 2. Agentic Architecture and Orchestration
▶ [3:06–6:14](https://www.youtube.com/watch?v=akzKBQVyFEI&t=186s)
As Claude is stateless, your code must implement the agent loop for multi-step tasks. When calling `messages.create` with allowed tools, the `stop_reason` field dictates the next step: `end_turn` means Claude is done, while `tool_use` indicates Claude needs your code to execute a function. The full agent loop involves calling, inspecting the `tool_use` response, locally executing the function, appending the result as a `tool_result` message, and then recalling `messages.create` with updated history. Exam questions frequently highlight missing steps in this cycle.

For tasks exceeding a single Claude's context budget, use multi-agent systems where a top-level coordinator Claude spawns smaller sub-agents (via the `task_tool` in the Agent SDK). This keeps the coordinator's context lean by receiving only compact summaries from sub-agents. Decompose tasks either sequentially (when steps are interdependent) or adaptively (for open-ended work). When a sub-agent fails, the correct recovery is almost always a targeted retry of only the failed agent to prevent unwanted side effects from re-executing successful ones.

---

## 3. Claude Code Configuration and Workflows
▶ [6:14–24:47](https://www.youtube.com/watch?v=akzKBQVyFEI&t=374s)
Claude Code operates as a terminal agent within your repository, starting each session with no memory of your project. This is remedied by `Claude.md` files, which are stitched into the system prompt based on their directory hierarchy. There are three levels:
*   **User level (`~/.claude/claude.md`)**: For personal settings, not version controlled.
*   **Project level (`repo root/claude.md`)**: For team-wide conventions, committed to Git.
*   **Directory level (`sub-package/claude.md`)**: For rules specific to a particular folder.

Custom slash commands offer reusable prompts, defined in `.claude/commands/` with YAML front matter to constrain behavior, such as limiting `allowed_tools` to read-only access. For headless CI/CD, use `claude code -p` with a structured output schema. Pipelines should only fail on explicitly named violation categories, like 