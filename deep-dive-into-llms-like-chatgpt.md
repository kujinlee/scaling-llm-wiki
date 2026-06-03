---
tags:
  - video-summary
  - en
  - large language models
  - llms
  - ai training
  - neural networks
  - reinforcement learning
  - tokenization
  - supervised fine-tuning
video_id: "7xTGNNLPyMI"
channel: "Andrej Karpathy"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.8
---

# Deep Dive into LLMs like ChatGPT

**Channel:** Andrej Karpathy | **Duration:** 3:31:24 | **URL:** https://www.youtube.com/watch?v=7xTGNNLPyMI

> [!summary] Quick Reference
> **TL;DR:** This video details the multi-stage process of building Large Language Models (LLMs) like ChatGPT, covering data processing, pre-training, fine-tuning, and advanced reasoning.
>
> **Key Takeaways:**
> - LLMs begin with vast, filtered internet text data, tokenized into numerical sequences for neural networks.
> - Pre-training involves Transformer models predicting the next token from massive datasets, creating a base model for text generation.
> - Supervised Fine-tuning (SFT) uses human-curated conversations to transform base models into helpful AI assistants.
> - LLMs hallucinate and have "cognitive deficits"; external tools and step-by-step reasoning mitigate these limitations.
> - Reinforcement Learning, including RLHF, enables advanced reasoning by rewarding solutions or aligning with human preferences.
>
> **Concepts:** large language models · llms · ai training · neural networks · reinforcement learning · tokenization · supervised fine-tuning

---

## 1. The Foundation: Data and Tokenization
The journey of building a Large Language Model (LLM) like ChatGPT begins with acquiring and processing vast amounts of text data, primarily from the internet. This involves leveraging resources like Common Crawl, which has indexed billions of web pages since 2007. A crucial step is extensive data filtering, including URL blacklisting (removing spam, malware, adult content), sophisticated text extraction from raw HTML, language filtering (e.g., keeping only English for a specific model), and removal of Personally Identifiable Information (PII). A representative dataset like FineWeb, despite the internet's size, condenses to about 44 terabytes of high-quality, diverse text.

Once raw text is collected, it must be converted into a numerical format for neural networks. This process, called tokenization, transforms continuous text into a one-dimensional sequence of discrete symbols or "tokens." While basic computer representations use bits or bytes, LLMs employ Byte Pair Encoding (BPE) to create a larger vocabulary (e.g., GPT-4 uses over 100,000 unique tokens) while maintaining manageable sequence lengths. Tools like TickTokenizer illustrate how phrases like "hello world" are broken down into specific token IDs. This results in massive sequences, such as FineWeb's 15 trillion tokens, forming the raw material for the next stage.
---
## 2. Pre-training: Building the Brain of an LLM
With the tokenized data, the next stage involves training neural networks, specifically the Transformer architecture. The core task is to model the statistical relationships of how tokens follow each other. The neural network is fed "windows" of tokens (up to thousands in length) and trained to predict the next token in the sequence. Initially, the network's billions of parameters (weights) are randomly set, leading to random predictions. Through an iterative process, the network's parameters are adjusted via mathematical updates, nudging the probabilities of correct next tokens higher. This continuous "training" aligns the network's predictions with the statistical patterns observed in the vast text dataset.

The computational demands are immense, requiring thousands of powerful GPUs working in parallel within data centers. Researchers monitor a "loss" metric, which ideally decreases over time, indicating improved prediction accuracy. While the internal mathematical details of a Transformer can be complex, the essence is a fixed function transforming input tokens into output probabilities. This pre-training stage results in a "base model"—an internet document simulator capable of generating text with statistical properties similar to its training data.
---
## 3. From Raw Model to Helpful Assistant: Supervised Fine-tuning (SFT)
The base model, while knowledgeable, isn't yet a helpful AI assistant. It merely acts as a "token autocomplete," completing text sequences based on its training. To transform it into an interactive assistant capable of answering questions and engaging in conversations, a "post-training" stage, specifically Supervised Fine-tuning (SFT), is employed. This stage is computationally less expensive than pre-training but crucial for shaping the model's behavior.

SFT involves training the base model on a new, much smaller dataset comprised of human-curated conversations. These conversations are carefully encoded into token sequences using specific protocols, interspersing special tokens to delineate user and assistant turns. Human labelers, guided by detailed "labeling instructions" (e.g., be helpful, truthful, harmless), craft ideal assistant responses to a diverse range of prompts. Modern SFT pipelines also extensively leverage other LLMs to generate synthetic conversations, which are then often edited and refined by humans. The model learns to statistically imitate these human-labeled examples, adopting the persona of a helpful assistant. Therefore, interacting with ChatGPT can be thought of as conversing with a "neural network simulation of a data labeler" from the company that trained it.
---
## 4. Understanding LLM Cognition: Strengths, Weaknesses, and Tool Use
LLMs exhibit unique cognitive traits and limitations. A prominent issue is "hallucinations," where models fabricate information, especially when uncertain. This arises from their tendency to confidently imitate the style of correct answers seen in training, even when lacking factual knowledge. Mitigation involves explicitly training models to refuse to answer when they "don't know."

To overcome the inherent limitations of their "vague recollection" (knowledge stored in parameters), LLMs can be equipped with "tools." By learning to emit special tokens (e.g., `search_start`, `code_start`), models can pause generation, execute external functions (like web searches or code interpreters), and integrate the retrieved information into their "working memory" (the context window). This greatly enhances factuality and problem-solving.

However, LLMs also suffer from "cognitive deficits" due to their token-based processing and finite computation per token. They struggle with tasks requiring precise, distributed reasoning (e.g., complex multi-step math problems, counting characters, or intricate spelling manipulation) if not given enough "tokens to think" (intermediate steps). For such tasks, explicit step-by-step reasoning or leveraging external tools (like a Python interpreter) dramatically improves accuracy, highlighting that models need sequential tokens to perform complex "mental arithmetic." LLMs also lack a true "self" or persistent identity; their "self-knowledge" is a programmed statistical imitation.
---
## 5. The Frontier: Reinforcement Learning for Advanced Reasoning
The final, and most advanced, stage of LLM training is Reinforcement Learning (RL), analogous to "practice problems" in human education. Unlike SFT, which imitates expert solutions, RL encourages models to discover optimal solution paths through trial and error. The model generates numerous solutions for a given prompt, and those leading to a correct answer are reinforced, iteratively refining the model's strategy. This process, particularly as seen in models like DeepSeek R1, cultivates "thinking" or "reasoning" capabilities, where the model generates internal monologues and chains of thought (e.g., "wait, let me check my math again") to improve problem-solving accuracy in verifiable domains like math and coding. This results in longer, more reflective responses and represents an emergent cognitive strategy, not explicitly programmed by humans.

For unverifiable domains (e.g., creative writing, joke generation), Reinforcement Learning from Human Feedback (RLHF) is employed. This involves training a separate "reward model" to simulate human preferences by having humans rank multiple model-generated responses. The reward model then acts as an automated "human simulator," allowing the LLM to learn which types of responses are preferred by humans without extensive human labor. While RLHF improves models in diverse domains, it faces limitations as reward models can be "gamed" by the LLM, preventing indefinite scaling compared to RL in perfectly verifiable domains (like the game of Go, where AlphaGo surpassed human experts). The potential for RL to uncover novel, even superhuman, reasoning strategies remains a key area of research.
---
## Conclusion
Building and training Large Language Models is a multi-stage process akin to human education, encompassing pre-training for foundational knowledge, supervised fine-tuning for expert imitation, and reinforcement learning for problem-solving mastery. These powerful tools, while capable of remarkable feats, are statistical simulations and should be treated with caution. They exhibit "Swiss cheese" capabilities, with surprising deficiencies (e.g., hallucinations, simple arithmetic errors) alongside advanced skills. Users are advised to leverage LLMs as creative assistants and productivity tools, always verifying their outputs and employing strategies like providing explicit context, encouraging step-by-step reasoning, and utilizing external tools to mitigate their inherent limitations. The field is rapidly advancing, with future models expected to be multimodal, integrate into long-running agents, and potentially unlock novel forms of AI cognition.