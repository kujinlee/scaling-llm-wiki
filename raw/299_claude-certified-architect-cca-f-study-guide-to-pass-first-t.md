---
tags:
  - video-summary
  - en
  - anthropic
  - claude
  - certification
  - llm architecture
  - agentic design
  - prompt engineering
video_id: "akzKBQVyFEI"
channel: "Preporato | AI for Engineers"
lang: EN
type: Tutorial
audience: Advanced
score: 4.4
---

# Claude Certified Architect (CCA-F): Study Guide to Pass First Try

**Channel:** Preporato | AI for Engineers | **Duration:** 24:47 | **URL:** https://www.youtube.com/watch?v=akzKBQVyFEI

> [!summary] Quick Reference
> **TL;DR:** This video provides a comprehensive guide to passing the Anthropic Cloud Certified Architect exam, covering core concepts, domain knowledge, a study plan, and common pitfalls.
>
> **Key Takeaways:**
> - Master the `call-inspect-execute-append-call` agent loop for multi-step tasks.
> - Configure Claude Code with `Claude.md` hierarchy and slash commands for team conventions.
> - Use explicit, categorical rules in prompts and tool schemas for reliable structured output.
> - Mitigate "lost in the middle" by anchoring durable facts in a case block.
> - Implement prompt caching for static sections to significantly reduce API costs.
>
> **Concepts:** anthropic · claude · certification · llm architecture · agentic design · prompt engineering

---

## 1. Anthropic Certified Architect Exam Structure and Claude Fundamentals
▶ [0:06–3:06](https://www.youtube.com/watch?v=akzKBQVyFEI&t=6s)
The Anthropic Cloud Certified Architect exam features 60 scenario-based multiple-choice questions. To pass, candidates need a 75% score within approximately 2 minutes per question. The questions are drawn from four randomly selected production scenarios out of a total of six.

---

Claude, at its core, is a stateless language model accessed via a single HTTP endpoint (`api.anthropic.com/v1/messages`). It operates without memory between calls, does not run loops, and cannot execute code independently. All other functionalities are built as layers of discipline around this fundamental API. These layers include the Claude API (raw endpoint + SDKs), the Agent SDK (for agent loops and sub-agents), Claude Code (terminal agent with file system access), and the Model Context Protocol (MCP) for external tool integration. Understanding which layer handles specific behaviors is crucial for the exam.

---

## 2. Designing Agentic Architectures and Orchestration
▶ [3:06–6:07](https://www.youtube.com/watch?v=akzKBQVyFEI&t=186s)
Claude's stateless nature means that for multi-step tasks, the external code acts as the orchestrating agent loop. When Claude suggests a tool use, the code executes the tool, appends the result to the conversation history, and recalls the model. This `call-inspect-execute-append-call` cycle is fundamental to agent design, and the exam frequently tests for missing steps in this loop.

---

For complex tasks exceeding a single agent's context budget, multi-agent systems are used. A top-level "coordinator" Claude spawns smaller "sub-agents" via the Agent SDK's `task` tool, passing specific tasks. Decomposition can be sequential (where steps depend on previous outputs) or adaptive (where the next step is chosen based on the current output). When a sub-agent fails, the correct recovery is a targeted retry of only the failed agent, preventing unintended side effects from re-executing successful agents.

---

## 3. Effective Claude Code Configuration and Prompt Engineering
▶ [6:07–12:42](https://www.youtube.com/watch?v=akzKBQVyFEI&t=367s)
Claude Code operates directly within your repository. Its behavior is configured using `Claude.md` files, which are stitched into the session's system prompt. These files operate in a hierarchy: user-level (`~/.claude/claude.md`) for personal settings, project-level (repo root) for team conventions, and directory-level (sub-packages) for specific folder rules. Exam questions often test the correct placement of shared configurations.

---

Custom slash commands allow reusable prompts to be invoked efficiently. Defined in `.claude/commands`, they use YAML front matter to restrict `allowed_tools` and provide `argument_hint` documentation. For headless CI/CD, Claude Code can run non-interactively with structured output schemas (e.g., JSON) to enable pipeline failures only on explicitly named violation categories, avoiding noise from vague concerns.

---

Prompt engineering emphasizes specific, mechanically checkable rules over vague adjectives like "carefully." Replacing subjective terms with categorical, quantifiable instructions (e.g., "flag if function exceeds 40 lines") significantly reduces false positives. For reliable structured output, instead of relying on free-text formatting instructions, declare the output shape as a tool using `input_schema` and force its use with `tool_choice`. Implement a validation and retry loop to handle schema drift, feeding validation errors back to the model for correction. For large-scale, offline, latency-insensitive tasks, use the message batches API for cost-effective processing.

---

## 4. Designing Robust Tools and Managing Context
▶ [12:42–20:27](https://www.youtube.com/watch?v=akzKBQVyFEI&t=762s)
The Model Context Protocol (MCP) is an open standard for external tools to expose themselves to language models. Effective tool descriptions are critical: they must clarify what the tool does, when to use it over similar tools (disambiguation rules), provide example invocations, and list error conditions.

---

Structured error responses are essential for robust recovery. Tools should return JSON with fields like `is_error` (boolean), `category` (string, e.g., "rate limited"), `retryable` (boolean), and `retry_after_ms` (integer). This allows the model to form intelligent recovery plans instead of getting raw exceptions.

---

MCP supports two transports: STDIO (same process, zero latency/auth, default) and SSE (different host, HTTP, network latency/auth needed). Choose STDIO when the server can coexist with the client, and SSE only when a remote server is necessary.

---

Context management addresses the "lost in the middle" effect, where models pay less attention to the middle of long contexts. To combat this, extract durable facts (e.g., account numbers) into a small "case block" and re-anchor it at the end of the context on every turn. Avoid summarization, which is lossy and can drop critical details.

---

Prompt caching reduces costs for repetitive prompt sections (like system prompts or few-shot examples). Add a `cash_control_breakpoint` to cache internal states, achieving significant cost savings for reused prefixes. Cache only static, frequently reused portions, not dynamic user inputs.

---

Reliable agents must know when to escalate. The exam prioritizes escalating too eagerly over confidently providing incorrect answers. Implement explicit confidence checks and ambiguity detection to trigger human handoff, providing a structured summary of the agent's knowledge, attempts, and sticking points.

---

## 5. Comprehensive Study Plan and Exam Distractor Patterns
▶ [20:27–24:21](https://www.youtube.com/watch?v=akzKBQVyFEI&t=1227s)
The recommended 4-week study plan involves a weekly rhythm of reading domain guides for theory, building graded projects for practical experience, and consistent flashcard review. Six practice exams serve as checkpoints. Domain weights dictate study allocation, with agentic architecture being the heaviest. Week 1 focuses on agentic architecture, Week 2 on Claude Code and prompt engineering, Week 3 on tool design and MCP, and Week 4 on context management and a full dress rehearsal with timed practice exams.

---

Candidates should recognize five common distractor patterns:
1.  **Vague adjective trap:** Avoid prompts using "careful" or "thorough"; use numbered, categorical rules instead.
2.  **Summarization trap:** Do not summarize long conversations with critical IDs/amounts; extract durable facts into a case block.
3.  **Blanket retry trap:** Do not rerun all sub-agents if one fails after others had side effects; retry only the failed agent.
4.  **User `claude.md` trap:** Don't put team-shared config in the user-level `claude.md`; use the project-level file at the repo root.
5.  **SSE on localhost trap:** Pick STDIO for tools running on the same machine as the client, not SSE.

---

## Conclusion
▶ [24:21–24:47](https://www.youtube.com/watch?v=akzKBQVyFEI&t=1461s)
Passing the Anthropic Cloud Certified Architect exam requires a deep understanding of Claude's architecture, agentic design principles, prompt engineering best practices, robust tool integration, context management, and reliability patterns. By diligently following a structured study plan that includes hands-on building and recognizing common exam traps, candidates can confidently prepare for and successfully pass the certification. The exam is designed to reward practical architectural decisions and a solid grasp of how Claude operates and integrates within complex systems.