---
tags:
  - video-summary
  - en
  - large language models
  - knowledge graph
  - code analysis
  - token optimization
  - Graphify
  - AI agents
  - retrieval augmented generation
video_id: "HQEm4rBKdec"
channel: "Eric Tech"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.4
---

# Graphify Solves Claude's Biggest Limitation (Finally)

**Channel:** Eric Tech | **Duration:** 11:52 | **URL:** https://www.youtube.com/watch?v=HQEm4rBKdec

> [!summary] Quick Reference
> **TL;DR:** This video introduces Graphify, a tool that optimizes LLM interaction with local codebases by creating knowledge graphs, reducing tokens and boosting accuracy.
>
> **Key Takeaways:**
> - Graphify transforms local codebases into structured knowledge graphs for LLMs.
> - It significantly reduces LLM token consumption, improving performance and accuracy.
> - Explore code connections visually or query concepts using command-line tools.
> - Efficiently update knowledge graphs by re-extracting only changed files.
> - Integrates with various AI agent frameworks and RAG systems like Claude Code.
>
> **Concepts:** large language models · knowledge graph · code analysis · token optimization · Graphify · AI agents · retrieval augmented generation

---

## 1. Introduction to Graphify and its Core Problem
Graphify is a powerful tool designed to enhance the efficiency and accuracy of Large Language Models (LLMs) when interacting with local codebases and documentation. Inspired by Andrej Karpathy's insights on LLM knowledge bases, Graphify addresses the challenge of high token consumption and slower performance when LLMs process raw files directly.

---

## 2. Installation and Setup
To get started with Graphify, users need Python (version 3.10 or above) and a package installer like UV (or PIPX). The video demonstrates a manual installation process on macOS, involving installing Python and UV, then using UV to install the Graphify package. After installation, `graphify install` registers the tool's capabilities as "skills" with AI assistants like Claude Code, creating a `.claude` folder and a `claude.md` usage guide. Graphify supports various AI agent frameworks, including Codex, OpenCode, and Hermes agents.

---

## 3. Building a Knowledge Graph from Your Codebase
The primary function of Graphify is to convert a local folder containing code and documentation into a structured knowledge graph. By simply running `graphify dots` in the desired directory, the tool analyzes the content. Users can choose the scope of extraction: "code only," "code plus documentation (skipping images)," or "full extraction (including images)," depending on their research needs. This process generates an interactive `graph.html`, a `graph.json` (raw data), and a `graph.report`. The speaker highlights a significant benefit: a 27x reduction in token consumption when querying the LLM about the codebase, leading to faster, more accurate results.

---

## 4. Interacting with and Querying the Knowledge Graph
Once the knowledge graph is built, it offers various ways to interact with the codebase. The `graph.html` provides an interactive visualization where users can explore connections between files and components, such as viewing specific layouts and their related API routes. Graphify also includes command-line functionalities like `graphify path <source> <destination>` to find the shortest connection between two files or functionalities (e.g., admin panel and AI chat). The `graphify explain <concept>` command allows users to query the graph for explanations of specific concepts within the codebase, providing clear definitions based on the indexed knowledge.

---

## 5. Advanced Features and Integration Options
Graphify extends its utility with several advanced features. Users can `graphify query` to ask specific questions directly to the knowledge graph. For managing evolving codebases, `graphify raw --update` re-extracts only changed files, efficiently updating the knowledge base. The tool can also generate Obsidian vaults (`graphify obsidian`) from specific folders (e.g., `/docs`), useful for documentation and knowledge management. Furthermore, Graphify supports generating various output formats and integrations, including wikis, SVGs, Neo4j graphs, and even an MCP server to allow other LLMs to query the knowledge base, demonstrating its versatility for different RAG (Retrieval Augmented Generation) systems.

---

## Conclusion
Graphify presents itself as an essential tool for anyone working with large language models on complex codebases. By transforming raw files into an optimized knowledge graph, it dramatically improves LLM performance, reduces token usage, and enhances accuracy. Its diverse functionalities, from interactive visualization and targeted querying to advanced integrations and efficient updates, make it invaluable for research, code comprehension, and building more intelligent AI-powered applications.