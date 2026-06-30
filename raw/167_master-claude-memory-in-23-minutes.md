---
tags:
  - video-summary
  - en
  - claude memory
  - LLM memory systems
  - vector databases
  - Hermes agent
  - Memarch
  - context management
  - AI agent development
video_id: "rFWxRZ5D-lM"
channel: "Simon Scrapes"
lang: EN
type: Framework
audience: Advanced
score: 4.8
---

# Master Claude Memory in 23 Minutes

**Channel:** Simon Scrapes | **Duration:** 23:13 | **URL:** https://www.youtube.com/watch?v=rFWxRZ5D-lM

> [!summary] Quick Reference
> **TL;DR:** This video outlines building a hybrid memory system from Memarch and Hermes to significantly enhance Claude's storage, injection, and recall.
>
> **Key Takeaways:**
> - Effective LLM memory relies on robust systems for storing, injecting, and recalling information.
> - Combine automatic, complete data capture (Memarch) with curated critical facts (Hermes) for storage.
> - Load a rich, "frozen snapshot" of key contexts at session start for efficient memory injection.
> - Enhance long-term recall with a multi-tier system using hybrid keyword/semantic vector searches.
> - A hybrid system integrating Memarch's recall with Hermes' injection significantly boosts Claude's capabilities.
>
> **Concepts:** claude memory · LLM memory systems · vector databases · Hermes agent · Memarch · context management · AI agent development

---

## 1. Understanding the Three Pillars of LLM Memory Systems

Effective memory for large language models (LLMs) like Claude is crucial for sustained, intelligent interaction. The video highlights that existing open-source solutions significantly surpass Claude's default memory capabilities. All robust memory systems must answer three fundamental questions:
*   **Storage:** How and when is information saved, whether it's a critical decision or routine conversational context?
*   **Injection:** How is relevant saved information brought back into the LLM's active context window, ensuring lean and timely access?
*   **Recall:** How is past information, ranging from recent to several months or years old, efficiently found and retrieved when needed?
This video dissects Claude's native approach and compares it to advanced systems like Hermes and Memarch across these three pillars, ultimately recommending a hybrid solution.

---

## 2. Advanced Approaches to Memory Storage

Claude's built-in "automemory" silently saves project-level and global preferences to `.md` files, but it's not comprehensive. It only stores what it deems "memory worthy."
*   **Memarch's Approach:** This system uses a `clawed code stop hook` to capture and summarize *every* turn of a conversation using a cheap, fast model (Haiku). This raw data is appended to date-specific memory files, then chunked, hashed, and vectorized into a local Milvus vector database for semantic retrieval. It prioritizes completeness, treating markdown as the source of truth, allowing the database to be rebuilt if lost.
*   **Hermes' Approach:** In contrast, Hermes relies on the agent to decide what to save, using `add`, `replace`, or `remove` tools. It curates essential facts into `memory.md` (environment info) and `user.md` (user profile), enforcing character caps for consolidation. While lean, Hermes also autosaves complete raw transcripts to a database and uses a curator to prune and consolidate information weekly.
Both Memarch and Hermes offer significantly more robust storage than Claude's default. The video recommends combining automatic, complete capture (Memarch) with curated, critical facts (Hermes) for injection.

---

## 3. Optimizing Context Injection into LLM Conversations

Memory injection is about feeding the *right* context at the *right time*, not just loading more.
*   **Claude's Default:** When a session starts, Claude injects the full `claude.md` file. A `pre-tool use hook` can also inject relevant `memory.md` files based on the query.
*   **Memarch's Approach:** Surprisingly, Memarch has no dedicated injection layer; it relies entirely on Claude's default mechanisms. Its strength lies in recall, not immediate injection.
*   **Hermes' Approach:** Hermes excels here by loading a "frozen snapshot" at the start of each session. This includes `claude.md`, `memory.md`, `user.md`, and `soul.md`, totaling around 1,300 tokens. This snapshot is cached per session, providing a rich initial context. Any updates during the session are saved to disk but loaded in the *next* session.
The recommended injection strategy combines Claude's default `claude.md` injection with Hermes' frozen snapshot logic, using consolidated `memory.md`, `user.md`, and `soul.md` for a balanced, context-rich start to every conversation.

---

## 4. Enhancing Long-Term Information Recall

Recall is Claude's biggest weakness out-of-the-box, struggling to retrieve past project or client-specific information without explicitly resuming a session.
*   **Claude's Default:** It checks `automemory` files. If not found, it resorts to "trolling" through past conversations, which is token-intensive and lacks methodology.
*   **Memarch's Three-Tier Retrieval:** This powerful system prioritizes progressive disclosure:
    1.  **Tier 1 (Search Query):** Converts the query into vectors to semantically search the Milvus vector database, finding matches by meaning (e.g., "monetization" for "pricing") and keywords (BM25).
    2.  **Tier 2 (Expand):** If Tier 1 is insufficient, it provides more context and metadata around potential matches.
    3.  **Tier 3 (Raw Dialogue):** As a last resort, it retrieves the full raw session dialogue from the stored bullet summaries.
*   **Hermes' Approach:** Hermes first checks its in-context `memory.md` for answers (zero-cost, instant). If not found, it searches a database of sessions by keywords and summarizes the top three matches using a fast model. While good for exact matches, it lacks semantic search capabilities.

---

## 5. Recommended Hybrid Memory System Setup

The optimal memory system for Claude Code integrates the strengths of all discussed approaches, focusing on best practices for storage, injection, and recall.
*   **Storage:**
    *   Leverage Claude's built-in automemory.
    *   Implement Memarch's `stop hook` to capture *all* conversation transcripts.
    *   Maintain curated `memory.md` and `user.md` files (Hermes logic).
    *   Run a nightly job (Memarch index) to consolidate all transcripts into a semantically searchable vector database.
*   **Injection:**
    *   Adopt Hermes' logic for session start. Inject `claude.md`, `soul.md`, `user.md`, `memory.md`, and potentially today's/yesterday's log (approx. 3,000 cached tokens per session).
*   **Recall:**
    *   Implement a "Tier 0" check: First, search the `memory.md` and daily log files already in the conversation context (zero-cost, immediate).
    *   If not found, proceed to Memarch's three-tier system:
        *   Level 1: Hybrid keyword and semantic search of the vector database.
        *   Level 2: Expand with more context.
        *   Level 3: Retrieve raw dialogue as a last resort.
This hybrid setup offers both rapid access to recent, curated facts and deep, semantic long-term recall, making Claude significantly more capable for complex, multi-client, or long-running projects.

---

## Conclusion

Claude Code's default memory system is currently far outmatched by open-source alternatives like Memarch and Hermes. By strategically combining the strengths of these systems – Memarch's comprehensive, vectorized storage and multi-tier recall with Hermes' curated, consolidated injection and quick in-context lookup – users can build a highly effective and reliable memory framework. This approach ensures Claude stops "forgetting things" and can efficiently access relevant information across vast amounts of past interactions, without incurring excessive token costs for irrelevant context. Implementing such a hybrid system is a must-have for anyone working on complex projects with LLMs.