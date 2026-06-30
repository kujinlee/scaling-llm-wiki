---
tags:
  - video-summary
  - en
  - ai context
  - open knowledge format
  - model context protocol
  - okf
  - mcp
  - llm tools
  - data management
video_id: "bwQ70NMd57k"
channel: "Cloud Codes"
lang: EN
type: Framework
audience: Intermediate
score: 4.4
---

# Google OKF + MCP : Explained The New "AI Context Stack"

**Channel:** Cloud Codes | **Duration:** 8:32 | **URL:** https://www.youtube.com/watch?v=bwQ70NMd57k

> [!summary] Quick Reference
> **TL;DR:** This video explains how OKF and MCP, two open standards, form an "AI context stack" to give models durable knowledge and live access to real-world
>
> **Key Takeaways:**
> - Understand the two core problems AI faces: knowledge and access gaps.
> - Learn how OKF provides AI agents with durable, version-controlled knowledge.
> - Grasp how MCP enables AI models to interact with live tools and data.
> - Recognize that OKF and MCP together ensure AI responses are both correct and current.
> - Leverage these standards to build more reliable and context-aware AI applications.
>
> **Concepts:** ai context · open knowledge format · model context protocol · okf · mcp · llm tools · data management

---

## 1. The Core Problem: AI Lacks Context
▶ [0:00–0:18](https://www.youtube.com/watch?v=bwQ70NMd57k&t=0s)
Modern AI models, while intelligent, struggle with specific, real-time company data because they lack context. This manifests as two gaps: a knowledge gap (understanding company specifics like schema and metrics) and an access gap (inability to interact with live systems like databases or Slack).

---

## 2. Introducing OKF: The Open Knowledge Format
▶ [0:18–4:10](https://www.youtube.com/watch?v=bwQ70NMd57k&t=18s)
OKF (Open Knowledge Format) provides durable, curated knowledge, acting as the AI agent's memory. Published by Google Cloud, it uses plain markdown files organized into "bundles" (directories). Each file defines a concept (e.g., table, metric) with YAML frontmatter (including a `type` and an optional `resource` URI pointing to the real-world asset) and plain markdown for descriptions. Concepts link via standard markdown, forming a rich knowledge graph that compounds over time, preventing agents from re-discovering information.

---

## 3. Introducing MCP: The Model Context Protocol
▶ [4:10–5:34](https://www.youtube.com/watch?v=bwQ70NMd57k&t=250s)
MCP (Model Context Protocol), open-sourced by Anthropic, provides live reach, acting as the AI agent's hands. It serves as a universal plug for AI to connect to tools and fetch real-time data. It defines three roles: a host (the application), a client (connecting host to server), and a server (exposing tools, resources, and prompts). Models call tools by name with arguments, and the server executes real actions against live APIs or databases, returning structured results. MCP has seen rapid adoption across major tech platforms.

---

## 4. The AI Context Stack: OKF and MCP in Harmony
▶ [5:34–7:06](https://www.youtube.com/watch?v=bwQ70NMd57k&t=334s)
OKF and MCP are not rivals but complementary layers forming the "AI Context Stack." OKF is the "slow layer" providing meaning and definitions (e.g., "what does 'weekly active users' mean?"), while MCP is the "fast layer" enabling real-time actions (e.g., "go run that query"). Together, an agent uses OKF to understand a concept and its associated resources, then leverages MCP to execute a live query or action using that resource URI, ensuring both correctness and currency of information. MCP can even serve OKF bundles, unifying knowledge discovery and action under one protocol.

---

## 5. Benefits and Applications
▶ [7:06–8:02](https://www.youtube.com/watch?v=bwQ70NMd57k&t=426s)
The AI context stack excels for curated knowledge and real tools, complementing rather than replacing vector databases for large, unstructured document piles. Economically, OKF is low-cost, relying on Git for version control, while MCP drastically simplifies tool integrations by replacing brittle custom connectors with a universal protocol. This leads to cheaper and simpler systems. Practical applications include data teams exposing tables and metrics as OKF bundles over MCP, and on-call agents utilizing OKF runbooks to trigger actions via MCP.

---

## Conclusion
▶ [8:02–8:33](https://www.youtube.com/watch?v=bwQ70NMd57k&t=482s)
The combination of OKF for durable, version-controlled knowledge and MCP for live, governed access to tools creates a powerful AI context stack. This integration provides AI agents with both deep understanding and the ability to act on real-time data, leading to more trustworthy and effective AI applications by ensuring answers are both correct and current.