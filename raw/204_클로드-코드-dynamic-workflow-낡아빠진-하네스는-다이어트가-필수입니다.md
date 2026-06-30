---
tags:
  - video-summary
  - ko
  - claude code
  - dynamic workflow
  - ai agent
  - harness engineering
  - llm optimization
  - prompt engineering
  - coding agent
video_id: "fInMcawbKng"
channel: "개발동생"
lang: KO
type: Tutorial
audience: Advanced
score: 4.6
---

# 클로드 코드 Dynamic Workflow | 낡아빠진 하네스는 다이어트가 필수입니다...!

**Channel:** 개발동생 | **Duration:** 24:53 | **URL:** https://www.youtube.com/watch?v=fInMcawbKng

> [!summary] Quick Reference
> **TL;DR:** This video demonstrates how to use Claude Code's new Dynamic Workflow feature to audit and optimize existing coding agent harnesses for better performance.
>
> **Key Takeaways:**
> - Regularly audit your coding agent harnesses to identify outdated or redundant rules.
> - Utilize Claude Code's Dynamic Workflow to orchestrate multiple sub-agents for complex tasks like harness scanning.
> - Develop custom workflows to automate the 'dieting' and optimization of your agent's safety rules.
> - Save and reuse custom workflows to ensure consistent and periodic maintenance of agent configurations.
> - Recognize that agent harnesses are not static; continuously adapt them as LLM models evolve.
>
> **Concepts:** claude code · dynamic workflow · ai agent · harness engineering · llm optimization · prompt engineering · coding agent

---

## 1. 하네스 최적화의 필요성
---
최근 LLM 모델의 성능 향상과 코딩 에이전트(Claude Code, Codex, Cursor 등) 자체에 내장된 다양한 기능(파일 읽기, 코드 수정, 터미널 실행 등)으로 인해 기존에 우리가 수동으로 추가했던 하네스(안전 장치)들이 불필요해지거나 오히려 에이전트의 성능을 저해하는 요인이 되고 있습니다. 과거에는 에이전트가 지시를 잘 따르지 않아 강제적인 규칙이 필요했지만, 이제는 모델이 스스로 잘 수행하기 때문에 오래된 하네스는 중복 지시나 방해가 될 수 있습니다. 따라서 더 이상 하네스를 추가하는 것보다 불필요한 하네스를 덜어내는 '다이어트'에 집중해야 할 시점입니다.

## 2. 클로드 코드의 다이나믹 워크플로우 소개
---
이 영상은 클로드 코드에 새로 추가된 '다이나믹 워크플로우' 기능을 소개합니다. 이 기능은 자바스크립트를 사용하여 여러 개의 서브 에이전트를 한꺼번에 오케스트레이션(orchestration)하는 것으로, 복잡한 작업을 효율적으로 처리할 수 있게 해줍니다. 워크플로우는 백그라운드에서 동작하며, 메인 세션은 다른 작업을 진행할 수 있습니다. 워크플로우는 `울트라 코드` 키워드를 사용하거나, `워크플로우` 자연어 요청, 또는 `/` 명령어 형태로 호출할 수 있습니다. 에이전트에게 생각할 시간을 주는 `Effort` 레벨을 `Ultra Code`로 설정하여 모든 작업을 워크플로우로 진행하게 할 수도 있습니다.

## 3. 내장 워크플로우: 딥 리서치 활용
---
클로드 코드에는 `Deep Research`라는 기본 내장 워크플로우가 있습니다. 이 워크플로우는 검색, 출처 수집, 적대적 검증, 종합 리포트 생성 등 여러 단계를 멀티 에이전트 방식으로 병렬 처리합니다. 예를 들어, `클로드 코드 사용자들이 클로드.md, 스킬 훅을 어떻게 쓰는지 리서치 해 줘`와 같은 요청을 통해 딥 리서치 워크플로우를 실행하면, 백그라운드에서 수많은 서브 에이전트가 동시에 웹에서 정보를 찾아오고, 검증하고, 최종 보고서를 생성하여 메인 에이전트의 컨텍스트를 효율적으로 활용합니다. 이는 다이나믹 워크플로우의 강력한 기능을 보여주는 좋은 예시입니다.

## 4. 커스텀 워크플로우 제작: 하네스 감사 및 다이어트
---
영상에서는 레거시 하네스를 최적화하기 위한 두 가지 커스텀 워크플로우를 직접 만들어봅니다. 첫 번째는 `Harness Legacy Scan` 워크플로우로, 현재 하네스의 낡은 규칙, 중복 지식, 과도한 컨텍스트, 불필요한 훅 등을 다각도의 관점(인벤토리, 글로벌 컨텍스트, 스킬, 프로덕트 오버랩, 세이프티 퍼미션, 리팩터 에이전트)에서 감사하고 검증 리포트를 생성합니다. 두 번째는 `Harness Diet` 워크플로우로, `Harness Legacy Scan` 리포트를 기반으로 실제로 하네스를 압축, 이동, 삭제하는 등 최적화 작업을 수행합니다. 이 과정에서 여러 서브 에이전트가 병렬로 작동하며, 하이리스크 항목에 대한 적대적 검토 단계까지 포함하여 안정적인 개선을 목표로 합니다.

## 5. 워크플로우 저장 및 재사용
---
생성된 커스텀 워크플로우는 `S` 키를 눌러 저장할 수 있습니다. `클로드 워크플로우` 폴더 내에 자바스크립트 파일 형태로 저장되어 다음번에 클로드 코드를 재시작할 때 다시 사용할 수 있게 됩니다. 이렇게 저장된 워크플로우는 `/` 명령어를 통해 쉽게 호출할 수 있습니다. 영상을 통해 `Harness Legacy Scan`과 `Harness Diet` 워크플로우를 저장하고 재사용하는 방법을 시연하며, 이를 통해 하네스 관리의 효율성을 높일 수 있음을 보여줍니다. 최종적으로 `Harness Diet` 워크플로우를 통해 불필요한 스킬이 정리되고 컨텍스트가 줄어드는 개선 효과를 확인합니다.

## Conclusion
---
하네스는 한 번 만들고 끝나는 것이 아니라, LLM 모델과 코딩 에이전트 자체의 지속적인 발전과 함께 주기적으로 검토하고 갱신되어야 합니다. 클로드 코드의 다이나믹 워크플로우는 이러한 하네스 관리 및 최적화 작업을 자동화하고 효율적으로 수행할 수 있는 강력한 도구입니다. `Harness Legacy Scan`과 `Harness Diet` 워크플로우를 주기적으로 활용하여 불필요한 하네스를 제거하고, 에이전트의 성능을 최적화하는 것이 중요합니다. 이 두 워크플로우는 통합할 수도 있지만, 스캔 결과를 먼저 검토한 후 다이어트 워크플로우를 실행하는 것을 권장합니다. 공유된 프롬프트를 기반으로 자신만의 워크플로우를 개선하여 하네스를 지속적으로 관리하시길 바랍니다.