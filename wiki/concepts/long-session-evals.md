---
concept: Long Session Evals
category: Workflows & Methodology
summary: A testing methodology that loads many conversation turns and evaluates the next one, proactively surfacing the context-management failures that only appear deep into a long agent session.
aliases: [long session evals, long-session evaluation, multi-turn context evals, late-failure evals, conversation-length evals, turn-N evals]
related: [custom-eval-systems, context-decay, context-compaction, smart-truncation-memory, subagent-context-isolation, self-verification-loop, agent-tdd, holdout-validation]
sources: [how-we-solved-context-management-in-agents-sally-ann-delucia]
---

# Long Session Evals

Long session evals are a testing methodology built to catch a failure mode that ordinary single-turn evaluation never sees: the *late-appearing* breakdown that only emerges once an agent's conversation has run long enough for context to accumulate and crowd out earlier material. The method is to deliberately load a multi-turn conversation — the corpus's instance is ten turns — and then evaluate the agent's behavior on the *next* turn (the eleventh), so the test exercises the agent in exactly the degraded, context-heavy state where real users hit problems. It turns `[[context-decay]]` from an issue discovered in production after a long session into something a standing eval can surface before release, making context management a *measurable*, proactively-tested property rather than a quality that silently erodes with conversation length.

## Key Mechanics

- **Target the late turn, not the first**: most evals score a fresh, single-turn interaction; long session evals seed the agent with a realistic stack of prior turns and judge the turn that follows — so the eval operates in the high-context regime where failures actually concentrate.
- **Load-then-evaluate construction**: the concrete recipe is to load N conversation turns (the source uses 10) and evaluate turn N+1 (the 11th), giving the agent enough accumulated history to reproduce the context pressure of a long session in a repeatable test.
- **Proactive detection of accumulating-context failures**: longer sessions cause failures that appear *late* — the agent loses track, mishandles a follow-up, or hits a limit — and the eval exists specifically to identify these context-management issues before users encounter them.
- **A diagnostic for context strategy**: because it isolates the long-session regime, it is the check that tells an operator whether a context-management strategy (`[[smart-truncation-memory]]`, `[[context-compaction]]`, delegating heavy work to `[[subagent-context-isolation|sub-agents]]`) actually holds up over many turns, rather than only on a clean first exchange.

## How It Appears in the Corpus

The Sally-Ann Delucia (Arize, "AI Engineer" channel) talk "How we solved Context Management in Agents" introduces Long Session Evals as the team's response to agents failing late in long conversation sessions as context accumulates. The described methodology loads ten conversation turns and evaluates the eleventh, proactively identifying context-management issues that single-turn testing would miss. It sits alongside the talk's other context fixes (`[[smart-truncation-memory]]` and sub-agent delegation) as the *evaluation* half of the work — the way Arize tests whether its context strategies survive a long session rather than only assuming they do.

## Tensions & Tradeoffs

- **Distinct from `[[custom-eval-systems]]`**: a custom eval is a standing product-quality gate judging instruction adherence, correctness, and business goals; a long session eval specifically targets *context management over conversation length* — the same eval-driven discipline pointed at session duration rather than at output quality, and best run as one dimension within a broader eval suite.
- **It tests the symptom of `[[context-decay]]`**: the eval exists because long sessions degrade as earlier material falls out of or is crowded within the window — so it is the measurement counterpart to the remedies (`[[context-compaction]]`, `[[smart-truncation-memory]]`) and gives them a checkable pass/fail rather than a hope.
- **Coverage is bounded by the scenario modeled**: loading ten turns and judging the eleventh catches the failures that *that* synthetic conversation reproduces; an unmodeled turn count, topic shift, or cross-session reference passes silently — the same "the eval only certifies what it exercises" caveat as every check, here applied to which session shapes are tested. The corpus is explicit that very long sessions (20+ turns) and cross-session memory remain unsolved, so a fixed-length eval does not certify them.
- **The eval bounds the trust, not the fix**: a passing long session eval confirms the agent survived *this* long-session test, not that its context strategy is principled — the team still names principled context budgeting and clear context-quality metrics as open, so the eval surfaces problems without supplying the budget that would prevent them.
- **Vantage caveat**: the ten-turns-then-evaluate-the-eleventh recipe is one team's convention, not a standard; the durable idea is *seeding a multi-turn session and evaluating the late turn to surface accumulating-context failures*, not the specific turn count.
