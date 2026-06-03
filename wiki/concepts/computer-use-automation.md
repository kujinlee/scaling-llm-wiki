---
concept: Computer-Use Automation
category: Agent Architecture & Patterns
summary: Operating existing applications through their GUI — clicking, typing, reading the screen — to automate workflows that expose no API.
aliases: [GUI automation, app control without API, human-like app operation, screen automation]
related: [agent-router, harness-engineering, github-as-blueprint]
sources: [나의-ai-에이전트-전환기-w-클로드-코드-오픈클로]
---

# Computer-Use Automation

Computer-use automation is the technique of having an agent operate existing applications and websites the way a human would — clicking, typing, and reading the screen — so a task can be automated even when the target system exposes no API. It removes the dependency on official integrations: if a person can do it through an app, an agent can be made to do it too.

## Key Mechanics

- The agent drives real software through its user interface rather than a programmatic API, reading state from the screen and issuing input events.
- Device-control tooling extends this to mobile: pairing a spare Android phone with ADB and a screen-mirroring library (Scrcpy) lets the agent operate native apps end-to-end.
- It unlocks "long-tail" automations that vendors never provide hooks for, treating the GUI as the universal integration surface.

## How It Appears in the Corpus

The Korean agent-transition talk's everyday-assistant layer leans on strong computer-control ability: it archives KakaoTalk "message-to-self" notes into a spreadsheet without any KakaoTalk API, and monitors KTX train-seat availability by driving the KorailTalk app on an old Android phone via ADB and Scrcpy.

## Tensions & Tradeoffs

- Brittleness: UI-driven automation breaks when layouts change, and is slower and less robust than a real API.
- Operational overhead: it depends on spare devices and always-on infrastructure, and screen-scraping app data sits in a legal/terms-of-service gray area.
