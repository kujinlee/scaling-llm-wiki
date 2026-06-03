---
concept: Agent Router
category: Agent Architecture & Patterns
summary: A top-level orchestrator agent that receives all incoming instructions and dispatches them to the appropriate specialized downstream agent, acting as single point of contact for a fleet.
aliases: [router agent, dispatcher agent, secretary agent, single entry point agent]
related: [harness-engineering, computer-use-automation, multi-agent-code-review, meta-skills]
sources: [나의-ai-에이전트-전환기-w-클로드-코드-오픈클로]
---

# Agent Router

An agent router is a top-level orchestrator agent that acts as the single point of contact for a fleet of specialized agents, interpreting each incoming request and dispatching it to the right downstream agent. It turns a sprawling collection of task-specific automations into one coherent interface the operator can command from a single channel.

## Key Mechanics

- One inbound channel, many workers: the router receives every instruction and routes it to the appropriate specialized agent rather than the operator addressing each agent directly.
- It functions like a chief-of-staff: classifying the request, selecting the handler, and coordinating the response.
- Pairs naturally with a chat surface (e.g. Telegram) so the entire agent fleet is driven from one conversation.

## How It Appears in the Corpus

In the Korean agent-transition talk, a router agent nicknamed "Jarvis" serves as the secretary/chief-of-staff layer: all agent tasks are issued through it over Telegram, and it distributes work to the underlying professional (`[[harness-engineering]]`-defined) and everyday agents.

## Tensions & Tradeoffs

- Single point of failure and bottleneck: concentrating all dispatch in one router makes its reliability and routing accuracy critical.
- As fleet size grows, routing and oversight become their own management problem — the corpus likens running many agents to a manager's or executive's coordination workload.
