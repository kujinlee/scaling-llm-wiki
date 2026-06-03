---
tags:
  - video-summary
  - en
  - ai agents
  - anthropic
  - claude
  - llm architecture
  - agentic workflows
  - generator-evaluator
  - long-running tasks
video_id: "mR-WAvEPRwE"
channel: "AI Engineer"
lang: EN
type: Analysis
audience: Advanced
score: 4.8
---

# Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson

**Channel:** AI Engineer | **Duration:** 1:15:40 | **URL:** https://www.youtube.com/watch?v=mR-WAvEPRwE

> [!summary] Quick Reference
> **TL;DR:** This video covers building robust, long-running AI agents by using an adversarial generator-evaluator harness pattern and careful context management.
>
> **Key Takeaways:**
> - Employ an adversarial evaluator for objective critique; avoid self-evaluation.
> - Prioritize clean contexts and structured hand-offs for long-running agents.
> - Define detailed rubrics to grade subjective quality effectively and consistently.
> - Analyze agent traces extensively to understand model behavior and improve harnesses.
> - Leverage primitives like sub-agents, harsh system prompts, and Playwright for robust systems.
>
> **Concepts:** ai agents · anthropic · claude · llm architecture · agentic workflows · generator-evaluator · long-running tasks

---

## 1. The Core Challenges of Long-Running AI Agents
Building agents that can run for extended periods (5-6 hours or even days) presents significant difficulties. Three primary buckets of problems include:
*   **Context Management**: Finite context windows lead to "amnesia" and "context rot" over time. Models can also suffer from "context anxiety," rushing to finish as the window nears its end.
*   **Planning Limitations**: Out-of-the-box LLMs are often poor at long-term planning, attempting to do everything in one shot or leaving tasks unfinished.
*   **Self-Evaluation Weaknesses**: Models struggle to objectively judge their own output, often exhibiting "sycophantic" tendencies and prematurely declaring tasks complete even when features are incomplete or broken.

---

## 2. Evolution of Anthropic's Agent SDK and Claude Models
Anthropic has continuously evolved its Claude models and the Agent SDK to address these challenges. Key milestones include:
*   **Early Innovations**: Pre-Claude Code, Sonnet 3.5 showed promise with coding verification and the introduction of "computer use" (clicking, screenshots) and "MCP spec" for tool use.
*   **Claude Code Research Preview (Sonnet 3.7)**: Focused on understanding developer interaction to inform model improvements, enabling agents to run for approximately 1 hour.
*   **Claude Code GA (Opus 4.0, Sonnet 4.0)**: Models improved context management, leading to the release of the Claude Code SDK (later renamed Agent SDK).
*   **Advanced Features**: Checkpoints for session rewinding, multi-agent capabilities (Haiku 4.5, Opus 4.5 for planning, Sonnet 4.5 for execution), "skills" for progressive context disclosure, and programmatic tool calling significantly enhanced agent efficiency and runtime.
*   **Opus 4.6 and Sonnet 4.6**: Marked a significant leap, with Opus 4.6 becoming highly "agentic" for planning and enabling runtimes of up to 12 hours with minimal scaffolding.

---

## 3. Co-evolution of Models and Harnesses: The Ralph Wiggum Technique
Model improvements and harness (scaffolding around the model) changes are co-evolving. Early harness strategies included:
*   **The Ralph Loop**: A technique that gained traction, involving feeding a prompt to Claude Code CLI in a loop. It initially relied on breaking down tasks into features, picking one, and starting a new session with a fresh context window. Anthropic's internal Ralph Loop, however, ran within a single session, relying on compaction.
*   **Long-Running Agent Harness (November blog post)**: An early iteration involved an initializer agent breaking a vague prompt into features, progress files, and an init script. A harness loop then sequentially picked unfinished features, implemented them, performed tests (e.g., with Puppeteer), and committed changes in fresh context windows, using persistent artifacts for state management.

---

## 4. The GAN-Inspired Generator-Evaluator Harness Pattern
A more experimental and powerful harness pattern draws inspiration from Generative Adversarial Networks (GANs), splitting roles between a "generator" model that builds and an "evaluator" model that critiques.
*   **Separate Contexts and Roles**: The generator and evaluator operate with distinct context windows and system prompts, preventing the generator from rubber-stamping its own work.
*   **Standalone Critic**: The key insight is that tuning a standalone critic to be harsh is tractable, whereas tuning a builder for self-criticism is not.
*   **Live Testing**: The evaluator doesn't just read diffs; it uses tools like Playwright to open live pages, click around, and test the application, providing concrete critique back to the generator.
*   **Adaptive Iteration**: This adversarial pressure allows the agent to pivot and restart from scratch if it consistently struggles with certain criteria, unlike single-pass or RALF loops that try to patch the same thing.

---

## 5. Designing Effective Critics and Collaborative Agent Workflows
To make the generator-evaluator pattern effective, careful design of critics and multi-agent collaboration is crucial:
*   **Rubric-Based Evaluation**: Critics are designed using detailed rubrics (e.g., for design, originality, craft, functionality) and calibrated with few-shot examples from reference sites to converge on desired "taste."
*   **Planner Agent**: A "planner" agent takes a high-level prompt and breaks it into a series of sprints, focusing on general workflow rather than granular technical details, to avoid cascading errors.
*   **Contract Negotiation**: Before building, the generator and evaluator negotiate a "contract" by proposing features and verification tests. The evaluator pushes back on scope or weak tests until both agree on specific, testable assertions. The evaluator then grades against this contract, not just the original high-level spec.
*   **Debugging by Traces**: Tuning the QA agent (evaluator) requires extensive reading of agent traces to identify where judgment diverges from human expectations and then adjusting prompts accordingly.

---

## 6. Demonstrated Impact and Harness Adaptability
The GAN-inspired harness has shown significant improvements in building complex applications:
*   **Retro Game Maker Example**: A solo agent produced a visually appealing but non-functional game, failing at actual play mode. The harness-driven agent (Retro Forge) produced a more complete product with a 54-color palette, an AI-level assistant, and a fully functional play mode with live physics and collision detection, demonstrating the power of external verification.
*   **Catching Subtle Bugs**: The evaluator caught subtle issues like FastAPI route ordering bugs and Boolean logic errors, which a solo agent might miss, by actively using the app.
*   **Adapting to Model Evolution**: As models improve (e.g., Opus 4.6's improved context handling), harnesses can be simplified. For instance, context resetting between sessions was dropped, and the evaluator cadence was adjusted, proving that harnesses must continually adapt to fill new gaps or leverage new model strengths.

---

## Conclusion
Key takeaways for building robust and long-running AI agents:
*   **Avoid Self-Evaluation**: Instead, employ an adversarial evaluator for objective critique.
*   **Prioritize Clean Contexts**: Compaction alone does not equal coherence; structured hand-offs and clean contexts are crucial for long-running agents.
*   **Grade Subjective Quality**: Define and write down strong opinions on subjective qualities (e.g., design taste) into detailed rubrics for effective evaluation.
*   **Read the Traces**: Spend time analyzing agent transcripts to truly understand model behavior and identify areas for harness improvement.
*   **Leverage Existing Primitives**: Utilize tools like custom sub-agents, harsh system prompts, detailed rubrics, Playwright/Claude for Chrome MTP, and skills to build sophisticated agent systems.