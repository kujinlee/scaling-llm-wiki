---
tags:
  - video-summary
  - en
  - andrej karpathy
  - ai prompting
  - claude ai
  - llm engineering
  - ai workflow
  - prompt engineering
  - ai productivity
video_id: "7zZy1QTvokM"
channel: "Austin Marchese"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# Stop Prompting Claude. Use Karpathy's Method Instead.

**Channel:** Austin Marchese | **Duration:** 13:19 | **URL:** https://www.youtube.com/watch?v=7zZy1QTvokM

> [!summary] Quick Reference
> **TL;DR:** This video breaks down Andrej Karpathy's three-layer method (Spec, Verifier, Environment) for building AI systems ten times faster.
>
> **Key Takeaways:**
> - Define clear goals for AI, as AI cannot infer your true objectives.
> - Adopt an agile approach, breaking AI tasks into small, verifiable steps.
> - Establish precise evaluation criteria before AI generates any output.
> - Build a persistent AI environment with custom skills and knowledge bases.
> - Implement tool-level guardrails for critical tasks, not just prompt-level requests.
>
> **Concepts:** andrej karpathy · ai prompting · claude ai · llm engineering · ai workflow · prompt engineering · ai productivity

---

## 1. Introduction to Karpathy's 10x Method
▶ [0:14–0:27](https://www.youtube.com/watch?v=7zZy1QTvokM&t=14s)
Andrej Karpathy's method for building 10 times faster with AI is structured around three simple layers: the Spec, the Verifier, and the Environment. This approach addresses common pitfalls, like prompting LLMs incorrectly, by providing a systematic way to interact with AI agents to achieve better and more reliable outcomes.

---

## 2. Layer One: The Spec – Bridging the Context Gap
▶ [0:27–3:31](https://www.youtube.com/watch?v=7zZy1QTvokM&t=27s)
AI models are incredibly intelligent computationally but often lack context-driven understanding. For example, an AI might advise walking 50 meters to a car wash because it's close, missing the crucial need for a car *for* the wash. The "spec" is the critical bridge, translating your contextual understanding into a detailed, usable format for AI. Karpathy advises going deeper than high-level "plan mode" to design an extremely detailed specification.

Creating an effective spec involves three key steps:
1.  **Uncover Your Goal:** Move beyond just giving a task (e.g., "Create an end-of-month report") to identifying the underlying conclusion or decision the task aims to support. AI cannot determine this goal on its own. Prompt Claude to interview you to extract this core objective.
2.  **Be Agile:** Avoid the "waterfall" approach of handing AI a large task all at once. Instead, adopt an "agile specking" method: break tasks into small, compartmentalized units, review outputs frequently, and adjust iteratively. Instruct Claude to bias towards smaller, more focused specs.
3.  **Be Precise and Use Your Brain:** The more precise your instructions, the fewer assumptions AI has to make. Every AI assumption is an opportunity for it to drift from your desired outcome. When AI generates a spec, critically review it yourself and explicitly verify key decisions.

---

## 3. Layer Two: The Verifier – Ensuring Quality AI Output
▶ [3:31–8:48](https://www.youtube.com/watch?v=7zZy1QTvokM&t=211s)
The Verifier layer is dedicated to ensuring the quality and correctness of AI outputs. Karpathy describes AI not as an "animal" (with human-like motivations or understanding of non-measurable things) but as a "ghost" or, more simply, a "robot librarian." AI excels where answers are clear (like math) but can confidently make things up when it lacks specific "books" or context. Therefore, robust verification is essential, as yelling or pleading with it like a human is ineffective.

Three key strategies for effective verification:
1.  **Set Evaluation Criteria Up Front:** Before AI begins any task, define precisely what "good" looks like. Instead of a vague instruction like, "Make this report look good," provide specific criteria such as, "The report must have three sections, each ending with a recommendation." This upfront precision significantly limits AI's potential for error.
2.  **Use a Second AI Model as a Critic:** Employ a different AI model (e.g., using a Codex plugin within Claude code) to review and grade the output of the first. This leverages a diverse "library" of knowledge, potentially providing new insights or validating results from a different perspective.
3.  **Pull External Signal Where Possible:** Integrate external data sources to enhance verification. For example, connect your Claude session to a deployment system to confirm an app's successful deployment, or provide historical reports as a format reference for new reports. This creates concrete, verifiable data points, boosting certainty in AI's actions.

---

## 4. Layer Three: The Environment – Building a Replicable Foundation
▶ [8:48–12:40](https://www.youtube.com/watch?v=7zZy1QTvokM&t=528s)
The Environment is the persistent, evolving workspace where the Spec and Verifier layers live and improve over time. It's about establishing the proper tooling and system to function at a high level, moving beyond starting from scratch with every AI interaction. This layer ensures your AI setup compounds its effectiveness over time.

Key components for building a robust AI environment:
1.  **Set Up a Proper Claude MD File:** This file is automatically injected into every Claude prompt, acting as initial instructions on how Claude should operate. Use it to enforce system-wide behaviors, such as requiring a verification plan for all multi-step builds, so you don't have to remember to prompt it every time.
2.  **Build Your LLM Knowledge Base:** Create a structured folder system on your machine that allows you to ingest your own training data. This makes it easy for Claude to access and understand your domain-specific information, forming your intellectual data property and a unique "moat."
3.  **Build Out Your Skill Set:** For any task you plan to do repeatedly, create a custom AI skill (like a handbook). The more these skills are used and iterated upon, the better they become. Continuous usage helps identify and fix leaks, leading to a compounding system.
4.  **Create Rules for AI Actions (Guardrails):** Establish clear boundaries for what AI "always does," "asks first," or "never does." For critical functions, implement tool-level guardrails (e.g., pre-tool use hooks) that physically prevent AI from making undesired edits, rather than relying on prompt-level requests that AI can potentially bypass.

---

## Conclusion
▶ [12:40–13:19](https://www.youtube.com/watch?v=7zZy1QTvokM&t=760s)
Despite the advanced capabilities of AI, Karpathy emphasizes that the one thing we should profoundly focus on in the age of AI is *understanding*. While AI can outsource much of our thinking, it cannot outsource our understanding of the bigger picture, our true goals, and the necessary direction to effectively guide and utilize AI. The three layers—Spec, Verifier, and Environment—are all fundamentally centered around leveraging *your* understanding to drive AI's computational power and achieve superior results.