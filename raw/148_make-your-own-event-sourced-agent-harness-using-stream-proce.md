---
tags:
  - video-summary
  - en
  - event sourcing
  - ai agents
  - stream processing
  - distributed systems
  - agent harnesses
  - typescript
  - llms
video_id: "vi-2nasppAg"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Advanced
score: 4.2
---

# Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate

**Channel:** AI Engineer | **Duration:** 1:04:27 | **URL:** https://www.youtube.com/watch?v=vi-2nasppAg

> [!summary] Quick Reference
> **TL;DR:** This video introduces an event-sourced architecture for AI agent harnesses, emphasizing debuggability, extensibility, and dynamic configuration via stream processors.
>
> **Key Takeaways:**
> - Adopt event sourcing to capture all system activity as immutable, debuggable events in a stream.
> - Design agent logic using stream processors with pure reducer functions and separate side-effect hooks.
> - Enable dynamic agent updates and self-modification by appending code directly to event streams.
> - Utilize a distributed architecture for agents, supporting polyglot components and stream control features.
>
> **Concepts:** event sourcing · ai agents · stream processing · distributed systems · agent harnesses · typescript · llms

---

## 1. The Vision: Event-Sourced Agent Harnesses
Jonas introduces a novel approach to building AI agent harnesses, driven by the need for enhanced debuggability, extensibility, and composability. Traditional agent frameworks are often limited by single-threaded execution and opaque internal states, hindering experimentation and integration. The proposed architecture fundamentally treats every action and state change within an agent as a durable event in a stream, moving towards a truly 'debuggable' and 'polyglot' system.

---

## 2. Core Principles of the Iterate Platform
The `events.iterate.com` service is the backbone of this architecture, embodying several key design philosophies:
*   **Event Sourcing:** All system activity, from user input to LLM responses, is captured as a stream of immutable, YAML-formatted events. Each event has a `type` (often a URL linking to documentation) and a `payload`.
*   **Extensibility & Composability:** Agents are designed to be dynamically extensible, not just by humans, but by other agents or even themselves, facilitating the combination of diverse functionalities.
*   **Publicly Routable (On the Edge):** The goal is for every agent to have a direct URL, enabling them to communicate via HTTP, simplifying integration with webhooks and internet services. While acknowledging security concerns (lack of authentication in the demo), the vision is for agents to be internet-native entities.
*   **Distributed Architecture:** Components (agents, plugins) can run across different machines and in various programming languages (e.g., Rust, TypeScript), fostering a highly distributed and resilient ecosystem. Potential challenges like race conditions and infinite loops are addressed through features like stream pausing.

---

## 3. Interacting with `events.iterate.com`
The workshop demonstrates basic interaction with the platform using `curl` commands. Users can:
*   **Append Events:** Post events to hierarchical 'agent paths'. Events are automatically assigned `stream path`, `offset`, and `created at` metadata.
*   **Stream Events:** Subscribe to live event streams using Server-Sent Events (SSE) with a `live=true` parameter, allowing for real-time consumption of new events.
*   **Stream Control:** Features like idempotency keys prevent duplicate events, and a circuit breaker mechanism automatically pauses streams exceeding a certain event rate (e.g., 100 events/second) to prevent infinite loops. Pausing/resuming is itself managed by appending specific events to the stream.
*   **Advanced Features:** Mentions the ability to schedule future events (e.g., heartbeats) and configure push subscriptions (webhooks) to external services based on stream activity.

---

## 4. The Stream Processor Paradigm
Agent logic is encapsulated in 'stream processors', which are executed by a runtime. Each processor comprises:
*   **Reducer Function:** A pure, synchronous function that takes the current agent state and a new event, returning an updated state. This function should *not* have side effects. This design allows the system to efficiently 'catch up' on a backlog of events without re-triggering external actions.
*   **After Append Hook:** A function triggered after the reducer, where side effects (e.g., making LLM requests, appending new events to the stream or sub-streams) are performed. This separation ensures predictable state management and control over external interactions.
*   **Polyglot Support:** Although the demo uses TypeScript, the architecture supports processors written in any language, communicating via HTTP API.

---

## 5. Dynamic Worker Configuration and AI Agent Integration
A standout feature is the ability to make streams programmable by appending a `dynamic worker configured` event. This event's `script` payload contains JavaScript source code for a reducer and `afterAppend` hook. This effectively deploys agent logic directly into the stream, allowing:
*   **On-the-fly Agent Updates:** Agents can be reconfigured or enhanced by simply appending new code-containing events.
*   **Self-Modifying Agents:** Future implementations could allow AI agents to generate and append new code to modify their own behavior. Error handling would also be event-sourced, with compiler errors potentially triggering AI self-correction.
*   **Modular AI Capabilities:** The vision extends to bundling full OpenAI SDKs within these dynamic workers, allowing a simple event stream to become a powerful, self-contained AI agent. This also provides a clear model for integrating external services, like prompt injection protection, into an agent's processing loop in an eventually consistent manner.

---

## Conclusion
Despite technical hitches during the live demo, the workshop effectively introduced a compelling event-sourced architecture for building highly debuggable, extensible, and distributed AI agent harnesses. The `events.iterate.com` platform, with its stream-centric approach and dynamic worker capabilities, offers a flexible foundation for experimenting with and deploying complex AI systems, emphasizing a `web standards-based` and `one abstraction` philosophy. The potential for agents to be self-configuring and to integrate seamlessly with various external services through a unified event stream presents an innovative direction for AI engineering.