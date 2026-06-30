---
tags:
  - video-summary
  - ko
  - rag
  - graph-rag
  - knowledge-graph
  - langchain
  - neo4j
  - llm
  - ai-agent
video_id: "yWyJKCZG990"
channel: "Bloom AI"
lang: KO
type: Tutorial
audience: Intermediate
score: 4.2
---

# 단 30분 만에 이해하는 GraphRAG (with 랭체인, Neo4j)

**Channel:** Bloom AI | **Duration:** 35:05 | **URL:** https://www.youtube.com/watch?v=yWyJKCZG990

> [!summary] Quick Reference
> **TL;DR:** This video explains Graph RAG as an advanced solution to traditional RAG's limitations, demonstrating how to build and query knowledge graphs with Neo4j and LangChain.
>
> **Key Takeaways:**
> - Recognize traditional RAG's limitations, like context loss from chunking or top-K retrieval.
> - Understand knowledge graphs consist of nodes, edges, and properties for meaningful data representation.
> - Leverage Graph RAG to improve retrieval accuracy and scalability for complex, interconnected data.
> - Utilize LangChain and Neo4j to practically implement and query a knowledge graph-based RAG system.
> - Consider Graph RAG as a complementary approach to vector database-based RAG for enhanced performance.
>
> **Concepts:** rag · graph-rag · knowledge-graph · langchain · neo4j · llm · ai-agent

---

## 1. 기존 RAG 시스템의 한계점
RAG(Retrieval-Augmented Generation)는 사용자 질문에 가장 유사한 문서를 검색하고, 이를 질문과 함께 LLM에 전달하여 답변을 생성하는 방식입니다. 데이터 로드, 분할(청킹), 임베딩, 저장(벡터 DB)의 4단계로 시스템이 구축됩니다. 하지만 이 과정에서 다음과 같은 명확한 한계가 존재합니다.
*   **청킹(Chunking) 과정에서의 문맥 단절:** 문서를 일정한 크기로 나누는 과정에서 중요한 문맥 정보가 여러 청크에 분산되어, 잘못된 답변을 생성할 수 있습니다. (예: VIP 고객 수수료 면제 정책에서 해외 송금 예외 조항 누락)
*   **Top-K 검색의 한계:** LLM에 제공할 컨텍스트로 상위 K개의 문서만 검색할 경우, 중요한 연결 고리나 관계 정보가 Top-K에 포함되지 않아 답변의 정확도가 떨어질 수 있습니다. (예: 김민수와 보안팀의 관계를 설명하는 중간 문맥 누락)
이러한 한계는 RAG 시스템의 성능 저하로 이어집니다.
---
## 2. 그래프 RAG의 등장 배경 및 중요성
기존 RAG의 한계를 보완하기 위해 리랭크(Re-rank), 하이브리드 RAG, 에이전틱 RAG 등 다양한 RAG 디자인 패턴이 등장했습니다. 그중에서도 **그래프 RAG**는 “지식 그래프(Knowledge Graph)”를 구축하여 엔티티 간의 관계를 바탕으로 검색하는 시스템으로 각광받고 있습니다.
*   **높은 벤치마크 점수:** 그래프 RAG는 기존의 단순 RAG 시스템보다 더 높은 성능을 보입니다.
*   **시장 성장 전망:** 2024년 11억 달러 규모에서 2030년까지 69억 달러로 성장할 것으로 예측되며, 지식 그래프는 기술 하이프 사이클에서 실질적인 성장 단계에 진입했다고 평가됩니다.
*   **실제 적용 사례:** 미래에셋 증권은 AWS 서밋 서울 2026에서 금융 상품 에이전트에 그래프 RAG를 적용하여 사용자의 검색 경험을 개선한 사례를 발표했습니다. 팔란티어의 온톨로지(Ontology)도 데이터 간의 의미 있는 연결을 위해 지식 그래프를 활용합니다.
---
## 3. 지식 그래프(Knowledge Graph)란 무엇인가?
지식 그래프는 AI 에이전트가 데이터를 탐색할 수 있도록 노드(Node), 엣지(Edge), 속성(Property)의 세 가지 요소로 구성된 개념 지도입니다.
*   **노드(Node):** 일반적으로 명사에 해당하며, 사람, 장소, 개념, 객체 등 독립적인 개체를 나타냅니다. (예: 김민수, 결제 시스템 리팩토링)
*   **엣지(Edge):** 노드 간의 관계를 정의하며, 보통 동사에 해당합니다. (예: 김민수는 ‘담당한다’ 결제 시스템 리팩토링)
*   **속성(Property):** 노드나 엣지에 대한 상세 정보(메타데이터)를 담습니다. (예: 김민수의 나이, 프로젝트 진행 상태)
데이터를 이러한 그래프 형태로 구축함으로써, 에이전트는 복잡한 관계망 속에서 필요한 정보를 효과적으로 탐색하고 맥락을 이해할 수 있습니다. 예를 들어, “김민수와 보안팀의 관계” 질문에 대해 노드를 따라가며 연결된 관계를 파악하여 정확한 답변을 도출합니다.
---
## 4. 지식 그래프의 실제 활용 사례 및 장점
지식 그래프는 이미 다양한 서비스에서 활용되고 있습니다.
*   **구글 지식 그래프:** 2012년부터 구글 검색 결과에서 에펠탑이나 크리스토퍼 놀란과 같은 검색어에 대한 관련 정보를 한눈에 요약하여 보여주는 것이 대표적인 예시입니다. 이는 미리 구축된 지식 그래프를 통해 해당 엔티티와 관련된 노드 및 관계를 빠르게 검색하여 시각화한 것입니다.
*   **방대한 데이터 처리 속도:** 지식 그래프는 데이터 규모가 증가하더라도 검색 지연 시간이 크게 증가하지 않아, 방대한 데이터 환경에서 기존 RAG 대비 훨씬 빠른 검색 속도를 제공합니다.
*   **높은 성능:** 나이브한 RAG 시스템에 비해 더 정확하고 풍부한 답변을 생성할 수 있습니다.
따라서 지식 그래프 기반의 그래프 RAG는 방대한 데이터 속에서 정보를 빠르고 정확하게 찾아내어 LLM의 답변 품질을 향상시키는 데 효과적인 솔루션입니다.
---
## 5. 그래프 RAG 시스템 구축 (feat. Neo4j & LangChain)
그래프 RAG 시스템 구축을 위해서는 지식 그래프를 저장할 **그래프 데이터베이스(Graph DB)**가 필요합니다. 대표적인 그래프 DB로는 Neo4j, Amazon Neptune, OntoText GraphDB, TigerGraph 등이 있으며, 영상에서는 LangChain과의 연동이 용이한 **Neo4j**를 활용한 실습을 진행합니다.
*   **실습 개요:** 주어진 텍스트 문서(“김민수는 결제 시스템 리팩토링을 담당했고…”)를 지식 그래프로 구축한 후, “김민수와 보안팀은 어떤 관계야?”라는 질문에 대해 그래프 검색을 통해 정확한 답변을 생성하는 과정을 시연합니다.
*   **구축 과정:**
    1.  Neo4j 데스크톱 앱 설치 및 연결 테스트.
    2.  LangChain(`langchain-openai`, `langchain-neo4j` 패키지)을 사용하여 LLM이 텍스트에서 노드와 관계를 자동으로 추출하여 지식 그래프를 생성합니다. (Cypher 쿼리를 통해 Neo4j 앱에서 그래프 시각화 확인)
    3.  구축된 그래프를 기반으로 사용자 질문(`langchain`을 통해)이 들어오면, LLM이 Cypher 쿼리를 생성하여 그래프를 조회하고, 조회된 컨텍스트를 바탕으로 최종 답변을 생성합니다.
이 실습을 통해 복잡한 관계를 가진 데이터에서 LLM이 추론하기 어려운 질문에 대해서도 그래프 RAG가 효과적으로 컨텍스트를 제공하여 정확한 답변을 도출할 수 있음을 보여줍니다.
---
## Conclusion
그래프 RAG는 기존 RAG 시스템의 고질적인 한계, 특히 문맥 단절과 관계 정보 누락 문제를 해결하는 강력한 대안입니다. 지식 그래프를 활용하여 데이터 내의 엔티티와 그 관계를 명확히 정의함으로써, LLM이 더 정확하고 풍부한 컨텍스트를 기반으로 답변을 생성할 수 있도록 돕습니다. Neo4j와 LangChain 같은 도구를 사용하여 지식 그래프를 손쉽게 구축하고 활용할 수 있으며, 방대한 데이터를 빠르게 검색하고 복잡한 질문에 대해 추론 능력을 향상시키는 데 필수적인 기술입니다. 벡터 DB 기반 RAG와 상호 보완적으로 활용하여 최적의 검색 증강 생성 시스템을 구축하는 것이 중요합니다.