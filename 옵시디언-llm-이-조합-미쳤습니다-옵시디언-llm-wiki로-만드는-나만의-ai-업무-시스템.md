---
tags:
  - video-summary
  - ko
  - lm wiki
  - 옵시디언
  - 개인 지식 관리
  - ai 활용
  - 생산성
  - 마크다운
  - 업무 자동화
video_id: "UbxFpDuWt8Q"
channel: "칼퇴연구소┃AI생산성"
lang: KO
type: Framework
audience: Intermediate
score: 4.4
---

# 옵시디언 + LLM 이 조합 미쳤습니다 | 옵시디언 + LLM Wiki로 만드는 나만의 AI 업무 시스템

**Channel:** 칼퇴연구소┃AI생산성 | **Duration:** 8:46 | **URL:** https://www.youtube.com/watch?v=UbxFpDuWt8Q

> [!summary] Quick Reference
> **TL;DR:** This video explains how to build a personal AI-powered knowledge management system using Obsidian and LLMs based on Andrej Karpathy's LM Wiki concept.
>
> **Key Takeaways:**
> - AI revolutionizes knowledge management by structuring, summarizing, and connecting information stored in AI-friendly formats.
> - Use Obsidian's Markdown-based system to create an AI-friendly knowledge workspace for efficient LLM interaction.
> - Implement Andrej Karpathy's LM Wiki by having AI manage and update topic-specific wikis from your source materials.
> - Set up your Obsidian vault with `Source`, `Wiki`, `Agent`, and `Output` folders for an effective LM Wiki.
> - Delegate repetitive information processing to AI, allowing you to focus on strategic thinking and crucial decision-making.
>
> **Concepts:** lm wiki · 옵시디언 · 개인 지식 관리 · ai 활용 · 생산성 · 마크다운 · 업무 자동화

---

## 1. 기존 지식 관리의 한계와 AI의 등장

과거 사람들은 '두 번째 뇌'를 구축하여 업무 자료, 프로젝트 기록, 의사 결정 과정 등의 중요한 인사이트를 한곳에 모으고 싶어 했습니다. 하지만 대부분의 노트 앱은 자료 입력, 검색, 유지 관리의 높은 비용으로 인해 결국 '지식 무덤'이 되고 말았습니다. AI의 등장은 이러한 구조를 변화시키고 있습니다. 이제 AI는 자료를 직접 정리하지 않아도 요약, 분류, 연결, 변환하는 역할을 수행하며 지식 관리의 효율성을 혁신하고 있습니다. 단, AI가 잘 이해할 수 있는 형식으로 지식이 저장되어야 한다는 중요한 전제가 있습니다.

---

## 2. 옵시디언(Obsidian)을 활용한 AI 친화적 지식 관리

AI가 지식을 효과적으로 활용하기 위한 핵심은 바로 마크다운(Markdown) 형식입니다. 마크다운은 사람과 AI 모두가 읽고 이해하기 쉬운 구조화된 텍스트 형식입니다. 기존의 예쁜 노트 앱들이 내부 구조가 앱 자체에 강하게 의존하는 반면, 옵시디언은 폴더와 텍스트 파일 기반의 구조를 가지고 있습니다. 이는 AI 에이전트나 LLM이 폴더를 읽고, 파일을 수정하며, 새 문서를 생성하고 기존 문서와 연결하는 작업을 훨씬 용이하게 만듭니다. 옵시디언은 단순히 자료를 저장하는 공간이 아닌, 사람과 AI가 함께 작업할 수 있는 지식 작업장으로서 강력한 이점을 제공합니다.

---

## 3. 안드레 카파시의 LM 위키(LM Wiki) 개념 소개

오픈AI 멤버이자 테슬라의 AI 총괄이었던 안드레 카파시가 소개한 'LM 위키(LM Wiki)'는 AI가 관리하는 개인 업무 위키 시스템입니다. 이 시스템은 모든 자료를 한 폴더에 모아두고, AI에게 이 자료들을 읽어 주제별 위키 문서로 정리해 달라고 요청하는 방식으로 작동합니다. 새로운 자료가 추가될 때마다 AI가 기존 위키와 연결하여 요약하고 관련 문서를 자동으로 업데이트하도록 하여, 사용자가 매번 AI에게 업무 맥락을 설명할 필요 없이 일관된 지식 기반을 유지할 수 있게 합니다.

---

## 4. LM 위키 구축을 위한 실질적인 단계

LM 위키를 구현하기 위해서는 옵시디언, 옵시디언 플러그인, 그리고 ChatGPT와 같은 LLM이 필요합니다. 구축 절차는 다음과 같습니다:
1.  **옵시디언 볼트 생성**: 새로운 옵시디언 볼트를 만듭니다.
2.  **핵심 폴더 구조**: `소스(Source)`, `위키(Wiki)`, `에이전트(Agent)`, `아웃풋(Output)` 네 가지 폴더를 생성합니다. `소스`에는 원본 자료를, `위키`에는 AI가 정리한 결과물을, `에이전트` 파일에는 AI의 작업 규칙을, `아웃풋`에는 최종 결과물을 저장합니다. `소스` 폴더의 원본 자료는 절대 수정하지 않는 것이 중요합니다.
3.  **자료 투입**: 원본 자료를 `소스` 폴더에 넣습니다. 처음에는 소량의 자료로 시작할 수 있습니다.
4.  **AI 지식 정리 요청**: AI에게 `소스` 폴더의 자료를 읽고 `위키` 폴더에 주제별 문서를 생성해달라고 요청합니다.
5.  **지속적인 업데이트 요청**: 새 자료가 생길 때마다 AI에게 이를 `위키` 문서에 업데이트하고 새로운 개념을 연결하도록 요청합니다.
6.  **결과물 생성 요청**: 필요할 때 `위키` 내용을 바탕으로 요약본이나 보고서 초안 등 특정 결과물을 `아웃풋` 폴더에 생성하도록 요청합니다.

---

## 5. 실제 업무에 LM 위키 적용하기

예를 들어 신규 프로젝트 기획 업무에 LM 위키를 적용할 수 있습니다. 회의록, 리서치 자료, 시장 조사 자료 등을 `소스` 폴더에 넣고 AI에게 이를 바탕으로 프로젝트 개요, 문제 정의, 경쟁사 비교, 핵심 의사 결정, 리스크 요인 등의 `위키` 문서를 생성하도록 지시합니다. 이후에는 AI에게 이 `위키` 내용을 참조하여 한 페이지 기획안 초안이나 경쟁사 차별화 포인트 등을 요청할 수 있습니다. 이 과정에서 사람은 방향 설정, AI 결과 검토, 중요한 판단에 집중하고, AI는 반복적인 정보 정리와 연결을 담당하여 업무 효율을 극대화할 수 있습니다.

---

## Conclusion

안드레 카파시의 LM 위키는 AI가 개인의 지식을 관리하고 지속적으로 업데이트하는 강력한 시스템입니다. 이 시스템을 통해 사용자는 AI에게 매번 업무 맥락을 설명하는 수고를 덜고, 옵시디언에 저장된 자료들이 단순한 기록을 넘어 실제 업무 결과물을 만드는 핵심 재료가 되도록 할 수 있습니다. 앞으로 AI를 잘 활용하는 사람은 단순히 질문을 잘하는 것을 넘어, AI가 참고할 수 있는 자신만의 지식 시스템을 갖춘 사람이 될 것입니다. 따라서 옵시디언을 단순한 메모 앱을 넘어 LM 위키의 기반으로 활용해보는 것을 강력히 추천합니다.