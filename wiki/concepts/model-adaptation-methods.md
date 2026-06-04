---
concept: Model Adaptation Methods
category: LLM Internals & Training
summary: The spectrum of techniques for specializing a foundation model to a task — from prompt design (no weight change) through parameter-efficient tuning (modifying a subset of parameters) to distillation (a teacher model trains a smaller student) — ordered by cost, data, and depth.
aliases: [model adaptation, model tuning methods, model customization, parameter-efficient tuning, PET, adapter tuning, reinforcement tuning, model distillation, teacher-student distillation, tuning spectrum]
related: ["[[foundation-models]]", "[[supervised-fine-tuning]]", "[[in-context-learning]]", "[[automated-prompt-optimization]]", "[[rlhf]]", "[[on-device-inference]]", "[[expert-domain-defensibility]]", "[[per-node-model-routing]]", "[[next-token-prediction]]"]
sources: [introduction-to-vertex-ai-studio]
---

# Model Adaptation Methods

Model adaptation methods are the family of techniques for specializing a general `[[foundation-models|foundation model]]` to a particular task, arranged as a spectrum from lightest to heaviest by how much they cost, how much data they need, and how deeply they reshape the model. At one end, **prompt design** steers a frozen pretrained model with no parameter change at all; in the middle, **parameter-efficient tuning (PET)** modifies only a small subset of the model's parameters; at the far end, **distillation** trains a separate, smaller "student" model from a larger "teacher." The unifying logic is amortization made flexible: one expensive base model is adapted by whichever method matches the task's stakes, data, and latency budget — cheap prompt-level steering for the common case, deeper tuning only where it earns its cost.

## Key Mechanics

- **Prompt design — guide without changing weights**: the cheapest, non-technical method shapes a pretrained model's behavior through instructions and examples (`[[in-context-learning]]`) without altering any parameters, enabling rapid experimentation. It is the no-training-run baseline — the same adapt-the-base instinct as the rest of the spectrum, applied entirely at inference time.
- **Parameter-efficient tuning (PET) — modify a subset**: a more technical approach that updates only a *fraction* of a large model's parameters rather than retraining the whole thing, sharply cutting computational cost. Variants include supervised **adapter tuning** (which can work from as few as ~100 labeled examples) and unsupervised **reinforcement tuning**. PET is the middle ground: real weight change, but bounded.
- **Distillation — teacher trains a student**: a larger, more capable "teacher" model trains a smaller "student" model to perform a specific task, producing a compact model with lower latency and cost. It uses labeled examples plus *rationales* (explanations from the teacher) so the student inherits not just answers but reasoning. The output is a *different, smaller model* — the heaviest adaptation, and the one that changes the deployed artifact's size.
- **Tuning as a configured job**: the deeper methods run as a training job — define the base model, supervised or unsupervised mode, and a training dataset (e.g. a JSON file of input/output pairs in cloud storage) — and the resulting tuned model is registered for deployment or further testing. Adaptation becomes a repeatable pipeline, not a one-off.
- **The ordering is the insight**: prompt design → PET → distillation ascends in technical effort, data requirements, and how much of the model is touched, so the method is chosen by matching the task's value and constraints to the cheapest rung that suffices.

## How It Appears in the Corpus

The Google Cloud "Introduction to Vertex AI Studio" tutorial lays out model tuning as a progression: prompt design (a non-technical method that guides behavior without changing parameters), parameter-efficient tuning (modifying a subset of parameters — supervised adapter tuning from as few as 100 examples, and unsupervised reinforcement tuning), and distillation (a Google-Cloud-exclusive technique where a teacher model trains a smaller student using labeled examples and rationales for lower latency and cost). It describes launching a tuning job by selecting the base model, mode, and a JSON training dataset, with tuned models registered in a model registry for deployment.

## Tensions & Tradeoffs

- **It is the spectrum `[[in-context-learning]]` and `[[supervised-fine-tuning]]` are points on**: in-context learning is the weight-free prompt-design rung; SFT is a fuller-weight supervised tuning that turns a base model into an assistant. This page names the *ordering* that connects them — adapt with the cheapest method that meets the need, escalate only when it does not.
- **Cost/depth vs. capability**: prompt design is instant and free but bounded to what the base can already do; PET buys more capability for modest data and compute; distillation buys a cheaper, faster *deployable* model but requires a capable teacher and a full training pipeline — each rung trades more effort for deeper or cheaper-to-serve specialization.
- **Distillation feeds `[[on-device-inference]]`**: because distillation produces a smaller student with lower latency and cost, it is one route to the compact, edge-deployable models that on-device inference depends on — the adaptation method that directly serves the small-model end of the spectrum.
- **Distinct from `[[automated-prompt-optimization]]` and `[[rlhf]]`**: automated prompt optimization searches for a better *prompt* (staying on the prompt-design rung) against an eval set; RLHF is a specific reinforcement-based post-training of the full model. Reinforcement *tuning* here is the lighter, parameter-efficient cousin — same RL idea, far fewer parameters touched.
- **Adaptation is where defensibility lives**: because the expensive base is shared, the durable advantage for a builder is in the *adaptation and proprietary data* layered on top, exactly the model-domain-vs-expert-domain split of `[[expert-domain-defensibility]]` — these methods are the concrete tools that build that layer.
- **Vantage caveat**: the method taxonomy and the specific claims (adapter tuning from ~100 examples, distillation as a vendor-exclusive teacher-student technique) come from a beginner-oriented vendor tutorial, so they illustrate the *pattern* — a cost/depth-ordered spectrum of base-model adaptation — rather than measured results or universal techniques; the durable idea is the adaptation hierarchy, not any one platform's offerings.
