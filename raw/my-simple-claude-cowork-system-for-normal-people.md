---
tags:
  - video-summary
  - en
  - ai assistant
  - claude
  - personal workflow
  - context management
  - markdown system
  - ai customization
  - productivity tools
video_id: "0_dSWLOHKng"
channel: "Jeff Su"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# My Simple Claude Cowork System (for normal people)

**Channel:** Jeff Su | **Duration:** 21:18 | **URL:** https://www.youtube.com/watch?v=0_dSWLOHKng

> [!summary] Quick Reference
> **TL;DR:** This video introduces a 'Co-worker OS' system using structured markdown files to give AI assistants persistent, personalized context, automating tasks and improving interactions.
>
> **Key Takeaways:**
> - Establish persistent AI context using `claude.md` for instructions, `memory.md` for ongoing projects, and resource files.
> - Create specialized 'workstations' (subfolders) with dedicated `claude.md` and `memory.md` files for specific tasks.
> - Implement a 'session audit' skill to continually teach the AI your preferences and improve its understanding over time.
> - Optimize token costs by keeping root `claude.md` lean, avoiding rule repetition, and using cheaper AI models.
>
> **Concepts:** ai assistant · claude · personal workflow · context management · markdown system · ai customization · productivity tools

---

## 1. Understanding the Co-worker AI System Architecture
--- 
The video introduces a powerful AI system, 'Co-worker OS' (a play on 'iCloud OS' and Claude), designed to personalize AI interactions. The core idea revolves around using simple markdown files (`claude.md`, `memory.md`, and resource files) to provide persistent context to an AI assistant like Claude. `claude.md` acts as a master instruction manual, `memory.md` stores ongoing information and active projects, and resource files hold detailed knowledge. This hierarchical system ensures the AI always has relevant context, from general rules to specific project details, without repeated prompting.

## 2. Building the Root Level (Level Zero)
--- 
The first step in setting up Co-worker OS is creating a root folder (e.g., 'Co-work OS') and populating it with three essential starter files: `claude.md`, `memory.md`, and `voice_principles.md`. The `claude.md` file contains foundational rules like instructing Co-worker to read `memory.md` at the start of every session and how to save new information. The `memory.md` file is used for active projects and remembering specific user inputs. A `00_resources` folder is created for the `voice_principles.md` file, which Co-worker uses to learn and apply the user's unique tone of voice by analyzing past emails or writing samples.

## 3. Workstations: Universal and Dedicated
--- 
The system extends to 'workstations,' which are subfolders for specific areas of life or tasks, each with its own `claude.md`, `memory.md`, and resources folder. 

*   **Universal Workstations** (e.g., Email HQ): These handle tasks common across various life areas. The `email_hq/claude.md` file would contain email-specific rules (greetings, sign-offs, inbox workflow) that layer on top of the root `voice_principles.md`.
*   **Dedicated Workstations** (e.g., Personal Finances): These focus on single, specialized areas. For personal finances, Co-worker can analyze credit card statements, categorize spending, and create master spending trackers. The video demonstrates how a prompt can automate the creation of such a workstation and its initial setup.

## 4. Practical Use Cases and Advanced Features
--- 
The video illustrates several practical applications of the Co-worker OS, showcasing its ability to automate complex tasks by leveraging stored context:

*   **Saving Information**: Automatically categorizing and saving new information (e.g., a copywriting framework screenshot) into the correct resource file based on the root `claude.md` routing map.
*   **Email Automation**: Drafting follow-up emails after meetings, pulling calendar data, reading transcripts, and applying both general voice principles and email-specific rules from the Email HQ workstation.
*   **Project Management**: Creating and populating Notion project pages with specific properties and sections based on predefined user conventions.

## 5. Pro Tips for Efficiency and Cost Management
--- 
Two key pro tips are shared to optimize the Co-worker OS:

*   **Session Audit Skill**: Installing a 'session audit' skill (`/session audit`) prompts Co-worker to scan the conversation for unsaved principles and preferences to remember for future sessions, continuously improving its understanding.
*   **Token Usage Optimization**: 
    *   Keep the root `claude.md` file lean (under 300 lines) as it's loaded in every session.
    *   Avoid rule repetition; specific rules should only exist in the most relevant `claude.md` file.
    *   Default to the cheaper Claude Sonnet model for 80% of tasks, only switching to Opus for complex, multi-step operations.

## Conclusion
--- 
The Co-worker AI system, built on persistent context through structured markdown files, offers a significant leap in personalized AI assistance. By establishing a hierarchical structure of rules, memory, and resources, users can train an AI to understand their unique preferences, workflows, and projects. This approach ensures that the AI consistently provides relevant and high-quality outputs, compounding its effectiveness over time. The video strongly advocates for building such a personal context system now, regardless of the specific AI model or tools used, to stay ahead in an evolving AI landscape.