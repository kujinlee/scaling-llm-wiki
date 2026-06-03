---
tags:
  - video-summary
  - en
  - ai coding
  - claude code
  - codex
  - llm comparison
  - software development
  - real-time editor
  - code quality
  - developer tools
video_id: "E2UgYp2vh5U"
channel: "Tech With Tim"
lang: EN
type: Analysis
audience: Intermediate
score: 4.2
---

# I Built the Same App With Claude Code and Codex

**Channel:** Tech With Tim | **Duration:** 27:00 | **URL:** https://www.youtube.com/watch?v=E2UgYp2vh5U

> [!summary] Quick Reference
> **TL;DR:** This video compares Claude Code and Codex for app development, noting Claude's speed vs. Codex's superior code quality, cost-efficiency, and proactiveness.
>
> **Key Takeaways:**
> - Claude Code excels in speed for rapid prototyping and quick task completion.
> - Codex produces higher quality, more structured code and performs proactive testing.
> - Codex is more token-efficient and cost-effective despite slower execution times.
> - Claude is direct; Codex is autonomous, offering deeper reasoning and bug fixes.
> - Use Claude for initial rapid development and Codex for quality-focused, long-term project phases.
>
> **Concepts:** ai coding · claude code · codex · llm comparison · software development · real-time editor · code quality · developer tools

---

## 1. Introduction and Methodology
This video conducts a practical comparison between Claude Code (using Opus 4.7) and Codex (using GPT 5.5) as AI coding assistants. The objective was to build a relatively complex real-time collaborative markdown editor called Collab MD. The evaluation criteria included speed, cost (token usage), the quality of the finished application (bugs, adherence to specifications), and the overall code quality.

The development process was structured into eight distinct phases, starting from project scaffolding, implementing a basic editor and preview, adding real-time synchronization and cursor presence, and finally incorporating features like a landing page, document management (CRUD), version history, export functionality, and dark mode. Both models were given full file system access and configured for their highest reasoning capabilities to ensure a comprehensive test.

---

## 2. Initial Development & Early Challenges
During the initial **scaffolding phase**, Codex demonstrated greater thoroughness, taking approximately 14 minutes compared to Claude's estimated 6 minutes, but produced a more complete and structured project directory. Claude, however, failed to successfully run the application for a preview at this stage.

For the **basic editor and preview implementation**, both models finished around the same time. Codex introduced an infinite loop bug upon document creation, while Claude's editor worked, although its "new document" button was non-functional. Claude consistently struggled with getting the development server to run or deploy effectively throughout the early stages.

When implementing **real-time collaboration and cursor presence**, Codex took the lead, completing the task in about 7 minutes and successfully integrating these features with functional cursor identity. Claude also managed to implement these features, but its document saving mechanism appeared to be buggy, requiring a refresh to show changes.

---

## 3. Advanced Features and Final Application State
For the **combined implementation of advanced features** (landing page, version history, export, and dark mode), Codex took a significantly longer time of 26 minutes, as opposed to Claude's 7-8 minutes. This substantial difference in completion time was largely attributed to Codex's proactive approach, which involved extensive internal testing and verification of the features it built.

Despite the time discrepancy, the **final applications produced by both models were remarkably similar** in functionality and appearance. Both included features like dark/light mode toggles, document export options (e.g., Markdown, HTML), sharing capabilities, and seamless real-time updates with active cursor presence. Minimal differences were observed in the user interface or overall user experience between the two final products.

---

## 4. Code Quality Review and Model Behavior
A manual review of the **code quality** generally favored Codex. Its codebase was found to be more structured, with better separation of concerns (e.g., dedicated files for API calls, types, themes, and presence management). It featured less nesting, fewer excessive inline comments, and appeared generally cleaner and easier to read compared to Claude's output. Claude's code, while functional, often included more nesting, verbose inline comments, and less optimal practices like direct API calls within components.

Both models were also tasked with **reviewing the other's code**. Codex's review of Claude's application pointed out issues such as local fetch calls within components and general repository hygiene. Claude's review of Codex's code identified several areas for improvement, including minor UI quirks and potential performance concerns like disk writes on every keystroke.

In terms of **model behavior**, Claude was noted for its speed and directness, typically executing exactly what was explicitly requested. Codex, while slower, demonstrated a more proactive and autonomous approach, often performing automatic testing, verification, and even attempting minor bug fixes without direct instruction. This makes Codex potentially better suited for more complex, larger applications where robust testing and deeper reasoning are critical.

---

## 5. Performance, Cost, and Token Efficiency
**Speed Comparison:** Claude consistently outperformed Codex in terms of speed, often completing tasks 50-70% faster. This makes Claude ideal for quick prototyping or rapid iteration where immediate results are paramount.

**Token Usage & Cost:** A critical finding was the difference in resource consumption. Claude was observed to use significantly more tokens, estimated at 2 to 2.5 times the usage of Codex for similar tasks. This translated to a projected 3-4 times higher cost for Claude over time. Codex efficiently managed its context window, automatically compacting it when limits were approached, and demonstrated greater token efficiency despite its longer run times and more intensive processing.

---

## Conclusion
Both Claude Code and Codex are exceptionally capable AI coding assistants, but they exhibit distinct strengths tailored to different development scenarios. Claude's primary advantage lies in its **speed and directness**, making it excellent for rapid initial project spin-ups, quick iterations, and scenarios where immediate, straightforward output is prioritized.

Codex, while slower, offers superior **code quality, proactiveness, and cost efficiency** in terms of token usage. Its ability to perform deeper reasoning, automatic testing, and verification makes it more suitable for complex, larger-scale applications, debugging, and situations where robustness and maintainability are critical. The video suggests that developers should consider using both tools strategically, leveraging Claude for initial rapid development and Codex for more intricate, quality-focused, and long-term project phases. Furthermore, Codex's 'fast mode' could potentially bridge the speed gap while still maintaining its cost advantage.