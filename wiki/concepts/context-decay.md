---
concept: Context Decay
category: Harness & Context Engineering
summary: Degradation that sets in as a long task crowds earlier instructions out of the finite context window, causing the agent to forget constraints or terminate work prematurely.
aliases: [context decay, context window forgetting, long-session forgetting, premature task termination]
related: ["[[context-rot]]", "[[claude-md]]", "[[context-engineering]]", "[[harness-engineering]]", "[[persistent-agent-memory]]"]
sources: [하네스-공식문서-100번-읽은-것처럼-만들어드림]
---

# Context Decay

Context decay is the degradation that sets in as a task runs long: because the context window is finite, an agent forgets instructions and content from earlier in the session, or terminates the work prematurely, once the relevant material falls out of or is crowded within that window. It is distinct from `[[context-rot]]` — rot is signal *dilution* caused by too much standing material loaded up front, while decay is the *loss of earlier context over the length of a session*. The standard remedy is a context file (`[[claude-md]]` / `agent.md`) read first on every session so the agent is continually re-grounded in the project's rules, goals, and prohibitions despite its forgetting.

## Key Mechanics

- Finite-window failure: as the conversation or task lengthens, the model loses access to earlier content, so it either forgets prior constraints or stops the task short of completion.
- Re-grounding as the fix: a context file read at the start of every session (and re-consulted as work proceeds) restores the durable rules and objectives, preserving continuity across the agent's lossy memory.
- It is one of the two motivating problems behind `[[harness-engineering]]` (the other being the rules-and-fence problem), and specifically the problem the context-file pillar of a harness exists to solve.

## How It Appears in the Corpus

The 캐슬 (아는 개발자) harness explainer names "context decay" (컨텍스트 부패) as one of the two problems that make harness engineering necessary, citing an Anthropic experiment in which Claude Opus, while cloning `claude.ai`, visibly forgot earlier work and cut tasks short as the session grew. It presents the always-read `claude.md`/`agent.md` context file as the structural answer.

## Tensions & Tradeoffs

- Adjacent to `[[context-rot]]` but opposite in cause: decay is loss from session *length*, rot is dilution from *volume* of standing material — both stem from the finite window and are attacked differently (decay by re-grounding, rot by trimming).
- The two remedies pull against each other: re-grounding wants a richer context file, but enlarging that file feeds `[[context-rot]]`, so the file must stay small while still re-establishing the essentials — the same map-not-manual discipline that bounds `[[claude-md]]`.
- A single re-read file cannot hold everything a long task touches; deeper, retrieval-backed `[[persistent-agent-memory]]` addresses what re-grounding alone cannot carry.
