# Corpus cleanup — 2026-06-08

Maintenance pass on the `raw/` corpus following the accidental parent-ingest incident
(see the front-end write-path fix in the app repo, commit `8b17efd`).

## Context

An earlier accidental ingest wrote the live playlist (141 videos) flat into the data
vault ROOT instead of `raw/`. That orphan corpus was quarantined to a sibling folder
`…-data/_orphan-parent-ingest/` (outside this git repo) pending a clean re-ingest.

## What this pass found

The "clean re-ingest" was effectively already complete — later backfill sessions had
regenerated the previously-missing artifacts. An **index→disk audit** of all
**236** records in `raw/playlist-index.json` found exactly **one** genuinely-missing
artifact:

- `ixA6FG099uM` — *AI가 못 이기는 일은 따로 있다 — a16z 분석 4가지 방어선* — its `.md`
  existed but the summary PDF file was absent.

## Actions

1. **Regenerated the one missing PDF** from its existing `.md` via a throwaway
   `md-to-pdf` render (same CSS as the app's `lib/pdf.ts`; no LLM call, no `.md`
   mutation). PDFs are gitignored here, so this is not a tracked change. Re-audit after:
   **0 gaps** across all 236 records × {summaryMd, summaryPdf, deepDiveMd, deepDivePdf}.

2. **Deleted the quarantine folder** `…-data/_orphan-parent-ingest/` (19 MB), but only
   after proving the deletion was lossless: every one of the 141 quarantine `.md` files
   carried a `video_id` already present in the `raw/` index. A naive filename comparison
   falsely flagged ~5 files as "unique" — they were the same videos under **drifted
   slugs** (the orphan ingest and the canonical ingest slug a title differently). The
   lesson recorded for future cleanups: **reconcile corpus identity by `video_id`, never
   by filename.**

## Result

`raw/` is the single canonical corpus, fully consistent index↔disk. This commit also
syncs the accumulated corpus `.md` files and the grown `playlist-index.json` that prior
ingest/backfill sessions had left untracked.
