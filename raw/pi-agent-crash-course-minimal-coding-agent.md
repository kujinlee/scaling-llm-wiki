---
tags:
  - video-summary
  - en
  - pi agent harness
  - ai agents
  - coding assistant
  - llm customization
  - agent framework
  - workflow automation
  - cli tool
video_id: "N30XGyPrr6I"
channel: "Alejandro AO"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.2
---

# Pi Agent – Crash Course | Minimal Coding Agent

**Channel:** Alejandro AO | **Duration:** 26:34 | **URL:** https://www.youtube.com/watch?v=N30XGyPrr6I

> [!summary] Quick Reference
> **TL;DR:** This video introduces Pi Agent Harness, a minimalist, customizable AI coding assistant focusing on personalized features via prompts, skills, and efficient session management.
>
> **Key Takeaways:**
> - Install Pi via `pip install pi` and log in using an API key from LLM providers like Hugging Face or
> - Customize agent interaction by switching LLM models, adjusting 'thinking level,' and defining custom prompt slash commands.
> - Extend functionality by integrating reusable 'skills' from specified directories and managing conversational context with `agents.md` files.
> - Personalize Pi's UI with custom themes, implement advanced features via TypeScript 'extensions,' and install community 'packages'.
> - Manage conversations efficiently by renaming, forking, compacting, and exporting sessions to HTML or JSONL files.
>
> **Concepts:** pi agent harness · ai agents · coding assistant · llm customization · agent framework · workflow automation · cli tool

---

## 1. Introduction to Pi Agent Harness & Initial Setup
Pi Agent Harness is a minimalist and highly customizable agent harness designed to grow with the user. Unlike bloated alternatives, it starts with a minimal set of tools and features, allowing users to build and add only what they need. Key functionalities like Multi-Conversation Planning (MCP), sub-agents, permission pop-ups, plan mode, and built-in to-dos are not included by default but can be easily integrated.

To get started, install Pi using `pip install pi`. After installation, simply type `pi` in your terminal. For initial use, you'll need to log in with an API key from providers like Hugging Face, ChatGPT, or GitHub Copilot (Anthropic may be discontinued for third-party harnesses). Once logged in, you can select and manage various LLM models using the `/model` command.

---

## 2. Model & Interaction Customization
Pi offers extensive control over how your agent interacts with LLMs. You can change the active model at any time using `/model` and browse available options from your connected providers. For frequent use, you can define 'scoped models' (favorites) using `/scoped models` and quickly switch between them with Ctrl+P.

For models that support it, you can also adjust the 'thinking level' (e.g., minimal, low, medium, high) by pressing Shift+Tab, allowing you to fine-tune the model's processing depth.

Custom prompt templates are another powerful feature, allowing you to create custom slash commands for frequently used prompts. Pi can even assist in generating these custom prompts (e.g., for code review), which are stored in your `.py/agent/prompts/` directory. You can manually add or copy prompts from other assistants and even create workspace-specific `.py` configurations.

---

## 3. Extending Functionality with Skills and Context
Pi integrates seamlessly with 'skills,' which are reusable scripts or tools that enhance your agent's capabilities. It automatically loads skills from your `.agents` and `.clote` directories (both home and workspace) and also supports skills placed in `.py/agent/skills`. You can activate skills using the `/skill` command and even run direct bash commands within the Pi terminal using `!` (adds to history) or `!!` (does not add to history) prefixes.

For managing conversational context, Pi adheres to the `agents.md` and `clod.md` standards. It reads both of these files from your workspace and home directories, providing the agent with relevant background information and instructions. This ensures consistency with other AI agents that follow these conventions.

---

## 4. Advanced Customization: Themes, Extensions & Packages
Pi's minimalist design extends to its user interface, allowing for complete customization, including themes. You can change existing themes or have Pi generate new ones, which require a reload to take effect. These customizations give you full control over the terminal's appearance.

The true power of Pi lies in its modularity through 'extensions.' These are essentially TypeScript files that add custom functionality, enabling you to implement features like MCP, sub-agents, permission pop-ups, or custom command guards (e.g., asking for confirmation before `rm -rf` or `git push --force`). Pi can help you write these extensions, and they can be stored globally or per-workspace in `.py/agent/extensions/`.

'Packages' are bundles of extensions, skills, and prompts created by the community. They offer pre-built functionalities like `PySubagents` or `WebSearch`, which can be installed with a single command. Users are advised to review the open-source code of packages before installation to ensure security, as they may contain executable scripts.

---

## 5. Efficient Session Management
One of Pi's standout features is its robust session management, making it easy to retrieve, edit, and navigate through your conversation threads. You can rename a session using `/name` and view its details, including its storage location within `.py/agent/sessions/`, using `/session`.

The `tree` command provides a chronological list of all messages in a session, allowing you to effortlessly jump back to any point in the conversation. You can also `fork` a session to create a duplicate and continue from a specific point or `clone` it to duplicate the current session and position.

For long conversations, Pi can `compact` your session to manage context window limits. Additionally, you can `export` any session into a visual HTML file for easy review and navigation, or download it as a JSONL file, which is highly useful for training LLMs or creating new skills.

---

## Conclusion
Pi Agent Harness truly stands out for its minimalist design, exceptional customizability, and powerful session management. It empowers users to build a personalized AI coding assistant by selectively adding features through prompts, skills, extensions, and community packages. The ability to efficiently navigate, fork, and export conversation sessions further enhances productivity, making Pi a versatile and adaptable tool for developers and AI enthusiasts. This video provides a comprehensive guide to get started, laying the foundation for further customization and exploration of Pi's capabilities.