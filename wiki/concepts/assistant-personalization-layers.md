---
concept: Assistant Personalization Layers
category: Harness & Context Engineering
summary: Separating the distinct axes of customizing an AI assistant — domain context (projects), repeatable working method (skills), and user profile (memory) — so each is configured deliberately rather than collapsed into one prompt.
aliases: [personalization layers, projects vs skills vs memory, context vs method vs profile, customization axes, assistant specialization layers, work-OS layers]
related: [claude-md, context-engineering, persistent-agent-memory, thin-harness-fat-skills, lazy-context-loading, agentic-capability-ladder, cross-tool-memory, model-context-protocol]
sources: [26년-5월-업데이트-클로드-핵심-기능-300-활용법ㅣ코워크-skills-커넥터-어플]
---

# Assistant Personalization Layers

Assistant personalization layers is the principle that customizing an AI assistant is not one undifferentiated act of "configuring the prompt" but a separation into distinct, orthogonal axes — each answering a different question and best managed on its own surface. The corpus's clean three-way split is *domain context* (a project workspace that makes the assistant a topic expert), *working method* (a skill that standardizes how a recurring task is performed), and *user profile* (memory that makes the assistant a secretary who knows you). Keeping these distinct prevents the common error of stuffing domain facts, procedures, and personal preferences into a single instruction blob where they dilute one another.

## Key Mechanics

- **Context layer — Projects**: a dedicated workspace with custom instructions, uploaded reference documents, and a conversation-derived memory that raises the assistant's understanding of one topic, turning it into a "subject-matter expert" for that domain (e.g. a project per YouTube channel or per lecture series). This is the curated-standing-context discipline of `[[context-engineering]]` and `[[claude-md]]` applied at the consumer-workspace granularity.
- **Method layer — Skills**: a reusable capability that specifies *how* a repeated task is done (e.g. drafting a new-project proposal), so the quality of recurring work stays consistent across runs. Where the project manages *what the assistant knows*, the skill manages *the way it works* — the prose-runbook idea of `[[thin-harness-fat-skills]]`.
- **Profile layer — Memory**: automatic retention of the user's name, work style, and preferred answer format, carrying conversational context across sessions so the assistant adapts to the person rather than the topic — the personal-fact tier of `[[persistent-agent-memory]]`.
- **They compose, not substitute**: the layers are designed to stack — a project (context) plus a skill (method) plus memory (profile) together make the assistant behave like a real teammate. The video extends the stack outward to an *integration* layer (Connectors to external tools, see `[[model-context-protocol]]`) and an *execution* layer (Co-work driving local files), framing the whole as an integrated "work operating system" rather than a chat box.

## How It Appears in the Corpus

The 이동훈의 루트AI ("Claude core-features 300% guide") tutorial draws the separation explicitly: "if a Project manages *context*, a Skill manages *the way of working*," and "a Project creates a subject-matter expert while Memory creates a secretary who knows me." It presents Projects, Memory, and Skills as three complementary collaboration tools that, combined, let the user treat Claude like a genuine team member, and its conclusion frames Claude as an integrated work OS — Projects set context, Skills standardize method, Connectors link external tools, and Co-work executes.

## Tensions & Tradeoffs

- **Boundary blur in practice**: domain context and working method can leak into each other — a project's custom instructions often encode procedure, and a skill often carries context — so the clean three-axis taxonomy is a design ideal that requires discipline to maintain, the same exhaustiveness-vs-concision tension that bounds `[[claude-md]]`.
- **Each layer carries its own failure mode**: an over-stuffed project context invites `[[context-rot]]`-style dilution, a stale skill propagates an outdated procedure, and a wrong memory silently personalizes against the user — so separating the axes localizes problems but does not eliminate them, and `[[lazy-context-loading]]` is the loading-side discipline for keeping each layer lean.
- **Profile portability**: the user-profile layer is tied to one assistant unless externalized — the lock-in concern `[[cross-tool-memory]]` addresses by moving memory into a user-owned store shared across tools.
- **A pedagogical framing, not a strict architecture**: like the `[[agentic-capability-ladder]]`, the layered "work OS" model is a teaching structure for adopting features deliberately; the layers blur and an operator can lean on one (e.g. memory) without configuring the others.
