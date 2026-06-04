---
concept: Generative vs. Discriminative Models
category: LLM Internals & Training
summary: The foundational distinction between models that learn the joint distribution p(x,y) to create new data instances and models that learn the conditional p(y|x) to classify or label existing ones.
aliases: [generative vs discriminative, discriminative models, generative models, joint vs conditional distribution, classify vs create, p(x,y) vs p(y|x)]
related: ["[[next-token-prediction]]", "[[generative-world-models]]", "[[foundation-models]]", "[[llm-hallucination]]", "[[supervised-fine-tuning]]"]
sources: [introduction-to-generative-ai]
---

# Generative vs. Discriminative Models

Generative vs. discriminative models is the foundational distinction that defines what "generative AI" actually means as a class of system. A **discriminative** model learns to *classify or predict a label* for a data point — it models the conditional probability distribution p(y|x), answering "what is this?" (e.g. is this image a dog or a cat). A **generative** model instead learns the *joint* probability distribution p(x,y) over the data itself, so it can produce *new* instances that resemble the patterns it was trained on — answering "create something like this" (e.g. generate a picture of a dog). The crisp rule of thumb is the output type: if the output is a number, a class, or a probability, the model is discriminative; if the output is natural language, audio, an image, or other rich content, it is generative. Generative AI is positioned as the subset of deep learning whose models do the latter.

## Key Mechanics

- **Discriminative — learn the boundary, model p(y|x)**: the model estimates the probability of a label given an input, drawing decision boundaries between classes rather than modeling how the data itself is distributed. Its job is identification, not creation.
- **Generative — learn the data, model p(x,y)**: the model captures the joint distribution of inputs and labels, learning the underlying structure of the data well enough to *sample* new, plausible instances from it.
- **Output type as the diagnostic**: the practical test for whether a system is generative AI is what it emits — a class/number/probability marks a discriminative classifier, while generated natural language, audio, or imagery marks a generative model.
- **Both are deep-learning model types**: the distinction sits *within* deep learning — discriminative and generative are two ways of using neural networks, not two separate fields, so the same architectural substrate underlies both.
- **Generation rests on learned structure**: because a generative model has internalized the joint distribution, it produces new content by predicting what fits the learned patterns — the conceptual root of the next-word prediction in language models (`[[next-token-prediction]]`) and of interactive world generation (`[[generative-world-models]]`).

## How It Appears in the Corpus

The Google Cloud "Introduction to Generative AI" tutorial frames generative AI by first separating discriminative models (which learn p(y|x) to classify a data point, e.g. labeling an image "dog" or "cat") from generative models (which learn p(x,y) to generate new instances, e.g. producing a picture of a dog). It positions generative AI as a subset of deep learning and gives the output-type heuristic — number/class/probability means not generative; natural language, audio, or image means generative.

## Tensions & Tradeoffs

- **The distinction is foundational, not architectural**: "generative" vs. "discriminative" describes what a model is trained to *do* (sample data vs. assign labels), not a specific architecture — a transformer can serve either role, so the label is about the learning objective and output, not the network.
- **Generation buys creativity at the cost of verifiability**: a discriminative classifier's output is a checkable label, whereas a generative model produces open-ended content that can be fluent yet wrong — the structural reason generative systems are prone to `[[llm-hallucination]]` in a way pure classifiers are not.
- **The line blurs in practice**: modern foundation models (`[[foundation-models]]`) trained generatively are routinely adapted to discriminative downstream tasks (sentiment classification, captioning), so a single pretrained generative base can be fine-tuned to do discriminative work — the categories describe usage, not a permanent partition.
- **Vantage caveat**: the framing comes from a beginner-oriented vendor tutorial, so the joint/conditional contrast is presented as a clean pedagogical dividing line rather than a sharp technical boundary — the durable idea is *create new data vs. classify existing data*, not the probability notation itself.
