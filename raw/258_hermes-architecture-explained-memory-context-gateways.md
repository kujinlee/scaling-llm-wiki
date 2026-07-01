---
tags:
  - video-summary
  - en
  - hermes agent
  - ai architecture
  - agentic loop
  - llm context
  - memory systems
  - cron jobs
  - messaging gateways
video_id: "n32qq7Kwzh0"
channel: "Hugging Face"
lang: EN
type: Analysis
audience: Advanced
score: 4.4
---

# Hermes Architecture EXPLAINED: Memory, Context & Gateways

**Channel:** Hugging Face | **Duration:** 40:29 | **URL:** https://www.youtube.com/watch?v=n32qq7Kwzh0

> [!summary] Quick Reference
> **TL;DR:** This video explains the Hermes AI agent's architecture, detailing its core agentic loop, memory systems, context management, and multi-platform messaging gateway.
>
> **Key Takeaways:**
> - Hermes uses an agentic loop: user message -> context -> LLM -> tools -> response -> memory update.
> - Context is managed via soul.md, user.md, and memory.md files, with compression for LLM efficiency.
> - Memory involves persistent markdown files, a SQLite DB for transcripts, and optional external semantic search.
> - A versatile gateway connects Hermes to multiple messaging platforms, maintaining conversation history per session.
> - Automated tasks run via an internal cron system, storing jobs in JSON and outputs in markdown files.
>
> **Concepts:** hermes agent · ai architecture · agentic loop · llm context · memory systems · cron jobs · messaging gateways

---

## 1. High-Level Architecture Overview
▶ [0:58–3:51](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=58s)
The Hermes agent is built around a core AI agent, driven by an agentic loop, and offers multiple connection interfaces. Users can interact with Hermes via a Command Line Interface (CLI), an API, or through a robust gateway that integrates with various messaging services like Telegram, email, and Slack.

The AI agent core leverages pre-installed tools and skills to perform diverse functions. Its memory system is bifurcated into external memory, supported by third-party providers such as Mem Zero, and internal memory, which records session transcripts and maintains key markdown files like `soul.md` (agent's personality) and `user.md` (user information).

---

## 2. The Hermes Agent Loop
▶ [3:51–7:52](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=231s)
The agentic loop in Hermes is a straightforward, cyclical process triggered by user input. It operates as follows:
1.  **User Message:** The cycle begins when a user sends a message to the agent.
2.  **Context Building:** Hermes dynamically constructs a comprehensive context from its internal memory and predefined prompts.
3.  **LLM Interaction:** The assembled context, along with the message history, is transmitted to the Large Language Model (LLM).
4.  **Tool Calling:** The LLM evaluates the input and determines whether to invoke any available tools (e.g., web search, file manipulation). This step can iterate if multiple tools are required.
5.  **Final Response:** Once all necessary tool actions are completed, the LLM generates and delivers a final response to the user.
6.  **Memory Update:** The agent analyzes the interaction to extract and store pertinent information, facilitating continuous learning and refinement for future engagements.

---

## 3. Agent Context Management
▶ [7:52–19:58](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=472s)
The Hermes agent constructs its operational context from a minimalist set of components, primarily markdown files. These include `soul.md`, which defines the agent's personality and goals; `user.md`, which stores information learned about the user; and `memory.md`, containing arbitrary facts and learned workflows. These files are consistently appended to the context sent to the LLM.

To effectively manage the LLM's context window and prevent overflow, Hermes implements a sophisticated context compression strategy. This mechanism is typically triggered when 50% of the context window is utilized (a customizable threshold). Upon activation, previous conversation messages are summarized and replaced with this summary, optimizing token usage. Compression checks occur before each LLM turn and as a fallback on context window errors. Token count for compression is initially estimated (characters/4) and later accurately reported by the LLM, with a rich internal prompt guiding the summarization process.

---

## 4. Understanding the Gateway
▶ [19:58–28:05](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1198s)
The gateway is a critical system that enables interaction with the Hermes agent across various messaging platforms such as Telegram, email, Slack, WhatsApp, and SMS. It maintains an `async IO loop` that continuously listens for or polls incoming messages from these diverse providers, each requiring unique configuration (e.g., webhooks, polling APIs, websockets).

The gateway's role extends to reconstructing the conversation context for each interaction. When a single message arrives, it queries a local SQLite database, using a session identifier (e.g., `Telegram + session_ID`), to retrieve the complete message history for that conversation. This history is then combined with other context elements and forwarded to the AI agent.

Furthermore, a session manager within the gateway is responsible for handling incoming messages while the agent is processing a request, allowing for actions like interrupting, steering, or queuing messages based on specific user commands.

---

## 5. Hermes Memory System
▶ [28:05–34:43](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1685s)
Hermes' memory system is structured into three primary components:
*   **Markdown Files**: `soul.md`, `memory.md`, and `user.md` are persistent files that are consistently included in the LLM's context window. They define the agent's personality, store arbitrary facts, and retain user-specific information, respectively.
*   **SQLite Database**: This local database stores full transcripts of every interaction session, allowing the gateway to retrieve complete conversation histories. It also includes a bare text table, facilitating efficient similarity searches across past conversations.
*   **External Memory**: An optional, non-default component, external memory integrates with third-party providers like MemZero, Super Memory, and Honcho. These services specialize in enhancing agent intelligence by employing methods such as semantic search or LLM-based extraction to retrieve relevant past memories. When enabled, Hermes queries external memory after the first message of a new turn, anticipating future questions and improving recall based on the evolving conversation context.

---

## 6. Cron Jobs
▶ [34:43–39:53](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=2083s)
Hermes incorporates its own internal cron system for automating scheduled tasks, such as sending daily news updates or managing Slack notifications. This system operates independently of server-level cron processes, executing a `tick` function every minute.

All scheduled cron jobs are stored in a plain JSON file located at `.hermes/cron/jobs.json`, which the `tick` function checks hourly. Upon execution, the results of each job run are saved as a markdown file within a job-specific directory under `.hermes/cron/output/`.

Notably, cron job notifications are delivered directly to the user's designated "home" messaging platform (configured during gateway setup) by the system itself, rather than by the agent invoking a "send message" tool.

---

## Conclusion
▶ [39:53–40:30](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=2393s)
This overview has provided a comprehensive, high-level understanding of the Hermes AI agent's architecture, covering its core components, operational loops, context management, communication gateway, memory systems, and automation capabilities. This detailed analysis aims to be a valuable resource for developers and enthusiasts looking to understand, build, or customize AI agents like Hermes.