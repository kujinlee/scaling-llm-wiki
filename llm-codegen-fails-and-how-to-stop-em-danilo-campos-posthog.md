---
tags:
  - video-summary
  - en
  - ai agents
  - llm engineering
  - posthog wizard
  - model rot
  - agent security
  - prose over code
  - agent development
video_id: "juoNbJiZUi0"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Intermediate
score: 4.4
---

# LLM codegen fails and how to stop 'em — Danilo Campos, PostHog

**Channel:** AI Engineer | **Duration:** 19:18 | **URL:** https://www.youtube.com/watch?v=juoNbJiZUi0

> [!summary] Quick Reference
> **TL;DR:** This video outlines strategies for building effective autonomous coding agents, addressing challenges like model rot, inconsistent architecture, improvisation, and security.
>
> **Key Takeaways:**
> - Combat model rot by using Retrieval Augmented Generation (RAG) with fresh, current documentation for LLMs.
> - Guide agent architecture by providing "model airplanes," which are examples of best practices for desired patterns.
> - Limit agent improvisation through "breadcrumbing": sequential instructions that guide agent thought processes gradually.
> - Ensure agent safety and reliability with "inference time interrogation" and fine-grained control over tool access.
> - Prioritize clear prose and structured instructions over extensive code when developing AI agents.
>
> **Concepts:** ai agents · llm engineering · posthog wizard · model rot · agent security · prose over code · agent development

---

## 1. The Promise of Autonomous Agents and the Pitfalls
Danilo from PostHog introduces the PostHog Wizard, an autonomous coding agent designed to automate PostHog integration. This tool streamlines a typically 2-hour manual process into an 8-minute experience, with 15,000 monthly users reporting high satisfaction. While powerful, the creation of such an agent reveals significant challenges, as autonomous tools can "bloody your nose" through bad practices or unexpected behaviors. The presentation aims to outline these pitfalls and provide strategies for building effective and reliable AI agents.

---

## 2. Combating Model Rot with Fresh Context
One major challenge for autonomous coding agents is "model rot." Large language models (LLMs) are trained on historical data, often 6 to 18 months old. For fast-moving software projects, this means the model's knowledge quickly becomes outdated, leading to incorrect integrations, invented APIs, or non-existent patterns. The PostHog Wizard addresses this by using Retrieval Augmented Generation (RAG). It leverages fresh, up-to-date documentation from posthog.com, allowing the agent to select and integrate the most current information directly into its context. This ensures the agent works with relevant data, preventing many common integration errors caused by stale knowledge.

---

## 3. Guiding Agent Architecture with "Model Airplanes"
LLMs learn from vast quantities of scraped code, which inevitably includes projects with suboptimal architecture. This can lead agents to make technically functional but non-ideal design decisions when constructing new integrations. To counter this, the PostHog Wizard team maintains a fleet of "model airplanes." These are lightweight, stripped-down projects across various frameworks and languages that embody the "correct shape" and best practices for PostHog implementation. By providing these token-efficient "simulacrums" as examples, the agent learns preferred architectural patterns, ensuring consistent and well-structured integrations, such as correctly placing event tracking logic within authentication flows.

---

## 4. Limiting Agent Improvisation through Breadcrumbing
When an agent handles thousands of integrations, unconstrained improvisation can lead to a support nightmare with myriad unique, hard-to-maintain setups. To ensure consistency and predictability, the PostHog Wizard employs a "breadcrumbing" strategy, guiding the agent through a structured thought process rather than giving all instructions upfront. This involves:
1.  **Identifying Business Value:** Asking the agent to locate files with significant business impact (e.g., login, payment interfaces).
2.  **Event Definition:** Requesting a list of interesting events within those files, along with descriptions, *before* any code is written.
3.  **Gradual Implementation:** Only then, with a clear understanding of events and relevant documentation (dynamically loaded), does the agent proceed to modify files and implement PostHog.
This sequential approach limits erratic behavior and ensures thoughtful, consistent integration outcomes.

---

## 5. Addressing Human Error and Ensuring Agent Safety
Even with sophisticated agents, human error in defining instructions or tools can lead to significant problems (e.g., contradictory directives, missing tool definitions, wrong language contexts). To catch these issues, the PostHog team implements "inference time interrogation." At the end of every agent run, a simple question is posed to the robot: "What could we have done better to set you up for success?" This automated self-reflection helps identify misconfigurations and improves agent reliability.

Furthermore, deploying agents on user machines demands paramount trust and security. Early versions of the wizard, for instance, would read `.env` files, posing a security risk. The solution involved fine-grained control over tool usage, restricting the agent's access to sensitive files. Custom tools were developed that could only check for a key's presence or write a new value, preventing the transmission of full `.env` contents and safeguarding user data.

---

## 6. The Paradigm Shift: Prioritizing Prose Over Code
The speaker argues for a fundamental shift in how we approach building with AI agents: valuing well-crafted plain-text prose over complex, elaborate code. Traditional software development rewards clever, extensive coding, but code is a depreciating asset. In contrast, great prose — such as documentation and structured instructions — retains and even increases its value as models improve, allowing them to extract more meaning and perform better actions. The PostHog Wizard itself is described as "90% markdown files, 8% tools for delivering and processing markdown files, and the rest is Agent Harness." The key is to treat the agent as an "octopus" – an adaptive, flexible entity that should not be over-constrained with rigid code scaffolding. Instead, focus on providing it with sufficient, well-sequenced information through prose to achieve desired outcomes.

---

## Conclusion
Building successful autonomous coding agents like the PostHog Wizard requires a holistic approach that acknowledges and addresses several key challenges: outdated model knowledge, architectural inconsistencies, unpredictable agent improvisation, human error in configuration, and critical security concerns. By implementing strategies such as dynamic context retrieval (RAG), providing structured architectural examples ("model airplanes"), guiding agent behavior through "breadcrumbing," actively interrogating agent performance, and applying fine-grained security controls, developers can create reliable and trustworthy AI tools. Fundamentally, this new paradigm shifts focus from writing exhaustive code to crafting clear, precise prose, empowering agents to deliver valuable and consistent results efficiently.