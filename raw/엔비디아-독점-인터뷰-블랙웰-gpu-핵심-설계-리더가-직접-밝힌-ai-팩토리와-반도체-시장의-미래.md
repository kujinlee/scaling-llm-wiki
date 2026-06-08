---
tags:
  - video-summary
  - ko
  - nvidia
  - agentic ai
  - vera rubin
  - ai factory
  - gpu
  - data center
  - extreme codesign
video_id: "xO3wxkk-y6M"
channel: "안될공학 - IT 테크 신기술"
lang: KO
type: Interview
audience: Intermediate
score: 4.4
---

# 엔비디아 독점 인터뷰 | 블랙웰 GPU 핵심 설계 리더가 직접 밝힌 AI 팩토리와 반도체 시장의 미래

**Channel:** 안될공학 - IT 테크 신기술 | **Duration:** 19:42 | **URL:** https://www.youtube.com/watch?v=xO3wxkk-y6M

> [!summary] Quick Reference
> **TL;DR:** This video interviews an NVIDIA director about their strategy for the Agentic AI era, focusing on the Vera Rubin platform and holistic system design.
>
> **Key Takeaways:**
> - Optimize AI factory investments by prioritizing token cost, setup speed, and longevity.
> - Understand Agentic AI demands a complete shift in data center architecture, not just faster GPUs.
> - Recognize Vera CPU as a critical orchestrator for complex Agentic AI workloads.
> - Appreciate extreme codesign across GPU, CPU, and software for next-gen AI platforms.
> - NVIDIA's culture of transparency and in-house research drives rapid architectural innovation.
>
> **Concepts:** nvidia · agentic ai · vera rubin · ai factory · gpu · data center · extreme codesign

---

## 1. AI 팩토리와 토큰당 비용 최적화
과거에는 단순히 GPU의 속도에 주목했다면, 이제는 AI 팩토리 시대에 접어들며 고객들은 토큰당 생성 비용과 와트당 효율성 같은 상업적 가치를 중시합니다. 엔비디아는 토큰 비용 최소화, AI 팩토리 구축 속도 및 토큰 생산량 극대화, 그리고 소프트웨어 개선을 통한 AI 팩토리 수명 연장에 중점을 두어 고객의 수익성을 높이는 데 집중하고 있습니다.

---

## 2. 에이전트 AI 시대의 워크로드 변화
AI 기술은 단순 질의응답을 넘어 스스로 계획을 세우고 코드를 실행하는 에이전트 AI로 진화하고 있습니다. 이는 AI 연산 과정이 매우 길고 복잡한 워크플로우로 바뀐다는 것을 의미하며, 데이터 센터 내 GPU, CPU, 네트워크 간의 데이터 이동 방식 자체를 완전히 변화시켜야 합니다. 엔비디아는 전체 AI 팩토리 관점에서 병목 현상을 식별하고 해소하기 위해 멜라녹스 인수와 자체 CPU 개발 등 통합적인 접근 방식을 취합니다.

---

## 3. 에이전트 AI를 위한 베라(Vera) CPU의 역할
에이전트 AI는 복잡한 태스크 제어, 파이썬 코드 실행, 하드웨어 조율 등 CPU 측 연산 부담을 크게 증가시킵니다. 이에 엔비디아는 에이전트 AI 워크로드에 최적화된 새로운 프로세서인 베라(Vera) CPU를 선보였습니다. 베라 CPU는 높은 단일 스레드 성능, 대규모 메모리 대역폭, 확장 가능한 일관성 패브릭을 특징으로 하며, GPU에 데이터를 효율적으로 공급하고 워크플로우를 오케스트레이션하는 핵심 역할을 합니다.

----- 

## 4. 베라 루빈 플랫폼의 극단적인 공동 설계 (Extreme Co-design)
차세대 AI 플랫폼인 베라 루빈은 단순한 GPU 세대 교체가 아니라 GPU, CPU, 인터커넥트, 소프트웨어까지 시스템 전체를 하나의 거대한 컴퓨터처럼 동시에 설계하는 '극단적인 공동 설계'의 정점입니다. 엔비디아는 자체 AI 모델 연구팀을 통해 미래 워크로드의 요구사항과 병목 현상을 예측하고, 이를 해결하기 위해 전체 데이터 센터를 총체적으로 최적화하여 경쟁사 제품과 차별화된 압도적인 성능을 제공합니다.

---

## 5. 블랙웰에서 베라 루빈으로의 전환 및 인프라 연속성
엔비디아는 플랫폼의 하위 호환성을 항상 유지하며, 쿠다(CUDA)는 10년 이상 이를 보장해왔습니다. 블랙웰에서 베라 루빈으로 전환 시에도 NBL72 랙 아키텍처가 유지되어 고객은 기존 AI 팩토리를 크게 변경하지 않고도 원활하게 업그레이드할 수 있습니다. 또한, HBM은 계속해서 중요하며, 베라 CPU에 LPDDR과 내장 오류 정정 기능을 도입하여 비용 효율적이면서 엔터프라이즈급 메모리 솔루션을 제공합니다. 블루필드 4 SDX와 같은 가속 스토리지 인프라는 에이전트 AI의 긴 컨텍스트 추론을 위한 실시간 확장 메모리 역할을 합니다.

---

## 6. 엔비디아의 신속한 아키텍처 전환 문화
엔비디아는 AI 워크로드의 변화에 맞춰 시스템 아키텍처를 민첩하게 재구성합니다. 이는 개방적이고 투명한 사내 문화, 자체 파운데이션 모델을 개발하는 강력한 연구팀, 그리고 긴밀한 팀 간 협업 덕분입니다. 이러한 문화적 강점이 시장 변화에 빠르게 대응하고 로드맵을 유연하게 조정하여 최적의 AI 팩토리 솔루션을 제공하는 핵심 동력입니다.

---

## Conclusion
AI 시대에는 단순한 칩 성능을 넘어선 시스템 전체의 최적화가 중요하며, 엔비디아는 극단적인 공동 설계와 자체 모델 연구, 그리고 유연한 조직 문화를 통해 에이전트 AI의 복잡한 요구사항에 대응하고 있다.