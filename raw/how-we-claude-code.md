---
tags:
  - video-summary
  - en
  - claude
  - ai agents
  - prompting
  - html specs
  - agent-native verification
  - developer workflow
  - anthropic
video_id: "IlqJqcl8ONE"
channel: "Claude"
lang: EN
type: Tutorial
audience: Advanced
score: 4.6
---

# How we Claude Code

**Channel:** Claude | **Duration:** 31:43 | **URL:** https://www.youtube.com/watch?v=IlqJqcl8ONE

> [!summary] Quick Reference
> **TL;DR:** This video details optimizing AI agent workflows with Claude using HTML specs and embedding verification directly into development artifacts for efficiency.
>
> **Key Takeaways:**
> - Let AI agents proactively extract requirements via interactive questioning for better outcomes.
> - Utilize Claude's `ask user question` tool to facilitate interactive requirement gathering.
> - Use HTML files for AI agent specifications to enable richer planning and feedback.
> - Embed agent-native verification directly into development artifacts for robust, long-running agents.
>
> **Concepts:** claude · ai agents · prompting · html specs · agent-native verification · developer workflow · anthropic

---

## 1. The Evolution of AI Agent Workflows
AI models are becoming increasingly capable, enabling agents to run for longer periods and tackle more complex tasks. This advancement necessitates a shift in traditional development practices to optimize for agentic workflows. The speaker, Ara from Anthropic's Applied AI team, introduces a new approach, building on Tar's concept of "the unreasonable effectiveness of HTML files," advocating for HTML over Markdown for specifications.

---

## 2. Optimizing Prompting for Agentic Intelligence
Drawing inspiration from Richard Sutton's "Bitter Lesson," the talk emphasizes resisting the urge to over-constrain AI models upfront. Instead, developers should allow Claude to proactively extract requirements through iterative questioning, much like a user interview. Effective prompting involves specifying domains and desired audience rather than over-defining the outcome, and crucially, leveraging Claude's `ask user question` tool to facilitate this interactive process. Recommended settings for Claude include `auto mode` and `effort: x-high`, with `fast mode` suggested for rapid spec iteration.

---

## 3. Harnessing HTML for Richer Planning and Understanding
While Markdown has served as the "lingua franca" for AI-native software development, its limitations become apparent with complex or lengthy specifications. HTML files offer a more information-dense and ergonomic format for planning and understanding, allowing for richer interaction and visual feedback. The speaker demonstrates how Claude can generate diverse HTML design directions for an app (e.g., a bill-splitting app), enabling developers to provide more nuanced feedback, including screenshots, particularly effective with Opus 4.7's enhanced vision capabilities.

---

## 4. Agent-Native Verification for Robust Development
Critical for long-running agents, verification must be embedded directly into the artifacts themselves. The workshop introduces a framework using Storybook fixtures, testing libraries, and Playwright MCP for a React to-do app. Key to this approach is having components publish their internal state as data contracts in the DOM, allowing agents to read and verify these states directly. This enables verification steps to be run in multiple ways: a human-readable dashboard, an agent-first browser experience, or headlessly in CI. The process can even record video clips of verification as evidence, a practice already adopted by Anthropic's Claude Code team.

---

## 5. Conclusion
This new methodology encourages developers to embed verification directly into the development artifacts, making them inherently agent-first. The approach, which re-arranges familiar primitives, is actively used by the Claude Code team at Anthropic. Attendees are strongly encouraged to explore the provided GitHub repository for hands-on experience and leverage Opus 4.7's vision model and fast mode for optimal results. While HTML specs might seem token-inefficient initially, they lead to fewer iterations and greater long-term efficiency.