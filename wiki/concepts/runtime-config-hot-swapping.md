---
concept: Runtime Config Hot-Swapping
category: Agent Architecture & Patterns
summary: Managing an agent's prompt, model, and behavioral config as externally-stored variables that can be changed live in production — switching behavior without restarting the service or redeploying code.
aliases: [runtime config hot-swapping, managed variables, dynamic agent configuration, live config updates, hot-swapping prompts, no-redeploy config, production config management, feature-flagged agent config]
related: [automated-prompt-optimization, model-abstraction-layer, per-node-model-routing, agent-as-infrastructure, deterministic-workflow-orchestration, custom-eval-systems, graduated-autonomy]
sources: [agent-optimization-with-pydantic-ai-gepa-evals-feedback-loop]
---

# Runtime Config Hot-Swapping

Runtime config hot-swapping is the pattern of externalizing an agent's behavior-defining configuration — its prompt, its underlying model, its instructions — into managed variables stored *outside* the code, so the running service reads them at request time and an operator can change agent behavior live, with no restart and no code redeployment. The corpus's instance is Logfire "managed variables," which extend simple prompt management to hold *any* structured (Pydantic-defined) object, so a richly-typed configuration — not just a text string — can be swapped on the fly. The defining shift is that the prompt and model stop being baked into a deployment and become operational knobs, turning agent tuning into a config change rather than a release.

## Key Mechanics

- **Config externalized as managed variables**: the agent's prompt/model/instructions live in a managed store the running service reads, rather than as constants in the codebase — so updating behavior is a data change, not a build-and-deploy.
- **Structured, not just text**: managed variables can hold any Pydantic-defined object, so a whole typed configuration (model choice, language, behavioral parameters) is swappable as a unit, not merely a prompt string.
- **Live switch, no restart**: the corpus demonstrates a FastAPI web server hosting an MP-search agent whose response language or underlying LLM is changed instantly by altering managed variables in Logfire — the server keeps running while its behavior changes underneath it.
- **Built on feature-flag infrastructure**: the variables leverage the OpenFeature standard, so the same mechanism supports A/B testing and gradual rollouts — different users can be served different agent configurations, and a change can be ramped rather than flipped globally.
- **The deploy seam for optimization**: because config is hot-swappable, a newly optimized prompt (`[[automated-prompt-optimization]]`) or a cheaper model can be promoted into production immediately, closing the loop between offline improvement and live behavior.

## How It Appears in the Corpus

The Samuel Colvin / Pydantic ("AI Engineer" channel) talk presents Logfire managed variables as an extension of prompt management that can encompass any Pydantic object, enabling dynamic updates of agent behavior, models, or instructions in production without code redeployment, using the OpenFeature standard for A/B testing and rollouts. A live demo swaps a FastAPI MP-search agent's response language and underlying model by editing managed variables while the server runs. The stated vision is to automate this — let the observability platform continuously optimize managed variables from evaluation feedback — yielding "self-driving" agent configurations in production.

## Tensions & Tradeoffs

- **It is the production seam beneath "self-driving" agents**: paired with `[[automated-prompt-optimization]]` and a standing eval gate (`[[custom-eval-systems]]`), hot-swapping completes an autonomous eval → optimize → deploy loop — but an autonomous loop that rewrites live production config without a human is exactly where `[[graduated-autonomy]]` applies: a bad optimized config can be promoted to all traffic instantly, so the deploy step needs the same fail-closed validation a `[[dark-factory]]` merge does.
- **Convenience vs. auditability**: changing behavior without a code deploy removes the git history, review, and rollback discipline that a release carries — the agent's effective "source" now lives in a mutable variable store, so what the agent did on a given day can drift from what the repository says, demanding its own versioning and change log.
- **Adjacent to but distinct from `[[model-abstraction-layer]]` and `[[per-node-model-routing]]`**: those decide *which* model a system or step targets for portability or cost; managed variables are the *runtime mechanism* that makes such a switch take effect live without redeploying — they implement the swap rather than choosing it, and the model is just one of many fields they can carry.
- **A control surface to secure**: a store that can change an agent's prompt and model in production is high-privilege infrastructure — the same operational-surface concern as `[[agent-as-infrastructure]]`, since whoever can edit a managed variable can silently redirect every request.
