---
concept: Age of Research
category: LLM Internals & Training
summary: The thesis that AI progress is shifting from scaling laws toward fundamental research as pre-training data becomes scarce relative to available compute.
aliases: [age of research, scaling-to-research shift, end of scaling, post-scaling era]
related: [value-functions, reward-hacking, continuous-learning, research-aesthetics]
sources: [ilya-sutskever-we-re-moving-from-the-age-of-scaling-to-the-a]
---

# Age of Research

The age of research is the thesis that AI progress is shifting away from an era dominated by scaling laws and pre-training toward a return to fundamental research. Pre-training data is finite while compute is now abundant, so simply enlarging models yields diminishing returns. The open problems — generalization and sample efficiency — are research problems about *how* models learn, not engineering problems solved by bigger runs.

## Key Mechanics

- Scaling laws and pre-training are approaching their limits as usable data becomes scarce relative to available compute.
- The field returns to a research era reminiscent of earlier AI, but now equipped with vastly more computation to explore new architectures and training methods.
- Central research targets are the sample-efficiency and generalization gaps — understanding why models need exponentially more data and explicit rewards than humans, who learn continuously from unstructured experience (see `[[value-functions]]`).

## How It Appears in the Corpus

This is the titular thesis of the Ilya Sutskever / Dwarkesh Patel interview: "moving from the age of scaling to the age of research," with the speaker questioning whether a genuine paradigm shift beyond scaling is required.

## Tensions & Tradeoffs

- It remains open whether a true paradigm shift (new methods/architectures) is necessary, or whether scaling plus refinements still has room to run.
- Tension with metric-driven progress: continuing to chase benchmark scores (`[[reward-hacking]]`) can mask the absence of the fundamental generalization gains the research era is meant to deliver.