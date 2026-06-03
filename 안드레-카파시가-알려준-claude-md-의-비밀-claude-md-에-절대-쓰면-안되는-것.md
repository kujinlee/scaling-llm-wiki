---
tags:
  - video-summary
  - ko
  - claude.md
  - ai 코딩
  - 프롬프트 엔지니어링
  - 하네스 엔지니어링
  - anthropic
  - 워크플로우 최적화
  - 개발 생산성
video_id: "IyOgsIFUUcY"
channel: "실밸개발자"
lang: KO
type: Tutorial
audience: Advanced
score: 4.6
---

# 안드레 카파시가 알려준 CLAUDE.md 의 비밀: CLAUDE.md 에 절대 쓰면 안되는 것

**Channel:** 실밸개발자 | **Duration:** 25:09 | **URL:** https://www.youtube.com/watch?v=IyOgsIFUUcY

> [!summary] Quick Reference
> **TL;DR:** This video explains how to write effective Claude.md files, treating them as AI guardrails to prevent errors, not human READMEs.
>
> **Key Takeaways:**
> - Claude.md guides AI, preventing repeated errors; it's not a human-readable document.
> - Focus Claude.md on project `gotchas` and hidden rules, not code-inferable details.
> - Keep Claude.md concise (<100 lines), structured, and update it immediately after AI errors.
> - Include build, test, and lint commands to optimize AI workflow and token use.
>
> **Concepts:** claude.md · ai 코딩 · 프롬프트 엔지니어링 · 하네스 엔지니어링 · anthropic · 워크플로우 최적화 · 개발 생산성

---

## 1. Claude.md의 핵심 이해: 가드레일로서의 역할
Claude.md는 사람이 읽는 README가 아니라, Claude AI가 같은 실수를 반복하지 않도록 만드는 "가드레일"이자 "인스트럭션"입니다. 이 차이를 이해하는 것이 중요하며, 이는 더 짧고 정확하며 결과 품질이 좋은 Claude.md를 작성하는 기반이 됩니다. Claude.md는 끊임없이 성장하는 살아있는 문서로, AI가 실수를 할 때마다 업데이트하며 채워나가야 합니다.

---

## 2. Claude.md 파일의 구조와 컨텍스트 계층
Claude.md 파일은 전역(개인 설정), 팀 공유(공통 규칙), 로컬(임시 메모), 서브 디렉토리(패키지별 규칙)의 네 가지 위치에 존재하며, 이들은 매 요청마다 자동으로 합쳐져 Claude에게 전달됩니다. Claude AI는 시스템 프롬프트, 도구 정의, 전역 Claude.md, 프로젝트 Claude.md, 로컬 Claude.md, 서브 디렉토리 Claude.md, 대화 히스토리, 현재 사용자 메시지 등 총 8개의 컨텍스트 레이어를 읽습니다. 이 레이어들은 위에서 아래로 갈수록 더 구체적이고 우선순위가 높으며, 충돌 시 하위 레이어의 지침이 우선 적용됩니다.

---

## 3. 좋은 Claude.md 작성 원칙 및 핵심 습관
좋은 Claude.md의 첫 번째 원칙은 "코드로 알 수 있는 내용은 절대 쓰지 않는 것"입니다. 대신 코드만으로는 알 수 없는 프로젝트의 함정, 숨겨진 규칙, 자주 발생하는 실수(`gotcha`)에 집중해야 합니다. Anthropic이 권장하는 작성 원칙은 다음과 같습니다:
1.  **구체적**: 추상적인 지시 대신 어떤 것을 해야 하고 어떤 것을 하지 말아야 하는지 구체적인 규칙을 명시합니다.
2.  **구조화된 마크다운**: 가독성을 위해 헤딩, 리스트 등을 활용하여 스캔하기 쉽게 만듭니다.
3.  **정기적 검토**: 한 달에 한 번 또는 몇 주에 한 번씩 검토하여 사용하지 않는 규칙은 잘라내고 새로운 실수는 반영합니다.
4.  **간결함**: 100줄 이하를 권장하며, 필요한 경우 서브 디렉토리 Claude.md를 활용하여 분할 관리합니다.

---

## 4. Claude.md 최적화를 위한 실용적인 팁
Claude.md를 최적화하는 가장 높은 ROI(투자 대비 효율)를 가진 습관은 Claude가 실수를 했을 때 즉시 "이 실수를 다시 하지 않도록 Claude.md에 반영해 줘"라고 지시하는 것입니다. 또한, 빌드, 테스트, 린트 명령어를 Claude.md에 명시하면 Claude가 명령어를 추측하는 데 드는 시간과 토큰 비용을 절약하여 효율적인 워크플로우를 구축할 수 있습니다. Claude.md의 길이가 80~100줄에 가까워지기 시작하면 코딩 컨벤션과 같이 특정 주제를 별도 파일로 분리하고 Claude.md에서 참조하는 방식으로 관리하는 것이 좋습니다. Codex와 같은 다른 AI 에이전트와 함께 사용할 경우, agent.md 파일을 Claude.md 내에서 참조하도록 설정할 수 있습니다.

----- 

## 5. Claude.md 관리를 위한 강력한 도구 활용
Claude.md의 효율적인 관리를 위해 두 가지 강력한 도구를 활용할 수 있습니다.
*   **Andrej Karpathy의 Claude.md 스킬**: Karpathy가 평소 코딩할 때 사용하는 워크플로우나 컨벤션(코드 리뷰 방법, 디버깅 순서, 변수 네이밍 규칙 등)을 정리한 스킬입니다. 이는 특정 프로젝트 규칙이 아닌 범용적인 지침이므로 전역 Claude.md에 복사하여 모든 프로젝트에 일관되게 적용하는 것을 권장합니다.
*   **Anthropic의 공식 플러그인 ("Claude.md Management")**: 이 플러그인은 두 가지 주요 기능을 제공합니다.
    *   `revise_claude_md`: 현재 세션에서 Claude가 저지른 실수나 유용한 학습 내용을 바탕으로 Claude.md를 자동으로 업데이트하여 실수가 반복되지 않도록 돕습니다.
    *   `claude_md_improver`: 프로젝트 내 모든 Claude.md 파일의 품질을 분석하고 점수를 매기며, 개선이 필요한 이슈를 제안하고 공식 가이드에 맞춰 리팩토링까지 지원합니다. 
이러한 자동화 도구를 활용하면 Claude.md를 훨씬 빠르고 정확하게 개선하고 관리할 수 있습니다.

---

## Conclusion
Claude.md는 Harness Engineering의 핵심입니다. AI에게 프로젝트를 소개하는 문서가 아니라, AI가 실수를 하지 않도록 가드레일을 치는 도구임을 명심해야 합니다. 처음부터 완벽하게 작성하려 하기보다는 작게 시작하여 실수가 발생할 때마다 채워나가는 '살아있는 문서'로 관리하는 것이 Claude.md를 가장 효과적으로 활용하는 방법입니다. 오늘 배운 체크리스트(100줄 이하 유지, 빌드/테스트/린트 명령어 명시, 코드로 알 수 있는 내용 제거, 구체적인 규칙, 정기적 점검, 즉각적인 실수 반영)를 통해 여러분의 Claude.md를 점검하고 개선해 보시기 바랍니다.