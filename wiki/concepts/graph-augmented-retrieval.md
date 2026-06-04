---
concept: Graph-Augmented Retrieval
category: Memory & Knowledge Systems
summary: Grounding RAG in a knowledge graph so retrieval pulls specific, complete, relationship-connected context (e.g. a full patient history) rather than the generic, disconnected chunks a vector-only store returns.
aliases: [graph-augmented retrieval, GraphRAG, graph RAG, graph-grounded RAG, graph-powered RAG, knowledge-graph retrieval]
related: ["[[context-graph]]", "[[agentic-search]]", "[[llm-knowledge-wiki]]", "[[persistent-agent-memory]]", "[[codebase-knowledge-graph]]", "[[reasoning-trace-memory]]"]
sources: [connecting-the-dots-with-context-graphs-stephen-chin-neo4j]
---

# Graph-Augmented Retrieval

Graph-augmented retrieval is the technique of grounding Retrieval-Augmented Generation in a knowledge graph so that retrieval returns *specific, complete, relationship-connected* context instead of the generic, loosely-related chunks a vector-only store surfaces. A baseline LLM answers from parametric memory and gives generic responses; a vector database improves on that but still returns somewhat generic, disconnected matches; a graph-grounded retriever instead traverses explicit relationships to pull an entity's full connected history — making the agent's recommendation precise and personalized rather than plausible-but-vague. It is the retrieval face of the `[[context-graph]]`: the mechanism that converts a connected store of facts into grounded answers.

## Key Mechanics

- **Three retrieval qualities compared**: baseline LLM (generic), vector DB (better but still generic), graph-grounded RAG (specific and complete) — the graph wins by following relationships, not just nearest neighbors. The canonical illustration is medical advice: a graph pulls in a patient's actual diagnoses, operations, and medications, so the answer is tailored to that person rather than to the population.
- **Relationships drive the fetch**: because edges are explicit, retrieval performs fast multi-hop traversals to gather all the context connected to a query entity — the connected subgraph, not an isolated chunk.
- **Hybrid retrieval stack**: the retriever combines the knowledge graph with vector/similarity search and graph data-science algorithms (graph embeddings, community detection such as Louvain), blending semantic matching with structural traversal.
- **LLM + graph division of labor**: the LLM supplies language, reasoning, and creativity while the graph supplies knowledge, context, and enrichment — the model reasons over context the graph guarantees is grounded and complete.

## How It Appears in the Corpus

The Stephen Chin (Neo4j, "AI Engineer" channel) talk contrasts a baseline LLM's generic answer, a vector database's marginally-better-but-still-generic medical advice, and a graph-grounded RAG that pulls a complete patient history (diagnoses, operations, medications) to make a highly personalized, accurate recommendation. It frames relationships as first-class citizens enabling performant hop traversals and explainable decisions, and demonstrates the same retrieval style in a financial-services application that grounds loan-approval reasoning in a customer's connected financial and fraud history.

## Tensions & Tradeoffs

- **Distinct from `[[agentic-search]]`**: agentic search is about the agent *deciding when and how often* to retrieve; graph-augmented retrieval is about the *structure of the store* being retrieved from — they compose, an agent can drive iterative retrieval over a graph. It also differs from `[[llm-knowledge-wiki]]`'s semantic-markdown / vector-RAG approach by making relationships, not chunk similarity, the primary retrieval signal.
- **Build cost vs. precision**: constructing and maintaining a knowledge graph is far more infrastructure than embedding a pile of documents, justified only when the connected context the graph captures actually improves answers over flat retrieval — the same build-cost-vs-payoff tradeoff as `[[codebase-knowledge-graph]]`.
- **Graph quality is the bottleneck**: retrieval is only as good as the graph's nodes, edges, and embeddings; missing or wrong relationships silently feed the agent incomplete context, and relationship depth bounds how many hops of real context can be reached — the recurring "retrieval quality is the new bottleneck" caveat.
- **Vendor framing**: the comparison comes from a graph-database vendor's talk, so the superiority of graph grounding is asserted through demos rather than controlled measurement; the durable idea is *relationship-grounded retrieval*, not a specific stack.
