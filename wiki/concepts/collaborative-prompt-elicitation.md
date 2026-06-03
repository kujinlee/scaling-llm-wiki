---
concept: Collaborative Prompt Elicitation
category: Workflows & Methodology
summary: The shift in which the model itself helps the user articulate intent — interviewing them, suggesting clarifications, handling edge cases — so prompting becomes a two-way collaboration rather than one-way instruction.
aliases: [collaborative prompt elicitation, model-assisted prompting, prompt elicitation, model interviews the user, intent elicitation, prompting as collaboration, externalizing your brain, AI as consultant not temp, ask user question tool, agent-driven requirement gathering]
related: [prompt-engineering, plan-first-workflow, aspirational-prompting, thinking-vs-understanding, spec-driven-development, theory-of-mind-for-llms, instruction-budget, html-as-spec, agent-native-verification]
sources: [ai-prompt-engineering-a-deep-dive, how-we-claude-code]
---

# Collaborative Prompt Elicitation

Collaborative prompt elicitation is the reframing of prompting from a one-way instruction into a two-way collaboration in which the model itself helps the user articulate what they actually want. Instead of the human bearing the full burden of specifying intent precisely up front, a more capable model interviews the user to draw out requirements, suggests clarifications, and proactively raises edge cases — behaving like an expert consultant who refines the brief rather than a temp agency employee mechanically following strict instructions. The human skill correspondingly shifts toward introspection and "externalizing your brain": making nuanced ideas legible to an intelligent but context-agnostic AI. What the Anthropic prompt-engineering panel framed as a future trajectory, the corpus's later first-party workshop shows arriving as a concrete, tool-backed practice.

## Key Mechanics

- **Model as prompting assistant**: rather than only executing a prompt, the model helps *compose* it — eliciting the user's real goal through questions and surfacing ambiguities the user hadn't articulated.
- **Consultant, not temp**: the interaction resembles an expert who pushes back and clarifies, versus an order-taker who follows literal instructions — the model takes initiative in defining the task.
- **Intent still required, articulation assisted**: the need to *specify* what you want never disappears; what becomes assisted is the *articulation* of that intent, lowering the precision burden on the human.
- **Introspection as the new skill**: the human contribution moves toward externalizing complex, tacit ideas clearly — making one's own reasoning legible to a smart but context-free collaborator, akin to making a nuanced argument understandable to an educated layperson.
- **A dedicated elicitation tool**: the practice becomes concrete when the agent is given an explicit *ask-user-question* tool, so requirement-gathering is a structured tool call the agent makes mid-task rather than an implicit hope that it will ask — turning "the model interviews you" into a wired capability the harness supports.
- **Don't over-constrain — let the agent extract**: drawing on Richard Sutton's "Bitter Lesson," the discipline is to *resist over-specifying the outcome up front* and instead let the model proactively extract requirements through iterative questioning, specifying only the domain and desired audience. This both respects the model's capability and conserves the `[[instruction-budget]]`, since a leaner brief plus elicitation beats a monolithic over-defined prompt.

## How It Appears in the Corpus

The Anthropic "AI prompt engineering: A deep dive" panel envisions the future of prompt engineering as a highly collaborative process: models become powerful prompting assistants that interview users to draw out precise requirements, suggest clarifications, and handle edge cases — an expert consultant rather than an instruction-follower — with the human skill set shifting toward introspection and the ability to "externalize one's brain."

The Anthropic "How we Claude Code" workshop (Ara, Applied AI team) operationalizes the same idea: invoking the "Bitter Lesson," it urges developers to resist over-constraining the model and instead let Claude proactively extract requirements through iterative questioning — much like a user interview — by specifying the domain and audience rather than over-defining the result, and crucially by leveraging Claude's `ask user question` tool to drive that interactive gathering. The elicited requirements then feed a richer planning artifact (an `[[html-as-spec|HTML spec]]`). This is the panel's forward-looking trajectory shown as a wired, tool-backed default rather than a hope.

## Tensions & Tradeoffs

- **Articulation can be assisted, deciding cannot**: elicitation helps express intent, but `[[thinking-vs-understanding]]` holds that knowing *what* to build and *why* is the non-delegable core — the model can interview you, but it cannot supply the understanding the answers come from.
- **Upstream of `[[plan-first-workflow]]`**: a plan-first loop has the agent surface a *plan* to review *after* the request is set; elicitation runs earlier, helping *form* the request itself — they chain, elicitation feeding a sharper brief into planning and `[[spec-driven-development]]`.
- **Precision vs. ambition**: it pushes the request toward *precision* (drawing out exact requirements), complementing `[[aspirational-prompting]]`, which pushes the request toward *ambition* (the most valuable version) — different axes of refining what to ask for.
- **From trajectory to practice**: the prompt-engineering panel framed elicitation as where prompting is *heading*; the "How we Claude Code" workshop shows it becoming load-bearing via an explicit `ask user question` tool and the "don't over-constrain" posture — so the corpus's two sources mark a shift from anticipated to adopted, though how reliably the agent asks the *right* questions still bounds the gain, the same `[[theory-of-mind-for-llms]]` caveat about anticipating where the model under- or over-elicits.