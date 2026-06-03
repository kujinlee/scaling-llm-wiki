---
tags:
  - video-summary
  - en
  - code analysis
  - ai research tools
  - understand anything
  - graphy ai
  - knowledge base
  - code documentation
  - llm tools
video_id: "Ynv_WYO_slw"
channel: "Eric Tech"
lang: EN
type: Analysis
audience: Intermediate
score: 4.8
---

# Understand-Anything vs Graphify: I Tested Both on My SaaS

**Channel:** Eric Tech | **Duration:** 16:21 | **URL:** https://www.youtube.com/watch?v=Ynv_WYO_slw

> [!summary] Quick Reference
> **TL;DR:** This video compares Understand Anything and Graphy AI, two AI tools for converting codebases into interactive knowledge bases, highlighting their features and performance.
>
> **Key Takeaways:**
> - Understand Anything uses more AI tokens for initial graph generation than Graphy AI.
> - Understand Anything offers superior, hierarchical dashboards for code visualization.
> - Understand Anything delivers more visualized, detailed AI query responses with context.
> - Graphy AI supports local LLMs, offering better privacy and cost control options.
>
> **Concepts:** code analysis · ai research tools · understand anything · graphy ai · knowledge base · code documentation · llm tools

---

## 1. Introduction to AI Codebase Research Tools
This video introduces and compares two AI-powered tools, "Understand Anything" and "Graphy AI," designed to transform codebases into interactive knowledge bases. Both tools aim to assist developers with code research, understanding, and saving AI tokens. The primary goal of the video is to demonstrate the setup, usage, and key differences between these two platforms through a direct comparison.

---

## 2. Setup and Installation Guide
The video provides a step-by-step guide for installing both Graphy AI and Understand Anything. Graphy AI installation typically involves using `uv` (a Python package installer) and installing Graphy skills. Understand Anything is installed as a plugin through the Cloud Code marketplace. The process includes cloning the repository and adding the plugin to the project level, setting the stage for subsequent comparisons and testing.

---

## 3. Knowledge Graph Generation and Token Consumption
Once installed, the video compares how each tool generates a knowledge graph from a codebase. Understand Anything begins by analyzing candidate files, offering options to scope the analysis (e.g., core applications, libraries) and to generate an `understand ignore` file to exclude irrelevant files like tests or mock data, optimizing the analysis. Graphy AI also allows for scope definition and file exclusion based on pre-defined ignore files. A key finding is that Understand Anything consumed approximately double the AI tokens compared to Graphy AI for the initial graph generation, which is a significant consideration for budget-conscious users.

---

## 4. Dashboard Visualization and User Experience
A major point of comparison is the visualization of the generated knowledge bases. Understand Anything provides a superior, more intuitive, and hierarchical dashboard. It offers a project overview with distinct sections and connections between layers. Users can drill down into specific components, trace their usage, identify parent-child relationships, and view summaries and definitions of files. This detailed and structured view makes it easier to understand code dependencies and identify unused code. In contrast, Graphy AI's output is presented as a more cluttered HTML file with all components on a single, flat graph, making it harder to discern relationships beyond direct neighbors.

---

## 5. AI Query Capabilities and Response Quality
The video evaluates how both tools perform when answering specific AI queries about the codebase, using the same question for both. While both tools return similar token usage and time for queries, Understand Anything consistently delivers a more visualized and detailed response. It provides file locations, context (e.g., original source like an N8N workflow), detailed algorithms with step-by-step breakdowns, and even flowcharts for better understanding. Graphy AI, while providing accurate information, tends to present it in a less structured and more text-heavy format.

---

## 6. Additional Features: Onboarding, Updates, and Privacy
Beyond core functionality, the video touches on other features: 
-   **Onboarding**: Understand Anything summarizes the codebase into a single markdown (`.md`) file, including project overview and architecture layers. Graphy AI generates a wiki with multiple articles.
-   **Stale Data**: Both tools offer auto-update workflows that automatically refresh the knowledge graph on Git commits or branch checkouts, ensuring the data remains current.
-   **Privacy and Local Models**: Graphy AI supports local language models (like Ollama or Bedrock), allowing users to process code locally for privacy and cost control. Understand Anything, by default, does not document support for local models, meaning code might be sent to external AI providers depending on the IDE's configuration.

---

## Conclusion
In summary, both Understand Anything and Graphy AI offer valuable features for AI-powered codebase research. Understand Anything excels in dashboard visualizations, AI query response quality (especially with its structured and visual explanations), and providing an `.md` summary for onboarding. Graphy AI, on the other hand, wins on lower token consumption for initial graph generation, offers a wiki for onboarding, and crucially, supports local large language models for enhanced privacy and cost efficiency. The video recommends trying both, using Understand Anything for better visualization and Graphy AI for lower token usage or when local model support is essential. The ultimate choice depends on specific priorities regarding cost, visualization preference, and data privacy needs.