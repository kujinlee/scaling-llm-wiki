---
tags:
  - video-summary
  - en
  - language models
  - post-training
  - supervised fine-tuning (SFT)
  - reinforcement learning from human feedback (RLHF)
  - DPO
  - instruction following
  - LLM
  - data annotation
  - AI alignment
video_id: "2oH6PWPrYFo"
channel: "Stanford Online"
lang: EN
type: Analysis
audience: Intermediate
score: 4.2
---

# Stanford CS336 Language Modeling from Scratch | Spring 2026 | Lecture 15: Mid/Post-Training

**Channel:** Stanford Online | **Duration:** 1:19:55 | **URL:** https://www.youtube.com/watch?v=2oH6PWPrYFo

> [!summary] Quick Reference
> **TL;DR:** This video explains post-training of language models through Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF) to enable instruction following and alignment.
>
> **Key Takeaways:**
> - Post-training (SFT, RLHF) is essential to turn pre-trained LLMs into instruction-following and aligned agents.
> - Supervised Fine-Tuning (SFT) has evolved from general NLP data to specialized, high-quality, and model-generated instruction data.
> - RLHF (Reinforcement Learning from Human Feedback) aligns models by maximizing a reward learned from human preference rankings.
> - DPO (Direct Preference Optimization) simplifies RLHF by directly optimizing preferences without needing a separate reward model.
> - RLHF faces challenges like overoptimization, model collapse, and uncalibrated confidence, necessitating careful implementation.
>
> **Concepts:** language models · post-training · supervised fine-tuning (SFT) · reinforcement learning from human feedback (RLHF) · DPO · instruction following · LLM · data annotation · AI alignment

---

## 1. The Imperative of Post-Training for Language Models
The lecture introduces post-training as a crucial and "artisanal" phase in language model development, distinguishing it from the broad scalability of pre-training. While pre-training can yield a "souped-up GPT-3," its utility for instruction following and reliability is limited compared to models like ChatGPT. The goal of post-training is to bridge this gap, enabling models to accurately interpret and respond to complex prompts—a capability deemed "instruction following." This process moves from a "primordial soup" of pre-training to explicitly extracted behaviors through meticulous data collection and engineering, a task often messier than architectural design. Information on frontier post-training, particularly data collection guidelines, is sparse due to trade secrets and competitive dynamics, with many public references being older works like the InstructGPT and Anthropic HH papers.

---

## 2. Supervised Fine-Tuning (SFT): The Data-Driven Foundation
SFT is presented as the initial and primarily data-centric phase of post-training. It involves collecting high-quality input-output pairs to fine-tune a pre-trained model. The lecture outlines the historical evolution of SFT data:
*   **FLAN (Google T5):** Early approach using existing NLP datasets for multitask training. Faced issues with unnatural structures, short/hallucinated outputs, and lower quality from source datasets. It aimed for scale, but later recognized that strong pre-trained models need fewer *high-quality* examples.
*   **Self-Instruct:** Pioneered using models themselves to generate instruction-following data.
*   **Distillation Approaches (Alpaca, Vicuna):** Leveraged traces from powerful models like ChatGPT to create chat-style input-output pairs, effectively inducing ChatGPT-like behavior on smaller models (e.g., Llama).
*   **Human-Driven Efforts (Open Assistant):** A large crowdsourced initiative to build high-quality, expert-written prompts and responses, similar to Wikipedia, though challenging to sustain.
*   **Advanced LM-Generated Data (WizardLM, Tulu 3):** Developed more sophisticated methods for language models to generate instruction-following data.
*   **Agentic SFT (Neotron):** Recent shift towards training models for tool use and agent systems, incorporating structured formats like tool calls and to-do lists within SFT data.
These developments highlight a transition towards more "chatty," detailed, and expert-driven data, and increasingly, data for agentic capabilities.

---

## 3. Navigating the Minefield: Challenges in SFT Data Collection
Collecting high-quality SFT data is fraught with challenges:
*   **Style and Length Variation:** Conscious data collection decisions significantly influence a chatbot's tone and response length. Evaluators often favor detailed or bullet-pointed responses, which can inflate engagement signals without necessarily improving core model capabilities, necessitating separate control for style versus capability.
*   **Tail Knowledge and Hallucinations:** Training models on facts they don't inherently know, especially when tied to specific formats (e.g., "reference:"), can lead to "tail knowledge" and induce hallucinations. This is because the model learns both the knowledge and the format, misgeneralizing to emit unknown facts. Reinforcement learning (RL) is suggested as a method to help models calibrate what they know and don't know, preventing forced emission of unknown knowledge.
*   **Safety Tuning:** Post-training is critical for implementing safety controls, balancing a low "violation rate" (allowing harmful queries) with a low "false refusal rate" (overly cautious responses to legitimate queries). This involves creating tailored datasets of unsafe behaviors and jailbreaks, with corresponding refusal responses. Surprisingly, even a few hundred examples can significantly reduce safety issues, suggesting that pre-trained models already contain latent "safe/unsafe" axes that can be readily steered.
*   **Integrating SFT into Pre-training:** A growing trend blurs the lines between pre-training and SFT by incorporating high-quality, instruction-tuning data into the later stages (decay phase) of pre-training. This "two-phase training" emphasizes quality data when the learning rate is low, enhancing instruction following capabilities and making it harder to define a "base model" in the traditional sense.

---

## 4. Reinforcement Learning from Human Feedback (RLHF): Shifting to Reward Maximization
RLHF represents a fundamental conceptual shift from generative modeling (SFT) to *maximizing a reward*. Unlike SFT, which fits a distribution, RLHF aims to find a policy that optimizes a downstream reward (e.g., user engagement, math problem-solving), even if it means collapsing the distribution to a single point for an input. This approach is favored because human preferences can differ from their generated demonstrations, and verification is often easier than generation (e.g., proof checking).

The RLHF process involves:
1.  A pre-trained and SFT-tuned model generates multiple outputs for a prompt.
2.  Human annotators rank these outputs.
3.  A reward model is trained on these human rankings.
4.  Reinforcement learning algorithms then maximize the scores given by the reward model.

Data collection primarily uses pairwise comparisons where annotators choose between two model responses. Annotation guidelines (e.g., InstructGPT, Google Bard) typically balance helpfulness, truthfulness, and harmlessness. There's a notable trend towards more expert and highly compensated annotators (e.g., doctors, lawyers for specialized tasks), moving beyond the traditional low-cost crowd-worker model, though the latter still exists. Challenges include preventing annotators from using AI, unrealistic time pressures, and managing the significant influence annotator demographics and expertise have on model behavior (e.g., political alignment, emphasis on formatting vs. factuality). The lecture also notes a shift towards model-generated annotations (e.g., UltraChat, UltraFeedback), which offer scalability and often comparable performance to human annotations for catching up to frontier capabilities, though human expertise remains crucial for pushing the frontier.

---

## 5. RLHF Algorithms: From PPO Complexity to DPO Simplicity
The core algorithmic challenge in RLHF is to maximize the policy's expected reward while keeping it close to the reference pre-trained model (controlled by a KL divergence term).
*   **PPO (Proximal Policy Optimization):** This standard RL algorithm starts from the policy gradient identity, which is essentially weighted SFT. To address the expensiveness of on-policy sampling, PPO uses off-policy techniques with importance weighting and a heuristic clipping mechanism to prevent policy updates from deviating too far from the current policy. While effective, PPO is known for its complexity.
*   **DPO (Direct Preference Optimization):** Developed as a simpler, more stable alternative to PPO, DPO eliminates the need for a separate reward model and on-policy sampling. It leverages the insight that if the policy can be non-parametric, the optimal solution for the RLHF objective can be expressed in closed form: the reference policy exponentially tilted by the reward. This allows for a direct optimization objective that simplifies to increasing the log-likelihood of preferred responses and decreasing that of dispreferred responses, with step sizes scaled by how "wrong" the model's current probabilities are. DPO is significantly less complex, effectively resembling a form of differential SFT. It has proven reasonably effective and is used in models like Llama, though its performance relative to PPO can be sensitive to experimental setup.

---

## 6. The Enduring Challenges and Future Direction of RLHF
Despite advancements, RLHF faces several significant challenges:
*   **Overoptimization:** A major pitfall is overfitting to the learned reward model. The KL regularizer in the RLHF objective is crucial to prevent the policy from becoming degenerate by exploiting flaws in the reward model rather than genuinely improving.
*   **Model Collapse/Lack of Diversity:** RL policies, by nature, are designed to maximize reward, which can lead to a collapse in output diversity, concentrating on only a few highly rewarded responses. This is a fundamental difference from generative modeling, which intrinsically maintains diversity.
*   **Uncalibrated Models:** Post-RLHF models often become uncalibrated, meaning their confidence scores do not accurately reflect the likelihood of correctness. This is a recognized open problem, particularly relevant for future advancements in areas like reasoning.
RLHF data collection remains inherently difficult and messy. While algorithms like DPO have simplified the optimization step, the overall process is complex. The transition to "RL from AI Feedback" (RLAIF) or "RL from Verifiable Rewards" (RLVR) is seen as a promising path to overcome overoptimization by using intrinsically robust rewards (e.g., for verifiable math proofs), allowing for more monotonic performance gains with increased compute.

---

## Conclusion
Post-training is a critical and intricate process essential for transforming pre-trained language models into instruction-following, utility-driven agents like ChatGPT. This involves a delicate interplay of Supervised Fine-Tuning (SFT) for foundational behavior shaping and Reinforcement Learning from Human Feedback (RLHF) for nuanced alignment with human preferences and values. The evolution of data collection for both SFT and RLHF reflects a continuous quest for higher quality, more specialized, and increasingly model-generated annotations. While algorithmic advancements like DPO have simplified optimization, the core challenges remain rooted in the messiness of data, the biases of annotators, and the inherent risks of overoptimization and model collapse. Addressing these complexities is paramount for pushing the frontiers of responsible and capable AI.