---
concept: Engineering Taste
category: Industry, Strategy & Careers
summary: The human capacity for strategic technical judgment — sensing which direction is right — that concentrates and grows more valuable as agents absorb routine implementation work.
aliases: [engineering judgment, strategic technical judgment]
related: ["[[shifting-bottlenecks]]", "[[multi-agent-code-review]]", "[[agentic-issue-resolution]]", "[[jagged-intelligence]]", "[[thinking-vs-understanding]]", "[[custom-eval-systems]]", "[[ai-native-company]]"]
sources: [live-coding-session-with-boris-cherny-and-jarred-sumner, 꼭-알아야할-안드레-카파시-30분-인터뷰-완전정리-ai시대의-필수-인사이트, stanford-cs153-frontier-systems-the-ai-native-company-how-on]
---

# Engineering Taste

Engineering taste is the human capacity for strategic technical judgment — the sense for which direction is right — that remains valuable even as AI automates implementation. As agents take over more of the mechanical work, the distinctively human contribution concentrates in high-stakes decisions where correctness is not yet machine-verifiable and trust in AI judgment is not yet warranted.

## Key Mechanics

- AI shifts, rather than removes, the human role: routine coding and review move to agents, while humans retain strategic decisions.
- Taste governs choices like whether to integrate a new library — judgment calls where AI's recommendation is not yet fully trusted.
- As the agent absorbs implementation, the human role concentrates in aesthetic judgment, making the *right* decision, pursuing elegance, and supervision — designing the high-level spec the agent then fills in.
- It is the complement to `[[shifting-bottlenecks]]`: wherever verification cannot yet establish trust, human taste fills the gap.

## How It Appears in the Corpus

In the Boris Cherny and Jarred Sumner session, the speakers argue that even with agents merging simple PRs and contributing heavily, "engineering taste" stays essential for strategic decisions such as adopting new dependencies.

The Kimflip (김플립) summary of Karpathy's interview reinforces this from the model-behavior side: because the LLM is only intern-level and `[[jagged-intelligence]]` leaves it prone to systemically serious mistakes (e.g. a working feature that introduces a security hole), the human role becomes aesthetic judgment, correct decision-making, the pursuit of elegance, and supervision — designing clear high-level specifications and conducting the agent rather than writing the code. It pairs taste with comprehension as `[[thinking-vs-understanding]]`.

The Garry Tan / Diana Hu Stanford CS153 lecture makes taste the one capability that does not collapse even as the cost of shipping code approaches zero: the ability to discern good from bad and build what users actually want cannot be delegated to AI. Crucially it operationalizes taste as `[[custom-eval-systems]]` — domain-specific evaluation criteria plus human labeling of failed interactions — casting taste as the human judgment that *defines the eval*, and as the durable core of an `[[ai-native-company]]` where agents do the building.

## Tensions & Tradeoffs

- Boundary is moving: as verification deepens, the set of decisions requiring human taste is expected to shrink, but the corpus does not claim it vanishes.
- Open question: which judgments are intrinsically human versus merely not-yet-automated — the Karpathy framing ties the answer to `[[verifiability-law]]`, locating durable human taste in the regions that resist clean scoring.
- Increasingly *exercised through* evals rather than direct review: `[[custom-eval-systems]]` scale a human's judgment across agent output, but the eval is only as good as the taste that authored it — so taste does not disappear, it relocates up into defining the verifier.
