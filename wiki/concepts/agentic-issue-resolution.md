---
concept: Agentic Issue Resolution
category: Workflows & Methodology
summary: End-to-end workflow where an agent reproduces a filed bug, writes a fix with regression tests that fail on the old code and pass on the fix, then opens a PR automatically.
aliases: [automated issue reproduction, auto-fix bot, agentic bug fixing]
related: ["[[self-verification-loop]]", "[[multi-agent-code-review]]", "[[claude-md]]", "[[engineering-taste]]", "[[deterministic-workflow-orchestration]]", "[[dark-factory]]", "[[harness-debugging]]"]
sources: [live-coding-session-with-boris-cherny-and-jarred-sumner, the-ai-dark-factory-is-alive-a-codebase-that-writes-its-own-, live-coding-session-with-boris-cherny-and-jarred-sumner-deep-dive]
---

# Agentic Issue Resolution

Agentic issue resolution is an end-to-end workflow in which an AI agent takes a newly filed bug report, reproduces it, writes a fix, and opens a pull request — with no human in the loop until review. The defining quality gate is a regression test that demonstrably fails on the old code and passes on the fix, providing machine-checkable proof that the reported problem is actually solved.

## Key Mechanics

- On a new issue, the agent first attempts to *reproduce* the bug; reproduction is the entry condition for everything downstream.
- If reproduction succeeds, the agent generates a PR containing both a fix and tests.
- Validity gate: the new tests must fail on the previous version and pass on the fix branch — turning "is this fixed?" into a verifiable, automatable check (a form of `[[self-verification-loop]]`).
- The same pipeline can handle feature requests, transforming a request directly into a PR.
- Reproduction can itself be a dedicated workflow: classify the issue by area (web UI, API, CLI, database), gather context, start the necessary services, and attempt to replicate the report — separating genuine bugs from user error before any fix is attempted.

## How It Appears in the Corpus

In the Boris Cherny and Jarred Sumner session, Bun's "Robbun" agent uses this loop and has become a major contributor to the codebase, auto-producing fix-and-test PRs for incoming GitHub issues. The deep-dive analysis details the closed-loop mechanics: a new GitHub issue triggers a webhook that spins up the RoboBun agent in its own container, which ingests `[[claude-md]]` for build/test/layout context, reproduces the issue, writes a test that must fail on `main`, develops a fix until the test passes, and submits the PR — which then enters an automated `[[multi-agent-code-review]]` loop (RoboBun resolving comments from Code Rabbit and a Claude reviewer) before any human sees it.

The Cole Medin "AI Dark Factory is ALIVE" live stream shows the pattern applied *reflexively* to maintain an open-source tool's own backlog: the presenter builds an Archon workflow *for the Archon repository itself* that automatically reproduces reported GitHub issues — classifying them (web UI / API / CLI / database), gathering context, starting services such as the Archon backend, and attempting to replicate the problem — so the maintainer gets early feedback distinguishing user error from real bugs. It is the reproduction front-half of issue resolution turned into a standing, self-maintaining workflow.

## Tensions & Tradeoffs

- Reproduction is the bottleneck: bugs that cannot be reproduced automatically fall outside the loop — which is precisely why the live-stream system makes reproduction its own classified, service-starting workflow rather than an implicit first step.
- Verification horizon: the failing-then-passing test gate is strong but cannot catch everything — performance regressions, subtle security vulnerabilities, or UX changes not captured by tests slip through, which is why merge trust still requires human judgment.
- High setup and compute cost: the closed loop is not out-of-the-box — it requires a robust containerized environment, CI/CD plumbing, and a comprehensive `[[claude-md]]`, and running an agent per issue is resource-intensive (the cost moves from developer time to compute, see `[[shifting-bottlenecks]]`).
- Merge trust: even with passing regression tests, the corpus notes that fully automated merges of complex changes still require deeper verification — see `[[shifting-bottlenecks]]` and `[[engineering-taste]]`. When this loop runs inside a `[[dark-factory]]`, its trust is only as good as a validation gate that does not *fail open* (`[[harness-debugging]]`).
