---
concept: CLAUDE.md
category: Harness & Context Engineering
summary: The project-specific documentation file an agent reads every session: build/test instructions, forbidden actions, and conventions — the foundational always-loaded tier of agent context.
aliases: [Claude MD, project memory file, agent context document, agent.md]
related: ["[[compound-engineering]]", "[[agentic-issue-resolution]]", "[[multi-agent-code-review]]", "[[self-verification-loop]]", "[[context-rot]]", "[[persistent-agent-memory]]", "[[context-decay]]", "[[harness-engineering]]", "[[permission-tiering]]", "[[plan-first-workflow]]"]
sources: [live-coding-session-with-boris-cherny-and-jarred-sumner, every-claude-code-memory-system-compared-so-you-don-t-have-t, every-level-of-claude-explained-in-21-minutes, 하네스-공식문서-100번-읽은-것처럼-만들어드림, claude-code-창시자-boris의-ai-에이전트-셋업-전부-다-까보자, 12-claude-code-features-every-engineer-should-know-subagents]
---

# CLAUDE.md

CLAUDE.md is the project-specific documentation file that supplies a coding agent with the operational knowledge it needs to work in a codebase autonomously. It is the cornerstone that makes high levels of automation possible: without a meticulous, well-maintained context document, agents cannot reliably build, test, or repair a project on their own. Loaded at the start of every session, it carries rules, brand information, and coding conventions — the agent's first and most foundational tier of memory. The file is tool-agnostic in spirit; the same role appears under generic names like `agent.md` for non-Claude agents.

## Key Mechanics

- Captures the concrete operational knowledge of a repository: how to build, how to run, how to write and execute tests, folder structure, dependencies, tech-stack and naming conventions, and how to interpret CI errors and build logs.
- Specifies *forbidden* actions, not only how-to: an explicit list of what the agent must not do (e.g. never modify migration files without authorization) is as important as the positive instructions, because it prevents whole classes of damaging mistakes the agent would otherwise make confidently.
- Functions as a *living document* — continuously updated with solutions to recurring problems so the agent does not repeat past mistakes, a form of self-training the operator does once and reuses every session. In the harness framing, new rules are added incrementally each time the agent fails.
- Acts as a precondition for hands-off work: the more complete and accurate the file, the further an agent can go without human intervention. As the always-read file each session, it is the structural answer to `[[context-decay]]` — re-grounding an agent whose context window has forgotten earlier instructions.
- Stays small and references out: rather than inlining everything, the core file points to external documents, and an auto-generated `memory.md` can index more granular memory files — keeping the always-loaded core high-signal. The guiding image is a "map, not a 1,000-page manual."

## How It Appears in the Corpus

In the Boris Cherny and Jarred Sumner live coding session, Bun's automated agent ("Robbun") depends on a meticulous "Claude MD" to reproduce issues, build the project, and run tests. The session frames documentation quality as the limiting factor for how much can be automated — see `[[compound-engineering]]` for the practice of iteratively improving it.

The Simon Scrapes memory-systems comparison frames `claude.md` as the foundational (Level 1) memory of Claude Code — rules, brand, and coding styles loaded every session — paired with an auto-generated `memory.md` index into more granular documents, and warns explicitly against overloading it.

The Nate Herk "Every Level of Claude" overview reiterates `claude.md` as the Level-4 project file read at the start of every session — carrying tech stack, naming conventions, and project goals — and stresses dynamically updating it so the agent stops repeating past mistakes, framing the practice explicitly as self-training the model.

The 캐슬 (아는 개발자) harness explainer casts the context file (`claude.md`/`agent.md`) as the first of three harness pillars: the file an agent reads first every session, written as a concise map of core, universal rules (a guideline of ~60 lines) and refined by adding a new rule each time the agent fails — the context-engineering pillar that counters `[[context-decay]]` within a `[[harness-engineering]]` harness.

The 김플립 (LLM 코딩) breakdown of Boris's Claude Code setup casts `Claude.md` as the agent's work manual for onboarding and control — project structure, tech stack, code style, and especially forbidden actions (e.g. no unauthorized edits to migration files) so the agent works the team's way and avoids damaging moves. It adds a concrete budget heuristic: keep the file to its essentials, around 2,500 tokens, so the agent can reference it easily without bloat.

The ByteByteAI "12 Claude Code Features" overview reiterates the file (which it calls `cloud.md`) as project-root memory storing coding preferences and project structure that the agent reads every session to overcome its initial lack of project context, and notes it can be initialized in one step with `/init`.

## Tensions & Tradeoffs

- Maintenance burden: the file must be kept current, and silent staleness degrades agent performance without obvious signals.
- Exhaustiveness vs concision: balancing complete instructions against context budget is the central tension, and over-stuffing the file is the named failure mode `[[context-rot]]` — the corpus offers conflicting rough heuristics (line-count: under ~200 lines, or as tight as ~60; token-count: around 2,500 tokens) and the consistent advice to reference external context, scaling further recall into `[[persistent-agent-memory]]`. The differing units (lines vs tokens) confirm these are rules of thumb, not measured thresholds.
- Positive instructions vs prohibitions: a file rich in build/test know-how can still omit the forbidden-action list that prevents catastrophic edits, so the two kinds of content are distinct and both required; prohibitions in prose are weaker than the mechanical block of `[[permission-tiering]]`, making the two complementary rather than redundant.