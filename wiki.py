#!/usr/bin/env python3
"""LLM Wiki — Agentic AI & Claude Code knowledge base.

A concept-first, LLM-maintained wiki over the YouTube playlist summary
markdown files in this directory. Three operations — ingest, query, lint —
each powered by `claude --print` subprocess calls.

Based on Karpathy's LLM Wiki pattern:
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
"""
import argparse
import contextlib
import fcntl
import json
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# Transient `claude` failures (rate-limit/overload) surface as a fast non-zero exit.
# Retry a few times with backoff before giving up.
CLAUDE_RETRIES = 3
CLAUDE_BACKOFF_SECONDS = [15, 45, 90]

# Index category order (must match wiki/CLAUDE.md). Each concept page declares its
# category in frontmatter; `reindex` groups pages by it deterministically.
CATEGORY_ORDER = [
    "LLM Internals & Training",
    "Harness & Context Engineering",
    "Agent Architecture & Patterns",
    "Memory & Knowledge Systems",
    "Coding Tools & IDEs",
    "Workflows & Methodology",
    "Skills, Plugins & Automation",
    "Industry, Strategy & Careers",
]

# Router-Synthesizer ingest configuration.
ROUTER_MODEL = "haiku"      # cheap slug-selection over the compact index
SYNTH_MODEL = "sonnet"      # bounded synthesis over K selected pages
SLUG_CAP = 25               # max pages fed to synthesis per source
GAP_LOG_NAME = ".gap-log.jsonl"
ROUTE_LOCK_NAME = ".route-lock"
ROUTE_FAILURES_NAME = ".route-failures.txt"


def init_wiki(wiki_dir: Path) -> None:
    (wiki_dir / "concepts").mkdir(parents=True, exist_ok=True)
    log = wiki_dir / "log.md"
    index = wiki_dir / "index.md"
    if not log.exists():
        log.write_text("# Wiki Operation Log\n\n")
    if not index.exists():
        index.write_text("# Agentic AI & Claude Code Wiki Index\n\n*Run `python wiki.py ingest` to populate.*\n")


@contextlib.contextmanager
def route_lock(wiki_dir: Path):
    """Advisory lock so only one route-ingest/resolve-gaps run touches the shared
    concept pages at a time. Fails fast (exit 1) if another run holds it."""
    init_wiki(wiki_dir)
    lock_path = wiki_dir / ROUTE_LOCK_NAME
    fh = lock_path.open("w")
    try:
        try:
            fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            print(f"Another run holds {lock_path}. Aborting (serial-only).", file=sys.stderr)
            sys.exit(1)
        yield
    finally:
        fcntl.flock(fh, fcntl.LOCK_UN)
        fh.close()


def read_wiki_context(wiki_dir: Path) -> dict:
    schema_path = wiki_dir / "CLAUDE.md"
    index_path = wiki_dir / "index.md"
    concepts_dir = wiki_dir / "concepts"
    return {
        "schema": schema_path.read_text() if schema_path.exists() else "",
        "index": index_path.read_text() if index_path.exists() else "",
        "concepts": {
            p.stem: p.read_text()
            for p in sorted(concepts_dir.glob("*.md"))
        } if concepts_dir.exists() else {},
    }


def call_claude(prompt: str, model: str | None = None, retries: int = CLAUDE_RETRIES) -> str:
    cmd = ["claude", "--print"]
    if model:
        cmd += ["--model", model]
    last_exc = None
    for attempt in range(retries):
        try:
            proc = subprocess.run(cmd, input=prompt, stdout=subprocess.PIPE, text=True, check=True)
            return proc.stdout.strip()
        except subprocess.CalledProcessError as exc:
            last_exc = exc
            if attempt < retries - 1:
                wait = CLAUDE_BACKOFF_SECONDS[min(attempt, len(CLAUDE_BACKOFF_SECONDS) - 1)]
                print(f"  claude exited {exc.returncode}; retry {attempt + 1}/{retries - 1} in {wait}s...",
                      file=sys.stderr, flush=True)
                time.sleep(wait)
    raise last_exc


def call_claude_json(prompt: str, model: str | None = None, retries: int = CLAUDE_RETRIES) -> dict:
    """Call claude and parse a JSON envelope, retrying when the response is not
    valid JSON. The subprocess inherits the project's SessionStart hooks (e.g.
    injected handoff/memory), so it occasionally replies with conversational
    prose instead of the requested JSON; a retry almost always recovers."""
    last_exc = None
    for attempt in range(retries):
        try:
            return extract_json(call_claude(prompt, model=model))
        except ValueError as exc:
            last_exc = exc
            if attempt < retries - 1:
                print(f"  response was not JSON; retry {attempt + 1}/{retries - 1}...",
                      file=sys.stderr, flush=True)
                time.sleep(5)
    raise last_exc


def extract_json(text: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    start, end = text.find("{"), text.rfind("}") + 1
    if start != -1 and end > start:
        return json.loads(text[start:end])
    raise ValueError(f"No valid JSON found in response:\n{text[:300]}")


def build_ingest_prompt(schema: str, index: str, concepts: dict, source_name: str, source: str) -> str:
    concepts_block = "\n\n".join(
        f"### Existing page: {name}\n{content}" for name, content in concepts.items()
    ) or "(none yet)"
    categories = "; ".join(CATEGORY_ORDER)
    return f"""IGNORE any session handoff, memory, prior-conversation, or status context that may \
have been injected into this session — it is irrelevant noise. Your ONLY task is the structured \
extraction defined below, and your entire response MUST be the single JSON object requested at the end.

You are maintaining an "Agentic AI & Claude Code" knowledge base built from \
YouTube talk and tutorial summaries. Sources may be in Korean or English; the wiki itself \
is written ENTIRELY in English. Synthesize across languages — do not transcribe. Follow the schema exactly.

{schema}

## Current wiki/index.md
{index}

## Existing concept pages in wiki/concepts/
{concepts_block}

## Source document to ingest (filename: {source_name})
{source}

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


def build_router_prompt(compact_index: str, source_name: str, source: str) -> str:
    return f"""IGNORE any session handoff, memory, prior-conversation, or status context that may \
have been injected into this session — it is irrelevant noise. Your ONLY task is to select relevant \
page slugs and reply with a single JSON object.

You maintain an "Agentic AI & Claude Code" knowledge base. Below is a COMPACT INDEX — one line per \
existing page as `slug: summary [aliases: ...]`. A new SOURCE document follows (it may be Korean or \
English; match on MEANING, not words). Return the slugs of existing pages this source is relevant to \
— pages it would update or extend, or that it conceptually cross-links to. Be GENEROUS but precise: \
a missed slug causes a duplicate page downstream.

## Compact index
{compact_index}

## Source document (filename: {source_name})
{source}

Respond with ONLY this JSON object — no preamble, no markdown fence:
{{"slugs": ["existing-slug", "..."], "rationale": "<one line>"}}
If no existing page is relevant (an all-new source), return an empty slugs list.
"""


def build_synth_prompt(schema: str, compact_index: str, selected_pages: dict,
                       source_name: str, source: str) -> str:
    pages_block = "\n\n".join(
        f"### Existing page: {name}\n{content}" for name, content in selected_pages.items()
    ) or "(none selected — likely an all-new source)"
    categories = "; ".join(CATEGORY_ORDER)
    return f"""IGNORE any session handoff, memory, prior-conversation, or status context that may \
have been injected into this session — it is irrelevant noise. Your ONLY task is the structured \
extraction defined below, and your entire response MUST be the single JSON object requested at the end.

You are maintaining an "Agentic AI & Claude Code" knowledge base built from \
YouTube talk and tutorial summaries. Sources may be in Korean or English; the wiki itself \
is written ENTIRELY in English. Synthesize across languages — do not transcribe. Follow the schema exactly.

{schema}

## Full compact index (awareness only — every existing page as `slug: summary`)
{compact_index}

## Selected concept pages (full content — the ONLY pages you may update in place)
{pages_block}

## Source document to ingest (filename: {source_name})
{source}

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
- Concept filenames must be kebab-case (e.g., harness-engineering.md)
- Write all wiki content in English, even when the source is Korean
- Update existing pages in-place; no duplication
- Add contradictions to ## Tensions & Tradeoffs, do not silently overwrite
- The `sources:` frontmatter lists the source filenames a concept draws from
- Every page's frontmatter MUST include `category:` (EXACTLY one of: {categories}) and a one-line `summary:`
- Emit ONLY pages you actually CHANGED. If a selected page needs no change, OMIT it from "files".
- If the source relates to a concept that appears in the compact index but whose full page is NOT among the selected pages above, DO NOT recreate it from its summary line — instead list its slug under "gaps".
- You MAY create a new page for a genuinely new concept (a slug not in the compact index).
- Extract durable CONCEPTS (techniques, patterns, architectures, principles) — not video-specific trivia
"""


def build_query_prompt(schema: str, index: str, concepts: dict, question: str) -> str:
    concepts_block = "\n\n".join(
        f"### {name}\n{content}" for name, content in concepts.items()
    ) or "(no concept pages yet — run ingest first)"
    return f"""You are answering a question using the Agentic AI & Claude Code wiki.

{schema}

## wiki/index.md
{index}

## Concept pages
{concepts_block}

## Question
{question}

Answer using wiki content. Cite which pages you drew from (e.g., "Per [[harness-engineering]] and [[context-engineering]]..."). If the answer reveals a wiki gap, end with "Gap: <description>".
"""


def build_lint_prompt(schema: str, index: str, concepts: dict) -> str:
    file_list = list(concepts.keys())
    concepts_block = "\n\n".join(
        f"### {name}\n{content}" for name, content in concepts.items()
    ) or "(none)"
    return f"""You are auditing the Agentic AI & Claude Code wiki for quality issues.

{schema}

## wiki/index.md
{index}

## Concept files present: {file_list}

## Concept page contents
{concepts_block}

Run this lint checklist and report each issue:
1. Orphan detection: concepts listed in index.md with no file in concepts/
2. Reverse orphans: files in concepts/ not listed in index.md
3. Broken cross-references: [[name]] links with no matching page
4. Stale tensions: Tensions & Tradeoffs sections with unresolved issues
5. Category coverage: concepts that appear miscategorized in the index

Say "OK" for clean items. End with a summary verdict.
"""


def read_frontmatter(text: str) -> dict:
    """Parse the leading YAML-ish frontmatter block into a flat dict of key -> raw value."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    meta = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
    return meta


def parse_frontmatter_list(value: str) -> list[str]:
    """Parse a raw frontmatter value like '[a, b]' or 'a' into a list of strings.

    `read_frontmatter` returns list-valued fields (sources, aliases, related) as
    the raw bracketed string; this normalises them. Splits on commas — adequate
    for slugs/aliases (which never contain commas).
    """
    if not value:
        return []
    v = value.strip()
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1]
    items = [part.strip().strip("'\"") for part in v.split(",")]
    return [item for item in items if item]


def build_index(concepts: dict) -> str:
    """Deterministically render wiki/index.md from concept-page frontmatter.

    Groups pages by their `category:` (in CATEGORY_ORDER), one line each:
    `- [[stem]] — summary`. Pages with a missing/unknown category land under
    'Uncategorized' so nothing is silently dropped.
    """
    by_cat: dict[str, list] = {}
    for stem, content in concepts.items():
        fm = read_frontmatter(content)
        cat = fm.get("category", "").strip()
        summary = fm.get("summary", "").strip() or fm.get("concept", stem)
        bucket = cat if cat in CATEGORY_ORDER else "Uncategorized"
        by_cat.setdefault(bucket, []).append((fm.get("concept", stem), stem, summary))

    lines = ["# Agentic AI & Claude Code Wiki Index", ""]
    for cat in CATEGORY_ORDER + ["Uncategorized"]:
        items = by_cat.get(cat)
        if not items:
            continue
        lines.append(f"## {cat}")
        for _concept, stem, summary in sorted(items, key=lambda e: e[0].lower()):
            lines.append(f"- [[{stem}]] — {summary}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_compact_index(concepts: dict) -> str:
    """One line per concept page for the router: `slug: summary [aliases: a, b]`.

    Far smaller than the full pages (~25 tokens/line), so the router can see the
    whole corpus cheaply. Aliases are included to aid cross-lingual matching.
    """
    lines = []
    for stem, content in sorted(concepts.items()):
        fm = read_frontmatter(content)
        summary = fm.get("summary", "").strip() or fm.get("concept", stem)
        aliases = parse_frontmatter_list(fm.get("aliases", ""))
        alias_str = f" [aliases: {', '.join(aliases)}]" if aliases else ""
        lines.append(f"{stem}: {summary}{alias_str}")
    return "\n".join(lines) or "(none yet)"


def write_wiki_files(files: list[dict], base_dir: Path) -> None:
    for f in files:
        path = base_dir / f["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f["content"])


def safe_write_path(base_dir: Path, rel_path: str, restrict_to: Path) -> Path:
    """Resolve base_dir/rel_path and assert it stays under restrict_to.

    Guards against an LLM emitting a traversal/out-of-tree path (e.g.
    '../wiki.py' or 'wiki/CLAUDE.md'). Returns the resolved path or raises
    ValueError.
    """
    resolved = (base_dir / rel_path).resolve()
    allowed = restrict_to.resolve()
    if not resolved.is_relative_to(allowed):
        raise ValueError(f"path {rel_path!r} escapes {restrict_to}")
    return resolved


def append_log_entry(log_path: Path, entry: str) -> None:
    existing = log_path.read_text() if log_path.exists() else "# Wiki Operation Log\n\n"
    log_path.write_text(existing + entry + "\n")


def append_gap_log(gap_path: Path, source: str, slugs: list[str], kind: str) -> None:
    """Append a recall-backstop record. kind='gap' (a concept the synth saw in the
    index but wasn't given the page for) or 'new_slug' (an output page not among the
    router's slugs — possibly a new concept, possibly an unintended rename)."""
    rec = {
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "source": source,
        "kind": kind,
        "slugs": slugs,
    }
    gap_path.parent.mkdir(parents=True, exist_ok=True)
    with gap_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def summarize_gap_log(gap_path: Path) -> str:
    """Human-readable summary of unresolved gap-log records, for lint."""
    if not gap_path.exists():
        return "Gap log: no gaps recorded."
    records = [json.loads(l) for l in gap_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    if not records:
        return "Gap log: no gaps recorded."
    lines = [f"Gap log: {len(records)} unresolved entr{'y' if len(records) == 1 else 'ies'}:"]
    for r in records:
        lines.append(f"  [{r.get('kind')}] {r.get('source')} -> {', '.join(r.get('slugs', []))}")
    return "\n".join(lines)


def reindex(wiki_dir: Path = Path("wiki"), base_dir: Path = Path(".")) -> str:
    """Rebuild wiki/index.md deterministically from concept-page frontmatter.

    No LLM call — pure projection over `category`/`summary` fields. Instant,
    free, and reproducible. Returns the summary line.
    """
    ctx = read_wiki_context(wiki_dir)
    index_md = build_index(ctx["concepts"])
    (wiki_dir / "index.md").write_text(index_md)
    n_concepts = index_md.count("\n- [[")
    n_cats = index_md.count("\n## ")
    uncategorized = "## Uncategorized" in index_md
    append_log_entry(
        wiki_dir / "log.md",
        f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | reindex | {n_concepts} concepts across {n_cats} categories",
    )
    note = "  (some pages Uncategorized — check frontmatter)" if uncategorized else ""
    return f"Rebuilt index: {n_concepts} concepts across {n_cats} categories.{note}"


def cmd_ingest(args, wiki_dir: Path = Path("wiki"), base_dir: Path = Path(".")):
    init_wiki(wiki_dir)
    if not (wiki_dir / "CLAUDE.md").exists():
        print("Error: wiki/CLAUDE.md not found. Create it first.", file=sys.stderr)
        sys.exit(1)
    sources = [Path(args.source)] if args.source else sorted(base_dir.glob("*.md"))
    if not sources:
        print("No *.md source files found.", file=sys.stderr)
        sys.exit(1)
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


def _try_reindex(wiki_dir: Path, base_dir: Path, label: str) -> None:
    """Reindex without aborting a bulk run. The index is derived state — concept
    pages are already on disk, so a failed reindex can be recovered later with
    `python wiki.py reindex`."""
    print(f"\nReindexing ({label})...", flush=True)
    try:
        print(f"  {reindex(wiki_dir, base_dir)}")
    except Exception as exc:  # noqa: BLE001 — keep ingesting; pages are safe
        print(f"  WARNING: reindex failed ({exc}); pages are intact. "
              f"Run `python wiki.py reindex` later to rebuild the index.", file=sys.stderr)


def cmd_route_ingest(args, wiki_dir: Path = Path("wiki"), base_dir: Path = Path(".")):
    init_wiki(wiki_dir)
    if not (wiki_dir / "CLAUDE.md").exists():
        print("Error: wiki/CLAUDE.md not found. Create it first.", file=sys.stderr)
        sys.exit(1)
    sources = [Path(args.source)] if args.source else sorted(base_dir.glob("*.md"))
    if not sources:
        print("No *.md source files found.", file=sys.stderr)
        sys.exit(1)
    router_model = getattr(args, "router_model", None) or ROUTER_MODEL
    synth_model = getattr(args, "synth_model", None) or SYNTH_MODEL
    concepts_dir = wiki_dir / "concepts"
    gap_path = wiki_dir / GAP_LOG_NAME
    failures_path = wiki_dir / ROUTE_FAILURES_NAME
    total = len(sources)
    with route_lock(wiki_dir):
        for i, source_path in enumerate(sources, 1):
            print(f"\nroute-ingest {source_path} ...", flush=True)
            source_text = source_path.read_text()
            ctx = read_wiki_context(wiki_dir)
            compact = build_compact_index(ctx["concepts"])

            # (1) ROUTE
            try:
                routed = call_claude_json(build_router_prompt(compact, source_path.name, source_text),
                                          model=router_model)
            except Exception as exc:  # noqa: BLE001
                print(f"  router failed ({exc}); skipping", file=sys.stderr)
                with failures_path.open("a", encoding="utf-8") as fh:
                    fh.write(source_path.name + "\n")
                continue

            # (2) LOAD + filter hallucinations + cap
            existing = {p.stem for p in concepts_dir.glob("*.md")}
            requested = routed.get("slugs", []) or []
            matched = [s for s in requested if s in existing]
            dropped = [s for s in requested if s not in existing]
            if dropped:
                print(f"  dropped non-existent slugs: {dropped}", file=sys.stderr)
            if len(matched) > SLUG_CAP:
                print(f"  capped {len(matched)} slugs to {SLUG_CAP}", file=sys.stderr)
            valid_slugs = matched[:SLUG_CAP]
            selected = {s: (concepts_dir / f"{s}.md").read_text() for s in valid_slugs}

            # (3) SYNTHESIZE
            try:
                resp = call_claude_json(
                    build_synth_prompt(ctx["schema"], compact, selected, source_path.name, source_text),
                    model=synth_model,
                )
            except Exception as exc:  # noqa: BLE001
                print(f"  synthesis failed ({exc}); skipping", file=sys.stderr)
                with failures_path.open("a", encoding="utf-8") as fh:
                    fh.write(source_path.name + "\n")
                continue

            # (4) VALIDATE paths, WRITE, record gaps + new-slug flags
            valid_files = []
            for f in resp.get("files", []):
                try:
                    safe_write_path(base_dir, f["path"], concepts_dir)
                    valid_files.append(f)
                except (ValueError, KeyError) as exc:
                    print(f"  rejected unsafe path ({exc})", file=sys.stderr)
            write_wiki_files(valid_files, base_dir)

            out_slugs = {Path(f["path"]).stem for f in valid_files}
            new_slugs = [s for s in out_slugs if s not in selected]
            if new_slugs:
                append_gap_log(gap_path, source_path.name, new_slugs, kind="new_slug")
            gaps = resp.get("gaps") or []
            if gaps:
                append_gap_log(gap_path, source_path.name, gaps, kind="gap")

            append_log_entry(wiki_dir / "log.md", resp["log_entry"])
            print(f"  {resp['summary']}")
            _try_reindex(wiki_dir, base_dir, label=f"{i}/{total}")


def cmd_reindex(args, wiki_dir: Path = Path("wiki"), base_dir: Path = Path(".")):
    init_wiki(wiki_dir)
    print(reindex(wiki_dir, base_dir))


def cmd_query(args, wiki_dir: Path = Path("wiki")):
    ctx = read_wiki_context(wiki_dir)
    prompt = build_query_prompt(ctx["schema"], ctx["index"], ctx["concepts"], args.question)
    answer = call_claude(prompt)
    print(answer)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    append_log_entry(wiki_dir / "log.md", f"{timestamp} | query | {args.question[:80]}")


def cmd_lint(args, wiki_dir: Path = Path("wiki")):
    ctx = read_wiki_context(wiki_dir)
    prompt = build_lint_prompt(ctx["schema"], ctx["index"], ctx["concepts"])
    report = call_claude(prompt)
    print(report)


def main():
    parser = argparse.ArgumentParser(
        description="LLM Wiki — Agentic AI & Claude Code knowledge base",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n  python wiki.py ingest\n  python wiki.py query 'What is harness engineering?'\n  python wiki.py lint",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("ingest", help="Ingest source docs into the wiki")
    p.add_argument("source", nargs="?", metavar="FILE", help="Specific *.md file; defaults to all")
    p.add_argument("--model", default=None, help="Model for ingest calls (default: inherit CLI default)")
    p.set_defaults(func=cmd_ingest)

    p = sub.add_parser("reindex", help="Rebuild index.md deterministically from concept-page frontmatter")
    p.set_defaults(func=cmd_reindex)

    p = sub.add_parser("query", help="Ask a question against the wiki")
    p.add_argument("question", help="The question to ask")
    p.set_defaults(func=cmd_query)

    p = sub.add_parser("lint", help="Health-check the wiki for drift and orphans")
    p.set_defaults(func=cmd_lint)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
