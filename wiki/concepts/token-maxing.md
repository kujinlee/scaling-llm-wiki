---
concept: Token Maxing
category: Workflows & Methodology
summary: The philosophy that it is expensive *not* to burn tokens: deliberately spending on capable models and token-heavy processes yields more complete, more correct output at marginal extra cost.
aliases: [tokenmaxxing, token maxxing, expensive not to burn tokens, token maximization]
related: [per-node-model-routing, thin-harness-fat-skills, harness-engineering, llm-knowledge-wiki, shifting-bottlenecks]
sources: [tokenmaxxing-how-top-builders-use-ai-to-do-the-work-of-400-e]
---

# Token Maxing

Token maxing is the philosophy that, when AI capability is the real constraint on output quality, it is "expensive *not* to burn tokens." Rather than economizing on inference, the operator deliberately spends more — on the latest, most capable models and on token-heavy processes (cross-referencing many sources, generating exhaustive tests, building rich context) — because the marginal cost of tokens is small relative to the value of more complete, more correct output. It inverts the default cost-minimization instinct: under-spending tokens is treated as the true cost.

## Key Mechanics

- Reframes the binding resource as output quality and completeness, not token spend; spending too little is therefore the expensive mistake.
- Spend on capability: pay for the newest, strongest models for high-stakes work instead of defaulting to cheaper ones.
- Spend on breadth: token-heavy moves such as cross-referencing 20 sources instead of one, or driving 80–90% test coverage, yield more complete and trustworthy results.
- Throughput framing: a headline "400x lines of code" is the output of roughly 15 directed AI agents working in parallel, not human typing — token spend buys machine labor at scale.
- Analogized to paying high San Francisco rent: a large fixed cost justified by disproportionate, otherwise-unavailable upside.

## How It Appears in the Corpus

The Garry Tan / Y Combinator "Tokenmaxxing" talk centers this philosophy. Garry's List recreated the Posterous platform in five days for ~$200 using Claude Code Max, and its "agentic newsroom" ingests vast internet data and cross-references dozens of sources per article — doing a human journalist's work at a fraction of the cost precisely by maximizing token usage rather than minimizing it.

## Tensions & Tradeoffs

- Direct tension with `[[per-node-model-routing]]`, which *minimizes* token cost by routing cheap models to easy steps; token maxing argues for spending up on capability instead. The reconciliation is capability-based routing — route cheaply on trivial nodes but max out tokens and model strength where completeness drives value.
- "Only as good as the verification": burning more tokens raises output volume but not necessarily correctness, so the stance leans on heavy test coverage and self-checks to convert spend into trust (see `[[shifting-bottlenecks]]`).
- Economic assumption: the position holds only while token prices stay low relative to the value of output, and is asserted from a high-leverage builder's vantage rather than as a universal cost analysis.