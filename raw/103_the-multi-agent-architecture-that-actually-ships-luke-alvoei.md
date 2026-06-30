---
tags:
  - video-summary
  - en
  - multi-agent systems
  - llm agents
  - software development
  - agent orchestration
  - validation
  - factory
  - missions framework
video_id: "ow1we5PzK-o"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Advanced
score: 4.6
---

# The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory

**Channel:** AI Engineer | **Duration:** 18:31 | **URL:** https://www.youtube.com/watch?v=ow1we5PzK-o

> [!summary] Quick Reference
> **TL;DR:** This video introduces Missions, a multi-agent framework for autonomous software development, using structured validation and diverse LLMs to overcome human attention bottlenecks.
>
> **Key Takeaways:**
> - Combine delegation, creator-verifier, broadcast, and negotiation for robust agent systems.
> - Use a three-role architecture: Orchestrator plans, Workers implement, and Validators verify rigorously.
> - Define "validation contracts" before coding to ensure unbiased, adversarial verification of work.
> - Execute features serially to dramatically reduce error rates in long-running autonomous agent tasks.
> - Select specific LLM models for each role (planning, implementation, validation) based on their strengths.
>
> **Concepts:** multi-agent systems · llm agents · software development · agent orchestration · validation · factory · missions framework

---

## 1. The Bottleneck in Software Engineering and Multi-Agent Solutions
The primary bottleneck in modern software engineering is not intelligence but human attention. Even skilled engineers can only manage a few tasks simultaneously, leading to backlogs. Today's large language models (LLMs) are capable of understanding and potentially tackling many tasks, but human supervision limits their implementation. The speaker proposes a system where humans define "what" to build, and agents autonomously figure out "how," working for extended periods without constant oversight.

---

## 2. A Taxonomy of Multi-Agent Frameworks
The field of multi-agent systems is complex, with varying terminology. The speaker proposes five frontier frameworks:
*   **Delegation**: A parent agent spawns sub-agents for specific sub-tasks (e.g., "figure out database schema"). This is the simplest and most common form.
*   **Creator-Verifier**: One agent builds something, and a separate, unbiased agent checks the work. This mirrors human code review and leverages a separation of concerns to find issues effectively.
*   **Direct Communication**: Agents communicate directly without a central coordinator, similar to direct messaging. This is challenging due to state fragmentation.
*   **Negotiation**: Agents communicate over shared resources (e.g., APIs, code sections). Best used for net-positive sum trading where win-win situations can arise.
*   **Broadcast**: One agent sends information (status updates, shared constraints) to many. Crucial for maintaining coherence in long-running tasks.

---

## 3. Introducing Missions: A Multi-Role Agent Architecture
Missions is a system that combines delegation, creator-verifier, broadcast, and negotiation into a unified workflow designed for long-running software development tasks. It uses a three-role architecture:
*   **Orchestrator**: Handles planning, scopes goals through conversation, and produces a plan including features, milestones, and a critical "validation contract." This contract defines "done" *before* any coding begins.
*   **Workers**: Handle implementation. Each worker receives clean context for a specific feature, implements it, and commits changes via Git, ensuring a clean slate for the next worker.
*   **Validators**: Handle verification. Beyond traditional checks (lint, type, tests), validators also verify *behavior* end-to-end, preventing system drift over time.

---

## 4. Rethinking Validation for Long-Running Agent Systems
Traditional validation where tests are written *after* implementation often confirms decisions rather than catching bugs, leading to system drift. Missions addresses this with a "validation contract" written during the planning phase, *before* any code. This contract defines correctness independently of implementation and consists of numerous assertions. At each milestone, two types of validators run:
*   **Scrutiny Validator**: Performs traditional checks (test suite, type checking, linting) and spawns dedicated code review agents.
*   **User Testing Validator**: Acts like a QA engineer, spawning the application and interacting with it (e.g., filling forms, clicking buttons) to ensure holistic functional flows.
Crucially, neither validator has seen the code before, making validation adversarial by design and ensuring unbiased verification. Errors caught at milestones lead to corrective work, allowing the system to self-heal.

---

## 5. Operationalizing Missions: Execution, Monitoring, and Model Selection
Missions prioritize correctness over raw speed by executing features serially, running only one worker or validator at a time. Within features or validators, read-only operations (like searching code or API research) can be parallelized. This serial execution dramatically reduces the error rate, which is critical for tasks running for days. For monitoring, "Mission Control" provides a dedicated UI to track progress, budget burn, active worker status, and handoff summaries, enabling asynchronous oversight.

A key aspect is "droid whispering" – the deliberate choice of the right LLM for each role:
*   **Planning**: Benefits from models good at slow, careful reasoning.
*   **Implementation**: Requires models with fast code fluency and creativity.
*   **Validation**: Needs models excellent at precise instruction following.
The model-agnostic architecture allows using different providers or models for different roles, leveraging their strengths and compensating for weaknesses. It even enables successful runs with open-weight models by relying on the system's structure (validation contracts, checkpoints).

---

## 6. Real-World Impact and Future Directions
In production, Missions has been used for prototyping new ideas, building internal tools, large refactors, ML research, and codebase modernization. An example showed 60% of time/tokens spent on implementation, with validation almost always requiring follow-up features, highlighting the value of the QA loop. The system ensures that the architecture improves with every new model, as orchestration logic is defined in prompts and skills rather than hard-coded state machines. This approach shifts the bottleneck from human attention to higher-level architectural and product decisions, allowing engineers to focus on more complex problems. The result is often a cleaner codebase with extensive tests and structure, boosting future productivity for both agents and humans. Future work includes further parallelization and orchestrating missions into even more complex workflows.

---

## Conclusion
Missions provides a robust, multi-agent framework for autonomous software development that addresses the human attention bottleneck. By combining various agent interaction strategies with a novel validation approach, role-specific model selection, and a structured, serial execution model, it enables long-running, self-healing development tasks. This system empowers engineering teams to achieve orders of magnitude harder tasks, driving innovation and improving codebase quality.