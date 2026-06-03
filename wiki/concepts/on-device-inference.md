---
concept: On-Device Inference
category: LLM Internals & Training
summary: Running LLM inference locally on edge devices rather than in the cloud — trading raw model capability for privacy, low latency, offline operation, and elimination of per-token cloud cost.
aliases: [on-device inference, edge AI, edge LLM, on-device ML, local inference, edge inference, on-device LLMs, edge model deployment, edge agents]
related: [inference-batching-economics, kv-cache-economics, subscription-vs-metered-pricing, agent-as-infrastructure, model-abstraction-layer, compute-memory-tradeoff]
sources: [accelerating-ai-on-edge-chintan-parikh-and-weiyi-wang-google]
---

# On-Device Inference

On-device inference is running an LLM's forward pass locally on the user's own edge hardware — phone, laptop, single-board computer, IoT device — instead of calling a hosted model in a datacenter. The bet is that a small, quantized model running on the device buys four properties a cloud API cannot: data never leaves the device (privacy), there is no network round-trip (low latency for real-time uses like video filters and camera effects), it functions without connectivity (offline), and it carries no per-token cloud bill (cost). The price is capability — edge models are far smaller than frontier cloud models — so on-device inference is a deliberate trade of raw model strength for locality, the local-execution counterpart to the cloud-hosted always-on pattern of `[[agent-as-infrastructure]]`.

## Key Mechanics

- **Four drivers for moving inference to the edge**: privacy (sensitive data processed where it lives), latency (no network hop, enabling real-time camera/video uses), offline operation (works with poor or no connectivity), and cost (offsetting cloud inference spend).
- **Small models by necessity**: edge-targeted models are sized to fit device memory and compute (the corpus cites 2B–4B-parameter models, down to ~270M for the most compact uses) — the opposite end of the parameter-count spectrum from datacenter-served frontier models.
- **Quantization to fit and accelerate**: weights are quantized to reduce footprint and speed execution — a deployment-stage instance of the `[[compute-memory-tradeoff]]`, spending precision to buy memory and throughput on constrained hardware.
- **Cross-platform runtime**: a common on-device model format with converters from training frameworks (PyTorch, JAX) lets one model run across Android, iOS, desktop, web, and IoT, decoupling the deployed model from the target hardware.
- **Hardware-native acceleration**: routing the model onto the device's CPU/GPU and especially its NPU yields large speed and energy gains (cited at 3–10x, up to ~13x in some scenarios), which is what makes otherwise-too-slow local inference practical.
- **On-device agents**: small edge models now carry agent primitives — function/tool calling to local APIs and native structured-JSON output, plus a visible chain-of-thought "thinking mode" — so the core reasoning runs locally while still reaching out to external tools, rather than being a chatbot only.

## How It Appears in the Corpus

The Chintan Parikh / Weiyi Wang (Google DeepMind) "Accelerating AI on Edge" talk presents Gemma 4 Edge models (2B/4B, with sub-billion Gemma 3 variants) deployed via the Lite RT framework (formerly TensorFlow Lite). It motivates edge inference with privacy, latency, offline use, and cloud-cost savings; demonstrates on-device agent skills — function calling, structured JSON, and demos such as Wikipedia-augmented knowledge and a mood/sleep journaling agent — in an open-source Gallery App where all work is performed locally; and details a deployment stack that converts PyTorch/JAX models to the TFLite format, quantizes them, and accelerates them on CPU/GPU/NPU (with Qualcomm and MediaTek partners) for large gains, running cross-platform across Android, iOS, Linux, and Raspberry Pi.

## Tensions & Tradeoffs

- **Capability vs. locality**: edge models are far smaller and less capable than frontier cloud models, so on-device inference suits scoped, well-bounded tasks rather than the hardest reasoning — the inverse choice from the cloud-hosted, always-on model of `[[agent-as-infrastructure]]`, which already names this local-vs-cloud execution locality as a capability tradeoff.
- **Different cost physics**: the batch-size amortization that makes cloud serving cheap (`[[inference-batching-economics]]`, `[[kv-cache-economics]]`) does not apply to a single user's device — on-device cost is paid in device compute and battery, not per token, which sidesteps the metered-vs-flat-rate tension of `[[subscription-vs-metered-pricing]]` entirely rather than resolving it.
- **Acceleration bounds the promise**: practical speed depends on hardware-native (NPU) support actually existing for the target device; without it, local inference can be too slow, so the cross-platform claim is bounded by per-device acceleration availability.
- **Portability moves, it does not vanish**: a common runtime format plus framework converters is a deployment-level analogue of a `[[model-abstraction-layer]]`, but lock-in relocates to the runtime/format rather than disappearing.
- **Vendor-benchmark caveat**: the performance figures (3–13x speedups, tokens/sec) are vendor benchmarks from a product talk, not independent measurements.
