# scaling-llm-wiki

An **LLM-maintained knowledge wiki** over an ever-growing corpus of raw sources — built on Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern, then re-architected to scale past the point where the brute-force version falls over.

The corpus here is ~200 YouTube-talk summaries (mixed Korean/English) on agentic AI and Claude Code, distilled into ~180 cross-linked concept pages across 8 categories. The interesting part isn't the content — it's the **ingest pipeline** that keeps a coherent, deduplicated wiki affordable as the source count grows into the hundreds and beyond.

## The problem this solves

Karpathy's LLM-Wiki pattern is excellent for small, high-value corpora: every ingest re-inlines the *entire* concept corpus into the prompt, which is exactly what produces a coherent, non-duplicated knowledge base. But that coherence is **O(N²)**:

- **Quadratic token cost** — each of N ingests re-reads the growing corpus. On this corpus, 49 successful ingests burned **~10.1M input tokens** to produce a **~226K-token** wiki — a **~45× amplification**, and rising with N.
- **Context-window ceiling** — the synthesized corpus hit ~226K tokens at 180 pages, past Sonnet's 200K window, forcing the 1M-context Opus model.
- **Quota walls** — back-to-back large Opus calls drained the 5-hour subscription window repeatedly: **65 of 114 ingests failed** in contiguous blocks.

The fix is to **separate "find what's relevant" (cheap) from "synthesize the update" (the expensive LLM call)**.

## The Router-Synthesizer pipeline

`route-ingest` replaces the brute-force read with a bounded two-call pipeline, turning per-ingest cost from *linear in corpus size* into *flat* (bounded by K selected pages):

```
  source.md ──────────────►  ① ROUTE  (Haiku — tiny, ~free)
  wiki/concepts/*.md            in:  source + COMPACT index (one line/page: slug: summary [aliases])
   (frontmatter only) ──────►   out: {"slugs": [...]}   ← the K relevant existing pages
                                       │  K ≤ 25
                               ② LOAD  (Python)
                                  read the K page files; drop hallucinated slugs; cap
                                       │  K full concept pages
                               ③ SYNTHESIZE  (Sonnet — bounded context)
                                  in:  source + full compact index (for awareness) + K full pages
                                  out: {"files": [...changed pages only...], "gaps": [...], "log_entry": "..."}
                                       │
                               ④ WRITE  (Python, under an advisory lock)
                                  path-guard → write only changed pages → record gaps/renames → reindex
```

Why it scales:

| | Brute-force `ingest` | `route-ingest` |
|---|---|---|
| Synthesis context | entire corpus (linear ↑) | K ≤ 25 pages (flat) |
| Model required | Opus 1M | **Sonnet** (200K is plenty) |
| Per-ingest quota | grows with N | flat |
| Recall safety | inherent (sees everything) | index-aware synthesis + gap log + `resolve-gaps` |

**Recall backstop.** A cheap router can miss a relevant page, which would create a duplicate concept. Three mechanisms catch that: (1) synthesis always sees the *full* compact index, so it can flag a relevant-but-not-loaded page as a `gap`; (2) gaps are journaled to `wiki/.gap-log.jsonl`; (3) `resolve-gaps` re-synthesizes those sources with the missed pages forced into context. `lint` reports outstanding gaps and orphans.

No extra API cost: every model call goes through the `claude --print` CLI on a subscription — Haiku for routing, Sonnet for synthesis.

## Usage

Requires the [Claude Code](https://claude.com/claude-code) CLI on your `PATH` and Python 3.10+.

```bash
# Scalable ingest (recommended for large corpora)
python wiki.py route-ingest                    # all raw/*.md sources
python wiki.py route-ingest raw/some-talk.md   # a single source
python wiki.py resolve-gaps                     # repair any router misses logged as gaps

# Original brute-force ingest (kept as a fallback / for small corpora)
python wiki.py ingest

# Maintenance & retrieval
python wiki.py reindex                       # rebuild index.md from page frontmatter (deterministic, no LLM)
python wiki.py query "what is harness engineering?"
python wiki.py lint                          # health-check: drift, orphans, outstanding gaps
```

Useful flags: `route-ingest --router-model/--synth-model`, `ingest --model`.

## Layout

```
wiki.py                      # single-module CLI (ingest, route-ingest, resolve-gaps, reindex, query, lint)
raw/                         # ~200 raw source summaries (the corpus) + playlist-index.json
wiki/
  CLAUDE.md                  # wiki conventions + category order
  concepts/*.md              # ~180 LLM-maintained concept pages (the knowledge base)
  index.md                   # deterministically generated from page frontmatter
  log.md                     # ingest history
  .gap-log.jsonl             # router-miss / rename journal (backstop)
tests/test_wiki.py           # 111 tests
scripts/measure_router_recall.py   # router-recall validation harness (spec §8 gate)
docs/superpowers/
  specs/  …-llm-router-architecture-design.md   # the approved design + roadmap
  plans/  …-llm-router-synthesizer-ingest.md    # the TDD implementation plan
```

## Development

```bash
python -m venv .venv && .venv/bin/pip install pytest
.venv/bin/python -m pytest tests/test_wiki.py -q     # 110 passing
```

The implementation follows TDD; the LLM↔Python contract is "the model returns JSON, Python does all writes," which keeps the pipeline deterministic and testable (tests mock the `claude` call with canned JSON).

## Roadmap

The Router-Synthesizer ingest is subsystem #2 of a larger "second brain" design (see [the spec](docs/superpowers/specs/2026-06-03-llm-router-architecture-design.md)):

1. **Intake / farmers** — per-medium workers (YouTube / PDF / Slack → Markdown) feeding a `raw/` queue
2. **Router-Synthesizer ingest** — *this repo* ✅
3. **Embeddings retrieval layer** — a sublinear pre-filter beneath the router, for when the compact index itself gets large (~thousands of pages)
4. **Lint / consolidation** — periodic dedup, orphan, and contradiction sweeps

Before `route-ingest` becomes the default ingest path, `scripts/measure_router_recall.py` validates router recall against ground truth (ship criteria in spec §8: aggregate ≥ 0.90, per-source floor ≥ 0.50, Korean ≈ English).

---

🤖 Built with [Claude Code](https://claude.com/claude-code).
