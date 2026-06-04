---
concept: Context Graph
category: Memory & Knowledge Systems
summary: A knowledge-graph-backed memory architecture that unifies an agent's short-term, long-term, and reasoning memory into one traversable structure, giving decisions grounded context and explainable provenance.
aliases: [context graph, context graphs, agent context graph, unified memory graph, graph agent memory, Neo4j agent memory]
related: ["[[graph-augmented-retrieval]]", "[[reasoning-trace-memory]]", "[[persistent-agent-memory]]", "[[memory-storage-injection-recall]]", "[[codebase-knowledge-graph]]", "[[causal-decision-modeling]]", "[[ontology-operating-system]]", "[[llm-knowledge-wiki]]", "[[cross-tool-memory]]"]
sources: [connecting-the-dots-with-context-graphs-stephen-chin-neo4j]
---

# Context Graph

A context graph is an agent-memory architecture built on top of a knowledge graph that unifies three otherwise-fragmented kinds of memory — short-term, long-term, and reasoning — into a single traversable structure, so an AI agent can act with grounded context and produce decisions that are explainable and auditable. Where enterprise knowledge is normally scattered across Slack, customer threads, CRMs, and internal systems — leaving agents to decide without context — the context graph consolidates it into explicit nodes and relationships and layers an agent's operational state and decision history on top. It is the graph-database expression of `[[persistent-agent-memory]]`: rather than tiered markdown files, memory lives in a connected graph where the *relationships between facts* are first-class and queryable.

## Key Mechanics

- **Knowledge-graph foundation**: the substrate stores nodes (people, things, companies) with their properties and vector embeddings, and explicit edges (relationships) between them. Combining an LLM's language/reasoning with the graph's knowledge/context lets the system store relationships, visualize data, and surface hidden patterns rather than answering from disconnected fragments.
- **Three unified memory layers**: *short-term memory* holds current pipeline activity, conversations, and agent state, persisted in the graph; *long-term memory* holds organized historical data, domain models, and past agent interactions across tasks and users; *reasoning traces* (`[[reasoning-trace-memory]]`) capture the "why" behind decisions — thought process, provenance, and lessons from past experience.
- **Relationships as first-class citizens**: because edges are explicit, the system performs highly performant hop traversals and yields explainable decisions, further aided by graph embeddings and community-detection algorithms (e.g. Louvain) that group related entities.
- **Write-back loop**: agents retrieve through a context-graph tool (combining the knowledge graph, vector search, and graph data-science algorithms), then push new information and decisions back into the context memory, so subsequent queries reuse accumulated reasoning traces for improved outputs — knowledge accumulation as a graph rather than a document store.
- **Knowledge hub effect**: centralizing previous decisions and advice turns an application into an intelligent knowledge hub able to solve complex, cross-domain problems that span support, CRM, and internal business systems.

## How It Appears in the Corpus

The Stephen Chin (Neo4j, "AI Engineer" channel) talk "Connecting the Dots with Context Graphs" introduces context graphs as a way to escape fragmented, siloed enterprise knowledge, noting Gartner's placement of context graphs on the AI hype cycle. It presents the open-source Neo4j Agent Memory package, which unifies short-term, long-term, and reasoning memory into a context-graph structure, and demonstrates it with a Lenny's-podcast summarization graph and a financial-services application that integrates support tickets, CRM, and internal systems via OpenAI embeddings — querying a loan-approval decision (for "Jessica Norris") to surface financial history, prior rejections, and fraud patterns through Cypher queries over a traversable graph.

## Tensions & Tradeoffs

- **Graph substrate vs. tiered files**: it is an alternative implementation of `[[persistent-agent-memory]]` and the storage/injection/recall axes of `[[memory-storage-injection-recall]]` — trading the simplicity of markdown tiers for explicit, queryable relationships, at the cost of standing up and maintaining a graph database. It shares the relationship-first discipline of `[[codebase-knowledge-graph]]` and the entity/relationship modeling of an `[[ontology-operating-system]]`, applied to agent memory.
- **Graph quality bounds the answer**: like `[[llm-knowledge-wiki]]` and `[[agentic-search]]`, the context graph only helps if its nodes, edges, and embeddings surface the *relevant* connected context; a thin or wrong graph confidently feeds the agent bad grounding — relationship depth caps how far reasoning can hop, the same ceiling noted for `[[codebase-knowledge-graph]]`.
- **Build and maintenance cost**: consolidating diverse sources into a graph and keeping it current is real infrastructure, and the unification of three memory types into one store is heavier to operate than a single conversational context.
- **Vendor vantage**: the framing and demo come from a graph-database vendor, so the architecture is presented as transformative rather than independently measured — the durable idea is the *graph-as-unified-agent-memory* pattern, not any single product.
- **Ownership and portability**: centralizing all memory in one graph store raises the custody and lock-in questions `[[cross-tool-memory]]` addresses, since the value concentrates in a single, vendor-shaped structure.
