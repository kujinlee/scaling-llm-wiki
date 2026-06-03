---
tags:
  - video-summary
  - en
  - llm development
  - ai engineering
  - domain-driven design
  - ubiquitous language
  - software documentation
  - code context
  - developer tools
video_id: "6BB6exR8Zd8"
channel: "Matt Pocock"
lang: EN
type: Framework
audience: Intermediate
score: 4.8
---

# I stopped using /grill-me for coding. Here’s what I use instead:

**Channel:** Matt Pocock | **Duration:** 15:17 | **URL:** https://www.youtube.com/watch?v=6BB6exR8Zd8

> [!summary] Quick Reference
> **TL;DR:** This video introduces 'Grill with Docs', an AI tool that uses a 'Ubiquitous Language' via `context.md` to formalize shared understanding for clearer code.
>
> **Key Takeaways:**
> - Adopt 'Ubiquitous Language' and `context.md` to formalize shared project terminology.
> - Use Architectural Decision Records (ADRs) to document significant, hard-to-reverse design choices.
> - Leverage tools like 'Grill with Docs' to dynamically update documentation during AI-assisted development.
> - Formalizing language upfront drastically reduces AI verbosity and clarifies codebase structure.
>
> **Concepts:** llm development · ai engineering · domain-driven design · ubiquitous language · software documentation · code context · developer tools

---

## 1. From Grill Me to Grill with Docs: Identifying the Need

The video begins by celebrating "Grill Me," an AI skill designed to interview users relentlessly to achieve shared understanding, which garnered significant praise for its effectiveness in project development and even personal use cases like writing a eulogy.

However, the creator identified limitations: Grill Me often led to verbose AI responses and required constant re-explanation of domain-specific jargon (e.g., "standalone videos") and non-obvious codebase concepts. There was no persistent documentation of the refined language or decisions made during grilling sessions, leading to inefficiencies.

---

## 2. The Ubiquitous Language and Documentation Strategy

To address Grill Me's shortcomings, the creator adopted the "Ubiquitous Language" concept from Domain-Driven Design, which advocates for a shared language across domain experts, developers, and the codebase.

This led to the development of the "Ubiquitous Language skill" for creating a `context.md` file – a living glossary of shared terminology.

Additionally, Architectural Decision Records (ADRs) were introduced as simple markdown files to document non-obvious, hard-to-reverse architectural decisions that couldn't be captured in `context.md`.

---

## 3. Introducing Grill with Docs: Features and Workflow

"Grill with Docs" is the new skill that integrates the grilling process with context-aware documentation. It combines the core functionality of Grill Me with the ability to leverage and update `context.md` and ADRs.

During a session, Grill with Docs is instructed to:
*   Look for an existing `context.md` file to bootstrap shared language.
*   Challenge language usage against the glossary.
*   Sharpen fuzzy language, discuss concrete scenarios, cross-reference with code.
*   Update the `context.md` file dynamically as new terms and definitions are agreed upon.

A live demo showcases how the skill prioritizes language alignment (e.g., defining "pitch" and "standalone video" relationships, resolving terminology collisions) before delving into implementation details, ultimately saving agreed-upon definitions to `context.md`.

---

## 4. Key Benefits and Use Cases

The primary benefits of using Grill with Docs include significantly more concise AI replies and internal thinking, as the shared language reduces the need for verbose explanations.

This approach also leads to easier-to-navigate code, as variable names, file names, and overall structure align with the documented ubiquitous language.

The video clarifies that Grill Me is not dead; it remains excellent for general use cases without a codebase (e.g., personal writing, early project ideation where no code exists). Grill with Docs is recommended specifically when working with an existing or nascent codebase to establish and maintain a shared, consistent language.

---

## Conclusion

Grill with Docs represents a significant evolution in AI-assisted development by formalizing shared understanding through documentation. By integrating Domain-Driven Design principles like Ubiquitous Language and ADRs, it enables developers to achieve magical alignment with AI, leading to more efficient communication, cleaner code, and a more robust development process. This approach highlights how established human-centric development techniques translate effectively to AI collaboration.