---
concept: Usage Pattern Analysis
category: Workflows & Methodology
summary: Having the assistant audit the operator's own recent usage to surface effective patterns, anti-patterns, and tailored recommendations — a self-reflection loop for improving how the tool itself is used.
aliases: [usage pattern analysis, usage audit, usage insights, self-audit, productivity analysis, usage reflection, workflow self-review]
related: [compound-engineering, custom-eval-systems, ai-enablement-consulting, harness-engineering, assistant-personalization-layers, thinking-vs-understanding]
sources: [7-secret-prompts-that-make-claude-code-10x-better]
---

# Usage Pattern Analysis

Usage pattern analysis is the practice of turning the assistant's analytical capability back on *the operator's own behavior* — having it review a window of recent usage and report which patterns are effective, which are anti-patterns, and which specific commands, prompts, or features would improve the workflow. It reframes the human's *use of the tool* as itself an object to be measured and improved, closing a self-reflection loop: rather than only getting better at the work, the operator gets better at *directing the agent*. It is `[[compound-engineering]]` pointed at the user's practice instead of at the codebase — capturing learnings about how to wield the tool and feeding them back as concrete recommendations.

## Key Mechanics

- **Audit a recent window**: the assistant analyzes a bounded span of past activity (the corpus cites the last 30 days), giving the review enough history to detect habits rather than one-off choices.
- **Surface patterns and anti-patterns**: the output names what the operator does *well* and what they do *poorly*, making invisible workflow habits legible — a personalized reality check on how effectively the tool is being leveraged.
- **Tailored, actionable recommendations**: rather than generic tips, it suggests specific commands, prompts, or features matched to the operator's actual workflow, so the advice is grounded in observed behavior.
- **A periodic cadence**: framed as a recurring review (e.g. monthly), it is a standing self-improvement ritual rather than a one-time setup step — the operator-facing analogue of a scheduled consolidation or eval pass.

## How It Appears in the Corpus

The Sabrina Ramonov "7 Secret Prompts" tutorial presents an `/insights` command that analyzes the user's past 30 days of usage and generates a detailed report highlighting effective patterns, identifying anti-patterns, suggesting improvements, and recommending specific commands, prompts, or features tailored to the actual workflow — positioned as a monthly self-review that reveals how well the operator is leveraging the assistant and where more productivity is available.

## Tensions & Tradeoffs

- **Only as good as its criteria**: an automated review judges "effective" against whatever notion of good usage it encodes, so it can confidently flag a deliberate habit as an anti-pattern or miss a real one — the "quality of the check bounds the trust" caveat that `[[custom-eval-systems]]` raises, here applied to the operator rather than to product output.
- **Recommendation ≠ comprehension**: acting on suggested commands without understanding *why* they help produces surface-level adoption that does not transfer — the `[[thinking-vs-understanding]]` gap, since the value is in internalizing better practice, not in mechanically running new commands.
- **It is the self-service form of `[[ai-enablement-consulting]]`**: the same literacy-gap improvement an enablement consultant sells as a service, here delivered by the tool auditing its own usage — useful, but bounded to patterns the analyzer can observe and name, not the strategic judgment a human coach supplies.
- **Distinct from harness refinement**: `[[harness-engineering]]` and `[[compound-engineering]]` improve the *environment* the agent works in; usage pattern analysis improves the *operator's* technique for driving it — adjacent feedback loops on different subjects.
