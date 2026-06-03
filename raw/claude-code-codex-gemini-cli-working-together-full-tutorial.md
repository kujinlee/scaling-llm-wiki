---
tags:
  - video-summary
  - en
  - maestri app
  - ai development
  - multi-agent system
  - claude code
  - gemini cli
  - codex cli
  - isolated workspaces
video_id: "Mg4WUTNM1hw"
channel: "Ramanpal Singh"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# Claude Code + Codex + Gemini CLI Working Together (Full Tutorial)

**Channel:** Ramanpal Singh | **Duration:** 15:12 | **URL:** https://www.youtube.com/watch?v=Mg4WUTNM1hw

> [!summary] Quick Reference
> **TL;DR:** This video demonstrates Maestri, a canvas-based app integrating multiple AI CLIs for collaborative, efficient software development using isolated workspaces and agent roles.
>
> **Key Takeaways:**
> - Maestri unifies AI CLIs (Claude, Gemini, Codex) on a canvas for collaborative software development tasks.
> - Use 'Floors' to create isolated workspaces for feature development, merging changes safely to the main project.
> - Assign specific roles (leader, reviewer, researcher) to different AI agents for structured project collaboration.
> - Leverage embedded portals for AI agents to visually test and fix live applications directly within Maestri.
> - Automate complex development workflows and integrate testing to build sophisticated applications more rapidly.
>
> **Concepts:** maestri app · ai development · multi-agent system · claude code · gemini cli · codex cli · isolated workspaces

---

## 1. Introducing Maestri: Bridging AI CLI Collaboration

Maestri is a powerful canvas-based application designed to integrate multiple AI Command Line Interfaces (CLIs) like Claude Code, Codex, and Gemini CLI into a cohesive development environment. It enables these diverse AI agents to communicate and collaborate on a single project, streamlining the entire app development lifecycle from architecture to bug fixing. The platform acts as a central hub, allowing users to delegate specific tasks—such as frontend, backend, or security analysis—to different AI models working in concert.

---

## 2. Core Features and Workspace Management

The video demonstrates setting up a workspace within Maestri, which serves as an infinite canvas for organizing development tasks. Key features include:
*   **AI Terminals:** Launching and managing separate terminals for each AI CLI (e.g., Claude Code, Codex, Gemini), each assigned a specific role (leader, reviewer, researcher).
*   **Connectors:** Visually linking these terminals to facilitate inter-agent communication and task flow.
*   **Notes:** Adding task-specific notes that agents can read and act upon.
*   **File Attachments & Folder View:** Providing context files, prompts, and a real-time folder view to monitor generated files.
*   **Portals:** Embedding live web browsers or local hosts directly into the canvas, allowing agents to interact with and visually test applications in real-time.
*   **Drawing Tools:** Utilizing shapes and text for conceptualization and planning.
The platform also integrates "Embro AI" on Mac for contextual assistance within the workspace.

---

## 3. Advanced Collaboration with Routines and Floors

Maestri introduces advanced features to enhance productivity and project management:
*   **Routines:** Scheduling recurring tasks for AI agents to run automatically, enabling continuous background development or maintenance.
*   **Floors (Isolated Workspaces):** A standout feature allowing the creation of independent, isolated workspaces using Apple's Copy-on-write file system. This enables developers to work on specific features (e.g., backend) in a sandbox environment without affecting the main project. Once development and testing are complete, changes can be "landed" (committed) to the ground floor, ensuring the main codebase remains intact during experimental phases.

---

## 4. Building the "Client Desk" App: Architecture and Agent Roles

The video provides a detailed case study by demonstrating the creation of a "Client Desk"—a single-user freelance management tool. This project showcases Maestri's collaborative power with defined AI roles:
*   **Claude Code:** Designated as the "Leader Agent," responsible for overall project coordination, code finalization, UI development, and deployment.
*   **Gemini CLI:** Acts as the "Researcher," tasked with gathering information and insights from the internet.
*   **Codex CLI:** Functions as the "Reviewer," performing security analysis and code reviews.
The initial phase involves Claude delegating research to Gemini, which then passes its findings to Codex for review. Upon approval, Claude scaffolds the Next.js project and performs the initial Git commit.

---

## 5. Iterative Development: Backend, Frontend, and Visual Testing

The development process continues iteratively:
*   **Backend Development:** A dedicated "backend" floor is created for isolated development of backend logic and seed data. Claude deploys tasks to Codex within this isolated environment. Upon completion and verification, the changes are seamlessly "landed" onto the main ground floor, merging the new backend into the primary codebase.
*   **Frontend Development:** The frontend, consisting of nine pages, is then built.
*   **Visual Testing via Portal:** The embedded live portal is utilized for visual testing. Agents are directed to interact with the live application, review the frontend, identify any issues, and automatically implement fixes, demonstrating a robust QA process directly within the development environment.

---

## Conclusion

Maestri presents an innovative solution for AI-powered software development, effectively integrating various AI CLIs into a highly interactive and collaborative canvas. The demonstration of building a "Client Desk" app illustrates how Maestri can significantly boost efficiency, automate complex workflows, and provide an environment for iterative development and testing. The resulting fully functional "Client Desk" app, complete with a dashboard, project management, invoicing, client tracking, and robust security features, showcases the platform's capability to deliver comprehensive applications in a remarkably expedited timeframe (approx. 45 minutes for the demo). Maestri offers a glimpse into the future of augmented development, where AI agents work together seamlessly under human guidance to build sophisticated software.