---
tags:
  - video-summary
  - en
  - llm wiki
  - knowledge management
  - obsidian
  - ai workflow
  - retrieval augmented generation
  - personal knowledge base
  - claude code
video_id: "iXd0t60YmMw"
channel: "Teacher's Tech"
lang: EN
type: Tutorial
audience: Beginner
score: 4.8
---

# Karpathy's LLM Wiki - Full Beginner Setup Guide

**Channel:** Teacher's Tech | **Duration:** 15:05 | **URL:** https://www.youtube.com/watch?v=iXd0t60YmMw

> [!summary] Quick Reference
> **TL;DR:** This video explains Karpathy's LLM Wiki setup, where AI builds a persistent, interlinked knowledge base from documents, overcoming basic RAG limitations.
>
> **Key Takeaways:**
> - LLM Wiki addresses RAG's memory gaps by building a persistent, interlinked knowledge base that continuously grows.
> - The system uses AI to read raw sources and create/update interlinked markdown files (wiki) guided by a schema.
> - Set up requires Obsidian for viewing, an AI coding agent, and creating `raw`, `wiki`, and `schema` folders.
> - Knowledge compounds over time, allowing AI to answer complex queries from an organized, evolving knowledge base.
> - AI can 'lint' the wiki for accuracy, but human review is essential, especially at early stages.
>
> **Concepts:** llm wiki · knowledge management · obsidian · ai workflow · retrieval augmented generation · personal knowledge base · claude code

---

## 1. The Core Problem with Current AI Document Interaction
Most AI tools, employing Retrieval Augmented Generation (RAG), approach every query from scratch. When you upload documents and ask questions, the AI retrieves relevant pieces and generates an answer. However, it lacks memory and accumulation; asking a similar question later means the AI performs all the work again, without building upon previous interactions. This repetitive, non-compounding process is a significant bottleneck, especially for complex questions requiring connections across multiple documents.

---

## 2. Introducing the LLM Wiki: A Persistent Knowledge Base
Andre Karpathy's concept of the "LLM Wiki" offers a solution to this problem. Instead of re-searching raw documents every time, the AI reads your documents once and constructs a structured, persistent wiki made of interlinked markdown files. When new sources are added, the AI integrates them by extracting key ideas, updating existing pages, creating new concepts, linking related ideas, and even flagging contradictions. This means the wiki continuously grows richer, with connections and synthesis pre-built, allowing the AI to answer questions from an organized, accumulated knowledge base rather than starting from zero.

---

## 3. Architecture and Setup of an LLM Wiki
The LLM Wiki system comprises three simple layers:
1.  **Raw Sources:** Your original, read-only documents (PDFs, articles, notes). The AI reads from these but never alters them.
2.  **Wiki:** A folder of markdown files actively created and maintained by the AI, including index, concept, entity, and summary pages.
3.  **Schema:** A rules document that dictates how the AI should structure the wiki, handle new sources, format pages, and answer questions. For Claude Code users, this is typically a `claude.md` file.

To set up, you'll need Obsidian (a free note-taking app that serves as your viewer for markdown files) and an AI coding agent like Claude Code or OpenAI Codex. The setup involves creating an Obsidian vault with `raw`, `wiki`, and an optional `templates` folder, then placing your customized `claude.md` schema file in the vault's root.

----- 

## 4. Building and Evolving Your Wiki with AI
The video demonstrates building a Japan trip planning wiki. Initially, a travel blog post about Tokyo is added to the `raw` folder. The AI agent, instructed to "ingest the new source," reads the article, extracts concepts like neighborhoods, creates new wiki pages for them, and interlinks them, visible through Obsidian's graph view. When a second source (a Japan food guide) is ingested, the AI doesn't just create new pages; it intelligently updates existing neighborhood pages with food-related information, showing the wiki's cumulative intelligence. Subsequently, asking a question that requires information from both sources yields an answer drawn from the interconnected wiki pages, complete with citations, showcasing a distinct advantage over basic RAG.

---

## 5. Practical Applications and Maintenance
The LLM Wiki is highly versatile. Students and researchers can build structured knowledge bases from papers. Teachers can accumulate curriculum and professional development materials. Businesses can organize meeting notes and project documents for new team members. Curious individuals can create personal encyclopedias from books, podcasts, and articles. The pattern is effective wherever knowledge accumulation and organization over time are desired. 

Maintenance is crucial; the AI can "lint" the wiki, checking for contradictions, outdated claims, orphan pages, or unpaged concepts. This periodic review helps maintain the wiki's health and accuracy as it grows. While powerful, the LLM Wiki works best at personal scale (hundreds of articles), relies on quality input ("garbage in, garbage out"), requires an AI coding agent, and the AI can still make mistakes, necessitating human review, especially in early stages.

---

## Conclusion
The LLM Wiki represents a significant advancement in personal knowledge management using AI. By allowing an AI to build and maintain a structured, persistent knowledge base, it overcomes the limitations of traditional RAG systems that restart from scratch with every query. This approach ensures that knowledge compounds over time, making research, learning, and information retrieval far more efficient and insightful. It's a practical, accessible workflow that puts you in control of your data, housed in plain text files, and offers a dynamic way to interact with and grow your understanding of information.