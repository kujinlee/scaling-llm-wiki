---
tags:
  - video-summary
  - en
  - agentic search
  - context engineering
  - rag
  - tools
  - elasticsearch
  - shell commands
  - agent skills
video_id: "ynJyIKwjonM"
channel: "AI Engineer"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# Agentic Search for Context Engineering — Leonie Monigatti, Elastic

**Channel:** AI Engineer | **Duration:** 1:03:13 | **URL:** https://www.youtube.com/watch?v=ynJyIKwjonM

> [!summary] Quick Reference
> **TL;DR:** This video details agentic search for context engineering, covering its evolution, robust tool design, common failure modes, and effective tool stack curation strategies.
>
> **Key Takeaways:**
> - Agentic RAG lets agents decide when and how often to use search tools, improving context retrieval significantly.
> - The Shell Tool offers extreme versatility, allowing agents to execute terminal commands and interact with various systems.
> - Craft highly descriptive tool descriptions, reinforce instructions in system prompts, and implement robust error handling.
> - Provide detailed documentation as an 'Agent Skill' to help agents generate complex queries correctly, like ESQL.
> - Combine specialized tools (low floor) with general-purpose tools (high ceiling) for a robust search stack.
>
> **Concepts:** agentic search · context engineering · rag · tools · elasticsearch · shell commands · agent skills

---

## 1. The Core of Context Engineering: Agentic Search
This section introduces context engineering as the process of curating the most relevant information for an LLM's context window. The speaker asserts that agentic search, powered by various search tools, constitutes approximately 80% of context engineering. It highlights how search tools are crucial for deciding what context moves from diverse sources into the LLM's operational window.

---

## 2. Evolution from RAG to Agentic RAG and Diverse Context Sources
The presentation traces the evolution from traditional Retrieval Augmented Generation (RAG), which uses a fixed retrieval pipeline, to agentic RAG. Original RAG suffered from limitations like retrieving unnecessary context or only performing single-hop retrieval. Agentic RAG overcomes these by empowering the agent to decide *when* and *how often* to use a search tool. The discussion then expands to the multitude of context sources—local files, databases, web, memory, and agent skills—and their corresponding native search tools. A significant highlight is the **Shell Tool** (bash/exec), which offers extreme versatility by allowing agents to execute terminal commands, interacting with various systems via CLIs or scripts. The key takeaway here is the complexity of good search, necessitating a curated stack of diverse search techniques.

---

## 3. Fundamentals for Building Robust Search Tools: Addressing Failure Modes
Building effective agentic search involves anticipating and mitigating common failure modes. The speaker identifies three main issues: the agent not calling *any* tool, calling the *wrong* tool, or generating *incorrect* search parameters. Solutions emphasize crafting highly descriptive tool descriptions that detail purpose, trigger conditions, and relationships between tools. Reinforcing these instructions in the agent's system prompt is also crucial. The complexity of tool parameters is noted as a source of error; simple parameters are easy, but complex query languages (like ESQL) require more agent intelligence. Implementing robust error handling (e.g., `try-except` blocks) to allow the agent to self-correct is essential.

---

## 4. Practical Demonstrations: From Semantic Search to Custom CLIs
The core concepts are illustrated through code demonstrations using LangChain and conference session data.
- **Vanilla Semantic Search:** A basic semantic search tool is shown to be brittle when dealing with specific keywords (e.g., "GDPA") that lack strong semantic proximity to embedded data.
- **General Purpose Query Tool with Agent Skills:** To overcome limitations, the semantic search is replaced by a tool allowing the agent to write full ESQL queries. An initial failure (wrong wildcard symbol) leads to the introduction of an **Agent Skill Loading Tool**. This skill provides detailed ESQL syntax documentation, which, when explicitly instructed in the tool description and system prompt, enables the agent to generate correct, complex queries, including aggregations.
- **Shell Tool for File System Search:** The versatility of the shell tool is demonstrated for searching local files using `ls` and `grep`. Interestingly, the agent effectively "cheats" at semantic search by chaining multiple synonyms with `grep` commands. The ultimate solution for robust semantic search over files is shown using a custom CLI, **Gina Grap**, which leverages multi-vector embeddings for efficient and accurate results.

---

## 5. Practical Recommendations for Tool Stack Curation
The presentation concludes with practical advice: there's no single "silver bullet" search tool. Instead, a balanced tool stack is recommended, combining **specialized tools** (low floor – easy for the agent to use, efficient for common tasks, minimal errors) with **general purpose tools** (high ceiling – capable of handling unexpected or complex queries, though potentially requiring more iterations). For scenarios where the agent's query behavior is unknown, the recommendation is to start with general-purpose tools, meticulously log agent behavior, and then develop more specialized tools or interfaces as specific patterns or frequent failures emerge.

---

## Conclusion
Agentic search is a foundational component of effective context engineering, enabling LLMs to access and utilize external knowledge intelligently. By understanding the evolution of RAG, the diversity of context sources, common failure modes in tool usage, and strategic tool stack curation—balancing specialized and general-purpose tools—developers can build more robust, efficient, and versatile AI agents. The key lies in thoughtful tool design, clear instructions, and continuous observation of agent behavior to refine the retrieval process.