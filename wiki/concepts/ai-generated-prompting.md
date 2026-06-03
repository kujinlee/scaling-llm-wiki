---
concept: AI-Generated Prompting
category: Workflows & Methodology
summary: Using one AI to synthesize research into a precise, high-quality prompt that is then fed to a second AI to execute — an AI coaching another AI rather than a human hand-writing the instruction.
aliases: [AI-generated prompts, AI coaching AI, model-generated prompting, cross-model prompt authoring, prompt relay, research-to-prompt pipeline, one AI prompts another]
related: [collaborative-prompt-elicitation, cross-model-critique, automated-prompt-optimization, agentic-coding-tool-selection, explicit-gears, prompt-engineering, per-node-model-routing, self-verification-loop]
sources: [claude-opus-4-7-notebooklm-is-insane]
---

# AI-Generated Prompting

AI-generated prompting is the technique of handing the job of *writing the prompt* to an AI rather than composing it by hand: one model synthesizes accumulated research or context into a precise, detailed instruction, and that generated instruction is then fed to a second model (or a second pass) to actually execute the task. The defining move is that a prompt — normally the human's responsibility — becomes an *artifact produced by a model*, so the quality bottleneck shifts from the operator's prompt-writing skill to a model's ability to distill context into a well-structured instruction. The corpus frames it as "using one AI to coach another": because most operators omit critical details when writing complex prompts by hand, offloading prompt construction to a model that has been pre-loaded with thorough research yields a far more complete and effective instruction than the human would have typed.

## Key Mechanics

- **Prompt as a generated artifact, not a hand-typed string**: rather than the operator composing the instruction, a model reads source material and emits the prompt — turning prompting into a synthesis task the AI performs, with the human supplying the upstream research and the downstream execution target.
- **Three-role pipeline (research → strategize → build)**: the corpus's instance splits the work across specialized roles — a *thinker* model produces broad, structured research on the task (features, use cases, a step-by-step plan, common mistakes); a *strategist* model ingests that research and synthesizes it into a high-quality, tailored prompt (incorporating logic, features, and UI suggestions); and a *builder* model takes the generated prompt and produces the final implementation. Each stage plays to a different tool's strength.
- **Context-grounded, not context-free**: the prompt-generating model is fed the prior stage's research as a source, so the prompt it writes is grounded in concrete detail rather than improvised — the synthesis quality is what makes the resulting instruction better than a one-shot human prompt.
- **A division of cognitive labor across tools**: the technique is a whole-tool analogue of switching cognitive modes (`[[explicit-gears]]`) and of routing different stages to different models by fit — assigning *thinking*, *prompt-strategizing*, and *building* to whichever tool is best at each, rather than running the entire task through one model with one vague prompt.
- **Reusable prompt assets**: effective generated prompts are saved for future reuse, accumulating into an asset library — the same compounding-capture instinct as feeding learnings back into the environment.

## How It Appears in the Corpus

The Julian Goldie SEO tutorial "Claude Opus 4.7 + NotebookLM is INSANE" presents a concrete three-step workflow: prompt Claude Opus 4.7 as a research assistant to break a broad goal (e.g. building a keyword-cluster tool) into features, use cases, a plan, and common mistakes; paste that research into Google NotebookLM and instruct it to generate a precise, build-ready prompt synthesizing the research; then feed that generated prompt back into Claude to build the tool. The video's stated core innovation is *using one AI (NotebookLM) to generate a superior prompt for another AI (Claude)* — "using one AI to coach another" — arguing this beats single-prompt attempts because the human-written prompt usually misses critical detail that a research-grounded model fills in.

## Tensions & Tradeoffs

- **Distinct from `[[collaborative-prompt-elicitation]]`**: there the model interviews the *human* to draw out their intent; here the model writes the prompt from *research material* with no user articulation in the loop. One assists the human's articulation; the other replaces the human as prompt author entirely.
- **Distinct from `[[cross-model-critique]]` and `[[per-node-model-routing]]`**: cross-model critique runs the *same* task on different vendors to harvest disagreement, and per-node routing splits workflow steps by difficulty for cost/capability — AI-generated prompting instead runs a *sequential relay* where one model's output is a prompt that becomes another model's input, closest in spirit to the "plan with one, execute with another" posture of `[[agentic-coding-tool-selection]]` but with an explicit prompt-synthesis stage between.
- **No verifier in the loop**: unlike `[[automated-prompt-optimization]]`, the generated prompt is produced by a single synthesis pass with no golden dataset, eval, or scoring — so "better prompt" is asserted by construction, not measured, and a confidently-wrong synthesis produces a confidently-wrong build with no `[[self-verification-loop]]` to catch it.
- **Garbage-in cascades through the relay**: the build is only as good as the generated prompt, which is only as good as the upstream research — an error introduced at the research stage propagates silently through prompt synthesis into the final artifact, and the longer pipeline gives it more places to drift.
- **Overhead vs. payoff**: running three tool stages for one task adds coordination, context-handoff, and token cost over a single prompt, justified only when the task is complex enough that a hand-written prompt would genuinely fall short.
- **Vantage caveat**: the source is a short SEO/monetization tutorial demonstrating one workflow, so the dramatic-improvement claim is an illustrative pitch, not a controlled comparison — the durable idea is the *prompt-as-generated-artifact* pattern, not the specific tool pairing or the "insane" framing.
