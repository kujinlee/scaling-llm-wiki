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
WIKI_FILE_SENTINEL = "===WIKI-FILE: {path}==="          # prompt rendering
WIKI_FILE_SENTINEL_RE = r"(?m)^===WIKI-FILE: (.+?)===[ \t]*$"   # parser split
```

## 5. Parser — `parse_synthesis_response(text) -> dict`

Replaces `extract_json` for the two ingest paths.

```
1. parts = re.split(WIKI_FILE_SENTINEL_RE, text)
       → [header, path1, body1, path2, body2, ...]
2. if len(parts) == 1 (no sentinel):
       try:  meta = extract_json(text)
             if meta has a "files" key → return adapted old-style envelope (FALLBACK, backward compat)
             else → return {**meta, "files": []}        # legitimate "changed nothing"
       except ValueError → re-raise (total garbage; triggers retry upstream)
3. header = parts[0]
   try:  meta = extract_json(header)
   except ValueError:  meta = {}                          # blocks still valid; metadata defaults
4. files = []
   for (path, body) in pairs(parts[1:]):
       path = path.strip()
       content = strip exactly ONE leading and ONE trailing "\n" from body
       if content == "":  warn (empty page) but still include
       files.append({"path": path, "content": content})
5. return {
       "files": files,
       "log_entry": meta.get("log_entry"),
       "summary":   meta.get("summary"),
       "gaps":      meta.get("gaps") or [],
   }
```

Newline trimming removes the single `\n` after the sentinel line and the single `\n` before the next sentinel — **not** `strip("\n")`, which would eat intentional leading/trailing blank lines in the body.

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
- Each changed page follows as: a line `===WIKI-FILE: <path>===` on its own, then the page's raw markdown.
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
| `cmd_ingest` | Same swap. **Plus**: change `response["log_entry"]`/`["summary"]` hard-keys to `.get("log_entry") or <generated default>` and `.get("summary", "(no summary)")`, matching `cmd_route_ingest` (also removes a latent KeyError present today). |
| `write_wiki_files`, `safe_write_path`, `build_router_prompt`, `call_claude_json` | Unchanged. |

## 9. Error handling

| Failure | Handling |
|---|---|
| Neither sentinel nor JSON parseable (total garbage) | `parse_synthesis_response` raises `ValueError` → `call_claude_synthesis` retries → after retries the caller's existing `except` logs failure + records router slugs as a gap (route-ingest) / writes to the failures file |
| Header JSON malformed, content blocks present | `meta = {}`; files written; `log_entry`/`summary` fall back to caller default |
| Sentinel `path` escapes the wiki tree | Rejected per-file by the existing `safe_write_path` check in callers (unchanged) |
| Empty content between two sentinels | Page written empty + stderr warning (lint-detectable; not a crash) |
| `===WIKI-FILE:` as a full line inside content | Accepted residual risk — documented; prompt forbids it; near-impossible in wiki prose |

## 10. Testing (TDD)

**Parser unit tests — `parse_synthesis_response`:**
1. Header + 2 blocks → 2 files with exact raw content; `log_entry`/`summary`/`gaps` from header.
2. **Regression case:** content containing `"quotes"`, code fences, and `{json-like}` text → preserved verbatim (would have broken the old JSON contract).
3. Header-only, no blocks → `files: []`.
4. No sentinel + valid old-style JSON envelope → fallback returns its `files`.
5. Malformed header JSON + blocks present → files parsed, `meta` defaults.
6. Non-full-line `===WIKI-FILE:` substring in content → not split.
7. `gaps` absent in header → `gaps: []`.
8. Newline trimming exact, including content with internal blank lines (not over-trimmed).
9. Path whitespace stripped.
10. Total garbage (no sentinel, no JSON) → raises `ValueError`.

**Integration tests:**
11. `call_claude_synthesis` retries on `ValueError` then succeeds (`side_effect=[garbage, valid]`).
12. `cmd_route_ingest` / `cmd_resolve_gaps` / `cmd_ingest` end-to-end with **new-format** mocked responses → pages written, gaps recorded, reindex called.
13. Prompt builders: assert `WIKI_FILE_SENTINEL` literal and "no escaping / no fences" instruction appear; `gaps` present for synth, absent for brute-force ingest.

**Existing tests:** current route-ingest/resolve-gaps/ingest tests mock `call_claude` returning JSON strings — these now exercise the **fallback path** and must stay green (proves the change is non-breaking). New-format tests (12) are added alongside.

## 11. Out of scope

- Router prompt/format (unaffected).
- The recall/floor question (separate — spec §8 of the router design).
- The two pre-existing corrupted placeholder pages (`outcome-first-prompting.md`, `skill-by-demonstration.md`) — a data-repair task, tracked separately.
- Streaming/unbuffered CLI output, embeddings, lint evolution.
