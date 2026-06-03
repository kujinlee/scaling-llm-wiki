---
tags:
  - video-summary
  - ko
  - ai design
  - design tokens
  - design.md
  - prompt engineering
  - frontend development
  - design system
  - consistency
video_id: "w33YxZ7auZs"
channel: "메이커 에반 | Maker Evan"
lang: KO
type: Tutorial
audience: Intermediate
score: 4.2
---

# 구글이 사양 공개한 design.md 정체

**Channel:** 메이커 에반 | Maker Evan | **Duration:** 13:17 | **URL:** https://www.youtube.com/watch?v=w33YxZ7auZs

> [!summary] Quick Reference
> **TL;DR:** This video introduces `design.md`, a new Google-backed open-source file that standardizes design rules for AI, improving consistency and collaboration.
>
> **Key Takeaways:**
> - Use `design.md` to standardize design rules for AI, ensuring consistent outputs like colors and fonts.
> - `design.md` bridges designers, developers, and AI by using quantitative, W3C-standard design tokens.
> - Add `@design.md` to your AI tool's config file for automatic rule application and reduced prompts.
> - First, establish your design system using AI, then document key elements in `design.md`.
> - Prioritize filling core elements (colors, fonts) in `design.md`, adding others as needed.
>
> **Concepts:** ai design · design tokens · design.md · prompt engineering · frontend development · design system · consistency

---

## 1. AI 디자인 일관성 문제 해결: design.md의 등장
AI를 활용하여 디자인 작업을 할 때 매번 색상, 폰트, 간격 등이 다르게 나오는 문제에 대해 설명합니다. 이는 우리가 AI에게 모호하거나 반복적인 지시를 주기 때문이며, 마치 도면 없이 인테리어를 맡기는 것과 같다고 비유합니다. 이러한 비효율성을 해결하기 위해 '디자인 시방서'와 같은 역할을 하는 `design.md` 파일이 등장했습니다.

---

## 2. design.md 파일의 구조와 작동 원리
`design.md`는 Google Labs의 'Stitch' 프로젝트에서 시작되어 오픈 소스로 공개된 파일입니다. 프로젝트 폴더 내 `README.md` 파일 옆에 위치하며, 디자인 규칙의 새로운 표준으로 자리 잡고 있습니다. 이 파일은 색상, 타이포그래피, 간격, 모서리, 그림자 등 8가지 카테고리로 구성되어 있으며, 컴퓨터가 읽을 수 있는 정량적인 값(예: 컬러 코드)과 사람이 이해할 수 있는 설명(예: "이 보라색은 강조 버튼에 사용")이 함께 담겨 있습니다.

---

## 3. design.md가 게임 체인저인 핵심 이유: 자동 적용 및 표준화
`design.md`의 가장 큰 장점은 AI가 이를 자동으로 읽고 디자인 규칙을 적용한다는 것입니다. 사용하는 AI 도구의 설정 파일(예: `claude.md`)에 `@design.md` 한 줄만 추가하면, AI는 더 이상 디자인에 대한 구체적인 프롬프트 없이도 일관된 결과물을 생성합니다. 이로 인해 프롬프트 길이가 획기적으로 줄어들고 토큰 비용이 절약됩니다.

더 나아가 `design.md`는 W3C의 디자인 토큰 표준(DTCG)을 따르고 있어 강력한 표준화 효과를 제공합니다. 이는 디자인 정의로부터 코드를 자동으로 변환하거나, 디자인 툴(예: Figma)에서 디자인 시스템을 `design.md` 파일로 직접 내보낼 수 있게 하여 디자이너-개발자-AI 간의 커뮤니케이션 비용과 오차를 획기적으로 줄여줍니다. 마치 도량형 표준처럼 디자인 세계의 공통 언어가 되는 것입니다.

---

## 4. 고려해야 할 단점 및 적합한 프로젝트
`design.md`는 아직 알파 단계에 있어 사양 변경 가능성이 높고, 다크 모드나 애니메이션, 반응형 디자인 규칙 등은 공식적으로 지원하지 않는 단점이 있습니다. 또한, 코드와의 자동 동기화 기능이 없어 코드가 수정될 경우 `design.md` 파일도 수동으로 업데이트해야 합니다. 소규모 개인 프로젝트의 경우 관리 자체가 오버스펙이 될 수도 있습니다.

하지만 디자이너와 개발자가 협업하는 SaaS 제품, AI 에이전트로 프론트엔드를 반복 생성하는 환경, 브랜드 일관성이 매우 중요한 회사 프로젝트 등에서는 그 효과가 극대화됩니다.

---

## 5. design.md 실전 적용 3단계
1.  **디자인 시안 먼저 뽑기:** `design.md`를 작성하기 전에 AI 도구를 활용하여 다양한 컬러, 폰트 조합의 시안을 여러 개 생성하고, 그중 마음에 드는 것을 선택하여 프로젝트의 디자인 시스템을 먼저 확정합니다. 이 단계가 가장 중요하며, 절대 건너뛰지 말아야 합니다.
2.  **공식 사양 참고하여 핵심만 채우기:** `design.md`의 공식 가이드를 참고하여 카테고리별 내용을 채웁니다. 이때 모든 8가지 카테고리를 한 번에 채우려 하지 말고, 가장 자주 사용하는 메인 색상 5개와 폰트 2~3개 등 핵심적인 요소부터 시작하는 것이 좋습니다. 나머지는 프로젝트를 진행하며 필요할 때 추가합니다.
3.  **AI 설정 파일에 한 줄 추가:** 사용하는 AI 도구의 설정 파일(예: 클로드 코드의 `claude.md` 또는 코덱스의 `agent.md`)에 `@design.md`라는 문구를 한 줄 추가합니다. 이 한 줄로 AI는 `design.md`의 규칙을 자동으로 따르게 됩니다.

---

## Conclusion
`design.md`는 AI 코딩 시대에 디자인 일관성을 확보하고 디자이너-개발자 간의 협업 효율을 극대화하는 새로운 표준 파일로 자리매김할 가능성이 큽니다. 구글의 지원과 W3C 표준 채택을 바탕으로, 디자인 일관성이 중요한 프로젝트에서는 시도해볼 가치가 충분합니다. 단 한 번의 설정으로 AI 디자인 작업의 패러다임을 바꿀 수 있는 강력한 도구입니다.