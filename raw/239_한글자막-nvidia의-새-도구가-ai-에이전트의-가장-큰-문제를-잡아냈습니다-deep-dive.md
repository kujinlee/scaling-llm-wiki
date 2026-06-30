---
tags:
  - video-summary
  - deep-dive
  - en
  - ai agents
  - skill specter
  - ai security
  - vulnerability detection
  - claude code
  - secure workflow
  - llm security
video_id: "VBnG5Fse2ms"
channel: "Tech Bridge"
lang: EN
type: Tutorial
audience: Intermediate
score: 4.6
---

# [한글자막] Nvidia의 새 도구가 AI 에이전트의 가장 큰 문제를 잡아냈습니다 (Deep Dive)

**Channel:** Tech Bridge | **Duration:** 9:17 | **URL:** https://www.youtube.com/watch?v=VBnG5Fse2ms

---

## The Problem of Insecure AI Agent Skills
▶ [0:00–0:11](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=0s)
The video begins by highlighting the widespread and often unchecked use of "skills" for AI agents. While these skills are run by every agent, users tend to trust them without performing any security checks. This trust is misplaced, as a study of over 30,000 such skills revealed that more than a quarter contained security vulnerabilities. This presents a significant risk to users and their systems.

## NVIDIA's SkillSpector Tool
▶ [0:11–0:38](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=11s)
To address the security risks posed by AI agent skills, NVIDIA has developed an open-source tool called SkillSpector. Its primary function is to scan any skill *before* installation to assess its potential danger. The tool analyzes the skill's code and provides a detailed report on its safety.

However, the video points out a critical limitation: a specific type of attack can bypass the tool's default settings. The setting that can detect this attack is disabled by default, and enabling it typically costs money because it requires API calls to a powerful AI model. The video promises to show a workaround for this cost, and to demonstrate how SkillSpector can be integrated into a complete workflow that fundamentally changes how users find and install skills securely.

## Installation and Basic Usage
▶ [0:38–1:22](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=38s)
The SkillSpector tool is available on GitHub at `NVIDIA/SkillSpector`. The video demonstrates the installation process, which involves cloning the repository and running a series of shell commands. These commands can be given directly to an AI coding assistant like Claude Code, which will then handle the entire setup, including installing all necessary Python dependencies.

### Testing with Malicious Skills
To verify that SkillSpector is working correctly, the repository includes a `tests` folder containing a collection of intentionally dangerous skills. Users can run the scanner on these test skills to see how it identifies and reports threats.

The video shows an example of running the scan from the command line:
`skill_spector scan tests/fixtures/mcp_poisoned_tool/ --no-llm`

The scanner outputs a detailed security report, which includes:
*   **Risk Assessment:** A numerical `Score` (e.g., 100/100), a `Severity` level (e.g., CRITICAL), and a clear `Recommendation` (e.g., DO NOT INSTALL). The higher the score, the more dangerous the skill.
*   **Conflict Location:** The report pinpoints the exact file and line number (e.g., `Location: SKILL.md:10`) where a security issue was found, explaining what caused the high-risk score.

## AI Skill Attack Vectors
▶ [1:22–1:38](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=82s)
The video categorizes the 14 known types of skill attacks into six main groups for simplicity. Understanding these attack vectors is crucial for appreciating how SkillSpector detects them.

### 1. Hidden Instructions
▶ [1:38–2:05](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=98s)
A skill is essentially a text file of instructions that an AI agent follows. Attackers can embed malicious commands that are invisible to the human user but are read and executed by the agent. These hidden instructions can be concealed in several ways:
*   Tucked inside code comments.
*   Using invisible characters.
*   Scrambling text into code that appears as nonsense to humans but is parsable by the AI.

SkillSpector is specifically designed to hunt for and identify these types of hidden instructions.

### 2. Impersonation
▶ [2:05–2:44](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=125s)
AI agents trust and call upon tools by name. An attacker can exploit this by creating a malicious tool that has the same name as a trusted, legitimate tool (e.g., a file-reading tool named `read`). The agent, intending to use the safe tool, might inadvertently execute the malicious one instead.

This is often achieved using a sneaky technique involving look-alike characters from different alphabets. For example, the tool might be named `read`, but the "a" is a Cyrillic character (U+0430) that looks identical to the Latin "a" (U+0061). To a human and the agent at a glance, the word is the same, but it refers to a completely different, malicious tool. SkillSpector counters this by checking the underlying Unicode identity of every character, allowing it to spot and flag these fakes.

```ascii
      [Trusted Agent]
            ↓
  [Requests tool "read"]
            |
            +----------------------------------+
            |                                  |
            ↓ (Correct)                        ↓ (Hijacked)
  [Safe "read" tool]           [Malicious "read" tool with Cyrillic 'a']
 (Reads a file)                (Executes harmful code)
```

### 3. Deception
▶ [2:44–3:05](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=164s)
This attack involves a mismatch between what a skill *claims* to do and what its code *actually* does.
*   **Example 1:** A skill might describe itself as a simple "formatter" but its code quietly accesses the internet in the background.
*   **Example 2:** A skill might request only "read files" permission, but its underlying code is also capable of writing files and running commands.

This type of attack is harder to catch with simple pattern matching, which is why the tool's more advanced "AI scan" mode is necessary.

### 4. Credential Theft
▶ [3:05–3:15](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=185s)
A malicious skill can be designed to steal sensitive user credentials, such as API keys and passwords. The skill's code can search for saved keys on the user's machine, collect them, and exfiltrate them to a remote server controlled by the attacker.

### 5. Malware Execution
▶ [3:15–3:32](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=195s)
This is a direct attack where the skill's primary purpose is to run malware on the user's system. An example given is a "reverse shell," which grants a remote attacker full control over the user's computer. SkillSpector detects this by matching the skill's code against a large database of known malware fingerprints.

### 6. Poisoned Dependencies
▶ [3:32–4:02](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=212s)
Skills often rely on external command-line interface (CLI) tools or software packages to function. An attacker can create a malicious package with a name that is a common typo of a popular, legitimate package (a "typosquatting" attack). When the skill calls this dependency, it pulls in the wrong package, which then executes malware. SkillSpector protects against this by checking every package a skill references against a live database of known malicious packages and flagging fake names or dangerous "download and run" commands.

## The AI Scan Mode (Mode 2)
▶ [4:02–4:19](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=242s)
SkillSpector's default mode relies on static analysis and pattern matching. While effective, it can sometimes produce "false positives," flagging harmless code as malicious because it lacks context.

To solve this, the tool has a second, more powerful mode called the **AI scan**. This mode uses a Large Language Model (LLM) to analyze the skill with a deeper understanding of context and intent, making it particularly effective at catching "Deception" attacks where the skill's description and code do not match.

By default, this mode is disabled. To run a scan *with* the AI check, you simply run the command *without* the `--no-llm` flag.

### Bypassing the OpenAI API Cost
▶ [4:19–5:18](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=259s)
The documentation reveals that running the AI scan requires an OpenAI API key, which incurs a cost. The video presents a workaround: modifying the tool's code to use **Claude Code's headless mode** instead. This allows the AI check to be performed using the monthly credits included with Anthropic plans, effectively making it free for many users. The video shows that this modification can be requested from Claude Code itself with a single prompt, such as: `use claude -p for the AI check instead of the OpenAI key`.

## Building a Full Workflow: The "Discover Skills" Skill
▶ [5:18–7:07](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=318s)
The video goes beyond simply using the scanner as a standalone tool and integrates it into a complete, automated workflow by creating a new skill called `discover-skills`. This master skill orchestrates the entire process of finding, vetting, and installing new skills securely.

The workflow is as follows:
1.  **Discover:** The skill searches for new skills on `skills.sh`, a Git-based repository and shared library for AI agent skills.
2.  **Scan & Report:** Before installation, it automatically runs the downloaded skill through the SkillSpector scanner (including the AI scan).
3.  **Triage:** The agent reviews the scan's findings to determine if there is malicious intent or just a minor vulnerability.
4.  **Fix (Optional):** If the issue is a fixable vulnerability (not malicious), the agent can attempt to repair the code.
5.  **Re-scan:** After fixing, it runs the scan again to confirm the skill is clean.
6.  **Install:** Only once the skill is confirmed safe does the agent proceed with the installation.

```ascii
 [Agent needs a new function]
            ↓
[Runs the "discover-skills" skill]
            ↓
  [Searches for skills on skills.sh]
            ↓
  [Clones a candidate skill locally]
            ↓
    [Runs SkillSpector scan on the local copy]
            ↓
  [Agent reviews the scan report]
            |
            +----------------------+
            |                      |
            ↓ (Problem Found)      ↓ (Clean)
      [Fixes the code]      [Installs the skill]
            ↓
       [Re-scans]
            ↓ (Clean)
   [Installs the skill]
```

### Workflow in Action
▶ [7:07–8:08](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=427s)
The video provides a practical example where the user wants to create a `design.md` file.
1.  The agent is instructed to find tools to help with this task.
2.  It uses the `discover-skills` skill, which searches `skills.sh` and finds several potentially relevant skills.
3.  The user asks the agent to install and test the two most promising candidates.
4.  Following the workflow, the agent first clones and scans both skills *before* installing.
5.  The static scan (without AI) returns a score of `10` (SAFE) for the first skill and `100` (DO_NOT_INSTALL) for the second.
6.  The user then explicitly asks the agent to run the AI scan on the second, flagged skill.
7.  The AI scan re-evaluates the skill and determines the initial flag was a false positive, returning a new score of `0` (SAFE).
8.  With both skills now verified as safe, the agent can proceed to use them. This demonstrates the system's ability to not just block threats but also to intelligently resolve false positives.

## Sponsor: Nimbalyst
▶ [8:08–9:17](https://www.youtube.com/watch?v=VBnG5Fse2ms&t=488s)
The video features a sponsor segment for **Nimbalyst**, a free and open-source visual workspace designed to manage complex AI agent sessions. It solves the problem of having to constantly switch between multiple terminal, browser, and editor windows when working with several AI agents (like Claude Code or Codex) simultaneously.

Key features of Nimbalyst include:
*   **Kanban Board View:** Displays all running agent sessions in a single, organized interface.
*   **Session Management:** Allows users to jump into any session, see what the agent is doing, and review code changes.
*   **Visual Diffing:** Code changes are shown as red and green diffs, which can be approved or rejected individually.
*   **Visual Editing:** Users can edit markdown documents, UI mockups, and architecture diagrams visually alongside the agent.
*   **AI-Powered Commits:** Automatically generates Git commit messages based on the changes made during a session.
*   **Mobile App:** Lets users continue and manage their agent sessions on the go.

The tool is available for download, with a link provided in the video's pinned comment.