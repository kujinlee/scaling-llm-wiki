---
tags:
  - video-summary
  - en
  - openclaw
  - containers
  - kubernetes
  - podman
  - ai agents
  - devops
  - security
video_id: "F1DYkY1BlfM"
channel: "AI Engineer"
lang: EN
type: Demo
audience: Intermediate
score: 4
---

# Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat

**Channel:** AI Engineer | **Duration:** 21:56 | **URL:** https://www.youtube.com/watch?v=F1DYkY1BlfM

> [!summary] Quick Reference
> **TL;DR:** This video champions securely deploying AI agents like OpenClaw within containers using Podman and Kubernetes for reproducibility, scalability, and efficient workflows.
>
> **Key Takeaways:**
> - Run AI agents in containers for reproducibility, secret isolation, portability, and enhanced security.
> - Securely manage AI agent credentials using Podman/Kubernetes secrets and OpenClaw's secret ref feature.
> - Leverage Kubernetes for secure, scalable deployment and lifecycle management of AI workloads.
> - Standardized OpenClaw baselines in containers streamline onboarding and ensure consistent team standards.
> - Custom installers enable rapid local deployment of OpenClaw instances using Podman efficiently.
>
> **Concepts:** openclaw · containers · kubernetes · podman · ai agents · devops · security

---

## 1. The Genesis of Containerized AI Agents
Sally from Red Hat shares her journey into AI, discovering OpenClaw during a staycation. Despite initial security concerns from colleagues, she championed running OpenClaw securely within containers, leveraging her decade-long experience in Linux security and Kubernetes. This experience highlighted the potential for securely deploying rapidly evolving AI applications.

---

## 2. Unpacking the Advantages of Running AI in Containers
The speaker passionately advocates for running *everything* in containers, especially AI agents. She illustrates this with her "forever claw" personal agents (Joy for astrology, Bruno for Bruins updates). Key benefits highlighted include:
- **Reproducibility:** Ensuring consistent environments.
- **Secret Isolation:** Securely managing sensitive API keys.
- **Portability:** Running across diverse infrastructure (laptops, X86, Mac, Kubernetes).
- **Backup and Recovery:** Simplified via backed volumes.
- **Natural Sandbox:** Providing inherent security isolation.
- **Clean Environment:** Eliminating OS quirks and stale dependencies.

---

## 3. Advanced Secret Management for OpenClaw Deployments
A critical aspect of deploying AI agents is managing credentials securely. The talk details using Podman secrets (specifically `podman secrets`) for API keys, which are then referenced within OpenClaw's own secret ref feature. This layered approach provides enhanced separation and prevents secrets from appearing in logs. The same principle extends to Kubernetes secrets, replacing direct environment variables with secure references, emphasizing a robust security posture for AI workloads.

---

## 4. Scaling AI Workloads with Kubernetes: A Vision for the Future
The speaker envisions a future where interconnected OpenClaw agents run ubiquitously, especially for business applications. Kubernetes is presented as the ideal platform to provide the necessary security, scalability, and lifecycle management for these AI workloads. An example from PyTorchCon highlights Nvidia's use of OpenClaw in Kubernetes for model evaluations, demonstrating significant efficiency gains and freeing engineers for more creative, non-tedious tasks. This shift enables teams to "dream bigger" and focus on innovation.

---

## 5. Transforming Workplace Workflows and Onboarding with OpenClaw
A compelling vision for enterprise OpenClaw deployment is introduced: a curated "baseline OpenClaw" for new hires. This baseline would include company-approved MCP servers, authentication, team-specific skills, and access to internal resources. This standardized yet personalizable setup promotes team standards, provides portable environments, and ensures reproducible onboarding. It streamlines the integration of AI tools into daily workflows, contrasting sharply with the ad-hoc setup often faced by new team members.

---

## 6. Live Demonstration: Rapid OpenClaw Deployment via a Custom Installer
The presentation culminates in a live demonstration of a custom installer tool. This opinionated NPM-based tool simplifies spinning up OpenClaw instances locally using Podman (or Docker). The demo showcased:
- Quickly creating a named pod.
- Mapping Podman secrets for API keys directly into OpenClaw's secret ref.
- Selecting AI model providers (e.g., Open Router, Anthropic).
- Optional features like Open Telemetry integration and SSH sandbox.
The process was shown to be extremely fast, highlighting the ease of deployment. The speaker also briefly touched on extending this deployment model to Kubernetes and OpenShift.

---

## Conclusion
The talk makes a strong case for the secure and efficient deployment of AI agents like OpenClaw using containerization technologies such as Podman and Kubernetes. By embracing these practices, organizations can achieve reproducibility, enhanced security, scalability, and streamlined team workflows, ultimately enabling engineers to focus on higher-value, creative work. The vision for a future of interconnected, containerized AI agents is compelling, promising a transformative impact on how we develop and deploy AI applications.