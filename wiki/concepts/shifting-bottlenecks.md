---
concept: Shifting Bottlenecks
category: Industry, Strategy & Careers
summary: As AI automates each constraint (code generation, basic checks), the binding constraint migrates to the next weakest link — currently deep verification and the trust required for autonomous merges.
aliases: [moving bottleneck, bottleneck migration in agentic development]
related: [engineering-taste, self-verification-loop, agentic-issue-resolution]
sources: [live-coding-session-with-boris-cherny-and-jarred-sumner, live-coding-session-with-boris-cherny-and-jarred-sumner-deep-dive]
---

# Shifting Bottlenecks

As AI coding capability improves, the binding constraint in the development process does not disappear — it moves. Tasks that were once the hard part (writing code, basic verification) become cheap, and the bottleneck migrates to whatever is now the weakest link, typically deeper verification and establishing enough proof of correctness to trust automated action.

## Key Mechanics

- The constraint relocates: early on, writing code and basic checks were limiting; as those are automated, the limit becomes deeper verification layers and proof sufficient for automated merges.
- Diagnosing "where is the bottleneck now?" becomes a recurring, ongoing activity rather than a one-time analysis.
- Each capability gain should prompt re-examination of what is now slowest, because the previous constraint is likely solved.
- **From developer time to compute time**: once agents generate and self-verify code autonomously, the slowest link is no longer a human typing — it becomes the *CI/CD pipeline speed* and the *compute cost* of running hundreds of agents that each compile code and run test suites in their own environments. The bottleneck migrates from labor to infrastructure throughput.
- **Cheap PRs raise the merge bar**: when an agent produces fix-and-test PRs almost for free, each PR becomes a low-cost "suggestion" rather than a costly human effort. This lowers the *social cost of rejecting* a PR and correspondingly *raises the bar for what gets merged*, pushing the human's scarce attention toward architectural integrity and `[[engineering-taste]]` rather than line-by-line review.

## How It Appears in the Corpus

The Boris Cherny and Jarred Sumner session frames agentic development as continuous experimentation and bottleneck identification: with code generation and the `[[self-verification-loop]]` largely solved, the open frontier is trustworthy automated merging of complex changes. The deep-dive analysis sharpens the relocation — as RoboBun autonomously reproduces, fixes, tests, and reviews, the human bottleneck becomes verification and high-level decision-making, while the *operational* bottleneck shifts from developer hours to CI/CD pipeline speed and the compute cost of running many containerized agents at once.

## Tensions & Tradeoffs

- Fully automated merges of complex work remain out of reach pending deeper verification; simple issues are closer to hands-off merging.
- The human bottleneck persists where judgment is required — see `[[engineering-taste]]`.
- Compute as the new cost center: shifting the bottleneck from developer time to compute time trades a labor constraint for an infrastructure bill — running hundreds of agents in isolated environments compiling and testing is resource-intensive, so the saving in human hours is partly paid back in CI/CD spend.
