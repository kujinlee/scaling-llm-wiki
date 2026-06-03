---
concept: Tool Integration Hierarchy
category: Harness & Context Engineering
summary: Preference ordering for giving agents new capabilities: CLI tools first (60–70% fewer tokens), then APIs, then skills, then MCP only when nothing lighter fits — a context-budget discipline.
aliases: [tool integration hierarchy, CLI-first integration, MCP-last principle, token-efficient tool integration, integration preference order]
related: [token-maxing, per-node-model-routing, harness-engineering, context-rot, model-context-protocol, low-floor-high-ceiling-tooling, robust-tool-design]
sources: [every-level-of-claude-explained-in-21-minutes, 12-claude-code-features-every-engineer-should-know-subagents, agentic-search-for-context-engineering-leonie-monigatti-elas]
---

# Tool Integration Hierarchy

The tool integration hierarchy is a preference ordering for how to give an agent a new capability, ranked by token efficiency: reach for command-line tools first, then API endpoints, then skills, and only fall back to MCP when nothing lighter expresses the task. It reframes integration choice as a token-economy decision — the same underlying work plumbed through a heavier interface silently inflates context cost, so *how* a capability is wired matters as much as *whether* it exists.

## Key Mechanics

- Ordered fallback: CLI tools → API endpoints → skills → MCP, descending by token efficiency, with MCP reserved as the last resort.
- CLI-first is quantified: command-line invocation is cited as consuming roughly 60–70% fewer tokens than the heavier alternatives for equivalent work.
- MCP is positioned as the most capable but most token-expensive option — appropriate when lighter integrations cannot represent the task, not as the default reach.
- Integration economy complements model economy: this trims tokens on the *plumbing*, just as `[[per-node-model-routing]]` trims them on the *model* — both are levers on the same inference budget.

## How It Appears in the Corpus

The Advanced (Level 4) MCP discussion in the Nate Herk overview explicitly orders integration choices — use CLI tools first (60–70% fewer tokens), then API endpoints, then skills, and finally MCP when other options are unsuitable — presenting it as a token-cost discipline inside Claude Code.

The ByteByteAI "12 Claude Code Features" overview supplies the complementary positive case for the heaviest tier: connecting to an MCP server (`[[model-context-protocol]]`) gives the agent access to a large ecosystem of external tools and services (e.g. Figma, Slack), significantly extending its scope — the capability that justifies MCP's place in the ordering even though it is the most token-expensive option.

The Leonie Monigatti (Elastic, "AI Engineer") agentic-search talk reinforces the CLI-first end from the retrieval angle: the **shell tool** (bash/exec) is presented as an extremely versatile, low-token way to give an agent broad capability — searching files with `ls`/`grep`, chaining CLIs, invoking custom search binaries — confirming that a command-line surface is often the most efficient integration, while also showing it is a *high-ceiling* general-purpose tool (`[[low-floor-high-ceiling-tooling]]`) that trades ease-of-use for reach.

## Tensions & Tradeoffs

- In tension with `[[token-maxing]]`'s "spend tokens freely" stance: here token frugality on integration is the goal. The reconciliation is that tokens saved on plumbing can be spent where they actually drive output quality.
- A lighter interface can be more brittle or less expressive than MCP, so choosing CLI to save tokens can cost capability or robustness on complex integrations.
- The two corpus framings of MCP are complementary, not contradictory: this hierarchy ranks it *last by token cost*, while `[[model-context-protocol]]` emphasizes the *breadth of capability* that access buys — the discipline is to reach for it when lighter tiers cannot express the task, not to avoid it.
- **Token rank is not the only axis**: a CLI/shell tool is cheap on tokens yet can be *hard for the agent to use correctly*, so the token ordering must be weighed against the floor-vs-ceiling ordering of `[[low-floor-high-ceiling-tooling]]` and the authoring discipline of `[[robust-tool-design]]` — a tool being light does not make it reliable.
- Bloated tool schemas are themselves a path to `[[context-rot]]`, so the hierarchy is also a context-hygiene move, not only a cost one.
- The 60–70% figure is a rule-of-thumb from a tutorial, not a controlled measurement, and varies with the tool and task.
