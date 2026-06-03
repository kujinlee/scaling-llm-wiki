---
tags:
  - video-summary
  - en
  - spec-driven development
  - ai coding
  - software frameworks
  - developer tools
  - open-source
  - market analysis
  - agentic ai
video_id: "b6cbxSaa4U4"
channel: "The Gray Cat"
lang: EN
type: Analysis
audience: Intermediate
score: 4.4
---

# Spec-Driven Development in 2026: What Actually Changed

**Channel:** The Gray Cat | **Duration:** 23:08 | **URL:** https://www.youtube.com/watch?v=b6cbxSaa4U4

> [!summary] Quick Reference
> **TL;DR:** This video details the rapidly evolving spec-driven development landscape, highlighting OpenSpec's rise, challenges for older frameworks, and native AI tools reshaping the market.
>
> **Key Takeaways:**
> - Native AI coding tools are absorbing functionalities, reshaping the competitive landscape for SDD frameworks.
> - OpenSpec is the recommended SDD framework for new teams due to its speed, efficiency, and lightweight design.
> - BMAD is better for individual builders, while Spec Kit's growth might be brand-driven; test alternatives like OpenSpec.
> - SDD is maturing, with new players emerging, and discussions now focus on effective implementation strategies.
>
> **Concepts:** spec-driven development · ai coding · software frameworks · developer tools · open-source · market analysis · agentic ai

---

## 1. SDD Market Overview and Shifting Landscape
Over the last six months, spec-driven development (SDD) frameworks have seen significant momentum, with combined GitHub stars for the top five jumping by 131%. However, this growth is highly uneven, with some frameworks experiencing explosive growth while others stalled or even shrank their scope. A key trend is that native AI coding tools, such as Claude Code's plan mode and skills, are increasingly absorbing functionalities that dedicated SDD frameworks used to provide. This has shifted the competitive landscape, with frameworks now competing not just with each other, but also with the underlying platforms.
---
## 2. OpenSpec: The Runaway Success and Author's Recommendation
OpenSpec experienced an astounding 863% growth in GitHub stars, becoming the clear leader. Its v1 release, a significant rewrite, resulted in smaller, clearer output and expanded compatibility with over 25 agents and IDEs. The author initially recommended Spec Kit but switched to OpenSpec due to its superior speed and efficiency. OpenSpec's lightweight approach is highlighted as a primary reason for its success, especially as frontier models handle more implementation work. The author recommends OpenSpec as the default starting point for new teams exploring SDD due to its speed, minimal ceremony, and rapidly growing community.
---
## 3. BMAD and Spec Kit: Different Growth Stories
**BMAD** saw a 133% star increase, tracking with market growth. Its version six was a ground-up rewrite, consolidating agents into a single persona ("Amelia"), introducing a "Skills Architecture," and spinning out "BMad Builder." Despite technical advancements and a highly active community (one of the largest Discord communities), criticisms persist regarding its high ceremony, extensive markdown files, and full PM-to-developer handoff rituals. The author suggests BMAD is better suited for individual builders who desire a full agile ritual layered on their AI coding setup, rather than traditional teams.

**Spec Kit** achieved a 123% star increase, amassing almost 50,000 new stars and leading in absolute star count. Key developments include 136 releases, support for over 14 AI agent platforms, and an official Microsoft Learn training module. However, community reception is mixed, with critiques from Martin Fowler highlighting its verbose and repetitive markdown files and agents often ignoring instructions. The author expresses skepticism, suggesting much of its growth might stem from GitHub's brand and Microsoft's backing rather than superior merit, and advises rigorous testing against alternatives like OpenSpec.
---
## 4. Agent OS and Taskmaster: Challenges and Retreats
**Agent OS** experienced the slowest growth among the original five, at 72%, and has seen no releases in three months, suggesting the project is largely abandoned. Its version three was an explicit downsizing, refocusing on "establishing and injecting standards" rather than full spec writing or orchestration, as frontier models now handle many of these tasks. While its refined scope offers a valid value proposition for standards automation, its dormancy raises questions about its viability.

**Taskmaster** grew by only 18%, effectively falling behind in a rapidly expanding market. This decline is attributed to a combination of factors: a commercial pivot (Hamster), a non-pure MIT license with a Commons Clause rider, telemetry concerns (opt-out by default), and a slowed release cadence. Despite its strong task decomposition engine and good code output, the commercial strategy and related community concerns appear to have stalled its growth, presenting an interesting case study in monetization timing.
---
## 5. The Rise of New Players & Native AI Capabilities
Beyond the original five, new projects like **Superpowers**, **GSD (Get Shit Done)**, and **Beads** have emerged and gained significant traction. Superpowers, an agentic skills system for Claude Code enforcing TDD, boasts 156,000 stars and is used daily by the author for large features. GSD, with 51,600 stars, focuses on execution-first, wave-based parallel orchestration. Beads, with 20,800 stars, offers a distributed graph issue tracker for AI agents, presenting a sharper alternative in task tracking. Concurrently, native AI coding tools like Claude Code have quietly absorbed many features (skills, plan mode, ultra plan mode, CLAUDE.md files) previously offered by frameworks, thereby intensifying competition for SDD projects.
---
## 6. SDD's Maturation and Ongoing Debates
Spec-driven development has achieved broader recognition, now having a Wikipedia page, four recent arXiv papers, and a place on Thoughtworks' Technology Radar. The debate has evolved from "is SDD a good idea?" to "how do you do SDD well?". Critics like Martin Fowler express cautious skepticism, drawing parallels to failed model-driven development, fearing SDD might introduce new complexities ("making things worse through attempted improvement"). François Zaninotto views SDD as a return to "Waterfall," while Marc Brooker argues it fosters earlier and more iterative design. Enthusiast anecdotes, such as Prezi Engineering's successful migration, highlight SDD's potential at scale, further fueling adoption and discussion.
---
## Conclusion
The spec-driven development landscape is rapidly evolving and highly dynamic. OpenSpec has emerged as the clear frontrunner due to its speed and lightweight approach, while BMAD maintains a loyal, active community through significant rewrites. Spec Kit's growth appears heavily influenced by brand, and both Taskmaster and Agent OS have faced challenges leading to stalled growth or narrowed scope. Crucially, the increasing capabilities of native AI coding tools are reshaping the competitive environment, pushing frameworks to offer clearer, distinct value propositions. SDD is no longer a niche concept but a legitimate, debated, and rapidly maturing approach to software development, albeit one that requires continuous evaluation as tools and methodologies evolve.