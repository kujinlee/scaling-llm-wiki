---
tags:
  - video-summary
  - en
  - agent client protocol
  - open claw
  - kubernetes
  - agent orchestration
  - ai workflows
  - pull request automation
  - enterprise agents
video_id: "VaS2h-dY1-4"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Advanced
score: 4.4
---

# Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw

**Channel:** AI Engineer | **Duration:** 19:00 | **URL:** https://www.youtube.com/watch?v=VaS2h-dY1-4

> [!summary] Quick Reference
> **TL;DR:** This video presents ACP, ACP-X, and Spritz to standardize, automate, and orchestrate scalable AI agents on Kubernetes for enterprise applications.
>
> **Key Takeaways:**
> - ACP standardizes human-agent interaction, overcoming "telephone game" issues and unifying disparate interfaces for AI models.
> - ACP-X automates PR review by using agents to refine "AI slop," presenting polished PRs to human maintainers.
> - Enterprise agents require on-demand provisioning, orchestrated via Kubernetes (e.g., Spritz), for scalable and task-specific deployment.
> - Spritz (an open-source Kubernetes orchestrator) deploys and manages AI agents, abstracting complexity while leveraging ACP for interoperability.
>
> **Concepts:** agent client protocol · open claw · kubernetes · agent orchestration · ai workflows · pull request automation · enterprise agents

---

## 1. The Genesis of Agent Client Protocol (ACP)
--- 
The speaker, a founding engineer, detailed their journey building AI coding harnesses and engaging with Open Claw. An early challenge involved the indirect communication between different AI models (e.g., Opus relaying instructions to Codex), which often led to a "telephone game" effect and unreliable outcomes for complex tasks. This experience underscored the critical need for a standardized method of interaction between humans (clients) and AI agents. ACP, or Agent Client Protocol, emerged as a solution to this problem, aiming to standardize agent-to-client interaction. This protocol addresses the wasted effort in developing disparate plugins for various IDEs and platforms (like VS Code or Cloud Code), by proposing a unified interface. The speaker chose ACP due to the availability of crucial adapters for Codex and Cloud Code at the time, highlighting its practical utility over competing standards focused on agent-to-agent communication.

## 2. ACP CLI: A Swiss Army Knife for Agent Interoperability
--- 
To further operationalize ACP, the speaker spearheaded the creation of a Command Line Interface (CLI) for the protocol. The initial goal was to enable agents to interact with each other via command-line instructions, abstracting away underlying complexities. This ACP CLI has since evolved into a versatile "Swiss Army knife" for various agent orchestration tasks, showcasing its growing utility. This development is crucial for accelerating the enterprise adoption of Open Claw and other adjacent AI software, by providing a robust and standardized mechanism for agent interaction and management within complex operational environments.

## 3. Automating Open Claw's PR Overload with ACP-X
--- 
Open Claw faces a significant challenge with an overwhelming volume of pull requests (PRs)—averaging 300 to 500 daily from tens of thousands of stakeholders. Many of these PRs are often AI-generated or simplistic "please fix" requests, termed "AI slop," which are difficult to merge directly but contain crucial user feedback. Inspired by an existing workflow, the speaker developed ACP-X, an A10-like workflow engine, to automate the mechanical aspects of PR review and management. ACP-X uses agents to identify intent, judge implementation quality, resolve conflicts, ensure CI passes, and address review comments. It incorporates "shameful refactor loops," allowing agents to autonomously fix shallow bugs and perform superficial refactors without engaging in complex design decisions. This system aims to create standard operating procedures for agents, ensuring that PRs presented to human maintainers are already polished and viable.

## 4. The Vision for Enterprise Agents and On-Demand Provisioning
--- 
The presentation distinguishes between personal and enterprise agents, positing that enterprise applications will drive significantly higher inference consumption and thus greater commercial opportunity. The speaker envisions a future with on-demand, disposable agents, tailored for specific tasks. A significant current hurdle for this vision is the lack of standardized multi-agent provisioning support in popular chat platforms like Slack, Teams, and Discord. Currently, each agent requires a separate application instance and manual configuration, preventing dynamic, cosmetic agent creation. Until platform support improves, custom UIs are necessary. The ideal infrastructure for this multi-agent paradigm requires Kubernetes for orchestration, a flexible agent harness (like Open Claw, Codex, or Cloud Code), read/write access for agents, and robust state/data synchronization mechanisms, akin to Dropbox or rsync, to ensure seamless operation across distributed agent environments.

## 5. Spritz: An Open-Source Kubernetes Orchestrator
--- 
As part of their day job at Text Cortex, the speaker introduced Spritz (`textecortex/spritz`), an open-source Kubernetes orchestrator designed to manage and deploy AI agents. Spritz acts as a "goal operator," abstracting away the complexities of running agents on Kubernetes. It enables enterprise use cases such as dispatching a concierge agent on Slack that can then provision new agents for specific tasks, like debugging a production issue. When a new agent is created, Spritz provides a link to a separate, dedicated UI (a React app hosted within the cluster) where the conversation and work unfold. Each agent operates within its own Kubernetes pod, a seemingly "wasteful" but ultimately more powerful abstraction, as it grants the agent a full computing environment. Spritz leverages ACP for agent interoperability, ensuring that users are not locked into any specific agent technology and can easily switch between different agent harnesses, making it a flexible and powerful solution for complex enterprise AI workflows.

## Conclusion
--- 
The presentation effectively bridges the gap between the theoretical promise of AI agents and their practical, scalable deployment in enterprise environments. By championing standardized protocols like ACP and developing innovative orchestration tools such as ACP-X and Spritz, the speaker demonstrates a clear path toward overcoming current limitations in agent interoperability and management. The emphasis on automating routine tasks, streamlining complex workflows like PR review, and building robust, Kubernetes-native agent infrastructures highlights a forward-thinking approach to leveraging AI. This vision ultimately leads to more efficient, powerful, and adaptable AI-driven operations, underscoring the transformative potential of well-architected agent ecosystems in the future of software development and beyond.