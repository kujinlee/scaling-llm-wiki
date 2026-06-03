---
tags:
  - video-summary
  - en
  - claude code
  - ai agents
  - self-improvement
  - auto-research
  - binary evaluation
  - llm automation
  - skill optimization
video_id: "wQ0duoTeAAU"
channel: "Simon Scrapes"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.4
---

# Build Self-Improving Claude Code Skills. The Results Are Crazy.

**Channel:** Simon Scrapes | **Duration:** 11:02 | **URL:** https://www.youtube.com/watch?v=wQ0duoTeAAU

> [!summary] Quick Reference
> **TL;DR:** This video demonstrates how to build self-improving Claude Code skills by implementing an autonomous AI loop that refines skill outputs using objective binary assertions.
>
> **Key Takeaways:**
> - AI systems can autonomously improve themselves using a propose-test-check-revert/keep loop, inspired by Karpathy.
> - Claude's skill creator already automates improving skill activation by refining descriptions through test queries.
> - Implement an auto-improvement loop for skill outputs by using binary assertions to objectively measure structural adherence.
> - Create an `eval.json` with 25+ true/false statements to guide the autonomous refinement of skill behavior.
> - Automated loops excel at refining structural elements, format, and word counts, but not subjective creative quality.
>
> **Concepts:** claude code · ai agents · self-improvement · auto-research · binary evaluation · llm automation · skill optimization

---

## 1. The Power of Self-Improving AI Skills
Skills in Claude Code are powerful, but traditional refinement is slow and repetitive. Drawing inspiration from Andrej Karpathy's auto-research concept, this video introduces a method for Claude Code skills to autonomously improve themselves. The core idea is a loop: an AI system proposes a change, runs a test, checks the score, and if improved, keeps the change; otherwise, it reverts and tries again. This process can run continuously, even overnight, leading to significantly better systems without human intervention.

---

## 2. Karpathy's Auto-Research Framework
Karpathy's original auto-research setup involves three key files: `program.md` (markdown instructions for the agent), a `fixed data` file (for recording results), and a `training script` (which the agent edits). The core logic, summarized in about 10 lines, includes instructions to `tune train.py` (make a change), `run the experiment`, `read out results`, and then either `advance the branch` (keep the commit if improved) or `reset` (if worse). A crucial instruction is "Never stop," emphasizing continuous, autonomous operation until manually interrupted or a perfect score is achieved.

---

## 3. Layer 1: Improving Skill Activation
Before improving skill output, Claude needs to reliably activate the skill. Claude uses the YAML description to decide relevance, and vague descriptions can lead to low activation rates (as low as 20%). Anthropic's built-in `skill creator skill` already includes an automated loop for this. It provides test queries, evaluates trigger accuracy, proposes better descriptions, and retests them. This process is fully automated within Claude Skills 2.0, meaning there's no need to reinvent the wheel for improving skill description and activation.

---

## 4. Layer 2: Autonomous Skill Output Improvement with Binary Assertions
While skill activation is handled, producing high-quality outputs is a separate challenge. The video introduces an amended Karpathy-style loop specifically for improving Claude skill outputs. This framework mirrors Karpathy's logic but targets the `skill.md` file (skill instructions) and measures improvement using a "pass rate" against a set of binary assertions. The key difference is the metric: instead of a general value, it uses a pass rate against 25 binary assertions across five tests.

---

## 5. Setting Up the Self-Improvement Loop for Outputs
To implement this, an `eval` folder and `eval.json` file are created within the skill's directory. This `eval.json` contains 25+ binary assertions (true/false statements) that the autonomous agent can validate. Examples include "does not contain m-dashes," "under 300 words," or "the final line is a question." Subjective metrics (e.g., "compelling subject line") are avoided because they cannot be reliably automated. Claude Code can even generate this `eval.json` file based on your `skill.md`. The self-improvement loop then feeds prompts, checks assertions, and if any fail, Claude makes one change to `skill.md`, reruns tests, and keeps or reverts changes based on improved pass rates. An example of a marketing copywriting skill achieving a perfect score after fixing a conflicting rule is provided.

---

## Conclusion
The self-improvement process for Claude skills operates on two layers: Layer one, handled by the skill creator, improves skill activation through description optimization. Layer two, the focus of this video, adapts Karpathy's auto-research for autonomous skill output improvement using objective, binary assertions. This binary loop excels at refining structural elements, format, word counts, and forbidden patterns. However, it's important to note that qualitative aspects like tone of voice, creative quality, or proper contextual usage still require human judgment, often supported by the skill creator's qualitative review dashboard. This autonomous approach allows for significant structural refinement of skills overnight, leading to more robust and reliable AI agents.