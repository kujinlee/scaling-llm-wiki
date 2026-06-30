---
tags:
  - video-summary
  - ko
  - claude
  - html
  - markdown
  - ai productivity
  - code visualization
  - anthropic playground
  - prompt engineering
video_id: "Mhl1kje4Mjc"
channel: "AI는 야근중"
lang: KO
type: Tutorial
audience: Intermediate
score: 4.4
---

# 마크다운 문서 더미 탈출법 — Claude Code Playground 실전 3가지

**Channel:** AI는 야근중 | **Duration:** 4:27 | **URL:** https://www.youtube.com/watch?v=Mhl1kje4Mjc

> [!summary] Quick Reference
> **TL;DR:** This video shows how to transform unreadable AI-generated markdown into clear, interactive HTML using Claude Code and the Playground plugin for better comprehension.
>
> **Key Takeaways:**
> - Transform long, unreadable AI-generated markdown into structured HTML with simple prompts.
> - Utilize Claude's Playground plugin for interactive code dependency maps and execution flows.
> - Add comments to interactive visualizations, which convert directly into actionable feedback prompts for AI.
> - Strategically use HTML for visual clarity and markdown for basic content to optimize token usage.
> - Prioritize quickly understanding AI outputs over just generating them for true productivity gains.
>
> **Concepts:** claude · html · markdown · ai productivity · code visualization · anthropic playground · prompt engineering

---

## 1. 긴 마크다운 문서의 문제점과 HTML 전환의 필요성
▶ [0:00–0:28](https://www.youtube.com/watch?v=Mhl1kje4Mjc&t=0s)
클로드 코드(Claude Code)로 작업 시 마크다운으로 생성되는 기획 문서, 코드 분석, 리서치 요약 등의 결과물은 내용이 충분하더라도 100줄이 넘어가면 읽기 어렵습니다. 기호와 들여쓰기만 가득하여 앞부분만 대충 보고 넘어가게 되는 경우가 많습니다. 엔스로픽(Anthropic) 엔지니어 역시 이 문제를 인지하고 있으며, HTML이 새로운 마크다운이라며 HTML로 결과물을 받기 시작했다고 합니다.

---

## 2. 기본 HTML 변환을 통한 가독성 향상
▶ [0:28–1:04](https://www.youtube.com/watch?v=Mhl1kje4Mjc&t=28s)
기존의 길고 가독성이 떨어지는 마크다운 리서치 문서를 개선하기 위해 클로드 코드에 `내 리서치 마크다운 파일을 HTML로 변환해 줘. 상단에 탭을 만들어서 채널별로 정리하고 내용은 주제별로 묶어서 카드 레이아웃으로 만들어 줘.`와 같은 프롬프트를 사용하면 이해도가 완전히 달라집니다. 채널별 탭과 주제별 카드 레이아웃을 통해 스크롤 없이 한눈에 내용을 파악할 수 있어 이해 속도가 크게 향상됩니다. 레이아웃, 차트, 표 등을 명확히 지정하면 더욱 맞춤형 결과물을 얻을 수 있습니다.

---

## 3. 동적 시각화를 위한 플레이그라운드 플러그인 활용
▶ [1:04–1:48](https://www.youtube.com/watch?v=Mhl1kje4Mjc&t=64s)
단순히 HTML로 변환하는 것만으로는 동적인 시각화(인터랙션)를 구현하기 어렵습니다. 버튼 클릭, 슬라이더 조작, 토글 변경 등을 통해 결과를 동적으로 확인할 수 있는 화면은 클로드에게 단순히 HTML을 요청해서는 얻기 힘듭니다. 엔스로픽은 이를 위해 '플레이그라운드(Playground)'라는 플러그인을 제공하며, 두 줄의 코드로 쉽게 설치하고 내장 템플릿을 활용하여 다양한 문제 유형에 맞는 결과물을 생성할 수 있습니다.

----- 

## 4. 코드 의존성 맵을 통한 모듈 분석
▶ [1:48–2:57](https://www.youtube.com/watch?v=Mhl1kje4Mjc&t=108s)
플레이그라운드를 활용하여 헤르메스(Hermes) 코드 구조를 시각적으로 보여주는 의존성 맵을 만들 수 있습니다. `헤르메스 구조를 시각적으로 보여주는 플레이그라운드를 만들어 줘. 모듈한 의존성을 노드로 표시하고 내가 각 노드에 코멘트를 달 수 있게 해 줘.`와 같은 프롬프트를 사용하면 모듈 의존성이 노드로 표현되고 색상으로 구분되어 한눈에 파악하기 쉽습니다. 노드를 클릭하여 코멘트를 달면 자동으로 아래 피드백 프롬프트로 변환되어 클로드 코드에 바로 수정 요청으로 연결할 수 있습니다.

---

## 5. 코드 실행 흐름도를 통한 프로세스 이해
▶ [2:57–3:43](https://www.youtube.com/watch?v=Mhl1kje4Mjc&t=177s)
또 다른 플레이그라운드 활용 예시로, 헤르메스 에이전트 코드의 실행 흐름도를 인터랙티브 HTML로 생성할 수 있습니다. `헤르메스 에이전트 코드를 분석해서 인터랙티브 HTML을 만들어 줘. 사용자 질문이 들어와서 답변이 나오기까지 전체 프로세스가 이해될 수 있도록 가시성 있게 보여줘.`와 같은 프롬프트로 8단계 다이어그램을 얻을 수 있습니다. 사용자 질문 프리셋을 선택하면 해당 요청이 처리되는 과정이 강조되며, 각 레이어의 프로세스와 활성화되는 툴을 쉽게 확인할 수 있습니다. 여기서도 자동 생성되는 피드백 프롬프트를 통해 특정 단계에 대한 수정 요청을 클로드에 전달할 수 있습니다.

---

## 6. HTML과 마크다운의 적절한 활용 전략
▶ [3:43–4:07](https://www.youtube.com/watch?v=Mhl1kje4Mjc&t=223s)
HTML 변환 및 플레이그라운드 사용은 토큰을 더 많이 소모합니다. 따라서 완성된 결과물 중 표, 다이어그램, 카드 등으로 보아야 이해가 빠른 내용(시각화가 중요한 경우)에는 HTML을 사용하고, 초안, 메모, 에이전트 데이터처럼 텍스트로도 충분히 이해 가능한 내용에는 마크다운을 사용하여 토큰을 절약하는 전략이 필요합니다.

---

## 결론: AI 결과물 이해 속도 향상과 생산성
▶ [4:07–4:28](https://www.youtube.com/watch?v=Mhl1kje4Mjc&t=247s)
토큰을 더 많이 사용하더라도 HTML 및 플레이그라운드 활용은 충분히 가치 있습니다. AI가 문서를 만드는 속도가 사람이 이해하는 속도를 이미 앞질렀기 때문에, 이 간극을 줄이는 것이 현재 시점에서 진정한 생산성이라고 할 수 있습니다. AI에게 작업을 맡기는 능력보다 AI 결과물을 빠르게 읽고 검증하는 능력이 중요해졌으며, 단순한 `HTML로 만들어 줘.` 한 마디로 시작할 수 있습니다.