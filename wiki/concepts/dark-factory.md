---
concept: Dark Factory
category: Skills, Plugins & Automation
summary: A fully autonomous AI coding system that triages, implements, tests, and ships code with no human review before merge, relying entirely on governance documents and an independent validation gate.
aliases: [dark factory, lights-out software development, autonomous code factory, fully autonomous coding, level 5 coding autonomy, self-shipping codebase]
related: ["[[agentic-capability-ladder]]", "[[deterministic-workflow-orchestration]]", "[[governance-layer]]", "[[holdout-validation]]", "[[satisfaction-testing]]", "[[agent-as-infrastructure]]", "[[self-verification-loop]]", "[[graduated-autonomy]]", "[[harness-engineering]]", "[[harness-debugging]]"]
sources: [i-m-building-an-ai-dark-factory-that-ships-its-own-code-publ, the-ai-dark-factory-is-alive-a-codebase-that-writes-its-own-]
---

# Dark Factory

A dark factory is a fully autonomous AI coding system that owns an entire codebase lifecycle — triaging issues, planning, implementing, testing, fixing bugs, and shipping to production — with no human review before merge. The name borrows from "lights-out" manufacturing: a plant that runs in the dark because no humans are on the floor. It is the top rung of a coding-autonomy ladder, and it inverts the human-in-the-loop assumption of safe production AI coding: rather than a human approving every plan and diff, trust is manufactured entirely by the system's own governance and validation machinery.

## Key Mechanics

- A self-driving-style autonomy ladder frames the progression: Level 0 "spicy autocomplete" (AI as smarter search; the human writes code) → Level 1 coding intern (boilerplate, like cruise control) → Level 2 junior developer (interactive pair programmer) → Level 3 human-in-the-loop developer (AI writes the majority, but a human reviews every plan and diff — the recommended bar for reliable production software today) → Level 4 harness (unattended overnight runs reviewed later, e.g. an agentic loop) → Level 5 dark factory (defines, writes, tests, fixes, and ships with no pre-merge human review).
- Three layers make autonomy safe enough to remove the human: a `[[governance-layer]]` of mission/rules/global-context files that constrains *what* gets built, a deterministic factory loop that structures *how* work flows, and an independent validation stage that decides *whether* a change ships.
- The factory loop is a continuous triage → implement → validate cycle built on Arkon (Cole Medin's open-source harness builder — the same Archon of `[[deterministic-workflow-orchestration]]`): a scheduled triage workflow classifies, prioritizes, and labels incoming GitHub issues; each accepted issue kicks off a parallel implement workflow (research → classify bug/feature → plan → implement → open PR); and a separate validation workflow gates the merge.
- Auto-merge is conditional, not unconditional: code is merged to main without human approval *only after* the independent validation stage passes, so the quality gate — not a person — is what authorizes production.
- Issues can originate from the factory itself (e.g. from regression testing), closing the loop so the system generates its own work — and the same machinery can be pointed reflexively at the tooling that runs it, e.g. an Archon workflow that reproduces and triages Archon's own GitHub issues.

## How It Appears in the Corpus

The Cole Medin "AI Dark Factory" public experiment builds exactly this system to develop an agentic, RAG-powered AI tutor with no human in the loop. It presents the five-level self-driving analogy for coding autonomy, names Level 5 the dark factory, and wires a triage-implement-validate loop with Arkon workflows, a three-file `[[governance-layer]]`, and a held-out validation stage (`[[holdout-validation]]`, `[[satisfaction-testing]]`) before direct-to-main merges.

The follow-up "AI Dark Factory is ALIVE" live stream runs that system in public on a VPS — building a RAG application over the presenter's own content — and shows the loop end to end: Claude Code auto-files GitHub issues for observed UI/UX problems, the factory periodically scans and triages them (priority, batching similar issues), assigns them to Archon workflows, and aims to reflect fixes live in the web UI within an hour or two. The stream's defining content is *failure and live correction*: the validation workflow couldn't start the app (missing `DATABASE_URL`) and its verdict was too permissive, so changes risked passing without a real end-to-end test — debugged on air as `[[harness-debugging]]`. It also begins a reflexive Archon-for-Archon workflow that reproduces reported issues to separate user error from real bugs.

## Tensions & Tradeoffs

- It is the autonomy frontier `[[graduated-autonomy]]` and `[[shifting-bottlenecks]]` point at: removing the pre-merge human is precisely the merge-trust step the rest of the corpus treats as not-yet-solved, so the dark factory is offered as an *experiment* in manufacturing that trust, not a proven default — the same source still recommends Level 3 (human-in-the-loop) for reliable production software.
- Trust rests entirely on the validation gate: with no human backstop, any blind spot in `[[holdout-validation]]` or `[[satisfaction-testing]]` ships straight to production, so the system is only as safe as its weakest verifier — the "quality of the check bounds the trust" caveat of `[[self-verification-loop]]` taken to its limit. The live stream sharpens this: a validation gate can *fail open* (its environment breaks, its E2E test never runs, yet a permissive verdict approves the change) — a `[[harness-debugging]]` failure mode that the gate must be hardened against by failing closed.
- It is a distinct ladder from the `[[agentic-capability-ladder]]`: that model stages an operator's *usage* of an assistant, while the dark factory stages how much *code-shipping authority* is delegated; both culminate in always-on `[[agent-as-infrastructure]]`.
- Maturity caveat: the flagship is an in-progress public experiment, and the live stream's on-air workflow debugging is direct evidence that the pattern is not yet reliable without an operator watching — reliability at scale is being tested in the open rather than demonstrated.
