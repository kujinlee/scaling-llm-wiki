---
tags:
  - video-summary
  - deep-dive
  - en
  - claude code
  - ai development
  - coding tools
  - agent swarms
  - design systems
  - obsidian integration
  - code quality
video_id: "L2JKgj7WzU4"
channel: "Nuno Tavares | Automated Marketer"
lang: EN
type: Framework
audience: Intermediate
score: 4.4
---

# 6 Claude Code GitHub Repos That Change Everything (Deep Dive)

**Channel:** Nuno Tavares | Automated Marketer | **Duration:** 21:19 | **URL:** https://www.youtube.com/watch?v=L2JKgj7WzU4

---

## The Six-Repo Stack for Claude Code

▶ [0:00–0:33](https://www.youtube.com/watch?v=L2JKgj7WzU4&t=0s)

The central premise of the video is that while Claude Code is a "good developer" out of the box, its capabilities can be dramatically enhanced by installing a specific "stack" of six GitHub repositories. The speaker contrasts the typical user who gets a "fancy autocomplete" with power users who "actually ship" with Claude by using these tools. Installing this stack transforms Claude from a good developer into a more capable, multi-faceted assistant, described as:

*   A **Senior Engineer** with discipline.
*   A **Designer** that builds.
*   A **Swarm Agent** that can run a business.

The video promises to detail each of the six repositories, explain their purpose, and provide the one-line installation commands for each.

```ascii
      +---------------------+
      |   Claude Code (Base)|
      | (Good Developer)    |
      +---------------------+
                ↓ (Stack 6 Repos)
      +---------------------+
      |   Superpowered      |
      |     Claude Code     |
      +---------------------+
                |
  +---------------------------+
  |             |             |
  ↓             ↓             ↓
+-----------+ +-----------+ +-----------+
|  Senior   | |  Designer | | Swarm     |
| Engineer  | |           | | Agent     |
+-----------+ +-----------+ +-----------+
```

## 1. Superpowers

▶ [0:33–5:39](https://www.youtube.com/watch?v=L2JKgj7WzU4&t=33s)

The first and most recommended repository is **Superpowers**. It is not just a prompt pack, but a "complete dev methodology" designed to make Claude Code significantly better.

### Components

*   **Set of Skills:** Pre-defined capabilities for Claude.
*   **Set of Agents:** Specialized autonomous entities for tasks.
*   **Set of Hooks:** Rules that trigger specific actions.
*   **Set of Configuration Files:** Pre-sets to ensure better project outcomes.

### Workflow

The Superpowers methodology forces a structured, conversational development process:
1.  **Conversation:** Before writing any code, it forces a conversation to clarify "what you're really trying to build."
2.  **Specification:** It physically writes out specification files for the project.
3.  **Planning:** It creates plans that take 2-5 minutes each.
4.  **TDD (Test-Driven Development):** It runs a "RED-GREEN-REFACTOR TDD" process, which involves designing a better system before building begins.
5.  **Execution:** It dispatches sub-agents to work on tasks in parallel.
6.  **Review:** It reviews its own code.
7.  **Completion:** It finishes the development branch and pushes the code to GitHub or saves it locally.

This process transforms Claude from a "fancy autocomplete" to a "junior engineer with discipline overnight."

```ascii
         +---------------------+
         | Red (Failing Test)  |
         +---------------------+
                   ↓
         +---------------------+
 технической  | Green (Passing Test)|
         +---------------------+
                   ↓
         +---------------------+
         | Refactor (Clean Code)|
         +---------------------+
```

### Installation

The skills "auto trigger" once installed. It can be installed directly from within the Claude Code terminal.
1.  Open the Claude terminal (e.g., by pressing `Ctrl` + `~` in VS Code).
2.  Type `/plugin` and press Enter.
3.  Superpowers should be one of the first options. If not, use the arrow keys to navigate to the search bar and type "Superpowers."

The GitHub repository is located at `github.com/obra/superpowers`.

## 2. Everything Claude Code

▶ [5:39–8:40](https://www.youtube.com/watch?v=L2JKgj7WzU4&t=339s)

This repository is an "Anthropic hackathon winner" with over 140,000 stars and is described as "battle-tested." It is a comprehensive performance optimization system for AI agent harnesses.

### Features

*   **48 specialized agents**
*   **182 skills**
*   **68 commands**
*   **Token Optimization:** Reduces token usage, which "cuts your bill in half."
*   **Memory Persistence:** Allows memory to survive across sessions.
*   **Continuous Learning:** Turns every successful action ("win") into a reusable skill.
*   **Security:** Includes CVE scanning and prompt-injection blocking via AgentShield.
*   **Cross-Harness Compatibility:** Works not only in Claude Code but also in Codex, Cursor, OpenCode, and Gemini.

### Installation

There are two primary commands for installation:
1.  Add the repo to the marketplace: `/plugin marketplace add https://github.com/affaan-m/everything-claude-code`
2.  Install the plugin: `/plugin install everything-claude-code@everything-claude-code`

The speaker notes that this package is "massive" and contains a huge number of skills, rules, and configurations.

## 3. Ruflo

▶ [8:40–11:36](https://www.youtube.com/watch?v=L2JKgj7WzU4&t=520s)

Ruflo is an advanced tool for when "one Claude isn't enough—run a hundred." It enables multi-agent orchestration for Claude Code.

### Features

*   **Agent Swarms:** Organizes over 100 specialized agents that self-organize into swarms.
*   **Shared Memory:** Memory is shared across different sessions.
*   **Federated Comms:** Agents can securely talk to each other across different machines (e.g., on a teammate's laptop) without leaking data.
*   **Extensive Plugins:** Comes with 32 plugins covering security, testing, documentation, observability, and cost tracking.

This is considered a more advanced repository for users who need to manage complex builds, minimize token usage, and deploy large teams of agents to work on big projects.

### Installation

*   `/plugin marketplace add ravnet/ruflo`
*   `/plugin install ruflo-core@ruflo`

## 4. Open Design

▶ [11:36–16:08](https://www.youtube.com/watch?v=L2JKgj7WzU4&t=696s)

The speaker's personal favorite, Open Design is described as "Anthropic's Claude Design—but open, local, and yours." It is an open-source alternative for generating high-quality designs.

### Features

*   **13 coding-agent CLIs** auto-detected on the user's machine.
*   **31 design skills**.
*   **72 brand-grade design systems** based on the design languages of major tech companies like Linear, Stripe, Vercel, Airbnb, Tesla, Apple, and Notion.
*   **Automated Workflow:** It can take a prompt (e.g., "make me a magazine pitch deck for our seed round"), pick a direction, build the project on-disk, run a "5-dimensional self-critique," and ship the final artifact.
*   **Local-First:** It operates locally on the user's machine.

This tool is highly recommended for anyone designing websites, PDFs, or other visual artifacts, as it can be used in tandem with a human front-end designer to enhance their workflow.

### Installation

There are two ways to install it:
1.  **Git Clone (via terminal):**
    ```
    git clone https://github.com/nexu-io/open-design
    cd open-design && pnpm tools-dev
    ```
2.  **Ask Claude:** Since Claude can execute terminal commands, you can simply ask it to install the GitHub repo.

The GitHub repository is located at `github.com/nexu-io/open-design`.

## 5. Obsidian Skills

▶ [16:08–17:58](https://www.youtube.com/watch?v=L2JKgj7WzU4&t=968s)

This repository acts as a bridge, allowing a user's "second brain" to "finally talk to your AI." It is designed specifically for users of the note-taking application Obsidian.

### Features

*   **Creator:** Built by Kepano, the design lead at Obsidian.
*   **Obsidian Integration:** Provides native skills for Obsidian-flavored markdown, including wikilinks, embeds, callouts, and properties.
*   **Data Access:** Can work with Obsidian's features like bases, views, filters, formulas, and JSON Canvas.
*   **Seamless Workflow:** Eliminates the need to copy-paste information between your Obsidian notes (your "second brain") and your AI. The AI can directly access and work with the knowledge stored in your Obsidian vault.

This tool is highly recommended for anyone who uses Obsidian for notes, research, or Personal Knowledge Management (PKM).

### Installation

*   `/plugin marketplace add kepano/obsidian-skills`
*   `/plugin install obsidian@obsidian-skills`

## 6. Karpathy Skills

▶ [17:58–21:14](https://www.youtube.com/watch?v=L2JKgj7WzU4&t=1078s)

This repository is the "simplest install" but "maybe the most important." It is a single `CLAUDE.md` file based on Andrej Karpathy's analysis of common mistakes Large Language Models (LLMs) make when writing code.

### Purpose

It aims to fix common LLM coding pitfalls such as:
*   Wrong assumptions
*   Hidden confusion
*   Overcomplication
*   Drive-by refactoring (changing things without a clear purpose)

### The Four Principles

The repository instills four core principles into Claude's coding behavior:
1.  **Think Before You Code:** Avoids jumping into implementation without a plan.
2.  **Build the Simplest Thing:** Prevents over-engineering.
3.  **Make Surgical Changes:** Teaches the AI to not "improve" what wasn't asked.
4.  **Define Success Criteria:** Ensures the agent loops until the task is actually complete and verified.

By installing this, you are providing Claude with a set of guidelines and models to produce higher-quality, more reliable code.

### Installation

*   `/plugin marketplace add forrestchang/andrej-karpathy-skills`
*   `/plugin install andrej-karpathy-skills@karpathy-skills`