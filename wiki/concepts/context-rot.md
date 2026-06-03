---
concept: Context Rot
category: Harness & Context Engineering
summary: Behavior degradation caused by overloading the always-loaded context with too much standing material, diluting the relevant signal and making recall unreliable.
aliases: [context rot, context bloat, context overload, oversized claude.md]
related: [claude-md, context-engineering, persistent-agent-memory, llm-knowledge-wiki, context-decay]
sources: [every-claude-code-memory-system-compared-so-you-don-t-have-t, 하네스-공식문서-100번-읽은-것처럼-만들어드림]
---

# Context Rot

Context rot is the degradation of an agent's behavior when its context window is overloaded with too much standing material — most concretely an always-loaded instruction file that has grown too large — so the relevant signal is diluted and recall becomes unreliable. The remedy is to cap what loads by default and push the rest behind on-demand references or retrieval, keeping the persistent core small and high-signal.

## Key Mechanics

- It manifests when a file injected into every session (e.g. `[[claude-md]]`) grows too large; the corpus offers concrete heuristics — keep such a file under roughly 200 lines (Simon Scrapes), or as tight as ~60 lines and shaped like a "map, not a 1,000-page manual" (캐슬).
- The fix is indirection: keep the always-loaded core small and reference external files for extensive context, loading them only when a task needs them.
- It is the failure mode that motivates tiered memory and retrieval: rather than stuffing everything into the prompt, index it and pull only the relevant chunks on demand (see `[[persistent-agent-memory]]` and `[[llm-knowledge-wiki]]`).

## How It Appears in the Corpus

The Simon Scrapes "Every Claude Code Memory System Compared" video names context rot as the central pitfall of native Claude Code memory: overloading `claude.md` degrades the agent's behavior, so the video recommends keeping it under 200 lines and referencing external files, with an auto-generated `memory.md` acting as an index into more granular memory documents.

The 캐슬 (아는 개발자) harness explainer reaches the same conclusion from the harness angle: a context file (`claude.md`/`agent.md`) should be a concise "map, not a 1,000-page manual," written within roughly 60 lines of core, universal rules and grown only incrementally as the agent fails — a tighter line-count rule of thumb for the same dilution problem.

## Tensions & Tradeoffs

- It promotes the recurring "more context is not better context" warning already noted for `[[context-engineering]]` and `[[claude-md]]` into a named failure mode with a concrete (if rough) line-count heuristic.
- The line-count figures conflict across sources (~200 lines vs ~60 lines), confirming that these are rules of thumb, not measured thresholds; the real limit depends on the model, the task, and how much of the window other material already consumes.
- Distinct from `[[context-decay]]`: rot is dilution by *volume* of standing material, decay is loss of earlier context over session *length*. Both stem from the finite window but are attacked oppositely — rot by trimming what loads, decay by re-reading a grounding file — and the two remedies trade off, since the file you re-read to fight decay is the file that, overgrown, causes rot.
- Trading completeness for signal: moving context behind references risks the agent not loading something it actually needed, shifting the burden onto retrieval quality rather than eliminating it.
