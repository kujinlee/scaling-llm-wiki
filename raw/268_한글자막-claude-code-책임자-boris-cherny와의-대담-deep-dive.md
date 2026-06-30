---
tags:
  - video-summary
  - deep-dive
  - en
  - ai in coding
  - software development
  - developer productivity
  - ai agents
  - claude code
  - loops
  - fable
video_id: "uvg9UmI0PuQ"
channel: "Tech Bridge"
lang: EN
type: Interview
audience: Advanced
score: 4.4
---

# [한글자막] Claude Code 책임자 Boris Cherny와의 대담 (Deep Dive)

**Channel:** Tech Bridge | **Duration:** 41:05 | **URL:** https://www.youtube.com/watch?v=uvg9UmI0PuQ

---

This is a comprehensive, structured deep-dive of the video.

## Introduction and Audience Poll on AI Adoption
▶ [0:03–1:45](https://www.youtube.com/watch?v=uvg9UmI0PuQ&t=3s)
The session begins with a "Live Fireside Chat" featuring Jesse Chen from Meta and Boris Cherny from Anthropic. Jesse Chen, a Director of Product on the Dev Infra team at Meta, introduces his guest, Boris Cherny, the Head of Claude Code at Anthropic.

Before diving into the discussion, Jesse Chen conducts a quick poll of the audience to gauge the adoption of AI in coding:
1.  **"How many people here use AI to write their code?"** A significant portion of the audience raises their hands.
2.  **"Keep your hands up though if you 100% of your code is written by AI."** A smaller, but still notable, number of people keep their hands up. Jesse remarks, "it's a lot more than before when I ask these questions," highlighting the rapid transformation in the industry.

## Boris Cherny's Personal Coding Metrics and Workflow
▶ [1:45–2:59](https://www.youtube.com/watch?v=uvg9UmI0PuQ&t=105s)
Boris Cherny shares his personal coding and AI usage statistics for the year, demonstrating the profound impact of AI on his own productivity:
*   **Pull Requests:** 1,700
*   **Lines of Code:** 400,000 added, 250,000 deleted. He notes that in the previous year, he deleted more code than he added.
*   **Token Usage:** 8 billion tokens since March.

When asked how much of this code was written by him versus an AI, Boris states, "100% of my code has been written by Claude code since Opus 4.5. So, that's like November of last year." This was the moment he uninstalled his IDE because he was no longer using it.

He also notes a significant shift in his work environment, stating, "most of my coding now is on my phone," a change he would have found "crazy" just six months prior.

## ROI vs. Cost: A Framework for AI Adoption
▶ [2:59–7:16](https://www.youtube.com/watch?v=uvg9UmI0PuQ&t=179s)
The discussion shifts to the business considerations of AI adoption, specifically the tension between efficiency/cost and the power of more expensive, capable models. Boris Cherny outlines two primary ways companies approach this:
1.  **Cost-focused:** Some companies view the technology primarily through the lens of its cost.
2.  **ROI-focused:** Other companies think in terms of Return on Investment (ROI), which Boris advocates as "absolutely the right framing."

He proposes a strategy for deploying AI tools like Claude Code within an organization:
*   **Initial Phase (Experimentation):** Give tokens to *everyone* in the organization—not just engineers, but also product managers, designers, data scientists, and marketers. The goal is to let the entire company experiment and discover where the most valuable ideas emerge. Boris emphasizes that innovation often comes from unexpected places, such as "an accountant somewhere in the corner of the org."
*   **Scaling Phase (Optimization):** Once successful internal use cases are identified and begin consuming a lot of tokens, the focus can shift to controlling costs on the backend. Boris states it's "too early in the adoption of this technology to think a lot about" cost-cutting upfront. He recommends focusing on increasing the return, as "there's so much more upside right now than there is room to optimize the downside."

## The Abstraction Ladder: From Code to Agents to Loops
▶ [7:16–41:04](https://www.youtube.com/watch?v=uvg9UmI0PuQ&t=436s)
Boris introduces the concept of "Loops" (or routines) as the next major step up the "abstraction ladder" in software development. He explains this progression as a series of increasingly powerful abstractions, which can be visualized as follows:

```ascii
     +-------------------------------------------------+
     | Loops / Routines (Agents prompting other agents)|
     +-------------------------------------------------+
                             ↑ (The next major step)
     +-------------------------------------------------+
     | Agents (AI writes the code from a prompt)       |
     +-------------------------------------------------+
                             ↑ (The transition we're in now)
     +-------------------------------------------------+
     | Source Code (Humans write the code by hand)     |
     +-------------------------------------------------+
```

He analogizes this to the levels of abstraction in traditional programming:
*   **Source Code** is like a **statement**.
*   An **agent run** is like a **function**.
*   A **Loop** is like a **higher-order function**.

Boris explains that "Loops" are as significant a step from "Agents" as "Agents" were from "Source Code." He personally uses Loops for tasks like automating his team's daily stand-up process and booking all of his work-related travel (flights and hotels) automatically by having the agent read his emails and Google Calendar.

## The Evolving Role of the Software Engineer
The conversation addresses the question of how the role of a software engineer is changing now that AI can handle most of the coding. Boris argues that the bottleneck is shifting away from the physical act of writing code.

### From Coding to Higher-Level Tasks
Boris notes that engineers do many things besides coding, such as:
*   Talking to customers
*   Idea generation and jamming with PMs and designers
*   Data analysis
*   Figuring out what to build next
*   Aligning with other parts of the organization

With AI handling the coding, engineers can focus more on these higher-value, upstream activities. The new bottleneck becomes "good ideas," so the engineer's role shifts to supervising agents, managing the end-to-end process, and helping to productize ideas.

### Preventing Laziness and Ensuring Learning
Addressing the concern that engineers might get "lazy" and blindly accept AI-generated code, Boris explains how Claude's design helps mitigate this and fosters learning.
*   **Permission Prompts and "Auto Mode":** Initially, Claude Code required a human to approve every command (e.g., run a bash command, fetch a URL). However, they observed "prompt fatigue" where users would just click "yes" without reading. To solve this, they created "Auto Mode," where another AI model reviews the permission prompt and decides whether to approve it based on the conversation's context. This is both more secure and removes a tedious task from the engineer.
*   **Output Styles for Learning:** Claude Code has different output styles to help engineers stay in the loop and learn.
    *   **Exploratory Style:** When Claude makes a change, it explains the architecture, the language (if new to the user), and the relevant part of the codebase. This is recommended for new engineers joining a team.
    *   **Learning Style:** For non-coders, this style teaches them *how* to do a task rather than just doing it for them. It provides a step-by-step walkthrough (e.g., "Step 1 is open this file and edit it in this way. Step 2 is run this command.").

## Tackling Downstream Bottlenecks: Code Review and Security
Boris describes Anthropic's process of identifying and solving the "next bottleneck" after coding itself was largely addressed.
*   **Code Review Bottleneck:** With AI generating so much code, the new bottleneck became code review. To solve this, Anthropic built `Claude Code Review`, a product that automates the process and is now publicly available. It is the exact same tool used internally at Anthropic and is capable of catching 98-99% of bugs before a human ever sees the pull request.
*   **Security Review Bottleneck:** The subsequent bottleneck was security review. Their solution is the `Claude Security` product, which runs weekly, scans all codebases, finds security issues, and fixes them autonomously. This tool has become so effective that it is "catching issues that even pen testers didn't catch."

## Future Vision: What's Next for Claude Code
Boris outlines the broad, high-level vision for Claude Code and Anthropic's products over the next year. He prefaces this by noting that they plan on a weekly or monthly cycle because "this space is changing too fast."
The core goals are:
1.  **Be the Most Capable Agent:** Continue to improve the model's core capabilities, especially in long-running tasks and complex reasoning.
2.  **Work Everywhere:** Ensure Claude can integrate into any team's existing workflow and toolset without requiring them to switch to a proprietary full stack.
3.  **Experience New Capabilities:** Build products that allow users to fully experience the new capabilities of each model generation, focusing on better alignment with user intent, increased nuance, and higher-quality outputs.