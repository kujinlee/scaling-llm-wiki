---
concept: Tokenization
category: LLM Internals & Training
summary: Converting filtered text into a one-dimensional sequence of discrete sub-word tokens via Byte Pair Encoding — the numerical substrate a neural network actually consumes.
aliases: [tokenization, byte pair encoding, BPE, tokens, vocabulary, sub-word units, token IDs]
related: ["[[next-token-prediction]]", "[[tokens-to-think]]", "[[supervised-fine-tuning]]", "[[mixture-of-experts]]", "[[on-device-inference]]"]
sources: [deep-dive-into-llms-like-chatgpt]
---

# Tokenization

Tokenization is the step that turns raw text into the numerical form a neural network can process: a continuous stream of characters is converted into a one-dimensional sequence of discrete symbols called *tokens*, each a sub-word unit drawn from a fixed vocabulary. It sits at the very front of the LLM pipeline — after vast internet text is collected and filtered, but before any training happens — and the choices made here (vocabulary size, how words are split) silently shape both the model's efficiency and a class of its later cognitive deficits. The dominant method is **Byte Pair Encoding (BPE)**, which builds a vocabulary large enough to keep sequences short while small enough to stay manageable.

## Key Mechanics

- **Filter first, then tokenize**: raw web text (e.g. Common Crawl, indexing billions of pages since 2007) is heavily filtered — URL blacklisting (spam, malware, adult content), HTML text extraction, language filtering (e.g. English-only), and PII removal — condensing the internet to a high-quality corpus (the cited FineWeb is ~44 TB).
- **Text must become numbers**: a network cannot operate on characters, so text is mapped to a sequence of discrete token IDs — the universal input format for the Transformer.
- **Byte Pair Encoding balances two pressures**: BPE merges frequent byte/character pairs into single tokens, trading a *larger vocabulary* (GPT-4 cited at >100,000 unique tokens) for *shorter sequences*. Tools like TickTokenizer show how a phrase such as "hello world" decomposes into specific token IDs.
- **Sub-word, not word or character**: tokens are typically word fragments, so common words may be one token while rare strings fragment into several — the unit the model reasons over is neither letters nor whole words.
- **Scale of the substrate**: the resulting training sequence is enormous — FineWeb yields ~15 trillion tokens — the raw material `[[next-token-prediction]]` trains against.

## How It Appears in the Corpus

The Andrej Karpathy "Deep Dive into LLMs like ChatGPT" tutorial opens with data and tokenization as stage one of building an LLM: filtering Common Crawl down to a FineWeb-style corpus, then converting that text into a one-dimensional token sequence via BPE, illustrating token IDs with TickTokenizer and citing GPT-4's 100k+ vocabulary and FineWeb's 15 trillion tokens.

## Tensions & Tradeoffs

- **Vocabulary size is a genuine tradeoff**: a larger vocabulary shortens sequences (cheaper attention, longer effective context) but inflates the embedding/output table and dilutes per-token training signal — there is no free choice, only a balance point.
- **Token boundaries cause downstream cognitive deficits**: because the model sees tokens, not characters, character-level tasks (counting letters, spelling manipulation) are unnaturally hard — a root cause of the failures `[[tokens-to-think]]` and `[[jagged-intelligence]]` describe, traceable directly to this representation choice.
- **Filtering quality bounds the model**: the corpus the model learns from is exactly what survives filtering, so blacklist and extraction decisions made here set an upper bound on what pre-training can learn — garbage filtered in is garbage learned.
- **A fixed vocabulary is a frozen assumption**: tokens are decided before training and baked in, so domains, languages, or symbol systems poorly covered by the vocabulary remain awkward for the life of the model.