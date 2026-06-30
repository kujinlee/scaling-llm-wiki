---
tags:
  - video-summary
  - en
  - deepmind
  - agi
  - transformers
  - diffusion models
  - world models
  - ai strategy
  - continual learning
video_id: "8oyZB24-vAM"
channel: "Pourya Kordi"
lang: EN
type: Analysis
audience: Advanced
score: 4.6
---

# DeepMind Was Two Steps Ahead, AGAIN!

**Channel:** Pourya Kordi | **Duration:** 31:07 | **URL:** https://www.youtube.com/watch?v=8oyZB24-vAM

> [!summary] Quick Reference
> **TL;DR:** This video analyzes DeepMind's unconventional AGI strategy, innovating architectures, embracing diffusion models, and building world models through simulation.
>
> **Key Takeaways:**
> - DeepMind is actively exploring alternatives to standard transformer architectures for efficiency.
> - Diffusion models offer superior speed, efficiency, and flexibility compared to autoregressive LLMs.
> - Developing "world models" through generative AI is key to overcoming "jagged intelligence."
> - The debate between generative and predictive world models is central to AGI development.
> - DeepMind believes large-scale pre-training combined with planning is vital for AGI, differing from critics.
>
> **Concepts:** deepmind · agi · transformers · diffusion models · world models · ai strategy · continual learning

---

## 1. DeepMind's Foundational Bet on AGI
▶ [0:00–0:55](https://www.youtube.com/watch?v=8oyZB24-vAM&t=0s)
DeepMind consistently tackles seemingly intractable problems, much like their investment in AlphaGo. Currently, they are pouring resources into challenges that other AI labs avoid, representing either an extraordinary vision or a significant miscalculation in modern history. The current blueprint of modern AI, based on transformer-based, autoregressive, pre-trained, and generative models, holds immense potential but possesses theoretical limitations preventing human-level intelligence. DeepMind is actively moving beyond these conventional limitations.

---

## 2. Architectural Innovations: Moving Beyond Pure Transformers
▶ [0:55–7:31](https://www.youtube.com/watch?v=8oyZB24-vAM&t=55s)
A core focus for DeepMind is evolving beyond pure transformer models, which, despite their power, suffer from quadratic scaling costs as sequence length increases. While other labs primarily use efficient approximations to manage this, DeepMind actively explores entirely new foundations. Their research includes recurrent and state-space inspired architectures, such as the Titans architecture (Titans, Nested Learning, Titans Plus Miras) which employs a "surprise mechanism" for selective long-term memory. Another key innovation is Recurrent Gemma, built on the Griffin architecture. Griffin mixes gated linear recurrences with local attention, maintaining a fixed-size, evolving "index card" of context instead of a growing KV cache. This design is highly efficient for long contexts. Gemma 4 further refines this with sparsity methods and a hybrid local/global attention mechanism, enabling multimodal models with vast context windows for edge devices. These efforts serve as public experiments for DeepMind's broader AGI strategy.

---

## 3. The Diffusion Paradigm: An Alternative to Autoregressive LLMs
▶ [7:31–15:45](https://www.youtube.com/watch?v=8oyZB24-vAM&t=451s)
Modern LLMs primarily rely on autoregression, predicting the next token sequentially. However, the original transformer was not purely autoregressive. DeepMind and others are exploring diffusion models as a superior alternative for language generation, mirroring their success in image, video, and music generation. Diffusion models offer several advantages: they are significantly more efficient and faster due to parallel iterative refinement, require fewer steps than autoregressive models, and can naturally correct mistakes by working on the entire response holistically. Furthermore, diffusion LLMs provide greater flexibility, allowing prompts at any arbitrary position, which is particularly useful for tasks like code completion. While other major labs like OpenAI are doubling down on autoregressive transformer models, DeepMind is actively developing diffusion-based language models, such as Gemini Diffusion, recognizing the potential for this approach.

---

## 4. The Core Debate: Generative AI, World Models, and AGI
▶ [15:45–26:54](https://www.youtube.com/watch?v=8oyZB24-vAM&t=945s)
A central debate in AI, championed by Demis Hassabis (DeepMind) and Yann LeCun (Meta AI), revolves around the path to AGI, particularly regarding generative models and world models. LeCun argues that next-token prediction works for language due to its constrained nature but is mathematically intractable for natural modalities like video, where the number of possible futures is immense. DeepMind counters that modern video models (like Sora, VEO) don't predict every pixel; instead, they learn to predict within a compressed "latent space" or "visual language," implicitly capturing underlying physics and real-world regularities.

DeepMind posits that generative AI video is a crucial stepping stone to AGI. Current language models exhibit "jagged intelligence," performing exceptionally in narrow tasks but failing at common sense. Human intelligence relies on a wordless internal representation of reality – a "world model" – that language merely approximates. By forcing AI to generate hyperrealistic videos, systems like DeepMind's VEO are compelled to develop an intuitive understanding of physics, object permanence, and causality. This forms the foundation of a world model, essential for long-term planning.

LeCun, however, argues that generative models, with their objective of pixel-level reconstruction, waste compute predicting irrelevant details. He advocates for Joint Embedding Predictive Architectures (JEPA), where the model predicts a *compatible latent representation* of missing parts, not the raw pixels. This encourages learning robust, abstract representations without the burden of perfect reconstruction. While JEPA is theoretically appealing, generative models currently show stronger empirical performance. DeepMind's ultimate strategy involves using generative diffusion models to create hyperrealistic simulations, within which multimodal, autoregressive models like Gemini Omni can train to develop explicit, evolving internal models of reality.

---

## 5. Re-evaluating the Role of Large-Scale Pre-training
▶ [26:54–31:08](https://www.youtube.com/watch?v=8oyZB24-vAM&t=1614s)
DeepMind has consistently advocated for large-scale pre-training as a foundational component for AGI, a philosophy that underpinned breakthroughs like AlphaGo. However, researchers like Ilya Sutskever and Richard Sutton argue that this approach may be a dead end. They contend that massive pre-training inherently assumes an inefficient learner and that a truly intelligent system should be an extremely efficient *continual learner* from experience in messy, dynamic environments, requiring minimal initial pre-training. Human intelligence, they highlight, is not a "finished" pre-trained mind but a continuous process of learning and adapting, with rich internal feedback mechanisms that enable robust and efficient acquisition of new skills. DeepMind's stance is that leveraging all existing world knowledge through large pre-trained multimodal models serves as a powerful "prior" to bootstrap learning, believing these models will be key components, potentially combined with additional planning and search layers, in the final AGI system.

---

## Conclusion
DeepMind's current strategy is a highly specific, multifaceted bet on the future of AGI, simultaneously pushing the boundaries of existing architectures and exploring entirely new paradigms. They are challenging conventional AI wisdom by moving beyond pure transformers, embracing diffusion models over strict autoregression, using generative models to build intuitive world models, and integrating large-scale pre-training with a vision for continual learning in simulated environments. The next few years will reveal whether this extraordinary vision leads to groundbreaking advancements or significant miscalculations in the pursuit of human-level intelligence.