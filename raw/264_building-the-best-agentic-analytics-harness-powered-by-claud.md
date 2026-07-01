---
tags:
  - video-summary
  - en
  - claude
  - llm development
  - ai analytics
  - semantic layer
  - agentic ai
  - sql generation
  - error recovery
video_id: "K4-flzsPraE"
channel: "Claude"
lang: EN
type: Case Study
audience: Advanced
score: 4.4
---

# Building the best agentic analytics harness: Powered by Claude, built with Claude Code

**Channel:** Claude | **Duration:** 26:46 | **URL:** https://www.youtube.com/watch?v=K4-flzsPraE

> [!summary] Quick Reference
> **TL;DR:** This video details how Omni built its AI analytics platform, Blobby, using Claude, focusing on the evolution of its agentic architecture and semantic layer.
>
> **Key Takeaways:**
> - Invest in developer tools that mirror user experience to improve product design.
> - Localize context next to data definitions for better LLM performance.
> - Implement robust agentic loops with error recovery for system reliability.
> - Consolidate agent "brains" to avoid split-knowledge issues in complex systems.
> - Leverage LLMs' inherent SQL capabilities for efficient query generation.
>
> **Concepts:** claude · llm development · ai analytics · semantic layer · agentic ai · sql generation · error recovery

---

## 1. Claude's Impact on Omni's Engineering
▶ [2:06–5:20](https://www.youtube.com/watch?v=K4-flzsPraE&t=126s)
Omni, an AI analytics platform, significantly boosted its engineering velocity and development culture by adopting Claude. The CTO highlights a notable increase in commits to the main branch after Claude Code with the OS model was released. This allowed even the CTO to continue contributing code, an unexpected benefit. The company encouraged early experimentation with AI tools, finding that Claude consistently provided real help, leading to a rapid skill-up across the engineering team by January. This velocity aligns with Omni's core values of "ship it" and transparency, as demonstrated by their public demo releases of new features every Friday.

---

## 2. Omni AI Analytics and the Semantic Layer
▶ [5:20–11:56](https://www.youtube.com/watch?v=K4-flzsPraE&t=320s)
Omni's platform enables users to interact with their data using natural language, translating questions into semantic queries via Claude. A crucial component is the semantic layer, which acts as a translation layer sitting atop data warehouses or databases. This layer curates data, provides a map for translating queries into SQL, and resolves business terminology ambiguities (e.g., "last quarter" meaning different things in different departments). It addresses the challenge of navigating vast, complex enterprise data sets, allowing definition of how data elements should be used together and ignoring irrelevant ones.

---

## 3. The Evolution of Blobby: From Single-Shot to Agentic AI
▶ [11:56–42:32](https://www.youtube.com/watch?v=K4-flzsPraE&t=716s)
Omni's AI agent, Blobby, has evolved significantly over 18 months. Initially a single-question, single-answer system, early improvements focused on providing extensive metadata. This included adding "AI context" to guide LLMs on field usage, "sample queries" for typical use cases, and providing a "taste of values" (e.g., region abbreviations) to help the LLM infer and correctly interpret user input. The next major leap was adding an agentic loop, building a custom harness to enable Blobby to recover from errors by leveraging descriptive error messages. This dramatically increased quality scores. The transition from Claude Haiku to Sonnet further unlocked more complex, elaborate agentic conversations, leading to a surge in Blobby's usage as it could tackle questions previously unanswerable or time-consuming.

---

## 4. Consolidating the Brain and SQL Generation
▶ [42:32–43:55](https://www.youtube.com/watch?v=K4-flzsPraE&t=2552s)
Addressing critical user feedback, Omni invested in understanding agent trace data from "bad sessions." This revealed a "split brain" problem where an outer agent (responsible for task lists) and a sub-agent (responsible for query generation) had misaligned knowledge. The sub-agent could only generate single queries, but the outer agent might request complex tasks requiring multiple queries, leading to failures. The solution was "consolidating the brain" by pulling tools and knowledge into the outer agent, eliminating unpredictable behavior. Further, Omni revived an old, discarded SQL parsing engine. By allowing Claude to generate raw SQL (which it excels at, especially with CTEs) rather than a proprietary JSON form, and providing parsing guidelines, Blobby became capable of answering complex questions in single, efficient queries, significantly improving system efficiency and simplifying the LLM's task.

---

## 5. Current Platform Capabilities and Evaluation
Today, Omni's agentic system features an outer loop for checkpointing and failure recovery, and an inner loop with a growing set of tools for generating dashboards, visualizations, and even performing data modeling to improve the semantic layer. The platform relies heavily on both internal and customer evaluation (Eval) systems to ensure predictability and consistent quality of answers. The CTO emphasizes that Evals are invaluable for the raw trace data they provide, offering deep observability into agent behavior to debug and improve. Additionally, using Claude Code internally has helped Omni engineers understand what a good AI harness looks like, enabling them to apply those lessons to Blobby's development, bridging the gap between a semantic model and a code base.

---

## Conclusion
Omni's AI analytics platform, powered by Claude, demonstrates a sophisticated approach to building intelligent data interaction systems. Through iterative development, a focus on robust agentic design, intelligent context management via a semantic layer, and continuous evaluation, Omni has created a powerful tool for users to "talk to their data." The journey highlights key architectural and learning principles for developing reliable, high-quality LLM-powered applications.