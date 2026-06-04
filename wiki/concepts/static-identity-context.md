---
concept: Static Identity Context
category: Harness & Context Engineering
summary: Persistent identity, brand, and voice files (e.g. user.md, personality.md) supplied as always-loaded static context — distinct from operational project knowledge — so the AI consistently knows who you are and how you communicate.
aliases: [static identity context, identity files, brand context files, user.md, personality.md, persona files, voice and brand context, identity layer]
related: ["[[claude-md]]", "[[assistant-personalization-layers]]", "[[second-brain]]", "[[persistent-agent-memory]]", "[[context-engineering]]", "[[context-rot]]", "[[agentic-operating-system]]", "[[collaborative-prompt-elicitation]]"]
sources: [creating-your-own-agentic-os-is-easy-insanely-powerful]
---

# Static Identity Context

Static identity context is the layer of persistent files — identity, brand, and voice — that tells an AI assistant *who the operator is and how they communicate*, supplied as always-loaded context so the model does not start every session from scratch. By default an AI tool has no memory of the user's role, style, business, or audience, forcing them to re-explain it each time; identity files (the corpus cites `user.md` and `personality.md` plus brand-context documents) capture that once. The defining distinction is *what* this context is about: where a project file like `[[claude-md]]` carries the *operational* knowledge of a codebase (how to build, test, and what not to touch), static identity context carries the *personal and brand* knowledge of the operator — communication style, preferences, business details, ideal customer profile, and market positioning — so the model's output is shaped to the person, not just the task.

## Key Mechanics

- **Identity and brand files as static context**: a small set of persistent documents records communication style, personal preferences, business specifics, ideal-customer profile, and market positioning — the "about me / about my brand" layer, distinct from the "about this project" layer of `[[claude-md]]`.
- **Injected or referenced**: the files are either injected into the system prompt directly or pulled in by skills when they run, so every piece of work is grounded in the same identity rather than reconstructing it per prompt — the curated-standing-context discipline of `[[context-engineering]]`.
- **Shared grounding for skills**: skills are written to *always reference* this shared identity/brand context, so recurring outputs (drafts, posts, proposals) stay consistent with the operator's voice and positioning across every run.
- **AI-assisted authoring**: rather than writing the files by hand, the recommended shortcut is to have the model *interview the operator* to draft them — a focused use of `[[collaborative-prompt-elicitation]]` to externalize identity into a reusable file.
- **A foundational floor on quality**: establishing this layer alone, before any memory or skill machinery, already raises output quality — it is the cheapest first step toward a consistent assistant and the static-context base of an `[[agentic-operating-system]]`.

## How It Appears in the Corpus

The Simon Scrapes "Creating Your Own Agentic OS" tutorial names static identity context as the first layer of the OS: identity files (`user.md`, `personality.md`) and brand context that inform the AI about communication style, preferences, business details, ideal customer profile, and market positioning, injected into the system prompt or referenced by skills. It recommends letting the AI interview you to create the files quickly and notes that this foundational layer alone significantly improves output quality.

## Tensions & Tradeoffs

- **Distinct from `[[claude-md]]`, same always-loaded tier**: both are static context read every session, but identity context is about the *person and brand* while a project file is about the *codebase's operations* — keeping them separate prevents personal voice and build instructions from diluting each other, the same separation-of-axes discipline as `[[assistant-personalization-layers]]`.
- **Distinct from `[[persistent-agent-memory]]`**: identity context is *static* (a deliberate, stable description of who you are), whereas agent memory is *evolving* (facts and decisions accumulated across sessions) — the profile layer is hand-authored and durable, the memory layer is grown and pruned.
- **It is the voice half of a `[[second-brain]]`**: injecting one's style and tone so AI output sounds like the operator is the same voice-injection move a second brain makes, here isolated as a standing context layer rather than a whole knowledge store.
- **Bounded by the same context budget**: an over-stuffed identity file consumes window space and dilutes signal like any standing material — the `[[context-rot]]` risk — so it must stay a concise description, not an exhaustive autobiography.
- **Staleness as identity and brand evolve**: a person's role, positioning, and voice change, and a stale identity file silently shapes output to an outdated self — the same maintenance burden that bounds every standing-context artifact.
