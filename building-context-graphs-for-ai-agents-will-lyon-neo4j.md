---
tags:
  - video-summary
  - en
  - context graphs
  - knowledge graphs
  - ai agents
  - neo4j
  - graph embeddings
  - hybrid search
  - agent memory
video_id: "qMV64p-4Deo"
channel: "Neo4j"
lang: EN
type: Framework
audience: Intermediate
score: 4.2
---

# Building Context Graphs for AI Agents, Will Lyon, Neo4j

**Channel:** Neo4j | **Duration:** 20:47 | **URL:** https://www.youtube.com/watch?v=qMV64p-4Deo

> [!summary] Quick Reference
> **TL;DR:** This video explains how Neo4j context graphs empower AI agents with deep understanding, explainability, and auditable decision-making by integrating various data and memory types.
>
> **Key Takeaways:**
> - Context graphs unify data across systems, providing "why" for AI decisions, ensuring explainability and auditability.
> - Enhance AI agents using hybrid search, combining vector similarity and graph traversal for richer, more relevant context.
> - Utilize Neo4j Agent Memory's abstractions (short-term, long-term, reasoning) to build structured, comprehensive agent memory.
> - Integrate all agent memory types into a single connected graph for holistic understanding and shared AI context.
>
> **Concepts:** context graphs · knowledge graphs · ai agents · neo4j · graph embeddings · hybrid search · agent memory

---

## 1. The Imperative of Context Graphs for AI
A context graph is a knowledge graph designed to capture all necessary information for organizational decision-making, aiming to address the "missing why" behind AI agent recommendations and other operational decisions. It integrates data from various disparate systems into a unified view, making it a trillion-dollar opportunity for AI by providing explainability and auditability.

---

## 2. Practical Application in Financial Services
The video presents a financial services example using a Neo4j-powered context graph data model, including people, accounts, transactions, decisions, and policies. A demo application illustrates an AI agent processing a credit limit request, utilizing defined tools to interact with the context graph. The agent fetches relevant data, visualizes interconnected entities, and ultimately provides a recommendation. Importantly, the agent's decision is recorded back into the graph, serving as a precedent for future interactions.

---

## 3. Enhancing AI Agents with Hybrid Search
AI agents leverage the context graph by searching for customer-specific information and traversing relationships to uncover relevant context, such as previous fraud flags. A key technique discussed is "hybrid search," which combines vector similarity search with graph traversal. Neo4j's Graph Data Science (GDS) tools, including graph embeddings like FastRP, allow agents to find not only semantically similar data (via text embeddings) but also structurally similar patterns and relationships within the graph, providing a richer and more relevant context.

---

## 4. Building Context Graphs with Neo4j Agent Memory
Neo4j provides an open-source Python package, "Neo4j Agent Memory," to facilitate the construction of graph-based agent memory, supporting integrations with various agent frameworks (e.g., Google ADK, AWS Strands). This package introduces three critical memory abstractions:
*   **Short-term memory:** Manages conversational state and working memory.
*   **Long-term memory:** Extracts entities and relationships from unstructured message data and loads them into the graph. It employs an optimized pipeline (NER, Glyner 2, LLM fallback) for efficiency and emphasizes domain-specific data models (default POLE+O).
*   **Reasoning memory:** Records the procedural steps, tool calls, and decisions made by the agent, crucial for understanding the agent's logic and for auditing purposes.

---

## 5. Unified Graph for Comprehensive AI Context
By integrating short-term, long-term, and reasoning memories into a single connected graph, the Neo4j agent memory system enables agents to query across all data types for a holistic understanding. The presentation highlights a "Lenny's Podcast Memory" demo, where a context graph is built from podcast transcripts, extracting and enriching entities like locations with geospatial data. Another example, the "Agent Swarm" demo, showcases multiple agents (e.g., anti-money laundering, compliance) sharing a common Neo4j memory layer, collaboratively contributing to and utilizing the shared context.

---

## Conclusion
Context graphs, powered by Neo4j's robust graph database and specialized agent memory tools, empower AI agents with unprecedented depth of understanding and explainability. By unifying various memory types and employing advanced hybrid search techniques, organizations can build more intelligent, auditable, and context-aware AI systems, addressing the critical "why" behind their operational decisions.