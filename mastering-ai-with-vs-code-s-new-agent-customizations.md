---
tags:
  - video-summary
  - en
  - vs code
  - ai development
  - copilot
  - agentic ai
  - chat customizations
  - developer tools
  - plugins
video_id: "os2eqa69gko"
channel: "James Montemagno"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# Mastering AI with VS Code's New Agent Customizations

**Channel:** James Montemagno | **Duration:** 14:03 | **URL:** https://www.youtube.com/watch?v=os2eqa69gko

> [!summary] Quick Reference
> **TL;DR:** This video demonstrates how VS Code's new chat customizations unify and streamline agentic AI development by centralizing management of agents, skills, and instructions.
>
> **Key Takeaways:**
> - VS Code's new chat customizations centralize all agentic AI development assets for easy management.
> - Use the `/create` command to generate new AI agents tailored to specific development tasks.
> - The powerful `/init` command automatically updates AI agent instructions based on your project's code.
> - Customize AI agent behavior with hooks for lifecycle events and extend functionality via plugins.
> - Manage and differentiate between local, extension-provided, and built-in AI development assets.
>
> **Concepts:** vs code · ai development · copilot · agentic ai · chat customizations · developer tools · plugins

---

## 1. Introduction to VS Code Chat Customizations
VS Code is highlighted as the central hub for agentic AI development, offering a rich ecosystem of features like custom agents, skills, instructions, prompts, hooks, and plugins. The newly introduced chat customizations consolidate all these capabilities into a single, streamlined interface. This feature significantly simplifies and accelerates the AI development workflow, allowing for easy creation and management of these assets, often with AI assistance. Accessing this feature is done via a dedicated gear icon in the chat pane, leading to the "Open customizations" panel.

---

## 2. Unified Customization Management Interface
The chat customizations interface presents a comprehensive overview of all available AI development assets. On the left-hand side, users can navigate through categories such as Agents, Skills, Instructions, Prompts, Hooks, MCP Servers (Multi-Container Project Servers), and Plugins. This panel offers visibility into local, Copilot CLI, and Claude-specific customizations, distinguishing between items specific to the current workspace, those contributed by extensions, and built-in functionalities. This centralized view eliminates the previous need to search through various project folders and user settings for customization files.

---

## 3. Managing Agents, Skills, Instructions, and Prompts

### Agents
The platform allows users to view and manage custom agents, agents provided by extensions (e.g., .NET Upgrade Assistant), and built-in agents (like `ask`, `explore`, `plan`). A key feature is the ability to generate new agents with AI using the `/create` command, where users describe the agent's job (e.g., a "C# Azure function specialist"). The creation process guides users through defining the agent's scope and terminal execution preferences.

### Skills, Instructions, and Prompts

*   **Skills:** Sourced from the workspace, installed plugins (e.g., Copilot SDK, .NET plugin system), and extensions. An example shown is the `troubleshoot` skill.
*   **Instructions:** Users can define main agent instructions and context-specific guidance (e.g., C# function guidance), with options for auto-generation.
*   **Prompts:** The system includes numerous built-in prompts such as `create agent`, `create hook`, `create instructions`, `create prompt`, `create skill`, `init`, and `plan`.

---

## 4. The Power of the `/init` Command
One of the most powerful features highlighted is the `/init` command. This command is designed to automatically create or update workspace instructions for AI coding agents based on the current state and changes within the project. It intelligently explores the codebase, identifies conventions, breaks down functionality, and generates or merges instructions. The `/init` command can also suggest further customizations, helping developers evolve their AI agents alongside their projects, ensuring the instructions remain relevant and optimized. It asks for feedback and clarifies instructions during the process.

---

## 5. Advanced Customization: Hooks, MCP Servers, and Plugins

*   **Hooks:** Enable developers to create lifecycle events, such as prompting for a code commit upon session completion. These can be configured for various stages including session start, user prompt submission, pre/post-tool use, and sub-agent stops, and can trigger custom scripts.
*   **MCP Servers:** These provide model access and context. The interface lists servers like GitHub and Microsoft Docs, and those from extensions. Users can disable global MCP servers for specific workspaces and browse a marketplace for additional servers (e.g., Playwright, Unity, Azure).
*   **Plugins:** Act as collections of agents, skills, instructions, and hooks. The video demonstrates browsing and managing plugins from repositories like `.NET/skills` (covering data, diagnostics, MSBuild, etc.). Plugins can be enabled or disabled per workspace, and users can browse various marketplaces or add custom ones.

---

## Conclusion
The new VS Code chat customizations provide an indispensable, unified environment for agentic AI development. By centralizing the management and creation of agents, skills, instructions, prompts, hooks, MCP servers, and plugins, it significantly streamlines the developer workflow. Features like the AI-powered agent creation and the intelligent `/init` command for instruction updates are particularly impactful. This comprehensive feature set empowers developers to efficiently tailor their AI coding agents, making VS Code an even more potent tool for modern software development.