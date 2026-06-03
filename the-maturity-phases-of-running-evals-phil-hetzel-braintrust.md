---
tags:
  - video-summary
  - en
  - agent evaluations
  - llm as judge
  - ai agents
  - generative ai
  - observability
  - evaluation platforms
  - testing
video_id: "FB-MLPhL9Ms"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Intermediate
score: 4.4
---

# The maturity phases of running evals — Phil Hetzel, Braintrust

**Channel:** AI Engineer | **Duration:** 18:34 | **URL:** https://www.youtube.com/watch?v=FB-MLPhL9Ms

> [!summary] Quick Reference
> **TL;DR:** This video outlines the evolving maturity phases of AI agent evaluations, from human checks to automated systems, to build confidence and ensure continuous improvement.
>
> **Key Takeaways:**
> - Start with human 'vibe checks' but document detailed justifications to capture domain knowledge.
> - Scale human insights by analyzing justifications to identify and automate failure modes using LLM-as-judge.
> - Evaluate entire agent traces, not just outputs, especially for agents interacting with external systems.
> - Evals are crucial for confidence, risk mitigation, and guiding continuous improvement of AI agents.
> - Automate evaluations with cloud code and CLI for continuous integration and robust quality checks.
>
> **Concepts:** agent evaluations · llm as judge · ai agents · generative ai · observability · evaluation platforms · testing

---

## 1. The Critical Role of Agent Evaluations
Evals are paramount for establishing and maintaining confidence in AI agents, from initial development to production. BrainTrust, an agent quality company, emphasizes evals and observability as intertwined problems. Their purpose extends beyond mere testing, serving as a defense against reputational, systemic, compliance, and legal risks, while also playing offense by guiding agent improvements.

Evals differ from unit tests; they focus on high-level failure modes rather than exhaustive scenarios, acknowledging that comprehensive testing is an infinite endeavor. Results don't need to be perfect; directional trends are often sufficient, especially with non-deterministic LLM-as-judge techniques. Every eval comprises three primitives: the task (agent/prompt under test), a dataset of example inputs, and scoring functions to gauge quality.

---

## 2. Starting with Human Annotation: "Vibe Checks" and Justification
The initial stage of agent evaluation, often termed "vibe checking," is a valid starting point, but critically, it must include rigorous documentation. When an agent is tested with sample inputs, human annotators—ideally subject matter experts—should provide not just a binary good/bad judgment, but also detailed justifications for their assessment. This process is essential for extracting domain-specific knowledge from human experts, which can later be scaled and automated using techniques like LLM-as-judge.

The recommended workflow involves capturing an agent trace, applying a human judgment (thumbs up/down), and adding a justification. Platforms should offer highly specific, tailored annotation views to encourage accurate and consistent human evaluation, rather than generic interfaces.

---

## 3. Scaling Evaluations: From Human Insight to Automated Scoring
Building on human annotation, the next maturity level involves "Measuring to Manage" by scaling that human knowledge. This means analyzing the justifications provided by human annotators to identify and categorize specific failure modes, often using LLMs (e.g., Cursor Cloud Code, Codex). Once failure modes are understood, they can be automated.

A key technique is using LLMs to judge other LLMs (LLM-as-judge). However, caution is advised: LLM-as-judge outputs should also be evaluated to ensure alignment with human judgment. Additionally, objective failure modes can be deterministically identified via code (e.g., excessive tool calls or token usage). Crucially, eval datasets should incorporate production or UAT-level traces to simulate real-world scenarios, fostering a "flywheel" effect where production issues inform offline experimentation and agent improvement.

---

## 4. Tackling Complexity: External Systems and Trace Analysis
As agents become more complex and interact with external systems (e.g., for context gathering or CRUD operations), the number of potential failure vectors increases significantly. This necessitates the evaluation of entire agent traces, not just final outputs, requiring specialized tooling to capture and introspect each step of an agent's interaction, including individual tool or external service calls.

Significant challenges arise when dealing with external system state during offline evaluations: accurately representing the system's state at the time of the original input and avoiding modifications to live production data. Emerging solutions include encapsulating system state directly within arbitrarily large traces and using timestamp-based queries on versioned databases (like vector databases) to reconstruct historical states. Mock APIs can also be used to simulate external system interactions without impacting production.

---

## 5. Advanced Evaluation Techniques and Future Directions
Looking ahead, the field of agent evaluations is evolving towards even more sophisticated techniques. One significant area is the automatic discovery of failure modes in production at scale, often leveraging methods like topic modeling. This allows for proactive identification of issues without constant manual review.

Another advanced pattern is the complete automation of evaluations through cloud code and command-line interfaces provided by evaluation platforms. This enables continuous integration and deployment of agent improvements with robust, automated quality checks, ensuring that changes reliably enhance agent performance and prevent regressions.

---

## Conclusion
The journey of agent evaluation is a continuous evolution from rudimentary "vibe checks" to highly sophisticated, automated systems. It necessitates scaling human expertise through LLM-as-judge techniques, addressing the inherent complexities of external system interactions, and embracing emerging patterns like automated failure mode discovery and cloud-native evaluation automation. The ultimate goal is to cultivate unwavering confidence in agent performance, effectively mitigate risks, and establish a robust framework for continuous improvement, transforming evaluations into a proactive strategy for refining AI applications.