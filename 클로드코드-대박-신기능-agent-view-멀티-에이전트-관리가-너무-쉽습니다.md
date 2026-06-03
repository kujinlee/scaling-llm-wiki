---
tags:
  - video-summary
  - ko
  - claude code
  - agent view
  - multi-agent
  - anthropic
  - ai development
  - terminal management
  - slash goal
video_id: "MPWKZzP-bQs"
channel: "개발동생"
lang: KO
type: Tutorial
audience: Intermediate
score: 4.4
---

# 클로드코드 대박 신기능 Agent View | 멀티 에이전트 관리가 너무 쉽습니다

**Channel:** 개발동생 | **Duration:** 10:10 | **URL:** https://www.youtube.com/watch?v=MPWKZzP-bQs

> [!summary] Quick Reference
> **TL;DR:** This video introduces Claude Code's Agent View, a powerful new feature simplifying multi-agent management in a single terminal environment.
>
> **Key Takeaways:**
> - Use `claude agents` to launch Agent View for managing all active Claude sessions.
> - Integrate active Claude sessions into Agent View by typing `/bg` within the session.
> - Press `Space` on a session for a quick summary and direct prompt input.
> - Utilize `/goal` to set completion conditions, enabling agents to autonomously work until met.
> - Manage agent sessions across multiple directories using the `@` command in Agent View.
>
> **Concepts:** claude code · agent view · multi-agent · anthropic · ai development · terminal management · slash goal

---

## 1. 클로드 코드의 에이전트 뷰 소개

엔트로픽이 클로드 코드에 새로운 기능인 '에이전트 뷰(Agent View)'를 출시했습니다. 이 기능은 하나의 환경에서 여러 개의 에이전트를 효율적으로 관리하는 데 매우 유용합니다. 기존에 `tmux`와 같은 터미널 멀티플렉서를 사용하여 여러 에이전트를 병렬로 실행하는 것은 복잡했지만, 에이전트 뷰는 여러 터미널 탭을 띄우거나 세션 간의 컨텍스트 스위칭 없이도 다중 에이전트를 손쉽게 다룰 수 있도록 돕습니다. 현재는 리서치 프리뷰(Research Preview) 기능으로 제공됩니다.

---

## 2. 에이전트 뷰 기본 사용법

에이전트 뷰는 `claude agents` 명령어를 사용하여 실행합니다. 실행하면 하나의 터미널 창에 현재 활성화된 여러 에이전트 세션이 한 번에 표시됩니다. 방향키를 이용해 각 세션을 선택하고, 엔터를 눌러 특정 세션 내부로 진입할 수 있습니다. 다시 에이전트 뷰 화면으로 돌아가려면 뒤로 가는 방향키를 누르면 됩니다. 또한, 에이전트 뷰 화면 하단의 채팅창에 프롬프트를 입력하여 새로운 세션을 즉시 생성하고 작업을 시작할 수 있습니다.

---

## 3. 고급 세션 관리 및 기능

*   **세션 정렬**: `Ctrl + S` 단축키를 사용하여 디렉토리 단위로 세션을 정렬하여 볼 수 있습니다.
*   **외부 세션 추가**: 에이전트 뷰로 시작하지 않은 기존 클로드 세션을 에이전트 뷰로 가져오려면 해당 세션 내에서 `/bg` (백그라운드) 명령어를 입력합니다. 그러면 해당 세션이 백그라운드로 전환되며 에이전트 뷰에 표시됩니다.
*   **빠른 요약 및 응답**: 특정 세션에 포커스를 맞춘 상태에서 `Space` 키를 누르면 해당 세션의 요약본이 하단에 표시되며, 여기서 직접 빠르게 프롬프트를 입력하여 응답할 수 있습니다. 클로드 모델이 내부적으로 내용을 요약하여 보여줍니다.
*   **세션 종료**: 종료하고자 하는 세션을 선택한 후 `Ctrl + X`를 두 번 누르면 해당 세션이 종료됩니다.

---

## 4. 다중 디렉토리 및 세션 통합 관리

에이전트 뷰는 현재 열려 있는 디렉토리뿐만 아니라, 모든 코드 베이스 위치의 에이전트 세션을 한 화면에서 관리할 수 있습니다. 에이전트 뷰를 실행한 디렉토리가 아닌 다른 디렉토리에서 작업을 시작하려면, 채팅창에 `@` 명령어를 입력한 후 원하는 디렉토리를 선택하고 프롬프트를 작성하면 됩니다. 이 기능을 통해 여러 프로젝트 또는 디렉토리에서 실행되는 다양한 에이전트 세션을 한 곳에서 효율적으로 모니터링하고 제어할 수 있습니다.

---

## 5. 슬래시 골(Goal) 명령어 활용

에이전트 뷰와 함께 `/goal` 명령어 기능도 소개되었습니다. 이 기능은 에이전트에게 특정 완료 조건을 설정해 주면, 에이전트가 그 완료 조건이 달성될 때까지 사용자에게 제어권을 넘기지 않고 자율적으로 작업을 계속 수행하도록 합니다. 예를 들어, 특정 세션에 진입한 후 `/goal "현재 생성되어 있는 테스트가 모두 완료가 될 때까지 작업을 계속해서 진행해 줘."` 와 같이 프롬프트를 입력하면, 에이전트는 모든 테스트가 성공할 때까지 스스로 수정하고 작업을 이어갑니다. 이는 에이전트의 자율성을 극대화하여 복잡하고 반복적인 작업을 자동화하는 데 유용합니다.

---

## Conclusion

클로드 코드의 에이전트 뷰는 멀티 에이전트 환경에서 작업 효율성을 혁신적으로 향상시키는 강력한 도구입니다. `tmux`와 같은 기존 방식의 복잡성을 해소하고, 직관적인 UI를 통해 여러 에이전트 세션을 쉽게 관리할 수 있게 해줍니다. 특히 `/goal` 명령어 및 "딥 인터뷰" 스킬(이전 영상에서 소개)과 결합하면, 에이전트 부대를 구축하여 복잡한 프로젝트를 자동화하고 관리하는 데 있어 엄청난 시너지를 발휘할 수 있을 것으로 기대됩니다. 현재는 터미널 환경에서만 작동하는 리서치 프리뷰 기능입니다.