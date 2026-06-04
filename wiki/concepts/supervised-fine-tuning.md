---
concept: Supervised Fine-Tuning
category: LLM Internals & Training
summary: Post-training a base model on human-curated conversation examples so it imitates a helpful assistant — turning a token-autocomplete into a chatbot that statistically simulates a data labeler.
aliases: [supervised fine-tuning, SFT, post-training, instruction tuning, conversation fine-tuning, simulation of a data labeler]
related: ["[[next-token-prediction]]", "[[rlhf]]", "[[reasoning-reinforcement-learning]]", "[[sycophantic-agreement]]", "[[llm-hallucination]]", "[[jagged-intelligence]]"]
sources: [deep-dive-into-llms-like-chatgpt]
---

# Supervised Fine-Tuning

Supervised fine-tuning (SFT) is the first post-training stage that converts a knowledgeable-but-inert base model into an interactive assistant. The base model produced by `[[next-token-prediction]]` is only a "token autocomplete"; SFT trains it further on a much smaller dataset of *human-curated conversations*, so it learns to adopt the persona of a helpful assistant that answers questions and follows instructions. The defining reframing is that talking to a fine-tuned model is conversing with a "neural network simulation of a data labeler" — the assistant's voice and values are a statistical imitation of the human labelers, working from the labeling instructions, employed by the company that trained it.

## Key Mechanics

- **Imitate curated conversations**: the model is trained on example dialogues encoded into token sequences with special tokens delineating user and assistant turns, learning to produce the assistant side.
- **Labelers follow explicit instructions**: human labelers craft ideal assistant responses guided by detailed "labeling instructions" (be helpful, truthful, harmless) across a diverse range of prompts — so the assistant's behavior is shaped by those written guidelines.
- **Synthetic data at scale**: modern SFT pipelines lean heavily on *other LLMs* to generate synthetic conversations, which humans then edit and refine — scaling the dataset beyond what hand-written examples alone could supply.
- **Statistical imitation, not new knowledge**: SFT mostly reshapes *behavior* (persona, format, instruction-following) rather than adding facts; the model imitates the distribution of labeler responses.
- **Cheap relative to pre-training**: the dataset is far smaller and the stage is computationally light compared with `[[next-token-prediction]]`, yet it is what makes the model usable.

## How It Appears in the Corpus

The Andrej Karpathy "Deep Dive into LLMs like ChatGPT" tutorial presents SFT as stage three: training the base model on human-curated conversations encoded with turn-delimiting special tokens, guided by labeling instructions, increasingly augmented by LLM-generated synthetic dialogues. Its memorable framing is that interacting with ChatGPT is conversing with "a neural network simulation of a data labeler" from the training company.

## Tensions & Tradeoffs

- **The assistant persona is imitation, not understanding**: SFT teaches the model to *sound like* a helpful labeler, which underlies the corpus's observations that the model agrees too readily (`[[sycophantic-agreement]]`) and is unevenly competent (`[[jagged-intelligence]]`) — it is simulating a helpful answerer, not reasoning about correctness.
- **Quality is bounded by the labeling instructions and labelers**: the model inherits the values, blind spots, and errors encoded in the guidelines and the labelers' judgments — "helpful, truthful, harmless" is only as good as how those words were operationalized.
- **Distinct from `[[rlhf]]` and `[[reasoning-reinforcement-learning]]`**: SFT *imitates* expert solutions, whereas reinforcement learning has the model *discover* solution paths by trial and error — SFT sets the persona, RL sharpens problem-solving, and they are sequential, not interchangeable.
- **Imitation can entrench hallucination**: training the model to confidently mirror well-formed answers — even where the base model's knowledge is thin — reinforces the fabrication problem that `[[llm-hallucination]]` describes, which is why refusal must be explicitly trained in.