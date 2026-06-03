---
tags:
  - video-summary
  - en
  - tmux
  - agentic engineering
  - vps
  - ai agents
  - terminal multiplexer
  - ssh
  - persistent development
video_id: "z7xyZQVK4Dg"
channel: "David Ondrej"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.2
---

# Build Anything with Tmux, Here's How

**Channel:** David Ondrej | **Duration:** 25:39 | **URL:** https://www.youtube.com/watch?v=z7xyZQVK4Dg

> [!summary] Quick Reference
> **TL;DR:** This video explains how Tmux on a VPS facilitates persistent, uninterrupted AI agent development, crucial for long-running tasks in agentic engineering.
>
> **Key Takeaways:**
> - Tmux ensures terminal sessions remain active and persistent even after disconnection, vital for long-running AI agent tasks.
> - Install Tmux locally and learn basic commands like `new`, `detach`, `attach`, and `ls` to manage sessions.
> - Deploy Tmux on a Virtual Private Server (VPS) to guarantee persistent, independent AI agent operation.
> - Use `Ctrl+B %` and `Ctrl+B "` within Tmux on a VPS to efficiently run multiple AI agents concurrently.
> - This setup allows continuous, uninterrupted AI agent development around the clock, overcoming local machine limitations.
>
> **Concepts:** tmux · agentic engineering · vps · ai agents · terminal multiplexer · ssh · persistent development

---

## 1. The Essential Role of T-Max in Agentic Engineering
T-Max, a terminal multiplexer, is presented as an indispensable tool for agentic engineers. Its core functionality allows users to run multiple terminal sessions simultaneously. Crucially, T-Max ensures that terminal sessions remain active and persistent even after disconnection, making it vital for AI agents that require hours or even days of uninterrupted operation (e.g., using `/go` or `/goal` features in tools like Hermes or Codex).

---

## 2. Getting Started with T-Max: Local Setup & Core Concepts
The video demonstrates how to install T-Max locally, using `brew install tmux` for macOS. It then introduces fundamental T-Max commands and concepts:
- `tmux new -s [session_name]`: To start a new session.
- `Ctrl+B D`: To detach from a session.
- `tmux attach -t [session_name]`: To reattach to an active session.
- `tmux ls`: To list all active T-Max sessions.
- `exit`: To close a pane or session.
The three essential building blocks of T-Max are explained: Sessions (the entire workspace), Windows (like browser tabs), and Panes (split screens within a window). This structure enables programmatic interaction between agents.

---

## 3. Unlocking Full Potential with T-Max on a VPS
To truly harness T-Max's power for agentic engineering, the video emphasizes using it on a Virtual Private Server (VPS). A VPS provides dedicated computing resources and ensures agents run persistently, independent of the local machine. The tutorial guides viewers through acquiring and setting up a VPS (using Hostinger as an example), including selecting a plan and configuring SSH access. SSH (Secure Shell) is explained as the protocol for securely accessing and controlling the VPS remotely from any device, such as a MacBook or even a smartphone.

---

## 4. Deploying and Managing AI Agents with T-Max on a VPS
After setting up a VPS and installing T-Max on it (e.g., via `apt install tmux` on Ubuntu), the video details critical configurations like enabling mouse support for easier navigation (`echo "set -g mouse on" >> ~/.tmux.conf`). It then demonstrates T-Max's multiplexing capabilities for running multiple agents concurrently:
- `Ctrl+B %`: To split the terminal horizontally.
- `Ctrl+B "`: To split the terminal vertically.
Step-by-step instructions are provided for installing and authenticating AI agent command-line interfaces, specifically Codex CLI and Claude CLI, within different T-Max panes. This setup allows agents to execute long-running development tasks using features like `/go` or `/goal`, all while the user can detach from the VPS and continue other work.

---

## 5. The Paradigm Shift: Agentic Workflow and Persistent Development
Leveraging T-Max on a VPS offers numerous advantages over local development. It eradicates concerns about battery drain, accidental laptop closure, or local internet disconnections interrupting agent progress. Developers can run multiple AI agents simultaneously, each working on different features or projects, thereby accelerating development. The ability to detach from sessions and reattach later means continuous development can occur around the clock, even while the developer is away or their local machine is off. The video illustrates this by showing agents building a web app persistently on the VPS, accessible remotely via SSH tunneling, proving the effectiveness of this setup for extensive, long-term AI-driven software development.

---

## Conclusion
The video strongly advocates for the adoption of T-Max on a VPS as a non-negotiable standard for agentic engineering. This setup is presented as essential for maximizing productivity, enabling AI agents to undertake complex, multi-hour or multi-day tasks without interruption, and ultimately positioning early adopters ahead in the evolving landscape of AI-powered software development. Viewers are encouraged to take immediate action and implement this workflow.