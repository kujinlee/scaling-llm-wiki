---
concept: High-Bandwidth Agent Interfaces
category: Agent Architecture & Patterns
summary: The argument that linear chat is too low-bandwidth for complex agent collaboration — as agents make "doing" cheap, planning and reviewing become the bottleneck, demanding richer artifacts (collaborative documents, tabular reviews) plus trust and control levers rather than a single conversational stream.
aliases: [agents need more than chat, high-bandwidth artifacts, beyond chat, low-bandwidth chat problem, trust and control for agents, verifier's rule, tabular review]
related: ["[[collaborative-prompt-elicitation]]", "[[interactive-artifacts]]", "[[plan-first-workflow]]", "[[verifiability-law]]", "[[shifting-bottlenecks]]", "[[multi-agent-code-review]]", "[[holdout-validation]]", "[[satisfaction-testing]]", "[[thinking-vs-understanding]]"]
sources: [aie-europe-keynotes-coding-agents-ft-pi-google-deepmind-anth]
---

# High-Bandwidth Agent Interfaces

High-bandwidth agent interfaces is the argument that a linear chat window is the wrong surface for serious human-agent collaboration: chat is *low-bandwidth* and sequential, while the work that now matters is *high-bandwidth* and parallel. Once agents make the "doing" of a task cheap, the binding constraints shift to *planning* (deciding what should be built) and *reviewing* (confirming what was built is right), and neither is well served by scrolling a conversation. The prescription is to give humans and agents richer shared artifacts — collaborative documents, tabular reviews, structured plans — through which judgment can flow at a higher rate than a chat transcript allows, backed by deliberate levers for *trust* and *control*.

## Key Mechanics

- **Doing is cheap; planning and reviewing are the bottleneck**: as agents absorb execution, value migrates to the two ends — specifying the task well and verifying the result — the human-collaboration face of `[[shifting-bottlenecks]]` and the interface side of `[[thinking-vs-understanding]]`.
- **The Verifier's Rule**: usefulness tracks how well a task's output can be verified, so the interface must make verification efficient — a restatement of the corpus's `[[verifiability-law]]`, here turned into an interface-design requirement rather than a model property.
- **Trust levers**: decomposition (break the task into checkable pieces), guardrails, and proxies for verification raise how much autonomy a human can safely grant — the same trust-manufacturing machinery as `[[holdout-validation]]` and `[[satisfaction-testing]]`, surfaced as collaboration controls.
- **Control levers**: structured planning, reusable skills, and *elicitation* — the agent drawing requirements out of the user — let the human steer intent precisely, the interface counterpart of `[[collaborative-prompt-elicitation]]`.
- **High-bandwidth artifacts over linear chat**: collaborative documents and tabular review surfaces present many decisions at once for parallel human judgment, where a chat stream forces them through one narrow, sequential channel — the same "output as a manipulable object" shift as `[[interactive-artifacts]]`, applied to the *review and planning* surface rather than the deliverable.

## How It Appears in the Corpus

The AIE Europe keynotes (AI Engineer channel) feature Jacob Laurson of Lagora arguing that "agents need more than chat" for complex vertical AI applications such as legal tech: AI makes doing work cheap, so planning and reviewing become the new bottlenecks. He introduces the "Verifier's Rule" and discusses raising human *trust* (decomposition, guardrails, proxies for verification) and *control* (structured planning, skills, and elicitation from the user), emphasizing the need for high-bandwidth artifacts — collaborative documents, tabular reviews — as interfaces for human-agent collaboration rather than relying on the low-bandwidth, linear nature of chat. The keynotes' broader "agent experience as a primary design focus" theme, and tools that translate debugging surfaces into agent-analyzable file systems, sit alongside it as instances of designing the collaboration surface, not just the model.

## Tensions & Tradeoffs

- **Chat's universality vs. its bandwidth**: a conversation is the lowest-friction, most general interface, which is exactly why it underserves complex planning and review — the durable claim is *not* that chat is bad but that high-stakes collaboration outgrows it, so richer surfaces are added where bandwidth matters.
- **Richer interfaces are more to build and maintain**: a tabular review surface or collaborative planning doc is real product engineering, so the bandwidth gain is paid for in interface complexity — the same build cost as any purpose-built surface like `[[interactive-artifacts]]` or `[[multi-agent-code-review]]`'s comment cycle.
- **Verification efficiency is the ceiling**: the Verifier's Rule cuts both ways — a high-bandwidth review surface only helps if the human can actually judge correctness from it, so it presupposes the task sits on the verifiable side of `[[verifiability-law]]`; for genuinely unverifiable work, more interface bandwidth does not manufacture trust.
- **Elicitation assists articulation, not deciding**: richer control levers help the user *express* intent (`[[collaborative-prompt-elicitation]]`), but the understanding of what to build remains the human's, per `[[thinking-vs-understanding]]` — the interface widens the channel without supplying the signal.
