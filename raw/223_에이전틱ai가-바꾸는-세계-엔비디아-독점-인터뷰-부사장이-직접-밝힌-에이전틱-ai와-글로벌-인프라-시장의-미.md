---
tags:
  - video-summary
  - en
  - agent ai
  - enterprise ai
  - nvidia
  - open models
  - ai workflows
  - ai costs
  - ai toolkit
video_id: "b06GM7Ok1io"
channel: "안될공학 - IT 테크 신기술"
lang: EN
type: Analysis
audience: Intermediate
score: 4.2
---

# "에이전틱AI가 바꾸는 세계" 엔비디아 독점 인터뷰 | 부사장이 직접 밝힌 에이전틱 AI와 글로벌 인프라 시장의 미래

**Channel:** 안될공학 - IT 테크 신기술 | **Duration:** 18:10 | **URL:** https://www.youtube.com/watch?v=b06GM7Ok1io

> [!summary] Quick Reference
> **TL;DR:** This video explains how Agent AI moves beyond chatbots to enable autonomous, goal-oriented workflows for enterprises, discussing deployment, cost, and open models.
>
> **Key Takeaways:**
> - Transition from chatbots to autonomous Agent AI for complex, goal-oriented tasks.
> - Utilize secure runtimes like OpenShell to deploy Agent AI from POC to production.
> - Shift cost evaluation from tokens to "cost per complete task" for Agent AI workflows.
> - Adopt hybrid agent architectures combining cloud and specialized open models for optimal control.
> - Start Agent AI adoption with a critical business function and a dedicated "tiger team."
>
> **Concepts:** agent ai · enterprise ai · nvidia · open models · ai workflows · ai costs · ai toolkit

---

## 1. Agent AI: Beyond Chatbots, Towards Autonomous Workflows
▶ [0:54–3:43](https://www.youtube.com/watch?v=b06GM7Ok1io&t=54s)
Agent AI represents a fundamental shift from traditional chatbots to a new kind of workflow. Unlike chatbots that respond to individual prompts, Agent AI is designed for complex, long-running tasks. It involves reasoning, retrieval, tool use (like RAG or code interpreters), and response generation, enabling it to define a plan, understand context, and achieve specific goals autonomously over extended periods, sometimes for hours. This evolution makes AI useful for actions, not just entertainment, as demonstrated in recent keynotes.

---

## 2. Bridging the Gap: From POC to Production with Secure Runtimes
▶ [3:43–5:26](https://www.youtube.com/watch?v=b06GM7Ok1io&t=223s)
Transitioning Agent AI from a proof-of-concept (POC) to a production-ready system presents challenges in data connection, security, cost, and performance. NVIDIA addresses this with its Agent Toolkit, which includes NeMo models, an orchestration harness (like Hermes), and a secure runtime called OpenShell. OpenShell is crucial for enterprise deployment as it enforces guardrails, controlling what an agent can and cannot do, which systems it can access, and where inference occurs. This secure runtime is essential for overcoming integration challenges and enabling reliable production-level AI.

---

## 3. Rethinking Costs and Value in Agent AI Deployment
▶ [5:26–7:43](https://www.youtube.com/watch?v=b06GM7Ok1io&t=326s)
For enterprises adopting Agent AI, cost considerations extend beyond mere token costs. A single request can expand into multiple steps of reasoning and retrieval, making metrics like "cost per complete task" or "cost per successful workflow" more relevant. While token economics may decrease, consumption often increases due to the enhanced capabilities (Jevons paradox). The true value of Agent AI lies in its ability to unlock new markets, enable new products, and significantly boost productivity, often measured in terms of previously impossible outcomes rather than just raw processing cost. Compute serving agents are also proliferating beyond data centers to local devices and edge.

---

## 4. The Rise of Open Models and Hybrid Agent Architectures
▶ [7:43–9:34](https://www.youtube.com/watch?v=b06GM7Ok1io&t=463s)
There's growing enterprise interest in using open models over external APIs for better control over costs and security. Most effective agents are "systems of models," combining powerful cloud frontier models for orchestration and planning with specialized, post-trained open models (like NVIDIA's NeMo) for specific tasks, such as domain-specific research or coding. NVIDIA's commitment to open models includes sharing checkpoints, pre/post-training datasets, algorithms, and research papers, fostering transparency and trust, which are vital for customization and broader adoption within enterprises.

---

## 5. Transforming Specialized Workflows and Software Development
▶ [9:34–14:38](https://www.youtube.com/watch?v=b06GM7Ok1io&t=574s)
Agent AI is profoundly impacting highly specialized engineering workflows, such as RTL verification, and has revolutionized software engineering. Tools like the NVIDIA Agent Toolkit, using CUDA X libraries as skills, allow agents to execute complex tasks much faster—e.g., 40 times faster in chip design with Cadence. This is more than a co-pilot; it's an autonomous entity iteratively working towards an objective, freeing engineers to focus on architecture and problem-solving. This automation doesn't reduce engineer workload but shifts it to higher-value, creative tasks, enabling the design of more systems and chips.

---

## 6. Strategic Deployment: Choosing the Right Starting Point and Environment
▶ [14:38–17:54](https://www.youtube.com/watch?v=b06GM7Ok1io&t=878s)
Enterprise agents are increasingly deployed across hybrid environments—cloud, on-premise, edge, and local PCs—rather than in a single location. The optimal execution environment depends on factors like data security, latency, cost, and user experience. Agents, as systems of models, can leverage powerful cloud orchestrators alongside specialized local models running in an AI factory, on-premise, or even on a DGX Spark station. For initial adoption, enterprises should identify a critical business function (not a "nice-to-have"), form a "tiger team," and go deep on one use case, establishing observability and security policies (via OpenShell) before scaling.

---

## Conclusion
▶ [17:54–18:04](https://www.youtube.com/watch?v=b06GM7Ok1io&t=1074s)
Agent AI is ushering in an era of autonomous, goal-oriented AI systems that fundamentally change how enterprises operate. By enabling complex workflows, secure deployment, flexible cost models, and hybrid architectures with open models, it empowers businesses to unlock new markets and dramatically enhance productivity in specialized domains like engineering and software development. The key to successful adoption lies in strategic, focused implementation on critical business functions, leveraging comprehensive toolkits and secure runtimes.