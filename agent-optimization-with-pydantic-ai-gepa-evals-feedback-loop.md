---
tags:
  - video-summary
  - en
  - pydantic
  - jeppa
  - prompt optimization
  - llm agents
  - logfire
  - managed variables
  - observability
video_id: "A48uhxfxbsM"
channel: "AI Engineer"
lang: EN
type: Demo
audience: Intermediate
score: 4
---

# Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic

**Channel:** AI Engineer | **Duration:** 1:20:40 | **URL:** https://www.youtube.com/watch?v=A48uhxfxbsM

> [!summary] Quick Reference
> **TL;DR:** This video explains how Pydantic AI, Jeppa, and Logfire optimize LLM agents by dynamically updating prompts and configurations for continuous, self-driving improvements.
>
> **Key Takeaways:**
> - Jeppa uses a genetic Pareto algorithm to iteratively optimize LLM prompts, including complex JSON, for specific tasks.
> - Logfire Managed Variables enable dynamic updates of agent behaviors or models in production without code redeployments.
> - Pydantic AI agents can be fine-tuned using evaluation datasets and optimization techniques like Jeppa for improved accuracy.
> - Optimized prompts significantly enhance agent performance and reduce costs, especially for domain-specific data and cheaper models.
> - The future aims for autonomous agent optimization, where Logfire continuously refines configurations based on live feedback.
>
> **Concepts:** pydantic · jeppa · prompt optimization · llm agents · logfire · managed variables · observability

---

## 1. Introduction to Pydantic and Observability
The speaker, Samuel, introduces Pydantic, the open-source library, and the company Pydantic. The company maintains Pydantic validation, offers Pydantic AI (an agent framework), and Pydantic Logfire, an observability platform. Logfire goes beyond standard logs, metrics, and traces by incorporating features like evals and managed variables, with a future vision for autonomous agent optimization. This talk will specifically dive into Jeppa and Logfire's managed variables.

---

## 2. Jeppa: Genetic Pareto Optimization for LLM Prompts
Jeppa is an optimization library based on a genetic Pareto algorithm. It iteratively identifies optimal values by "breeding" the best candidates from a Pareto frontier, similar to selecting top racehorses for reproduction. Jeppa can optimize strings, ranging from simple text prompts to complex JSON data structures that define agent behavior. This approach aims to find the most effective prompts for specific tasks.

---

## 3. Logfire Managed Variables for Dynamic Configuration
Managed variables, a feature within Logfire, extend traditional prompt management. Unlike simple text prompts, these variables can encompass any Pydantic-defined object, allowing for rich and structured configuration. This enables developers to dynamically update agent behaviors, models, or instructions in production without requiring code redeployments. Logfire's managed variables leverage the OpenFeature standard for A/B testing and rollouts.

---

## 4. The MP Political Relations Extraction Challenge
The core demonstration task involves optimizing an agent designed to extract political relations (specifically ancestors) from Wikipedia articles about Members of Parliament (MPs). The initial Pydantic AI agent, despite being robust, struggled to consistently filter out non-ancestral relations (e.g., spouses, children). The goal is to fine-tune the agent's prompt to accurately identify only ancestral political ties, using a curated "golden relations" dataset as ground truth.

---

## 5. Practical Evaluation and Jeppa Optimization Flow
The talk details the process of evaluating agent performance using Logfire's evaluation capabilities. Initial runs with simple and "expert" prompts yield accuracy scores of approximately 85% and 92%, respectively, against the golden dataset. Jeppa then takes over, using a Pydantic AI agent as its "proposer" to iteratively generate and evaluate new prompts. Through this genetic optimization, the agent's accuracy for the MP relations task was significantly improved to 96.7%, demonstrating Jeppa's ability to discover highly effective, albeit sometimes verbose, prompts. Discussions also touched upon the practical considerations of such optimization, including variance, model specificity, and the suitability for private data domains.

---

## 6. Applying Optimized Prompts with Managed Variables
The final segment showcases how Logfire's managed variables facilitate the live application of optimized prompts or model changes. A Fast API web server hosting an MP search agent is used to demonstrate dynamic updates. By altering managed variables in Logfire, the agent's behavior (e.g., response language or underlying LLM model) can be switched instantly without restarting the server. The vision is to automate this process, allowing Logfire to continuously optimize managed variables based on evaluation feedback, leading to "self-driving" agent configurations in production.

---

## Conclusion
Prompt optimization, especially with tools like Jeppa and managed variables, offers significant value for specific use cases, particularly when working with cheaper or faster models, or when handling large volumes of private, domain-specific data. While challenges like model specificity, data variance, and the difficulty of optimizing for open-ended tasks persist, these techniques provide powerful ways to enhance agent performance and reduce operational costs without constant code redeployments. The future aims towards autonomous "self-driving" optimization of agent configurations directly in production.