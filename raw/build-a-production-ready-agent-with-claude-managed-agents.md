---
tags:
  - video-summary
  - en
  - cloud managed agents
  - anthropic claude
  - llm agents
  - multi-agent systems
  - developer tools
  - api integration
  - agent orchestration
video_id: "jWWsLe4Gh5Y"
channel: "Claude"
lang: EN
type: Demo
audience: Intermediate
score: 4.4
---

# Build a production-ready agent with Claude Managed Agents

**Channel:** Claude | **Duration:** 27:23 | **URL:** https://www.youtube.com/watch?v=jWWsLe4Gh5Y

> [!summary] Quick Reference
> **TL;DR:** This video introduces Anthropic's Cloud Managed Agents, simplifying production-ready LLM agent development by abstracting complexities like tools, context, and secure integrations.
>
> **Key Takeaways:**
> - CMAs abstract LLM agent complexities, handling tool access, context, memory, and error recovery for production apps.
> - Agents, Environments, and Sessions are core primitives to define agent behavior and manage interactions.
> - Securely integrate private data and services using self-hosted sandboxes and MCP tunnels for enhanced privacy.
> - Build sophisticated multi-agent applications by orchestrating specialized sub-agents with diverse tools.
> - The Claude Console offers robust tools for real-time monitoring, debugging, and managing agent activities and memories.
>
> **Concepts:** cloud managed agents · anthropic claude · llm agents · multi-agent systems · developer tools · api integration · agent orchestration

---

## 1. Introduction to Cloud Managed Agents
Cloud Managed Agents (CMAs) are a set of API endpoints developed by Anthropic, offering access to scaled, production-ready AI agents and their underlying primitives. The goal of CMAs is to abstract away the complexities of building and managing sophisticated LLM-powered applications, allowing developers to focus on the product experience. They handle crucial aspects like giving Claude access to tools (e.g., a computer, web search), managing credential vaults for secure access to external services (like Linear MCP), handling tool calling, retries, error recovery, memory, and context management. A significant feature is built-in observability in the developer console for live debugging.

---

## 2. Core Components and Event Model
CMAs are built around four main primitives:

*   **Agent:** Defined as a template with a system prompt, skills, and specific tools. Developers can choose which tools an agent has access to (e.g., Bash, web search) and define per-tool permission controls (e.g., auto-execute file read, explicit approval for sensitive actions).
*   **Environment:** Configures the behavior of the agent's sandbox, including network access and pre-installed packages (NPM, pip). Newly introduced self-hosted environments allow users to bring their own sandboxes (e.g., Cloudflare, Modal, Vercel) for enhanced control and data privacy.
*   **Session:** Represents an ongoing conversation with an agent, initialized with an agent ID and environment ID. Sessions can incorporate external resources like GitHub repositories or preloaded files.
*   **Events:** Sessions are streams of various event types:
    *   **User Events:** User messages (text, images, documents), interrupts to steer Claude, tool results, human-in-the-loop confirmations, and `outcome` definitions (specs for Claude to iterate against).
    *   **Agent Events:** Claude's messages, context compaction, tool executions, and multi-agent coordination events.
    *   **Session Events:** Lifecycle updates (status changes, errors, idle, termination).
    *   **Span Events:** Indicate the start and end of long-running operations.

---

## 3. Advanced Features and Ecosystem Integration
Beyond the core primitives, CMAs offer advanced capabilities designed for secure and flexible integration:

*   **Self-Hosted Sandboxes:** Users can deploy agents within their own container infrastructure, ensuring private data remains within their VPC or perimeter, rather than Anthropic's.
*   **MCP Tunnels:** Secure tunnels allow Claude to connect directly and safely to private MCP (Model Control Plane) servers within a user's network, without exposing those servers to the internet. This is crucial for integrating private data sources.
*   **Credential Vaults:** Securely store authentication tokens for MCP services, injecting them into sessions without ever exposing them to Claude's context window.
*   **Memory Stores:** Provide agents with persistent memory, allowing them to read and write memories across sessions, leading to continuous improvement.

---

## 4. Building a Multi-Agent Application (Live Demo)
The speaker demonstrates building a "Deal Desk" web application designed to assist with mergers and acquisitions decisions. This application leverages the new multi-agent feature, allowing a primary agent to delegate tasks to specialized sub-agents (e.g., one for macro trends, another for financial analysis) each with their own personas and tools. The live coding segment shows how to use the Anthropic SDK to list and retrieve sessions, and how Claude itself (via the `Claude API skill`) can assist in implementing complex functionalities like streaming events. The demo highlights the process of defining `outcome` events, where Claude is given a detailed spec for analyzing multiple companies and then iteratively criticizes its own findings against that rubric.

---

## 5. Observability and Management with the Claude Console
The Claude developer console provides robust tools for monitoring and debugging CMA interactions:

*   **Live Session Monitoring:** Users can observe agents processing tasks in real-time, seeing individual sub-agents running concurrently and the detailed inputs/outputs of tool calls (e.g., web searches).
*   **Environment and Credential Vault Views:** Manage and review configured environments and securely stored authentication tokens.
*   **Memory Store Inspection:** Users can review and even edit the memories Claude has stored, allowing for correction or manual addition of information to guide future agent behavior.
*   **Quick Start and Templates:** The console offers guided experiences and predefined templates for quickly setting up agents and sessions.
*   **Agent Versioning:** Agents are versioned, enabling developers to revert to previous configurations if an update to the system prompt or tools proves unsatisfactory.

---

## 6. Conclusion
Cloud Managed Agents significantly streamline the development of intelligent applications by abstracting away the complex infrastructure and operational challenges inherent in building and deploying LLM agents. By providing out-of-the-box solutions for agent orchestration, context management, secure integrations, durable storage, sandboxing, and authentication, Anthropic empowers developers to rapidly build sophisticated, production-ready, multi-agent systems. This allows for a focus on delivering unique product experiences rather than grappling with underlying technical complexities.