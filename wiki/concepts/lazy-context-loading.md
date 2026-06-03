---
concept: Lazy Context Loading
category: Harness & Context Engineering
summary: Loading instructions into an agent's context only when triggered by the task at hand (via resolvers), keeping the active window lean and high-signal instead of always preloading.
aliases: [resolvers, lazy context loading, on-demand context, just-in-time context, context resolvers, resolver triggers, check resolvable]
related: [context-engineering, context-rot, persistent-agent-memory, tool-integration-hierarchy, thin-harness-fat-skills, claude-md]
sources: [stanford-cs153-frontier-systems-the-ai-native-company-how-on]
---

# Lazy Context Loading

Lazy context loading is the technique of loading instructions and reference material into an agent's context *only when they are needed* — triggered by the task at hand — rather than holding the entire corpus in the window at once. Its corpus instance is the "resolver": a mechanism that fires on a condition (for example, loading `changelog.md` only when the agent is about to write to it) and injects just the relevant slice. By keeping the active window small and high-signal, it prevents context-window overflow and improves agent performance — the just-in-time counterpart to always-loaded context like `[[claude-md]]`.

## Key Mechanics

- **Trigger-based injection**: a resolver is bound to a condition; when that condition is met it loads the matching instructions, so context arrives exactly when it is actionable instead of sitting in the window unused.
- **Overflow prevention**: by deferring detail to retrieval, the standing context stays lean — the loading-side answer to `[[context-rot]]`, complementing the trimming-side discipline of keeping `[[claude-md]]` a "map, not a manual."
- **"Check resolvable" compliance**: a verification step confirms a skill's resolver triggers are correctly wired, treated as an audit/compliance check so context routing is not left to chance.
- **The org-chart primitive**: in the company-as-agentic-system framing, the resolver is the *org chart* — it routes the right context to the right skill, just as an org chart routes work to the right role.

## How It Appears in the Corpus

The Garry Tan / Diana Hu Stanford CS153 lecture introduces resolvers as one of the core agentic-workflow primitives (alongside skills and the memory brain) in tools like Gstack and Open Claw: mechanisms to manage context and load instructions only when needed, with the worked example of loading `changelog.md` only when writing to it, a "check resolvable" compliance/audit step in the Skillify process, and the mapping of a resolver to a company's org chart.

## Tensions & Tradeoffs

- **Coverage equals the triggers you wired**: a resolver only loads what its condition anticipates, so an unwired need silently goes unloaded — the same coverage gap noted for `[[lifecycle-hooks]]` and `[[auto-correction-loop]]`.
- **Shifts the burden onto trigger quality**: trading always-available context for on-demand loading does not remove the risk that the agent lacks something it needed; it relocates it to whether retrieval fires correctly — the retrieval-quality bottleneck of `[[persistent-agent-memory]]`.
- **Complementary, not redundant**: it works the same lean-window goal as `[[tool-integration-hierarchy]]`'s token economy and `[[claude-md]]`'s reference-out discipline — three levers on the same finite context budget, attacked from loading, plumbing, and authoring sides respectively.
