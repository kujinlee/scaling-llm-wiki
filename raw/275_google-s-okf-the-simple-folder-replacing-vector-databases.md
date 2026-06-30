---
tags:
  - video-summary
  - en
  - open knowledge format
  - okf
  - ai standard
  - knowledge management
  - vector databases
  - llm context
  - metadata as code
video_id: "2kKkb01GxYQ"
channel: "Cloud Codes"
lang: EN
audience: Intermediate
score: 4.4
---

# Google's OKF: The Simple Folder Replacing Vector Databases

**Channel:** Cloud Codes | **Duration:** 6:00 | **URL:** https://www.youtube.com/watch?v=2kKkb01GxYQ

> [!summary] Quick Reference
> **TL;DR:** This video introduces Google's Open Knowledge Format (OKF), a markdown-based AI standard making expensive vector databases optional for curated knowledge.
>
> **Key Takeaways:**
> - Explore OKF for managing curated enterprise knowledge with LLMs.
> - Consider markdown files as a portable, version-controlled context for AI agents.
> - Leverage OKF to establish metadata as code workflows alongside your SQL.
> - Recognize OKF's strength in accuracy, versioning, and portability for agent context.
> - Understand that OKF complements, rather than replaces, vector databases for unstructured data.
>
> **Concepts:** open knowledge format · okf · ai standard · knowledge management · vector databases · llm context · metadata as code

---

## 1. Google's Open Knowledge Format (OKF): A New AI Standard
▶ [0:00–0:34](https://www.youtube.com/watch?v=2kKkb01GxYQ&t=0s)
Google has introduced OKF, the Open Knowledge Format, turning simple text files into an official AI standard. This "beautifully boring" standard challenges the necessity of expensive vector databases by allowing AI agents to directly read and follow links within markdown files to answer complex queries. Version 0.1 was shipped by Google Cloud in June.

---

## 2. Addressing the Context Problem for LLMs
▶ [0:34–1:09](https://www.youtube.com/watch?v=2kKkb01GxYQ&t=34s)
Large Language Models often struggle not with intelligence, but with access to context — specific knowledge about systems, metrics, and data structures that is usually scattered across various enterprise tools and documents. OKF provides a unified, readable context, enabling agents to operate more effectively by simply opening a file and following links, rather than reassembling context from disparate sources for every query.

---

## 3. OKF vs. RAG and the LLM Wiki Concept
▶ [1:09–2:40](https://www.youtube.com/watch?v=2kKkb01GxYQ&t=69s)
Traditional Retrieval Augmented Generation (RAG) involves uploading documents, chunking them, vectorizing, and storing them in a vector database. This approach means the model "rediscovers" information repeatedly, as knowledge doesn't accumulate. OKF, inspired by Andrej Karpathy's "LLM wiki" concept, allows models to build and maintain a wiki where knowledge compounds. It defines three layers: raw sources, a model-owned wiki, and a schema file to manage it, standardizing what were previously bespoke solutions.

---

## 4. Structure and Design Principles of an OKF Bundle
▶ [2:40–3:53](https://www.youtube.com/watch?v=2kKkb01GxYQ&t=160s)
An OKF bundle is a directory of markdown files, where each file represents a single concept (e.g., a table, a metric, an API). The file path serves as its identity. Each file begins with a small YAML front matter block (only `type` is required), followed by plain markdown content. Ordinary markdown links connect concepts, transforming a flat folder into a rich graph. Optional `index` and `log` files provide navigation and version history. The design emphasizes minimal opinionation, independence of producers and consumers, and functioning purely as a format, not a platform, ensuring portability and zero installation.

---

## 5. Practical Advantages and Use Cases
▶ [3:53–5:07](https://www.youtube.com/watch?v=2kKkb01GxYQ&t=233s)
Unlike RAG which re-derives knowledge from raw chunks, OKF stores curated, cross-linked concepts that agents can directly read and edit. It offers significant advantages over solutions like Notion (which locks data into a database) and vector indexes (which provide fuzzy chunks). OKF is portable markdown, requiring zero translation for agents, and drastically reduces infrastructure costs and complexity compared to vector databases. Google has already released supporting tools, including a BigQuery agent for bundle creation and a static visualizer. Key use cases include "metadata as code," on-call agents utilizing runbooks, vendor catalogs for agents, and model-maintained team wikis.

---

## Conclusion
▶ [5:07–6:01](https://www.youtube.com/watch?v=2kKkb01GxYQ&t=307s)
While OKF will not replace vector databases for large, unstructured, or uncurated document piles where semantic search is paramount, it shines where knowledge is curated, requiring accuracy, version history, context fit, and portability. OKF represents a broader shift towards context becoming a portable, version-controlled artifact. This movement towards open formats, which previously revolutionized data, is now poised to win in the agent era, proving that sometimes the "boring" solution is indeed the better one.