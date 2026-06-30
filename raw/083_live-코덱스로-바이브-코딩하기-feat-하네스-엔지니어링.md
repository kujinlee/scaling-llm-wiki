---
tags:
  - video-summary
  - ko
  - youtube analytics
  - codex cli
  - ai coding
  - gpt 5.5
  - harness framework
  - llm development
  - automation
video_id: "GJQ0rNvTfPw"
channel: "실밸개발자"
lang: KO
type: Tutorial
audience: Intermediate
score: 4.4
---

# [LIVE] 코덱스로 바이브 코딩하기 (feat. 하네스 엔지니어링)

**Channel:** 실밸개발자 | **Duration:** 2:10:56 | **URL:** https://www.youtube.com/watch?v=GJQ0rNvTfPw

> [!summary] Quick Reference
> **TL;DR:** This video demonstrates using Codex CLI with Harness to develop a YouTube analysis app and Pomodoro timer, showcasing advanced AI coding features and emphasizing planning.
>
> **Key Takeaways:**
> - Prioritize planning (problem, architecture) for high-quality LLM-assisted coding.
> - Utilize Codex features (`fork`, `go`, `side`, `compact`) to maximize development productivity.
> - Codex, especially GPT 5.5, produces excellent code given clear instructions.
> - The Harness framework helps LLMs efficiently manage complex development tasks in phases.
>
> **Concepts:** youtube analytics · codex cli · ai coding · gpt 5.5 · harness framework · llm development · automation

---

## 1. 라이브 코딩 목표 및 Codex CLI 설정
이번 라이브 코딩 세션에서는 OpenAI와의 협업을 통해 Codex CLI를 활용하여 유튜브 채널 분석 앱을 개발하는 과정을 시연합니다. 세션 말미에는 참석자를 위한 Codex 무료 구독 이벤트가 준비되어 있습니다.

Codex CLI 사용에 앞서 최적의 개발 환경을 위한 설정 방법을 소개합니다. 권한 모드는 `auto-review`를 추천하지만, 시연을 위해 `full access`를 사용합니다. 모델은 최신 `GPT 5.5`를 추천하며, 추론 레벨(`reasoning level`)은 `Extra High`로 설정합니다. 또한, 터미널 하단에 `status line`을 커스터마이징하여 모델, 추론 레벨, 컨텍스트 사용량 등 중요한 정보를 실시간으로 확인할 수 있도록 합니다. 빠른 개발 속도를 위해 `fast mode` 사용도 권장하며, 이는 토큰 소모량이 두 배지만 Codex의 관대한 토큰 정책 덕분에 효율적이라고 설명합니다.

---

## 2. 유튜브 채널 분석 앱 기획
오늘 만들 앱은 유튜브 채널 URL을 입력하면 해당 채널의 데이터를 자동으로 분석하여 인사이트를 제공하는 도구입니다. 이 앱은 유튜브 API로 데이터를 수집하고, ChatGPT API로 분석을 수행할 것입니다.

개발 초기 단계에서 기획의 중요성을 강조하며, 이는 LLM과 함께 코딩할 때 가장 중요한 부분이라고 역설합니다. PRD(Product Requirements Document), 아키텍처 문서, ADR(Architectural Decision Record)을 활용하여 문제 정의, 사용자 흐름, 기술 스택(Next.js, TypeScript, TailwindCSS) 등을 상세하게 계획하는 과정을 보여줍니다. MVP(Minimum Viable Product)는 데이터베이스 없이 공개 유튜브 API만을 사용하여 빠른 구현에 중점을 둡니다. TDD(Test-Driven Development) 훅과 린트/빌드/테스트 훅을 추가하여 코드 품질을 강제하고 개발 프로세스를 체계화하는 방법도 소개됩니다.

---

## 3. Harness 프레임워크 및 Codex 고급 기능 활용
Harness 프레임워크는 복잡한 개발 작업을 작은 `phase` 단위로 나누어 LLM이 효율적으로 작업을 수행하도록 돕는 도구입니다. PRD, 아키텍처, ADR 문서를 기반으로 `phase` 폴더를 생성하고, 각 스텝의 진행 상황을 `index.json` 파일로 추적합니다. 이는 메인 컨텍스트를 보존하고 병렬 작업을 가능하게 합니다.

라이브 코딩 중에는 다음과 같은 Codex 고급 기능들이 시연됩니다:
*   **`fork`**: 현재 세션의 컨텍스트를 복제하여 기획 단계의 중요한 컨텍스트를 보존하고, 필요시 이전 상태로 돌아갈 수 있는 '보험' 역할을 합니다.
*   **`compact` & `clear`**: 컨텍스트 윈도우가 가득 찼을 때 컨텍스트를 압축하거나 완전히 초기화하여 효율적인 작업을 돕습니다. 컨텍스트 사용량은 20~30%를 유지하는 것이 좋습니다.
*   **`ImageGen`**: GPT-2 모델을 활용하여 유튜브 채널 관련 이미지를 생성하는 기능을 보여줍니다.
*   **`Go` (Slash Go) 스킬**: 명확한 시작, 중단, 검증 조건을 가진 장기 실행 목표를 설정하는 데 사용됩니다. 이를 통해 포모도로 타이머 앱을 프롬프트 한 줄로 자율적으로 개발하는 과정을 시연하며, 개발자가 개입하지 않아도 목표를 달성하는 Codex의 능력을 보여줍니다.
*   **`Side`**: 메인 세션의 컨텍스트에 영향을 주지 않으면서 별도의 서브 세션에서 질문이나 작업을 수행할 수 있습니다.
*   **`Computer Use` 스킬**: 브라우저를 직접 조작하여 웹 애플리케이션의 자동화된 테스트 및 상호작용을 수행하는 시연을 합니다. 이는 채널 URL 입력, 분석 시작 버튼 클릭 등을 포함합니다.

---

## 4. 라이브 데모: 유튜브 분석 앱 및 포모도로 타이머
Harness 프레임워크를 통해 개발된 유튜브 채널 분석 앱이 최종적으로 시연됩니다. 채널 URL을 입력하면 유튜브 API를 통해 영상 데이터를 수집하고, ChatGPT API를 통해 이 데이터를 분석하여 채널 진단 점수, 가장 강한 신호, 위험한 병목, 다음 영상 아이디어, 액션 리스트 등을 제공합니다. UI는 간단하지만 핵심 기능은 성공적으로 작동함을 보여줍니다.

`Go` 스킬로 개발된 포모도로 타이머 앱도 시연됩니다. 단 한 줄의 프롬프트로 시작, 일시정지, 재설정, 작업/휴식 모드, 키보드 단축키, 반응형 레이아웃 등을 갖춘 웹 기반 타이머가 자동으로 생성되는 것을 보여주며, Codex의 자율적인 개발 능력을 입증합니다.

---

## 5. 자동화 설정 시도 및 주요 교훈
라이브 세션 말미에는 개발된 분석 앱을 활용하여 매일 아침 유튜브 채널 리포트를 자동으로 받아볼 수 있도록 Codex 앱 내에서 자동화 스크립트를 설정하려는 시도가 있었습니다. 비록 포트 충돌 등의 문제로 인해 자동화 실행 자체는 성공하지 못했지만, 스크립트 생성 및 자동화 설정 개념을 소개하고 Codex 앱의 자동화 기능(`Automation`)에 대해 설명합니다.

**주요 교훈**:
*   LLM과의 코딩 시 기획 단계의 중요성: 문제 정의, 사용자 스토리, 아키텍처 설계에 충분한 시간을 할애하는 것이 구현 퀄리티를 높이는 핵심입니다.
*   Codex CLI 및 앱의 효율적인 사용법: `fork`, `compact`, `clear`, `go`, `side`, `computer use`와 같은 다양한 스킬 및 명령어를 활용하여 개발 생산성을 극대화할 수 있습니다.
*   Codex의 높은 코딩 능력: 명확한 지침이 주어졌을 때 뛰어난 코드를 생성하며, 특히 `GPT 5.5` 모델 이후 퀄리티가 크게 향상되었습니다.
*   Codex Harness의 가치: 모델 자체의 상향 평준화 시대에, 모델을 효율적으로 활용하는 Harness의 역할이 더욱 중요해지고 있으며, Codex CLI의 오픈소스 Harness는 학습 및 활용에 큰 이점을 제공합니다.

---

## 결론
이번 라이브 코딩 세션은 Codex CLI와 앱을 활용하여 실제 유용한 애플리케이션을 기획하고 개발하는 전반적인 과정을 생생하게 보여주었습니다. 특히 기획의 중요성, 다양한 Codex 기능 활용법, 그리고 강력한 AI 개발 도구로서의 Codex의 잠재력을 확인할 수 있었습니다. 시청자들과의 적극적인 소통과 함께 진행된 이번 세션은 LLM 기반 개발의 현재와 미래를 엿볼 수 있는 귀중한 시간이었습니다.