---
tags:
  - video-summary
  - en
  - claude code
  - ai memory
  - llm memory systems
  - knowledge management
  - semantic search
  - rag
  - memory architecture
video_id: "UHVFcUzAGlM"
channel: "Simon Scrapes"
lang: EN
type: Analysis
audience: Advanced
score: 4.8
---

# Every Claude Code Memory System Compared (So You Don't Have To)

**Channel:** Simon Scrapes | **Duration:** 41:21 | **URL:** https://www.youtube.com/watch?v=UHVFcUzAGlM

> [!summary] Quick Reference
> **TL;DR:** This video details six levels of Claude Code memory systems, from simple files to universal AI memory, suitable for diverse needs.
>
> **Key Takeaways:**
> - Keep `claude.md` under 200 lines to avoid 'context rot' in Claude Code.
> - Organize memories into structured topic files (`general.md`, `domain.md`) for consistent recall.
> - Utilize semantic search plugins like `MemSearch` for meaning-based query results beyond keywords.
> - `Mem Palace` provides verbatim conversation recall, ideal for precise past decision retrieval.
> - Implement `Open Brain` for a user-owned, universal memory across all your AI tools.
>
> **Concepts:** claude code · ai memory · llm memory systems · knowledge management · semantic search · rag · memory architecture

---

## 1. Native Claude Code Memory Systems (Levels 1 & 2)
This section introduces the foundational memory systems built into Claude Code: `claude.md` and `memory.md`. `claude.md` stores rules, brand information, and coding styles, loaded at the start of every session. A common pitfall is overloading this file, leading to 'context rot'; it's recommended to keep it under 200 lines and reference external files for more extensive context. Claude Code's auto-memory feature creates `memory.md` files project-by-project, serving as an index to separate, more granular memory documents.

Building on this, Level 2 introduces a structured memory system, often implemented via `claude.md` prompts and session start hooks. This method organizes memories into `general.md` (cross-project facts), `domain/topic.md`, and `tools/tool.md` files, ensuring consistent and automatic loading of relevant context. This approach significantly improves the reliability of memory injection and offers potential for team collaboration on shared knowledge.

---

## 2. Advanced Context Retrieval with Semantic Search (Level 3)
Level 3 addresses the limitations of keyword search and scaling issues as memory files grow. It introduces semantic search capabilities, primarily through the `MemSearch` plugin for Claude Code. Inspired by OpenClaude's memory architecture, `MemSearch` maintains a `memory.md` file for long-term facts, daily notes for short-term logs, and an optional 'dreaming' process to promote frequently accessed information to long-term memory. 

`MemSearch` works by chunking documents into semantic vectors, allowing Claude Code to understand the meaning behind queries rather than just keywords. It uses a `user prompt submit` hook to automatically inject the top three semantically relevant memory matches into every prompt. An alternative, `Claude Mem`, offers more features like a dashboard and team collaboration but stores data in a less readable format and relies on Claude actively calling a search tool.

---

## 3. Verbatim Conversation Recall with Mem Palace (Level 4)
For situations requiring precise, word-for-word recall of past conversations, Level 4 introduces the `Mem Palace` framework. This RAG (Retrieval Augmented Generation) system stores content verbatim, ensuring no information is lost through summarization. It utilizes a sophisticated indexing method (AAAK dialect) that points to exact locations of data stored in 'wings', 'rooms', 'closets', and 'drawers' within two separate databases: an SQL database for entities and relationships, and a Chroma DB for searchable chunks.

`Mem Palace` silently stores and indexes information using Claude Code hooks on session end or pre-compaction. This allows Claude to search every conversation in plain English, word for word, with extremely high efficiency. While the verbatim content isn't directly stored in readable markdown files, its rapid and precise retrieval capabilities make it ideal for recalling exact decisions or discussions.

---

## 4. Building Interconnected Knowledge Bases (Level 5)
Level 5 shifts focus from conversational memory to building a comprehensive, interconnected knowledge base from consumed content like articles, videos, podcasts, and client notes. This is ideal for those who regularly consume and need to retain and connect vast amounts of information, essentially creating a 'second brain'.

Andre Karpathy's LLM Wiki pattern is a prominent example, using two folders: `raw` (for source documents, read-only by Claude) and `wiki` (Claude-owned, where it writes and maintains cross-referenced markdown files). This system can be visualized and navigated using tools like Obsidian. `Recall` is a hosted alternative that automates the LLM Wiki setup with a browser extension, summarizing and tagging content into a knowledge graph. However, `Recall` involves data ownership concerns (data on their servers) and is primarily geared towards content consumption rather than operational memory.

---

## 5. Universal, Cross-Tool AI Memory (Level 6)
Level 6 addresses the challenge of managing memory across multiple AI tools (e.g., Claude Code, ChatGPT, Cursor, phone apps). The `Open Brain` framework by Nate Jones provides a future-proof and portable solution where all AI tools can access the same memory automatically in real-time. This system centralizes memory in a user-owned Postgres database (e.g., hosted on Superbase), with each 'thought' as a row containing text, an embedding vector, tags, and a timestamp.

`Open Brain` uses an MCP server from Claude Code connected to Superbase's edge functions, acting as a universal front door for any AI tool to query the database. While setup is more complex, it offers maximum ownership, portability, and low running costs. `Mem0` is a production-ready, well-funded alternative offering similar cross-tool memory, but it's a hosted service, meaning data resides on their servers. Open Brain provides user control over the data, making it a stronger choice for those prioritizing ownership.

---

## Conclusion
Choosing the right memory system for Claude Code depends heavily on your specific needs and usage patterns. Beginners should start with Level 1, utilizing `claude.md` and `memory.md` effectively. Intermediate users will benefit significantly from Level 2's structured memory and hooks. For those with substantial context and a need for improved recall over months of work, Level 3's `MemSearch` (for semantic search) or Level 4's `Mem Palace` (for verbatim recall) are highly recommended.

Levels 5 and 6 cater to more specialized use cases: Level 5 (LLM Wiki, Recall) for building interconnected knowledge bases from consumed content, and Level 6 (Open Brain, Mem0) for establishing a universal, portable memory accessible across all your AI tools. The speaker personally implements up to Level 3 in their agentic operating system, combining OpenClaude conventions with semantic search and hooks to enhance search and recall functionality.