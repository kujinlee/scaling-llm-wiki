# Synthesis Output Contract — Sentinel-Delimited Page Bodies

**Date:** 2026-06-03
**Status:** Approved (design)
**Scope:** the ingest/synthesis **response format and its parser** only. Replaces the JSON-string `content` payload for `route-ingest` synthesis and brute-force `ingest`. The router path is unaffected.

---

## 1. Motivation

Both `build_synth_prompt` (route-ingest) and `build_ingest_prompt` (brute-force) ask the model to return a JSON object whose `files[].content` is the **full page markdown embedded as a JSON string value**. Reliably escaping every `"`, newline, and control character across a multi-KB markdown body is something the model does only *probabilistically*.

Observed live (2026-06-03): `resolve-gaps` on the Korean source `live-코덱스로-바이브-코딩하기-feat-하네스-엔지니어링.md` failed all 3 synthesis attempts with `Expecting ',' delimiter: line 1 column 1167` — an **unescaped nested quote** (`("boss")`) inside a `content` field. The same source's earlier `route-ingest` call happened to escape correctly and parsed fine. The failure is non-deterministic and content-dependent: any synthesized body containing quotes/backticks/braces can break the single-line JSON envelope, and retries are just independent dice rolls.

This is a **contract-design problem, not a parser bug.** The fix is to stop carrying large free text as JSON string values.

## 2. Goal

Eliminate the JSON-escaping failure class for synthesized page bodies, on both ingest paths, without changing the "LLM returns structured output → Python writes files" contract that keeps the pipeline deterministic and testable. No extra cost (subscription CLI only; no format that wastes tokens).

## 3. Key decisions

| Decision | Choice | Rationale |
|---|---|---|
| Format | **JSON metadata header + sentinel-delimited raw content blocks** (Approach A) | Keeps JSON for what it is good at (small structured metadata, esp. the `gaps` array); removes it from what it is bad at (multi-KB free text = 100% of failures) |
| Path source of truth | **The sentinel line**, not the header | No header/blocks reconciliation; header carries only `log_entry`/`summary`/`gaps` |
| Scope | **Both** route-ingest synthesis and brute-force ingest, via a shared format-instruction helper | Same envelope, same bug; a shared source prevents prompt/parser drift |
| Router | **Unchanged** | Its JSON (`{"slugs":[...]}`) is tiny with no embedded bodies — no escaping risk |
| Backward compatibility | **Parser falls back to `extract_json`** when no sentinel is present | A reply that still comes back as pure JSON degrades gracefully; the change is strictly additive (worst case ≥ today) |
| Return shape | **Identical dict** to today: `{"files":[{"path","content"}...],"log_entry","summary","gaps"}` | `write_wiki_files`, `safe_write_path`, and callers are unchanged |
| Sentinel recognition | **Only a concept-path-shaped sentinel splits** — the captured path must match `wiki/concepts/<kebab>.md` | Prose discussing delimiter formats (this corpus is *about* LLM I/O) won't accidentally split; an injected/spoofed path is bounded to the concepts tree |
| Line endings | **Normalize `\r\n`/`\r` → `\n` at parser entry** | A CRLF response otherwise matches the line-anchored regex zero times and loses 100% of pages deterministically |
| Malformed/absent header with content blocks present | **Raise → retry** (never silently default `meta={}`) | The header carries `gaps`, the recall backstop; silently dropping it = a permanently missed page. A loud retry is correct |

## 4. Wire format

The response is a single-line JSON metadata object, then one block per changed page:

```
{"log_entry": "2026-06-03 18:35 | route-ingest | updated 2 pages", "summary": "<one paragraph>", "gaps": ["session-context-forking"]}
===WIKI-FILE: wiki/concepts/harness-engineering.md===
---
concept: Harness Engineering
category: Harness & Context Engineering
summary: ...
---
# Harness Engineering

Body with "quotes", real newlines, `backticks`, and {braces} — all raw, no escaping.
===WIKI-FILE: wiki/concepts/context-compaction.md===
---
...second page, raw markdown...
```

- The header JSON carries `log_entry`, `summary`, and (synthesis only) `gaps`. It lists **no** file contents and **no** paths.
- Each changed page follows as a sentinel line `===WIKI-FILE: <path>===` on its own line, then the page's raw markdown.
- Content is **verbatim**: no escaping, no ` ``` ` fences.
- A response that changed no pages is just the JSON header line (zero content blocks).

**Sentinel constant** (shared by prompt and parser):

```python
WIKI_FILE_SENTINEL = "===WIKI-FILE: {path}==="          # prompt rendering (one space each side)

# Parser split. Notes:
#  - applied AFTER \r\n/\r → \n normalization (see §5 step 0)
#  - tolerates leading indentation and flexible spacing the model might add
#  - the captured group ONLY matches a concept-page path, so prose lines like
#    "===WIKI-FILE: foo===" do NOT split (concept-path-shape guard)
WIKI_FILE_SENTINEL_RE = r"(?m)^[ \t]*===WIKI-FILE:[ \t]*(wiki/concepts/[a-z0-9-]+\.md)[ \t]*===[ \t]*$"
```

A line is treated as a delimiter **only** if its captured path matches `wiki/concepts/<kebab>.md` — the only shape synthesis is permitted to emit (§7 rules). Any other `===WIKI-FILE: ...===`-looking line (e.g. quoted in prose) is left as ordinary content.

## 5. Parser — `parse_synthesis_response(text) -> dict`

Replaces `extract_json` for the two ingest paths.

Helper that keeps metadata shaping in one place:

```
def _meta_fields(meta):
    return {"log_entry": meta.get("log_entry"),
            "summary":   meta.get("summary"),
            "gaps":      meta.get("gaps") or []}
```

```
0. text = text.replace("\r\n", "\n").replace("\r", "\n")     # CRLF/CR normalization (C1)
1. parts = re.split(WIKI_FILE_SENTINEL_RE, text)
       → [header, path1, body1, path2, body2, ...]  (only concept-path-shaped sentinels split)
2. if len(parts) == 1 (no delimiter matched):
       meta = extract_json(text)        # raises ValueError on total garbage → upstream retry
       if "files" in meta:
           return {"files": meta["files"], **_meta_fields(meta)}   # FALLBACK: old-style envelope
       return {"files": [], **_meta_fields(meta)}                  # legitimate "changed nothing"
3. header = parts[0].strip()
   if header == "":
       raise ValueError("content blocks present but no metadata header")   # H1 → retry, never silent
   meta = extract_json(header)          # malformed header → ValueError propagates → retry (H1)
4. files = []
   for (path, body) in pairs(parts[1:]):
       content = body
       if content.startswith("\n"): content = content[1:]    # remove ONE leading \n if present
       if content.endswith("\n"):   content = content[:-1]   # remove ONE trailing \n if present
       if content == "":  print stderr warning (empty page — lint-detectable) but still include
       files.append({"path": path.strip(), "content": content})
5. return {"files": files, **_meta_fields(meta)}
```

**Exact fallback adapter (step 2 — C2):** when `meta` has a `files` key, return precisely `{"files": meta["files"], "log_entry": meta.get("log_entry"), "summary": meta.get("summary"), "gaps": meta.get("gaps") or []}` — passing `files`/`log_entry`/`summary` through **verbatim** and defaulting only an absent `gaps` to `[]`. This exactness is what makes §10's "existing tests stay green" claim true (the old tests' JSON-string mocks round-trip to the identical dict).

**Newline trimming (M4):** two **independent** conditionals — remove one leading `\n` *if present*, one trailing `\n` *if present*. NOT `strip("\n")` (eats intentional blank lines) and NOT `body[1:-1]` (corrupts bodies not bounded by newlines).

**Malformed/absent header (H1):** if delimiters matched but the header is empty or unparseable, the parser **raises `ValueError`** so `call_claude_synthesis` retries — it never silently sets `meta={}` and drops `gaps`. A header that legitimately omits `gaps` (valid JSON, no gaps) is fine → `gaps: []`.

## 6. Retry wrapper — `call_claude_synthesis(prompt, model=None, retries=CLAUDE_RETRIES) -> dict`

Mirrors `call_claude_json` but uses `parse_synthesis_response`:

```
for attempt in range(retries):
    try:    return parse_synthesis_response(call_claude(prompt, model=model))
    except ValueError:  log "response not parseable; retry N/..."; sleep; continue
raise last_exc
```

`call_claude_json` remains for the router. The new format rarely fails to parse, so retries will seldom trigger.

## 7. Prompt changes

**`OUTPUT_FORMAT_INSTRUCTIONS(include_gaps: bool) -> str`** — shared helper rendering the §4 format (synth passes `True`, brute-force ingest `False`). References `WIKI_FILE_SENTINEL` so prompt and parser cannot diverge. Body:

```
Respond in EXACTLY this format — a single-line JSON metadata object, then one
block per page you changed. Do NOT put page content inside the JSON.

{"log_entry": "<YYYY-MM-DD HH:MM | <kind> | summary>", "summary": "<one paragraph>"[, "gaps": ["<slug>", ...]]}
===WIKI-FILE: wiki/concepts/<kebab-case-name>.md===
<full raw page markdown — real newlines, quotes, backticks; NO escaping, NO code fences>
===WIKI-FILE: wiki/concepts/<another>.md===
<full raw page markdown>

Format rules:
- The FIRST line is the JSON metadata object and nothing else. It lists NO file contents and NO paths.
- Each changed page follows as: a line `===WIKI-FILE: <path>===` starting at column 0 (NO indentation), on its own line, then the page's raw markdown.
- The <path> is ALWAYS `wiki/concepts/<kebab-case-name>.md` — the parser ignores any sentinel whose path is not this shape.
- Write page content verbatim — do NOT escape characters and do NOT wrap it in code fences.
- NEVER write a line of the form `===WIKI-FILE: ...===` inside page content.
- If you changed no pages, emit only the JSON metadata line.
```

- **`build_synth_prompt`**: replace its `Respond with ONLY a JSON object {...files...gaps...}` block with `OUTPUT_FORMAT_INSTRUCTIONS(include_gaps=True)`. All **content** rules (kebab-case, English synthesis, update-in-place, `category:`/`summary:` frontmatter, "emit ONLY changed pages / OMIT unchanged", the `gaps` rule, "do not recreate from a summary line", "new page allowed for a genuinely new slug") are unchanged.
- **`build_ingest_prompt`**: same swap with `include_gaps=False`. Content rules unchanged.
- Both preambles: the clause "your entire response MUST be the single JSON object requested" becomes "your entire response MUST be ONLY the metadata-plus-files format defined below — no preamble, no prose."
- **`build_router_prompt`**: unchanged.

## 8. Integration (call sites)

| Site | Change |
|---|---|
| `cmd_route_ingest` | `call_claude_json(build_synth_prompt(...))` → `call_claude_synthesis(...)`. Already uses `resp.get(...)` — no other change. |
| `cmd_resolve_gaps` | Same swap. |
| `cmd_ingest` | Same swap, **plus three fixes** (see below). |
| `write_wiki_files`, `safe_write_path`, `build_router_prompt`, `call_claude_json` | Unchanged. |

**`cmd_ingest` fixes (M2, M3):**
1. Replace the hard keys `response["log_entry"]`/`["summary"]`/the `print(response["summary"])` with `.get(...)` + defaults, matching `cmd_route_ingest` (removes a latent KeyError; `files` is always present from the parser so `["files"]` is safe but should read via the validated-files loop below).
2. **Add the per-file `safe_write_path` guard** that `cmd_route_ingest`/`cmd_resolve_gaps` already use but `cmd_ingest` currently lacks entirely — validate each `f["path"]` under `wiki/concepts` before `write_wiki_files`, rejecting out-of-tree paths. The new raw-content format makes the pre-existing missing-guard reachable, so it is fixed in scope.
3. A zero-file response (now possible) gets a meaningful default log/summary, e.g. `"<ts> | ingest | <source>: no changes"`, not a bare `(no summary)`.

## 9. Error handling

| Failure | Handling |
|---|---|
| Neither sentinel nor JSON parseable (total garbage) | `parse_synthesis_response` raises `ValueError` → `call_claude_synthesis` retries → after retries the caller's existing `except` logs failure + records router slugs as a gap (route-ingest) / writes to the failures file |
| **Header JSON malformed or absent, content blocks present** | **Raises `ValueError` → retry** (H1). Never silently `meta={}`, because that would drop `gaps` (the recall backstop) and lose a page permanently |
| CRLF / CR line endings | Normalized to `\n` at parser entry (§5 step 0) before the regex runs — otherwise the line-anchored regex matches zero times and loses all pages (C1) |
| Sentinel `path` escapes the wiki tree | Rejected per-file by `safe_write_path` in **all three** callers (now including `cmd_ingest`, §8) |
| `===WIKI-FILE: <path>===` line inside content | Only splits if `<path>` is concept-path-shaped (§4 guard), so a prose mention of the format does not split. A body legitimately containing a real `wiki/concepts/x.md`-shaped sentinel line remains a residual risk (rare); the prompt forbids emitting one |
| **Injection / spoofed path** (a source doc instructs the model to emit a sentinel targeting an arbitrary page) | **Pre-existing exposure** — the path was model-controlled under the old JSON format too, so not a regression. Bounded by `safe_write_path` (stays under `wiki/concepts`) and the path-shape guard. `cmd_route_ingest`/`resolve-gaps` already log any write to a non-selected slug as a `new_slug` record for human review. Documented, not silently trusted |
| Empty content between two sentinels | Page written empty + stderr warning (lint-detectable; not a crash) |

## 10. Testing (TDD)

**Parser unit tests — `parse_synthesis_response`:**
1. Header + 2 blocks → 2 files with exact raw content; `log_entry`/`summary`/`gaps` from header.
2. **Regression case:** content containing `"quotes"`, code fences, and `{json-like}` text → preserved verbatim (would have broken the old JSON contract).
3. Header-only, no blocks → `files: []`.
4. No sentinel + valid old-style JSON envelope → fallback returns the **exact** adapter dict (assert `files`/`log_entry`/`summary` verbatim, `gaps` defaulted) — C2.
5. **CRLF input** (`\r\n` line endings) → parses identically to `\n` (C1 regression).
6. **Content blocks present but header empty/malformed** → raises `ValueError` (H1), NOT a silent `meta={}`.
7. **Collision guard:** content containing a line `===WIKI-FILE: not a path===` (non-concept-shape) → NOT split (stays in body); and a line `===WIKI-FILE: wiki/concepts/x.md===` *inside prose* would split — assert the shape guard only splits concept-path-shaped lines.
8. `gaps` absent in a valid header → `gaps: []` (distinguished from H1's malformed-header raise).
9. Newline trimming: independent single leading/trailing `\n` removal; body with internal blank lines not over-trimmed; final block without trailing `\n` intact.
10. Indented / extra-spaced sentinel (`  ===WIKI-FILE:  wiki/concepts/x.md  ===`) still recognized (L2/L3 tolerance).
11. Total garbage (no sentinel, no JSON) → raises `ValueError`.

**Integration tests:**
12. `call_claude_synthesis` retries on `ValueError` then succeeds (`side_effect=[garbage, valid]`).
13. `cmd_route_ingest` / `cmd_resolve_gaps` / `cmd_ingest` end-to-end with **new-format** mocked responses → pages written, gaps recorded, reindex called.
14. `cmd_ingest` rejects an out-of-tree sentinel path via the newly-added `safe_write_path` guard (M2).
15. Prompt builders: assert `WIKI_FILE_SENTINEL` literal, the "column 0 / no escaping / no fences" rules, and the concept-path-shape statement appear; `gaps` present for synth, absent for brute-force ingest.

**Existing tests:** current route-ingest/resolve-gaps/ingest tests mock `call_claude` returning JSON strings. These now exercise the parser's **fallback path** and stay green **contingent on the exact C2 adapter** (test 4) — in particular the resolve-gaps/ingest mocks that omit `gaps` rely on the adapter defaulting it to `[]` while passing `log_entry`/`summary` through verbatim. New-format tests (13) are added alongside to cover the primary path.

## 11. Out of scope

- Router prompt/format (unaffected).
- The recall/floor question (separate — spec §8 of the router design).
- The two pre-existing corrupted placeholder pages (`outcome-first-prompting.md`, `skill-by-demonstration.md`) — a data-repair task, tracked separately.
- Streaming/unbuffered CLI output, embeddings, lint evolution.
