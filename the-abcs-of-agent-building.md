---
tags:
  - video-summary
  - en
  - ai agents
  - agent protocols
  - google cloud
  - adk
  - external systems
  - real-time ui
  - payments
video_id: "rjoMZyxncUI"
channel: "Google Cloud Tech"
lang: EN
type: Framework
audience: Intermediate
score: 4.4
---

# The ABCs of agent building

**Channel:** Google Cloud Tech | **Duration:** 13:54 | **URL:** https://www.youtube.com/watch?v=rjoMZyxncUI

> [!summary] Quick Reference
> **TL;DR:** This video details six core protocols (MCP, A2A, UCP, AP2, A2UI, AGUI) for building capable AI agents that interact with external systems and users.
>
> **Key Takeaways:**
> - Connect AI agents to external tools and data sources dynamically using the Model Context Protocol (MCP).
> - Enable agents to discover and delegate tasks to other specialist agents for expertise via A2A protocol.
> - Standardize agent-driven commerce, including secure order placement and payment authorization with UCP and AP2.
> - Allow agents to generate dynamic, context-appropriate user interfaces using simple primitives with A2UI.
> - Stream real-time agent actions and progress to users for full transparency and insight using AGUI.
>
> **Concepts:** ai agents · agent protocols · google cloud · adk · external systems · real-time ui · payments

---

## 1. Model Context Protocol (MCP) for Tool Integration
AI agents are limited in connecting to external tools without custom API definitions for each. The Model Context Protocol (MCP) solves this by allowing agents to connect to MCP servers that dynamically expose available tools at runtime. Instead of hardcoding numerous tool definitions, agents point to a few MCP server URLs and discover capabilities on the fly. For a kitchen manager agent, this means connecting to MCP servers for inventory databases, recipes, and supplier emails, enabling real data access with minimal code. MCP is particularly useful for rapid prototyping, allowing quick integration of new data sources to see how an agent leverages them.

---

## 2. Agent-to-Agent Protocol (A2A) for Expertise Delegation
While MCP provides data, agents often lack specific expertise residing in other agents or systems. The Agent-to-Agent (A2A) protocol facilitates expertise sharing through standardized agent discovery. Each specialist agent serves an "agent card" at a well-known URL, describing its capabilities. Your agent fetches these cards, discovers what each can do, and communicates via `send message` without needing to know the remote agent's underlying framework. For the kitchen manager, A2A allows it to query specialist agents for wholesale prices, food quality grades, or delivery windows, routing questions to the correct expert. A2A offers an organizational standard for discovering and delegating tasks across different teams' agents.

---

## 3. Universal Commerce Protocol (UCP) for Structured Transactions
Traditional storefronts are designed for human browsing, not machine-readable information crucial for AI agents placing orders. The Universal Commerce Protocol (UCP) standardizes how agents discover merchants, place orders, and track status. It provides a well-known `/well-known/ucp` endpoint where agents can discover a supplier's catalog and send structured checkout requests with line items, quantities, and payment details. This eliminates the need for agents to browse websites or parse HTML. The kitchen manager agent can use UCP to discover a supplier's catalog, place a typed order for ingredients like salmon, and receive a confirmed order number through a structured, machine-readable process.

---

## 4. Agent Payments Protocol (AP2) for Authorization and Audit
Placing orders via UCP still leaves questions about payment authorization, spending limits, and audit trails. The Agent Payments Protocol (AP2) introduces typed mandates (checkout and payment) and signed receipts to enforce guardrails and provide an audit trail. Checkout mandates define approved merchants and purchasable items, while payment mandates enforce spending limits, specify payment methods, and record user authorization. When the kitchen manager agent attempts a purchase, AP2 ensures it adheres to pre-configured rules (e.g., approved vendors, spending limits, manager sign-off requirements), rejecting unauthorized attempts and providing a signed receipt for legitimate transactions, ensuring accountability beyond simple instructions.

---

## 5. Agent-to-User Interface Protocol (A2UI) for Dynamic UIs
Presenting agent responses as a "huge wall of text" is often insufficient. The Agent-to-User Interface Protocol (A2UI) enables agents to generate dynamic, context-appropriate user interfaces on the fly. Instead of building separate front-end components for every scenario (e.g., reorder checklists, order forms), A2UI defines 18 simple primitives like cards, buttons, text fields, and sliders. The agent composes these primitives into a declarative JSON payload, which client renderers (e.g., Lit, Angular, Flutter) interpret into native UI components. This allows the kitchen agent to generate diverse UIs—such as a reorder checklist, an order form with a date picker, or side-by-side supplier comparison cards—all from the same set of primitives, with zero changes to the agent logic.

---

## 6. Agent-Generated User Interface (AGUI) for Real-time Streaming
Even with dynamic UIs, users need to see the agent's progress in real time rather than waiting for a final response. The Agent-Generated User Interface (AGUI) protocol standardizes streaming events from the agent to the front end. It sends typed events (e.g., `text message content`, `tool call result`, `run finished`) that indicate what tools are being called, what they return, and what the agent is "thinking." This allows users to watch the agent's full execution sequence as it happens. For the kitchen manager agent, a user can observe each protocol firing in real-time: MCP checking inventory, A2A querying specialists, UCP placing an order, and AP2 authorizing payment, all streamed sequentially to the front end.

---

## Conclusion
Traditional APIs, designed for human interaction, often fail to meet the needs of autonomous AI agents. The six protocols covered—MCP, A2A, UCP, AP2, A2UI, and AGUI—provide robust solutions for building more capable agents. MCP and A2A enable agents to access real data and consult specialist expertise. UCP and AP2 facilitate structured commerce with secure payment authorization and audit trails. Finally, A2UI and AGUI allow agents to generate dynamic, interactive user interfaces and stream their actions in real time, enhancing user experience. These protocols are independent and can be adopted incrementally based on specific agent needs, with resources available in the ADK documentation and official GitHub repositories to aid implementation.