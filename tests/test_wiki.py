import sys
from pathlib import Path
import json
import subprocess
import fcntl
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
import wiki


def test_wiki_module_imports():
    assert hasattr(wiki, "__file__")


class TestInitWiki:
    def test_creates_concepts_dir(self, tmp_path):
        wiki.init_wiki(tmp_path / "wiki")
        assert (tmp_path / "wiki" / "concepts").is_dir()

    def test_creates_log_md(self, tmp_path):
        wiki.init_wiki(tmp_path / "wiki")
        assert (tmp_path / "wiki" / "log.md").exists()

    def test_creates_index_md(self, tmp_path):
        wiki.init_wiki(tmp_path / "wiki")
        assert (tmp_path / "wiki" / "index.md").exists()

    def test_idempotent(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        wiki.init_wiki(wiki_dir)
        wiki.init_wiki(wiki_dir)
        assert (wiki_dir / "concepts").is_dir()

    def test_preserves_existing_log(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        (wiki_dir / "log.md").write_text("existing log content")
        wiki.init_wiki(wiki_dir)
        assert (wiki_dir / "log.md").read_text() == "existing log content"


class TestReadWikiContext:
    def test_empty_wiki_returns_empty_strings(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        ctx = wiki.read_wiki_context(wiki_dir)
        assert ctx == {"schema": "", "index": "", "concepts": {}}

    def test_reads_schema_and_index(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        (wiki_dir / "CLAUDE.md").write_text("the schema")
        (wiki_dir / "index.md").write_text("the index")
        ctx = wiki.read_wiki_context(wiki_dir)
        assert ctx["schema"] == "the schema"
        assert ctx["index"] == "the index"

    def test_reads_concept_pages(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "concepts" / "rag.md").write_text("rag content")
        (wiki_dir / "concepts" / "cot.md").write_text("cot content")
        ctx = wiki.read_wiki_context(wiki_dir)
        assert ctx["concepts"]["rag"] == "rag content"
        assert ctx["concepts"]["cot"] == "cot content"


class TestCallClaude:
    def test_calls_claude_print_with_stdin(self):
        mock_proc = MagicMock()
        mock_proc.stdout = "  response text  "
        with patch("subprocess.run", return_value=mock_proc) as mock_run:
            result = wiki.call_claude("my prompt")
        assert mock_run.call_args[0][0] == ["claude", "--print"]
        assert mock_run.call_args[1]["input"] == "my prompt"
        assert result == "response text"

    def test_raises_on_nonzero_exit_after_retries(self):
        with patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "claude")):
            with pytest.raises(subprocess.CalledProcessError):
                wiki.call_claude("prompt", retries=1)

    def test_retries_then_succeeds(self):
        ok = MagicMock()
        ok.stdout = "recovered"
        with patch("subprocess.run", side_effect=[subprocess.CalledProcessError(1, "claude"), ok]) as run, \
                patch("wiki.time.sleep") as sleep:
            result = wiki.call_claude("p", retries=3)
        assert result == "recovered"
        assert run.call_count == 2
        sleep.assert_called_once()

    def test_no_model_flag_by_default(self):
        mock_proc = MagicMock()
        mock_proc.stdout = "x"
        with patch("subprocess.run", return_value=mock_proc) as mock_run:
            wiki.call_claude("p")
        assert mock_run.call_args[0][0] == ["claude", "--print"]

    def test_appends_model_flag(self):
        mock_proc = MagicMock()
        mock_proc.stdout = "x"
        with patch("subprocess.run", return_value=mock_proc) as mock_run:
            wiki.call_claude("p", model="sonnet")
        assert mock_run.call_args[0][0] == ["claude", "--print", "--model", "sonnet"]


class TestCallClaudeJson:
    def test_retries_on_non_json_then_succeeds(self):
        good = json.dumps({"files": [], "log_entry": "x", "summary": "y"})
        with patch("wiki.call_claude", side_effect=["sorry, here is some prose", good]) as cc, \
                patch("wiki.time.sleep") as sleep:
            result = wiki.call_claude_json("p", retries=3)
        assert result["summary"] == "y"
        assert cc.call_count == 2
        sleep.assert_called_once()

    def test_raises_after_exhausting_retries(self):
        with patch("wiki.call_claude", return_value="not json at all"), patch("wiki.time.sleep"):
            with pytest.raises(ValueError):
                wiki.call_claude_json("p", retries=2)

    def test_passes_model_through(self):
        good = json.dumps({"files": [], "log_entry": "x", "summary": "y"})
        with patch("wiki.call_claude", return_value=good) as cc:
            wiki.call_claude_json("p", model="haiku")
        assert cc.call_args[1]["model"] == "haiku"


class TestExtractJson:
    def test_parses_direct_json(self):
        data = {"files": [], "log_entry": "x", "summary": "y"}
        assert wiki.extract_json(json.dumps(data)) == data

    def test_parses_json_in_code_fence(self):
        data = {"files": [], "log_entry": "x", "summary": "y"}
        text = f"Here it is:\n```json\n{json.dumps(data)}\n```"
        assert wiki.extract_json(text) == data

    def test_parses_json_embedded_in_prose(self):
        data = {"files": [], "log_entry": "x", "summary": "y"}
        text = f"Sure! {json.dumps(data)} Done."
        assert wiki.extract_json(text) == data

    def test_raises_on_no_json(self):
        with pytest.raises(ValueError, match="No valid JSON"):
            wiki.extract_json("plain text with no JSON at all")


class TestBuildIngestPrompt:
    def test_includes_source_content(self):
        prompt = wiki.build_ingest_prompt("schema", "index", {}, "src.md", "source text here")
        assert "source text here" in prompt

    def test_includes_source_filename(self):
        prompt = wiki.build_ingest_prompt("schema", "index", {}, "my-talk.md", "body")
        assert "my-talk.md" in prompt

    def test_includes_existing_concept(self):
        prompt = wiki.build_ingest_prompt("schema", "index", {"rag": "rag page text"}, "s.md", "src")
        assert "rag page text" in prompt

    def test_shows_none_yet_when_no_concepts(self):
        prompt = wiki.build_ingest_prompt("schema", "index", {}, "s.md", "src")
        assert "none yet" in prompt

    def test_instructs_json_response(self):
        prompt = wiki.build_ingest_prompt("schema", "index", {}, "s.md", "src")
        assert '"files"' in prompt
        assert '"log_entry"' in prompt
        assert '"summary"' in prompt

    def test_includes_schema(self):
        prompt = wiki.build_ingest_prompt("MY_SCHEMA_TEXT", "index", {}, "s.md", "src")
        assert "MY_SCHEMA_TEXT" in prompt

    def test_instructs_english_output(self):
        prompt = wiki.build_ingest_prompt("schema", "index", {}, "s.md", "src")
        assert "English" in prompt

    def test_instructs_no_index_emission(self):
        prompt = wiki.build_ingest_prompt("schema", "index", {}, "s.md", "src")
        assert "Do NOT emit wiki/index.md" in prompt
        # the JSON output template lists only the concepts/ path, not index.md
        template = prompt.split('"files"', 1)[1].split("Rules:", 1)[0]
        assert "wiki/concepts/" in template
        assert "wiki/index.md" not in template


    def test_requires_category_and_summary(self):
        prompt = wiki.build_ingest_prompt("schema", "index", {}, "s.md", "src")
        assert "category:" in prompt
        assert "summary:" in prompt
        # the controlled category vocabulary is injected
        assert "Memory & Knowledge Systems" in prompt


class TestReadFrontmatter:
    def test_parses_simple_keys(self):
        text = "---\nconcept: RAG\ncategory: Memory & Knowledge Systems\nsummary: grounds answers\n---\n\n# RAG\nbody"
        fm = wiki.read_frontmatter(text)
        assert fm["concept"] == "RAG"
        assert fm["category"] == "Memory & Knowledge Systems"
        assert fm["summary"] == "grounds answers"

    def test_returns_empty_without_frontmatter(self):
        assert wiki.read_frontmatter("# No frontmatter\nbody") == {}


class TestBuildIndex:
    def _page(self, concept, category, summary):
        return f"---\nconcept: {concept}\ncategory: {category}\nsummary: {summary}\n---\n\n# {concept}\n"

    def test_groups_by_category_in_order(self):
        concepts = {
            "tool-calling": self._page("Tool Calling", "Agent Architecture & Patterns", "invoke tools"),
            "pre-training": self._page("Pre-training", "LLM Internals & Training", "next-token prediction"),
        }
        index = wiki.build_index(concepts)
        # LLM Internals category comes before Agent Architecture per CATEGORY_ORDER
        assert index.index("LLM Internals & Training") < index.index("Agent Architecture & Patterns")
        assert "- [[tool-calling]] — invoke tools" in index
        assert "- [[pre-training]] — next-token prediction" in index

    def test_unknown_category_goes_to_uncategorized(self):
        concepts = {"weird": self._page("Weird", "Nonexistent Category", "huh")}
        index = wiki.build_index(concepts)
        assert "## Uncategorized" in index
        assert "- [[weird]] — huh" in index

    def test_summary_falls_back_to_concept_name(self):
        concepts = {"x": "---\nconcept: Ecks\ncategory: LLM Internals & Training\n---\n# Ecks\n"}
        index = wiki.build_index(concepts)
        assert "- [[x]] — Ecks" in index


class TestBuildQueryPrompt:
    def test_includes_question(self):
        prompt = wiki.build_query_prompt("schema", "index", {}, "What is a harness?")
        assert "What is a harness?" in prompt

    def test_includes_concept_pages(self):
        prompt = wiki.build_query_prompt("schema", "index", {"rag": "rag page content"}, "q")
        assert "rag page content" in prompt

    def test_mentions_citation_requirement(self):
        prompt = wiki.build_query_prompt("schema", "index", {}, "q")
        assert "[[" in prompt


class TestBuildLintPrompt:
    def test_includes_concept_file_list(self):
        prompt = wiki.build_lint_prompt("schema", "index", {"rag": "c", "cot": "c"})
        assert "rag" in prompt
        assert "cot" in prompt

    def test_includes_checklist_items(self):
        prompt = wiki.build_lint_prompt("schema", "index", {})
        assert "Orphan detection" in prompt
        assert "Reverse orphans" in prompt
        assert "Broken cross-references" in prompt


class TestWriteWikiFiles:
    def test_creates_files_at_correct_paths(self, tmp_path):
        files = [
            {"path": "wiki/concepts/rag.md", "content": "# RAG"},
            {"path": "wiki/index.md", "content": "# Index"},
        ]
        wiki.write_wiki_files(files, tmp_path)
        assert (tmp_path / "wiki/concepts/rag.md").read_text() == "# RAG"
        assert (tmp_path / "wiki/index.md").read_text() == "# Index"

    def test_creates_parent_directories(self, tmp_path):
        files = [{"path": "wiki/concepts/new/nested.md", "content": "content"}]
        wiki.write_wiki_files(files, tmp_path)
        assert (tmp_path / "wiki/concepts/new/nested.md").exists()


class TestAppendLogEntry:
    def test_creates_file_if_missing(self, tmp_path):
        log = tmp_path / "log.md"
        wiki.append_log_entry(log, "2026-06-02 12:00 | ingest | test")
        assert "2026-06-02 12:00 | ingest | test" in log.read_text()

    def test_appends_to_existing_content(self, tmp_path):
        log = tmp_path / "log.md"
        log.write_text("# Log\n\nfirst entry\n")
        wiki.append_log_entry(log, "second entry")
        content = log.read_text()
        assert "first entry" in content
        assert "second entry" in content

    def test_does_not_erase_prior_entries(self, tmp_path):
        log = tmp_path / "log.md"
        wiki.append_log_entry(log, "entry one")
        wiki.append_log_entry(log, "entry two")
        wiki.append_log_entry(log, "entry three")
        content = log.read_text()
        assert "entry one" in content
        assert "entry two" in content
        assert "entry three" in content


class TestCmdIngest:
    def test_writes_concept_file_and_updates_log(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")

        source = tmp_path / "some-talk.md"
        source.write_text("# A talk about harnesses")

        response = {
            "files": [{"path": "wiki/concepts/harness-engineering.md", "content": "# Harness"}],
            "log_entry": "2026-06-02 12:00 | ingest | some-talk: created harness-engineering",
            "summary": "Created harness-engineering page.",
        }

        args = MagicMock()
        args.source = str(source)
        args.model = None
        args.reindex_every = 5
        args.reindex_model = "sonnet"

        # Patch reindex so the test isolates ingest behavior (no second claude call).
        with patch("wiki.call_claude", return_value=json.dumps(response)), \
                patch("wiki.reindex", return_value="reindexed") as mock_reindex:
            wiki.cmd_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)

        assert (tmp_path / "wiki/concepts/harness-engineering.md").read_text() == "# Harness"
        assert "2026-06-02 12:00 | ingest" in (wiki_dir / "log.md").read_text()
        # a final reindex always runs after ingestion
        mock_reindex.assert_called_once()

    def test_exits_if_claude_md_missing(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        source = tmp_path / "some-talk.md"
        source.write_text("content")

        args = MagicMock()
        args.source = str(source)

        with pytest.raises(SystemExit):
            wiki.cmd_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)

    def test_reindexes_after_every_source(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")
        for i in range(11):
            (tmp_path / f"src{i:02d}.md").write_text(f"source {i}")

        response = {
            "files": [{"path": "wiki/concepts/c.md", "content": "# C"}],
            "log_entry": "2026-06-02 12:00 | ingest | c",
            "summary": "ok",
        }
        args = MagicMock()
        args.source = None
        args.model = None

        with patch("wiki.call_claude", return_value=json.dumps(response)), \
                patch("wiki.reindex", return_value="reindexed") as mock_reindex:
            wiki.cmd_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)

        # one reindex after each of the 11 sources
        assert mock_reindex.call_count == 11

    def test_continues_when_reindex_fails(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")
        for i in range(3):
            (tmp_path / f"src{i}.md").write_text("body")

        response = {
            "files": [{"path": "wiki/concepts/c.md", "content": "# C"}],
            "log_entry": "2026-06-02 12:00 | ingest | c",
            "summary": "ok",
        }
        args = MagicMock()
        args.source = None
        args.model = None
        args.reindex_every = 5
        args.reindex_model = "sonnet"

        # reindex always raises; cmd_ingest must NOT propagate it (pages are safe)
        with patch("wiki.call_claude", return_value=json.dumps(response)), \
                patch("wiki.reindex", side_effect=RuntimeError("rate limit")):
            wiki.cmd_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)

        # all 3 sources still ingested despite the failing reindex
        assert (tmp_path / "wiki/concepts/c.md").exists()
        assert (wiki_dir / "log.md").read_text().count("| ingest | c") == 3


class TestReindex:
    def test_writes_index_from_frontmatter_no_llm(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "log.md").write_text("# Log\n\n")
        (wiki_dir / "concepts" / "rag.md").write_text(
            "---\nconcept: RAG\ncategory: Memory & Knowledge Systems\nsummary: grounds answers\n---\n# RAG\n"
        )

        # reindex must be pure Python — if it tries to call claude, fail loudly
        with patch("wiki.call_claude", side_effect=AssertionError("reindex must not call claude")):
            summary = wiki.reindex(wiki_dir=wiki_dir, base_dir=tmp_path)

        index = (wiki_dir / "index.md").read_text()
        assert "## Memory & Knowledge Systems" in index
        assert "- [[rag]] — grounds answers" in index
        assert "reindex" in (wiki_dir / "log.md").read_text()
        assert "1 concepts across 1 categories" in summary


class TestCmdReindex:
    def test_prints_summary(self, tmp_path, capsys):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        args = MagicMock()
        with patch("wiki.reindex", return_value="rebuilt 42 concepts"):
            wiki.cmd_reindex(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert "rebuilt 42 concepts" in capsys.readouterr().out


class TestCmdQuery:
    def test_prints_answer_and_logs_question(self, tmp_path, capsys):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")

        args = MagicMock()
        args.question = "What is a harness?"

        with patch("wiki.call_claude", return_value="A harness is the agent's scaffolding.") as mock_claude:
            wiki.cmd_query(args, wiki_dir=wiki_dir)

        captured = capsys.readouterr()
        assert "A harness is the agent's scaffolding." in captured.out
        assert "What is a harness?" in (wiki_dir / "log.md").read_text()
        prompt = mock_claude.call_args[0][0]
        assert "What is a harness?" in prompt

    def test_question_included_in_prompt(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")

        args = MagicMock()
        args.question = "Explain MCP"

        with patch("wiki.call_claude", return_value="answer") as mock_claude:
            wiki.cmd_query(args, wiki_dir=wiki_dir)

        prompt = mock_claude.call_args[0][0]
        assert "Explain MCP" in prompt


class TestCmdLint:
    def test_prints_lint_report(self, tmp_path, capsys):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")

        args = MagicMock()

        with patch("wiki.call_claude", return_value="All items OK. Wiki is clean."):
            wiki.cmd_lint(args, wiki_dir=wiki_dir)

        assert "All items OK. Wiki is clean." in capsys.readouterr().out

    def test_passes_all_wiki_content_to_claude(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema text")
        (wiki_dir / "index.md").write_text("index text")
        (wiki_dir / "concepts" / "rag.md").write_text("rag page content")

        args = MagicMock()

        with patch("wiki.call_claude", return_value="OK") as mock_claude:
            wiki.cmd_lint(args, wiki_dir=wiki_dir)

        prompt = mock_claude.call_args[0][0]
        assert "rag page content" in prompt
        assert "schema text" in prompt


class TestParseFrontmatterList:
    def test_parses_bracketed_csv(self):
        assert wiki.parse_frontmatter_list("[rag, chain-of-thought, mcp]") == ["rag", "chain-of-thought", "mcp"]

    def test_strips_quotes(self):
        assert wiki.parse_frontmatter_list("['a', \"b\"]") == ["a", "b"]

    def test_handles_korean_items(self):
        assert wiki.parse_frontmatter_list("[하네스, harness-engineering]") == ["하네스", "harness-engineering"]

    def test_empty_string_returns_empty_list(self):
        assert wiki.parse_frontmatter_list("") == []
        assert wiki.parse_frontmatter_list("[]") == []

    def test_unbracketed_single_value(self):
        assert wiki.parse_frontmatter_list("solo") == ["solo"]


class TestBuildCompactIndex:
    def _page(self, concept, summary, aliases=None):
        a = f"\naliases: [{', '.join(aliases)}]" if aliases else ""
        return f"---\nconcept: {concept}\ncategory: Memory & Knowledge Systems\nsummary: {summary}{a}\n---\n# {concept}\n"

    def test_one_line_per_page_slug_and_summary(self):
        concepts = {"rag": self._page("RAG", "grounds answers in retrieved text")}
        out = wiki.build_compact_index(concepts)
        assert "rag: grounds answers in retrieved text" in out

    def test_includes_aliases_when_present(self):
        concepts = {"rag": self._page("RAG", "grounds answers", aliases=["retrieval-augmented-generation", "검색증강"])}
        out = wiki.build_compact_index(concepts)
        assert "retrieval-augmented-generation" in out
        assert "검색증강" in out

    def test_falls_back_to_concept_name_without_summary(self):
        concepts = {"x": "---\nconcept: Ecks\ncategory: LLM Internals & Training\n---\n# Ecks\n"}
        out = wiki.build_compact_index(concepts)
        assert "x: Ecks" in out

    def test_empty_corpus_marker(self):
        assert wiki.build_compact_index({}) == "(none yet)"

    def test_sorted_by_slug(self):
        concepts = {
            "zeta": self._page("Zeta", "z"),
            "alpha": self._page("Alpha", "a"),
        }
        out = wiki.build_compact_index(concepts)
        assert out.index("alpha:") < out.index("zeta:")


class TestSafeWritePath:
    def test_accepts_path_under_concepts(self, tmp_path):
        restrict = tmp_path / "wiki" / "concepts"
        result = wiki.safe_write_path(tmp_path, "wiki/concepts/rag.md", restrict)
        assert result == (tmp_path / "wiki/concepts/rag.md").resolve()

    def test_rejects_traversal(self, tmp_path):
        restrict = tmp_path / "wiki" / "concepts"
        with pytest.raises(ValueError):
            wiki.safe_write_path(tmp_path, "wiki/concepts/../../wiki.py", restrict)

    def test_rejects_sibling_wiki_file(self, tmp_path):
        restrict = tmp_path / "wiki" / "concepts"
        with pytest.raises(ValueError):
            wiki.safe_write_path(tmp_path, "wiki/CLAUDE.md", restrict)


class TestGapLog:
    def test_append_writes_jsonl_record(self, tmp_path):
        gap = tmp_path / ".gap-log.jsonl"
        wiki.append_gap_log(gap, "some-talk.md", ["context-engineering"], kind="gap")
        line = gap.read_text().strip()
        rec = json.loads(line)
        assert rec["source"] == "some-talk.md"
        assert rec["slugs"] == ["context-engineering"]
        assert rec["kind"] == "gap"
        assert "ts" in rec

    def test_append_is_additive(self, tmp_path):
        gap = tmp_path / ".gap-log.jsonl"
        wiki.append_gap_log(gap, "a.md", ["x"], kind="gap")
        wiki.append_gap_log(gap, "b.md", ["y"], kind="new_slug")
        lines = [l for l in gap.read_text().splitlines() if l.strip()]
        assert len(lines) == 2

    def test_preserves_unicode_slugs(self, tmp_path):
        gap = tmp_path / ".gap-log.jsonl"
        wiki.append_gap_log(gap, "한글.md", ["하네스"], kind="gap")
        rec = json.loads(gap.read_text().strip())
        assert rec["slugs"] == ["하네스"]

    def test_summarize_empty_when_missing(self, tmp_path):
        assert "no gaps" in wiki.summarize_gap_log(tmp_path / ".gap-log.jsonl").lower()

    def test_summarize_lists_entries(self, tmp_path):
        gap = tmp_path / ".gap-log.jsonl"
        wiki.append_gap_log(gap, "a.md", ["x"], kind="gap")
        wiki.append_gap_log(gap, "b.md", ["y"], kind="new_slug")
        out = wiki.summarize_gap_log(gap)
        assert "a.md" in out and "x" in out
        assert "b.md" in out and "y" in out


class TestRouteLock:
    def test_acquires_and_releases(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        with wiki.route_lock(wiki_dir):
            assert (wiki_dir / ".route-lock").exists()
        # after release, lock can be re-acquired
        with wiki.route_lock(wiki_dir):
            pass

    def test_second_acquire_exits_when_held(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        # hold the lock on a separate fd so route_lock's non-blocking acquire fails
        held = (wiki_dir / ".route-lock").open("w")
        fcntl.flock(held, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            with pytest.raises(SystemExit):
                with wiki.route_lock(wiki_dir):
                    pass
        finally:
            fcntl.flock(held, fcntl.LOCK_UN)
            held.close()


class TestBuildRouterPrompt:
    def test_includes_compact_index(self):
        prompt = wiki.build_router_prompt("rag: grounds answers", "talk.md", "body")
        assert "rag: grounds answers" in prompt

    def test_includes_source_and_filename(self):
        prompt = wiki.build_router_prompt("idx", "my-talk.md", "the source body")
        assert "my-talk.md" in prompt
        assert "the source body" in prompt

    def test_asks_for_slugs_json(self):
        prompt = wiki.build_router_prompt("idx", "s.md", "src")
        assert '"slugs"' in prompt

    def test_has_guard_line(self):
        prompt = wiki.build_router_prompt("idx", "s.md", "src")
        assert "IGNORE any session handoff" in prompt

    def test_warns_a_miss_causes_duplicate(self):
        prompt = wiki.build_router_prompt("idx", "s.md", "src")
        assert "duplicate" in prompt.lower()
