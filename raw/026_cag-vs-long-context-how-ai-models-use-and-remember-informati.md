---
tags:
  - video-summary
  - en
  - LLM
  - long context
  - cache augmented generation
  - CAG
  - KV cache
  - prompt caching
  - external knowledge
video_id: "B_RrXwDupIg"
channel: "IBM Technology"
lang: EN
type: Analysis
audience: Intermediate
score: 4.2
---

# CAG vs Long Context: How AI Models Use and Remember Information

**Channel:** IBM Technology | **Duration:** 10:59 | **URL:** https://www.youtube.com/watch?v=B_RrXwDupIg

> [!summary] Quick Reference
> **TL;DR:** This video explores Long Context and Cache Augmented Generation (CAG) as effective methods for LLMs to use and remember external information, detailing their distinct advantages.
>
> **Key Takeaways:**
> - Long context windows enable LLMs to directly process vast external documents within the prompt.
> - CAG allows LLMs to remember documents via a KV cache, speeding up repeated queries by 10-40x.
> - Choose long context for one-off queries, but CAG for stable knowledge bases and frequent, repeated lookups.
> - Prompt caching as a service from LLM providers makes CAG more practical and offers substantial cost discounts.
>
> **Concepts:** LLM · long context · cache augmented generation · CAG · KV cache · prompt caching · external knowledge

---

## 1. The Challenge of Providing External Knowledge to LLMs
Large Language Models (LLMs) are limited by their training data and often need access to real-time or private external information. While Retrieval Augmented Generation (RAG) is a well-known method, this video explores two alternative approaches: Long Context and Cache Augmented Generation (CAG).

---

## 2. Long Context Windows: A Simple, Yet Powerful Approach
Long context windows allow developers to 'stuff' all necessary external documents directly into the LLM's prompt. Context window sizes have grown dramatically, from 1,000 tokens (GPT-3 in 2020) to 2 million tokens (Gemini 1.5 Pro in 2024), enabling models to process the equivalent of 20 full-length novels. This strategy eliminates the need for a separate retrieval pipeline, ensuring the model has full access to all provided information.

---

## 3. Limitations of Long Context
Despite its simplicity, long context windows come with several drawbacks. Firstly, costs scale directly with token count, making repeated queries with large contexts expensive. Secondly, processing a vast context window increases latency. Thirdly, LLMs suffer from a 'lost in the middle' effect, where information buried in the middle of the context window is often overlooked, with better recall at the beginning and end. Most significantly, long context requires the model to reprocess all documents from scratch with every single query, leading to inefficiency for repeated tasks.

---

## 4. Cache Augmented Generation (CAG): The Persistent Memory Solution
CAG addresses the reprocessing issue by allowing the LLM to read documents once and remember them. This is achieved through Key-Value (KV) Cache, which represents the model's internal understanding and encoding of text. CAG works in three phases:
1.  **Knowledge Preparation**: Documents are formatted to fit the context window.
2.  **Pre-computation**: The model processes the documents, generates the KV cache, and saves it.
3.  **Inference**: Upon a query, the model loads the pre-computed KV cache, appends the new question, and generates an answer, skipping the full document reprocessing. This can lead to a 10x to 40x speedup for subsequent queries.

However, CAG also has limitations: the entire knowledge base must still fit within the context window, and any changes to source documents require a full re-computation of the cache, making it less suitable for frequently changing data.

---

## 5. When to Choose Long Context vs. CAG
The choice between long context and CAG depends on the use case. Long context is ideal for one-time queries or analyzing a single document, where the overhead of pre-computation isn't justified. It's simple to set up and manage, with costs and latency incurred on every inference. CAG, conversely, shines in scenarios with stable knowledge bases and repeated queries, such as an HR chatbot. While the first query is as expensive as long context, subsequent queries become significantly faster and cheaper due to the cached KV state.

---

## Conclusion
Both long context and Cache Augmented Generation (CAG) offer powerful ways to provide LLMs with external knowledge, each with distinct advantages and ideal applications. The emergence of "prompt caching" as a service from major LLM providers further enhances CAG's practicality, abstracting cache management and offering substantial cost discounts (e.g., 90%) on cached reads. These techniques demonstrate that effective external knowledge integration can be achieved without always resorting to traditional RAG pipelines, opening up new possibilities for LLM applications.