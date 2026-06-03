---
tags:
  - video-summary
  - en
  - ai governance
  - autonomous systems
  - policy as data
  - runtime enforcement
  - enterprise architecture
  - software compliance
  - agentic ai
video_id: "TxottTsaOnE"
channel: "Jesper Lowgren"
lang: EN
type: Framework
audience: Advanced
score: 4.4
---

# Policy as Data Explained: Why Policy as Code Fails for Agentic AI

**Channel:** Jesper Lowgren | **Duration:** 7:12 | **URL:** https://www.youtube.com/watch?v=TxottTsaOnE

> [!summary] Quick Reference
> **TL;DR:** This video introduces "Policy as Data" as an architectural shift to effectively govern dynamic agentic AI systems, overcoming the limitations of "Policy as Code."
>
> **Key Takeaways:**
> - Agentic AI systems face a governance gap; static build-time policies cannot control dynamic, real-time decisions.
> - "Policy as Code" fails for live agents because it exits after deployment, leaving continuous actions ungoverned.
> - "Policy as Data" decouples rules from code into dynamic bundles, which agents bind at runtime for actions.
> - This approach allows instant policy updates without redeployment and ensures verifiable auditability for all decisions.
> - Architects must shift to designing active, dynamic runtime governance infrastructure for autonomous systems.
>
> **Concepts:** ai governance · autonomous systems · policy as data · runtime enforcement · enterprise architecture · software compliance · agentic ai

---

## 1. The Critical Governance Gap in Autonomous Systems
For decades, software deployment involved predictable, static structures. However, modern "agentic systems" comprise hundreds of autonomous, fast-moving nodes that make continuous decisions at speeds human operators cannot track. This creates a significant governance gap because traditional policy enforcement is static, designed at build time and left behind after deployment. As a result, 99% of agentic systems lack adequate runtime oversight, continually allocating resources and triggering effects without active control.

---

## 2. Why "Policy as Code" Fails for Dynamic Agents
Policy as code was a success, moving compliance into version-controlled repositories and enabling repeatable, testable rules in build pipelines. However, its operational boundaries are strict: it governs infrastructure provisioning, configuration, and the moment a workload is released. The exact millisecond an agent goes live and begins evaluating choices, policy as code exits. It assumes a system remains static after deployment, a contradiction for autonomous agents that process logic, trigger APIs, and spend money continuously between deployments. Applying static tools to dynamic multi-agent networks creates a severe visibility gap, making it impossible to govern real-time decisions.

---

## 3. The Need for Real-time Runtime Governance and Auditability
Standard telemetry fails regulatory scrutiny for autonomous systems. If a regulator asks why an agent made a specific anomalous trade, engineers relying on logs can see *when* it happened but cannot definitively cite the *exact rule*, its version, the evidence evaluated, or the approving authority. This forces a reconstruction of events and inference of compliance from fragmented logs, rather than producing a definitive citation. The problem is compounded when policies need to change quickly; reliance on slow code changes and redeployments creates unacceptable windows of risk, as active agents continue using outdated rules while a new policy waits in a deployment pipeline.

---

## 4. Introducing "Policy as Data" as the Architectural Solution
Solving this requires an architectural shift away from the static deployment model to "policy as data." Under this paradigm, rules are completely decoupled from application code and transformed into independent, version-controlled, machine-readable "policy bundles." In this new runtime execution, an agent queries and binds to a specific policy bundle (e.g., version 2.1) in real-time before executing an action. It then generates a "passport object," permanently fusing the action data with the exact policy citation, which comprehensively details permits, denials, obligations, and required evidence.

---

## 5. Operational Benefits and Guaranteed Auditability
Policy as data offers critical advantages: it eliminates deployment lag, as promoting a new bundle version allows every agent in scope to instantly bind to the new logic without any redeployment. Historically, it guarantees auditability because past decisions are cryptographically bound to the specific bundle version that governed them, ensuring a coherent audit trail across time. This approach closes the runtime governance gap by ensuring the governing rule physically travels with the decision at agent speed, providing immediate and verifiable context for every action.

---

## 6. The Evolving Role of the Enterprise Architect
Transitioning to policy as data redefines the enterprise architect's role from designing static boundaries to creating active runtime infrastructure. Instead of producing static documents for periodic reviews (indirect influence), the new mandate is to design dynamic governance infrastructure that operates actively within the running system. This requires defining the exact anatomy of policy bundles (standardizing permissions, obligations, evidence), specifying strict authority models for agents and policy types, governing the promotion lifecycle of policies, and designing runtime dials that allow compliance teams to adjust live thresholds without touching underlying code.

---

## Conclusion
Many organizations are operating autonomous systems without effective runtime governance. If, for any active decision happening now, you cannot instantly name the governing rule, its version, the evidence evaluated, or the approving authority without initiating a log search or contacting a developer, then your runtime governance is non-existent. Implementing policy as data is crucial for bridging this critical governance gap in the era of agentic systems.