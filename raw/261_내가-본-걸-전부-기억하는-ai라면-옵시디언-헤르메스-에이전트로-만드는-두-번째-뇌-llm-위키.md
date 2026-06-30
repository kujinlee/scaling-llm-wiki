---
tags:
  - video-summary
  - ko
video_id: "XT-_Mz18irE"
channel: "Aiden의 친절한 AI"
lang: KO
type: Tutorial
score: 4.6
---

# 내가 본 걸 전부 기억하는 AI라면? | 옵시디언 + 헤르메스 에이전트로 만드는 두 번째 뇌 [LLM 위키]

**Channel:** Aiden의 친절한 AI | **Duration:** 16:38 | **URL:** https://www.youtube.com/watch?v=XT-_Mz18irE

> [!summary] Quick Reference
> **TL;DR:** This video demonstrates building a personalized LLM Wiki using Obsidian and Hermes Agent to create an AI-powered "second brain" for knowledge management.
>
> **Key Takeaways:**
> - LLM Wiki autonomously organizes knowledge, creating and updating connected notes from raw input.
> - The system comprises three layers: original data, AI-managed wiki notes, and a guiding schema.
> - Set up your LLM Wiki by configuring Obsidian and Hermes Agent, letting AI build the initial structure.
> - Integrate personal perspectives by prompting the AI to ask questions after summarizing new content.
> - Maintain your AI wiki with periodic "Lint" checks to ensure accuracy and resolve knowledge inconsistencies.

---

## 1. LLM 위키: 나만의 두 번째 뇌
▶ [0:00–1:07](https://www.youtube.com/watch?v=XT-_Mz18irE&t=0s)
AI가 나만의 지식과 정보를 기억하고 활용하여 "두 번째 뇌"처럼 작동하는 시스템의 필요성을 제시합니다. 최근 안드레이 카파시가 제안한 LLM 위키 개념을 소개하며, 이를 통해 자료를 단순 보관하는 것을 넘어 AI가 능동적으로 정리하고 질문에 답하는 지식 공간을 구축할 수 있음을 설명합니다.

---

## 2. 기존 AI 활용 방식의 한계와 LLM 위키의 차이점
▶ [1:07–2:35](https://www.youtube.com/watch?v=XT-_Mz18irE&t=67s)
기존 AI 자료 활용 방식은 자료를 업로드하고 질문할 때마다 처음부터 다시 내용을 찾아 답하는 비효율성이 있습니다. 이로 인해 자료가 쌓여도 정리된 지식은 남지 않습니다. LLM 위키는 자료 입력 시 AI가 핵심을 뽑아 미리 정리된 노트로 만들고, 새 자료가 들어오면 기존 노트를 업데이트하며 관련 내용을 연결하고 불일치를 표시하는 방식으로 지식을 지속적으로 다듬어 나갑니다.

---

## 3. LLM 위키의 세 가지 핵심 층과 관리 파일
▶ [2:35–4:39](https://www.youtube.com/watch?v=XT-_Mz18irE&t=155s)
LLM 위키는 크게 '원본 자료층', '위키층', '스키마층'의 세 가지 층으로 구성됩니다. 원본 자료층은 사용자의 원본 데이터를 AI가 읽기만 하는 곳이고, 위키층은 AI가 원본을 바탕으로 생성하고 관리하는 정리된 노트들로 이루어집니다. 스키마층은 AI에게 위키 구조, 규칙, 처리 절차를 알려주는 운영 매뉴얼입니다. 또한, 위키 전체의 목차 역할을 하는 '인덱스 파일'과 작업 기록을 남기는 '로그 파일'이 길잡이 역할을 합니다.

---

## 4. 옵시디언과 헤르메스 에이전트로 LLM 위키 구축하기
▶ [4:39–11:00](https://www.youtube.com/watch?v=XT-_Mz18irE&t=279s)
옵시디언과 헤르메스 에이전트를 사용하여 LLM 위키를 실제로 구축하는 과정을 안내합니다. 먼저 두 도구를 설치하고, 헤르메스 에이전트의 모델 프로바이더(예: 오픈 라우터)를 선택한 후 옵시디언 볼트를 워킹 디렉토리로 설정합니다. 특정 프롬프트로 AI에게 위키의 뼈대(폴더 구조, 인덱스, 에이전트.md 파일 등)를 만들도록 요청하고 옵시디언에서 이를 확인합니다.

---

## 5. 나만의 관점을 더한 자료 수집 및 질문 전략
▶ [11:00–15:10](https://www.youtube.com/watch?v=XT-_Mz18irE&t=660s)
옵시디언 웹 클리퍼를 통해 웹 자료를 LLM 위키의 '로우 아티클' 폴더에 마크다운 형태로 저장하는 방법을 설명합니다. 단순히 자료를 모으는 것을 넘어, `agent.md` 파일에 프롬프트를 추가하여 AI가 자료 요약 후 사용자에게 질문을 던지게 함으로써 개인의 관점을 지식에 통합하는 방법을 제시합니다. 또한, LLM 위키의 활용도를 높이는 '좋은 질문'의 세 가지 원칙(단순 검색 질문 지양, 범위와 형태 구체화, 연결 및 비교 질문)을 소개하고 실제 질문 사례를 보여줍니다.

---

## 6. LLM 위키의 지속적인 성장과 관리
▶ [15:10–15:42](https://www.youtube.com/watch?v=XT-_Mz18irE&t=910s)
LLM 위키는 한 번 구축으로 끝나는 것이 아니라, 자료 수집, AI 정리, 관점 추가, 질문을 통한 산출물 생성의 순환 과정입니다. 시간이 지나면서 생기는 오래된 정보나 불일치를 해결하기 위해 주기적으로 '린트(Lint)', 즉 위키 건강 검진을 통해 점검하고 유지 관리해야 함을 강조합니다. 이 과정을 통해 위키는 점점 더 똑똑해지는 "두 번째 뇌"로 성장합니다.

---

## Conclusion
▶ [15:42–16:38](https://www.youtube.com/watch?v=XT-_Mz18irE&t=942s)
이 영상은 옵시디언과 헤르메스 에이전트를 활용하여 개인화된 LLM 위키를 처음부터 구축하고 운영하는 전체 과정을 다루었습니다. LLM 위키의 핵심 개념은 특정 도구에 묶이지 않으며, 파일을 읽고 쓰는 규칙을 따를 수 있는 어떤 에이전트라도 구현 가능하다고 결론지으며, 사용자에게 가장 익숙한 도구를 선택하여 시작할 것을 권장합니다.