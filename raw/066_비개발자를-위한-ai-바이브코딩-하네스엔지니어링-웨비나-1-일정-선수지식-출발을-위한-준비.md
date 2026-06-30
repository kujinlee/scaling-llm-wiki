---
tags:
  - video-summary
  - ko
  - harness engineering
  - terminal
  - docker
  - framework
  - library
  - rag
video_id: "t67mA2_D5FA"
channel: "우푸랩 (UpuLab)"
lang: KO
type: Tutorial
audience: Beginner
score: 4.6
---

# 비개발자를 위한 AI 바이브코딩, 하네스엔지니어링 웨비나 [1] : 일정, 선수지식, 출발을 위한 준비

**Channel:** 우푸랩 (UpuLab) | **Duration:** 3:21:32 | **URL:** https://www.youtube.com/watch?v=t67mA2_D5FA

> [!summary] Quick Reference
> **TL;DR:** This video provides a comprehensive introduction to AI engineering for non-developers, covering dev environments, modern tech stacks, Docker, and AI tools like RAG.
>
> **Key Takeaways:**
> - Master terminal commands and VS Code for efficient AI engineering development.
> - Use Docker for consistent development and deployment across different operating systems.
> - Select suitable frameworks (Next.js, FastAPI) and databases (PostgreSQL, Supabase) for your project.
> - Employ RAG to enhance LLM accuracy by enabling models to reference specific external data.
> - Integrate MCP, skills, libraries, and personas for optimal AI service development.
>
> **Concepts:** harness engineering · terminal · docker · framework · library · rag

---

## 1. AI 엔지니어링 입문 및 개발 환경 설정
본 웨비나는 강사의 갑작스러운 면접 일정으로 인해 시간이 단축되었음을 알리며 시작합니다. 하지만 알찬 내용으로 비개발자들도 AI 엔지니어링에 쉽게 접근할 수 있도록 돕습니다.

초반에는 Claude와 Figma를 연동하여 간단한 SNS 앱(우프그램)의 메인 및 로그인 화면을 디자인하는 시연을 통해 AI가 코딩 외에도 다양한 분야에서 활용될 수 있음을 보여줍니다. 이는 상세한 프롬프트와 디자인 기획이 AI 결과물의 품질에 얼마나 중요한지를 강조합니다.

이후 터미널의 기본 개념(컴퓨터의 본연의 모습)과 함께 `LS`, `CD`, `MKDIR`, `start .` (Windows), `open .` (Mac) 등의 필수 명령어를 실습하며 친숙해지는 시간을 가집니다. 이어서 Node.js가 JavaScript로 컴퓨터를 제어하는 방식과 설치 과정을 AI(Codex)를 활용하여 시연하고, `npm`을 통한 패키지 관리도 간략히 설명합니다.

개발 환경의 핵심 도구인 VS Code(통칭 '예쁜 메모장')의 설치와 사용법을 안내하며, VS Code 확장 프로그램(클로드, 코덱스 등)의 활용법을 소개합니다. 터미널을 VS Code 내에서 사용하는 효율적인 방법을 강조하며, 개발자가 여러 작업을 병렬로 처리하는 중요성을 역설합니다.

---

## 2. 도커: 일관되고 효율적인 개발 및 배포 환경
도커는 개발 환경의 OS 차이(Windows/Mac vs. Linux 서버)로 인해 발생하는 문제점을 해결하기 위해 탄생한 기술입니다. 개발자가 로컬 환경(Windows/Mac)에서 리눅스 기반의 가상 환경(컨테이너)을 구축하여 개발 및 테스트할 수 있게 함으로써, 배포 시 발생할 수 있는 오류를 최소화합니다.

주요 개념으로는 사용자의 PC를 지칭하는 '호스트', 호스트 내에서 독립적인 OS를 가질 수 있는 가상 환경인 '컨테이너', 컨테이너의 모든 설정과 코드를 담아 재사용할 수 있는 '이미지', 그리고 프로그램이 데이터를 주고받는 통로인 '포트'를 설명합니다. 이어서 AI를 활용해 간단한 'Hello Docker' 웹 서버를 도커 컨테이너에 띄우고, 호스트의 8000번 포트와 컨테이너의 7000번 포트를 연결하여 웹사이트에 접근하는 실습을 진행하며 도커의 원리를 보여줍니다. 이는 인프라 구축의 기본 개념이자, 개발된 애플리케이션의 일관된 배포를 가능하게 하는 핵심 기술임을 강조합니다.

---

## 3. 프레임워크, 라이브러리 및 최신 기술 스택
프레임워크는 소프트웨어 개발의 '뼈대'이자 '약속'으로, 특정 구조와 규칙을 제공하여 효율적인 유지보수를 가능하게 합니다. 반면 라이브러리는 특정 기능을 수행하는 '책'과 같아서, 프레임워크 내에서 필요에 따라 가져다 사용할 수 있는 도구들을 의미합니다.

**프론트엔드 추천 스택:**
*   **Next.js:** 웹 애플리케이션 개발에 적합하며, 핫 리로드 기능으로 개발 생산성을 높입니다.
*   **Flutter:** 모바일 앱 전용 개발에 최적화되어 있습니다.
*   **React Native:** 웹과 모바일 앱을 동시에 개발할 때 효율적이며, 배달의 민족과 같이 잦은 업데이트에도 사용자에게 인지되지 않는 자연스러운 UI 변경을 가능하게 합니다.

**백엔드 추천 스택:**
*   **FastAPI:** 파이썬 기반으로, 머신러닝/딥러닝 등 AI 기능을 백엔드에 통합할 때 유리합니다.
*   **Nest.js:** 안정성과 확장성을 갖춘 TypeScript 기반 프레임워크로, 일반적인 백엔드 서비스에 적합합니다.
*   **Serverless:** 백엔드 서버 없이 프론트엔드가 DB에 직접 연결되는 방식으로, 빠른 개발과 유지보수의 장점이 있습니다.

**데이터베이스 추천 스택:**
*   **PostgreSQL:** 현재 가장 강력하고 다재다능한 데이터베이스입니다.
*   **Supabase:** 서버리스 환경에 최적화된 데이터베이스로, 실시간 기능과 손쉬운 배포를 제공하며 PostgreSQL과 호환됩니다.

**소프트웨어 설계 팁:**
*   데이터 조회가 많은 서비스(예: 사람인)의 경우, Redis를 활용한 캐시(Cache) 기능을 설계하여 서버 부하를 줄일 수 있습니다.

---

## 4. AI 도구의 활용과 RAG의 이해
AI 엔지니어링에서 MCP(Meta-Contextual Protocol), 스킬(Skill), 라이브러리(Library)는 각각 다른 역할을 수행하며 시너지를 창출합니다.

*   **MCP:** 클로드와 피그마 연동 시연처럼, AI가 VS Code 프로젝트의 범위를 넘어 외부 애플리케이션을 제어하는 등 더 넓은 범위의 기능을 추가하고 제어하는 데 사용됩니다.
*   **스킬:** AI에 특정 기능을 부여하는 것으로, 더 세부적인 작업을 가능하게 합니다.
*   **라이브러리:** 프로젝트 자체에 필요한 기능을 추가하는 것으로, MCP나 스킬이 라이브러리를 활용하여 작업을 수행할 수 있습니다.

이러한 도구들을 단순히 개별적으로 활용하는 것을 넘어, 프레임워크, 라이브러리, 그리고 에이전트의 페르소나와 결합하여 최적의 결과물을 도출하는 것이 중요합니다.

**RAG(Retrieval Augmented Generation):**
대규모 언어 모델(LLM)의 할루시네이션(환각 현상) 문제를 해결하기 위한 기술입니다. LLM이 외부의 방대한 지식 대신, 특정 데이터베이스(예: 회사 취업 규칙)에서 관련 정보를 검색한 후 이를 기반으로 답변을 생성하게 하여 정확성과 실용성을 높입니다. 이는 AI가 원하는 정보를 참조하여 답변하도록 지시함으로써, 기존의 지식 기반으로는 얻기 힘든 맞춤형 고품질 답변을 가능하게 하는 핵심 기술입니다. 예를 들어, 아파트 건축 설계 데이터를 학습시켜 최적의 설계도를 제안하는 등 다양한 산업 분야에 적용될 수 있습니다.

---

## 결론
AI 엔지니어링은 프론트엔드, 백엔드, 데이터베이스, MCP, 스킬, 라이브러리, 그리고 에이전트 페르소나 등 다양한 요소들이 유기적으로 결합될 때 최고의 성능을 발휘합니다. "그냥 해 줘"라는 요청만으로는 원하는 결과를 얻기 어려우며, 각 기술 스택의 목적과 특성을 이해하고 상황에 맞춰 적절히 조합하는 '설계'의 과정이 매우 중요합니다. 이번 웨비나를 통해 비개발자들도 이러한 AI 엔지니어링의 기본 개념과 최신 기술 스택을 이해하고, 스스로 실용적인 AI 서비스를 구상하고 구축할 수 있는 첫걸음을 내딛기를 바랍니다.