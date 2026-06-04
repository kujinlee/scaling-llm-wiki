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
        assert "===WIKI-FILE:" in prompt
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
        # the output format template lists only the concepts/ path, not index.md
        template = prompt.split("===WIKI-FILE:", 1)[1].split("Rules:", 1)[0]
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
        (tmp_path / "raw").mkdir()
        for i in range(11):
            (tmp_path / "raw" / f"src{i:02d}.md").write_text(f"source {i}")

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
        (tmp_path / "raw").mkdir()
        for i in range(3):
            (tmp_path / "raw" / f"src{i}.md").write_text("body")

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

    def test_discovers_sources_only_in_raw_dir(self, tmp_path):
        # Sources live under raw/, not the project root. A stray root-level *.md
        # (e.g. README.md) must NOT be treated as a source.
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")
        (tmp_path / "README.md").write_text("# not a source")  # root-level, must be ignored
        (tmp_path / "raw").mkdir()
        (tmp_path / "raw" / "real-source.md").write_text("a real source")

        response = {
            "files": [{"path": "wiki/concepts/c.md", "content": "# C"}],
            "log_entry": "2026-06-03 12:00 | ingest | real-source",
            "summary": "ok",
        }
        args = MagicMock()
        args.source = None
        args.model = None

        with patch("wiki.call_claude", return_value=json.dumps(response)) as cc, \
                patch("wiki.reindex", return_value="reindexed"):
            wiki.cmd_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)

        # exactly one source ingested (raw/real-source.md), README.md ignored
        assert cc.call_count == 1
        assert "real-source" in cc.call_args_list[0][0][0]
        assert "not a source" not in cc.call_args_list[0][0][0]


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

    def test_summarize_skips_malformed_line(self, tmp_path):
        # FIX F: a corrupt JSONL line must be skipped, not crash the summary.
        gap = tmp_path / ".gap-log.jsonl"
        wiki.append_gap_log(gap, "a.md", ["x"], kind="gap")
        with gap.open("a", encoding="utf-8") as fh:
            fh.write("this is not json\n")
        out = wiki.summarize_gap_log(gap)
        assert "a.md" in out and "x" in out


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


class TestBuildSynthPrompt:
    def test_includes_schema_and_index_and_source(self):
        prompt = wiki.build_synth_prompt("MY_SCHEMA", "rag: grounds", {"rag": "full rag page"}, "t.md", "src body")
        assert "MY_SCHEMA" in prompt
        assert "rag: grounds" in prompt           # compact index for awareness
        assert "full rag page" in prompt          # selected page full content
        assert "src body" in prompt
        assert "t.md" in prompt

    def test_marks_none_selected(self):
        prompt = wiki.build_synth_prompt("s", "idx", {}, "t.md", "src")
        assert "none selected" in prompt.lower()

    def test_envelope_has_gaps_field(self):
        prompt = wiki.build_synth_prompt("s", "idx", {}, "t.md", "src")
        assert '"gaps"' in prompt
        assert "===WIKI-FILE:" in prompt

    def test_rule_omit_unchanged_pages(self):
        prompt = wiki.build_synth_prompt("s", "idx", {}, "t.md", "src")
        assert "OMIT" in prompt
        assert "gaps" in prompt

    def test_requires_category_vocabulary(self):
        prompt = wiki.build_synth_prompt("s", "idx", {}, "t.md", "src")
        assert "Memory & Knowledge Systems" in prompt

    def test_has_guard_line_and_english_rule(self):
        prompt = wiki.build_synth_prompt("s", "idx", {}, "t.md", "src")
        assert "IGNORE any session handoff" in prompt
        assert "English" in prompt


class TestCmdRouteIngest:
    def _setup(self, tmp_path, existing_pages=None):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")
        for slug, summary in (existing_pages or {}).items():
            (wiki_dir / "concepts" / f"{slug}.md").write_text(
                f"---\nconcept: {slug}\ncategory: Memory & Knowledge Systems\nsummary: {summary}\n---\n# {slug}\n"
            )
        src = tmp_path / "talk.md"
        src.write_text("a talk about RAG")
        args = MagicMock()
        args.source = str(src)
        args.router_model = None
        args.synth_model = None
        return wiki_dir, src, args

    def test_routes_then_synthesizes_and_writes(self, tmp_path):
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds answers"})
        router = json.dumps({"slugs": ["rag"], "rationale": "about RAG"})
        synth = json.dumps({
            "files": [{"path": "wiki/concepts/rag.md", "content": "# RAG updated"}],
            "log_entry": "2026-06-03 12:00 | route-ingest | rag updated",
            "summary": "updated rag",
            "gaps": [],
        })
        with patch("wiki.call_claude", side_effect=[router, synth]), \
                patch("wiki.reindex", return_value="reindexed"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert (wiki_dir / "concepts" / "rag.md").read_text() == "# RAG updated"
        assert "route-ingest | rag updated" in (wiki_dir / "log.md").read_text()

    def test_synth_only_receives_selected_pages(self, tmp_path):
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds", "mcp": "tool protocol"})
        router = json.dumps({"slugs": ["rag"], "rationale": "x"})
        synth = json.dumps({"files": [], "log_entry": "2026-06-03 12:00 | route-ingest | noop",
                            "summary": "s", "gaps": []})
        with patch("wiki.call_claude", side_effect=[router, synth]) as cc, \
                patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        synth_prompt = cc.call_args_list[1][0][0]      # 2nd call = synth
        assert "## Selected concept pages" in synth_prompt
        assert "rag" in synth_prompt
        # mcp page content not loaded into synthesis (only its compact-index line)
        assert "### Existing page: mcp" not in synth_prompt

    def test_filters_hallucinated_slug(self, tmp_path):
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds"})
        router = json.dumps({"slugs": ["rag", "does-not-exist"], "rationale": "x"})
        synth = json.dumps({"files": [], "log_entry": "2026-06-03 12:00 | route-ingest | n",
                            "summary": "s", "gaps": []})
        with patch("wiki.call_claude", side_effect=[router, synth]) as cc, \
                patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        synth_prompt = cc.call_args_list[1][0][0]
        assert "### Existing page: does-not-exist" not in synth_prompt

    def test_records_gaps_with_source(self, tmp_path):
        # A real gap is a corpus slug the synth saw in the compact index but was not
        # given the full page for. "context-engineering" exists on disk but is not
        # routed/selected, so synth flags it as a gap.
        wiki_dir, src, args = self._setup(
            tmp_path, {"rag": "grounds", "context-engineering": "shapes context"})
        router = json.dumps({"slugs": ["rag"], "rationale": "x"})
        synth = json.dumps({"files": [], "log_entry": "2026-06-03 12:00 | route-ingest | n",
                            "summary": "s", "gaps": ["context-engineering"]})
        with patch("wiki.call_claude", side_effect=[router, synth]), \
                patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        rec = json.loads((wiki_dir / wiki.GAP_LOG_NAME).read_text().strip())
        assert rec["kind"] == "gap"
        assert rec["source"] == "talk.md"
        assert rec["slugs"] == ["context-engineering"]

    def test_flags_output_slug_not_in_router_input(self, tmp_path):
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds"})
        router = json.dumps({"slugs": ["rag"], "rationale": "x"})
        synth = json.dumps({
            "files": [{"path": "wiki/concepts/brand-new.md", "content": "# New"}],
            "log_entry": "2026-06-03 12:00 | route-ingest | new", "summary": "s", "gaps": [],
        })
        with patch("wiki.call_claude", side_effect=[router, synth]), \
                patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        recs = [json.loads(l) for l in (wiki_dir / wiki.GAP_LOG_NAME).read_text().splitlines() if l.strip()]
        assert any(r["kind"] == "new_slug" and r["slugs"] == ["brand-new"] for r in recs)
        assert (wiki_dir / "concepts" / "brand-new.md").exists()   # still written

    def test_rejects_traversal_path(self, tmp_path):
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds"})
        router = json.dumps({"slugs": ["rag"], "rationale": "x"})
        synth = json.dumps({
            "files": [{"path": "wiki/concepts/../../evil.md", "content": "pwned"}],
            "log_entry": "2026-06-03 12:00 | route-ingest | n", "summary": "s", "gaps": [],
        })
        with patch("wiki.call_claude", side_effect=[router, synth]), \
                patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert not (tmp_path / "evil.md").exists()

    def test_router_failure_skips_source_and_logs(self, tmp_path):
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds"})
        with patch("wiki.call_claude", side_effect=subprocess.CalledProcessError(1, "claude")), \
                patch("wiki.time.sleep"), patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert "talk.md" in (wiki_dir / wiki.ROUTE_FAILURES_NAME).read_text()

    def test_exits_if_claude_md_missing(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        src = tmp_path / "talk.md"
        src.write_text("body")
        args = MagicMock()
        args.source = str(src)
        args.router_model = None
        args.synth_model = None
        with pytest.raises(SystemExit):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)

    def test_slug_cap_limits_selected_pages(self, tmp_path, capsys):
        # FIX G: when the router returns more than SLUG_CAP existing slugs, only
        # SLUG_CAP pages are loaded into the synthesis prompt, and a "capped"
        # message is emitted to stderr.
        n = wiki.SLUG_CAP + 5
        pages = {f"concept-{i:02d}": f"summary {i}" for i in range(n)}
        wiki_dir, src, args = self._setup(tmp_path, pages)
        router = json.dumps({"slugs": sorted(pages), "rationale": "x"})
        synth = json.dumps({"files": [], "log_entry": "2026-06-03 12:00 | route-ingest | n",
                            "summary": "s", "gaps": []})
        with patch("wiki.call_claude", side_effect=[router, synth]) as cc, \
                patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        synth_prompt = cc.call_args_list[1][0][0]
        # build_synth_prompt emits one "### Existing page: " heading per selected page
        assert synth_prompt.count("### Existing page: ") == wiki.SLUG_CAP
        assert "capped" in capsys.readouterr().err

    def test_missing_source_path_skips_without_traceback(self, tmp_path):
        # FIX E: a nonexistent source path must not raise — warn, record in the
        # failures file, and continue.
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds"})
        args.source = str(tmp_path / "does-not-exist.md")
        with patch("wiki.call_claude", side_effect=[]), patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert "does-not-exist.md" in (wiki_dir / wiki.ROUTE_FAILURES_NAME).read_text()

    def test_non_list_gaps_does_not_crash_or_log(self, tmp_path):
        # FIX D: synth returns a string for "gaps" instead of a list — no crash,
        # no gap record written.
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds"})
        router = json.dumps({"slugs": ["rag"], "rationale": "x"})
        synth = json.dumps({"files": [], "log_entry": "2026-06-03 12:00 | route-ingest | n",
                            "summary": "s", "gaps": "context-engineering"})
        with patch("wiki.call_claude", side_effect=[router, synth]), \
                patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        gap_file = wiki_dir / wiki.GAP_LOG_NAME
        recs = ([json.loads(l) for l in gap_file.read_text().splitlines() if l.strip()]
                if gap_file.exists() else [])
        assert not any(r["kind"] == "gap" for r in recs)

    def test_gap_slug_not_on_disk_is_dropped(self, tmp_path):
        # FIX D: a gap slug not present in the corpus is dropped, not logged.
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds"})
        router = json.dumps({"slugs": ["rag"], "rationale": "x"})
        synth = json.dumps({"files": [], "log_entry": "2026-06-03 12:00 | route-ingest | n",
                            "summary": "s", "gaps": ["context-engineering", "rag"]})
        with patch("wiki.call_claude", side_effect=[router, synth]), \
                patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        gap_file = wiki_dir / wiki.GAP_LOG_NAME
        recs = ([json.loads(l) for l in gap_file.read_text().splitlines() if l.strip()]
                if gap_file.exists() else [])
        gap_recs = [r for r in recs if r["kind"] == "gap"]
        # only the real corpus slug "rag" survives; "context-engineering" dropped
        assert gap_recs == [] or all("context-engineering" not in r["slugs"] for r in gap_recs)
        assert any(r["kind"] == "gap" and r["slugs"] == ["rag"] for r in gap_recs)

    def test_non_list_slugs_treated_as_empty(self, tmp_path):
        # FIX D: router returns a string for "slugs" — treated as empty, no crash.
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds"})
        router = json.dumps({"slugs": "rag", "rationale": "x"})
        synth = json.dumps({"files": [], "log_entry": "2026-06-03 12:00 | route-ingest | n",
                            "summary": "s", "gaps": []})
        with patch("wiki.call_claude", side_effect=[router, synth]) as cc, \
                patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        synth_prompt = cc.call_args_list[1][0][0]
        # no page selected since slugs was not a list
        assert "### Existing page: rag" not in synth_prompt

    def test_synth_failure_records_router_slugs_as_gap(self, tmp_path):
        # FIX A: a synthesis failure must not lose the router's already-selected
        # slugs — they are recorded as a kind="gap" record so resolve-gaps can retry.
        wiki_dir, src, args = self._setup(tmp_path, {"rag": "grounds"})
        router = json.dumps({"slugs": ["rag"], "rationale": "x"})
        with patch("wiki.call_claude",
                   side_effect=[router, subprocess.CalledProcessError(1, "claude")]), \
                patch("wiki.time.sleep"), patch("wiki.reindex", return_value="r"):
            wiki.cmd_route_ingest(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        # source recorded in the failures file
        assert "talk.md" in (wiki_dir / wiki.ROUTE_FAILURES_NAME).read_text()
        # AND a gap record retains the router's selected slugs
        recs = [json.loads(l) for l in
                (wiki_dir / wiki.GAP_LOG_NAME).read_text().splitlines() if l.strip()]
        assert any(r["kind"] == "gap" and r["source"] == "talk.md"
                   and r["slugs"] == ["rag"] for r in recs)


class TestCmdResolveGaps:
    def _setup(self, tmp_path):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        (wiki_dir / "log.md").write_text("# Log\n\n")
        (wiki_dir / "concepts" / "context-engineering.md").write_text(
            "---\nconcept: ce\ncategory: Harness & Context Engineering\nsummary: s\n---\n# ce\n"
        )
        (tmp_path / "raw").mkdir()
        (tmp_path / "raw" / "talk.md").write_text("source body about context engineering")
        args = MagicMock()
        args.synth_model = None
        return wiki_dir, args

    def test_resynthesizes_logged_gap_and_clears_it(self, tmp_path):
        wiki_dir, args = self._setup(tmp_path)
        gap_path = wiki_dir / wiki.GAP_LOG_NAME
        wiki.append_gap_log(gap_path, "talk.md", ["context-engineering"], kind="gap")
        synth = json.dumps({
            "files": [{"path": "wiki/concepts/context-engineering.md", "content": "# ce resolved"}],
            "log_entry": "2026-06-03 12:00 | resolve-gaps | ce", "summary": "resolved", "gaps": [],
        })
        with patch("wiki.call_claude", side_effect=[synth]), patch("wiki.reindex", return_value="r"):
            wiki.cmd_resolve_gaps(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert (wiki_dir / "concepts" / "context-engineering.md").read_text() == "# ce resolved"
        # the gap record is removed after resolution
        remaining = gap_path.read_text().strip()
        assert "context-engineering" not in remaining

    def test_keeps_new_slug_records(self, tmp_path):
        wiki_dir, args = self._setup(tmp_path)
        gap_path = wiki_dir / wiki.GAP_LOG_NAME
        wiki.append_gap_log(gap_path, "talk.md", ["brand-new"], kind="new_slug")
        with patch("wiki.call_claude", side_effect=[]), patch("wiki.reindex", return_value="r"):
            wiki.cmd_resolve_gaps(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        # new_slug records are not 'gaps' to resynthesize; they stay for lint review
        assert "brand-new" in gap_path.read_text()

    def test_no_gap_log_is_noop(self, tmp_path, capsys):
        wiki_dir, args = self._setup(tmp_path)
        with patch("wiki.call_claude", side_effect=[]):
            wiki.cmd_resolve_gaps(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        assert "no gaps" in capsys.readouterr().out.lower()

    def test_resolve_drops_gap_keeps_new_slug(self, tmp_path):
        wiki_dir, args = self._setup(tmp_path)
        gap_path = wiki_dir / wiki.GAP_LOG_NAME
        wiki.append_gap_log(gap_path, "talk.md", ["context-engineering"], kind="gap")
        wiki.append_gap_log(gap_path, "talk.md", ["brand-new"], kind="new_slug")
        synth = json.dumps({
            "files": [{"path": "wiki/concepts/context-engineering.md", "content": "# ce resolved"}],
            "log_entry": "2026-06-03 12:00 | resolve-gaps | ce", "summary": "resolved", "gaps": [],
        })
        with patch("wiki.call_claude", side_effect=[synth]), patch("wiki.reindex", return_value="r"):
            wiki.cmd_resolve_gaps(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        remaining = gap_path.read_text()
        assert "context-engineering" not in remaining   # resolved gap dropped
        assert "brand-new" in remaining                 # new_slug retained


    def test_resolve_emits_new_slug_record(self, tmp_path):
        # FIX C: when resolve synthesis emits a page slug that was not among the
        # selected (router-input) slugs, a kind="new_slug" record must be written
        # AND survive the gap-log rewrite, while the resolved kind="gap" is dropped.
        wiki_dir, args = self._setup(tmp_path)
        gap_path = wiki_dir / wiki.GAP_LOG_NAME
        wiki.append_gap_log(gap_path, "talk.md", ["context-engineering"], kind="gap")
        synth = json.dumps({
            "files": [
                {"path": "wiki/concepts/context-engineering.md", "content": "# ce resolved"},
                {"path": "wiki/concepts/brand-new.md", "content": "# New"},
            ],
            "log_entry": "2026-06-03 12:00 | resolve-gaps | ce",
            "summary": "resolved", "gaps": [],
        })
        with patch("wiki.call_claude", side_effect=[synth]), patch("wiki.reindex", return_value="r"):
            wiki.cmd_resolve_gaps(args, wiki_dir=wiki_dir, base_dir=tmp_path)
        recs = [json.loads(l) for l in gap_path.read_text().splitlines() if l.strip()]
        # resolved gap dropped
        assert not any(r["kind"] == "gap" for r in recs)
        # new_slug for the unexpected output page retained
        assert any(r["kind"] == "new_slug" and r["slugs"] == ["brand-new"] for r in recs)


class TestCmdLintGapReport:
    def test_lint_appends_gap_log_summary(self, tmp_path, capsys):
        wiki_dir = tmp_path / "wiki"
        (wiki_dir / "concepts").mkdir(parents=True)
        (wiki_dir / "CLAUDE.md").write_text("schema")
        (wiki_dir / "index.md").write_text("# Index")
        wiki.append_gap_log(wiki_dir / wiki.GAP_LOG_NAME, "talk.md", ["context-engineering"], kind="gap")
        args = MagicMock()
        with patch("wiki.call_claude", return_value="All items OK."):
            wiki.cmd_lint(args, wiki_dir=wiki_dir)
        out = capsys.readouterr().out
        assert "All items OK." in out
        assert "context-engineering" in out   # gap-log summary appended


class TestArgparseWiring:
    def test_route_ingest_parses_and_dispatches(self):
        parser_args = ["route-ingest", "talk.md", "--router-model", "haiku", "--synth-model", "sonnet"]
        with patch.object(sys, "argv", ["wiki.py"] + parser_args), \
                patch("wiki.cmd_route_ingest") as mock_cmd:
            wiki.main()
        assert mock_cmd.called
        ns = mock_cmd.call_args[0][0]
        assert ns.source == "talk.md"
        assert ns.router_model == "haiku"
        assert ns.synth_model == "sonnet"

    def test_route_ingest_source_optional(self):
        with patch.object(sys, "argv", ["wiki.py", "route-ingest"]), \
                patch("wiki.cmd_route_ingest") as mock_cmd:
            wiki.main()
        assert mock_cmd.call_args[0][0].source is None

    def test_resolve_gaps_dispatches(self):
        with patch.object(sys, "argv", ["wiki.py", "resolve-gaps"]), \
                patch("wiki.cmd_resolve_gaps") as mock_cmd:
            wiki.main()
        assert mock_cmd.called


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
        assert out["gaps"] == []

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
        text = (
            '{"log_entry": "l", "summary": "s", "gaps": []}\n'
            "===WIKI-FILE: wiki/concepts/rag.md===\n"
            "\n# RAG\n\nmid\n\n"
        )
        out = wiki.parse_synthesis_response(text)
        assert out["files"][0]["content"] == "\n# RAG\n\nmid\n"

    def test_total_garbage_raises(self):
        with pytest.raises(ValueError):
            wiki.parse_synthesis_response("not json and no sentinel at all")


class TestOutputFormatInstructions:
    def test_synth_prompt_uses_sentinel_format(self):
        p = wiki.build_synth_prompt("schema", "idx", {"rag": "# RAG"}, "src.md", "body")
        assert "===WIKI-FILE:" in p
        assert "NO escaping" in p
        assert "column 0" in p
        assert "wiki/concepts/<kebab-case-name>.md" in p
        assert '"gaps"' in p
        assert '"content": "<full page markdown>"' not in p

    def test_ingest_prompt_uses_sentinel_format_without_gaps(self):
        p = wiki.build_ingest_prompt("schema", "idx", {}, "src.md", "body")
        assert "===WIKI-FILE:" in p
        assert "NO escaping" in p
        assert '"gaps"' not in p
        assert '"content": "<full page markdown>"' not in p


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
