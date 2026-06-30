---
tags:
  - video-summary
  - en
  - hermes agent
  - llm architecture
  - ai agent
  - agentic loop
  - context management
  - memory systems
  - cron jobs
video_id: "n32qq7Kwzh0"
channel: "Hugging Face"
lang: EN
type: Analysis
audience: Intermediate
score: 3.6
---

# Hermes Architecture EXPLAINED: Memory, Context & Gateways

**Channel:** Hugging Face | **Duration:** 40:29 | **URL:** https://www.youtube.com/watch?v=n32qq7Kwzh0

> [!summary] Quick Reference
> **TL;DR:** This video explains the modular Hermes AI agent architecture, detailing its agentic loop, context building, multi-platform gateway, and comprehensive memory management.
>
> **Key Takeaways:**
> - Hermes utilizes a modular architecture with an AI agent core, accessible via CLI, API, or messaging gateways.
> - The agentic loop processes messages, builds context, uses LLMs, executes tools, and learns from interactions.
> - Context is dynamically built from markdown files (soul, user, memory), skills, and compressed message history.
> - A gateway system handles multi-platform communication, managing sessions and conversation history via SQLite.
> - Memory combines persistent markdown files, a SQLite database, and optional external memory providers.
>
> **Concepts:** hermes agent · llm architecture · ai agent · agentic loop · context management · memory systems · cron jobs

---

## 1. High-Level Architecture Overview
▶ [0:58–3:58](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=58s)
The Hermes AI agent features a simple, modular architecture centered around an AI agent core. It can be accessed via a command-line interface (CLI), an API, or a gateway connecting to various messaging services like Telegram, email, and Slack. The agent comes pre-installed with a suite of tools and skills, along with a dual memory system: internal memory (session transcripts, soul.md, user.md) and external memory (providers like MemZero).

---

## 2. The Agent Loop
▶ [3:58–7:52](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=238s)
The core of Hermes operates on a straightforward agentic loop, triggered by every user message. The steps include: the user sends a message, Hermes builds its context (integrating internal memory and prompts), this context and message history are sent to the Large Language Model (LLM), the LLM decides whether to call and execute tools, and finally, it provides a response. A crucial "memory update" step follows, where the agent analyzes the interaction to learn and store relevant information, enabling continuous improvement.

---

## 3. Context Building and Compression
▶ [7:52–20:21](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=472s)
Hermes constructs its context from several markdown files: `soul.md` for defining the agent's personality and goals, `user.md` for storing learned information about the user, and `memory.md` for arbitrary facts, workflows, and insights. Additionally, the context includes descriptions of available skills and tools, and recent message history. To manage LLM token limits, Hermes employs context compression. When the message history exceeds a set threshold (default 50% of the context window), previous messages are summarized and appended to the context, replacing the original verbose history. This check occurs before each LLM turn and on context window errors.

---

## 4. The Gateway System
▶ [20:21–28:10](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1221s)
The gateway is a critical component that allows Hermes to communicate with users across multiple messaging platforms (Telegram, WhatsApp, email, Slack). It operates an asynchronous I/O loop that continuously polls these services for incoming messages. The gateway's responsibilities include listening for messages, formatting them correctly, and constructing the full conversation context (including message history from a local SQLite database) before sending it to the AI agent. It also features a session manager to handle message flow, allowing users to interrupt, steer, or queue commands.

---

## 5. Memory Management
▶ [28:10–34:53](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1690s)
Hermes manages memory through three primary mechanisms. Firstly, markdown files (`soul.md`, `memory.md`, `user.md`) provide persistent context for personality and learned facts. Secondly, a local SQLite database stores full transcripts of all user sessions, enabling efficient retrieval of conversation history. This database also maintains a bare text table for similarity searches. Thirdly, optional external memory providers (e.g., MemZero, Super Memory) can be integrated to enhance the agent's ability to recall relevant information from past interactions, dynamically querying for context after the initial user message in a conversation.

---

## 6. Cron Jobs for Automation
▶ [34:53–40:30](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=2093s)
Hermes supports cron jobs for scheduling automated tasks. This system is an internal loop that runs every minute, executing a 