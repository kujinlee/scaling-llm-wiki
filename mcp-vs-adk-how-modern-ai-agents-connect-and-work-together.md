---
tags:
  - video-summary
  - en
  - ai agents
  - mcp
  - adk
  - model context protocol
  - agent development kit
  - llms
  - ai development
video_id: "BedAaB1RKgE"
channel: "IBM Technology"
lang: EN
type: Analysis
audience: Intermediate
score: 4.6
---

# MCP vs ADK: How Modern AI Agents Connect and Work Together

**Channel:** IBM Technology | **Duration:** 14:11 | **URL:** https://www.youtube.com/watch?v=BedAaB1RKgE

> [!summary] Quick Reference
> **TL;DR:** This video explains how MCP standardizes AI agent external connectivity, and ADK structures internal agent orchestration, providing complementary solutions for robust AI development.
>
> **Key Takeaways:**
> - MCP standardizes LLM connectivity to external tools and data, offering reusable, model-agnostic integrations via JSON RPC.
> - ADK is a Python framework structuring AI agent internal logic, orchestration, and memory for predictable, testable systems.
> - MCP solves the 'connectivity problem' (how agents communicate), while ADK solves the 'orchestration problem' (what agents do).
> - Leverage MCP for external communication standards and ADK for building, structuring, and debugging an agent's internal logic.
>
> **Concepts:** ai agents · mcp · adk · model context protocol · agent development kit · llms · ai development

---

## 1. The Landscape of AI Agents and Core Challenges
AI agents are evolving beyond simple chatbots to perform complex tasks, creating excitement and new development hurdles. As developers build these sophisticated systems, two fundamental questions arise: how do agents securely and effectively interact with external tools and data, and how are these agents themselves constructed and orchestrated? These distinct problems are precisely where the Model Context Protocol (MCP) and Agent Development Kit (ADK) offer solutions.

---

## 2. Model Context Protocol (MCP): Standardized Connectivity
Developed by Anthropic, the Model Context Protocol (MCP) is an open standard designed to solve the challenge of LLM connectivity to the outside world. Before MCP, developers had to create custom integrations for every external resource an agent needed to access, such as databases (e.g., Postgres), web scrapers, or file systems. MCP standardizes this interface, defining a protocol (using JSON RPC) for how an LLM host or AI agent communicates with servers exposing tools or data.

Its three core primitives include:
*   **Tools:** Functions an LLM can invoke (e.g., search the web, execute an SQL query).
*   **Resources:** Data sources an LLM can read (e.g., files, documentation, internal/external databases).
*   **Prompts:** Pre-built prompt templates to streamline interactions.

A significant advantage of MCP is its model-agnostic nature and reusability; an MCP server can be written once and utilized by any MCP-compatible client, regardless of the underlying LLM (e.g., Claude, GPT, Gemini). This saves considerable development time by eliminating redundant custom integrations, fostering a rapidly growing ecosystem of readily available servers for common services like GitHub, Slack, and Google Drive.

---

## 3. Agent Development Kit (ADK): Structured Agent Orchestration
From Google, the Agent Development Kit (ADK) is an open-source Python framework that provides crucial structure for building AI agents and complex multi-agent systems. While MCP handles external communication, ADK focuses on the internal logic and architecture of the agent itself, offering primitives like agents, tools, memory, events, and runners to build predictable and testable systems.

ADK defines an agent not merely as an LLM with a prompt, but as a structured execution unit encompassing a model, specific instructions, permissible tools, and a controlled reasoning loop. It supports various agent types: flexible LLM-driven agents for reasoning, deterministic workflow agents (sequential, parallel, loop-based) for strict control, and custom agent creation.

The ADK introduces a "runner" component that mediates between the user query and the agent. The agent, in its execution loop, yields control back to the runner whenever it needs to perform a tool call or report a state change. This suspension mechanism allows the runner to manage consequences and commit state changes, significantly improving debugging and traceability compared to ad-hoc agent implementations. ADK also differentiates between short-term "state" (within a conversation) and long-term "memory" (across sessions) and enables agents to use other agents as tools, facilitating robust multi-agent architectures where a root orchestrator can delegate tasks to specialized sub-agents.

---

## 4. Complementary Roles: When to Use MCP and ADK
Crucially, MCP and ADK are not competing technologies but rather complementary layers in AI agent development. The question is not which one to use, but rather for which problem.

Consider building a coding assistant:
*   **ADK's role:** It defines the agent's internal cognition—its planning, reasoning, tool orchestration, memory management, error handling, and guardrails to ensure predictable and safe behavior (i.e., *what* the agent should do).
*   **MCP's role:** It provides the standardized communication protocol for the agent to interact with external tools and resources like your code repository, test runner, or issue tracker in a consistent, reusable manner (i.e., *how* the agent communicates with the world to perform its tasks).

ADK dictates the agent's logic and decision-making, while MCP standardizes how that agent accesses and manipulates external data and services. Together, they form a powerful stack for building robust, reliable, and scalable AI agent applications.

---

## Conclusion
Navigating the rapidly evolving landscape of AI agent protocols can be confusing, but understanding the distinct yet complementary roles of the Model Context Protocol (MCP) and the Agent Development Kit (ADK) is key. MCP addresses the critical challenge of standardized external connectivity for LLMs, enabling agents to seamlessly interact with various tools and data sources. ADK, on the other hand, provides the robust framework and structure necessary for building, orchestrating, and debugging reliable AI agents and complex multi-agent systems. By understanding that MCP solves the "connectivity problem" and ADK solves the "orchestration problem," developers can effectively leverage both to build sophisticated, maintainable, and predictable AI applications.