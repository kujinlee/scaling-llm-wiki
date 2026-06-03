---
tags:
  - video-summary
  - ko
  - claude code
  - ai development
  - workflow automation
  - verification loop
  - developer tools
  - llm applications
  - best practices
video_id: "YQ_THFhjmdE"
channel: "김플립 - LLM 코딩"
lang: KO
type: Framework
audience: Advanced
score: 4.8
---

# Claude Code 창시자 Boris의 AI 에이전트 셋업. 전부 다 까보자!

**Channel:** 김플립 - LLM 코딩 | **Duration:** 18:13 | **URL:** https://www.youtube.com/watch?v=YQ_THFhjmdE

> [!summary] Quick Reference
> **TL;DR:** This video explains Boris's Claude Code setup, focusing on building AI agents that verify and improve their work through structured processes and safe automation practices.
>
> **Key Takeaways:**
> - Build an AI verification loop where agents test, debug, and refine their own output.
> - Define clear project rules and forbidden actions for your AI using a concise `Claude.md` file.
> - Implement a "plan first" workflow and granular permissions for safe and controlled AI automation.
> - Use powerful AI models and external tools to orchestrate complex tasks, reducing overall errors.
> - Gradually expand AI automation, focusing on manageability, starting with basic tasks and verification.
>
> **Concepts:** claude code · ai development · workflow automation · verification loop · developer tools · llm applications · best practices

---

## 1. AI 작업 검증 루프 구축의 핵심
AI에게 단순히 작업을 지시하는 것을 넘어, 작업 결과물의 검증 과정(테스트 코드 작성 및 실행, 오류 분석 및 수정)까지 맡겨야 합니다. 이는 클로드를 단순한 코드 생성기가 아닌, 스스로 작업을 확인하고 개선하는 에이전트로 만듭니다. 사람에게 일을 맡길 때처럼 검토 기준을 함께 제공하는 것이 중요합니다.

---

## 2. Claude MD를 활용한 AI 온보딩 및 제어
`Claude.md` 파일은 AI에게 프로젝트의 업무 매뉴얼 역할을 합니다. 프로젝트 구조, 기술 스택, 코드 스타일, 금지 사항 등을 명시하여 AI가 팀 방식에 맞게 일하도록 돕습니다. 특히 AI가 해서는 안 되는 작업을 명확히 지정하여 잠재적 문제를 방지하는 것이 중요합니다(예: 마이그레이션 파일 무단 수정 금지). `Claude.md`는 핵심적인 내용만 간결하게 작성하여 AI가 쉽게 참고할 수 있도록 해야 합니다(약 2,500 토큰 권장).

---

## 3. 안전한 자동화를 위한 권한 관리 및 계획 우선 원칙
클로드에게 너무 많은 자유 권한을 부여하는 위험한 자동 실행 모드는 피해야 합니다. 대신, 특정 명령어는 허용하고, 일부는 승인을 요청하며, 위험한 명령어는 금지하는 세분화된 권한 관리가 필요합니다. 작업을 바로 실행하기보다는 먼저 클로드가 작업 계획을 세우게 하고, 이를 검토 및 수정하는 '계획 우선' 워크플로우를 따릅니다. 이는 실제 개발 과정과 유사하며, 좋은 실행은 좋은 계획에서 나온다는 원칙을 따릅니다. 린터와 포매터를 자동화 파이프라인에 포함하여 AI가 놓칠 수 있는 작은 스타일 및 포맷 문제를 사전에 방지하고 코드 안정성을 높입니다.

---

## 4. 효율적인 업무 확장을 위한 도구 활용 및 모델 선택
클로드 코드는 단순한 코딩 도구를 넘어, 슬랙, 깃허브 등 다양한 외부 도구와 연동하여 복잡한 업무 흐름을 조율하는 '오케스트레이터' 역할을 할 수 있습니다. 이를 통해 코드 작성 외에 에러 분석, 이슈 생성, 문서 업데이트 등 다양한 업무를 자동화할 수 있습니다. 대규모 작업을 처리할 때는 여러 클로드 세션을 병렬로 사용하여 마치 여러 명의 주니어 개발자가 분담하는 것처럼 업무를 나눌 수 있습니다. 이때 각 세션의 역할과 검증 기준을 명확히 하는 것이 중요합니다. '오푸스'와 같은 강력한 모델은 비록 느리더라도 실수를 줄여 전체 작업 시간을 단축하고 재작업 비용을 줄이는 데 효과적입니다. 복잡한 작업일수록 느려도 덜 헤매는 모델을 선택하는 것이 좋습니다. 반복적인 작업은 슬래시 커맨드로 만들어 생산성을 높이고, 서브 에이전트는 꼭 필요한, 관점이 다른 검토 작업에만 단순하게 활용하여 관리 복잡성을 줄입니다.

---

## Conclusion
클로드 코드를 효과적으로 사용하기 위한 핵심은 AI에게 단순히 작업을 지시하는 것이 아니라, AI 스스로 작업을 확인하고, 오류를 고치며, 다시 검증할 수 있는 환경과 구조를 만들어 주는 것입니다. 보리스의 워크플로우를 무작정 따라 하기보다는, `Claude.md`를 간결하게 만들고, 계획 우선 원칙을 적용하며, 테스트와 린트를 활용하고, 권한을 세심하게 관리하는 등 자신의 상황에 맞춰 점진적으로 자동화의 범위를 확장해 나가는 것이 중요합니다. 궁극적으로 클로드 코드의 활용은 '관리 가능한 자동화'를 목표로 해야 합니다.