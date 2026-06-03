---
tags:
  - video-summary
  - en
  - agent skills
  - Superbase
  - LLM agents
  - evaluations
  - progressive disclosure
  - Postgres security
  - AI tooling
video_id: "GmAQKINjv1E"
channel: "AI Engineer"
lang: EN
type: Tutorial
audience: Intermediate
score: 4
---

# Skill Issue: How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase

**Channel:** AI Engineer | **Duration:** 1:18:41 | **URL:** https://www.youtube.com/watch?v=GmAQKINjv1E

> [!summary] Quick Reference
> **TL;DR:** This video explores using structured "agent skills" with progressive disclosure to enhance LLM agent performance and prevent issues, validated by robust evaluation pipelines.
>
> **Key Takeaways:**
> - Agent skills use markdown files with progressive disclosure, loading only necessary context to guide LLM behavior efficiently.
> - Combine MCP tools for server-side integrations with skills for rich context and workflow orchestration in agent environments.
> - Implement "evaluations" (evals) for non-deterministic testing of agent skills, assessing reasoning and tool usage.
> - Skills can prevent security misconfigurations, like ensuring `SECURITY INVOKER` for Postgres views to uphold Row Level Security.
> - Automate skill validation using evals with comparison scenarios and state resets to prevent regressions in production.
>
> **Concepts:** agent skills · Superbase · LLM agents · evaluations · progressive disclosure · Postgres security · AI tooling

---

## 1. Introduction to Agent Skills and Superbase AX
The workshop, led by Pedro, an AI tooling engineer at Superbase, focuses on enhancing agent performance through the strategic use of "skills." Pedro's day-to-day involves improving Agent Experience (AX) at Superbase, a concept akin to Developer Experience (DX) but for AI agents. This session will dive into how to write, manually test, and automate the testing of these crucial agent skills using evaluations.

---

## 2. Understanding Agent Skills: Structure and Progressive Disclosure
Agent skills are defined as organized folders containing instructions and files that enable agents to execute workflows, access custom information, or utilize specific scripts as tools. The core component is the `skill.md` markdown file, which acts as an "index on steroids." It begins with a frontmatter (including `name` and `description`) designed for "progressive disclosure." This means only the frontmatter is initially loaded into the agent's context, allowing the agent to decide whether to load the full skill content based on its immediate needs. Skills can reference other markdown files or scripts (e.g., Bash, Python) for extended functionality.

---

## 3. Skills vs. MCP Tools: A Collaborative Approach
A key discussion point is the distinction and synergy between agent skills and Multi-Modal Command Protocol (MCP) tools. MCP tools typically run server-side, do not require a local environment, and are ideal for integrations where agents might lack direct shell access. In contrast, skill scripts execute within the agent's local environment, bound by its operating system. While MCP tools handle integrations, skills excel at providing rich context and defining intricate workflows that exceed the scope of simple tool descriptions. The recommendation is to leverage both: MCP for robust integrations and skills for contextual guidance and workflow orchestration.

---

## 4. Testing Agent Skills with Evaluations (Evals)
Evaluating agent skills, particularly those defined in markdown, requires a non-deterministic testing methodology known as "evaluations" (evals). Evals assess an agent's output and behavior, considering its reasoning and tool usage. The recommended framework from Agent Skills Open Standard involves: 1) Defining clear metrics for success, 2) Crafting the skill itself, 3) Executing evaluations (both manual and automated), 4) Grading the agent's performance, and 5) Iterating based on feedback. Tools like Braintrust and LangFuse can assist in systematic eval execution and observability.

---

## 5. Practical Demonstration: Fixing Database Security with Skills
Pedro demonstrated skill application using a Superbase-backed "performance review" app. Initially, without a specific security skill, the agent created a database view that inadvertently bypassed PostgreSQL's Row Level Security (RLS). This allowed unauthorized access to sensitive departmental data, a common issue as views, by default, inherit creator permissions, not RLS policies. To rectify this, the `SECURITY INVOKER` flag must be explicitly included in the view definition. A pre-built "Superbase Security" skill, providing context on this specific PostgreSQL vulnerability, was then introduced. When the agent used this skill, it correctly applied the `SECURITY INVOKER` flag during view creation, demonstrating how skills can effectively guide agents to prevent security misconfigurations.

---

## 6. Automating Skill Validation and Overcoming Evals Challenges
Automating skill testing, particularly for production environments, is vital. Evals provide a robust pipeline to ensure that skill modifications do not introduce regressions or unexpected behaviors. However, implementing evals presents challenges: designing representative scenarios, managing non-deterministic LLM outputs, and ensuring accurate assertion logic. A practical setup involves comparing agent behavior with and without the skill, resetting the database state between runs, and using a headless agent harness. The demonstration highlighted how flawed evaluation logic could misrepresent a skill's positive impact, underscoring the importance of meticulously crafted eval scenarios and assertions.

---

## Conclusion
Agent skills, powered by progressive disclosure, offer a flexible and powerful way to enhance LLM agent capabilities and guide their behavior. While the field is still nascent, establishing robust evaluation pipelines for automated testing is crucial for deploying reliable skills in production. Managing skills in production requires treating them as living documentation, ensuring they are kept clean, updated, and continuously validated against desired agent workflows. The ongoing standardization efforts and innovative tools will continue to shape how we develop, deploy, and evaluate intelligent agents.