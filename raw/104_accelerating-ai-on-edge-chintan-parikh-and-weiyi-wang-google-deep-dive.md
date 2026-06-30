---
tags:
  - video-summary
  - deep-dive
  - en
  - gemma models
  - edge ai
  - on-device ml
  - lite rt
  - tensorflow lite
  - llm deployment
  - cross-platform ai
video_id: "Lm8BLHkxiAo"
channel: "AI Engineer"
lang: EN
type: Framework
audience: Intermediate
score: 4.2
---

# Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind (Deep Dive)

**Channel:** AI Engineer | **Duration:** 23:58 | **URL:** https://www.youtube.com/watch?v=Lm8BLHkxiAo

---

## Introduction and Agenda
▶ [0:15–1:27](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=15s)
The presentation is given by Chintan Parekh, a product manager for LiteRT, which is part of Google AI Edge. The talk begins with an overview of the agenda, which includes:
*   New models, specifically the Gemma 4 family.
*   Relevant on-device (Edge) use cases.
*   New capabilities demonstrated through a gallery app.
*   The technology stack for deploying AI on Edge devices.
*   Emphasis on the cross-platform support offered.

The speaker's goal is to cover these topics and leave time for discussion about specific use cases attendees might be working on.

## Google's On-Device Models: Gemma 4 and Gemma 3
▶ [1:27–2:13](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=87s)
Google DeepMind recently launched the Gemma 4 family of models. This presentation focuses specifically on the smaller variants designed for on-device deployment: the 2-billion (2B) and 4-billion (4B) parameter Edge models.

The speaker notes that the evolution with Gemma 4 represents a significant shift in capability, moving "from chatbot type capabilities to more autonomous agents that also support reasoning capabilities and more sophisticated features."

Alongside Gemma 4, the Gemma 3 family also includes smaller models, with sizes down to 270 million parameters, suitable for fine-tuning on extremely constrained devices. These models are available on Google's Hugging Face page.

## Benefits of On-Device AI (Running on Edge)
▶ [2:13–3:10](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=133s)
Running AI models directly on edge devices offers several key advantages over cloud-based execution:

*   **Latency:** For real-time applications like camera filters, background replacement, or video calls, low latency is critical. On-device processing eliminates network round-trip time.
*   **Privacy:** When dealing with sensitive data, such as summarizing confidential documents, processing on-device ensures the information never leaves the user's control.
*   **Offline Capability:** Models can function in environments with poor or no internet connectivity.
*   **Cost:** On-device inference can offset the cost of cloud computing. The speaker notes that many AI engineers complain about token usage, and a hybrid approach (running some tasks on-device and some in the cloud) can provide a cost-effective balance.

## Gemma 4 Edge Models Deep-Dive
▶ [3:10–3:51](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=190s)
The presentation focuses on two specific models from the Gemma 4 family, designed for edge deployment. Their characteristics are:

*   **Gemma 4 E2B (2 Billion parameters):**
    *   **RAM Usage:** Approximately 1 to 2 GB after quantization.
    *   **Use Cases:** Well-suited for voice interfaces, summarization, and other low-latency local processing tasks.
*   **Gemma 4 4B (4 Billion parameters):**
    *   **RAM Usage:** Higher RAM requirement, making it more suitable for "heavy duty" tasks.
    *   **Target Platforms:** Laptops and more powerful IoT devices.

The RAM usage figures are based on the models being quantized to a desired size.

## New Agent Capabilities in Gemma 4
▶ [3:51–5:12](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=231s)
Gemma 4 introduces several new capabilities that support the development of more sophisticated on-device agents:

*   **Function Calling:** The models have built-in support for tool calling, allowing them to interact with other local or external APIs. An inference task can start on the edge and then call out to other services to complete its work.
*   **Structured JSON Output:** The models natively support generating structured JSON. This capability is "built into the model architecture rather than achieving through some kind of specific prompt engineering."
*   **Chain of Thought:** A new "thinking mode" is available, which allows an application to demonstrate the model's thought process as it works through a problem. This feature is supported in the showcase gallery app.
*   **Hardware Optimization:** The models are optimized for hardware-native support, enabling them to run "seamlessly across multiple platforms and multiple hardwares" to provide developers with deployment flexibility.

## Model Availability
▶ [5:12–5:33](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=312s)
The Gemma models discussed are readily available for developers to use. They are hosted on Google's Hugging Face page and are licensed under the Apache 2.0 license. This allows developers to download the models and begin building applications with them immediately.

## Use Cases and The Gallery App
▶ [5:33–7:09](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=333s)
A gallery app is presented as a "playground to get a feel for what these models are capable of." All processing in the app happens on-device. The app demonstrates the new agent skills of Gemma 4 and provides sample code for each feature, which developers can use or fork to build their own experiences.

The new use cases focus on three key pillars: voice agent capabilities, local agent capabilities, and privacy.

### Augmenting Knowledge
▶ [7:09–7:36](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=429s)
A skill is demonstrated where the on-device agent can query Wikipedia. This allows the agent to answer encyclopedic questions by augmenting its knowledge with an external API call, showcasing the function-calling capability.

### Personal Tracking and Data Analysis
▶ [7:36–8:34](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=456s)
A video demo shows a user creating a "sleep and mood" tracking agent.
1.  The user provides a voice entry: "8 hours of sleep and I'm looking forward to hanging out with Amy today."
2.  The user then asks the agent to "Analyze the trend in my mood over the last 7 days."
3.  The agent processes this data entirely on-device and generates a chart showing the trend. This demonstrates the model's new reasoning and thinking capabilities.

### Creative Generation
▶ [8:34–9:29](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=514s)
Another demo showcases the model's ability to pair a photo with music.
1.  The user sends a photo to the agent and says, "Can you pair this vibe with some music?"
2.  The model uses its image understanding to analyze the photo's "vibe" and generates a piece of music to match it, all on the device.

### Complex Workflows
▶ [9:29–10:09](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=569s)
The final example demonstrates managing a more complex workflow involving multiple apps and users. The user gives a prompt to describe the vocal calls of animals, and the on-device agent generates the corresponding sound. This skill, like others, can be written and loaded by the user directly within the gallery app.

## Building Your Own Experiences
▶ [10:09–11:02](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=609s)
The speaker emphasizes that the ecosystem is designed to be open and extensible.
*   **GitHub Repository:** There is a GitHub repository where users post their own custom "skills" for the gallery app, sharing them with the community.
*   **Open Source App:** The sample gallery app itself is open source on GitHub, allowing developers to fork it and make changes.
*   **Instructions:** A QR code is provided that links to instructions on how to build a new skill from scratch.

## The LiteRT Deployment Framework
▶ [11:02–12:41](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=662s)
The underlying technology powering these on-device experiences is **LiteRT**.

*   **Foundation:** LiteRT is Google's on-device AI framework, built upon the well-established **TensorFlow Lite**. It uses the same `.tflite` model format.
*   **Scale:** It is a widely deployed and trusted framework, with statistics cited as:
    *   100,000+ apps in production.
    *   Billions of active users.
    *   Vast numbers of daily "interpreter invocations" (inferences).
*   **Multi-Framework Support:** The rebranding from TensorFlow Lite to LiteRT was partly to "demonstrate that it's not just TensorFlow Lite models that we accept, but also PyTorch models and JAX models."

A developer can take a model from PyTorch or JAX, convert it to the TFLite file format, and then deploy it using the LiteRT stack.

## Developer Workflow and The LiteRT Stack
▶ [12:41–16:30](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=761s)
LiteRT provides a complete, unified, cross-platform architecture for on-device AI deployment. The workflow and components of the stack are as follows:

```ascii
      [PyTorch / JAX / TensorFlow Models]
                       |
                       ↓ (Convert model)
               [LiteRT torch / Converter]
                       |
                       ↓ (Produces a .tflite model file)
            [.tflite Model Format]
                       |
   +-------------------+-------------------+
   | (LLM path)                            | (Other models)
   ↓                                       ↓
[LiteRT LLM]                           [LiteRT]
   |                                       |
   +-------------------+-------------------+
                       |
                       ↓ (Analyze and optimize graph)
      [Model Explorer & Quantization Tools]
                       |
                       ↓ (Benchmark on real devices)
                 [AI Edge Portal]
                       |
                       ↓ (Deploy to hardware)
        [CPU / GPU / NPU Acceleration]
                       |
                       ↓ (Run on target platform)
    [Android / iOS / Linux / Windows / Web / IoT]
```

### Stack Components
*   **Model Conversion (LiteRT torch):** Tools to convert models from PyTorch and JAX into the `.tflite` format.
*   **Runtimes (LiteRT / LiteRT LLM):** Optimized runtimes for general AI models (LiteRT) and Large Language Models (LiteRT LLM).
*   **Model Explorer:** A tool to visualize the model graph, allowing developers to inspect it and decide how to apply optimizations like mixed-precision quantization.
*   **AI Edge Portal:** A cloud-based benchmarking service that helps developers test their models on a broad fleet of real Android devices. This helps determine the right compilation strategy (e.g., ahead-of-time vs. just-in-time) to ensure reliability and performance.
*   **Acceleration:**
    *   **CPU/GPU:** Universal support is available across platforms.
    *   **NPU (Neural Processing Unit):** Integration is complete with partners like Qualcomm and MediaTek, with more in progress. NPU acceleration is a "game-changer," offering a **3 to 10x improvement in performance** and energy efficiency, which is critical for real-time AR/VR and TTS applications.

## Cross-Platform Support and Performance
▶ [16:30–19:08](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=990s)
A key strength of the LiteRT framework is its ability to deploy a single model file across numerous platforms. The Gemma models have been tested and verified on:
*   Android
*   iOS
*   Linux
*   macOS
*   Windows
*   Web
*   Raspberry Pi

A demo shows a small robot built with a Raspberry Pi running the Gemma model on-device via the LiteRT LLM runtime on its CPU. When shown a sign that says "move your antenna," the robot performs inference and then wiggles its "antennas" (made of Sharpies).

A new CLI tool with Python bindings is also available to simplify the deployment process.

### Performance Benchmarks
*   **NPU Boost:** Using NPUs can provide up to a **13x performance boost** in some cases.
*   **iOS:** Performance on iOS is cited at roughly **56 tokens per second**.
*   **Desktop & IoT:** Performance numbers for these platforms are available on the Hugging Face model pages.
*   **Runtime Comparison:** The LiteRT runtime is benchmarked against Llama.cpp:
    *   **Mobile:** Up to **35x faster**.
    *   **Desktop:** At par.
    *   **IoT:** Up to **3x faster**.

## Summary and Q&A
▶ [19:08–23:43](https://www.youtube.com/watch?v=Lm8BLHkxiAo&t=1148s)
In summary, LiteRT supports multiple frameworks (TensorFlow, PyTorch, JAX), provides open-weight Gemma models on Hugging Face, and offers the gallery app as a playground for developers.

### Q&A Session
*   **Q: Can this be used for on-device face unlock for a home camera?**
    *   **A:** Yes. Face unlock on phones (like Pixels and iPhones) already runs locally using similar on-device frameworks (LiteRT on Google devices, CoreML on Apple). A home camera solution would be slightly different, potentially requiring algorithms to check authenticity, but it is "totally" possible to run on-device, for instance on a Raspberry Pi, which could then send a message to your phone.
*   **Q: Do you have performance numbers for NVIDIA Orin?**
    *   **A:** The speaker does not have the numbers in the slides but believes they are available on the Hugging Face page for the models.
*   **Q: Are there examples of hybrid architectures that split work between edge and cloud?**
    *   **A:** Yes, there are groups working on concepts like "speaker and a thinking agent" architectures. An orchestration layer decides which tasks should run locally and which should be sent elsewhere. The speaker mentions potential applications like a "health agent or coaching agent" but has no specific examples to share in the presentation.
*   **Q: Do you support other open-weight models besides Gemma?**
    *   **A:** Yes. The framework can support any open-weight model, provided it can be converted to the correct file format and its size is appropriate for the target device. The Hugging Face page has other models available, and developers are welcome to convert and use their own preferred models.