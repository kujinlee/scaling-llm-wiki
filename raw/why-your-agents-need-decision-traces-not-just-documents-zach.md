---
tags:
  - video-summary
  - en
  - context graphs
  - neo4j
  - ai agents
  - knowledge graphs
  - graph embeddings
  - llm
  - decision making
video_id: "B9h9ovW5H9U"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Intermediate
score: 3.8
---

# Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j

**Channel:** AI Engineer | **Duration:** 20:12 | **URL:** https://www.youtube.com/watch?v=B9h9ovW5H9U

> [!summary] Quick Reference
> **TL;DR:** This video introduces context graphs using Neo4j to enhance AI agent decision-making by leveraging past decisions, precedents, and causal relationships.
>
> **Key Takeaways:**
> - Understand how context graphs move AI agents beyond answering questions to making informed decisions.
> - Utilize graph embeddings and hybrid search to find structurally and semantically similar past decision traces.
> - Leverage Neo4j's "create context graph" tool to quickly scaffold full-stack AI agent applications.
> - Explore Neo4j Agent Memory for robust short-term, long-term, and reasoning capabilities in AI agents.
>
> **Concepts:** context graphs · neo4j · ai agents · knowledge graphs · graph embeddings · llm · decision making

---

## 1. Understanding Context Graphs: Beyond Basic Retrieval
Context graphs extend traditional knowledge bases used in Retrieval Augmented Generation (RAG) by not only helping AI agents answer questions correctly but also enabling them to make *better decisions*. While knowledge bases provide facts and current states, context graphs integrate precedents, causal chains, and expected outcomes, empowering agents with subject matter expertise.

---

## 2. Core Components and Purpose of a Context Graph
A context graph models information through entities (things that exist), events (decisions, transactions, approvals), and context (policies, past human reasoning, and AI-recorded memory). Its primary goal is to provide agents with dynamic information about *why* decisions were made in the past, allowing them to provide actionable recommendations like "reject" or "accept" instead of just risk scores.

---

## 3. Practical Application: A Financial Analyst Agent Example
Consider a financial analyst agent assessing a loan request. A standard RAG system might provide customer info and transactions, leading to a risk score and review recommendation. A context graph, however, incorporates past decision traces and dynamic information, allowing the agent to provide a definitive "reject" or "accept" decision, complete with the underlying rationale and key risk factors.

---

## 4. Technical Foundations: Hybrid Search and Graph Embeddings
Context graphs leverage a hybrid search approach combining semantic and structural similarity. While vector indexes allow semantic search on text (like 'fraud rejection'), graph embeddings are crucial. Nodes in the graph (e.g., decision traces) are embedded into vectors, enabling lookup of *similar decision traces* by vector similarity. This allows discovery of complex patterns in past decisions that would be difficult with document-based search.

---

## 5. Rapid Development with the "Create Context Graph" Tool
Neo4j offers a "create context graph" command-line tool, similar to `create-react-app`, for quickly scaffolding full-stack AI agent applications. This boilerplate includes backend, frontend, a Neo4j database, and can be customized with various AI frameworks (Pydantic AI, OpenAI, LangGraph, etc.), pre-built domains (healthcare, FinServ), or custom ontologies generated on the fly. It also supports data connectors for importing data from sources like GitHub, Notion, Jira, and Slack.

---

## 6. The Neo4j Agent Memory Package
Underpinning the context graph project is the Neo4j agent memory package, a comprehensive memory API. It manages short-term memory (conversation history), long-term memory (extracted and resolved entities), and reasoning (the context graph traces). The package also includes built-in stages for extracting entities from raw text into a knowledge graph using tools like spaCy and LLMs, ensuring information seamlessly transitions from short-term to long-term memory.

---

## Conclusion
Context graphs represent a significant step in evolving AI agents from information retrieval to intelligent decision-making by integrating historical context and causal relationships. Neo4j provides robust tools and a foundational memory package to facilitate the development and deployment of these advanced agent systems, offering both conceptual clarity and practical implementation pathways.