---
tags:
  - video-summary
  - ko
  - qualcomm
  - hbc
  - ai반도체
  - 메모리월
  - 데이터센터
  - 엔비디아
  - 한국메모리
video_id: "t9c7kEktM3Q"
channel: "안될공학 - IT 테크 신기술"
lang: KO
type: Analysis
audience: Intermediate
score: 5
---

# 새로운 AI 메모리 등장… 퀄컴의 무서운 AI 서버 진격 | HBM 아닌 HBC의 정체와 삼성 SK하이닉스의 기회

**Channel:** 안될공학 - IT 테크 신기술 | **Duration:** 38:52 | **URL:** https://www.youtube.com/watch?v=t9c7kEktM3Q

> [!summary] Quick Reference
> **TL;DR:** This video analyzes Qualcomm's DragonFly platform, its HBC memory technology, and strategic entry into the AI data center market, challenging Nvidia's dominance.
>
> **Key Takeaways:**
> - Qualcomm aims for AI data center efficiency, not just raw power, through its DragonFly platform.
> - HBC reduces data transfer by integrating compute near memory, a different approach than HBM.
> - The AI chip market is diversifying, with specialized hardware for different inference tasks.
> - Korean memory companies are crucial due to their advanced packaging and PIM/PNM expertise.
> - Software platforms like Modular are key to breaking existing hardware ecosystems like NVIDIA's CUDA.
>
> **Concepts:** qualcomm · hbc · ai반도체 · 메모리월 · 데이터센터 · 엔비디아 · 한국메모리

---

## 1. 퀄컴의 AI 데이터 센터 시장 진출과 드래곤플라이 전략
▶ [0:12–4:29](https://www.youtube.com/watch?v=t9c7kEktM3Q&t=12s)
퀄컴은 6월 24일 인베스터 데이에서 '드래곤플라이'라는 이름으로 AI 데이터 센터 시장에 공식 출사표를 던졌습니다. 드래곤플라이는 효율적인 비행을 하는 잠자리처럼, 엔비디아의 힘 위주 전략 대신 효율성으로 승부하겠다는 퀄컴의 메시지를 담고 있습니다. 퀄컴은 AI 계산 가속기(MPU), 칩을 연결하는 네트워크, 그리고 서버용 CPU를 포함한 데이터 센터 서버 전체 부품 세트를 선보였는데, 이는 엔비디아가 이미 GPU뿐 아니라 CPU, 네트워크, 소프트웨어까지 묶어 파는 시장 상황에 대응하기 위한 전략입니다. 퀄컴은 2029년 비(非)핸드셋 매출 목표를 400억 달러로 상향하며 스마트폰 의존에서 벗어나 데이터 센터에서 활로를 찾겠다는 강력한 의지를 보였습니다.

---

## 2. AI 추론의 메모리 병목 현상과 HBM의 한계
▶ [4:29–10:46](https://www.youtube.com/watch?v=t9c7kEktM3Q&t=269s)
AI가 텍스트를 생성하는 과정은 크게 '프리필(질문 이해)'과 '디코드(답 생성)' 두 단계로 나뉩니다. 특히 디코드 단계에서는 토큰 하나를 만들 때마다 수백 GB에 달하는 모델의 가중치와 점점 커지는 KB 캐시를 메모리에서 반복적으로 읽어와야 합니다. 이는 계산 능력은 급증하는 반면 메모리 속도가 따라가지 못해 발생하는 전형적인 '데이터 병목' 현상, 즉 '메모리 월' 문제입니다. 이 병목을 해결하기 위해 HBM(High Bandwidth Memory)이 등장했지만, 이는 데이터를 더 빨리 옮기는 '길을 넓히는' 방식이었고, 비싸고 만들기도 까다로운 한계가 있었습니다. 메모리 월 현상으로 인해 AI 칩은 이제 계산 속도가 아닌 데이터 접근 속도가 중요한 병목이 되었습니다.

---

## 3. 퀄컴의 HBC: 데이터 이동량 감소를 통한 해법
▶ [10:46–17:53](https://www.youtube.com/watch?v=t9c7kEktM3Q&t=646s)
퀄컴은 메모리 월 문제를 해결하기 위해 'HBC(High-Bandwidth Compute)'라는 새로운 접근 방식을 제안했습니다. HBC는 메모리 다이 위에 연산 다이를 적층하여, 계산기를 메모리 바로 옆(near memory computing)에 배치하는 3D 적층 구조입니다. 이는 데이터가 메모리와 GPU 사이를 왕복하며 발생하는 지연을 줄이기 위해, 가벼운 계산은 메모리 근처에서 바로 처리하여 '옮길 데이터를 줄이는' 방식입니다. HBM이 '길을 넓히는' 방식이라면, HBC는 '통행량 자체를 줄이는' 방식으로 접근합니다. 퀄컴은 HBC 1세대 기반의 AI 250 가속기 카드가 유효 대역폭 초당 133TB를 달성하여 이전 세대 대비 18배 향상되었다고 주장하지만, 이는 실제 물리적 대역폭이 아닌 '유효 대역폭'으로 계산된 값임을 명심해야 합니다.

---

## 4. HBC, Groq LPU, 삼성 PIM/PNM 비교
▶ [17:53–21:46](https://www.youtube.com/watch?v=t9c7kEktM3Q&t=1073s)
AI 추론 병목 해결에 대한 접근 방식은 다양합니다. 그록(Groq)의 LPU(Language Processing Unit)는 S램을 사용하여 압도적인 속도와 일정한 응답 속도를 강조합니다. 반면 퀄컴의 HBC는 디램을 선택하여 S램의 높은 비용과 작은 용량 한계를 극복하고, 데이터 이동 감소를 통해 용량과 효율성을 동시에 확보합니다. 삼성전자 또한 메모리 내에서 직접 연산을 수행하는 '핌(PIM: Processing In Memory)'과 메모리 곁에서 연산하는 'PNM(Processor Near Memory)' 기술을 수년 전부터 연구해왔습니다. 퀄컴의 HBC는 삼성의 PNM과 유사하게 메모리 다이 위에 연산 다이를 쌓는 구조로, 데이터 병목을 해결하려는 동일한 방향성을 공유하지만 구현 방식은 퀄컴의 독자적인 구조입니다.

---

## 5. 퀄컴 드래곤플라이 플랫폼의 전체 그림 (CPU 및 소프트웨어)
▶ [21:46–32:19](https://www.youtube.com/watch?v=t9c7kEktM3Q&t=1306s)
퀄컴 드래곤플라이는 HBC 외에도 서버용 CPU 'C1000'과 소프트웨어 전략이 핵심입니다. C1000은 루비아(Nuvia) 인수를 통해 얻은 '오라이언(Oryon)' 코어를 기반으로, 스마트폰 분야에서 축적된 저전력 기술을 활용해 전력 대비 성능이 두 배 향상된 점을 내세웁니다. 이 CPU는 최신 연결 규격을 지원하여 AI 가속기들에게 일감을 나눠주는 관제탑 역할을 수행합니다. 또한 퀄컴은 AI 소프트웨어 회사 모듈러(Modular)를 39억 달러에 인수하여, 하드웨어 종류에 상관없이 AI 모델을 유연하게 구동할 수 있는 소프트웨어 생태계를 구축하고 엔비디아의 CUDA에 정면 도전하겠다는 의지를 보였습니다. 메타, 마이크로소프트, 바이트댄스와 같은 주요 고객사를 확보하여 플랫폼 확장의 기반을 다졌습니다.

---

## 6. 한국 메모리 기업의 역할 및 AI 메모리 시장의 변화
▶ [32:19–36:12](https://www.youtube.com/watch?v=t9c7kEktM3Q&t=1939s)
HBC와 같은 기술은 디램 제조뿐 아니라 칩을 정밀하게 쌓고 연결하는 첨단 패키징(예: SK하이닉스의 HBM 기술)과 메모리 내 연산 노하우(예: 삼성전자의 PIM/PNM)가 필수적입니다. 이처럼 HBC가 요구하는 기술 역량은 한국 메모리 기업의 강점과 정확히 일치하며, AI 시대에 메모리 주도권이 한국으로 기울 수 있는 구조적 이유를 제공합니다. 또한, 메모리 기업의 역할은 단순 부품 공급사에서 고객과 함께 설계하는 '코디자인 파트너'로 위상이 격상될 것입니다. AI 메모리 시장은 대규모 학습에는 HBM-GPU 조합, 낮은 지연 시간과 효율이 중요한 추론(디코드)에는 S램, HBC, PIM 같은 구조들이 경쟁하는 다각화된 형태로 진화하고 있습니다.

---

## Conclusion
▶ [36:12–38:47](https://www.youtube.com/watch?v=t9c7kEktM3Q&t=2172s)
퀄컴의 드래곤플라이 플랫폼은 아직 검증될 미래의 약속이지만, AI 시장이 학습 중심에서 추론 및 에이전트 중심으로 변화하면서 GPU 단독 구조가 아닌, 프리필에는 GPU, 빠른 디코드에는 S램, 대용량 디코드에는 HBC/PIM 등 AI 시스템이 세분화될 것임을 시사합니다. 미래 AI 반도체 경쟁은 가장 빠른 칩 하나가 아닌, 다양한 구성 요소를 최적으로 배치하여 최소 전력으로 최대 토큰을 생성하는 싸움이 될 것입니다. 퀄컴의 전략이 엔비디아의 독점을 흔들 새로운 기회가 될지 주목됩니다.