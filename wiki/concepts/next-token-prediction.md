---
concept: Next-Token Prediction
category: LLM Internals & Training
summary: The pre-training task of training a Transformer to predict the next token over trillions of tokens, producing a knowledgeable but un-aligned "base model" that simulates internet documents.
aliases: [next-token prediction, pre-training, base model, language model pretraining, internet document simulator, token autocomplete, Transformer training]
related: [tokenization, supervised-fine-tuning, llm-hallucination, mixture-of-experts, age-of-research, tokens-to-think]
sources: [deep-dive-into-llms-like-chatgpt]
---

# Next-Token Prediction

Next-token prediction is the core pre-training task that builds the foundational knowledge of an LLM: a Transformer is fed windows of tokens and trained to predict the *next* token in the sequence, over and over, across trillions of tokens. There is no notion of "helpfulness" or "truth" in this objective — only statistical modelling of how tokens follow one another in the training corpus. What emerges is a **base model**: an "internet document simulator" that can generate text with the statistical properties of its training data, deeply knowledgeable yet not yet a usable assistant. It is the single most computationally expensive stage of building an LLM and the substrate every later stage refines.

## Key Mechanics

- **Predict the next token**: the network ingests a window of tokens (up to thousands long) and outputs a probability distribution over the vocabulary for what comes next — the whole task, repeated across the corpus.
- **Iterative weight adjustment**: the model's billions of parameters start random (so predictions start random); mathematical updates nudge the probability of the *correct* next token upward each step, monitored by a *loss* metric that should fall over time.
- **The Transformer is a fixed function**: architectural internals aside, the network is a deterministic function mapping input tokens to output probabilities — complexity lives in the learned weights, not in branching logic.
- **Massive parallel compute**: training demands thousands of GPUs running in parallel in datacenters — the dominant cost of model creation, and the reason `[[mixture-of-experts]]` and serving economics matter.
- **Output is a base model, not an assistant**: the result is a "token autocomplete" that continues documents in-distribution. It holds vast knowledge but only *vaguely*, stored implicitly in parameters — and it has no persona, no instruction-following, and no notion of answering a question.

## How It Appears in the Corpus

The Andrej Karpathy "Deep Dive into LLMs like ChatGPT" tutorial presents pre-training as stage two: feeding tokenized windows to a Transformer, predicting the next token, watching loss decrease across thousands of GPUs, and arriving at a base model characterized as an internet document simulator — knowledgeable but merely a statistical text generator until post-training reshapes it.

## Tensions & Tradeoffs

- **A base model is not helpful by itself**: next-token prediction yields knowledge and fluency but not an assistant — that requires `[[supervised-fine-tuning]]` to imitate a helpful persona and reinforcement learning to sharpen reasoning, so pre-training is necessary but far from sufficient.
- **Knowledge is a vague parametric recollection**: facts are stored implicitly and lossily in the weights, which is precisely why the model `[[llm-hallucination|hallucinates]]` when its recollection is thin — the pre-training objective rewards plausible continuation, not factual accuracy.
- **Data is the binding constraint**: the objective is trivial to state but only as good as the corpus and its scale — and the corpus warns (`[[age-of-research]]`) that usable pre-training data is finite relative to compute, so simply training on more tokens yields diminishing returns.
- **Expensive and one-shot**: the compute cost concentrates here, and the base model's knowledge is frozen at training time — keeping it current means re-training or bolting on retrieval/tools rather than continuing the pre-training loop.