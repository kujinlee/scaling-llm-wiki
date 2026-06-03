# LLM Wiki — Agentic AI & Claude Code Summaries

**Date:** 2026-06-02
**Status:** Approved
**Based on:** Karpathy's LLM Wiki pattern (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
**Sibling implementation:** `../cs146s-the-modern-software-development/` (same pattern, course-week sources)

---

## Overview

Build a concept-first, LLM-maintained wiki over the ~200 YouTube playlist summary
markdown files in this directory. A Python CLI (`wiki.py`) orchestrates three
operations — ingest, query, lint — by calling the `claude` CLI subprocess. The wiki
compounds knowledge over time: each ingest reads prior synthesis before adding new
material, so a later source can update a page an earlier source created.

This is the same system built for CS146S, adapted for a larger, mixed-language
(Korean + English) corpus of talks and tutorials rather than 9 structured course weeks.

---

## Key Differences From the CS146S Wiki

| Aspect | CS146S | This wiki |
|--------|--------|-----------|
| Source count | 9 `wk*.md` | ~200 top-level `*.md` |
| Source language | English | Mixed Korean + English (wiki output: English only) |
| Source key | course week (`weeks:`) | source filename (`sources:`) |
| Source glob | `wk*.md` | `*.md` (top level) |
| Categories | LLM/agent/SRE | 8 categories spanning tools, harness, memory, strategy |
| Ingestion | all 9 | curated top-20 by `overallScore`, rest on demand |

---

## Project Structure

```
agentic-ai-claude-code/
├── wiki/
│   ├── CLAUDE.md           # Schema: page format, linking rules, categories
│   ├── index.md            # Content catalog organized by category
│   ├── log.md              # Append-only history of all operations
│   └── concepts/           # One .md per extracted concept
├── wiki.py                 # Single CLI entrypoint
├── tests/test_wiki.py      # Unit tests (mock the claude subprocess)
├── playlist-index.json     # (existing) video metadata incl. overallScore
└── *.md                    # (existing raw sources — never modified)
```

The `wiki/` directory is entirely LLM-owned. The top-level `*.md` files are immutable raw sources.

---

## CLI Interface

```bash
python wiki.py ingest                 # ingest all top-level *.md sources (auto-reindex every 5)
python wiki.py ingest some-talk.md    # ingest one source (+ final reindex)
python wiki.py reindex                 # rebuild index.md from frontmatter (deterministic, no LLM)
python wiki.py query "How does harness engineering relate to context engineering?"
python wiki.py lint                   # health-check for drift, orphans, broken links
```

---

## Index as Derived State (performance optimization)

Originally (and in the CS146S sibling) every `ingest` call regenerated the full
`index.md` in its JSON envelope — ~1,500 wasted output tokens per call. Since
`ingest` re-reads **all concept files from disk** every call, the concept pages —
not the index — are the source of truth for dedup/update decisions. The index is
only a navigation layer, so it can lag a few sources without harming compounding.

The wiki therefore treats the index as **derived state**:

- Each concept page carries `category:` and `summary:` in its frontmatter. The ingest
  LLM sets these (it is already synthesizing the page, so it knows the category).
- `ingest` emits **concept pages only** (no `index.md` in its envelope).
- `reindex` rebuilds `index.md` by a **deterministic Python projection** over those
  frontmatter fields — group by `category` (in schema order), emit `- [[stem]] — summary`.
  **No LLM call.** Pages with a missing/unknown category land under `## Uncategorized`
  so nothing is silently dropped.
- `ingest` runs `reindex` **after every file** — since the projection is ~0.1s and free,
  there is no reason to batch, and the index stays continuously correct even if a long run
  is interrupted. Reindex is non-fatal (pages are on disk; the index is always rebuildable
  with `python wiki.py reindex`).

Why deterministic rather than an LLM reindex: `claude --print` is an *agent with file
tools*, so "regenerate file X" is unreliable for structured capture — it may edit the file
directly and reply with prose instead of returning the expected JSON (observed in testing,
~400s and a parse failure even though the file ended up correct). A Python projection is
instant (~0.1s), free, reproducible, and has no rate-limit or parse failure modes.

```bash
python wiki.py reindex                   # rebuild index.md from frontmatter (Python, ~0.1s)
python wiki.py ingest                     # bulk ingest, reindex after every file
```

## Operations, Subprocess Protocol, Schema

Identical in structure to the CS146S design: ingest returns a JSON envelope
(`files` / `log_entry` / `summary`) and writes pages + index atomically after a
successful parse; query and lint return plain text. The schema (`wiki/CLAUDE.md`)
defines the concept page format, `[[concept-name]]` linking, the 8 index
categories, log entry format, and the ingest/query/lint rules. The only schema
changes from CS146S are the `sources:` frontmatter (was `weeks:`), the category
taxonomy, and an explicit English-output / cross-language-synthesis rule.

---

## Seeding Strategy

Rather than ingest all ~200 files at once (slow, token-heavy), the wiki is seeded
with the top 20 sources ranked by `overallScore` in `playlist-index.json`. This
produces a coherent, high-value initial wiki. Remaining sources can be ingested
incrementally with `python wiki.py ingest <file>`; the compounding design means
later ingests extend and cross-link the seeded pages.

---

## Out of Scope

- Embeddings or vector search (wiki is small enough for full-context reads)
- A web UI (Obsidian renders the `[[wikilinks]]` natively)
- Automatic git commits after ingest
- Non-markdown sources (PDFs in `pdfs/` are ignored; top-level `*.md` are the sources)
