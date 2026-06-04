---
concept: Model Context Protocol
category: Agent Architecture & Patterns
summary: An open protocol that connects an agent to external tools and services through a standard server interface, so capabilities can be added without bespoke per-integration code.
aliases: [MCP, model context protocol, MCP server, open tool protocol, external tool integration protocol, skills over MCP, agent-to-agent communication]
related: ["[[tool-integration-hierarchy]]", "[[agent-native-infrastructure]]", "[[plugin-packaging]]", "[[computer-use-automation]]", "[[cross-tool-memory]]", "[[deterministic-workflow-orchestration]]"]
sources: [12-claude-code-features-every-engineer-should-know-subagents, every-level-of-claude-explained-in-21-minutes, every-claude-code-memory-system-compared-so-you-don-t-have-t, 26년-5월-업데이트-클로드-핵심-기능-300-활용법ㅣ코워크-skills-커넥터-어플, aie-europe-keynotes-coding-agents-ft-pi-google-deepmind-anth]
---

# Model Context Protocol

The Model Context Protocol (MCP) is an open protocol that lets a coding agent integrate with external tools and services through a standard server interface, so new capabilities can be wired in without writing a bespoke integration for each one. An agent connects to an MCP server and thereby gains access to whatever tools that server exposes — design tools, messaging platforms, databases, internal systems — turning a single open standard into a doorway onto a large and growing ecosystem of publicly available tools. It is the heaviest, most capable tier in the corpus's `[[tool-integration-hierarchy]]`: maximally expressive, and reached when lighter integrations cannot represent the task.

## Key Mechanics

- **Standard server interface**: capabilities are published by an MCP *server*; the agent is an MCP *client* that connects to it, so the same protocol fronts arbitrarily different backends rather than each tool requiring its own adapter.
- **Ecosystem access**: connecting to a server (the corpus cites Figma and Slack as examples) grants the agent a whole set of external tools at once, significantly extending its operational scope beyond the local machine.
- **Open and tool-agnostic**: because the protocol is open, any compliant tool can be consumed by any compliant agent, which is what makes it the universal integration seam — the same property that lets `[[cross-tool-memory]]` expose one memory store to every assistant through an MCP server.
- **Tools ship their own interfaces**: an MCP server lets a service publish not just data but its *own* tools and rich semantics to agents, with centralized authorization — so a provider exposes an agent-ready surface rather than the agent scraping a human one (`[[agent-native-infrastructure]]`).
- **One artifact among many in a workflow**: an MCP connection is a capability source that a `[[deterministic-workflow-orchestration]]` node or a packaged `[[plugin-packaging|plugin]]` can bundle and invoke alongside skills, hooks, and sub-agents.

## How It Appears in the Corpus

The ByteByteAI "12 Claude Code Features" overview presents MCP (which the video calls a "Multi-Agent Communication Protocol"; the established term is Model Context Protocol) as an open protocol that lets Claude Code integrate with external tools and services such as Figma or Slack, gaining access to a vast ecosystem of publicly available tools by connecting to an MCP server. The Nate Herk "Every Level of Claude" overview places MCP at the end of the `[[tool-integration-hierarchy]]` — the most capable but most token-expensive integration, used when CLI tools, APIs, and skills cannot. The Simon Scrapes memory comparison uses an MCP server as the universal front door of a `[[cross-tool-memory]]` store so any MCP-capable tool can query the same memory. The 이동훈의 루트AI ("Claude core-features 300% guide") tutorial shows the consumer surface of the same integration seam: "Connectors" link Claude to external tools (Google Drive, Gmail, Google Calendar, Notion) so it can pull in data and act across them — e.g. summarizing and organizing incoming mail by connecting to Gmail — pre-packaged one-click integrations standing on the same external-tool-bridge idea as a developer-wired MCP server.

The AIE Europe keynotes (AI Engineer channel; the transcript's "Monocontext Protocol" is a transcription error for Model Context Protocol) frame MCP as critical *infrastructure* for the future of agents: a way for agents to ship their own interfaces and tools with rich semantics and centralized authorization, reported at 110M+ monthly downloads. Planned improvements include stateless transport, agent-to-agent communication primitives, and "skills over MCP" — and a 2026 vision of general agents performing complex knowledge work atop a connectivity stack of skills, CLI tools, and MCP. This places MCP not as one integration option among many but as the standard backbone the rest of the agent ecosystem is expected to build on.

## Tensions & Tradeoffs

- **Capability vs. token cost**: the corpus's two framings are complementary, not contradictory — the `[[tool-integration-hierarchy]]` ranks MCP *last by token cost* (its tool schemas are heavy in context), while this page emphasizes the *breadth of capability* that connecting buys. The discipline is to reach for MCP when lighter tiers cannot express the task, not to default to it.
- **Standardization vs. brittleness elsewhere**: MCP gives a robust programmatic interface where one exists, the structural opposite of `[[computer-use-automation]]`, which scrapes a human GUI when no API/protocol is offered — MCP is preferable wherever a server can be stood up.
- **Security and trust surface**: granting an agent access to an ecosystem of external tools through a server widens what it can touch, so an MCP connection is infrastructure to secure and scope (paired with `[[permission-tiering]]`), not merely a convenience — a concern sharpened when MCP servers are bundled into shareable `[[plugin-packaging|plugins]]`, and one the protocol's centralized-authorization direction is meant to address.
- **Ecosystem dependence**: the value of MCP scales with the available servers, so its usefulness for a given task is bounded by whether someone has published a server for it — an `[[agent-native-infrastructure]]` precondition rather than a guarantee.
- **A moving standard**: planned shifts (stateless transport, agent-to-agent primitives, "skills over MCP") mean the protocol's surface is still evolving, so building deeply on today's MCP carries the risk that its primitives change underneath — the cost of standing on a backbone that is still being poured.
