# Agentic AI & Claude Code Wiki — Schema & Conventions

This file defines the structure and rules for this knowledge base, built from
YouTube talk/tutorial summaries on agentic AI, Claude Code, and LLM-driven
software development. Every wiki operation (ingest, query, lint) reads this
file first.

**Language:** The wiki is written entirely in English. Source summaries may be
Korean or English — synthesize across both, never transcribe.

## Concept Page Format

Every concept page in `wiki/concepts/` uses this exact structure:

```markdown
---
concept: <Full Concept Name>
category: <EXACTLY one category name from the list below>
summary: <one-line description used verbatim in the index>
aliases: [<alternate name>, <abbreviation>]
related: [<kebab-case-concept-name>, ...]
sources: [<source-filename-stem>, ...]
---

# <Full Concept Name>

<One-paragraph synthesis: what this concept is and why it matters.>

## Key Mechanics

<How it works, technically. Bullet points or prose.>

## How It Appears in the Corpus

<Which source talks/tutorials introduced or expanded this concept, with direct references.>

## Tensions & Tradeoffs

<Contradictions, limitations, open questions, or competing approaches noted across sources.>
```

## Linking Convention

Use `[[concept-name]]` for inline cross-references within page content.
Concept names must match the filename stem exactly (kebab-case, no extension).
Example: "This is the operational core of `[[harness-engineering]]`."

## Index Structure

`wiki/index.md` is **generated deterministically** by `python wiki.py reindex` from each
page's `category:` and `summary:` frontmatter — never hand-edited and never written by the
ingest LLM. Each entry is one line: `- [[concept-name]] — summary`. Set the page's
frontmatter correctly and the index takes care of itself.

Categories (use the name EXACTLY; this is the index order):
1. **LLM Internals & Training** — pre-training, RLHF, mixture-of-experts, tokenization, inference/serving economics
2. **Harness & Context Engineering** — harnesses, context engineering, CLAUDE.md, prompt-as-source-code, context failure modes
3. **Agent Architecture & Patterns** — agentic loop, tool calling, MCP, multi-agent systems, orchestration, subagents
4. **Memory & Knowledge Systems** — LLM/second-brain wikis, RAG, context graphs, agent memory, knowledge bases
5. **Coding Tools & IDEs** — Claude Code, Codex, Gemini CLI, Cursor, Antigravity, terminal/IDE workflows
6. **Workflows & Methodology** — spec-driven development, TDD for agents, plan/research/implement, code review, evals
7. **Skills, Plugins & Automation** — skills, superpowers, plugins, hooks, self-improving loops (Ralph), dark factory
8. **Industry, Strategy & Careers** — AI-native orgs, business/moats, Palantir/ontology, funding, the changing engineer role

Create a category section only when it has at least one concept.

## Log Entry Format

```
YYYY-MM-DD HH:MM | operation | brief detail
```

Example: `2026-06-02 14:30 | ingest | harness-doc: created 4 pages (harness-engineering, context-engineering, claude-md, prompt-as-source-code)`

## Ingest Rules

1. Read all existing concept pages before deciding what to create or update.
2. If a concept page already exists, update it in-place. Do not duplicate content.
3. If a source contradicts an existing claim, add a note under `## Tensions & Tradeoffs` — do not silently overwrite.
4. Use kebab-case for all filenames (e.g., `context-engineering.md`, not `ContextEngineering.md`).
5. Always include an updated `wiki/index.md` in every ingest response.
6. Prefer specific, narrow concept pages over broad ones.
7. Extract durable CONCEPTS (techniques, patterns, architectures, principles), not video-specific trivia, speaker names, or news items.
8. Append (do not replace) the source filename to a page's `sources:` list when a new source expands it.

## Query Rules

1. Answer based on wiki content. Cite concept pages: "Per [[harness-engineering]] and [[context-engineering]]..."
2. If information is missing from the wiki, say so explicitly.
3. If the answer reveals a wiki gap, end with: `Gap: <brief description>`

## Lint Checklist

When running lint, check and report:
1. **Orphan detection**: concepts in `index.md` with no file in `wiki/concepts/`
2. **Reverse orphans**: files in `wiki/concepts/` not listed in `index.md`
3. **Broken cross-references**: `[[name]]` links with no matching concept file
4. **Stale tensions**: Tensions & Tradeoffs sections with unresolved contradictions
5. **Miscategorization**: concepts filed under the wrong index category

Report "OK" for each clean item. End with a one-sentence summary verdict.
