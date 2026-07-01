---
tags:
  - video-summary
  - en
  - ai models
  - code generation
  - fable 5
  - opus 48
  - 3d rendering
  - e-commerce
  - real-time strategy games
video_id: "TzJCly4YgDQ"
channel: "Pat Simmons"
lang: EN
type: Analysis
audience: Advanced
score: 4.6
---

# I Made Opus 4.8 and Fable 5 Build the Same App (RAW RESULTS)

**Channel:** Pat Simmons | **Duration:** 21:12 | **URL:** https://www.youtube.com/watch?v=TzJCly4YgDQ

> [!summary] Quick Reference
> **TL;DR:** This video critically compares Claude's new Fable 5 and Opus 48 by tasking them with building three complex web applications, revealing Fable 5's clear superiority.
>
> **Key Takeaways:**
> - Fable 5 significantly outperforms Opus 48 in complex code generation tasks.
> - Fable 5 excels in realistic 3D rendering and interactive UI/UX design.
> - Despite higher per-token cost, Fable 5's output quality often justifies the expense.
> - Expect higher quality and more functional applications from Fable 5.
> - AI models can now generate complex, interactive 3D environments and games.
>
> **Concepts:** ai models · code generation · fable 5 · opus 48 · 3d rendering · e-commerce · real-time strategy games

---

## 1. Introduction to the AI Model Showdown
▶ [0:00–0:24](https://www.youtube.com/watch?v=TzJCly4YgDQ&t=0s)
This video conducts a head-to-head comparison between Claude's Opus 48 and its new flagship model, Fable 5. Both models are tasked with building three complex projects: a fully functioning e-commerce store, an interactive 3D art museum, and an Age of Empires clone. The rules for the test were strict: a single one-shot output with no revisions, deployed live on the internet. The initial impression suggests the results were not even close.

---

## 2. E-commerce Store: Functionality vs. Finesse
▶ [0:24–8:06](https://www.youtube.com/watch?v=TzJCly4YgDQ&t=24s)
The first project involved building a complete e-commerce site for a fictional candle brand, "Slow Burn," aiming for Shopify-level production quality with 30 distinct products and visually distinct images. The prompt was refined to avoid previous UI pitfalls like low-contrast text and unlabelled products. This build tested landing page and e-commerce design, database integration, and overall architecture.

Opus 48 delivered a functional site, an improvement over previous attempts, with readable text and some image labels. However, it suffered from several UI/UX flaws, including poor candle placement, an unappealing CTA button, messy category filters, and a terrible navbar experience.

In contrast, Fable 5 produced a significantly cleaner and more polished e-commerce site. It featured classic e-commerce elements like a top notification bar, rotating product displays, much better buttons with gradients, a superior header image, and subtle hover animations. Fable 5 also demonstrated a smarter approach to prompting image generation for the product photos, resulting in a more cohesive aesthetic. Its filtering system was also vastly superior.

Fable 5 was approximately 15 minutes faster, completing the build in about 35 minutes compared to Opus's 50 minutes. Regarding cost, Opus 48 used 198k output tokens for an estimated $21.41, while Fable 5 used 188k output tokens for an estimated $36.84, indicating Fable 5 is more expensive per token but more token efficient in this instance. Fable 5 was the clear winner for this challenge.

---

## 3. Interactive 3D Art Museum: A Vision Realized
▶ [8:06–17:23](https://www.youtube.com/watch?v=TzJCly4YgDQ&t=486s)
The second, more ambitious project was to create an interactive 3D art history museum in the browser. The vision included a zoomable timeline of art periods, artists, museum placards, and realistic 3D galleries populated with paintings from the Wikimedia Commons API, stored in a Neon database. A key requirement was to avoid "blobby 3JS" and achieve realistic lighting, tone mapping, and an immersive experience.

During the build, Opus 48 encountered a public domain constraint for modern art images (e.g., Picasso), which Fable 5 also acknowledged but handled more gracefully. Fable 5 completed its output about 15 minutes faster than Opus and showed advanced self-correction capabilities, like identifying complex data parsing errors (e.g., "Francis Bacon (artist)"). It also demonstrated design opinions, such as disliking a "pitch black floor."

Opus 48 generated a color-coded timeline view that was zoomable, but artist elements were scattered and overlapped. Crucially, the galleries were not clickable, rendering the core interactive museum experience broken.

Fable 5 delivered an exceptionally clean and functional 3D museum. Its timeline featured an astrological motif with smoothly zooming artist representations that transformed into dots when zoomed out, preventing overlap. The most impressive aspect was the fully functional and highly realistic 3D galleries, allowing users to move around, view paintings, and interact with information placards. The fluid motion and detailed rendering truly brought the concept to life.

Cost-wise, Opus 48 consumed 437k output tokens for an estimated $46, while Fable 5 used 280k output tokens for an estimated $64. Despite Fable 5 being more expensive per token, its unparalleled functionality and quality made it the undeniable victor.

---

## 4. Age of Empires Clone: The Ultimate 3D Game Test
▶ [17:23–21:13](https://www.youtube.com/watch?v=TzJCly4YgDQ&t=1043s)
The final, and arguably most challenging, task was to build a fully playable Age of Empires-style real-time strategy (RTS) game in the browser, complete with a full 3D world, dozens of units, attack mechanics, and civilization building. The prompt explicitly requested realistic, multi-textured graphics, rejecting a stylized low-poly approach.

Opus 48 finished in 33 minutes, but its output was described as "blobs" with graphics nowhere near Age of Empires quality. More critically, the application was completely broken; there was no map movement or building functionality, making the game unplayable.

Fable 5 completed the task in 30 minutes and delivered an astonishing "Empires of Dawn" game. The graphics were lauded as "insane" and "just as good as Age of Empires," featuring detailed civilizations, navigable maps, and enemies with armor. The game appeared fully playable with building mechanics and resource management, although the presenter didn't delve deeply into gameplay. Fable 5's ability to render such high-quality, interactive 3D game environments was highlighted as being on "another level" compared to Opus 48.

---

## Conclusion: Fable 5's Dominance and Cost Implications
Across all three complex coding challenges—e-commerce, 3D art museum, and RTS game—Fable 5 consistently outperformed Opus 48. Fable 5 demonstrated superior speed, token efficiency (in terms of fewer output tokens for two of three tasks), and most notably, significantly higher quality and functionality in its outputs. It excelled in UI/UX design, realistic 3D rendering, complex data handling, and delivering truly interactive experiences, whereas Opus often produced functional but flawed or broken applications. While Fable 5's usage-based pricing is higher, the substantial leap in quality and capability it offers makes it a compelling choice for demanding development tasks. This comparison solidifies Fable 5's position as a powerful, next-generation AI model for code generation.