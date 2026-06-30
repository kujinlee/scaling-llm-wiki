---
tags:
  - video-summary
  - en
  - postgresql
  - database history
  - open source
  - relational model
  - extensibility
  - community governance
  - nosql
  - cloud computing
video_id: "_CB_Aa2ODeM"
channel: "Coding with Lewis"
lang: EN
type: Analysis
audience: Advanced
score: 4.8
---

# The Database That Should Be Dead but Runs the Internet

**Channel:** Coding with Lewis | **Duration:** 22:34 | **URL:** https://www.youtube.com/watch?v=_CB_Aa2ODeM

> [!summary] Quick Reference
> **TL;DR:** This video chronicles PostgreSQL's journey from academic theory to a critical open-source database, thriving through community effort and an extensible design despite market shifts.
>
> **Key Takeaways:**
> - Open-source projects can thrive through decentralized community effort, even without traditional corporate backing.
> - Prioritizing extensibility in software design enables long-term adaptability to unforeseen future demands.
> - A permissive licensing model can foster unexpected alliances with commercial entities, benefiting the core project.
> - Strong community governance and a culture of collaborative review are crucial for sustained project health.
> - Foundational software can be owned by 'nobody,' relying on continuous volunteer contribution for its evolution.
>
> **Concepts:** postgresql · database history · open source · relational model · extensibility · community governance · nosql · cloud computing

---

## 1. The Genesis of Relational Databases and Ingres
▶ [0:34–2:01](https://www.youtube.com/watch?v=_CB_Aa2ODeM&t=34s)
In 1970, Edgar F. Codd published a paper on the relational model, a mathematically precise way to organize data. After three years, two professors, Michael Stonebraker and Eugene Wong, implemented this theory with their project, Ingres. This successful implementation proved the relational database was the future of computing, quickly becoming an industry standard. Stonebraker commercialized Ingres, establishing a pattern of building a proof, commercializing it, and moving to the next idea.

---

## 2. Postgres: An Extensible Vision
▶ [2:01–4:36](https://www.youtube.com/watch?v=_CB_Aa2ODeM&t=121s)
By 1985, Stonebraker realized the limitations of traditional relational databases like Ingres, which were tailored for specific business data (payroll, inventory) and struggled with complex data types (molecular structures, maps). Recognizing the need for a more versatile solution, he launched Postgres (Post-Ingres), aiming to create a database capable of storing "everything." Funded by DARPA, the Army Research Office, and the National Science Foundation, Postgres was designed with extensibility, custom data types, and custom query operators as its core principles, prioritizing correctness over the then-dominant market demand for raw speed.

---

## 3. The Birth of a Volunteer Community
▶ [4:36–14:22](https://www.youtube.com/watch?v=_CB_Aa2ODeM&t=276s)
After Stonebraker commercialized Postgres as Illustra and left Berkeley for the second time, the open-source version of Postgres was left without a clear owner. Two PhD students, Andrew Yu and Jolly Chen, added SQL compatibility to Postgres, releasing "PostgreSQL 95" to make it accessible to the wider database community, then moved on. The project was then sustained by unexpected volunteers: Mark Fournier provided hosting, and Bruce Momjian started contributing patches. This mailing list-driven, volunteer-led development cycle eventually saw significant contributions like Tom Lane's work on the query optimizer and Vada Makeev's implementation of MVCC (Multi-Version Concurrency Control) from across the globe, establishing a relentless, around-the-clock development pace.

---

## 4. Navigating Market Shifts: NoSQL and Cloud Providers
▶ [14:22–18:02](https://www.youtube.com/watch?v=_CB_Aa2ODeM&t=862s)
PostgreSQL faced significant challenges from the rise of NoSQL databases in the late 2000s, which argued against the rigid relational model. Despite internal debate among maintainers, Postgres adapted by implementing native JSON support in version 9.2 (2012) and later JSONB (2014), offering the flexibility of a document database with relational guarantees. Following this, cloud providers began offering managed PostgreSQL services, monetizing the volunteers' work. Unlike other open-source projects that changed licenses, Postgres maintained its permissive license.

---

## 5. The Unconventional Success of Permissive Open Source
▶ [18:02–20:03](https://www.youtube.com/watch?v=_CB_Aa2ODeM&t=1082s)
PostgreSQL's decision to retain its permissive license led to an unexpected alliance: cloud providers and companies building on Postgres began hiring maintainers and funding development. This fragmented corporate sponsorship prevented any single entity from capturing the project, allowing it to maintain neutrality and resist corporate takeovers, a common fate for community projects. This decentralized model fostered innovation, exemplified by the PG vector extension for AI before the vector database boom. By 2023, Postgres surpassed MySQL as the most used database among professional developers, a testament to its enduring volunteer-driven, extensible design.

---

## Conclusion
▶ [20:03–22:19](https://www.youtube.com/watch?v=_CB_Aa2ODeM&t=1203s)
PostgreSQL's remarkable journey highlights the power of decentralized, volunteer-led open-source development. Michael Stonebraker, the project's founder, acknowledged that the greatest impact came from the dedicated volunteers who continued and robusted the codebase long after he moved on. The database, which underpins critical global infrastructure, is famously "owned by nobody," sustained by a continuous flow of contributions from individuals driven by personal need and a shared vision. The ongoing challenge is to ensure this volunteer spirit and community engagement persists for future generations in an increasingly abstracted software landscape.