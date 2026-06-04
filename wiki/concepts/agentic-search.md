---
concept: Agentic Search
category: Memory & Knowledge Systems
summary: Letting the agent decide when, how, and how often to invoke search tools to pull context on demand, replacing RAG's fixed single-shot retrieval pipeline with iterative, agent-driven retrieval.
aliases: [agentic search, agentic RAG, agent-driven retrieval, iterative retrieval, multi-hop retrieval, search as context engineering]
related: ["[[context-engineering]]", "[[llm-knowledge-wiki]]", "[[robust-tool-design]]", "[[low-floor-high-ceiling-tooling]]", "[[tool-integration-hierarchy]]", "[[persistent-agent-memory]]", "[[model-context-protocol]]", "[[computer-use-automation]]"]
sources: [agentic-search-for-context-engineering-leonie-monigatti-elas]
---

# Agentic Search

Agentic search is the pattern of handing the *decision to retrieve* to the agent itself: rather than running every query through a fixed retrieval pipeline, the agent chooses when to search, which search tool to use, and how many times to iterate before it has enough context. It is the retrieval evolution of Retrieval-Augmented Generation (RAG) — from a static, single-shot fetch bolted in front of the model to a dynamic loop the model drives — and the corpus frames it as the dominant part of `[[context-engineering]]`: deciding what context moves from diverse sources into the LLM's window is mostly a search problem, and the agent is the one making that call.

## Key Mechanics

- **Agent decides when and how often to search**: classic RAG retrieves once on a fixed pipeline, which over-fetches irrelevant context or cannot do multi-hop lookups; agentic RAG empowers the agent to call a search tool zero, one, or many times as the task demands, iterating until the context is sufficient.
- **Many context sources, many native search tools**: the retrievable surface spans local files, databases, the web, agent memory, and agent skills, each with its own search interface — so agentic search is less one tool than a *curated stack* of retrieval techniques the agent selects among.
- **Search is most of context engineering**: the source's claim is that agentic search constitutes roughly 80% of context engineering, because the hard part of curating a context window is deciding what relevant information to pull in from where — exactly the search decision.
- **Retrieval quality still depends on the tools**: agentic search only works if the underlying search tools are well-built and well-described — making `[[robust-tool-design]]` and `[[low-floor-high-ceiling-tooling]]` its enabling substrate rather than incidental detail.

## How It Appears in the Corpus

The Leonie Monigatti (Elastic, "AI Engineer" channel) talk on agentic search for context engineering traces the evolution from traditional RAG — a fixed retrieval pipeline that over-retrieves and is limited to single-hop — to agentic RAG, where the agent decides when and how often to use a search tool. It asserts agentic search is ~80% of context engineering, surveys the diversity of context sources (local files, databases, web, memory, skills) and their native search tools, and demonstrates the pattern across semantic search, full query-language access, and shell-driven file search using LangChain and conference-session data.

## Tensions & Tradeoffs

- **More agency, more failure surface**: handing the agent the retrieval decision introduces failure modes a fixed pipeline never had — the agent may call no tool, the wrong tool, or generate bad parameters — which is precisely the problem `[[robust-tool-design]]` exists to mitigate.
- **Retrieval quality is still the bottleneck**: like `[[llm-knowledge-wiki]]` and `[[persistent-agent-memory]]`, agentic search only helps if the tools surface the *relevant* context; a brittle semantic-search tool that misses exact keywords feeds the agent wrong context regardless of how well it decides to search.
- **Iteration costs tokens and latency**: letting the agent search repeatedly until satisfied trades the predictable cost of single-shot RAG for variable, sometimes high, retrieval cost — the same iteration-vs-economy tension that the `[[tool-integration-hierarchy]]` token discipline addresses from the plumbing side.
- **No silver-bullet tool**: the corpus is explicit that no single search tool covers all query behavior, so agentic search presupposes a deliberately curated stack (`[[low-floor-high-ceiling-tooling]]`) rather than one general retriever.
