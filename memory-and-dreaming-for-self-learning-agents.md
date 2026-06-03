---
tags:
  - video-summary
  - en
  - ai agents
  - llm memory
  - anthropic claude
  - agent self-improvement
  - organizational knowledge
  - multi-agent systems
  - context management
video_id: "IGo225tfF2I"
channel: "Claude"
lang: EN
type: Analysis
audience: Intermediate
score: 4.6
---

# Memory and dreaming for self learning agents

**Channel:** Claude | **Duration:** 21:34 | **URL:** https://www.youtube.com/watch?v=IGo225tfF2I

> [!summary] Quick Reference
> **TL;DR:** This video explains Anthropic's memory and dreaming systems, which empower Claude Managed Agents to learn from experiences and continuously self-improve over time.
>
> **Key Takeaways:**
> - Memory allows agents to learn from past experiences, avoid mistakes, and efficiently leverage tools across tasks.
> - Anthropic designs agent memory as a file system, enabling use of familiar tools like Bash and Grep.
> - Dreaming is an out-of-band batch process that analyzes session transcripts to optimize agent memory.
> - Dreaming significantly improves agent efficiency and completion rates by identifying and correcting patterns of error.
> - Memory supports multi-agent environments with shared stores, fostering collaborative intelligence and knowledge transfer.
>
> **Concepts:** ai agents · llm memory · anthropic claude · agent self-improvement · organizational knowledge · multi-agent systems · context management

---

## 1. The Evolution of Agent Capabilities & The Need for Memory
Anthropic has made significant strides in agent capabilities, from the Model Context Protocol (MCP) in 2024 to Claude Code, the Agent SDK, and Skills in 2025. These advancements culminated in Claude Managed Agents, enabling agents to operate over increasingly longer time horizons and tackle complex tasks. However, managing context effectively over these extended periods remained a challenge, highlighting the critical need for a robust memory system.

---

## 2. Introducing Memory for Claude Managed Agents
Memory is designed to empower agents to learn from past experiences, carry forward insights, and improve performance across a series of tasks. This allows agents to learn from common strategies, avoid repeating mistakes, and leverage tools or codebases more efficiently. Crucially, memory facilitates the transfer of learnings between agents, fostering collaborative intelligence. Early implementations show remarkable results, with Rakuten achieving a 97% decrease in first-pass errors and WiseDocs reducing common issues through cross-session memory, allowing teams to focus on product development rather than infrastructure.

---

## 3. Designing Memory as a File System
Anthropic's approach to memory leverages Claude's inherent strengths in navigating virtual environments and file systems. By modeling memory as a file system, agents can utilize familiar tools like Bash and Grep to read, update, and organize information, essentially letting Claude "cook" with its existing capabilities. The system supports multi-agent environments with shared memory stores, offering read-only and read-write scopes, and employs optimistic concurrency control to prevent conflicts. Enterprise-grade features include version control with audit trails, diffing capabilities, and a standalone API for comprehensive management of memory stores, including CRUD operations, exports, and redactions.

---

## 4. Dreaming: The Frontier of Self-Learning Agents
While agents can learn locally, they often suffer from inefficiencies like duplication, fragmentation, and repeating mistakes across sessions. Dreaming addresses this by providing an out-of-band, batch process that acts as a feedback loop. It analyzes session transcripts across multiple agents to identify patterns in mistakes and inefficiencies. Dreaming then automatically organizes, curates, and proposes optimizations to the memory, enabling continuous self-learning. This process has led to significant gains, such as Harvey's 6x increase in completion rates. Its decoupled architecture ensures clear objectives for memory improvement without impacting agent latency or task performance.

----- 

## 5. Practical Application: SRE Agent Demo
The presentation included a demo of an SRE agent platform utilizing both memory and dreaming. The SRE agents access a read-only organization-wide knowledge base (e.g., runbooks) and read-write task-specific memory stores. The demo highlighted cross-session memory in action: an agent investigating an alert noted a fix was in flight, and a subsequent agent, encountering a similar issue, used this shared memory to act proactively. The console view showcased audit logs, version history, and the process of kicking off a "dream." The dreaming process, itself powered by Claude Managed Agents, analyzed past sessions to identify recurring patterns (e.g., an alert consistently triggering 60 seconds after a CPU spike) and updated the memory to provide future agents with improved guidance and more holistic triage logs.

---

## Conclusion
Memory and dreaming represent foundational components for the next generation of AI agents. By enabling agents to learn and retain information over extended periods and globally optimize their knowledge base, these features are critical for developing agents that can continuously improve their understanding of complex environments. The ability for agents to self-improve and adapt over days-long timescales will unlock new levels of capability, making these memory systems an essential part of future AI development. Developers are encouraged to explore and build with these powerful new tools.