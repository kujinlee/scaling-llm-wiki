---
tags:
  - video-summary
  - deep-dive
  - en
video_id: "aKe71FrwL1o"
channel: "Cloud Codes"
lang: EN
type: Analysis
score: 4.6
---

# Ornith 1.0 Is INSANE with Claude Code (FREE + Local + open Source) (Deep Dive)

**Channel:** Cloud Codes | **Duration:** 9:57 | **URL:** https://www.youtube.com/watch?v=aKe71FrwL1o

---

This document provides a comprehensive, structured deep-dive into the video, explaining its core concepts and technical details.

## The "Cage Match" Fallacy
▶ [0:00–0:12](https://www.youtube.com/watch?v=aKe71FrwL1o&t=0s)
The video begins by addressing a common misconception that emerged on the internet: a "cage match" between two top-tier coding tools, **Ornith 1.0** and **Claude Code**. Ornith 1.0 is described as a "brand new open weight model," while Claude Code is a well-established tool. The central premise of the video is that this framing of a direct fight is a "completely wrong" category error. The rivalry is described as "imaginary from the start" because the two tools are not competitors but complementary components of a larger system.

## Meet Ornith 1.0
▶ [0:12–0:54](https://www.youtube.com/watch?v=aKe71FrwL1o&t=12s)
Ornith 1.0 is an open-weight model released on June 25, 2026, by a research lab named **DeepReinforce**. Its key characteristics are:
- **Open Weights:** The model's parameters are publicly available.
- **MIT License:** It uses a permissive license, allowing broad use.
- **No Regional Locks:** It is globally accessible without geographic restrictions.
- **Local Execution:** It can be downloaded and run entirely on a user's own hardware.

The video highlights that Ornith's most "short-circuiting" feature is its ability to learn its own problem-solving process during training. This "self-scaffolding" capability means it doesn't just write code; it learns to generate its own plans, make tool calls, inspect results, and repair its own work. Unlike most models that "wait to be told how to behave," Ornith "figured out the how on its own."

The on-screen graphic illustrates this self-written plan:
```ascii
      +---------------------+
      |   SELF-WRITTEN PLAN   |
      +---------------------+
      | 1. plan the task      |
      | 2. call the tools     |
      | 3. inspect results    |
      | 4. rewrite what failed|
      +---------------------+
```

This led to the "hot take" that if a model can scaffold itself, an external agent harness like Claude Code might no longer be necessary.

## The Category Error: A Brain vs. A Pair of Hands
▶ [0:54–1:21](https://www.youtube.com/watch?v=aKe71FrwL1o&t=54s)
The video's central thesis is that Ornith and Claude Code are fundamentally different types of tools that operate on different layers.
- **Ornith** is a **brain**; its function is to think and reason.
- **Claude Code** is a **pair of hands**; its function is to act and interact with the user's machine.

```ascii
     +-----------------+       +-----------------+
     |      Ornith     |       |    Claude Code  |
     |    IT THINKS    |       |     IT ACTS     |
     +-----------------+       +-----------------+
              ↓                     ↑
              +---------------------+
              |    They compose,    |
              |    not compete.     |
              +---------------------+
```

They are not interchangeable and are designed to work together. As proof, the video reveals that when DeepReinforce benchmarked Ornith, one of the harnesses they used to run the model was **Claude Code itself**. The on-screen text emphasizes, "they composed, not competed," dissolving the idea of a rivalry. A Terminal-Bench 2.1 benchmark shows Ornith achieving a score of **40.6** when "loaded as the brain" inside the Claude Code harness.

## Ornith Model Family and Performance
▶ [1:21–1:51](https://www.youtube.com/watch?v=aKe71FrwL1o&t=81s)
Ornith 1.0 is not a single model but a family of four, scaling from laptop-sized to data-center scale:
- **9B:** A dense model that can run on a single GPU.
- **31B:** A dense "workhorse" model.
- **35B:** A Mixture-of-Experts (MoE) model with approximately 3 billion active parameters per token.
- **397B:** The flagship model.

The flagship 397B model is shown to be highly competitive with frontier closed-source models. On the **SWE-Bench Verified** benchmark, Ornith 397B scores **82.4**, which ties with Claude Opus 4.7 (which scored 80.8 in the graphic, but the text says 82.4 ties it) and is only a few points behind the top-performing Claude Opus 4.8 (87.6). This places a fully open model in direct conversation with the best proprietary models.

## A New Paradigm: An Open Brain in a Frontier-Grade Harness
▶ [1:51–2:16](https://www.youtube.com/watch?v=aKe71FrwL1o&t=111s)
The combination of Ornith and Claude Code creates a new, powerful paradigm. By running an open-source "brain" like Ornith inside a top-tier "harness" like Claude Code, users can achieve a setup with unprecedented benefits:
- **Private:** All data and code remain on the user's machine.
- **Local:** The entire stack can run offline without an internet connection.
- **MIT-licensed:** Permissive and suitable for commercial use.
- **$0 / token:** No per-token costs, as the model is run locally.

The video states that "that exact combination simply did not exist a year ago."

## Deep Dive: The Model (Ornith 1.0)
▶ [2:16–2:17](https://www.youtube.com/watch?v=aKe71FrwL1o&t=136s)

### Training and Architecture
▶ [2:17–2:47](https://www.youtube.com/watch?v=aKe71FrwL1o&t=137s)
Ornith is not built from scratch. It is post-trained on two strong open base models: **Gemma 4** and **Qwen 3.5**. DeepReinforce took these existing models and pushed them "much, much further with reinforcement learning" to teach them to be effective agents.

```ascii
      +-----------------+
      |     Gemma 4     |
      | OPEN BASE MODEL |
      +-----------------+
              ↓
      +-----------------+
      |      + RL       |
      +-----------------+
              ↓
      +-----------------+
      |    Qwen 3.5     |
      | OPEN BASE MODEL |
      +-----------------+
              ↓
      +-----------------+
      |    ORNITH 1.0   |
      +-----------------+
```

### Context Window and Hardware
▶ [2:47–3:01](https://www.youtube.com/watch?v=aKe71FrwL1o&t=167s)
All models in the Ornith family support a large context window of **256K tokens**, which can be extended to **400K tokens** for tasks involving whole repositories. The smallest 9B model can run with this full context on a single 80GB GPU, requiring approximately 19 GB of memory in `bf16` (half precision).

### Agentic Behavior by Default
▶ [3:01–3:19](https://www.youtube.com/watch?v=aKe71FrwL1o&t=181s)
Ornith is "agentic out of the box." Its responses are structured to be easily parsed by agentic systems. Each response begins with a `<think>` block, where the model outlines its plan, followed by one or more `<tool_call>` blocks. Critically, these tool calls follow the standard **OpenAI-compatible format**, meaning that "every harness already understands it" without needing "exotic glue." This compatibility is what allows it to slot directly into a tool like Claude Code.

### Self-Scaffolding RL
▶ [3:19–3:51](https://www.youtube.com/watch?v=aKe71FrwL1o&t=199s)
This is Ornith's core innovation. While most models are trained with a fixed, human-written scaffold, Ornith treats the scaffold itself as a learnable object that it proposes, refines, and rewrites. This is achieved through a two-stage reinforcement learning process:
1.  **Stage 1: Propose a scaffold.** The model first generates a plan or process to solve the given task.
2.  **Stage 2: Solve the task.** The model then executes that plan to arrive at a solution.

The reward signal from the final outcome is fed back to both stages, allowing the model to improve not just its ability to answer questions but also its fundamental process for *how to work*.

```ascii
+-----------------------+      +------------------+
|        STAGE 1        |      |      STAGE 2     |
|  Propose a scaffold   |----->|   Solve the task |
+-----------------------+      +------------------+
          ↑                            ↑
          |                            |
          +----(reward + both stages)--+
```

### Safeguards
▶ [3:51–4:05](https://www.youtube.com/watch?v=aKe71FrwL1o&t=231s)
To prevent a model that designs its own process from "gaming" the system, DeepReinforce implemented three key guardrails:
1.  **Trust boundary:** A hard outer wall that the model cannot cross.
2.  **Deterministic monitor:** A system that flags any forbidden or unsafe moves.
3.  **Frozen judge:** A separate, fixed model that can veto an entire run if it detects undesirable behavior.

### Efficiency
▶ [4:05–4:21](https://www.youtube.com/watch?v=aKe71FrwL1o&t=245s)
The payoff for this advanced training method is extreme efficiency. The **Ornith 9B** model, despite its small size, performs on par with or better than much larger models. On SWE-Bench Verified, it scores **69.4**, slightly behind **Qwen 3.5 35B** (70.0) but significantly ahead of **Gemma4 31B** (52.0). This demonstrates that "learning a better process... is worth a lot of raw parameters."

## Deep Dive: The Harness (Claude Code)
▶ [4:21–4:23](https://www.youtube.com/watch?v=aKe71FrwL1o&t=261s)

### The Agent Loop
▶ [4:23–4:38](https://www.youtube.com/watch?v=aKe71FrwL1o&t=263s)
Claude Code is not a model but a **harness**. It is the agent loop that orchestrates the problem-solving process. This loop consists of four steps:
1.  Take a goal.
2.  Plan a step.
3.  Run a tool.
4.  Read the result.
The harness repeats this cycle until the job is complete.

### The Power of the Harness
▶ [4:38–4:50](https://www.youtube.com/watch?v=aKe71FrwL1o&t=278s)
The harness is crucial because it translates a model's text-only output into real-world actions. A raw model can only talk; the harness is what allows it to *do*. It is the layer that actually opens files, runs commands, and feeds error messages back to the model for correction.

### Security and Control
▶ [4:50–5:07](https://www.youtube.com/watch?v=aKe71FrwL1o&t=290s)
The harness is also the layer responsible for security and control. It holds the "real keys" to the system, which a raw model should never have direct access to. This includes:
- **Real file system** access (edit, create, move).
- A **real terminal** to run any command.
- A **permission gate** that pauses and asks for user approval before executing potentially dangerous commands.

### Model-Agnosticism: The "Quiet Superpower"
▶ [5:07–5:21](https://www.youtube.com/watch?v=aKe71FrwL1o&t=307s)
A key feature of Claude Code is that it is **model-agnostic**. It does not care which "brain" is powering it. By changing a single environment variable (`ANTHROPIC_BASE_URL`), a user can point the same harness at a completely different model, such as a local Ornith instance running on `localhost:8000`, instead of the default Anthropic API.

## The Complete Stack
▶ [5:21–5:36](https://www.youtube.com/watch?v=aKe71FrwL1o&t=321s)
The video presents the full system as a three-layer stack:
```ascii
      +---------------------+
      |         YOU         |
      |      (the goal)     |
      +---------------------+
              ↓
      +---------------------+
      | HARNESS (Claude Code) |
      |      (the hands)    |
      +---------------------+
              ↓
      +---------------------+
      |   MODEL (Ornith)    |
      |      (the brain)    |
      +---------------------+
```
You provide the high-level goal, the harness (Claude Code) provides the safe execution environment and tools, and the model (Ornith) provides the reasoning and planning to achieve the goal.

## The Myth of the Retired Harness
▶ [5:36–6:45](https://www.youtube.com/watch?v=aKe71FrwL1o&t=336s)
The video circles back to debunk the initial hot take: if Ornith can self-scaffold, is a harness like Claude Code just "dead weight"? The answer is a definitive **no**, because the two systems provide two different kinds of scaffolds at different times.
- **Training-Time Scaffold (Ornith):** This is what Ornith learned internally. It's about *how to behave* like a disciplined agent: planning before acting, using tools instead of guessing, checking its own output, and recovering from failure.
- **Runtime Harness (Claude Code):** This provides the tools and safety rails for the agent to *act* on a real machine. It manages the actual file edits and command executions.

Ornith's self-scaffolding training doesn't make the harness obsolete; it makes Ornith a "far better tenant for a harness."

## Practical Setup Guide
▶ [6:45–7:56](https://www.youtube.com/watch?v=aKe71FrwL1o&t=405s)
The video provides a three-step guide to run Ornith inside the Claude Code harness.

```ascii
+----------------+      +----------------+      +--------------+
|   Claude Code  |----->| PROXY / ADAPTER|----->| ORNITH + VLLM|
| (Anthropic fmt)|      | (maps both ways) |      | (OpenAI fmt)   |
+----------------+      +----------------+      +--------------+
```

1.  **Step 1: Serve the model.** Use a tool like **vLLM** to serve the Ornith model on a local port (e.g., 8000), creating an OpenAI-compatible API endpoint.
2.  **Step 2: Use a thin translator.** Because Claude Code expects an Anthropic message format and Ornith speaks an OpenAI format, a small proxy adapter is needed to translate requests and responses between them.
3.  **Step 3: Point Claude Code at the translator.** Set two environment variables in the terminal before running the `claude` command:
    - `export ANTHROPIC_BASE_URL="http://localhost:8000"`
    - `export ANTHROPIC_MODEL="Ornith-1.0-9B"`
This redirects the existing Claude Code CLI to use the local, open brain.

A live demo shows this setup successfully fixing a `TypeError: cannot read 'token' of null` in a failing test file (`auth.test.ts`).

## Performance Reality Check
▶ [7:56–8:43](https://www.youtube.com/watch?v=aKe71FrwL1o&t=476s)
While Ornith is highly capable, the video provides an "honest" assessment of where it stands relative to the absolute frontier.
- **When the open brain wins:** The open, local setup is the clear winner for tasks requiring privacy (code stays on your hardware), offline capability, a permissive MIT license, or zero per-token cost.
- **When the frontier still wins:** For the "hardest, longest-horizon jobs," the most advanced closed-source models (like Opus 4.8) still have a performance edge. The few extra percentage points on benchmarks can be the difference between a task succeeding or stalling.

## The Professional Workflow: Keep the Harness, Swap the Brain
▶ [8:43–9:33](https://www.youtube.com/watch?v=aKe71FrwL1o&t=523s)
The ultimate answer is not to choose one over the other, but to use both. The recommended "pro setup" is:
- **Keep Claude Code as the constant harness.**
- **Swap the brain to fit the job.**
  - Use **Ornith** for default, local, private, and free tasks.
  - Switch to a **frontier model like Opus** for the most difficult tasks where maximum performance is required.

```ascii
        +--------------------------------+
        | Claude Code (the constant)     |
        +--------------------------------+
                     ↑ (Same Harness)
                     ↓ (Swap Below)
+---------------------+ +--------------------+
|    Ornith - local   | |   Opus - frontier  |
| (default, private)  | | (when it counts)   |
+---------------------+ +--------------------+
```

## Conclusion: Not a Fight, A Stack
▶ [9:33–9:58](https://www.youtube.com/watch?v=aKe71FrwL1o&t=573s)
The video concludes by reiterating its main points. The relationship between Ornith and Claude Code is not a fight but a **stack**. An open-weight model is now good enough to be the "brain" in a top-tier "harness," a milestone that was just a research demo a year ago. The myth that a self-scaffolding model retires the harness is false, akin to saying "a better engine retires the car." The best systems combine a great brain with great hands.

```ascii
+----------------+      +-------------+      +-------------+
|     Ornith     |----->| Claude Code |----->| Your Machine|
| (the open brain) |      | (the hands)   |      | (real work)   |
+----------------+      +-------------+      +-------------+
```