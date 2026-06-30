---
tags:
  - video-summary
  - ko
  - ai agents
  - e2e testing
  - playwright
  - harness engineering
  - automated testing
  - software development
  - developer productivity
video_id: "wo0Rsh9hlTo"
channel: "NAVER D2"
lang: KO
type: Analysis
audience: Intermediate
score: 4.6
---

# AI 에이전트를 위한 Playwright E2E 테스트 하네스 구축하기

**Channel:** NAVER D2 | **Duration:** 32:11 | **URL:** https://www.youtube.com/watch?v=wo0Rsh9hlTo

> [!summary] Quick Reference
> **TL;DR:** This video explains how to build a Playwright E2E test harness for AI agents to enable self-correction, ensuring high-quality, verified code in the fast-paced AI
>
> **Key Takeaways:**
> - Design AI agent "self-correction loops" using E2E tests as both specifications and verifiers.
> - Implement a robust harness (docs, utils, context) to guide AI agents in test generation and repair.
> - Prioritize critical user flows for E2E testing to maximize impact in complex systems.
> - Adopt Playwright's best practices like API-based state setup and semantic selectors to prevent flaky tests.
> - Leverage AI agents (e.g., Playwright's Planner, Generator, Healer) to automate test creation and maintenance.
>
> **Concepts:** ai agents · e2e testing · playwright · harness engineering · automated testing · software development · developer productivity

---

## 1. AI 에이전트 시대, 검증의 중요성 부각
▶ [2:29–4:17](https://www.youtube.com/watch?v=wo0Rsh9hlTo&t=149s)
AI 에이전트의 도입으로 코딩 속도는 1.5배가량 빨라졌으나, 이로 인해 코드 검증이 병목 현상을 일으키고 있습니다. 모델은 스스로 작성한 코드에 대해 관대한 경향이 있어, 보리스 체르니가 언급했듯이 에이전트에게 스스로 작업을 검증할 수단을 제공하는 것이 중요해졌습니다. 이는 AI 시대에 모델의 작업 오류가 대부분 컴포넌트 경계 결함에서 발생하기 때문이며, 자동화된 검증 수단 없이는 이러한 문제를 찾아내기 어렵습니다.

---

## 2. E2E 테스트의 필요성 및 Playwright의 장점
▶ [4:17–10:08](https://www.youtube.com/watch?v=wo0Rsh9hlTo&t=257s)
기존의 단위 테스트만으로는 미들웨어, 서버사이드 프롭스, 컴포넌트 간의 복합적인 상호작용 문제를 잡아내기 어렵습니다. 켄트 시 다즈의 테스팅 트로피 개념에서 가장 높은 확신을 주는 엔드투엔드(E2E) 테스트의 중요성이 부각됩니다. 과거에는 비용과 느린 실행 속도로 인해 개발자가 꺼렸던 E2E 테스트가 AI 에이전트 시대에는 오히려 그 작성 부담이 줄어들고 시스템 검증의 중요도가 높아졌습니다. 발표 팀은 Playwright를 E2E 테스트 도구로 선택했는데, 이는 실제 브라우저 환경에서 사용자 경험을 검증하며, 테스트 코드가 사용자 명세(스펙 문서) 역할을 겸하고, 실패 시 풍부한 리포트(스크린샷, 비디오, 액션, 돔 스냅샷, 로그 등)를 제공하여 AI 에이전트가 문제 원인을 분석하고 수정하는 데 필요한 양질의 데이터를 제공하기 때문입니다.

---

## 3. Playwright E2E 테스트 구축 및 AI 에이전트 활용
▶ [10:08–16:41](https://www.youtube.com/watch?v=wo0Rsh9hlTo&t=608s)
네이버 파이낸셜의 6년차 Next.js 엔터프라이즈 코드베이스(17만 줄, 220개 페이지)와 같이 복잡하고 빠르게 변하는 환경에서는 모든 것을 테스트하는 것이 비현실적입니다. 이에 발표 팀은 매출 저해, 데이터 손실, 신뢰도 하락과 직결되는 '핵심 사용자 워크플로우(Critical User Flow)'를 우선적으로 선정하여 테스트를 구축했습니다. 초기 테스트 코드 작성은 Playwright의 공식 도구인 CodeGen으로 자동 생성된 러프한 코드에서 시작하며, AI 에이전트가 이를 팀의 컨벤션에 맞춰 구조화하고 다듬는 작업을 수행합니다. 더 나아가 마이크로소프트의 Playwright Agent 시스템(Planner, Generator, Healer)을 활용하여 테스트 계획 수립, 코드 작성, 그리고 실패한 테스트 자동 수정까지 AI 에이전트가 담당하는 워크플로우를 구축했습니다.

---

## 4. 효과적인 E2E 테스트 관리를 위한 전략
▶ [16:41–23:02](https://www.youtube.com/watch?v=wo0Rsh9hlTo&t=1001s)
구축된 E2E 테스트를 안정적으로 운영하기 위한 세 가지 핵심 전략이 제시됩니다. 첫째, '테스트 독립성'을 위해 각 테스트 시나리오의 시작점에서 API 호출을 통해 미리 사용자 상태를 세팅함으로써 공통 구간의 반복을 줄이고 실패 시 원인 파악을 용이하게 합니다. 둘째, '외부 의존성 Mocking'을 통해 네이버 인증서, 홈택스 등 외부 서비스 호출을 Playwright의 `page.route()`나 환경 변수를 이용한 고정 응답 반환으로 대체하여 테스트의 속도와 안정성을 확보합니다. 셋째, '간헐적 실패(Flaky Test) 예방'을 위해 `await for timeout`과 같은 하드 대기 대신 조건 기반 대기를 사용하고, CSS 클래스명 대신 역할(role)이나 이름(name) 같은 시맨틱 셀렉터를 활용하며, 작성 직후 `burn-in` 테스트(여러 번 반복 실행)를 통해 플래키 테스트를 조기에 발견하고 수정합니다.

---

## 5. AI 에이전트의 자가 개선 루프와 인간의 역할
▶ [23:02–31:06](https://www.youtube.com/watch?v=wo0Rsh9hlTo&t=1382s)
힐러 에이전트는 Playwright에서 생성되는 트레이스 파일(테스트 실행의 모든 기록)과 관련 CLI/스킬을 활용하여 실패한 테스트를 진단하고 수정하는 역할을 수행합니다. 이를 통해 에이전트가 작업을 푸시하고 CI에서 E2E 테스트가 실패하면, 에이전트가 피드백을 받아 스스로 디버깅하고 테스트를 고쳐 다시 PR을 올리는 '자가 개선 루프'가 완성됩니다. 이 루프는 '가이드(방향 제시)'와 '센서(관찰 후 교정)'라는 두 가지 핵심 부품으로 구성되며, Playwright E2E 테스트는 명세로서의 가이드와 검증 도구로서의 센서 역할을 동시에 수행합니다. 엔트로픽의 Evaluator-Optimizer 패턴에서 LM 평가자 대신 결정론적이고 빠르며 저렴한 Playwright를 대체재로 사용합니다. 이러한 자가 개선 루프의 설계, 에이전트에게 필요한 도구와 맥락 제공, 그리고 모델의 진화에 맞춰 하네스를 지속적으로 발전시키는 것이 AI 에이전트 시대에 인간 개발자의 핵심 역할인 '하네스 엔지니어링'임을 강조합니다.

---

## Conclusion
▶ [31:06–32:12](https://www.youtube.com/watch?v=wo0Rsh9hlTo&t=1866s)
AI 에이전트 시대에 테스트 코드는 실행 가능한 센서인 동시에 에이전트에게 지침을 주는 명세 문서의 역할을 겸합니다. 이러한 테스트 코드를 기반으로 에이전트가 스스로 코드를 작성하고 개선하는 자가 개선 루프를 구축할 수 있으며, 이 루프가 잘 작동하도록 환경을 설계하고 진화시키는 '하네스 엔지니어링'이 사람의 중요한 역할입니다. 올바른 행동을 쉽게 할 수 있도록 에이전트를 위한 환경을 만드는 것이 핵심입니다.