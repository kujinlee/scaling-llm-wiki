---
tags:
  - video-summary
  - ko
  - ai
  - llm
  - moe
  - memory tiering
  - ssd
  - macbook pro
  - on-device ai
  - cohere
  - hardware acceleration
video_id: "YVScoEeSNvs"
channel: "안될공학 - IT 테크 신기술"
lang: KO
type: Analysis
audience: Advanced
score: 4.8
---

# 맥북에서 초거대 4000억 AI 돌려봤습니다... 속도도 빠르다?  Flash-MoE 분석 || 메모리는 더욱 중요해질겁니다

**Channel:** 안될공학 - IT 테크 신기술 | **Duration:** 16:54 | **URL:** https://www.youtube.com/watch?v=YVScoEeSNvs

> [!summary] Quick Reference
> **TL;DR:** This video explains how a MacBook Pro runs a 400-billion parameter AI model by efficiently leveraging SSD and MOE architecture, highlighting memory tiering's future importance.
>
> **Key Takeaways:**
> - Understand MOE architectures enable running large LLMs on limited local hardware.
> - Recognize SSDs are becoming critical for AI model storage beyond just checkpoints.
> - Appreciate how OS-level optimizations like page cache enhance AI performance.
> - Grasp that memory tiering is crucial for optimizing AI inference systems.
> - Consider the evolving role of memory companies in the AI hardware ecosystem.
>
> **Concepts:** ai · llm · moe · memory tiering · ssd · macbook pro · on-device ai · cohere · hardware acceleration

---

## 1. M5 Max 맥북 프로에서 4천억 파라미터 AI 구동
최신형 M5 Max 맥북 프로(64GB DRAM)에서 3,970억(약 4천억) 파라미터의 초대형 AI 모델인 Cohere 3.5를 구동하는 혁신적인 사례를 소개합니다. 이는 기존의 상식을 뛰어넘는 성능으로, SSD를 활용하여 전체 모델을 상주시키지 않고 필요한 부분만 불러오는 방식으로 구현되었습니다.

---

## 2. MOE(Mixture of Experts) 아키텍처의 핵심 역할
해당 모델은 MOE(Mixture of Experts) 아키텍처를 채택하여, 전체 4천억 파라미터 중 실제 활성화되는 파라미터는 170억 개에 불과합니다. 이는 레이어 통과 시 필요한 소수의 '전문가'(Experts)만 선택적으로 불러와 계산하기 때문에 가능한 속도입니다. 덕분에 전체 모델을 DRAM에 올리지 않아도 빠르게 토큰을 생성할 수 있습니다.

---

## 3. SSD를 활용한 모델 웨이트 로딩 방식
기존 AI 시스템에서는 SSD가 학습 체크포인트 저장 등 보조적인 역할에 그쳤습니다. 그러나 이 사례에서는 SSD가 209GB에 달하는 전체 모델 웨이트를 저장하고, MOE 아키텍처에 맞춰 필요한 엑스퍼트들을 실시간으로 DRAM으로 불러와 연산에 활용합니다. 이는 SSD가 AI 인퍼런스 시스템의 핵심적인 메모리 계층으로 확장될 가능성을 보여줍니다.

---

## 4. 애플 맥 시스템의 최적화된 하드웨어 및 소프트웨어
이러한 성능은 단순한 MOE 모델뿐 아니라, 애플 맥 시스템의 고유한 최적화 덕분입니다. 빠른 로컬 SSD, CPU와 GPU가 공유하는 유니파이드 메모리(Unified Memory), 그리고 macOS의 페이지 캐시(Page Cache) 기능이 결합되어 SSD와 DRAM 간의 데이터 이동을 효율적으로 처리합니다. 커널 단의 심도 깊은 최적화도 주효했습니다.

---

## 5. AI 시대의 메모리 계층화(Memory Tiering) 전략
이 시연은 HBM과 DRAM뿐만 아니라 SSD와 같은 플래시 메모리도 AI 컴퓨팅에서 중요한 역할을 하게 될 것임을 시사합니다. AI 모델이 점점 커지면서 느리지만 용량이 큰 스토리지를 활용하는 메모리 계층화 전략이 필수적이 되고 있으며, 이는 국내 메모리 반도체 업계에도 큰 기회가 될 것입니다.

---

## Conclusion
이번 M5 Max 맥북 프로에서의 4천억 파라미터 AI 구동 사례는 MOE 아키텍처와 SSD를 효율적으로 활용하는 메모리 계층화 전략이 온디바이스 AI 및 데이터센터 환경에서 초대형 LLM을 구동하는 새로운 가능성을 열었음을 보여줍니다. SSD가 단순한 저장 장치를 넘어 AI 연산의 핵심 공급원으로 진화하며, 하드웨어와 소프트웨어 최적화의 중요성이 더욱 부각될 것입니다.