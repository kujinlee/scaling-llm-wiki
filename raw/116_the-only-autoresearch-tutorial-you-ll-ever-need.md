---
tags:
  - video-summary
  - en
  - auto research
  - andrej karpathy
  - ai agents
  - autonomous ai
  - machine learning optimization
  - website optimization
  - prompt engineering
video_id: "uBWuKh1nZ2Y"
channel: "David Ondrej"
lang: EN
type: Tutorial
audience: Beginner
score: 4.4
---

# The only AutoResearch tutorial you’ll ever need

**Channel:** David Ondrej | **Duration:** 19:53 | **URL:** https://www.youtube.com/watch?v=uBWuKh1nZ2Y

> [!summary] Quick Reference
> **TL;DR:** This video introduces Auto Research, an AI system that autonomously optimizes performance across diverse tasks by iteratively experimenting against objective metrics.
>
> **Key Takeaways:**
> - AI agents autonomously optimize tasks by running experiments, measuring outcomes, and keeping successful changes.
> - Success requires a clear, objective metric, fully automated evaluation, and limiting AI changes to one file.
> - Auto Research applies broadly to trading, marketing, prompt engineering, or any task with measurable outcomes.
> - Avoid subjective 'better' definitions; flawed metrics lead to confident optimization for wrong outcomes.
> - Practical implementation can quickly reduce website load times by automating code modifications.
>
> **Concepts:** auto research · andrej karpathy · ai agents · autonomous ai · machine learning optimization · website optimization · prompt engineering

---

## 1. Understanding Auto Research: Autonomous AI Self-Improvement
Andrej Karpathy's open-source project, Auto Research, revolutionizes AI development by enabling artificial intelligence to autonomously improve itself. The core idea is simple: an AI agent runs numerous experiments, automatically identifying and keeping successful outcomes while discarding failures. This process eliminates manual optimization, allowing the AI to iterate and refine its performance through a continuous loop. Karpathy initially applied this to optimize a GPT-2 training script, realizing the potential for AI to self-manage its own improvements.

---

## 2. The Auto Research Loop and Three-File Architecture
At the heart of Auto Research is a continuous feedback loop. The AI agent first forms a hypothesis, then modifies a designated code file (e.g., `train.py`) to test it. After a fixed training duration (e.g., 5 minutes), an independent evaluation script (`prepare.py`) measures the outcome against a predefined metric. If the results are positive, the changes are committed; if negative, the changes are reverted, and the loop restarts with a new experiment. The `prepare.py` file is critical and untouchable by the agent to prevent it from manipulating evaluation metrics. A fixed time budget for each experiment ensures fair comparison, allowing only genuinely better ideas to prevail.

---

## 3. Conditions for Success and Failure in Auto Research
For an Auto Research loop to be successful, three conditions are essential: 1) A *clear, objective metric* that provides a single number and a definite direction for improvement. 2) *Automated evaluation* with no human intervention, ensuring the process can run continuously and efficiently, even while you sleep. 3) *One designated file* that the agent is allowed to modify. Auto Research struggles and ultimately fails in domains where 'better' is subjective (e.g., brand design, UX, pricing without high-volume A/B testing). If success requires a judgment call or feeling, the agent cannot optimize effectively. Furthermore, providing a flawed or misaligned metric will lead the agent to confidently optimize for the wrong outcome.

---

## 4. Expansive Applications Beyond Machine Learning
The biggest misconception about Auto Research is that it's solely for optimizing machine learning models. The video strongly emphasizes that its principles apply to *any domain where an outcome can be clearly measured*. This includes: **Trading Strategies** (tweaking buy/sell rules, evaluating by Sharpe ratio), **Marketing** (A/B testing ad creatives, emails, landing pages, headlines, dramatically increasing experiment volume from 30/year to 100/day), **Developer Tools** (optimizing codebases for speed, fine-tuning open-source AI models for local devices), and **Prompt Engineering** (refining system instructions for AI agents to find optimal phrasing, language, or complexity levels). This paradigm shift suggests that intelligent agents can automate and optimize nearly any measurable task, making execution free and valuing the skill of defining the right metrics and constraints.

---

## 5. Practical Demonstration: Building Your First Auto Research Loop
The video provides a hands-on tutorial for building an Auto Research loop to optimize website loading times. Using Andrej Karpathy's open-source repository, an IDE (Cursor), and an AI coding agent (Claude Code), the process involves:

1.  **Setting up the Environment:** Cloning the original Auto Research repo and creating a new project folder for a simple Express web application.
2.  **Defining the Metric:** Creating a `benchmark.mjs` script using Puppeteer to measure website load times (the `prepare.py` equivalent).
3.  **Crafting the `program.md`:** Adapting Karpathy's detailed instructions to guide the AI agent toward optimizing website speed.
4.  **Initiating the Loop:** Commanding the AI agent to run baseline benchmarks, record results, and then begin the iterative experiment loop. The demonstration shows the AI agent making iterative changes to the website's code (`train.py` equivalent) and successfully reducing load times from 50ms to 25ms in a matter of minutes, showcasing the rapid, autonomous improvement capability.

---

## Conclusion
Auto Research represents a profound shift in how we approach problem-solving and optimization, extending far beyond traditional machine learning. By leveraging autonomous AI agents to run countless experiments against objective metrics, individuals and businesses can achieve unprecedented levels of efficiency and innovation across diverse domains. Andrej Karpathy's vision of a distributed AI research model, akin to SETI@home, underscores the transformative potential of this open-source framework, pointing towards a future where AI continuously refines and improves itself at scale, potentially ushering in the early stages of a technological singularity.
