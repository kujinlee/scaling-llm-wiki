---
tags:
  - video-summary
  - deep-dive
  - en
  - agent ai
  - enterprise ai
  - nvidia
  - open models
  - ai workflows
  - ai costs
  - ai toolkit
video_id: "b06GM7Ok1io"
channel: "안될공학 - IT 테크 신기술"
lang: EN
type: Analysis
audience: Intermediate
score: 4.2
---

# "에이전틱AI가 바꾸는 세계" 엔비디아 독점 인터뷰 | 부사장이 직접 밝힌 에이전틱 AI와 글로벌 인프라 시장의 미래 (Deep Dive)

**Channel:** 안될공학 - IT 테크 신기술 | **Duration:** 18:10 | **URL:** https://www.youtube.com/watch?v=b06GM7Ok1io

---

This document provides a detailed, structured analysis of the provided video, an interview with NVIDIA's VP of Enterprise Software, Adel El Hallak, about the company's vision and strategy for Agentic AI.

## The Core Value of Agentic AI: Unlocking New Markets
▶ [0:00–0:54](https://www.youtube.com/watch?v=b06GM7Ok1io&t=0s)

The interview begins by establishing the primary benefit of Agentic AI. According to Adel El Hallak, the "greatest benefit of of Agent AI" is not just incremental improvement but the "ability to unlock new markets." This foundational idea suggests that Agentic AI is a transformative technology capable of creating entirely new business opportunities and product categories that were previously not feasible.

## From Simple Chatbots to Useful Agentic AI
▶ [0:54–3:12](https://www.youtube.com/watch?v=b06GM7Ok1io&t=54s)

The interviewer frames the discussion by noting a key message from NVIDIA's keynote: Agentic AI is "not just a chatbot feature, but a new kind of workflow." This marks a significant evolution from the initial wave of generative AI.

### The Limitations of Traditional Chatbots
Adel El Hallak agrees with this assessment, explaining that early generative AI was primarily chatbot-based. While these chatbots could be "grounded" with Retrieval-Augmented Generation (RAG) to reduce hallucinations and answer questions against a specific knowledge base, their functionality was limited to a simple loop: "you write a prompt, it responds. You write another prompt, it responds." While this added value, it was not fundamentally transformative.

### The Shift to "Useful" AI
Agentic AI changes this paradigm. El Hallak states, "what Agent AI changed is now AI is useful, not just entertaining." This usefulness comes from the AI's ability to "actually achieve actions." Instead of just generating a response, an agent can perform a series of steps to accomplish a goal.

### The Core Components of an Agentic Workflow
This advanced capability is enabled by several key components, which were visualized in the keynote presentation.

```ascii
      ┌─────────────────┐
      │     Prompt      │
      └─────────────────┘
              ↓
      ┌─────────────────┐
      │  Orchestration  │
      └─────────────────┘
              ↓
      ┌─────────────────┐
      │  Agent (Loop)   │
      │ ┌─────────────┐ │
      │ │   Context   │ │
      │ │      ↓      │ │
      │ │   Observe   │ │
      │ │      ↓      │ │
      │ │   Reason    │ │
      │ │      ↓      │ │
      │ │     Act     │ │
      │ └─────────────┘ │
      └─────────────────┘
              ↓
      ┌─────────────────┐
      │     Memory      │
      └─────────────────┘
```

1.  **Reasoning and Planning:** "Because of reasoning, it can define a plan." The agent can understand its context and formulate a multi-step strategy.
2.  **Tool Use:** The agent "is able to utilize tools." This can range from RAG databases to a "coding terminal" or "code interpreter."
3.  **Harness and Orchestration:** The agent operates within a "harness" that represents all available tools and an "orchestration" layer that executes the plan.

With these components, an agent can be given a high-level goal, prescribed a set of tools, and then "work on your behalf for 4, 5, 6, 7 hours" to achieve a concrete outcome.

## Bridging the Gap: From POC to Production
▶ [3:12–5:26](https://www.youtube.com/watch?v=b06GM7Ok1io&t=192s)

The interviewer highlights a common challenge for enterprises: while it's easy to build an "AI agent demo," moving it into a "real workflow" presents practical issues around data connection, security, cost, and performance. The keynote acknowledged that Agentic AI workflows are becoming "much longer and more complex," creating a significant gap between a Proof-of-Concept (POC) and a production-ready system.

### Unbounded Autonomy vs. Enterprise Reality
Adel El Hallak introduces the concept of "unbounded autonomy," where an AI with no restrictions "can do a lot of things." However, in an enterprise context, this is dangerous. He draws an analogy: "if a new employee comes on a company, you don't just give them...your own laptop and tell them, 'Hey, go do whatever you want.'" Enterprises require "guardrails," defining what systems an agent can and cannot access.

### NVIDIA's Solution: The Agent Toolkit and Secure Runtime
To solve this, NVIDIA provides the **NVIDIA Agent Toolkit**, which consists of three main parts:
1.  **Models:** The **NeMo** family of models.
2.  **Harness:** The collection of tooling and orchestration.
3.  **Secure Runtime (OpenShell):** A critical component for production deployment. **OpenShell** "enforces and ensures what your agent can and cannot do," controlling where inference runs and what systems are accessed.

El Hallak states that this secure runtime is what will "help enterprises go from demonstrating a POC to deploying it in production."

```ascii
  ┌──────────────────────────────────────────────┐
  │     1. User Endpoint (IDE, terminal, etc.)     │
  └──────────────────────────────────────────────┘
                             ↓
  ┌──────────────────────────────────────────────┐
  │     2. Control Plane (Lifecycle, portal)     │
  └──────────────────────────────────────────────┘
                             ↓
  ┌──────────────────────────────────────────────┐
  │  3. Bootstrap Plane (BYO VDI provision engine) │
  └──────────────────────────────────────────────┘
                             ↓ (Trust Boundary)
  ┌──────────────────────────────────────────────┐
  │  4. Access Management (Enterprise SSO, broker) │
  └──────────────────────────────────────────────┘
                             ↓
  ┌──────────────────────────────────────────────┐
  │ 5. Agent Workspace (Tools, files, agents, GPU) │
  └──────────────────────────────────────────────┘
                             ↓ (Execution & Policy Plane)
  ┌──────────────────────────────────────────────┐
  │ 6. Safe Runtime (Sandbox, process scoping)   │
  └──────────────────────────────────────────────┘
                             ↓
  ┌──────────────────────────────────────────────┐
  │ 7. Enterprise Services (Source ctrl, docs)   │
  └──────────────────────────────────────────────┘
```
*A vertical representation of the "Secure Agent Workspace - seven logical planes" slide shown in the video.*

## The Role of Cost and Compute in Agentic AI
▶ [5:26–7:43](https://www.youtube.com/watch?v=b06GM7Ok1io&t=326s)

The interviewer notes that as agentic workflows become longer, enterprises must look beyond simple "token costs" and consider the "total cost of completing a task." He asks if metrics like "Cost per Completed Task" will become more important.

### Jevons Paradox and Token Consumption
Adel El Hallak acknowledges that "token economics...are going down." However, he points to **Jevons Paradox**, a concept where increased efficiency in resource use leads to an overall increase in resource consumption. As token costs decrease and efficiency rises, "the more consumption we're seeing." The focus, therefore, shifts from the cost of individual tokens to the overall value and productivity gains achieved.

### Distributed Compute: Beyond the Data Center
The execution of these workloads is also evolving. El Hallak emphasizes that "full stack computing, accelerated computing is starting to live outside the data center." NVIDIA sees a future where agentic workloads are deployed across a wide range of environments:
*   **Cloud Endpoints**
*   **On-premise Data Centers / AI Factories**
*   **Local Devices** (e.g., DGX Spark, RTX Laptops)

This proliferation of compute environments allows agents to be deployed wherever they are most effective.

## The Hybrid Model Approach: Systems of Models
▶ [7:43–9:34](https://www.youtube.com/watch?v=b06GM7Ok1io&t=463s)

The conversation explores the growing enterprise interest in using open models rather than relying solely on external APIs, primarily for better control over cost and security.

### Agents as "Systems of Models"
Adel El Hallak states that the future is not a binary choice between open models and proprietary APIs. Instead, he believes "most agents are systems of models." Even within NVIDIA, agents use a combination of models for different tasks:
*   **Orchestration/Planning:** A powerful cloud frontier model (e.g., from Anthropic or OpenAI) might be used as the "planner" to manage the overall task list.
*   **Specialized Tasks:** NVIDIA's open **NeMo** models, which are post-trained for specific tasks like research or domain-specific coding, are used for execution.

### The Value of Open Models
NVIDIA's commitment to open-sourcing NeMo goes beyond just providing model checkpoints on Hugging Face. El Hallak clarifies they are sharing:
*   Pre-training and post-training datasets
*   Algorithms and RL techniques
*   Associated research papers

This transparency allows enterprises to "trust something" because they can "see the inner workings." It also enables them to "post-train" and "customize" models for their specific, proprietary tasks.

## Agentic AI in Specialized Engineering Workflows
▶ [9:34–16:00](https://www.youtube.com/watch?v=b06GM7Ok1io&t=574s)

The interviewer raises the specific and highly specialized workflow of semiconductor design, referencing NVIDIA's collaboration with **Cadence**. He asks how Agentic AI can change such an expert-driven field, and whether agents will act as a "replacement for engineers" or more of an "engineering co-pilot."

### Not a Replacement, but an Enabler
El Hallak firmly rejects the idea of replacement, stating, "I don't think the...core mission of a software engineer is to be typing on a keyboard. Their soul, their mission is to solve problems, build things, think through architecture."

With Agentic AI, engineers at NVIDIA are not working less, but are "working more" because they are freed from mundane tasks to focus on higher-level challenges. An agent is not just a simple co-pilot that answers questions; it is a system that can take a high-level objective and run through "multiple iterations" on its own to achieve it.

The collaboration with Cadence demonstrated a **40x speedup** over traditional workflows, which El Hallak says allows for designing more chips and bringing more systems to the world. It "opens up opportunities to do things that you couldn't do in the past."

## A Practical Starting Point for Enterprise Adoption
▶ [16:00–18:04](https://www.youtube.com/watch?v=b06GM7Ok1io&t=960s)

The interviewer asks for the "most realistic starting point" for a company adopting Agentic AI for the first time, as starting too big can lead to failure, while staying at the demo level creates no real business value.

Adel El Hallak provides a clear, step-by-step recommendation:

1.  **Start with Software Development:** For any company doing software development, the easiest entry point is using AI coding tools like "Claude Code, Cursor, [or] Codex." The productivity gains are immediate and significant.
2.  **Identify a Critical Business Area:** Do not pick a trivial "nice-to-have" feature. Form a "tiger team" and "focus on a something that's critical" and important to the business, especially a function that involves repetitive tasks.
3.  **Go Deep and End-to-End:** Once a critical use case is identified, "go all the way through." This means:
    *   **Implement Observability:** Figure out how to monitor the system.
    *   **Set Policies:** Use the **OpenShell** runtime to establish policies for what the agent can and cannot do.
    *   **Collect Trace Data:** Gather data on the agent's execution to "make the system better."
4.  **Scale from Success:** After achieving a successful end-to-end implementation in one critical area, "use that to scale onto other other disciplines" and other parts of the company.