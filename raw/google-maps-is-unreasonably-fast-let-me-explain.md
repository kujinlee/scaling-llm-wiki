---
tags:
  - video-summary
  - en
  - dijkstra's algorithm
  - pathfinding
  - graph algorithms
  - google maps
  - a-star algorithm
  - customizable contraction hierarchies
  - computer science
  - navigation software
video_id: "kS-CGkiPetQ"
channel: "Veritasium"
lang: EN
type: Analysis
audience: Intermediate
score: 4.8
---

# Google Maps is unreasonably fast. Let me explain

**Channel:** Veritasium | **Duration:** 29:54 | **URL:** https://www.youtube.com/watch?v=kS-CGkiPetQ

> [!summary] Quick Reference
> **TL;DR:** This video explains how navigation apps find optimal routes using algorithms that evolved from Dijkstra's original invention to modern hierarchical methods.
>
> **Key Takeaways:**
> - Dijkstra's algorithm efficiently finds shortest paths on weighted graphs by prioritizing unexplored nodes with the lowest known cost.
> - A-star algorithm improves Dijkstra's by using a heuristic (like straight-line distance) to guide searches toward the target, making it faster.
> - Modern navigation systems use customizable contraction hierarchies to leverage road network structure for ultra-fast, accurate route calculations.
> - Contraction hierarchies pre-process graphs to rank nodes by importance and add "shortcuts," drastically reducing search space during queries.
> - Optimizing pathfinding involves a trade-off between pre-processing time (to build hierarchical structures) and real-time query speed.
>
> **Concepts:** dijkstra's algorithm · pathfinding · graph algorithms · google maps · a-star algorithm · customizable contraction hierarchies · computer science · navigation software

---

## 1. The Ubiquitous Problem and Dijkstra's Elegant Solution
Modern navigation systems, like Google Maps, solve the seemingly impossible task of finding the shortest path between two points in milliseconds, despite an astronomical number of possible routes. This video traces the origin of these solutions back to Edsger Dijkstra's 1956 quest to demonstrate the power of early computers. His inspiration for the "shortest path algorithm" came from a simple shopping trip in Amsterdam, aiming to find the quickest route between two Dutch cities.

---

## 2. From Basic Search to Weighted Graphs: The Birth of Dijkstra's Algorithm
Initial attempts to find shortest paths, such as Breadth-First Search, work well if all roads have equal length. However, real-world roads have varying distances. Dijkstra's breakthrough was an algorithm that maintains a running total of the shortest distance (cost) from the source to every node. It iteratively explores unexplored nodes, always prioritizing the one with the lowest current cost. By updating neighbor costs if a shorter path is found, Dijkstra's algorithm guarantees the shortest path to any target. This elegant "20-minute invention" was eventually published in 1959 and became a cornerstone of computer science.

---

## 3. Enhancing Pathfinding: A-star and Bi-directional Search
While Dijkstra's algorithm is fast for local areas, it becomes slow for continent-sized networks as it searches in all directions. The A-star algorithm improves upon Dijkstra's by incorporating a "heuristic" – an educated guess, like the straight-line distance to the target – to prioritize nodes that are geographically closer to the destination. This reduces the search space significantly, making it popular in video games. Further optimization comes from bi-directional searches, where two Dijkstra searches run simultaneously from the source and the target, meeting in the middle to cover a much smaller area. However, these still don't fully leverage the inherent hierarchy of road networks (highways vs. local roads).

---

## 4. The Need for Hierarchy: Limitations of Early Approaches
Early in-car GPS systems attempted to incorporate road hierarchy by manually categorizing roads (e.g., express highway, local major road). These systems would then run a bi-directional Dijkstra, prioritizing higher-level roads within a "candidate area." While this reduced search times, it was cumbersome due to manual categorization and risked missing optimal paths if the candidate area was too small. A more robust, automated approach was needed for global-scale mapping.

---

## 5. Modern Mapping: Customizable Contraction Hierarchies
Modern navigation apps employ sophisticated methods like customizable contraction hierarchies (CCHs). This approach involves two main steps: pre-processing and querying. Phase one automatically ranks nodes by their "importance" (how many shortest paths pass through them) using techniques like nested dissection, and adds "shortcuts" to represent shortest paths that might otherwise pass through lower-ranked nodes. Phase two calculates shortcut weights based on real-time data (like traffic). The actual search (phase three) then uses a bi-directional Dijkstra, restricted to only searching "up" the hierarchy, making it incredibly fast. CCHs can achieve query times of micro-seconds, exploring orders of magnitude fewer nodes than a standard Dijkstra, demonstrating a 35,000x speed improvement in experiments.

---

## Conclusion
Dijkstra's 20-minute invention, born from a simple need, continues to be the fundamental building block for cutting-edge pathfinding algorithms. Even with dramatic advancements like customizable contraction hierarchies, which provide speeds 35,000 times faster, the core principles of Dijkstra's algorithm remain central. This enduring legacy highlights the power and reliability of elegant, well-thought-out solutions in computer science.