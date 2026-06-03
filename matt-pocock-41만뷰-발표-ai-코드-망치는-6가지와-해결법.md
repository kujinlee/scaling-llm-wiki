---
tags:
  - video-summary
  - ko
  - ai engineering
  - software fundamentals
  - code quality
  - llm development
  - grill me
  - deep modules
  - tdd
video_id: "FOee3zb98wI"
channel: "AgentOS"
lang: KO
type: Framework
audience: Intermediate
score: 4.4
---

# Matt Pocock 41만뷰 발표 — AI 코드 망치는 6가지와 해결법

**Channel:** AgentOS | **Duration:** 12:23 | **URL:** https://www.youtube.com/watch?v=FOee3zb98wI

> [!summary] Quick Reference
> **TL;DR:** This video identifies six pitfalls of AI-generated code and offers solutions, stressing the enduring importance of strong software fundamentals for developers.
>
> **Key Takeaways:**
> - Bad AI-generated code is expensive; AI thrives on well-structured, maintainable codebases.
> - Actively 'Grill' AI with questions to build a shared understanding of design concepts.
> - Implement TDD (Test-Driven Development) to ensure AI produces working code iteratively and safely.
> - Guide AI to build 'Deep Modules' with simple interfaces, avoiding complex 'Shallow Module' structures.
> - Employ a 'Gray Box' strategy: design interfaces yourself, then delegate internal implementation to AI.
>
> **Concepts:** ai engineering · software fundamentals · code quality · llm development · grill me · deep modules · tdd

---

## 1. AI 시대, '코드는 결코 싸지 않다'
AI 업계의 'Specs-to-Code' 운동에 반기를 들며, 타입스크립트 전문가 포콕(Pocock)은 "코드는 싸지 않다. 오히려 나쁜 코드는 그 어느 때보다 비싸다"고 주장합니다. AI가 빛을 발하는 것은 좋은 코드 베이스 위에서이며, 변경하기 어려운 코드에 AI를 적용하면 오히려 시스템이 망가진다는 소프트웨어 엔트로피 개념을 강조합니다. 결국 AI 시대일수록 소프트웨어 펀더멘털이 더욱 중요해진다는 핵심 명제를 제시합니다.

---

## 2. AI와의 '공유된 이해' 구축: 'Grill Me'와 '유비쿼터스 언어'
- **함정 1: 의도와 다른 AI 결과물.** AI는 사용자 머릿속의 디자인 컨셉을 공유하지 못해 의도와 다른 코드를 만듭니다. **처방: 'Grill Me' 스킬.** AI가 사용자에게 끊임없이 질문하여 상호 이해에 도달할 때까지 심문하게 합니다. 이 스킬은 깃허브에서 큰 호응을 얻었습니다.
- **함정 2: AI의 장황함과 언어 불일치.** AI는 같은 의미를 다른 단어로 반복하여 말하며, 사람과 AI 사이에 '유비쿼터스 언어'가 부재합니다. **처방: 유비쿼터스 랭귀지.** 코드 베이스에서 공통 용어를 추출해 사람과 AI가 함께 사용하는 마크다운 사전을 만듭니다. 이를 통해 AI의 사고방식이 간결해지고 같은 결과를 도출할 수 있습니다.

---

## 3. 실행 가능한 코드 생산: 'TDD'와 'Deep Module' 아키텍처
- **함정 3: 의도대로 만들었으나 작동하지 않는 코드.** AI는 코드를 그럴듯하게 짜지만 실행 시 에러가 발생하는 경우가 많습니다. LLM은 피드백 루프를 잘 활용하지 못해 "헤드라이트보다 빨리 달리는" 위험에 처합니다. **처방: TDD(테스트 주도 개발).** 테스트를 먼저 작성하게 하여 AI가 작은 단위로 움직이도록 강제하고, 피드백 속도를 조절하게 합니다.
- **함정 4: AI가 만든 미로, 'Shallow Module'.** AI는 작은 모듈을 잔뜩 만들고 인터페이스가 복잡한 'Shallow Module' 구조를 선호하며, 정작 자신이 만든 미로에서 길을 잃습니다. 이로 인해 코드 이해 및 수정이 어렵습니다. **처방: 'Improve Codebase Architecture' 스킬.** 관련된 코드들을 묶어 단순한 인터페이스 뒤에 깊은 기능을 숨긴 'Deep Module'로 변환하는 반복 가능한 단계들을 제시합니다.

---

## 4. 코드량 폭증 시대의 생존 전략: '그레이 박스' 모델
- **함정 5: AI 코드량 폭증과 개발자의 피로.** AI 활용으로 코드 양이 급증하여 개발자가 모든 코드를 따라가기 어려워 피로감이 증대됩니다. **처방: '그레이 박스 전략'.** 사람이 인터페이스를 직접 설계하고, AI에게 내부 구현을 통째로 위임하며, 사람은 인터페이스 단위로만 검증하는 방식입니다. 금융처럼 중요도가 높은 모듈은 예외이지만, 일반 비즈니스 로직에는 이 전략이 효과적입니다. 핵심은 "인터페이스를 설계하고, 구현은 위임하라" 입니다.

---

## 결론: AI 시대의 진정한 무기, '소프트웨어 펀더멘털'
포콕의 여섯 가지 함정과 처방은 모두 새로운 도구가 아닌, 프레그매틱 프로그래머, 도메인 주도 설계 등 20년 이상 된 소프트웨어 펀더멘털에 뿌리를 두고 있습니다. AI는 "현장의 병장", 즉 전술 단위의 코드 변경을 담당하는 역할을 합니다. 하지만 그 위에 "전략가", 즉 시스템 설계와 방향성을 제시하는 사람이 필요하며, 그 전략가의 무기는 시대 변화에 흔들리지 않는 굳건한 펀더멘털임을 강조합니다. '매일 시스템 설계에 투자하라'는 메시지는 AI 시대에도 변함없는 소프트웨어 개발의 핵심 가치임을 상기시킵니다.