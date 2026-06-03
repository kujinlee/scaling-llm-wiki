---
tags:
  - video-summary
  - en
  - ai agents
  - product planning
  - g-stack
  - clawcode
  - saas development
  - mvp
  - software architecture
video_id: "6kM27uGP4n4"
channel: "Eric Tech"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.8
---

# This GStack Skill Saves Weeks of Development

**Channel:** Eric Tech | **Duration:** 30:59 | **URL:** https://www.youtube.com/watch?v=6kM27uGP4n4

> [!summary] Quick Reference
> **TL;DR:** This video showcases G-Stack's AI-driven planning workflow, utilizing multi-persona agents to meticulously refine product specifications and reduce development risks before coding.
>
> **Key Takeaways:**
> - Define the smallest viable feature (MVP) early, challenging assumptions and narrowing priorities.
> - Utilize multi-persona AI agents for comprehensive, independent reviews of product specifications.
> - Prioritize safe, efficient technical approaches for MVPs, like Structured Query Mappers.
> - Conduct thorough pre-coding deliberation with AI tools to refine specs and identify edge cases.
>
> **Concepts:** ai agents · product planning · g-stack · clawcode · saas development · mvp · software architecture

---

## 1. Introducing G-Stack's Planning Workflow
This video demonstrates a specialized product planning workflow using the G-Stack toolkit by Clawcode. The CEO, Gary Tan, emphasizes the importance of this workflow for challenging assumptions, narrowing down priorities, researching competitive landscapes, and leveraging multiple AI agents (CEO, design, engineering, QA, devil's advocate) to review specifications before any code is written. The practical application showcased is building an AI chat agent feature for an existing SaaS project, bookzero.ai, which has paying customers.

---

## 2. The Office Hours Phase: Defining the Product Vision
Starting with a Jira ticket, the G-Stack planning pipeline initiates an "Office Hours" session in Clawcode. The system intelligently gathers context by asking questions about the project's phase, goals, and customer base. A key objective is to define the "smallest possible version" (MVP or "wedge") that can be immediately useful to paying customers, pushing back against overly ambitious initial requests. User research is integrated, revealing that customers often export CSVs to analyze data, suggesting a need for native analytical capabilities. A "future-fit" analysis ensures the feature's long-term relevance and unique selling proposition, particularly by highlighting G-Stack's AI advantage in querying existing, verified data, thus avoiding the hallucination issues common in AI tools that generate financial entries. The phase concludes by challenging core premises and obtaining a cross-model second opinion from an independent AI agent.

---

## 3. Technical Approach & MVP Refinement
Following the vision definition, G-Stack presents and evaluates different technical approaches for implementing the AI chat's query functionality. The options explored include a Structured Query Mapper (where an LLM converts natural language into structured JSON intents mapped to existing queries), Direct SQL Generation (where the LLM generates parameterized SQL directly), and a hybrid approach combining both. The recommended approach is the Structured Query Mapper due to its higher safety, lower development effort, zero risk of SQL injection, and effectiveness in covering 90% of user queries. This decision aligns with principles of shipping an MVP safely and efficiently, focusing on leveraging existing structures.

----- 

## 4. The Spec Team: Detailing Design and Implementation
With the core technical approach decided, the "Spec Team" skill takes over to refine detailed design and implementation aspects. Discussions cover critical decisions such as the AI chat's UI placement (a dedicated page in the dashboard is chosen for richer display), conversation context retention (maintaining five turns), and the data aggregation strategy (opting for an ORM-style backend service for better scalability and database portability over raw SQL RPCs or JavaScript aggregation). User interface considerations for displaying tabular results (inline markdown with collapse/expand functionality) are addressed. Furthermore, the team identifies and plans for various edge cases, including handling empty data states, ambiguous user queries that require clarification, managing mixed currencies, and implementing rate limiting to prevent query spamming.

---

## 5. Automated Review with Multi-Persona Agents
The final stage of the planning pipeline involves the "Auto Plan" skill, which orchestrates a comprehensive, multi-perspective review of the refined specification. This is achieved by launching five parallel AI agents, each embodying a different persona: CEO, Design, Engineering, QA Strategist, and Devil's Advocate. These agents independently scrutinize the spec from their respective angles, identifying a significant number of findings (e.g., 10 from CEO, 15 from design, 16 from engineering). Through an iterative process, these findings lead to numerous decisions and modifications, ensuring the product specification is thoroughly vetted, robust, and aligned with various stakeholders' perspectives before proceeding to development.

---

## Conclusion
The entire G-Stack planning pipeline, encompassing the Office Hours, Spec Team, and Auto Plan phases, demonstrated a comprehensive and structured approach to feature development on a brownfield project. This process consumed approximately 600,000 tokens, highlighting the depth of analysis and multi-agent collaboration involved. By leveraging AI agents for contextual questioning, scope refinement, technical decision-making, and multi-disciplinary review, G-Stack significantly streamlines the product planning stage. The output is a highly refined and verified specification, ready for execution using subsequent tools like G-Stack's build pipeline, GSD, or Superpower. This systematic methodology aims to enhance accuracy, reduce risks, and accelerate the development of complex features by ensuring thorough pre-coding deliberation.