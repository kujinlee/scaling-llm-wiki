---
tags:
  - video-summary
  - en
  - ai agents
  - persistent memory
  - agent memory stores
  - dreaming feature
  - LLM development
  - session management
  - anthropic
video_id: "geUv4CjPpxI"
channel: "Claude"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# Agents that remember

**Channel:** Claude | **Duration:** 28:42 | **URL:** https://www.youtube.com/watch?v=geUv4CjPpxI

> [!summary] Quick Reference
> **TL;DR:** This video introduces memory stores for persistent agent knowledge across sessions, and a "dreaming" feature to organize and enrich that cumulative memory.
>
> **Key Takeaways:**
> - AI agents gain persistent memory across sessions by attaching flexible "memory stores" as a resource.
> - "Dreaming" is an asynchronous process that optimizes memory stores by organizing, consolidating, and enriching agent knowledge.
> - Memory stores provide a file system interface, enabling agents to read and write information using tools like `bash`.
> - Composable layers of sessions, memory stores, and dreaming create a robust, scalable long-term agent memory system.
>
> **Concepts:** ai agents · persistent memory · agent memory stores · dreaming feature · LLM development · session management · anthropic

---

## 1. The Challenge of Isolated Agents
Current agent deployments, particularly on platforms like Cloud Managed Agents, face a significant limitation: individual sessions are isolated. This means an agent does not retain information learned in one session for use in subsequent sessions. This ephemeral nature severely restricts their usefulness in complex, real-world workflows that require continuity and cumulative knowledge. The demonstration highlighted this by showing an agent unable to recall information it was just told in a previous, separate session.

---

## 2. Introducing Persistent Memory Stores
To overcome agent isolation, the concept of "memory stores" has been introduced. A memory store is a persistent, file system-like storage attached as a resource to agent sessions. This attachment allows agents to read and write information across multiple sessions, effectively giving them a long-term memory. Memory stores are highly flexible, allowing for per-user or per-workspace configurations, and are mounted as a powerful file system interface for the agent, enabling tools like `bash` for exploration and `grep` for searching. The presentation demonstrates creating a memory store, attaching it to sessions, and observing how an agent can now successfully recall information learned in an earlier session.

---

## 3. Optimizing Memory with "Dreaming"
As agents continuously write to memory stores, these stores can grow unbounded and become disorganized, leading to decreased efficiency and intelligence. To address this, a feature called "dreaming" is employed. Dreaming is an asynchronous batch process that runs in the background. It takes an input memory store and a collection of past session transcripts, then uses a multi-agent harness to distill new information, fact-check, organize, consolidate duplicates, and enrich the content. This non-destructive process generates an "output memory store" that is more efficient for future agent retrieval and enhances the agent's overall intelligence.

---

## 4. Hands-on Demonstration of Memory and Dreaming
The workshop provides a practical walkthrough using both the CLI and a console interface. It begins by showcasing the base case where agents lack memory, failing to transfer information between sessions. Then, it guides users through creating a memory store, attaching it to a session, and demonstrating how the agent can now write to and read from this persistent storage. Subsequently, the demonstration covers initiating a "dream" job, monitoring its progress, and observing the generated "diff" that highlights how dreaming enriches, organizes, and refactors the memory store. Finally, it shows how to use the improved output memory store in new sessions for enhanced information recall.

---

## 5. Composable Layers for Robust Agent Memory
The presented features—sessions, memory stores, and dreaming—are designed as composable layers to build robust agent memory systems. A session represents an isolated, ephemeral conversation. Memory stores augment sessions by providing persistent information transfer across these ephemeral instances. Dreaming then acts as a background intelligence layer, continuously organizing, enriching, and managing the memory stores over time. This layered approach ensures that as the scale of agent interactions and information processing grows, the memory system remains manageable, efficient, and up-to-date, preventing disorganization and staleness. Token usage for dreaming is acknowledged to be high by design for exhaustiveness, but optimizations like caching and model selection help manage costs.

---

## Conclusion
The workshop effectively illustrated a critical challenge in current agent implementations: the lack of persistent memory across sessions. It presented Anthropic's innovative solutions: memory stores for immediate cross-session recall and dreaming for long-term memory organization, enrichment, and maintenance. By combining these features, developers can build more intelligent, efficient, and scalable agents capable of retaining and leveraging cumulative knowledge, moving beyond isolated interactions towards more coherent and useful AI applications.