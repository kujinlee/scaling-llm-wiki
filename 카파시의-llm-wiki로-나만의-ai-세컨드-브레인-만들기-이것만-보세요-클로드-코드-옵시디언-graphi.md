---
tags:
  - video-summary
  - ko
  - ai knowledge management
  - obsidian
  - claude code
  - lm wiki
  - graphipy
  - second brain
  - knowledge graph
  - personal knowledge management
video_id: "cNlvrU-KcRg"
channel: "브레인 트리니티 (Brain Trinity)"
lang: KO
type: Tutorial
audience: Intermediate
score: 4.4
---

# 카파시의 LLM Wiki로 나만의 AI 세컨드 브레인 만들기, 이것만 보세요— 클로드 코드 × 옵시디언 × Graphify

**Channel:** 브레인 트리니티 (Brain Trinity) | **Duration:** 52:33 | **URL:** https://www.youtube.com/watch?v=cNlvrU-KcRg

> [!summary] Quick Reference
> **TL;DR:** This video explains how to build an AI second brain using Claude Code, Obsidian, LM Wiki, and Graphipy, focusing on purposeful knowledge collection.
>
> **Key Takeaways:**
> - Use Obsidian as your AI's knowledge base for efficient, structured learning.
> - Adopt LM Wiki for systematic knowledge collection, leveraging simple markdown files.
> - Establish an Obsidian vault with `raw`, `wiki`, `output` folders for structured knowledge.
> - Utilize Claude Code's `/ingest` skill to process raw data into organized wiki entries.
> - Integrate Graphipy to create knowledge graphs, enhancing AI's understanding and queries.
>
> **Concepts:** ai knowledge management · obsidian · claude code · lm wiki · graphipy · second brain · knowledge graph · personal knowledge management

---

## 1. AI 활용의 한계와 옵시디언 기반 지식 관리의 중요성
기존 AI 에이전트(`agent.md`, `claude.md`) 활용 방식은 대화에만 국한되거나 재활용 가능한 지식 축적에 한계가 있었습니다. 이러한 문제를 해결하기 위해 옵시디언을 AI 활용의 지식 베이스로 사용하는 방안이 주목받고 있습니다. 옵시디언은 순정 마크다운을 지원하여 AI 툴이 문서를 잘 이해하고 소화할 수 있도록 돕습니다. 안드레 카파시(Andrej Karpathy)는 옵시디언을 '지식 입력을 위한 인간의 프론트엔드'라고 언급하며 그 중요성을 강조했습니다. 가장 중요한 것은 '목적 있는 수집'입니다. 단순한 정보 수집을 넘어, 개인의 가치와 목적에 부합하는 '골드 데이터'를 쌓아야 AI가 이를 효과적으로 활용하여 고품질의 산출물을 만들어낼 수 있습니다.

---

## 2. LM 위키(LM Wiki) 개념과 RAG와의 차이
안드레 카파시가 제안한 LM 위키는 LLM 기반 에이전트(예: 클로드 코드)를 활용하여 지식을 체계적으로 수집하고 연결하며 소화하는 프레임워크입니다. 이는 인터넷에서 수집한 로(raw) 데이터를 에이전트가 처리하여 연관성을 파악하고, 간극을 채워 재활용 가능한 위키 형태로 정리하는 과정을 포함합니다. LM 위키는 기존의 검색 증강 생성(RAG, Retrieval Augmented Generation)과 비교되는데, RAG가 복잡한 세팅과 인베딩 모델이 필요한 반면, LM 위키는 마크다운 파일만으로 작동하며 인프라 구축이 필요 없습니다. 또한, LM 위키는 지식 축적이 복리 형태로 이루어져, 쌓일수록 지식 간 연결성이 강화되고 AI 활용도가 높아지는 장점이 있습니다.

---

## 3. LM 위키 시스템 구축 가이드: 옵시디언 & 클로드 코드
LM 위키 시스템 구축은 먼저 새로운 옵시디언 볼트를 생성하는 것부터 시작합니다. 그 다음, 개인의 목표와 가치를 담은 '나의 핵심 맥락' 노트를 작성하고, 클로드 코드와의 인터뷰를 통해 이를 심층적으로 이해하도록 돕습니다. 이 과정을 통해 AI가 지식 관리의 목적과 기준을 명확히 인지하게 됩니다. 이렇게 정립된 '핵심 맥락'을 바탕으로 클로드 코드에게 `claude.md` 파일을 생성하도록 요청하여 AI 에이전트의 운영 규칙과 스키마를 설정합니다. 최종적으로 LM 위키 패턴에 맞춰 `raw` (수집된 자료), `wiki` (정리된 지식), `output` (최종 산출물) 폴더 구조를 생성하여 체계적인 지식 관리 환경을 마련합니다.

---

## 4. 효율적인 자료 수집 및 위키 정리 워크플로우
자료 수집을 위해 옵시디언 웹 클리퍼(Web Clipper)를 활용하여 웹상의 다양한 정보를 마크다운 형식으로 옵시디언에 가져옵니다. 이때, LM 위키 스키마에 맞는 맞춤형 웹 클리퍼 템플릿을 생성하여 'raw' 폴더에 효율적으로 저장합니다. 이후 클로드 코드의 `/ingest` 스킬을 사용하여 'raw' 폴더의 자료를 위키로 반영합니다. 이 과정에서 AI는 자료를 읽고 요약하며, 주요 엔티티를 분리하고, 사용자에게 해당 자료를 수집한 '나의 관점'과 '목적'을 질문하여 목적 있는 수집이 이루어지도록 유도합니다. 이 외에도 `/query` 스킬로 위키 내 지식을 바탕으로 질문에 답변하고, `/lint` 스킬로 위키의 내용 일관성을 유지하고 업데이트를 관리할 수 있습니다.

---

## 5. 지식 그래프 강화를 위한 Graphipy 활용
LM 위키가 지식 축적의 효율성을 높이지만, 지식의 양이 방대해질 경우 비효율이 발생할 수 있습니다. 이를 보완하기 위해 '그래피파이(Graphipy)' 도구가 도입되었습니다. 그래피파이는 옵시디언의 마크다운 문서와 연결 정보를 분석하여 지식 그래프(Knowledge Graph)를 생성합니다. 이렇게 생성된 그래프 정보(`graph.json`, `graph.html`)는 클로드 코드가 지식 간의 복잡한 관계를 이해하고 그래프 기반으로 질의에 답변할 수 있도록 돕습니다. 이는 단순 키워드 검색을 넘어 지식의 의미론적 연결을 활용하는 '그래프 RAG'와 유사한 형태로 발전하여, AI 지식 관리 시스템의 탐색 및 추론 능력을 한 단계 끌어올립니다.

---

## Conclusion
이번 영상에서는 클로드 코드, 옵시디언, LM 위키, 그리고 그래피파이 조합을 통해 AI 기반의 개인 지식 관리 시스템을 구축하는 방법을 심층적으로 다루었습니다. 이 모든 과정에서 가장 핵심적인 원칙은 바로 '나의 목적이 있는 수집'입니다. 단순히 정보를 모으는 것을 넘어, 내가 왜 이 지식을 수집하는지, 어떤 가치를 찾고자 하는지 명확한 의도를 가지고 접근해야만 AI가 진정으로 유의미한 '세컨드 브레인' 역할을 수행할 수 있습니다. 앞으로 이 조합은 개인 지식 관리의 새로운 메타로 떠오를 것이며, 꾸준한 고민과 적용을 통해 지식의 가치를 극대화할 수 있을 것입니다.