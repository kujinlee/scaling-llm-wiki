---
tags:
  - video-summary
  - deep-dive
  - en
  - hermes agent
  - ai agent architecture
  - large language models
  - context management
  - memory systems
  - messaging gateways
  - cron jobs
video_id: "n32qq7Kwzh0"
channel: "Hugging Face"
lang: EN
type: Analysis
audience: Intermediate
score: 4
---

# Hermes Architecture EXPLAINED: Memory, Context & Gateways (Deep Dive)

**Channel:** Hugging Face | **Duration:** 40:29 | **URL:** https://www.youtube.com/watch?v=n32qq7Kwzh0

---

## High-Level Architecture Overview
▶ [0:58–1:21](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=58s)
The Hermes agent has a simple architecture with a few core components. At the center is the AI Agent Core, which contains the main "agentic loop." There are several ways for a user to connect to this core.

### Connection Methods
▶ [1:21–2:06](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=81s)
There are three primary ways to interact with the Hermes agent's core:
1.  **CLI (Command Line Interface)**: This is the most direct method, invoked by typing `Hermes` on the command line.
2.  **Gateway**: An always-running system that allows the agent to connect to various external messaging services like Telegram, email, and Slack. This component is key to its popularity.
3.  **API**: The agent can also be interacted with via an API.

```ascii
      +-----------------+
      |       CLI       |
      +-----------------+
              ↓
+-----------------------------+     +-----------------+
|           Gateway           | --> | AI Agent Core   |
| (Telegram, Slack, Email)    |     | (Agentic Loop)  |
+-----------------------------+     +-----------------+
              ↑                             |
      +-----------------+                   |
      |       API       |                   |
      +-----------------+                   ↓
                                +---------------------------+
                                |    Connected Services     |
                                | (Tools, Skills, Memory)   |
                                +---------------------------+
```

### Connected Services and Components
▶ [2:06–3:55](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=126s)
The AI Agent Core connects to several other services and components that come pre-installed with Hermes:
*   **Tools**: A collection of available functions the agent can use, such as web search, reading/writing files, etc.
*   **Skills**: A set of available skills for the agent to leverage.
*   **Memory**: The agent's memory system is divided into two distinct parts:
    *   **External Memory**: This involves connecting to third-party providers like Mem Zero for more advanced memory capabilities. This is an optional setup.
    *   **Internal Memory**: This consists of local files. It includes **session transcripts** from every conversation and key markdown files like `soul.md` (defining the agent's personality) and `user.md` (containing information about the user).

## The Agent Loop
▶ [3:55–7:52](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=235s)
The agent loop is a simple, iterative process that runs every time a user sends a message. It is similar to the loops found in minimalist agents like Pi agent or Open Code.

The process follows these steps:
1.  **User Sends Message**: The loop is initiated by user input.
2.  **Build Context**: Hermes assembles the context for the language model. This context includes the system prompt, contents of `soul.md` and `user.md` files, the message history, and other relevant information.
3.  **Send to LLM**: The complete context is sent to the Large Language Model (LLM).
4.  **Tool Calls (Optional Loop)**: The LLM may decide to call one or more tools (e.g., `web_search`, `write_file`). If it does, the tool is executed, and the result is returned to the LLM. This can happen multiple times until the LLM decides it has enough information.
5.  **Final Response**: Once all necessary tool calls are complete, the LLM generates a final response for the user.
6.  **Memory Update**: After providing the response, the agent analyzes the interaction to see if any new information is worth remembering. If so, it updates its memory. This step enables the agent to learn and improve over time.

```ascii
                  +---------------------+
                  | User Sends Message  |
                  +---------------------+
                            ↓
                  +---------------------+
                  |   Builds Context    |
                  +---------------------+
                            ↓
                  +---------------------+
                  |   Sends to LLM      |
                  +---------------------+
                            ↓ (Decides to use tool)
+-----------------------------------------------------------+
|                 +---------------------+                   |
|                 |    Calls Tool(s)    | <-----------------+
|                 +---------------------+                   | (Continues using tools)
|                           ↓ (Returns result)              |
|                 +---------------------+                   |
|                 |   Executes Tool     |                   |
|                 +---------------------+                   |
+-----------------------------------------------------------+
                            ↓ (Finishes tool use)
                  +---------------------+
                  |  Gives Final        |
                  |  Response to User   |
                  +---------------------+
                            ↓
                  +---------------------+
                  |  Updates Memory     |
                  +---------------------+
```

## Context Construction
▶ [7:52–8:18](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=472s)
The context sent to the LLM is constructed from several sources, primarily a series of markdown files and other dynamic information. This process is a key step in the agent loop.

### Markdown Files
▶ [8:18–11:41](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=498s)
The core of the context comes from three specific `.md` files:
*   **`soul.md`**: This file defines the agent's **personality**. It contains instructions on its tone, goals, and overall behavior, similar to a detailed system prompt. If this file is empty, a default system prompt is used which identifies the agent as "Hermes a virtual assistant."
*   **`user.md`**: Located in the `memory/` directory, this file stores information about the user that Hermes learns from conversations. For example, if a user mentions they are a "software engineer," the agent will automatically update this file.
*   **`memory.md`**: Also in the `memory/` directory, this file is for storing "arbitrary facts" and memories that are not specifically about the user. This can include information about how to use tools, notes on workflows, or interesting things learned during conversations. The agent also updates this file automatically.

### Other Context Components
▶ [11:41–13:32](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=701s)
In addition to the markdown files, the context includes:
*   **Information from External Memory**: If an external memory provider is configured, summaries of relevant past conversations are included. This is not enabled by default.
*   **Skill and Tool Descriptions**: The definitions and descriptions of available skills and tools are added to the context so the LLM knows how to use them.
*   **Messages**: The recent message history from the current conversation is appended. If the conversation becomes too long and exceeds a certain token threshold, it is summarized.

## Context Compression
▶ [13:32–14:09](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=812s)
To manage the limited context window of LLMs, Hermes employs a context compression mechanism. When a conversation's length exceeds a pre-defined threshold, the message history is summarized.

### Triggering Compression
▶ [14:09–16:17](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=849s)
*   **Threshold**: By default, compression is triggered when the context size reaches **50%** of the model's total context window. This threshold is customizable during setup and can be set higher (e.g., 70-80%) for models with smaller context windows.
*   **Checkpoints**: The agent checks if compression is needed at two key moments:
    1.  **Before each turn**: After the user sends a message and before the context is sent to the LLM.
    2.  **On error**: If the LLM returns an error indicating the context window was exceeded.

### Token Estimation
▶ [16:17–18:21](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=977s)
Hermes uses a two-stage process for estimating the token count to decide when to compress:
1.  **Before the first LLM call**: Since the exact token count isn't known, it uses a simple approximation: `total number of characters / 4`. If this approximation exceeds the threshold, compression is triggered.
2.  **After the first LLM call**: Subsequent checks are more accurate. The agent uses the `usage` data returned in the LLM's API response, which provides the precise number of input and output tokens used.

### The Compressor Prompt
▶ [18:21–20:20](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1101s)
The prompt used for summarizing the conversation is detailed and structured. It asks the LLM to generate a summary with multiple sections, including:
*   Full goal
*   Constraints
*   Completed actions
*   Active state
*   Historical progress
*   What the agent is blocked on
*   Key decisions made
*   Resolved questions
*   Relevant files
*   Critical context
*   Previous summaries

This approach is noted as being much richer and less minimalist than the one used by the Pi agent.

## The Gateway
▶ [20:20–20:56](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1220s)
The gateway is the component that allows Hermes to connect with external messaging platforms like Telegram, WhatsApp, Slack, and email. It is a crucial feature that contributes significantly to the agent's popularity.

### Core Functionality
▶ [20:56–24:03](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1256s)
The gateway runs a continuous `async IO` loop to listen for incoming messages from configured services. Each service integration is unique and must be configured independently. The connection methods vary by service and can include:
*   Webhooks
*   Polling loops (e.g., checking the Telegram API every second)
*   Websockets

When a message is received, the gateway's responsibility is to format it correctly and pass it to the AI agent core.

### Context and History Management
▶ [24:03–26:39](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1443s)
Since messaging platforms are stateless (i.e., they only send the latest message, not the whole conversation), the gateway must reconstruct the conversation history for each incoming message.
1.  **Receives a single message**: For example, from Telegram.
2.  **Identifies the session**: It creates a unique session identifier, often by combining the gateway name and the session ID from the platform (e.g., `Telegram-<session_id>`).
3.  **Queries the database**: It uses this identifier to query a local **SQLite database**, which stores the full transcripts of all past conversations.
4.  **Rebuilds message history**: It retrieves the message history for that session from the database.
5.  **Constructs full context**: It combines this history with the other context elements (`soul.md`, tools, etc.) before sending it to the agent loop.

### Session Manager
▶ [26:39–28:05](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1599s)
The gateway also includes a "session manager" that handles situations where the user sends multiple messages while the agent is still processing a previous one. It decides how to handle the new message based on user commands:
*   **Queue**: By default, the new message is queued to be processed after the current task is finished.
*   **Interrupt**: A command like `/interrupt` will stop the agent's current task.
*   **Steer**: A command like `/steer` will attempt to guide the agent's current task without stopping it.

## Memory Management
▶ [28:05–28:31](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1685s)
Hermes utilizes a multi-layered memory system to retain information across conversations. The memory is composed of three main types.

### 1. Markdown Files
▶ [28:31–29:32](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1711s)
These are plain text files that are always loaded into the agent's context.
*   **`soul.md`**: Defines the agent's core personality.
*   **`memory.md`**: Stores arbitrary facts and learned information.
*   **`user.md`**: Stores facts learned specifically about the user.
The latter two files are located in a `memory/` subdirectory.

### 2. SQLite Database
▶ [29:32–31:03](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1772s)
Hermes maintains a local SQLite database that stores the **full transcripts of all sessions**. Every single message from every interaction is saved here. This database is the source for reconstructing conversation histories, especially for interactions via the gateway. The database also contains a "bare text" table with just the text of all conversations, optimized for similarity searches.

### 3. External Memory
▶ [31:03–34:49](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=1863s)
This is an optional feature that is not configured by default but is highly recommended. It integrates with third-party memory providers to give the agent more powerful, long-term memory capabilities.
*   **Supported Providers**: Examples include **MemZero**, **Super memory**, and **Honcho**.
*   **Functionality**: Each provider works differently. Some use similarity search, while others use LLMs to extract relevant memories from past conversation histories.
*   **Query Cadence**: When enabled, the external memory is not queried before every message. Instead, it is queried **after the first message** of a conversation. This allows the agent to first understand the topic of the current conversation and then search for relevant long-term memories to use in subsequent responses.

## Cron Jobs
▶ [34:49–35:13](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=2089s)
Cron jobs allow users to schedule recurring tasks for the Hermes agent to perform automatically. Examples include sending a daily email with AI news or posting a weekly update to a Slack channel.

### Execution Loop
▶ [35:13–37:01](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=2113s)
The cron system in Hermes is self-contained and not tied to the server's system-level cron. It operates on its own loop:
1.  A `tick` function runs **every minute**.
2.  In each tick, the function checks a list of scheduled jobs to see if any are due to run at that particular minute.
3.  If a job is due, it is executed.

### Storage and Output
▶ [37:01–38:54](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=2221s)
Contrary to some documentation that may suggest SQLite, the cron jobs are stored in a plain JSON file.
*   **Job Definitions**: All scheduled jobs are listed in a file located at `~/.hermes/cron/jobs.json`. This file contains the prompts and schedules for each task.
*   **Output Logs**: The output of each cron job execution is stored as a markdown file. These are organized in the `~/.hermes/cron/output/` directory, with subdirectories for each `job_id`, containing the `run.md` files for each execution.

### Notification Delivery
▶ [38:54–40:30](https://www.youtube.com/watch?v=n32qq7Kwzh0&t=2334s)
When a cron job completes, it sends a notification. This notification is not sent via a standard `send_message` tool call. Instead, the system automatically delivers it to the user's "home" messaging platform. The "home" platform is designated during the gateway setup (e.g., a specific user ID on Telegram can be set as the home destination).