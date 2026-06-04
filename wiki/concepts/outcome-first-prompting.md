---
concept: Outcome-First Prompting
category: Workflows & Methodology
summary: Directing a file- and tool-capable agent by defining the end result, constraints, and quality bar — rather than choreographing the steps — because the agent delivers finished artifacts, not a chat reply you refine in place.
aliases: [Outcome-First Prompting Style, Result-First Prompting]
related: [plan-first-workflow, aspirational-prompting, collaborative-prompt-elicitation, permission-tiering, exploratory-spec-discovery]
sources: [learn-80-of-claude-cowork-in-under-20-minutes, 한글자막-현재-codex-에서-제일-핫한-기능-goal]
---

# Outcome-First Prompting

Outcome-first prompting describes *what success looks like* — the end result, its
constraints, and the quality bar — and lets the agent decide how to get there, instead
of dictating a step-by-step procedure. The distinction is sharpest with agents that act
on your environment: Claude Cowork writes finished files directly into your folders
rather than returning a response you iterate on in a chat window, so there is no cheap
in-place correction loop. That shifts the burden up front — you must specify the
*outcome* well, because the agent commits to artifacts based on it. This is the
"outcome-first" style Cowork demands, contrasted with Claude Chat's "task-first,"
step-by-step approach.

## Key Mechanics

- **Specify result, constraints, and quality bar.** Instead of "do step 1, then step 2,"
  state the deliverable, the boundaries it must respect, and what "good" means. The agent
  plans the steps to satisfy that definition.
- **Driven by the artifact-delivery model.** Because the agent produces ready-to-use
  files (a formatted spreadsheet, an editable deck) rather than a chat answer, the
  prompt must encode acceptance criteria the agent can build against — there is no
  turn-by-turn nudging once it writes to disk.
- **Pair it with guardrails.** Defining outcomes for an agent that touches your
  filesystem goes hand in hand with [[permission-tiering]] — e.g. Cowork guardrails that
  block unconfirmed file changes — so autonomy toward the outcome stays bounded.
- **Sharpen vague aims first.** An underspecified outcome ("make this better") gives the
  agent no exit condition; refine fuzzy goals into concrete, checkable ones, often via
  [[collaborative-prompt-elicitation]] before handing off.

## How It Appears in the Corpus

Introduced in Jeff Su's "Learn 80% of Claude Cowork in Under 20 Minutes"
(`learn-80-of-claude-cowork-in-under-20-minutes`), which frames the task-first vs.
outcome-first split as the core mindset shift when moving from Claude Chat to Cowork:
"define the end result, constraints, and quality" because Cowork delivers files, not
window responses. The same principle recurs in the Codex `/goal` tutorial
(`한글자막-현재-codex-에서-제일-핫한-기능-goal`), where a run is steered by a single
verifiable objective (e.g. "reduce P95 latency by 20%") and the agent iterates until the
metric is met — an outcome-first prompt whose result then feeds
[[exploratory-spec-discovery]]. It sits alongside [[plan-first-workflow]] (where the
agent first proposes a plan to satisfy the outcome) and [[aspirational-prompting]] (aiming
the agent at a high target rather than a rote instruction).

## Tensions & Tradeoffs

- **Up-front rigor replaces mid-stream correction.** The payoff — the agent produces a
  finished artifact autonomously — is also the cost: a poorly specified outcome yields a
  confidently wrong deliverable, and there is no cheap chat-style edit loop to catch it.
  Outcome-first prompting demands more care in *defining* success than task-first prompting.
- **Autonomy needs containment.** Granting an agent the latitude to choose its own steps
  toward an outcome is only safe with permission boundaries and confirmation gates around
  destructive or irreversible actions.
