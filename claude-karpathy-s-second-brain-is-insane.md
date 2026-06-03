---
tags:
  - video-summary
  - en
  - second brain
  - knowledge management
  - obsidian
  - claude code
  - LLM
  - AI productivity
  - personal wiki
video_id: "5FiHjotg2zU"
channel: "Corey Ganim"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.2
---

# Claude + Karpathy's Second Brain is INSANE

**Channel:** Corey Ganim | **Duration:** 22:21 | **URL:** https://www.youtube.com/watch?v=5FiHjotg2zU

> [!summary] Quick Reference
> **TL;DR:** This video details building a personalized "second brain" with Claude Code and Obsidian to organize all your data, enhancing personal and business effectiveness.
>
> **Key Takeaways:**
> - Build a personalized "second brain" using Claude Code and Obsidian to manage and leverage all your information.
> - Configure Obsidian with a web clipper and the open-source Claude Skill to easily capture and process data.
> - Establish separate, specialized second brains (e.g., personal, business) for better focus and efficiency.
> - Follow a workflow: ingest raw data, let AI organize it into a queryable wiki, then generate targeted outputs.
> - Regularly "lint" your second brain to identify conflicts and improve connections, ensuring accuracy and value.
>
> **Concepts:** second brain · knowledge management · obsidian · claude code · LLM · AI productivity · personal wiki

---

## 1. Understanding the "Second Brain" Concept
Andrej Karpathy's viral tweet ignited the idea of building a personalized "second brain" using Claude Code and Obsidian. This system is designed to organize all your data, enhancing personal and business effectiveness by streamlining information for tasks, content creation, and strategic planning. Karpathy's original "idea file" provided a loose architectural framework for an LLM-powered wiki, outlining core benefits, operational processes, indexing methods, and optional command-line enhancements.

---

## 2. Key Tools for Implementation
The video demonstrates a practical implementation leveraging several powerful tools:
*   **Obsidian:** A versatile note-taking application that creates a dynamic mind graph, visualizing the interconnections between disparate pieces of information.
*   **Obsidian Web Clipper (Chrome Extension):** A browser extension that effortlessly scrapes web page content, including text and images, directly into your Obsidian vault's designated "raw" directory.
*   **Summarize (Optional Open-Source Library):** Developed by Peter (Open Claw creator), this tool extracts YouTube video transcripts and formats them into LLM-friendly markdown, further enriching your knowledge base.
*   **The "Claude Skill" (Vercel Framework):** An end-to-end, open-source skill compatible with various AI agent harnesses (Claude Code, Codex, Gemini CLI). It simplifies vault setup, content ingestion, intelligent querying, and "linting" (health checks) for your second brain.

---

## 3. Step-by-Step Second Brain Setup
The video walks through the process of setting up your second brain using the custom Claude Skill:
*   **Skill Installation:** After installation, execute the `second brain` command within Claude Code.
*   **Vault Configuration:** The guided wizard prompts you to name your vault (e.g., "YouTube demo"), specify its local storage location, define a primary topic (e.g., "AI research"), and configure any additional AI agents (e.g., Codex) you wish to use.
*   **Optional Tools Integration:** You can integrate supplementary tools like Summarize, QMD (for large knowledge base searching), and Agent Browser (for web research).
*   **Vault Specialization:** It's recommended to create specialized second brains (e.g., one for personal use, another for business) rather than a single, all-encompassing vault, to maintain focus and efficiency.

---

## 4. The Second Brain Workflow: Raw, Wiki, Outputs
The system operates on a three-tiered data structure:
*   **Obsidian Web Clipper Setup:** Crucially, configure the Web Clipper to save all new content directly into the "raw" folder of your Obsidian vault, aligning with Karpathy's architecture for brain-dumping initial information.
*   **Raw Directory:** This acts as your initial repository for all incoming unstructured data, be it web clippings, personal notes, or YouTube transcripts.
*   **Ingestion Process:** Run the `second brain ingest` command. The AI then processes the content from the "raw" folder, summarizes key takeaways, and organizes it into the "wiki." Obsidian's graph view dynamically illustrates the new interconnections and relationships. This ingestion can be automated using Claude Code's "loop" feature for continuous updates.
*   **Querying the Wiki:** Once ingested, the wiki becomes a powerful, queryable knowledge base. You can ask specific questions (e.g., "Where did Karpathy go to school?"), and the system will provide context-aware answers derived directly from your collected data.
*   **Outputs:** This final tier consists of generated reports or decision files, which are the results of your queries and analyses drawn from the wiki.

---

## 5. Maintaining and Growing Your Knowledge Base
Maintaining the relevance and accuracy of your second brain is key to its long-term value:
*   **The "Lint" Command:** Utilize `second brain lint` to perform a comprehensive health check on your wiki. This command identifies potential conflicts, flags outdated information, and highlights areas where more connections could be established. It provides warnings and actionable suggestions for improvement.
*   **Iterative Refinement:** By addressing the linting suggestions—such as adding new Wikipedia entries for missing topics or refining existing ones—you continuously strengthen your knowledge graph and close information gaps.
*   **Compounding Value:** The true power of a second brain lies in its compounding value. As more data is added, organized, and interconnected over time, it evolves into an increasingly invaluable, unique, and powerful personal or company asset, providing a significant competitive "moat" in the AI landscape.

---

## Conclusion
Building a personalized "second brain" with tools like Claude Code and Obsidian represents a transformative leap in information management. It enables the conversion of raw, disparate data into a structured, intelligent, and highly queryable knowledge base, offering an unparalleled competitive advantage for individuals and businesses alike in the fast-evolving AI environment. The provision of a free, open-source skill to set this up democratizes access to this advanced capability, promising a surge in adoption and the emergence of new service models around this critical AI infrastructure.