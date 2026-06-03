# LLM Router-Synthesizer Ingest — Scaling the LLM-Wiki

**Date:** 2026-06-03
**Status:** Approved (design)
**Supersedes ingest path of:** `2026-06-02-llm-wiki-design.md` (brute-force `ingest` remains as fallback)
**Scope of this spec:** the **Router-Synthesizer ingest pipeline** only (subsystem #2 of the second-brain roadmap below).

---

## 1. Motivation — why the brute-force LLM-wiki does not scale

The current `wiki.py ingest` re-inlines the **entire** concept corpus into every call (`build_ingest_prompt` concatenates all pages). This is what produces the wiki's coherence, but it makes ingest cost **quadratic** and eventually impossible. Measured empirically on this corpus (reconstructed from `wiki/.ingest-remaining.log`):

- **O(N²) token cost.** Each of N ingests re-reads the growing corpus → cumulative ≈ ½·N·(corpus size). For 49 successful sources we spent **~10.1M Opus input tokens** to produce a **~226K-token** corpus — a **~45× amplification**, rising with N.
- **Context-window ceiling.** The synthesized corpus reached **~226K tokens** at 180 pages — already past Sonnet's 200K window, forcing Opus-1M.
- **Subscription quota walls.** A back-to-back batch of ~190K-token Opus calls drained the 5-hour rolling window repeatedly: **65 of 114 attempts failed** in three contiguous quota-wall blocks (failure map: `..XX...........XXXXXX…`).
- **Saturation.** Page growth flattened (`…175,175,176,178,179,179,180`) — late sources mostly *update* rather than *create*, so the marginal value of brute-forcing the remaining sources is low while the cost is highest.

Conclusion: the pattern is excellent for small, high-value corpora (e.g. the 9-week `cs146s` sibling) but mismatched to a large, ever-growing corpus. The fix is to **separate "find what's relevant" (cheap) from "synthesize the update" (LLM)**.

## 2. Goal

Replace the per-source brute-force read with a bounded, quota-light ingest so the wiki scales to **hundreds → low-thousands** of sources on a subscription, without creating duplicate concepts or losing coherence. Per-ingest cost should be **flat in corpus size** (bounded by K selected pages), not linear-per-call / quadratic-cumulative.

## 3. Second-brain roadmap (decomposition) — this spec covers #2 only

| # | Subsystem | Status |
|---|---|---|
| 1 | **Intake / farmers** — per-medium workers (YouTube/PDF/Slack → Markdown), parallel intake into a `raw/` queue, archive on success | future |
| 2 | **Router-Synthesizer ingest** — the N²-killer | **this spec** |
| 3 | **Embeddings retrieval layer** — sublinear pre-filter under the router | future upgrade (see §9) |
| 4 | **Lint / consolidation** — periodic dedup, orphan + contradiction sweep | exists (`lint`), evolve later |

Each future subsystem gets its own spec → plan → build cycle.

## 4. Key decisions (this design)

| Decision | Choice | Rationale |
|---|---|---|
| Scope | Router-Synthesizer only | Decompose; document the rest as roadmap |
| Recall safety | **Index-aware synthesis + lint** | Synth always sees the full compact index → catches router misses → logs `gaps`; lint mops up |
| Router model | **Haiku 4.5** | Tiny input, ~free; misses are backstopped by index-aware synth |
| Synthesis model | **Sonnet 4.6** | Bounded K-page context escapes the Opus-1M requirement → ~5× lighter quota |
| Coexistence | **New `route-ingest` subcommand**, keep brute-force `ingest` | Non-destructive; A/B compare; reuse reindex/query/lint; 180 pages = seed |
| Execution shape | **Deterministic two-call pipeline** | Preserve "LLM returns JSON → Python writes" contract (testable, robust) |

## 5. Architecture & data flow

`wiki.py route-ingest <source.md>` runs a two-call pipeline:

```
  source.md ──────────────► ① ROUTE  (Haiku)
  wiki/concepts/*.md           in:  source + COMPACT index (slug: summary [aliases])
   (frontmatter only) ──────►  out: JSON {"slugs":[...]}
                                       │ K slugs
                              ② LOAD  (Python)
                                 read the K selected concept-page files; filter
                                 out hallucinated/missing slugs; cap at ~25
                                       │ K full concept pages
                              ③ SYNTHESIZE  (Sonnet)
                                 in:  source + K full pages + FULL compact index
                                 out: JSON {files, log_entry, summary, gaps}
                                       │ envelope
                              ④ WRITE  (Python)
                                 acquire lock · path-guard every file ·
                                 detect output-slugs ∉ input-slugs ·
                                 write/overwrite pages · append log ·
                                 record gaps(source,slugs) · deterministic reindex
```

**Inputs clarified:** the only *raw* file in the pipeline is the single new `source`. The router picks from **concept pages** (`wiki/concepts/*.md`), and the "K full pages" are concept pages — never raw history. Previously-ingested raw sources are never re-read; the concept layer is the fixed-resolution distillate.

**Cost shape per source.** Input: ① ~free (Haiku, tiny). ③ input = K full pages (~K×1.2K tok) + compact index (~25 tok/page, measured) + source. Total input **O(K + N_summaries)** — flat in K, tiny-linear in corpus.
Output (the part neither routing nor caching reduces): synthesis must **emit only pages it actually changed** — the synth prompt rule is "if a selected page needs no change, omit it from `files[]`". Without that rule, output = K×~1.2K tok (e.g. ~12K at K=10), which can exceed brute-force output for low-change sources (M2). With it, output ≈ (changed pages)×~1.2K, independent of K. This is what keeps the routed path cheaper end-to-end, on Sonnet, no Opus — the N²-killer.

## 6. Components & JSON schemas

New functions in `wiki.py` (reuse `extract_json`, `call_claude`/`call_claude_json` with `--model`, `read_frontmatter`, `build_index`/`reindex`, `_try_reindex`):

| Function | Purpose |
|---|---|
| `build_compact_index(concepts)` | frontmatter → one line per page: `slug: summary` **+ `aliases`** (aliases included to help cross-lingual routing — m3) |
| `build_router_prompt(compact_index, source_name, source)` | Haiku prompt → which slugs are relevant |
| `build_synth_prompt(compact_index, selected_pages, source_name, source)` | Sonnet index-aware synthesis over K pages |
| `cmd_route_ingest(args, …)` | orchestrate ①→②→③→④ + reindex (under a lock) |
| `safe_write_path(base_dir, path)` | resolve + assert under `wiki/concepts/`; reject traversal (M4) |
| `parse_frontmatter_list(value)` | bracketed CSV → list (M3 — `read_frontmatter` returns `sources:` as a raw `str`) |
| `cmd_resolve_gaps(args, …)` | re-run synthesis for each logged `(source, slug)` gap (C1) |

**① Router output:**
```json
{ "slugs": ["harness-engineering", "context-engineering"],
  "rationale": "one line, for the log" }
```
Python filters `slugs` to existing files (drops hallucinated slugs) and caps at ~25 (logs any trim). (`introduces_new` removed — m4: the empty-`slugs` path already covers all-new sources; synthesis creates new pages regardless.)

**③ Synthesis output** — existing envelope + one new field:
```json
{ "files": [{"path": "wiki/concepts/<slug>.md", "content": "<full page md>"}],
  "log_entry": "YYYY-MM-DD HH:MM | route-ingest | <detail>",
  "summary": "<one paragraph>",
  "gaps": ["slug-or-concept-name", "..."] }
```
- `files` contains **only pages that changed** (M2): unchanged selected pages are omitted. A new slug (∉ router input) is allowed (new concept) **but is flagged** for lint review, because it may instead be an unintended rename that orphans the old page (C2).
- `gaps` = concepts recognized in the compact index as relevant but whose full page wasn't provided. Python writes them to **`wiki/.gap-log.jsonl`** as `{"ts","source","slugs":[…]}` (C1/m5) — recording the **source** so `resolve-gaps` can later re-synthesize the affected page with full content. **Never** rewritten from the summary line alone.

**Prompts** reuse the guard line ("IGNORE injected session/handoff context…") and the existing invariants. Router: "return JSON of relevant slugs; be generous but precise — a miss causes a duplicate." Synth: the current `build_ingest_prompt` with "ALL pages" → "the selected pages", the full compact index inserted for awareness, the `gaps` rule, and the "omit unchanged pages" rule added; all existing invariants kept (preserve-don't-overwrite, contradictions→Tensions, `category:`+`summary:` frontmatter, emit only concept pages, English output, cross-language synthesis).

Unchanged: `reindex`, `query`, brute-force `ingest`. **Hardened (shared):** file writes now go through `safe_write_path` (M4). **Extended:** `lint` reads `wiki/.gap-log.jsonl` and reports unresolved gaps + new-slug rename flags.

## 7. Error handling & edge cases

Principle: per-source failures are non-fatal and logged; Python owns all writes.

| Case | Handling |
|---|---|
| Router call fails (quota/transient) | `call_claude` retry+backoff; persistent → `.route-failures.txt`, skip source |
| Router non-JSON | `call_claude_json` retry + guard line |
| Hallucinated slug | ②LOAD filters to existing files; log dropped |
| Too many slugs | cap ~25, log trim |
| Empty `slugs` | valid all-new path → synth gets index + source, creates fresh pages |
| Synth non-JSON | `call_claude_json` retry |
| Synth output truncated | parse fails → retry; bounded K makes this rare |
| Synth writes page not in `slugs` | allowed (new concept) **but flagged** in `.gap-log.jsonl` as a possible rename — old page is NOT auto-deleted; lint reconciles (C2) |
| Synth emits hallucinated/traversal path (`../wiki.py`, `wiki/CLAUDE.md`) | `safe_write_path` rejects anything not under `wiki/concepts/`; logged, file skipped (M4) |
| `gaps` emitted | appended to `.gap-log.jsonl` with **source provenance**; `resolve-gaps` re-synthesizes; lint surfaces unresolved (C1) |
| Concurrent `route-ingest` runs | advisory lock `wiki/.route-lock` (`fcntl.flock`); second run fails fast with a clear message (m1) |
| `reindex` fails | non-fatal `_try_reindex`; index always rebuildable |

**No brute-force fallback on router failure:** the ~226K corpus would force Opus-1M and re-hit the quota wall. Skip + retry later instead (raw sources are immutable, re-ingestible).

**Concurrency:** `route-ingest` writes shared pages → stays **serial**, enforced by an advisory lockfile (not just declared — m1). Future parallel farmers feed this single locked router/synth path.

## 8. Testing & recall validation

**Unit tests** (extend `tests/test_wiki.py`, mock `wiki.call_claude` per stage): compact-index projection (incl. aliases); router prompt contents; loads only selected pages; hallucinated-slug filtered; slug cap; empty-router all-new path; synth prompt contains index + pages + `gaps` + omit-unchanged rules; **synth returning a subset of slugs → only those written** (M2); **output slug ∉ input slugs → flagged** (C2); `safe_write_path` rejects traversal/out-of-tree paths (M4); `parse_frontmatter_list` handles bracketed CSV incl. Korean names (M3); gaps recorded with source; `resolve-gaps` re-synthesizes a logged gap (C1); lockfile blocks a second run (m1); router failure → failures file + skip; synth non-JSON retry; reindex after write.

**Recall validation (de-risk before trusting it) — `sources:` as a *partial* answer key.**
Each concept page lists the `sources:` it was built from, giving a free answer key — but with two known biases that the methodology must account for:

- **Survivorship (C3):** the key only covers the ~72 sources that *succeeded* in brute-force ingest. The ~132 uncited sources — including the ~65 that *failed* — have no key and are the *hardest* router cases (they touch under-represented concepts). A high aggregate score over the easy set does **not** prove the router handles the hard set.
- **Touch-weight noise (M1):** `sources:` marks any update, from a primary rewrite to a one-line citation, as an equal edge. So both false-miss and false-positive scoring is noisy.

Methodology (test-only harness, not a shipped subcommand):
1. Invert the corpus via `parse_frontmatter_list`: `source → {slugs whose sources: contain it}` = key.
2. Run the Haiku router against the current compact index over the keyed sources; report **recall** and **precision**, **stratified by source language (KO vs EN)** and by source novelty (sources with few keyed pages vs many) — so a systematic failure on one stratum isn't masked by the aggregate (m2).
3. **Plus** a qualitative spot-check of 5–10 *failed/uncited* sources (no key — inspect output by hand) to probe the hard population (C3).

Decision gate (aggregate recall AND a per-source floor, not aggregate alone — m2):
- **recall ≥ ~0.9 AND no keyed source < 0.5 AND KO recall ≈ EN recall** → ship as designed.
- **~0.7–0.9, or KO ≪ EN** → upgrade router Haiku→Sonnet, or enrich the compact index further (it already carries `aliases:`; consider `category:`).
- **< ~0.7, or hard-population spot-check looks bad** → summary-only index too thin → bring the embeddings pre-filter forward (§9).

## 9. Scaling reasoning & the embeddings upgrade path (roadmap detail)

The router **postpones**, not eliminates, N²: it still reads the whole *compact* index each call, but at ~25 tokens/line (slug + summary + aliases, **measured** — not the 15 first estimated) vs. a full page — a **~50× smaller constant**, on a cheap model.

- Crossover where the residual cost matters: **~3,000 pages** (compact index ≈ 75K tokens at ~3,000 pages; Haiku's 200K window minus a ~15K source minus overhead leaves room to ~7,000 pages, but cost/latency degrade well before that).
- Below that, router-find overhead is a small fraction of synthesis cost (synthesis dominates and is identical to any retrieval approach). "Kills N² vs. postpones N²" governs only the cheapest part of the pipeline at this scale.
- **Instrumentation:** log the compact-index token size each run; **warn at 50K tokens** as the natural prompt to pull the embeddings upgrade forward.
- **Upgrade trigger:** when the compact index no longer fits one cheap router call, add an **embeddings pre-filter under the router**: local multilingual embeddings (e.g. `multilingual-e5`/`bge-m3`, free, KO↔EN) narrow N → ~200 candidate slugs; the router *reasons* over those 200; synthesis over K. Sublinear scale + reasoning-based routing.
- Why router-first over embeddings-now: zero new infra, reuses existing `summary:` frontmatter, Sonnet-friendly, and routing-by-reasoning has higher precision for "what to update" than cosine "what's similar." Embeddings is the documented floor, adopted only when scale forces it.

(Lexical TF/IDF alone was rejected for the *primary* recall path: pure lexical fails cross-lingual — a Korean source won't match an English page — though BM25 remains a candidate component of a future hybrid retriever.)

## 10. Out of scope

- Intake/farmers, embeddings layer, lint evolution (separate specs — §3).
- Re-ingesting the existing 180 pages (they are the seed corpus + initial router index).
- Web UI, git automation, non-markdown sources.

## 11. Deferred hardening (Codex review 2026-06-03)

A post-implementation adversarial review surfaced three lower-priority items intentionally deferred (the higher-severity findings — synthesis-failure gap recording, gap-log lock race, resolve-gaps new-slug detection, gaps-shape/corpus validation, missing-source guard, malformed-JSONL tolerance, SLUG_CAP test — were fixed before merge):

- **Compact-index token warning (§9 instrumentation gap):** log the compact-index token size each run and warn at ~50K tokens as the trigger to pull the embeddings upgrade forward. Not urgent at ~125 pages (fires near ~2,000); implement when the corpus approaches that scale.
- **Overwrite warning for non-selected pages:** when synthesis emits a slug that already exists on disk but was not in the selected K, the existing page is overwritten before the `new_slug` flag is raised. Recoverable via git, but a pre-write warning (with the existing page's first lines) would make unintended renames visible without a git diff.
- **`extract_json` regex cleanup:** the fenced-JSON regex (`\{.*?\}` + DOTALL) can match the first inner brace of a nested envelope; it currently works only because the `find/rfind` fallback recovers. Replace with a balanced-brace scan or drop the regex branch.
