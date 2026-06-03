---
tags:
  - video-summary
  - en
  - ai agents
  - context management
  - llm context
  - sub-agents
  - memory strategies
  - ai engineering
  - arize
video_id: "esY99nYXxR4"
channel: "AI Engineer"
lang: EN
type: Analysis
audience: Advanced
score: 4.6
---

# How we solved Context Management in Agents — Sally-Ann Delucia

**Channel:** AI Engineer | **Duration:** 16:17 | **URL:** https://www.youtube.com/watch?v=esY99nYXxR4

> [!summary] Quick Reference
> **TL;DR:** This video details how Arize improved AI agent performance by solving context management challenges, employing smart truncation memory and specialized sub-agents.
>
> **Key Takeaways:**
> - Context engineering is now more critical than prompt engineering for AI agent success.
> - Implement 'Smart Truncation Memory' (first/last 100 characters) for effective context recall.
> - Delegate data-intensive tasks to specialized sub-agents to manage heavy context loads efficiently.
> - Use 'Long Session Evals' to proactively test and identify context management issues in agents.
>
> **Concepts:** ai agents · context management · llm context · sub-agents · memory strategies · ai engineering · arize

---

## 1. The Critical Role of Context Engineering
The speaker, Sally Ann from Arize, emphasizes that context engineering has surpassed prompt engineering in importance for the success of AI agents. It's not merely about fitting data within token limits, but strategically selecting the most crucial information for the model to process. This strategic approach is vital because poor context leads to inaccurate agent responses, making it a critical product and user experience challenge, not just an engineering one. The complexities arise when agents, like Alex built by Arize, operate on vast datasets such as AI observability traces, where context can multiply rapidly.

---

## 2. Escaping the Vicious Context Loop: Evolution of Strategies
The Arize team encountered a "vicious loop" where Alex, an AI agent used to build itself, would fail due to ever-growing context data (spans) hitting token limits. Initial attempts to solve this included:
*   **Naive Truncation:** Simply taking the first 100 characters proved ineffective as the agent "forgot" crucial information, leading to broken reasoning and inability to handle follow-up questions.
*   **Summarization:** Relying on LLMs to condense context was inconsistent and unreliable, lacking control over which parts of the information were deemed important.
The breakthrough came with **Smart Truncation Memory**. This strategy involves keeping the first and last 100 characters of the context, truncating the middle, but storing the full middle section in an accessible memory store. Alex can then retrieve specific information from this memory (e.g., tool calls, past messages) when needed, providing more control and improving reasoning over conversations.

---

## 3. Managing Long Conversations and Data-Intensive Tasks with Sub-Agents
As users engage in longer conversation sessions, agents face challenges with accumulating context and late-appearing failures. To address this, Arize implemented **Long Session Evals**, a testing methodology that loads 10 conversation turns and evaluates the 11th to proactively identify context management issues.
A significant realization was that not all context belongs to a single agent. For heavy data operations, such as searching through extensive traces, keeping all intermediate data within the main conversation context proved problematic. The solution was the introduction of **Sub-agents**. The main agent maintains a light conversation history and delegates data-intensive tasks to specialized sub-agents. These sub-agents handle the heavy data context and complex reasoning, returning only the relevant results to the main agent, thus keeping the primary conversation focused and efficient.

---

## 4. Unresolved Challenges in Advanced Context Management
Despite their successes, Arize continues to grapple with several advanced context challenges:
*   **Huge Context Limits:** Extremely large prompts or inputs still hit provider limits, and the ongoing strategy involves further breaking down tasks into more sub-agents.
*   **Long-Term Memory:** Current memory solutions are insufficient for users who want to sustain very long conversations (20+ turns) or reference past discussions across different chat sessions. Real long-term memory is a current development focus.
*   **Context Selection Heuristics:** The "first 100, last 100" truncation remains a heuristic. The team is researching more principled context budgeting and clear metrics for context quality, noting that even advanced models like Claude employ similar truncation/compression strategies.

---

## Conclusion
Effective context management is an iterative and ongoing process crucial for the success of AI agents. Key takeaways from Arize's experience include the paramount importance of context engineering, robust memory strategies, and continuous evaluation. Ultimately, agents fail not due to inadequate prompts, but due to issues in managing and utilizing context effectively, driving a shift in focus from prompt optimization to strategic context engineering.