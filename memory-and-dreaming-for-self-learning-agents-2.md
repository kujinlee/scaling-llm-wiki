---
tags:
  - video-summary
  - en
  - anthropic
  - ai agents
  - memory systems
  - dreaming
  - multi-agent systems
  - continuous learning
  - llms
video_id: "RtywqDFBYnQ"
channel: "Claude"
lang: EN
type: Framework
audience: Advanced
score: 4.8
---

# Memory and dreaming for self-learning agents

**Channel:** Claude | **Duration:** 24:29 | **URL:** https://www.youtube.com/watch?v=RtywqDFBYnQ

> [!summary] Quick Reference
> **TL;DR:** This video introduces Anthropic's memory and "Dreaming" systems, enabling self-learning AI agents to continuously improve and manage knowledge for long-duration tasks.
>
> **Key Takeaways:**
> - Agents require continuous memory (virtual file system) to learn from experience and adapt strategies for long-duration tasks.
> - Anthropic's "Dreaming" asynchronously curates memory across agents, identifying common patterns and mistakes to boost collective intelligence.
> - The memory system offers enterprise-grade control via permissions, version history, and audit logs, scaling for multi-agent environments.
> - Dreaming ensures large knowledge bases stay fresh and relevant by proactively organizing insights from numerous agent sessions.
>
> **Concepts:** anthropic · ai agents · memory systems · dreaming · multi-agent systems · continuous learning · llms

---

## 1. The Critical Need for Agent Memory
As large language models (LLMs) and agents evolve to handle tasks spanning hours or even days, the need for continuous self-learning and sophisticated context management becomes paramount. Existing primitives like external tools (MCP) and skills have empowered agents, but a crucial missing piece for long-horizon tasks has been memory. This primitive is essential for agents to learn from their experiences, understand environments (like codebases), adapt strategies, identify common mistakes, and even share knowledge within multi-agent systems. Self-managed memory is seen as the key to developing self-learning agents that continuously improve and adapt.

---

## 2. Designing for Frontier Agent Memory
Anthropic's memory system for Claude-managed agents, now in public beta, is built on several core requirements. Firstly, it must maximize intelligence by default, allowing agents to autonomously manage their memory. This is achieved by modeling memory as a virtual file system that Claude can interact with using familiar tools like Bash and Grep. The latest models, such as Claude Opus 4.7, have shown state-of-the-art capabilities in discerning relevant content, structuring information, and organizing memory within such a file system.

---

## 3. Scaling Memory for Multi-Agent Systems and Enterprise Control
Designed for the demands of multi-agent systems, the memory primitive supports hundreds or thousands of agents running concurrently. Key features include permission scopes, allowing agents to access different memory stores with varying permissions (e.g., read-only for organizational knowledge, read-write for working memory). Optimistic concurrency, utilizing content hashes, prevents data overwrites in shared memory states. For enterprise deployment, robust control is offered through version history and attribution metadata, providing an audit log of all memory changes (who, when, what). A standalone API ensures flexibility, allowing developers to integrate memory management with external systems for tasks like PII scanning, cleanup, or cloning.

---

## 4. Introducing "Dreaming" for Autonomous Memory Curation
Recognizing the limitations of individual agent memory in complex multi-agent environments (e.g., siloed learnings, unshared patterns), Anthropic introduces "Dreaming" in research preview. Dreaming is an asynchronous, batch process that operates out-of-band from active agent sessions. It comprehensively analyzes recent agent sessions and transcripts to identify common patterns, mistakes, and successful strategies across multiple agents. From these insights, Dreaming automatically produces organized and up-to-date memory content, which can then be applied to memory stores. Early testing, such as with Harvey, demonstrated significant improvements in task completion rates (e.g., a 6x increase).

---

## 5. The Synergy of Memory and Dreaming
Dreaming's out-of-band nature is a critical design choice. It provides a holistic perspective across many agents, uncovering shared learnings that a single agent might miss, and separating the objective of memory quality from task completion. This also ensures no added latency to an agent's hot path. Furthermore, Dreaming facilitates the scaling of memory systems into vast, enterprise-scale knowledge bases. By amortizing the computational effort of organizing and curating memory upfront, similar to how search indexes are built, Dreaming ensures that large memory stores remain fresh, relevant, and efficient for numerous downstream agents. This combined approach bridges the gap between immediate, real-time agent memory and comprehensive, continuously enriched knowledge bases.

---

## 6. Real-World Application and Impact
A demonstration showcased an SRE agent reacting to alerts, equipped with both read-only organizational knowledge and a read-write SRE-specific memory store. When an alert triggered a second SRE agent, it leveraged the previous agent's learnings from the memory store, avoiding redundant investigation and significantly improving token efficiency and intelligence. The demo also highlighted the version history and concurrency features. Subsequently, a Dreaming job processed a week's worth of SRE agent sessions. It identified a recurring inefficient retry logic pattern (a 60-second delay), deduplicated entries, removed stale information, and verified the accuracy of existing memory. This proactive curation ensures future agents benefit from collective intelligence, making production agents more reliable and effective.

---

## Conclusion
Memory and Dreaming are pivotal primitives for the next generation of AI agents, particularly those designed for long-duration tasks spanning days or many hours. By enabling continuous self-learning, robust context management, and efficient knowledge curation across multi-agent systems, these capabilities are set to unlock significantly more powerful and reliable agent applications. The focus on enterprise-grade control, scalability, and autonomous improvement marks a significant step towards sophisticated, self-evolving AI systems.