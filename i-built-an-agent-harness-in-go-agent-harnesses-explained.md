---
tags:
  - video-summary
  - en
  - ai agents
  - coding agents
  - harness engineering
  - llm development
  - custom agents
  - tool use
  - go programming
video_id: "NAKFWH4aIIE"
channel: "What The Func? w/ Ed Zynda"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# I built an Agent Harness in Go. Agent Harnesses Explained

**Channel:** What The Func? w/ Ed Zynda | **Duration:** 15:14 | **URL:** https://www.youtube.com/watch?v=NAKFWH4aIIE

> [!summary] Quick Reference
> **TL;DR:** This video explains AI agents use an agent loop, but a harness is the control system, offering custom flexibility for specific needs.
>
> **Key Takeaways:**
> - The "agent loop" involves prompt, thinking, tool use, observing results, and repeating until a final answer.
> - The "harness" is the control plane managing an agent's behavior, tools, context, and stop conditions.
> - Build a custom harness for private APIs, compliance, embedding, or strong control not offered by existing agents.
> - Implement narrow tools, feed errors back, track budget, manage context, and log everything for robust harnesses.
>
> **Concepts:** ai agents · coding agents · harness engineering · llm development · custom agents · tool use · go programming

---

## 1. Understanding the Agent Loop
The foundational concept behind all AI agents is a simple `while` loop. This "agent loop" involves giving a language model (LLM) a prompt, allowing it to think, potentially call a tool if needed, observe the result, and then think again. This cycle continues until the model determines it has a final answer and stops.

The agent loop comprises four essential parts:
1.  **System Prompt**: Defines the agent's identity, rules, and instructions.
2.  **Message History**: Acts as the model's working memory, appending every tool call, result, and response to maintain context.
3.  **Tool Surface**: Represents the actions the model can take, such as reading files, running commands, or searching the web.
4.  **Stop Condition**: Determines when the agent should quit, typically when the model decides it's done, or via hard limits like max iterations or cost budgets.

---

## 2. The Role of the Harness
While the agent loop is the core engine, the "harness" is the control plane wrapped around it. It defines the agent's behavior by managing aspects like which model to use, which tools are available, how results are fed back, context management to avoid blowing token windows, guardrails, safety mechanisms, and overall loop termination. The analogy used is: the model is the engine, but the harness is the vehicle. Most product differentiation in coding agents lies in the harness's design, not just the underlying LLM.

---

## 3. Existing Coding Agents and When to Go Custom
Many popular coding agents like Claude Code, Open Code, and Cursor are essentially sophisticated harnesses built around the fundamental agent loop. They offer different tools, defaults, and user experiences but share the same core architecture. If your primary goal is to get work done quickly and an existing solution meets your needs, using an off-the-shelf harness is recommended to avoid over-engineering.

However, a custom harness becomes necessary when you have specific constraints or requirements, such as:
*   Calling private internal APIs.
*   Enforcing a specific tool execution order.
*   Satisfying compliance or audit requirements (e.g., specific permissions, logging).
*   Embedding the agent directly into your own product.
*   Needing strong control over policy, safety, and observability.

---

## 4. Building Your Own Agent Harness
Starting your own custom harness involves implementing the basic agent loop: setting up messages with a system prompt and user task, entering a `while` loop, calling the LLM, executing tool calls (if any), appending results to history, and repeating until a stop condition is met. This core loop is surprisingly compact and functional.

Key practices for building a robust custom harness include:
*   **Narrow Tools**: Design tools for single, clear jobs with precise descriptions.
*   **Feed Errors Back**: Always return tool call failures to the LLM so it can learn and try alternative approaches.
*   **Track Budget**: Implement limits for iterations, tokens, and costs from day one to prevent runaway expenses.
*   **Context Management**: Employ strategies like history summarization (compaction) to maintain model response quality and prevent context window degradation.
*   **Log Everything**: Comprehensive logging of model responses, tool calls, and results is crucial for debugging and understanding agent behavior in production.

---

## 5. Kit: An Example of a Custom Harness
Kit is a Go-based coding agent harness inspired by the principles of another agent called Pi. It features a radically small core with eight essential tools (bash, read, write, edit, grep, find, ls, spawn sub-agent). It's provider-agnostic, supporting LLMs from Anthropic, OpenAI, Gemini, and Ollama. Kit's design emphasizes composability over complexity: its core remains small, while advanced features like plan mode or permission gates are implemented as optional extensions written in Go. This allows for a single binary, eliminating dependency management issues. Kit is available as a CLI, an SDK for embedding, and an LSP server, offering flexibility for different integration needs.

---

## Conclusion
In essence, an AI agent's core is a simple "agent loop" of prompt-think-tool-observe-repeat. The "harness" is the surrounding control system that dictates its behavior and capabilities. While off-the-shelf agents serve many purposes, building a custom harness offers unparalleled control and flexibility for specific, demanding requirements. Projects like Pi and Kit demonstrate that a powerful custom harness can be built with a minimalist core and extensible architecture, allowing for tailored functionality without unnecessary complexity. Understanding these components empowers developers to either leverage existing solutions effectively or craft custom agents that precisely fit their needs.