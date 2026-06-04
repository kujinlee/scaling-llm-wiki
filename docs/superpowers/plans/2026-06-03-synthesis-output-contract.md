# Synthesis Output Contract Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the JSON-string `content` payload in synthesis/ingest responses with a JSON metadata header + raw `===WIKI-FILE:` sentinel-delimited content blocks, eliminating the non-deterministic quote/newline-escaping parse failures.

**Architecture:** A new `parse_synthesis_response` parses the sentinel format (falling back to the existing `extract_json` for plain-JSON replies) and a `call_claude_synthesis` wrapper retries on parse failure. A shared `output_format_instructions` helper rewrites the format section of both `build_synth_prompt` and `build_ingest_prompt`. The three ingest callers swap `call_claude_json` → `call_claude_synthesis`; the router path is untouched. All changes are in the single module `wiki.py`.

**Tech Stack:** Python 3.10+ stdlib (`re`, `json`), pytest in `.venv`. TDD throughout.

**Reference:** `docs/superpowers/specs/2026-06-03-synthesis-output-contract-design.md`

**Test command:** `.venv/bin/python -m pytest tests/test_wiki.py -q` (baseline: 110 passing). Commit author flags for every commit: `git -c user.name="Kujin Lee" -c user.email="kujinlee@gmail.com" commit ...`

---

## Task 1: Sentinel constants

**Files:**
- Modify: `wiki.py` (constants block, after `RAW_DIR_NAME` ~line 47)
- Test: `tests/test_wiki.py`

- [ ] **Step 1: Write the failing test**

Add near the other constant/helper tests in `tests/test_wiki.py`:

```python
class TestSentinelConstants:
    def test_sentinel_renders_path(self):
        assert wiki.WIKI_FILE_SENTINEL.format(path="wiki/concepts/rag.md") == \
            "===WIKI-FILE: wiki/concepts/rag.md==="

    def test_sentinel_regex_matches_concept_path_only(self):
        text = "===WIKI-FILE: wiki/concepts/rag.md==="
        m = wiki.WIKI_FILE_SENTINEL_RE.search(text)
        assert m and m.group(1) == "wiki/concepts/rag.md"
        # a non-concept-shaped path must NOT match
        assert wiki.WIKI_FILE_SENTINEL_RE.search("===WIKI-FILE: not a path===") is None

    def test_sentinel_regex_tolerates_indent_and_spacing(self):
        text = "   ===WIKI-FILE:   wiki/concepts/x-y.md   ===   "
        m = wiki.WIKI_FILE_SENTINEL_RE.search(text)
        assert m and m.group(1) == "wiki/concepts/x-y.md"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestSentinelConstants -v`
Expected: FAIL with `AttributeError: module 'wiki' has no attribute 'WIKI_FILE_SENTINEL'`

- [ ] **Step 3: Write minimal implementation**

In `wiki.py`, immediately after the line `RAW_DIR_NAME = "raw"        # raw source *.md files live under base_dir/raw/`:

```python
WIKI_FILE_SENTINEL = "===WIKI-FILE: {path}==="   # prompt rendering (one space each side)
# Parser split. Applied AFTER \r\n/\r -> \n normalization. Tolerates leading
# indentation and flexible spacing; the captured group matches ONLY a concept-page
# path, so prose lines like "===WIKI-FILE: foo===" do NOT split (collision guard).
WIKI_FILE_SENTINEL_RE = re.compile(
    r"(?m)^[ \t]*===WIKI-FILE:[ \t]*(wiki/concepts/[a-z0-9-]+\.md)[ \t]*===[ \t]*$"
)
```

(`re` is already imported at the top of `wiki.py`.)

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestSentinelConstants -v`
Expected: PASS (3 tests)

- [ ] **Step 5: Commit**

```bash
git add wiki.py tests/test_wiki.py
git -c user.name="Kujin Lee" -c user.email="kujinlee@gmail.com" commit -m "feat: add WIKI-FILE sentinel constant and concept-path-shape regex"
```

---

## Task 2: `parse_synthesis_response` parser

**Files:**
- Modify: `wiki.py` (add `_meta_fields` + `parse_synthesis_response`, after `extract_json` ~line 141)
- Test: `tests/test_wiki.py`

- [ ] **Step 1: Write the failing tests**

Add a new test class to `tests/test_wiki.py`:

```python
class TestParseSynthesisResponse:
    def test_header_plus_two_blocks(self):
        text = (
            '{"log_entry": "2026-06-03 12:00 | route-ingest | x", "summary": "did stuff", "gaps": ["g1"]}\n'
            "===WIKI-FILE: wiki/concepts/rag.md===\n"
            "---\nconcept: RAG\n---\n# RAG body\n"
            "===WIKI-FILE: wiki/concepts/mcp.md===\n"
            "# MCP body\n"
        )
        out = wiki.parse_synthesis_response(text)
        assert out["log_entry"] == "2026-06-03 12:00 | route-ingest | x"
        assert out["summary"] == "did stuff"
        assert out["gaps"] == ["g1"]
        assert out["files"] == [
            {"path": "wiki/concepts/rag.md", "content": "---\nconcept: RAG\n---\n# RAG body"},
            {"path": "wiki/concepts/mcp.md", "content": "# MCP body"},
        ]

    def test_content_with_quotes_fences_braces_verbatim(self):
        # The regression case: characters that break the old JSON-string contract.
        body = '# Title\n\nA *supervisor* ("boss") agent.\n\n```python\nx = {"k": 1}\n```\n'
        text = (
            '{"log_entry": "l", "summary": "s", "gaps": []}\n'
            "===WIKI-FILE: wiki/concepts/loop.md===\n"
            + body
        )
        out = wiki.parse_synthesis_response(text)
        assert out["files"][0]["content"] == body.rstrip("\n")

    def test_header_only_changed_nothing(self):
        text = '{"log_entry": "l", "summary": "no change", "gaps": []}'
        out = wiki.parse_synthesis_response(text)
        assert out["files"] == []
        assert out["summary"] == "no change"

    def test_fallback_old_style_json_envelope(self):
        text = json.dumps({
            "files": [{"path": "wiki/concepts/rag.md", "content": "# RAG"}],
            "log_entry": "2026-06-03 12:00 | ingest | rag",
            "summary": "made rag",
        })
        out = wiki.parse_synthesis_response(text)
        assert out["files"] == [{"path": "wiki/concepts/rag.md", "content": "# RAG"}]
        assert out["log_entry"] == "2026-06-03 12:00 | ingest | rag"
        assert out["summary"] == "made rag"
        assert out["gaps"] == []          # absent gaps defaulted

    def test_crlf_parses_like_lf(self):
        text = (
            '{"log_entry": "l", "summary": "s", "gaps": []}\r\n'
            "===WIKI-FILE: wiki/concepts/rag.md===\r\n"
            "# RAG body\r\n"
        )
        out = wiki.parse_synthesis_response(text)
        assert out["files"] == [{"path": "wiki/concepts/rag.md", "content": "# RAG body"}]

    def test_blocks_present_but_no_header_raises(self):
        text = (
            "===WIKI-FILE: wiki/concepts/rag.md===\n"
            "# RAG body\n"
        )
        with pytest.raises(ValueError):
            wiki.parse_synthesis_response(text)

    def test_malformed_header_with_blocks_raises(self):
        text = (
            "{this is not json}\n"
            "===WIKI-FILE: wiki/concepts/rag.md===\n"
            "# RAG body\n"
        )
        with pytest.raises(ValueError):
            wiki.parse_synthesis_response(text)

    def test_non_concept_sentinel_in_content_does_not_split(self):
        body = "Discussing the format: ===WIKI-FILE: example===\nmore text"
        text = (
            '{"log_entry": "l", "summary": "s", "gaps": []}\n'
            "===WIKI-FILE: wiki/concepts/formats.md===\n"
            + body + "\n"
        )
        out = wiki.parse_synthesis_response(text)
        assert len(out["files"]) == 1
        assert out["files"][0]["content"] == body

    def test_valid_header_absent_gaps_defaults_empty(self):
        text = (
            '{"log_entry": "l", "summary": "s"}\n'
            "===WIKI-FILE: wiki/concepts/rag.md===\n"
            "# RAG\n"
        )
        out = wiki.parse_synthesis_response(text)
        assert out["gaps"] == []

    def test_internal_blank_lines_preserved(self):
        # body has intentional leading+trailing blank lines beyond the trimmed pair
        text = (
            '{"log_entry": "l", "summary": "s", "gaps": []}\n'
            "===WIKI-FILE: wiki/concepts/rag.md===\n"
            "\n# RAG\n\nmid\n\n"
        )
        out = wiki.parse_synthesis_response(text)
        # one leading \n and one trailing \n removed; the rest kept
        assert out["files"][0]["content"] == "\n# RAG\n\nmid\n"

    def test_total_garbage_raises(self):
        with pytest.raises(ValueError):
            wiki.parse_synthesis_response("not json and no sentinel at all")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestParseSynthesisResponse -v`
Expected: FAIL with `AttributeError: module 'wiki' has no attribute 'parse_synthesis_response'`

- [ ] **Step 3: Write minimal implementation**

In `wiki.py`, immediately after the `extract_json` function (after its closing `raise ValueError(...)` line):

```python
def _meta_fields(meta: dict) -> dict:
    """Normalize the metadata header into the caller-facing fields."""
    return {
        "log_entry": meta.get("log_entry"),
        "summary": meta.get("summary"),
        "gaps": meta.get("gaps") or [],
    }


def parse_synthesis_response(text: str) -> dict:
    """Parse the synthesis/ingest response: a single-line JSON metadata header
    followed by raw `===WIKI-FILE: <path>===` content blocks. Falls back to a plain
    JSON envelope (extract_json) when no concept-path sentinel is present, so
    old-style replies still work. Returns the dict shape callers expect:
    {"files": [{"path","content"}...], "log_entry", "summary", "gaps"}.

    Raises ValueError on unparseable input (caller retries): total garbage, or
    content blocks present with an empty/malformed metadata header (which would
    otherwise silently drop `gaps`, the recall backstop)."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    parts = WIKI_FILE_SENTINEL_RE.split(text)
    if len(parts) == 1:                       # no concept-path sentinel matched
        meta = extract_json(text)             # raises ValueError on garbage -> retry
        if "files" in meta:
            return {"files": meta["files"], **_meta_fields(meta)}   # old-style envelope
        return {"files": [], **_meta_fields(meta)}                  # "changed nothing"
    header = parts[0].strip()
    if not header:
        raise ValueError("synthesis response has content blocks but no metadata header")
    meta = extract_json(header)               # malformed header -> ValueError -> retry
    files = []
    for i in range(1, len(parts), 2):
        path = parts[i].strip()
        content = parts[i + 1]
        if content.startswith("\n"):
            content = content[1:]
        if content.endswith("\n"):
            content = content[:-1]
        if content == "":
            print(f"  warning: empty content block for {path}", file=sys.stderr)
        files.append({"path": path, "content": content})
    return {"files": files, **_meta_fields(meta)}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestParseSynthesisResponse -v`
Expected: PASS (11 tests)

- [ ] **Step 5: Commit**

```bash
git add wiki.py tests/test_wiki.py
git -c user.name="Kujin Lee" -c user.email="kujinlee@gmail.com" commit -m "feat: add parse_synthesis_response (sentinel format + JSON fallback)"
```

---

## Task 3: `call_claude_synthesis` retry wrapper

**Files:**
- Modify: `wiki.py` (after `call_claude_json` ~line 127)
- Test: `tests/test_wiki.py`

- [ ] **Step 1: Write the failing test**

Add to `tests/test_wiki.py`:

```python
class TestCallClaudeSynthesis:
    def test_returns_parsed_dict(self):
        resp = (
            '{"log_entry": "l", "summary": "s", "gaps": []}\n'
            "===WIKI-FILE: wiki/concepts/rag.md===\n# RAG\n"
        )
        with patch("wiki.call_claude", return_value=resp):
            out = wiki.call_claude_synthesis("prompt", model="sonnet")
        assert out["files"] == [{"path": "wiki/concepts/rag.md", "content": "# RAG"}]

    def test_retries_then_succeeds(self):
        good = (
            '{"log_entry": "l", "summary": "s", "gaps": []}\n'
            "===WIKI-FILE: wiki/concepts/rag.md===\n# RAG\n"
        )
        with patch("wiki.call_claude", side_effect=["total garbage no json", good]), \
                patch("wiki.time.sleep"):
            out = wiki.call_claude_synthesis("prompt", model="sonnet")
        assert out["files"][0]["path"] == "wiki/concepts/rag.md"

    def test_raises_after_exhausting_retries(self):
        with patch("wiki.call_claude", return_value="never valid"), \
                patch("wiki.time.sleep"):
            with pytest.raises(ValueError):
                wiki.call_claude_synthesis("prompt", model="sonnet", retries=2)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestCallClaudeSynthesis -v`
Expected: FAIL with `AttributeError: module 'wiki' has no attribute 'call_claude_synthesis'`

- [ ] **Step 3: Write minimal implementation**

In `wiki.py`, immediately after the `call_claude_json` function:

```python
def call_claude_synthesis(prompt: str, model: str | None = None,
                          retries: int = CLAUDE_RETRIES) -> dict:
    """Like call_claude_json but parses the sentinel-delimited synthesis/ingest
    format (raw page bodies carried outside JSON), retrying on an unparseable
    response. Use for ingest/synthesis; the router keeps call_claude_json."""
    last_exc = None
    for attempt in range(retries):
        try:
            return parse_synthesis_response(call_claude(prompt, model=model))
        except ValueError as exc:
            last_exc = exc
            if attempt < retries - 1:
                print(f"  response not parseable; retry {attempt + 1}/{retries - 1}...",
                      file=sys.stderr, flush=True)
                time.sleep(5)
    raise last_exc
```

(`time` is already imported at the top of `wiki.py`.)

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestCallClaudeSynthesis -v`
Expected: PASS (3 tests)

- [ ] **Step 5: Commit**

```bash
git add wiki.py tests/test_wiki.py
git -c user.name="Kujin Lee" -c user.email="kujinlee@gmail.com" commit -m "feat: add call_claude_synthesis retry wrapper"
```

---

## Task 4: `output_format_instructions` + rewire the two prompt builders

**Files:**
- Modify: `wiki.py` (`build_ingest_prompt` ~line 144, `build_synth_prompt` ~line 212; add `output_format_instructions` before them)
- Test: `tests/test_wiki.py`

- [ ] **Step 1: Write the failing test**

Add to `tests/test_wiki.py`:

```python
class TestOutputFormatInstructions:
    def test_synth_prompt_uses_sentinel_format(self):
        p = wiki.build_synth_prompt("schema", "idx", {"rag": "# RAG"}, "src.md", "body")
        assert "===WIKI-FILE:" in p
        assert "NO escaping" in p
        assert "column 0" in p
        assert "wiki/concepts/<kebab-case-name>.md" in p
        assert '"gaps"' in p          # synth includes gaps in the header
        # the old JSON-content contract must be gone
        assert '"content": "<full page markdown>"' not in p

    def test_ingest_prompt_uses_sentinel_format_without_gaps(self):
        p = wiki.build_ingest_prompt("schema", "idx", {}, "src.md", "body")
        assert "===WIKI-FILE:" in p
        assert "NO escaping" in p
        assert '"gaps"' not in p       # brute-force ingest has no gaps field
        assert '"content": "<full page markdown>"' not in p
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestOutputFormatInstructions -v`
Expected: FAIL (the prompts still contain `"content": "<full page markdown>"` and lack `===WIKI-FILE:`)

- [ ] **Step 3: Write minimal implementation**

(3a) In `wiki.py`, add this function immediately before `build_ingest_prompt`:

```python
def output_format_instructions(include_gaps: bool) -> str:
    """Shared response-format instructions for ingest/synthesis prompts: a single
    JSON metadata line then raw ===WIKI-FILE: blocks. References WIKI_FILE_SENTINEL
    so prompt and parser cannot drift."""
    gaps_field = ', "gaps": ["<slug>", "..."]' if include_gaps else ""
    eg1 = WIKI_FILE_SENTINEL.format(path="wiki/concepts/<kebab-case-name>.md")
    eg2 = WIKI_FILE_SENTINEL.format(path="wiki/concepts/<another>.md")
    return f"""Respond in EXACTLY this format — a single-line JSON metadata object, then one \
block per page you changed. Do NOT put page content inside the JSON.

{{"log_entry": "<YYYY-MM-DD HH:MM | kind | summary>", "summary": "<one paragraph>"{gaps_field}}}
{eg1}
<full raw page markdown — real newlines, quotes, backticks; NO escaping, NO code fences>
{eg2}
<full raw page markdown>

Format rules:
- The FIRST line is the JSON metadata object and nothing else. It lists NO file contents and NO paths.
- Each changed page follows as a line `{eg1}` starting at column 0 (NO indentation), on its own line, then the page's raw markdown.
- The <path> is ALWAYS wiki/concepts/<kebab-case-name>.md — the parser ignores any sentinel whose path is not this shape.
- Write page content verbatim — do NOT escape characters and do NOT wrap it in code fences.
- NEVER write a line of the form ===WIKI-FILE: ...=== inside page content.
- If you changed no pages, emit only the JSON metadata line."""
```

(3b) Replace the format/response section of `build_ingest_prompt`. The current function ends with:

```python
Respond with ONLY a JSON object — no preamble, no explanation, no markdown fence:
{{
  "files": [
    {{"path": "wiki/concepts/<kebab-case-name>.md", "content": "<full page markdown>"}}
  ],
  "log_entry": "<YYYY-MM-DD HH:MM | ingest | summary>",
  "summary": "<one paragraph: what was created/updated>"
}}

Rules:
- Concept filenames must be kebab-case (e.g., harness-engineering.md)
- Write all wiki content in English, even when the source is Korean
- Update existing pages in-place; no duplication
- Add contradictions to ## Tensions & Tradeoffs, do not silently overwrite
- The `sources:` frontmatter lists the source filenames a concept draws from
- Every page's frontmatter MUST include `category:` (EXACTLY one of: {categories}) and a one-line `summary:` — these drive the index
- Emit ONLY concept page files. Do NOT emit wiki/index.md — the index is rebuilt deterministically from frontmatter by `reindex`.
- Extract durable CONCEPTS (techniques, patterns, architectures, principles) — not video-specific trivia
"""
```

Change the `Respond with ONLY a JSON object...` block (the `Respond...` line through the closing `}}` and its blank line) to `{output_format_instructions(include_gaps=False)}`, leaving the `Rules:` list intact. The result reads:

```python
{output_format_instructions(include_gaps=False)}

Rules:
- Concept filenames must be kebab-case (e.g., harness-engineering.md)
- Write all wiki content in English, even when the source is Korean
- Update existing pages in-place; no duplication
- Add contradictions to ## Tensions & Tradeoffs, do not silently overwrite
- The `sources:` frontmatter lists the source filenames a concept draws from
- Every page's frontmatter MUST include `category:` (EXACTLY one of: {categories}) and a one-line `summary:` — these drive the index
- Emit ONLY concept page files. Do NOT emit wiki/index.md — the index is rebuilt deterministically from frontmatter by `reindex`.
- Extract durable CONCEPTS (techniques, patterns, architectures, principles) — not video-specific trivia
"""
```

Also in `build_ingest_prompt`, update the preamble sentence. Change:

```python
extraction defined below, and your entire response MUST be the single JSON object requested at the end.
```

to:

```python
extraction defined below, and your entire response MUST be ONLY the metadata-plus-files format defined below — no preamble, no prose.
```

(3c) Replace the format/response section of `build_synth_prompt`. The current block:

```python
Respond with ONLY a JSON object — no preamble, no explanation, no markdown fence:
{{
  "files": [
    {{"path": "wiki/concepts/<kebab-case-name>.md", "content": "<full page markdown>"}}
  ],
  "log_entry": "<YYYY-MM-DD HH:MM | route-ingest | summary>",
  "summary": "<one paragraph: what was created/updated>",
  "gaps": ["<slug seen in the compact index but whose full page was not provided>", "..."]
}}

Rules:
```

becomes:

```python
{output_format_instructions(include_gaps=True)}

Rules:
```

Leave the entire `Rules:` list (kebab-case … durable CONCEPTS) unchanged. Also update the same preamble sentence in `build_synth_prompt` exactly as in (3b).

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestOutputFormatInstructions -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Run the FULL suite to confirm existing prompt tests still pass**

Run: `.venv/bin/python -m pytest tests/test_wiki.py -q`
Expected: PASS (all). If any existing test asserted the old `"files": [...]` JSON wording in a prompt, update that assertion to the new format wording (search for `"content": "<full page markdown>"` in the test file).

- [ ] **Step 6: Commit**

```bash
git add wiki.py tests/test_wiki.py
git -c user.name="Kujin Lee" -c user.email="kujinlee@gmail.com" commit -m "feat: emit sentinel output format from ingest/synth prompts via shared helper"
```

---

## Task 5: Wire `cmd_route_ingest` and `cmd_resolve_gaps` to `call_claude_synthesis`

**Files:**
- Modify: `wiki.py` (`cmd_route_ingest` synth call ~line 541, `cmd_resolve_gaps` synth call ~line 614)
- Test: `tests/test_wiki.py` (existing TestCmdRouteIngest / TestCmdResolveGaps cover behavior; add one new-format test each)

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_wiki.py` inside the existing `class TestCmdRouteIngest` (reuse its `_setup` helper):

```python
    def test_route_ingest_new_sentinel_format(self, tmp_path):
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds answers"})
        router = json.dumps({"slugs": ["rag"], "rationale": "about RAG"})
        synth = (
            '{"log_entry": "2026-06-03 12:00 | route-ingest | rag", "summary": "updated rag", "gaps": []}\n'
            "===WIKI-FILE: wiki/concepts/rag.md===\n"
            '# RAG\n\nUses "boss" quotes and {braces} fine.\n'
        )
        with patch("wiki.call_claude", side_effect=[router, synth]), \
                patch("wiki.reindex", return_value="reindexed"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert (wiki_dir / "concepts" / "rag.md").read_text() == \
            '# RAG\n\nUses "boss" quotes and {braces} fine.'
```

Add to `tests/test_wiki.py` inside the existing `class TestCmdResolveGaps` (reuse its `_setup`):

```python
    def test_resolve_new_sentinel_format(self, tmp_path):
        wiki_dir, args = self._setup(tmp_path)
        gap_path = wiki_dir / wiki.GAP_LOG_NAME
        wiki.append_gap_log(gap_path, "talk.md", ["context-engineering"], kind="gap")
        synth = (
            '{"log_entry": "2026-06-03 12:00 | resolve-gaps | ce", "summary": "resolved", "gaps": []}\n'
            "===WIKI-FILE: wiki/concepts/context-engineering.md===\n"
            "# ce resolved\n"
        )
        with patch("wiki.call_claude", side_effect=[synth]), patch("wiki.reindex", return_value="r"):
            wiki.cmd_resolve_gaps(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert (wiki_dir / "concepts" / "context-engineering.md").read_text() == "# ce resolved"
        assert "context-engineering" not in gap_path.read_text()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestCmdRouteIngest::test_route_ingest_new_sentinel_format tests/test_wiki.py::TestCmdResolveGaps::test_resolve_new_sentinel_format -v`
Expected: FAIL — `cmd_route_ingest`/`cmd_resolve_gaps` still call `call_claude_json`, which cannot parse the sentinel body (raises, source skipped → file not written / gap not cleared).

- [ ] **Step 3: Write minimal implementation**

In `cmd_route_ingest`, find the synthesis call:

```python
                resp = call_claude_json(
                    build_synth_prompt(ctx["schema"], compact, selected, source_path.name, source_text),
                    model=synth_model,
                )
```

Change `call_claude_json` to `call_claude_synthesis`:

```python
                resp = call_claude_synthesis(
                    build_synth_prompt(ctx["schema"], compact, selected, source_path.name, source_text),
                    model=synth_model,
                )
```

In `cmd_resolve_gaps`, find the synthesis call:

```python
                resp = call_claude_json(
                    build_synth_prompt(ctx["schema"], compact, selected, source_name, source_path.read_text()),
                    model=synth_model,
                )
```

Change `call_claude_json` to `call_claude_synthesis`:

```python
                resp = call_claude_synthesis(
                    build_synth_prompt(ctx["schema"], compact, selected, source_name, source_path.read_text()),
                    model=synth_model,
                )
```

No other changes — both functions already read `resp.get("files"/"gaps"/"log_entry"/"summary")`.

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestCmdRouteIngest tests/test_wiki.py::TestCmdResolveGaps -v`
Expected: PASS (all — the two new sentinel tests plus the existing JSON-mock tests, which now flow through the parser's fallback path)

- [ ] **Step 5: Commit**

```bash
git add wiki.py tests/test_wiki.py
git -c user.name="Kujin Lee" -c user.email="kujinlee@gmail.com" commit -m "feat: route-ingest and resolve-gaps use call_claude_synthesis"
```

---

## Task 6: `cmd_ingest` — swap, add path guard, harden key access

**Files:**
- Modify: `wiki.py` (`cmd_ingest` ~lines 471-494)
- Test: `tests/test_wiki.py` (existing TestCmdIngest + new tests)

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_wiki.py` inside the existing `class TestCmdIngest`:

```python
    def test_ingest_new_sentinel_format(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")
        source = tmp_path / "talk.md"
        source.write_text("# a talk")
        resp = (
            '{"log_entry": "2026-06-03 12:00 | ingest | talk", "summary": "made harness page"}\n'
            "===WIKI-FILE: wiki/concepts/harness-engineering.md===\n"
            '# Harness\n\nWith "quotes" and {braces}.\n'
        )
        args = MagicMock()
        args.source = str(source)
        args.model = None
        with patch("wiki.call_claude", return_value=resp), \
                patch("wiki.reindex", return_value="reindexed"):
            wiki.cmd_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert (wiki_dir / "concepts" / "harness-engineering.md").read_text() == \
            '# Harness\n\nWith "quotes" and {braces}.'
        assert "2026-06-03 12:00 | ingest | talk" in (wiki_dir / "log.md").read_text()

    def test_ingest_rejects_out_of_tree_path(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")
        source = tmp_path / "talk.md"
        source.write_text("# a talk")
        # an old-style JSON envelope (fallback path) carrying a traversal path
        resp = json.dumps({
            "files": [{"path": "../../evil.md", "content": "pwned"}],
            "log_entry": "2026-06-03 12:00 | ingest | talk",
            "summary": "tried to escape",
        })
        args = MagicMock()
        args.source = str(source)
        args.model = None
        with patch("wiki.call_claude", return_value=resp), \
                patch("wiki.reindex", return_value="reindexed"):
            wiki.cmd_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert not (tmp_path.parent / "evil.md").exists()
        assert not (tmp_path / "evil.md").exists()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestCmdIngest::test_ingest_new_sentinel_format tests/test_wiki.py::TestCmdIngest::test_ingest_rejects_out_of_tree_path -v`
Expected: FAIL — `cmd_ingest` still uses `call_claude_json` (cannot parse the sentinel body) and has no `safe_write_path` guard (would attempt the traversal write).

- [ ] **Step 3: Write minimal implementation**

The current loop body in `cmd_ingest` is:

```python
    ingest_model = getattr(args, "model", None)
    total = len(sources)
    for i, source_path in enumerate(sources, 1):
        print(f"\nIngesting {source_path}...", flush=True)
        ctx = read_wiki_context(wiki_dir)
        prompt = build_ingest_prompt(
            ctx["schema"], ctx["index"], ctx["concepts"], source_path.name, source_path.read_text()
        )
        response = call_claude_json(prompt, model=ingest_model)
        write_wiki_files(response["files"], base_dir)
        append_log_entry(wiki_dir / "log.md", response["log_entry"])
        print(f"  {response['summary']}")
        # Reindex after every file — it's a deterministic ~0.1s projection, so the
        # index stays continuously correct even if a long run is interrupted.
        _try_reindex(wiki_dir, base_dir, label=f"{i}/{total}")
```

Replace it with:

```python
    ingest_model = getattr(args, "model", None)
    concepts_dir = wiki_dir / "concepts"
    total = len(sources)
    for i, source_path in enumerate(sources, 1):
        print(f"\nIngesting {source_path}...", flush=True)
        ctx = read_wiki_context(wiki_dir)
        prompt = build_ingest_prompt(
            ctx["schema"], ctx["index"], ctx["concepts"], source_path.name, source_path.read_text()
        )
        response = call_claude_synthesis(prompt, model=ingest_model)
        valid_files = []
        for f in response.get("files", []):
            try:
                safe_write_path(base_dir, f["path"], concepts_dir)
                valid_files.append(f)
            except (ValueError, KeyError) as exc:
                print(f"  rejected unsafe path ({exc})", file=sys.stderr)
        write_wiki_files(valid_files, base_dir)
        append_log_entry(
            wiki_dir / "log.md",
            response.get("log_entry")
            or f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | ingest | {source_path.name}: no changes",
        )
        print(f"  {response.get('summary') or '(no changes)'}")
        # Reindex after every file — it's a deterministic ~0.1s projection, so the
        # index stays continuously correct even if a long run is interrupted.
        _try_reindex(wiki_dir, base_dir, label=f"{i}/{total}")
```

(`safe_write_path`, `datetime`, and `call_claude_synthesis` are all already defined/imported in `wiki.py`.)

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_wiki.py::TestCmdIngest -v`
Expected: PASS (all — the two new tests plus existing ingest tests via the parser fallback)

- [ ] **Step 5: Run the FULL suite**

Run: `.venv/bin/python -m pytest tests/test_wiki.py -q`
Expected: PASS (110 baseline + all new tests). If an existing TestCmdIngest test asserted on a hard `log_entry`/`summary` that is now `.get`-defaulted, confirm its mocked response includes those keys (the existing mocks do).

- [ ] **Step 6: Commit**

```bash
git add wiki.py tests/test_wiki.py
git -c user.name="Kujin Lee" -c user.email="kujinlee@gmail.com" commit -m "feat: cmd_ingest uses call_claude_synthesis + safe_write_path guard"
```

---

## Final verification

- [ ] Run the full suite once more: `.venv/bin/python -m pytest tests/test_wiki.py -q` → all green.
- [ ] Grep for stragglers: `grep -n "call_claude_json" wiki.py` should show ONLY the router path (`cmd_query`/`cmd_lint` use `call_claude` directly; the router in `cmd_route_ingest` uses `call_claude_json`). The three synthesis/ingest call sites must now use `call_claude_synthesis`.
- [ ] Confirm `git log --oneline` shows the 6 task commits.
