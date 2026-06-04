---
concept: Thinking vs. Understanding
category: Industry, Strategy & Careers
summary: Karpathy's distinction: analytical reasoning can be outsourced to an LLM, but genuine comprehension — knowing what to build and why — cannot be delegated.
aliases: [thinking vs understanding, outsource thinking not understanding, understanding as the final bottleneck, you can outsource thinking but not understanding]
related: ["[[engineering-taste]]", "[[shifting-bottlenecks]]", "[[jagged-intelligence]]", "[[agent-native-infrastructure]]", "[[vibe-coding-vs-agentic-engineering]]", "[[verifiability-law]]"]
sources: [꼭-알아야할-안드레-카파시-30분-인터뷰-완전정리-ai시대의-필수-인사이트]
---

# Thinking vs. Understanding

Thinking vs. understanding is Karpathy's distinction between the part of cognition that can be delegated to an AI and the part that cannot. "Thinking" — analyzing information, reasoning step by step, working a problem — is outsourceable to an LLM. "Understanding" — lodging information in your own mind, connecting it to what you already know, and converting it into genuine insight — cannot be outsourced; it must be done by the human. The deepest bottleneck of the AI era is therefore not the ability to write code but the understanding of *what* to build, *why* it is worth building, and *how* to direct the agents that build it.

## Key Mechanics

- **Thinking is delegable**: information analysis and multi-step reasoning can be handed to the model, which performs them at scale.
- **Understanding is not**: making knowledge "settle" in your own brain, linking it to other knowledge, and turning it into a realization is an irreducibly human act — delegating the reasoning does not transfer the comprehension.
- **Memorization vs. foundations**: rote, lookup-style knowledge (PyTorch/NumPy API details) should be left to agents; foundational *system* understanding (e.g. the storage model of a tensor) must stay with the human, because that is what enables correct direction and supervision.
- **The final bottleneck moves up the stack**: as coding itself is automated, the binding constraint becomes deciding what to make, judging whether it is worth making, and conducting the agents — all functions of understanding, not typing.

## How It Appears in the Corpus

The Kimflip (김플립) summary of Karpathy's interview makes "싱킹은 아웃소싱할 수 있지만, 언더스탠딩은 아웃소싱할 수 없다" (thinking can be outsourced, understanding cannot) its central message. It distinguishes delegable reasoning from non-delegable comprehension, advises offloading memorization-type API knowledge to agents while retaining foundational system understanding, and names deep understanding of what/why/how-to-direct as the final bottleneck of the AI era.

## Tensions & Tradeoffs

- It is the human-role companion to `[[shifting-bottlenecks]]`: where that concept observes the constraint migrating toward verification and merge-trust, this one locates the *human's* residual job at the understanding layer above any verifier.
- It sharpens `[[engineering-taste]]`: taste is the judgment, understanding is the comprehension that grounds it — both are the parts `[[jagged-intelligence]]` and `[[verifiability-law]]` say AI cannot yet be trusted to own.
- Risk of hollow delegation: outsourcing thinking without retaining understanding produces operators who can ship via `[[vibe-coding-vs-agentic-engineering]]` but cannot supervise — the corpus treats this as the failure mode to guard against, not a convenience to embrace.
