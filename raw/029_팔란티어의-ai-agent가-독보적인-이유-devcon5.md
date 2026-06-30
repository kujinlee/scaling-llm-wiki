---
tags:
  - video-summary
  - ko
  - palantir
  - ontology
  - ai agents
  - enterprise ai
  - simulation
  - decision making
  - digital twin
video_id: "YbcCKCy1bd0"
channel: "빅데이터닥터 BIGDATA DOCTOR"
lang: KO
type: Case Study
audience: Intermediate
score: 4.4
---

# 팔란티어의 AI agent가 독보적인 이유(DevCon5)

**Channel:** 빅데이터닥터 BIGDATA DOCTOR | **Duration:** 13:24 | **URL:** https://www.youtube.com/watch?v=YbcCKCy1bd0

> [!summary] Quick Reference
> **TL;DR:** This video explains how Palantir's AI agents leverage ontologies and simulations to find true causality for enterprise-wide decision-making, improving efficiency and reducing risk.
>
> **Key Takeaways:**
> - Differentiate correlation from causation to avoid common decision-making errors in data analysis.
> - Leverage ontologies to model real-world relationships and uncover true causal knowledge within complex enterprise data.
> - Use simulation 'sandboxes' to test decision scenarios and refine hypotheses without impacting live operations.
> - AI agents, powered by ontologies, can optimize complex schedules and automate actions based on simulated outcomes.
> - Build a comprehensive 'digital twin' through interconnected ontologies for holistic, enterprise-wide decision-making.
>
> **Concepts:** palantir · ontology · ai agents · enterprise ai · simulation · decision making · digital twin

---

## 1. 상관관계와 인과관계의 혼동

많은 사람들이 데이터에서 단순한 연관성인 상관관계와 명확한 원인-결과 관계인 인과관계를 혼동합니다. 부자가 아침형 인간이거나 초콜릿 소비량과 노벨상 수상자 수의 상관관계가 인과관계가 아니듯이, 기업 내에서도 매출 증가를 광고 예산 확대 때문이라고 착각하거나, 특정 팀장 부임 후 성과 지표 개선을 그 팀장 때문이라고 오해하는 경우가 흔합니다. 이러한 혼동은 빠른 의사결정 요구, 경험 과대평가, 부서 이기주의, 평가 지표의 한계 등으로 인해 발생합니다.

---

## 2. 팔란티어 온톨로지를 활용한 시뮬레이션

팔란티어 플랫폼은 이러한 혼동을 해소하고 기업만의 진정한 인과 관계 지식을 찾기 위해 온톨로지를 활용합니다. 온톨로지는 기업의 복잡한 데이터를 연결하여 실제 세계의 관계를 표현합니다. 이를 바탕으로 '샌드박스'라는 가상 환경에서 시뮬레이션을 수행할 수 있습니다. 사용자는 가설을 세우고 시뮬레이션을 통해 그 결과를 확인하며, 가설과 일치하지 않으면 수정하여 반복함으로써 진짜 인과 관계를 찾아나갈 수 있습니다. 이는 실제 데이터에 영향을 주지 않으면서 다양한 시나리오를 미리 테스트해 볼 수 있게 합니다.

---

## 3. 응급 수술 스케줄링 시뮬레이션 사례

개발자 컨퍼런스에서 소개된 병원 응급 수술 스케줄링 사례는 팔란티어 온톨로지와 AI 에이전트의 활용법을 잘 보여줍니다. 긴급 심장 수술이 필요한 환자가 발생했을 때, 응급실 간호사는 음성 에이전트의 도움을 받습니다. 이미 환자, 의사, 간호사, 장비 스케줄 등이 온톨로지로 구축되어 있기 때문에, 에이전트는 기존 스케줄 변경, 간호사 초과 근무 등을 고려하여 최적의 수술 스케줄 대안 세 가지를 제시합니다. 간호사는 이 대안들을 샌드박스 환경에서 시뮬레이션하며 각 대안이 불러올 결과를 미리 확인합니다.

---

## 4. 시뮬레이션의 협업과 자동화

간호사가 최적의 대안을 선택하기 어려울 때는 에이전트에게 A안과 B안의 차이를 상세히 문의하고, 에이전트는 최상위 심장 전문의 배정 및 잦은 스케줄 조정이 필요한 A안과, 숙련된 전문의 배정 및 한 번의 조정만 필요한 B안을 비교하며 병원 전체 관점에서는 B안이 최선이라고 조언합니다. 간호사가 B안을 선택하려 할 때, 관리자와의 협업 과정을 거쳐 최종 결정을 내립니다. 최종 결정이 내려지면 에이전트는 즉시 변경된 스케줄을 관련 환자들에게 자동으로 전화하여 통보하는 행동까지 수행합니다. 또한, 사람마다 볼 수 있는 정보를 제어하여 데이터 거버넌스를 유지하며, 여러 사람이 동시에 시뮬레이션을 수정하고 협업할 수 있습니다.

---

## 5. 엔터프라이즈 온톨로지의 중요성

팔란티어는 병원의 모든 온톨로지(수술, 인력, 재무, 환자 경험 등)가 연결되어 병원 전체가 '디지털 트윈'으로 구축될 때 진정한 가치가 발생한다고 강조합니다. 온톨로지 연결을 통해 모든 직원은 자신의 결정이 병원 전체에 미치는 영향을 파악하고, 전사적인 관점에서 의사결정을 할 수 있게 됩니다. 이는 의사결정 속도와 품질을 향상시키고, 실행 리스크를 감소시키며, 숨겨진 병목 현상이나 가짜 인과 관계를 발견하여 조직 전체의 효율을 극대화합니다.

---

## 6. AI 에이전트 성공을 위한 온톨로지 우선

연결되지 않은 파편화된 시스템에서 AI 에이전트가 작동하면 추론 비용이 증가하고, 판단 근거의 진위 여부를 확인할 수 없습니다. 팔란티어는 엔터프라이즈 에이전트가 진정한 가치를 발휘하려면, 기업을 동적으로 연결하고 제대로 표현하는 온톨로지 시스템이 가장 우선시되어야 한다고 주장합니다. AI의 지능 자체보다 조직 전체가 하나의 공유된 운영 세계를 보고 유기적으로 움직이는 것이 더욱 중요하다는 것입니다. 가설-시뮬레이션-조정의 피드백 루프를 통해 조직 구조를 계속 조정해 나가는 과정이 엔터프라이즈 에이전트의 핵심이며, 이는 팔란티어 에이전트가 다른 경쟁사와 차별화되는 지점입니다.

---

## Conclusion

팔란티어는 온톨로지 시스템이 조직의 실제 세계를 정확하게 시뮬레이션할 수 있을 때 비로소 기업용 AI 에이전트가 가장 큰 가치를 발휘한다고 주장합니다. 이는 단순한 데이터 연관성을 넘어 실제 인과 관계를 파악하고, 전사적인 의사 결정 효율과 신뢰도를 높이며, 나아가 위기 상황에서 생사를 가르는 중요한 역량으로 작용할 수 있음을 보여줍니다. 결국 조직 전체가 공유하는 '하나의 운영 세계'를 구축하는 것이 팔란티어 AI 에이전트의 핵심 경쟁력이라고 할 수 있습니다.