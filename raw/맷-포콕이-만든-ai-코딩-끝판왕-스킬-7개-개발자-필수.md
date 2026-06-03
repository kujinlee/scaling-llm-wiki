---
tags:
  - video-summary
  - ko
  - ai agent
  - mapper's skills
  - software development
  - tdd
  - code quality
  - software architecture
  - grillme
video_id: "nyAHYmDaGBk"
channel: "메이커 에반 | Maker Evan"
lang: KO
type: Framework
audience: Intermediate
score: 4.4
---

# 맷 포콕이 만든 AI 코딩 끝판왕 스킬 7개 (개발자 필수)

**Channel:** 메이커 에반 | Maker Evan | **Duration:** 7:18 | **URL:** https://www.youtube.com/watch?v=nyAHYmDaGBk

> [!summary] Quick Reference
> **TL;DR:** This video details Mapper's Skills, a framework to improve AI agent collaboration, tackling issues like poor code quality, requirement mismatch, and decaying architecture effectively.
>
> **Key Takeaways:**
> - GrillMe uses AI to ask persistent questions, clarifying design concepts and generating precise PRDs.
> - Apply TDD by having AI write tests first to catch errors early, improving feedback loops and code quality.
> - Instruct AI to use a structured 'Diagnose' process for debugging, avoiding guesswork to solve problems efficiently.
> - Have AI regularly suggest codebase architecture improvements to prevent decay and maintain high quality.
> - Design interfaces yourself and delegate implementation details to AI for better direction and quality control.
>
> **Concepts:** ai agent · mapper's skills · software development · tdd · code quality · software architecture · grillme

---

## 1. AI 에이전트 작업 시 직면하는 문제들
AI 에이전트와 협업할 때 빈번히 발생하는 네 가지 주요 문제가 있습니다. 첫째, **요구 사항과 구현의 불일치**로, AI가 지시와 다른 결과를 도출하는 경우가 잦습니다. 둘째, 프로젝트의 특정 맥락(색상, 폰트 등)을 **반복적으로 설명**해야 하여 시간과 토큰이 낭비됩니다. 셋째, AI가 생성한 **코드 품질**이 낮아 누더기처럼 되어 유지보수가 어렵습니다. 넷째, 초기에는 깔끔했던 아키텍처가 기능 추가에 따라 **점점 망가져** 손대기 어려운 코드가 됩니다. 매퍼의 스킬은 이러한 문제들을 해결하기 위해 고안된 체계적인 접근 방식입니다.

---

## 2. 매퍼의 핵심 스킬 1: 그릴미 & PRD 자동 생성
첫 번째 핵심 스킬은 **그릴미(GrillMe)**입니다. 이는 AI에게 단순히 문서를 던지는 것이 아니라, AI가 사용자에게 집요하게 질문하도록 유도하여 명확한 디자인 콘셉트에 도달하는 방식입니다. AI는 사용자의 머릿속 그림, 문서, 그리고 AI의 이해 사이의 간극을 줄이기 위해 끊임없이 질문을 던지고, 사용자는 이에 답하며 미처 생각하지 못했던 부분까지 구체화합니다. 이 과정은 사람이 반드시 참여해야 하는 '페어 프로그래밍'의 진화된 형태로 볼 수 있습니다. 그릴미를 통해 합의된 내용은 AI가 **PRD(제품 요구 사항 문서)**로 자동 요약 및 정리해 줍니다. AI의 요약 능력을 신뢰하여 PRD 검토에 시간을 낭비하기보다는 다음 단계로 빠르게 넘어가는 것이 중요합니다.

---

## 3. 매퍼의 핵심 스킬 2: TDD (테스트 주도 개발) 활용
AI에게 기능 구현과 테스트 작성을 동시에 지시하면, AI는 구현을 마친 후 이에 맞춰 테스트를 생성하여 테스트의 본래 목적을 훼손할 수 있습니다. 이를 해결하는 두 번째 핵심 스킬은 **TDD(테스트 주도 개발)**를 AI 작업에 적용하는 것입니다. 즉, 구현 전에 테스트를 먼저 작성하도록 지시하여 AI가 잘못된 구현을 하더라도 즉시 발견하고 수정할 수 있는 환경을 만듭니다. 이는 코드베이스의 **피드백 루프** 품질과 직결됩니다. 빠르고 정확한 테스트, 철저한 타입 체크 등으로 구성된 좋은 피드백 루프는 AI가 스스로 실수를 발견하고 개선하는 데 필수적입니다. AI의 출력 품질이 낮다면 AI 탓을 하기 전에 코드베이스의 피드백 루프부터 점검해야 합니다.

---

## 4. 매퍼의 핵심 스킬 3 & 4: 디아그노즈 & 코드베이스 아키텍처 개선
세 번째 스킬은 문제를 진단할 때 사용하는 **디아그노즈(Diagnose)**입니다. AI에게 "이거 왜 안 돼?"라고 물었을 때 단순 추측으로 시간을 낭비하는 대신, 에러 재현 -> 가설 수립 -> 가설 검증의 정해진 절차를 따르도록 지시합니다. 이는 의사가 환자를 진료하는 것과 유사하게 체계적인 접근을 통해 헛고생을 줄여줍니다. 네 번째 스킬은 **코드베이스 아키텍처 개선(Improve Codebase Architecture)**입니다. 나쁜 코드베이스는 결국 나쁜 AI 에이전트를 만듭니다. AI에게 정기적으로 코드베이스의 개선이 필요한 부분(통합, 모듈화 등)을 파악하고 제안하도록 하여, 지속적으로 건강한 코드베이스 환경을 유지하도록 돕습니다.

---

## 5. 효과를 높이는 추가 팁과 전체 워크플로우
매퍼의 스킬 효과를 극대화하기 위한 두 가지 추가 팁이 있습니다. 첫째, **인터페이스는 직접 설계하고 구현은 AI에게 위임**하는 것입니다. 마치 집을 지을 때 도면은 직접 그리고 벽돌 쌓기는 인부에게 맡기듯, 큰 그림은 사람이 그리고 세부 구현은 AI에게 맡겨 전반적인 방향성을 유지합니다. 둘째, **리뷰는 새 컨텍스트에서 진행**하는 것입니다. 구현 작업으로 토큰을 많이 사용하여 지쳐있는 같은 세션에서 바로 리뷰하지 말고, 리뷰 전용의 새로운 AI 컨텍스트를 띄워 코드를 던져 더 객관적이고 정확한 검토를 받도록 합니다. 이 모든 스킬은 그릴미 -> PRD 자동 생성 -> TDD -> (필요시) 디아그노즈 -> (정기적) 코드베이스 아키텍처 개선의 순서로 유기적인 워크플로우를 형성합니다.

---

## Conclusion
매퍼의 스킬은 AI 에이전트와의 비효율적인 협업 방식에서 벗어나, 요구 사항 불일치, 반복 설명, 낮은 코드 품질, 아키텍처 망가짐 등 네 가지 고질적인 문제들을 해결하기 위한 강력한 도구 모음입니다. 그릴미를 통한 명확한 디자인 컨셉 도출, TDD를 활용한 견고한 구현, 디아그노즈를 통한 효율적인 문제 해결, 그리고 코드베이스 아키텍처 개선을 통한 지속적인 품질 유지 등 다섯 가지 핵심 스킬과 추가적인 팁들을 통해 AI 개발 생산성과 결과물의 품질을 혁신적으로 향상시킬 수 있습니다. 특히 도메인 매핑을 통해 AI가 프로젝트의 맥락을 정확히 이해하도록 돕는 것이 중요하며, 이를 통해 DDI 기반 아키텍처링과 같은 복잡한 작업에도 AI를 효과적으로 활용할 수 있습니다.