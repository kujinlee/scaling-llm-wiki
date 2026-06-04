---
concept: Free Validation at Speed
category: Workflows & Methodology
summary: When generation runs at thousands of tokens per second, comprehensive validation — tests, lint, pre-commit hooks, diff review, browser QA — and automated refactoring cost effectively no time, so quality checks should run at every step rather than be rationed.
aliases: [validation is free, free validation, validation at every step, speed makes validation free, continuous validation, automated refactoring at speed]
related: ["[[fast-models-slow-developers]]", "[[auto-correction-loop]]", "[[self-verification-loop]]", "[[satisfaction-testing]]", "[[agent-tdd]]", "[[ai-garbage-collection]]", "[[surgical-change-discipline]]", "[[custom-eval-systems]]"]
sources: [fast-models-need-slow-developers-sarah-chieng-cerebras]
---

# Free Validation at Speed

Free validation at speed is the observation that hyper-fast inference inverts the economics of quality checking: when a model generates at ~1,200 tokens/second, running a full validation pass — test suites, linting, pre-commit hooks, diff reviews, browser-based QA — and even re-generating to fix what the pass flags no longer imposes a meaningful time cost. Validation that was once rationed because it slowed the loop becomes a step you can afford to run *everywhere*. The corollary is that the developer should integrate comprehensive checks at every step of the workflow rather than batching them at the end, and likewise fold automated refactoring (deleting unused imports, cleaning dead lines, standardizing function structure) into each task — because the cleanup, too, is now nearly free. It is the speed-era enabler of the corpus's verification disciplines: the same checks that `[[auto-correction-loop]]`, `[[agent-tdd]]`, and `[[satisfaction-testing]]` prescribe become continuously runnable rather than occasional.

## Key Mechanics

- **Speed collapses the cost of a check**: at high token throughput the wall-clock cost of generating *and* validating an increment approaches the cost of generating it alone, so the historical reason to skip or defer validation — it slows iteration — disappears.
- **Validate at every step, not at the end**: the prescription is to wire the full stack of checks (unit/integration tests, linters, pre-commit hooks, diff-size review, browser QA exercising the running app) into each workflow step, so defects are caught per-increment rather than discovered in a large unreviewed batch.
- **Automated refactoring as a free step**: because cleanup is cheap, continuous refactoring is run automatically after each task — removing unused imports, trimming unnecessary lines, normalizing structure — keeping the codebase clean as it grows rather than accumulating cruft, the speed-enabled counterpart to `[[ai-garbage-collection]]`.
- **Validation is the brake on technical debt**: in the `[[fast-models-slow-developers]]` framing, free validation is precisely what stops fast generation from mass-producing debt — the quality gate that converts the speed dividend into trustworthy output rather than more unverified code.

## How It Appears in the Corpus

The Sarah Chieng (Cerebras, "AI Engineer" channel) talk "Fast Models Need Slow Developers" states it directly: with 1,200 tokens/second generation, "validation is free," so developers should integrate comprehensive validation — test suites, linting, pre-commit hooks, diff reviews, browser-based QA — at every step of the workflow, since it no longer imposes a significant time cost. It pairs this with automated refactoring after each task, leveraging the same free speed for continuous code quality, and frames both as essential brakes on the technical debt that hyper-fast generation would otherwise create.

## Tensions & Tradeoffs

- **Free to run is not free to trust**: cheaper checks raise *how often* you validate, not *what* the validation captures — a green lint/test pass still only certifies what it measures, the "quality of the check bounds the trust" caveat of `[[self-verification-loop]]` and `[[custom-eval-systems]]`. Free validation removes the time excuse, not the coverage gap.
- **Cheap checks can encourage over-generation**: if validation is free, the temptation is to generate more and lean on the checks to sort it out — but unmodeled failure modes pass silently, so free validation must pair with the restraint of `[[surgical-change-discipline]]` rather than license unbounded output.
- **Browser/E2E checks are still the expensive, flaky tier**: even at high token speed, exercising the running app through `[[satisfaction-testing]]` is slower and more brittle than unit checks, so "free" applies most cleanly to the fast deterministic gates and only loosely to full end-to-end journeys.
- **Vantage caveat**: the "validation is free" claim is asserted from a vendor talk at a specific speed regime; the durable idea is that *faster generation lowers the marginal cost of checking enough to validate continuously*, not that validation literally costs nothing.
