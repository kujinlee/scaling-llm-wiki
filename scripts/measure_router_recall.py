#!/usr/bin/env python3
"""Measure router recall against `sources:` ground truth (spec §8).

For each raw source cited by at least one concept page, the set of pages whose
`sources:` contains it is the answer key. Run the Haiku router and compare.

CAVEAT (survivorship, spec C3): only sources that SUCCEEDED in brute-force ingest
appear in any `sources:` list. The ~132 uncited sources (incl. failed ones) have
no key and are the hardest cases — this harness cannot score them. Treat the
aggregate number as necessary-but-not-sufficient and ALSO spot-check uncited
sources by hand.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import wiki

WIKI_DIR = Path("wiki")
BASE_DIR = Path(".")
SAMPLE = 20  # keyed sources to score


def is_korean(name: str) -> bool:
    return any("가" <= ch <= "힣" for ch in name)


def build_answer_key(concepts: dict) -> dict:
    """source-filename-stem -> set(slugs whose sources: contain it)."""
    key: dict[str, set] = {}
    for slug, content in concepts.items():
        fm = wiki.read_frontmatter(content)
        for src in wiki.parse_frontmatter_list(fm.get("sources", "")):
            key.setdefault(src, set()).add(slug)
    return key


def main():
    ctx = wiki.read_wiki_context(WIKI_DIR)
    compact = wiki.build_compact_index(ctx["concepts"])
    key = build_answer_key(ctx["concepts"])
    keyed = sorted(key)[:SAMPLE]

    rows = []
    for src_stem in keyed:
        source_file = BASE_DIR / wiki.RAW_DIR_NAME / f"{src_stem}.md"
        if not source_file.exists():
            continue
        routed = wiki.call_claude_json(
            wiki.build_router_prompt(compact, source_file.name, source_file.read_text()),
            model=wiki.ROUTER_MODEL,
        )
        predicted = set(routed.get("slugs", []))
        truth = key[src_stem]
        recall = len(predicted & truth) / len(truth) if truth else 1.0
        precision = len(predicted & truth) / len(predicted) if predicted else 0.0
        rows.append((src_stem, is_korean(src_stem), recall, precision))
        print(f"{'KO' if is_korean(src_stem) else 'EN'}  r={recall:.2f} p={precision:.2f}  {src_stem[:50]}")

    def avg(items):
        return sum(items) / len(items) if items else 0.0

    ko = [r for _, k, r, _ in rows if k]
    en = [r for _, k, r, _ in rows if not k]
    floor = min((r for _, _, r, _ in rows), default=0.0)
    print("\n=== SUMMARY ===")
    print(f"keyed sources scored: {len(rows)}  (of {len(key)} keyed; "
          f"~132 uncited sources NOT covered — spot-check by hand)")
    print(f"aggregate recall: {avg([r for _, _, r, _ in rows]):.2f}")
    print(f"KO recall: {avg(ko):.2f}   EN recall: {avg(en):.2f}")
    print(f"per-source recall floor: {floor:.2f}  (gate: no source < 0.50)")
    print("GATE: ship if aggregate>=0.90 AND floor>=0.50 AND KO~=EN; "
          "else enrich index / upgrade router / bring embeddings forward")


if __name__ == "__main__":
    main()
