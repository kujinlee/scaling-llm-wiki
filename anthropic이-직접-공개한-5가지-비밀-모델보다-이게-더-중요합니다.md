---
tags:
  - video-summary
  - ko
  - ai tools
  - code management
  - claude
  - large scale development
  - software engineering
  - productivity
  - organizational setup
video_id: "waVkNkguDNc"
channel: "메이커 에반 | Maker Evan"
lang: KO
type: Framework
audience: Beginner
score: 4.4
---

# Anthropic이 직접 공개한 5가지 비밀, 모델보다 이게 더 중요합니다

**Channel:** 메이커 에반 | Maker Evan | **Duration:** 8:36 | **URL:** https://www.youtube.com/watch?v=waVkNkguDNc

> [!summary] Quick Reference
> **TL;DR:** This video explains how to effectively integrate Anthropic's Claude Code into large organizations using specific tools and structured management practices.
>
> **Key Takeaways:**
> - AI integration requires a clear company manual (Claude.md) and specialized guides (Skills).
> - Package AI settings (Plugins) for easy sharing and reuse across departments.
> - Regularly review AI setups and assign a Directly Responsible Individual (DRI) for management.
> - Organize codebases and establish human review processes for AI-generated code.
>
> **Concepts:** ai tools · code management · claude · large scale development · software engineering · productivity · organizational setup

---

## 1. 대규모 코드베이스에서 AI 활용의 도전과 Claude Code의 접근 방식
수백만 줄의 코드를 다루는 대규모 조직에서 AI를 활용하는 것은 쉽지 않습니다. 기존 AI는 코드 전체를 미리 읽어 색인을 만드는 방식으로 작동하는데, 코드가 매일 수천, 수만 개씩 바뀌는 회사에서는 이 색인을 유지하는 것이 매우 어렵습니다. Claude Code는 이러한 색인 방식을 사용하지 않고, 마치 신입사원이 직접 사무실을 돌아다니며 일을 배우는 것처럼 필요한 정보에 그때그때 접근하는 방식으로 동작합니다. 이는 코드가 변경될 때마다 색인을 업데이트할 필요가 없다는 장점이 있지만, 회사 구조를 모르면 헤맬 수 있다는 단점도 있습니다.

---

## 2. Claude Code를 '스마트'하게 만드는 5가지 핵심 도구
엔트로픽은 Claude Code를 대규모 환경에서 효과적으로 활용하기 위한 5가지 도구를 제시합니다.
*   **Claude.md (회사 매뉴얼)**: AI가 회사의 규칙이나 업무 방식을 이해하는 데 필요한 매뉴얼입니다. 너무 두껍지 않게, 부서별로 작게 나누어 관리하는 것이 효율적입니다.
*   **Hooks (자동 센서)**: 특정 조건이 충족될 때 자동으로 작업을 수행하도록 설정하는 기능입니다. 예를 들어, AI 작업 완료 시 자동으로 검수 프로그램을 실행할 수 있습니다.
*   **Skills (부서별 전문 매뉴얼)**: 특정 전문 작업(예: 결산)을 수행할 때만 AI가 참고하는 맞춤형 가이드입니다. 필요할 때만 꺼내 보므로 AI의 인지 부하를 줄여줍니다.
*   **Plugins (설정 패키지)**: 매뉴얼, 센서, 가이드 등을 하나로 묶어 부서 간에 공유하고 재사용할 수 있도록 하는 패키지입니다. 좋은 설정이 특정 개인에게만 머무르지 않게 합니다.
*   **LSP (정밀 검색 시스템)**: 코드 내에서 특정 함수나 변수를 정확하게 찾아 AI가 시간을 낭비하지 않도록 돕는 시스템입니다. 마치 특정 부서의 특정 직원을 정확히 지목하는 것과 같습니다.

---

## 3. 성공적인 AI 도입을 위한 기업의 3가지 공통점
도구 외에, 성공적으로 AI를 도입한 회사들은 공통적으로 다음 세 가지를 실천했습니다.
*   **정기적인 점검**: 3~6개월마다 매뉴얼과 셋업을 점검하고 업데이트합니다. AI는 지속적으로 발전하므로, 구식 규칙이 AI의 잠재력을 저해하지 않도록 해야 합니다.
*   **책임자(DRI) 지정**: AI 셋업 및 운영에 대한 명확한 책임자(Directly Responsible Individual)를 지정하여, 개인의 노하우가 회사 전체로 확산되도록 합니다.
*   **새로운 직책 도입 (AI 운영 매니저)**: AI 도구를 회사의 모든 직원이 효율적으로 활용할 수 있도록 관리하고 지원하는 전문 직책을 신설합니다.

----- 

## 4. AI 도입 시작을 위한 5단계 가이드
엔트로픽은 AI 도구 도입을 위한 다음 단계를 추천합니다.
1.  **책임자 지정**: 누가 AI 도입을 주도하고 관리할지 명확히 정합니다.
2.  **Claude.md (회사 매뉴얼) 작성**: 완벽하지 않더라도 짧게 시작하여 점차 다듬어 나갑니다.
3.  **코드 정리**: AI가 코드를 잘 찾을 수 있도록 폴더 구조를 깔끔하게 하고 불필요한 파일을 제외합니다.
4.  **부서별 전문 가이드 및 패키지 공유**: 좋은 셋업이 한 명에게만 머무르지 않도록 공유 시스템을 만듭니다.
5.  **검수 절차 마련**: AI가 생성한 코드도 사람이 작성한 코드와 동일하게 검수받는 절차를 만듭니다.

---

## 결론
Claude Code는 대규모 코드베이스를 가진 회사에서도 효과적인 도구가 될 수 있지만, 단순히 사용하는 것을 넘어 체계적인 셋업과 관리가 필수적입니다. 5가지 핵심 도구(회사 매뉴얼, 자동 센서, 부서별 전문 가이드, 통째 셋업 패키지, 정밀 검색 시스템)를 구축하고, 정기적인 점검, 책임자 지정, 그리고 AI 운영 매니저와 같은 전담 조직을 두는 것이 성공의 핵심입니다. 이러한 노력이 뒷받침될 때, AI는 대규모 조직의 개발 효율성을 혁신적으로 높일 수 있습니다.