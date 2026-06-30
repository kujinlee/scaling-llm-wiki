---
tags:
  - video-summary
  - en
  - archon
  - jira integration
  - ai coding assistant
  - llm workflow
  - developer tools
  - atlassian api
  - webhook
video_id: "qyB52HIiou8"
channel: "Cole Medin"
lang: EN
type: Tutorial
audience: Advanced
score: 4.4
---

# Archon + Jira: Drag a Ticket, Get a Pull Request (Live Build)

**Channel:** Cole Medin | **Duration:** 2:29:31 | **URL:** https://www.youtube.com/watch?v=qyB52HIiou8

> [!summary] Quick Reference
> **TL;DR:** This video demonstrates integrating Archon, an AI coding framework, with Jira to automate development tasks, allowing AI agents to generate pull requests directly from tickets.
>
> **Key Takeaways:**
> - Archon automates software development using AI, following a Plan, Implement, Validate (PIV) workflow.
> - Integrating AI like Archon with Jira allows agents to manage dev tickets, automating PR generation.
> - Jira integrations require Atlassian API tokens for authentication and webhooks for real-time communication.
> - The PIV loop provides a robust, iterative framework for building and debugging complex AI-driven integrations.
> - Expect frequent debugging challenges like API errors, misconfigurations, and AI model quirks in live builds.
>
> **Concepts:** archon · jira integration · ai coding assistant · llm workflow · developer tools · atlassian api · webhook

---

## 1. Introduction to Archon and Jira Integration
The video introduces **Archon**, an open-source framework for building deterministic and repeatable AI coding workflows. The main goal is to integrate Archon with **Jira**, a widely-used enterprise development tool, to enable AI agents to manage development tickets end-to-end. The vision is to have a dedicated AI agent per Jira ticket, allowing users to converse with Archon within each ticket to plan, build, and validate tasks, ultimately leading to automated pull request generation. The speaker notes Jira's pervasive use in 80% of organizations and individuals, making this integration highly valuable. Archon already supports various adapters like Web, CLI, Telegram, Slack, GitHub, and Discord, and the new Jira integration will be added as a "community adapter."

---

## 2. Building the Jira Adapter using the PIV Loop Workflow
The speaker demonstrates building the Jira adapter itself by leveraging an existing Archon workflow called "PIV System Evolution." This workflow is designed to automate software development tasks, taking a GitHub issue as input and outputting a pull request. The "PIV" stands for Plan, Implement, Validate, and System Evolution, a continuous loop for refining both code and the AI layer. The workflow incorporates human approval gates at key stages (planning and implementation) to ensure oversight. The initial model strategy involved using Claude Opus for planning (due to its stronger reasoning) and a faster, more token-efficient model like Sonnet or Kimmy for implementation. *However, the speaker later realizes an older workflow version used Opus for implementation.*

---

## 3. Setting Up Authentication and Webhooks
A crucial part of the integration involves configuring authentication and communication channels. The Archon Jira adapter requires an **Atlassian API token** along with the Jira domain and user email for HTTP basic authentication. The workflow guides the setup of necessary environment variables, including `JIRA_DOMAIN`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_WEBHOOK_SECRET`, and `JIRA_BOT_MENTION`. The integration relies on a **webhook** for inbound communication (Jira sending notifications to Archon when a bot is mentioned in a comment) and the **Jira API** for outbound actions (Archon posting replies or fetching comment history). `ngrok` is used to create a public tunnel for the local Archon instance to receive webhook events.

---

## 4. Debugging and Iterating on the Integration
The live stream features extensive debugging as the Archon workflow iteratively builds and tests the Jira adapter. Several issues were encountered and resolved:
*   **Claude Code Glitches:** Frequent pauses, "thinking" states, and UI anomalies in the Claude Code environment.
*   **Command Errors:** Claude hallucinating incorrect `archon chat` commands instead of `archon workflow approve`.
*   **Webhook Configuration:** A typo in the webhook URL, incorrect secret handling, and Jira sending comment bodies as plain text (not ADF JSON) required code modifications to the adapter.
*   **API Authentication:** Initial 401 errors with the Jira API token, later resolved by verifying the correct key and ensuring it was actively used.
*   **Environment Variables:** A specific `Jira base URL` variable was incorrectly assumed by Claude instead of `Jira domain`.
*   **Mention Detection:** The bot was initially expecting a Jira account ID for mentions, but the speaker intended a simpler `@archon` string, requiring code adjustments.
Despite the challenges, each issue was systematically identified and addressed through the iterative PIV loop, demonstrating the resilience of the workflow.

---

## Conclusion
The live stream concludes with the successful integration of Archon and Jira. The adapter is fully functional, capable of detecting `@archon` mentions in Jira tickets and posting AI-generated replies. The speaker expresses satisfaction with achieving the core functionality, acknowledging the learning curve and debugging inherent in live development. Future plans include publishing this Jira community adapter for wider use. An exciting prospect for a future live stream is to use this Jira adapter in conjunction with a mixed-provider Archon workflow (e.g., Gemini for UI design, Opus for content and planning) to manage a web development project directly through Jira tickets, further showcasing the power of integrated AI-driven development.