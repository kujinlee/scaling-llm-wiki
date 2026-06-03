---
concept: LLM Tool Augmentation
category: LLM Internals & Training
summary: Teaching a model to emit special tokens that pause generation, call an external tool (search, code interpreter), and inject the result into its context window as working memory — overcoming both knowledge and computation limits.
aliases: [tool use, LLM tool use, tool augmentation, special tokens for tools, working memory, context window as working memory, search and code tools]
related: [tokens-to-think, llm-hallucination, agentic-loop, robust-tool-design, context-engineering, next-token-prediction]
sources: [deep-dive-into-llms-like-chatgpt]
---

# LLM Tool Augmentation

LLM tool augmentation is the model-level mechanism by which a language model overcomes its own cognitive limits by reaching outside itself: it is trained to emit *special tokens* (e.g. `search_start`, `code_start`) that pause its own generation, trigger an external function — a web search, a code interpreter — and then paste the returned result back into its context window, where it becomes part of the model's *working memory* for the rest of the response. This cleanly separates two kinds of memory: the vague, lossy "recollection" baked into the model's parameters, versus precise, fresh facts and computations pulled in on demand. It is the cognition-level foundation beneath the corpus's whole agentic stack — the raw capability that the `[[agentic-loop]]` orchestrates and `[[robust-tool-design]]` hardens.

## Key Mechanics

- **Special tokens trigger tool calls**: the model learns to emit dedicated tokens that halt generation and hand control to an external function, then resume once the result returns — tool use expressed as a learned token-emission behavior, not a bolted-on wrapper.
- **Results enter the context window as working memory**: retrieved text or computed output is injected into the context, which acts as fast, precise working memory distinct from the slow, vague knowledge held in parameters (`[[next-token-prediction]]`).
- **Mitigates knowledge limits**: a web search supplies real facts the model would otherwise fabricate, directly attacking `[[llm-hallucination]]` by grounding answers in retrieved sources rather than parametric guesswork.
- **Mitigates computation limits**: a code/Python interpreter performs exact arithmetic and manipulation the model cannot reliably do within its per-token budget — the external counterpart to spreading reasoning across `[[tokens-to-think]]`.

## How It Appears in the Corpus

The Andrej Karpathy "Deep Dive into LLMs like ChatGPT" tutorial presents tool use as a core way to overcome LLM limitations: by learning to emit special tokens, models pause generation, execute external functions (web search, code interpreter), and integrate the retrieved information into their working memory (the context window) — greatly enhancing factuality and problem-solving versus relying on parametric "vague recollection" alone.

## Tensions & Tradeoffs

- **The cognition view beneath the agentic view**: this is the same act the `[[agentic-loop]]` treats as orchestration and `[[robust-tool-design]]` treats as an authoring problem — here it is framed as the model's way of extending its *cognition*, making explicit why "the model thinks, the tools do" is a capability, not just an architecture choice.
- **Working memory is finite**: pulling tool output into the context window spends the same finite budget `[[context-engineering]]` governs, so heavy retrieval competes with reasoning for space — tool augmentation trades parametric vagueness for context-window pressure.
- **Dependency on tool availability and correctness**: the model is only as factual as the source it searches and only as exact as the interpreter it calls — a wrong or missing tool result is injected with the same authority as a right one.
- **Distinct from internal reasoning**: `[[tokens-to-think]]` solves limits by reasoning *internally* across more tokens; tool augmentation solves them by offloading *externally* — complementary strategies, with tools winning on precision and internal reasoning winning where no tool fits.