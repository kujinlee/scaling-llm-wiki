---
tags:
  - video-summary
  - en
  - agent workflows
  - LLM context window management
  - AI coding
  - handoff skill
  - developer tools
  - productivity
  - conversational AI
video_id: "dtAJ2dOd3ko"
channel: "Matt Pocock"
lang: EN
type: Tutorial
audience: Advanced
score: 4.8
---

# /handoff is my new favourite skill

**Channel:** Matt Pocock | **Duration:** 12:24 | **URL:** https://www.youtube.com/watch?v=dtAJ2dOd3ko

> [!summary] Quick Reference
> **TL;DR:** This video introduces a 'handoff skill' for AI agents, allowing users to export session context to a portable markdown for new, focused task sessions.
>
> **Key Takeaways:**
> - Use 'handoff' to create new, focused agent sessions for sub-tasks, avoiding primary session dilution.
> - Delegate out-of-scope sub-tasks or complex components to separate agent sessions using handoff.
> - Employ 'round-trip handoff' to create temporary sub-agents that distil complex problems for the parent session.
> - Ensure handoff documents are concise, secure (redacting sensitive data), and include clear purpose for the next agent.
>
> **Concepts:** agent workflows · LLM context window management · AI coding · handoff skill · developer tools · productivity · conversational AI

---

## 1. Introduction to the Handoff Skill
A few weeks ago, the speaker developed a 'handoff skill' to address limitations in managing complex AI agent conversations. This simple yet highly effective skill allows users to compress the current session's context window into a portable markdown document. The primary purpose is to enable seamless transition of work to a fresh agent or a separate session, thereby improving focus and efficiency in agent-assisted coding and planning tasks.

---

## 2. Understanding LLM Context Windows and the 'Compact' Feature
Large Language Models (LLMs) operate with context windows that contain both a 'smart zone' and a 'dumb zone'. Agent performance degrades significantly as the context window fills up, with optimal 'smart' performance typically limited to around 120k tokens. To combat this, tools like 'Compact' summarize a conversation, effectively moving the agent back into the 'smart zone' of a *single* session. While useful for long-running, linear tasks such as debugging, `Compact` maintains a continuous, accumulating context, which can lead to 'sediment' from previous states.

---

## 3. Handoff vs. Compact: Enabling Independent Workflows
The `handoff` skill offers a crucial alternative to `Compact` by allowing users to 'branch off' tasks into *separate* agent sessions. Unlike `Compact`, which keeps the work within one continuous session, `handoff` facilitates the creation of independent sessions for specific sub-tasks. This is particularly valuable when encountering out-of-scope opportunities (e.g., a refactoring idea) that would otherwise dilute the current session's focus or prematurely push it into the 'dumb zone'. Handoff ensures that the primary session remains 'pure' and focused on its original goal.

---

## 4. Practical Handoff Patterns for Enhanced Agent Interaction
The video highlights several effective patterns for utilizing the handoff skill:

*   **Delegating Sub-tasks during 'Grilling' Sessions:** During planning or 'grilling' sessions, handoff can be used to delegate specific, out-of-scope tasks (e.g., designing a new API feature) to a separate agent. This keeps the current planning session sharp and focused.
*   **Prototyping Difficult Components:** For complex logic or UI elements, a task can be handed off to a dedicated prototyping session. This allows for deep exploration and iteration without affecting the main workflow.
*   **Round-Trip Handoff:** A highly effective pattern where an initial session hands off a task to a sub-session. The sub-session then processes the task, distills its learnings, and creates a *new* handoff document to return key insights to the original parent session. This acts as a 'DIY sub-agent', efficiently utilizing dedicated context for specific problems and compressing knowledge for upstream use.

---

## 5. Design Principles and Best Practices for the Handoff Skill
The handoff skill incorporates several key design principles:

*   **Interoperability:** By generating a simple markdown document, handoff facilitates seamless context transfer between different agent tools and harnesses (e.g., Clawed Code, Codex, Copilot CLI).
*   **Automated Skill Suggestion:** The handoff document can include a 'suggested skills' section, guiding the next agent session on which tools or modes to invoke.
*   **Avoid Duplication:** The skill encourages using pointers to existing artifacts (like GitHub issues) rather than duplicating content, keeping handoff documents concise.
*   **Disposable Nature:** Handoff files are saved to the operating system's temporary directory, indicating they are transient artifacts for immediate use, not long-term documentation.
*   **Security:** It is crucial to redact any sensitive information (e.g., API keys, PII) from handoff documents.
*   **Clear Purpose Definition:** The user must explicitly define the purpose and focus of the next session when initiating a handoff, as this context is vital for the agent to generate an effective and tailored document.

---

## Conclusion
The handoff skill is presented as an indispensable addition to an AI agent user's toolkit, offering a powerful solution to the inherent challenges of LLM context window management and task delegation. By enabling modular, focused, and efficient agent interactions through portable markdown documents, it significantly enhances productivity and allows for more sophisticated, multi-agent workflows. This innovative approach fosters better task isolation, knowledge aggregation, and overall quality in AI-assisted development.