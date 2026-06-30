---
tags:
  - video-summary
  - en
  - small model inference
  - AI agents
  - context management
  - GPU optimization
  - ML infrastructure
  - open source ML
  - vector databases
video_id: "qdh_x-uRs9g"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Advanced
score: 4.4
---

# The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked

**Channel:** AI Engineer | **Duration:** 18:30 | **URL:** https://www.youtube.com/watch?v=qdh_x-uRs9g

> [!summary] Quick Reference
> **TL;DR:** This video presents an open-source solution for efficient small AI model inference, optimizing GPU usage and providing full-stack infrastructure for production AI agents.
>
> **Key Takeaways:**
> - Small models are vital for agentic workflows to combat "context rot" and reduce token consumption.
> - Optimize small model inference by hot-swapping multiple models on a single GPU to maximize utilization.
> - Effective inference requires end-to-end infrastructure, including routing, auto-scaling, queuing, and monitoring.
> - Support diverse small model architectures by adapting forward passes and optimizing attention mechanisms for efficiency.
> - The Superlinked Inference Engine (SIE) offers a holistic open-source framework for small model deployment.
>
> **Concepts:** small model inference · AI agents · context management · GPU optimization · ML infrastructure · open source ML · vector databases

---

## 1. The Overlooked Challenge of Small Model Inference
This talk addresses a critical oversight in the practical application of AI: efficient inference for small models. While much attention is given to training and fine-tuning large models, the speaker highlights a significant gap in productionizing smaller models, especially for tasks like AI search and document processing. The inspiration for this realization came from feedback on a Substack article where the speaker initially overlooked the complexities of real-world inference.

---

## 2. Why Small Model Inference Matters for Agentic Workflows
Efficient small model inference is crucial for tackling "context rot" in agentic workflows. As context window sizes increase, the quality of agent responses often degrades. Small models can act as powerful preprocessing tools or tool-calling mechanisms to filter and manage context, significantly reducing token consumption for larger agents. This approach aligns with community efforts, including Andrej Karpathy's work on knowledge graphs and Chroma's context management models, demonstrating its real-world applicability in scenarios like e-commerce taxonomy classification.

---

## 3. Debunking Misconceptions About Inference
Contrary to popular belief, effective small model inference isn't simply about throwing more GPUs at the problem. Small models occupy minimal memory (e.g., a few gigabytes), meaning provisioning a dedicated GPU for each leads to substantial idle resources and wasted cost. The key is **hot-swapping** multiple small models on a single GPU, dramatically increasing utilization through mechanisms like a least recently used (LRU) eviction policy. Furthermore, inference isn't just about the server; it encompasses an end-to-end production solution including routing, auto-scaling, queuing, and monitoring, an area where open-source solutions have traditionally been lacking.

---

## 4. The Yin of Inference: Comprehensive Model Support
Effective inference demands robust model support. The open-source landscape is rapidly evolving, with millions of models available on Hugging Face offering increasing accuracy, often outperforming managed services for specific tasks. Supporting this diverse ecosystem is complex because different models (e.g., BERT, Qwen, ColBERT) have varied architectures, requiring distinct implementations for components like flash attention, positional embeddings, and QKV fusion. The solution involves re-implementing the forward pass to adapt to these differences, handle variable-length attention, and optimize padding to prevent wasted compute on empty tokens during token-based batching. This nuanced approach is vital for supporting a wide range of tasks and model types, including late-interaction and cross-encoder models.

---

## 5. The Yang of Inference: Robust Infrastructure
The other half of effective inference is sophisticated infrastructure. The presented solution, the Superlinked Inference Engine (SIE), provides an end-to-end system. Its API primitives (encode, score, extract) are backed by a robust infrastructure layer featuring a router, queuing mechanisms to handle varying loads, and dynamic GPU provisioning across different resource pools (e.g., spot instances, larger GPUs). This system utilizes KEDA auto-scaling with Prometheus metrics to ensure high GPU utilization, prevent idle resources, and enable rapid model switching. The goal is to provide a complete, opinionated framework for users, allowing them to manage models as simple configurations via tools like Terraform, Helm charts, and Docker images.

---

## Conclusion
The Superlinked Inference Engine (SIE) is an open-source solution designed to bridge the gap in small model inference. It offers both comprehensive model support, by intelligently adapting to diverse model architectures and optimizing attention mechanisms, and a full-stack infrastructure for production-grade deployment, including routing, auto-scaling, and GPU provisioning. This holistic approach addresses the real-world challenges of building efficient AI agents and document processing workflows, enabling developers to leverage the power of small open-source models without the burden of complex infrastructure management.